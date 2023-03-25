# 异常类型的积累
# 本case中，num本来没有定义，理论上应该报错。
# 使用try..except实际上就是拦截了错误 输出自定义
try:
    print(num)
except NameError as result:   #这里可以写所有可能出现的错误
# except Exception:   #Exception 可以承接所有异常
    print("产生错误了")
    print(result)


# try...finally...   finally 一定会被执行
# 文件open，无论发生什么都要 close

try:
    f = open("test1.txt","r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常....")