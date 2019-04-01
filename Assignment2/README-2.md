#### ASSIGNMENT 2
Imagine a server with the following specs:
- 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
- 64GB of ram
- 2 tb HDD disk space
- 2 x 10Gbit/s nics

The server is used for SSL offloading and proxies around 25000 requests per second.
Please let us know which metrics are interesting to monitor in that specific case 
and how would you do that? 
What are the challenges of monitoring this?

#### Solution
#### metrics to monitor:

**server general metrics :**

* Sever running state
* CPU

    *CPU used*
    
    *CPU load*
    
    *CPU temperature*
* Memeroy usage
* I/O

    *Disk space usage*
    
     *IO read, IO write*
* Network

    *Network traffic*
    
    *TCP connection states*

**application metrics :**

*SSL certificate validate status*
### how to monitor metrics:
* **Method 1: monitor Platform zabbix**
1. monitor all the important metrics  in value or gragh way within certain time(CPU_temp_value.png, CPU_temp_graph)
    * CPU

    *CPU used(15min_CPU_use.png)*
    
    *CPU load(15min_CPU_load.png)*
    
    *CPU temperature(5min_CPU_temp.png)*
* Memeroy usage
   *Memeroy used(6h_mem_use.png*
   
* I/O

    *Disk space usage(1day_disk_use.png)*
    
     *IO read, IO write*
     
* Network

    *Network traffic（1h_net_traffic.png）*
    
    *TCP connection states*
    
 * SSL application
 
 *SSL certificate validate status(template_SSL_Cert_Check_External.xml)*
 
2. when the metric value is over limit field, will trig the related trigger, and can send alert message through sms or email(triggers.png, send_alert_message.png)

3. custom metric item graph and trigger not in default(add_new_item(agentconfUserparameter).png, add_new_item(webfront), add_new_graph)

*  **Method 2: Custom Python script to monitor each metric and send warning when metric value over expected, then add a cron job in the server to run**
*  CPU

    *CPU used : cpu_used.py*
    
    *CPU load : cpu_load.py*
    
    *CPU temperature: cpu_temp.py*
* Memeroy usage
   *Memeroy used rate : mem_used.py*
   
* I/O

    *Disk space usage: disk_used.py*
    
     *IO read, IO write*
     
* Network
    *Network traffic*
    
    *TCP connection states*
    
 * SSL application
 *SSL certificate validate status*
 
    
 ### Challenge：
1. Metrics  monitoring tool should not effect the server's performance

2. Proper trigger warning value，minimum false alarm

3. Performance issue locating and Performance tunning

