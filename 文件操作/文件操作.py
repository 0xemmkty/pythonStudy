f = open("test.txt","r")
f1 = open("test1.txt","r")

#content = f.read(5)
#print(content)

#读一行
content = f.readline()
print("1:%s"%content, end="")
content = f.readline()
print("2:%s"%content, end="")
#全部读
content1 = f1.readlines()
print("%s"%content1)

f.close()
f1.close()

'''
import os
os.rename(test.txt, test2.txt)
'''