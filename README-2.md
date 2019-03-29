2.Imagine a server with the following specs:
- 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
- 64GB of ram
- 2 tb HDD disk space
- 2 x 10Gbit/s nics

The server is used for SSL offloading and proxies around 25000 requests per second.
Please let us know which metrics are interesting to monitor in that specific case 
and how would you do that? 
What are the challenges of monitoring this?

# Solution
## metrics to monitor:
### server general metrics:?
开机状态： on off
CPU：
current cpu usage and history record
Memory：current memory usage and history record
IO Network：current speed ，throughout， and history record
application metrics: SSL certificate validate? ?SSL 成功率? success rate

## how:
pyuntil
### python 监控和预警脚本，crontab 后台运行：
#### cpu：
load cpustat.py
#### 温度：

#### memory：
usage  memstat.py

#### 硬盘: 
usage  diskstat.py
#### 网络network
#### 应用层面的监控：

## Challenge：
1、监控脚本的采样时间运行时间，如果过于频繁会影响被监控服务器的性能
2、多个监控脚本，容易出错
3、进一步能够自动化，平台化，达到24*7的不间断监控


