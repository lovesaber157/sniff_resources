import httpx
import random
import time
import threading

def sendRequest(URL,headers,database,tableName):
    status_code = httpx.head(URL, headers=headers, verify=False).status_code
    reNumber = 0

    # 进行重放
    if(status_code >= 400):
        status_code,reNumber = reSendRequest(URL,headers,status_code)

    # 数据库数据存储
    lock = threading.Lock()
    lock.acquire()
    database.cursor().execute(f'''UPDATE "{tableName}" SET status_code = {status_code} , reapply = {reNumber} WHERE url = "{URL}"''')
    database.commit()
    lock.release()

    time.sleep(random.random())
    return -1

# 对于请求失败的重新发送请求以防网络波动等问题
def reSendRequest(url,headers,status_code):
    reNumber = 0
    timeout = 5
    while reNumber < 3:
        timeout = timeout + 1
        status_code = httpx.head(url, headers=headers, verify=False,timeout=timeout).status_code
        reNumber = reNumber + 1
    return status_code,reNumber

