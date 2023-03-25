import socket
import argparse
import sys
import time
# The above lines import necessary modules like socket 
# for creating a socket, argparse for parsing command-line
#  arguments, sys for system-specific parameters and functions,
#  and time for timing the execution of the script.

# https://zhuanlan.zhihu.com/p/56922793 
# https://vra.github.io/2017/12/02/argparse-usage/
parser = argparse.ArgumentParser() # create a object
parser.add_argument('host') # pass a para
args = parser.parse_args()
start = time.time()

# This block of code uses a for loop to iterate over all the 
# ports between 1 and 65535. It creates a new socket object for
#  each port and attempts to connect to the host using the 
# connect_ex() method of the socket object. The settimeout() 
# method sets the timeout value for the socket to 1 second. 
# If the result of the connection attempt is 0, it means the
#  port is open, and the script prints a message indicating 
# that the port is open. The socket is then closed. The try 
# and except blocks handle any keyboard interrupts that might
#  occur while the script is running.
try:
    for port in range(1, 65536):
        # 创建TCP Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((args.host, port))
        if result == 0:
            # format函数是一种格式化输出字符串的函数(str.format), 
            # 基本语法是通过 {} 和 : 来代替以前的%
            # 不需要知道替换字符的类型
            print("Port: {} Open".format(port))
        sock.close()
except KeyboardInterrupt:
    # 退出Python程序，exit(0)表示正常退出。当参数非0时，
    # 会引发一个SystemExit异常，可以在程序中捕获该异常
    sys.exit()

end = time.time()
# "f" refers to the format string in Python, 
# which is used to format the output of a value
#  as a string. In this case, it's used to format
#  the time value.{end-start:.3f} is the value 
# that is being formatted. It is the difference
#  between two time values (end and start), 
# which represents the time it took to complete
#  the scanning process. The ".3f" part specifies
#  that the value should be formatted as a float 
# number with 3 decimal places."Scanning 
# completed in:" is the message that is being printed 
# along with the formatted value.
print(f"Scanning completed in: {end-start:.3f}s")


"""
单个扫描
def scan_tools_v1(self):
    host = input('请输入服务器ip地址:')
    port = int(input('请输入要扫描的端口:'))

    sk = socket.socket()
    sk.settimeout(0.1)
    conn_result = sk.connect_ex((host, port))
    if conn_result == 0:
        print('服务器{}的{}端口已开放'.format(host, port))
    else:
        print('服务器{}的{}端口未开放'.format(host, port))
    sk.close()
"""