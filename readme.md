### 敏感资源嗅探脚本
利用 python + sqlit3 + httpx 所写出的敏感资源嗅探脚本
支持中断请求后重新发送请求,支持请求完成将 响应码<400 结果以 时间戳.csv 的文件保存在本地。

#### 运行过程截图展示
![](https://github.com/lovesaber157/sniff_resources/blob/main/runing.PNG)
![](https://github.com/lovesaber157/sniff_resources/blob/main/runing01.PNG)
![](https://github.com/lovesaber157/sniff_resources/blob/main/runing03.PNG)

1. 运行脚本
   `
   python main.py [-h] -U U [-D D] [-H H] [-T T] [-O O]
   `
   参数解释 
   `
   options:
  -h, --help  show this help message and exit
  -U U        指定需要探测的网站完整URL，形如https://www.baidu.com
  -D D        指定需要使用的字典，默认为./public/dict/test.txt
  -H H        指定headers
  -T T        开启线程数，默认为10
  -O O        输出的路径,默认为./
   `

#### 文件结构
sniff_resource
-| main.py # 入口文件
---| public # 共有文件夹
------| database.py # 数据库模块
------| loadDict.py # 字典加载模块
------| randonHeader.py # 随机UA头模块
------| sendHttp.py # 探测请求发送模块
------| showMessage.py # 输出提示模块
------| toollinit.py # 脚本初始化加载模块
---| dict # 字典文件存放处
------| top7K.txt # 常用7K敏感资源字典

#### 等待改进
1. 等待解决字典加载初期CPU占用率过高问题
2. 等待解决多进程 + 多线程问题
3. 等待改进进度条对于加载字典越大误差越大的问题