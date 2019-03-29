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
����״̬�� on off
CPU��
current cpu usage and history record
Memory��current memory usage and history record
IO Network��current speed ��throughout�� and history record
application metrics: SSL certificate validate? ?SSL �ɹ���? success rate

## how:
pyuntil
### python ��غ�Ԥ���ű���crontab ��̨���У�
#### cpu��
load cpustat.py
#### �¶ȣ�

#### memory��
usage  memstat.py

#### Ӳ��: 
usage  diskstat.py
#### ����network
#### Ӧ�ò���ļ�أ�

## Challenge��
1����ؽű��Ĳ���ʱ������ʱ�䣬�������Ƶ����Ӱ�챻��ط�����������
2�������ؽű������׳���
3����һ���ܹ��Զ�����ƽ̨�����ﵽ24*7�Ĳ���ϼ��


