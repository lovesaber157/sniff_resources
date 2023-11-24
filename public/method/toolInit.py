import argparse

def getParserArgs():
    parser = argparse.ArgumentParser(description="欢迎来到子域名爆破工具")
    parser.add_argument("-U",help="指定需要探测的网站完整URL，形如https://www.baidu.com",required=True)
    parser.add_argument("-D",help="指定需要使用的字典，默认为./public/dict/test.txt",default="./public/dict/top7k.txt")
    parser.add_argument('-H',help="指定headers",default=None)
    parser.add_argument('-T',help="开启线程数，默认为6",type=int,default=6)
    parser.add_argument('-P',help="开启经常数，默认为1",type=int,default=1)
    parser.add_argument('-O',help="输出的路径,默认为./",default=None)
    args = parser.parse_args()
    return args

def getLogo():
    logo = """              welcome this tools
                　☆  *　.  　☆
            　　. ∧＿∧　∩　* ☆
            *  ☆ ( ・∀・)/ .
            　.  ⊂　　 ノ* ☆
            ☆ * (つ ノ  .☆
            　　 (ノ
    """
    print(logo)
    return -1