from concurrent.futures import ThreadPoolExecutor,as_completed
import public.method.toolInit as toolInit
import public.method.loadDict as loadDict
import public.method.randomHeader as randomHeader
import public.method.sendHtpp as sendHttp
import public.method.database as database
from tqdm import tqdm
import time
import csv
import queue

if __name__ == "__main__":
    # 脚本工具初始化
    args = toolInit.getParserArgs()
    toolInit.getLogo()
    dictPath = args.D
    url = args.U
    threadNumber = args.T
    headers = args.H
    csvPath = args.O

    # 创建数据库
    conn, tableName, exist = database.createTables(url)

    # 加载字典
    q = queue.Queue()
    loadDict.getDict(dictPath,conn,exist,tableName,url,q)

    # 判断是否采用随机UA
    if headers == None:
        headers = randomHeader.setHeaders()

    # 数据陈列
    print(f"网站域名为:{url}\n采用的头部:{headers}\n字典路径:{dictPath}\n开启线程:{threadNumber}")

    # 创建线程池子
    pool = ThreadPoolExecutor(max_workers=threadNumber)
    futures = []

    # 敏感目录探测
    length = 0
    if exist:
        length = 6 * q.qsize()
    else:
        length = 65 * q.qsize()
    with tqdm(total=length,colour="yellow",position=0) as pbar:
        for i in range(q.qsize()):
            futures.append(pool.submit(sendHttp.sendRequest(q.get(), headers,conn,tableName)))
            for future in as_completed(futures):
                pbar.update()

    # 创建CSV文件
    csvName = "".join(str(time.time()).split('.'))
    pathFile = ""
    if csvPath != None:
        pathFile = f"{csvPath}\{csvName}"
    else:
        pathFile = csvName

    # 创建csv文件
    with open(f"{pathFile}.csv", "a+" , encoding="utf-8", newline="") as csvfile:
        name = ['id','url','status_code']
        csv_write = csv.writer(csvfile)
        csv_write.writerow(name)
        # 将结果导出为csv文件
        crawl_data = database.selectSuccessInfo(conn,tableName)
        number = 0
        for i in crawl_data:
            number = number + 1
            csv_write.writerow([number,i[0],i[1]])
        if csvPath == None:
            print(f"结果存放于当前目录下的{csvName}.csv")
        else:
            print(f"结果存放于{csvPath}\{csvName}.csv")
    conn.close()