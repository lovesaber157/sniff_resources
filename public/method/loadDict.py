def getDict(dictPath,database,exist,tableName,url,queue):
    if exist:
        # 读取缓存
        cacheItmes = database.cursor().execute(f"SELECT * FROM '{tableName}' WHERE status_code = 0 or reapply < 3 and status_code >= 400").fetchall()
        for item in cacheItmes:
            queue.put(item[1])
        print(f"加载缓存完成,待完成数量:{len(cacheItmes)}")
    else:
        with open(dictPath, "r", encoding="UTF-8") as fp:
            for line in fp:
                # 数据库初始化
                URL = f"{url}{line.strip()}"
                database.cursor().execute(f"INSERT INTO '{tableName}' (url, status_code , reapply) VALUES (?, ?,?)", (URL, 0, 0))
                database.commit()
                queue.put(URL)
        print(f"字典加载数量:{queue.qsize()}")
    return -1