import requests
import time
import datetime
import ast
import tkinter as tk
import random
import sys     # 导入模块（其中requests需要自己下载）

now_time = datetime.datetime.now ().strftime ('%Y-%m-%d')   # 获取当前时间便有比较

UID1 = 
UID2 = 
UID3 = 
UID4 = 
UID5 =    #指定UID 来统计（填数字即可）

"""
UID1 = input("UID:")
UID2 = input("UID:")
UID3 = input("UID:")
UID4 = input("UID:")
UID5 = input("UID:")
"""
# 如果不熟悉代码，可以直接把上面两组 三个（一共六个）双引号去掉，之后就可以直接输入了。

headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, lkie Gecko) Version/5.1 Safari/534.50"}
# 指定伪装头（建议填自己的）

with open("更新统计1.txt","a",encoding="utf-8") as fp:
    fp.write("\n")
    fp.write("\n")    # 先空两行便于区分
    fp.write(str(datetime.datetime.now()) + "\n")   # 表明当前时间，为下面记录做准备

def get_main(x):
    x = str(x)    # 先将其变成字符串方便输出
    a = requests.get(headers=headers,url=F"https://api.bilibili.com/x/space/arc/search?mid={x}&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp")
    # 通过B站的API平台获取信息（最终是一个像字典的字符串）
    result = a.text  # 通过text属性获取文本
    user_dict = ast.literal_eval(result.replace('false','False'))    # 将字符串转化为字典（eval()函数有安全漏洞，因此使用ast.literal_eval()）
    c = user_dict["data"]["list"]["vlist"][0]["created"]  # 通过字典获取发布时间（时间戳）
    b = user_dict["data"]["list"]["vlist"][0]["title"]   # 通过字典获取视频标题（便于输出）
    d = user_dict["data"]["list"]["vlist"][0]["author"]   # 通过字典获取发布者名称（便于输出）
    #转换成localtime
    time_local = time.localtime(c)
    #转换成新的时间格式
    created_time = time.strftime("%Y-%m-%d",time_local)   # 只取日期即可
    if now_time == created_time:    # 如当前日期与视频发布日期相同，则表示UP主更新
        print("更新了！")   # 先在控制台输出消息
        with open("更新统计1.txt","a",encoding="utf-8") as fp:
            fp.write(F"{x}（{d}）于 " + created_time + "更新！" + "  " + F"标题：{b}" + "\n")   # 输出谁于何时更新
        root = tk.Tk()  # 创建可视窗口
        w = tk.Label(root, text=F"UID:{x}（{d}）更新啦！\n标题：{b}")
        w.pack()   # 指定文字
        root.geometry("450x300")  # 指定大小
        root.mainloop()
        sys.exit()
        # 更新消息发出后，只需将UID号对应那一栏的函数（例如: get_main(UID3)）前加 # 号将其变为注释即可
    time.sleep(random.uniform(0.5,5))  # 等待一段时间以避免IP反爬
    print(d,x,created_time)  # 输出UID，昵称和日期

while True:
    get_main(UID1)
    get_main(UID2)
    get_main(UID3)
    get_main(UID4)
    get_main(UID5)   # 分别请求五个不同的UID号
