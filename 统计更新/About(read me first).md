# 关于

这是我们学习Python爬虫后的一个项目，请多多提出修改意见！

代码行数：69行（2021.6.22）

项目地址：Github地址: https://github.com/Technical-Support-1/Python_crawler-project/tree/main/%E7%BB%9F%E8%AE%A1%E6%9B%B4%E6%96%B0

国内Gitee地址：https://gitee.com/technical-support-1/Python_crawler-project/tree/main/%E7%BB%9F%E8%AE%A1%E6%9B%B4%E6%96%B0

# 使用指南

（完整版请见视频：https://www.bilibili.com/video/BV1Jg41137oq ）

这是一个可以帮你监测UP主是否更新的爬虫程序。

使用方法如下：

1、如果您对Python语法有一定的了解，您可以在以下字段内填充您想要的UID号：

`UID1 = `

`UID2 = `

`UID3 = `

`UID4 = `

`UID5 =    #指定UID 来统计（填数字即可）`

2、如果您不熟悉Python语法，那么请遵循以下的步骤：

    1、您可以在程序的第17行与第23行分别找到三个双引号，您可以将它们去掉后运行程序，之后您就可以在控制台输入UID了。
  
3、在控制台中，您看到的输出格式为 昵称+UID号+最近一个视频的发布时间

4、程序会在统计目录生成一个名称为"更新统计1.txt"的文件，其格式如下：
  
  
    【开始记录的时间】
    

    【BV号】【（昵称）】 于 【时间】更新！（如果有）

5、请使用Python3.6及以上版本运行

6、有问题请先自行解决，之后再去Issues中提问。（带上“更新统计”字样）

7、欢迎Fork此仓库并Pull Requests以完善此程序。

8、有问题发到邮箱(wikidot-cn@outlook.com)或在Issues中留言。（带上“更新统计”字样）

9、五个UID号必须全部填满！！！如果不需要这么多UID号，请在删除上面的语句后再删除下面的get_main()语句！（也可以在前面加 # 号设为注释）

10、如果您想要添加UID号，请在“UID5 = ”这一句后面加入如下语句：
    
    
    UID6 = 
    
    UID7 = 
接着，请在代码末尾（while True循环内）加入如下语句：

    get_main(UID6,test_for_uploaders.count(UID6))
    
    
    get_main(UID7,test_for_uploaders.count(UID7))


之后，您加入的UID号就会被检测。


11、当程序检测到UP主更新后，程序会生成一个可视化窗口以提醒您UP主已经更新。此时，您只需要关闭弹窗即可。程序将继续运行并停止监测已经更新的UP主。


12、如何查看headers?

打开您的谷歌浏览器，打开任意界面（推荐https://www.bilibili.com ），右击空白处，点“检查”，点击上方选项卡里的Network，之后按Ctrl+R刷新界面，点击主数据包（一般是最上面的那个），点击中间选项卡中的headers，拉到最下方，有一个"User_Agent"值，右击，点击"Copy value"，之后填入程序中headers后面字典的值（第二个）位置即可（这是一个字符串，不要漏掉符号。）

（完整版请见视频：https://www.bilibili.com/video/BV1Jg41137oq ）

祝使用愉快！
