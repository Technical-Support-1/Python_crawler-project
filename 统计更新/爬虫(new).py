import requests
import time
import datetime
import ast
import tkinter as tk
import random
import sys     # 导入模块（其中requests需要自己下载）

now_time = datetime.datetime.now ().strftime ('%Y-%m-%d')   # 获取当前时间便有比较
test_for_uploaders = []     # 创建一个列表用来存储判断是否更新的数据

UID1 = 24892260
UID2 = 433394272
UID3 = 327595494
UID4 = 306887340
UID5 = 107609241   #指定UID 来统计（填数字即可）

"""
UID1 = input("UID:")
UID2 = input("UID:")
UID3 = input("UID:")
UID4 = input("UID:")
UID5 = input("UID:")
"""
# 如果不熟悉代码，可以直接把上面两组 三个（一共六个）双引号去掉，之后就可以直接输入了。

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36"}
# 指定伪装头（建议填自己的）

with open("更新统计1.txt","a",encoding="utf-8") as fp:
    fp.write("\n")
    fp.write("\n")    # 先空两行便于区分
    fp.write(str(datetime.datetime.now()) + "\n")   # 表明当前时间，为下面记录做准备

def get_main(x,act):
    if act == 0:   # 如果act = 0，那么就说明列表里没有这个UID号（也就是没更新），之后再检测
        x = str(x)    # 先将其变成字符串方便输出
        a = requests.get(headers=headers,url=F"https://api.bilibili.com/x/space/arc/search?mid={x}&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp")
        # 通过B站的API平台获取信息（最终是一个像字典的字符串）
        result = a.text  # 通过text属性获取文本
        user_dict = ast.literal_eval(result.replace('false','False'))    # 将字符串转化为字典（eval()函数有安全漏洞，因此使用ast.literal_eval()）
        c = user_dict["data"]["list"]["vlist"][0]["created"]  # 通过字典获取发布时间（时间戳）
        b = user_dict["data"]["list"]["vlist"][0]["title"]   # 通过字典获取视频标题（便于输出）
        d = user_dict["data"]["list"]["vlist"][0]["author"]   # 通过字典获取发布者名称（便于输出）
        test_new = 3
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
            test_for_uploaders.append(int(x))   # 如果已经更新，就存入UID号（说明此项已被检测）
            # 更新消息发出后，您无需做任何事
        time.sleep(random.uniform(0.5,5))  # 等待一段时间以避免IP反爬
        print(d,x,created_time)  # 输出UID，昵称和日期

while True:
    get_main(UID1,test_for_uploaders.count(UID1))
    # 利用count()函数检测目标UID出现的次数，如果为0就表示未被存入（还没更新），需要继续运行。反之则不运行（下同）
    get_main(UID2,test_for_uploaders.count(UID2))
    get_main(UID3,test_for_uploaders.count(UID3))
    get_main(UID4,test_for_uploaders.count(UID4))
    get_main(UID5,test_for_uploaders.count(UID5))   # 分别请求五个不同的UID号
