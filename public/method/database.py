import sqlite3
import time

# 查询表格是否存在判断是否继续进行探测
def searchTable(tableName,database):
    findInfo = database.cursor().execute(f'''PRAGMA table_info("{tableName}")''').fetchall()
    if findInfo != []:
        try:
            choose = ord(input(f"检测到存在{tableName}缓存表，是否使用缓存？(Y/N)").strip())
            if choose == 89 or choose == 121:
                # 使用缓存
                return -1
            elif choose == 78 or choose == 110:
                # 删除已经存在的数据表
                database.cursor().execute(f'''DROP TABLE "{tableName}"''')
                # database.commit()
                return 0
            else:
                print("抱歉，您输入不合法")
                exit()
        except:
            print('抱歉，您输入不合法')
            exit()
    else:
        return 0

def createTables(url):
    # 数据库默认命名规则
    localtime = time.localtime()
    year = localtime.tm_year
    mon = localtime.tm_mon
    day = localtime.tm_mday
    tableName = f"{year}{mon}{day}-{url}"

    conn = sqlite3.connect("save.db", check_same_thread=False)

    # 判断以前是否执行过
    # 0 - 重新开始或未执行
    # -1 - 采用缓存
    exist = searchTable(tableName,conn)
    if exist == 0:
        print("不使用缓存！")
    else:
        print("使用缓存！")

    conn.cursor().execute(f'''create table if not exists "{tableName}"
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    url text,
    status_code INTEGER,
    reapply INTEGER
    )''')
    conn.commit()
    return conn,tableName,exist

def selectSuccessInfo(database,tableName):
    cursor = database.cursor()
    crawl_data = cursor.execute(f'''select url, status_code from "{tableName}" where status_code < 400''').fetchall()
    return crawl_data

# 根据字典向数据库内存放数据
def saveData(url,database,tableName):
    database.cursor().execute(f"INSERT INTO '{tableName}' (url, status_code , reapply) VALUES (?, ?,?)",(url, 0, 0))
    database.commit()
    return -1

