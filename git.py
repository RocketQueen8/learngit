import os
path = os.getcwd()
import psutil
total=psutil.disk_usage(path).total/1024/1024/1024
print(total)
