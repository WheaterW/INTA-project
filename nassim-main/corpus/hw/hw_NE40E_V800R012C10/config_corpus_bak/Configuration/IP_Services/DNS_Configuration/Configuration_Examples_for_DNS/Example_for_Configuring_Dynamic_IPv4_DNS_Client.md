Example for Configuring Dynamic IPv4 DNS Client
===============================================

This section describes how to configure dynamic DNS.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364815__fig_dc_vrp_dns_cfg_000901), Device A serves as the DNS client. With the help of the DNS server, Device A can use the domain name "huawei.com" to access the host with IP address 10.2.1.3/16.

**Figure 1** Networking diagram for dynamic DNS![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_dns_cfg_000901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable dynamic DNS.
2. Configure the IP address of the DNS server.
3. Configure a domain name suffix.

#### Data Preparation

To complete the configuration, you need the following data:

* Domain names of Device B and Device C
* IP address of the DNS server
* Domain name suffixes

#### Procedure

1. Configure Device A.
   
   
   
   # Configure dynamic DNS entries.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI]sysname DeviceA
   ```
   ```
   [*HUAWEI]commit
   ```
   
   # Enable dynamic DNS.
   
   ```
   [~DeviceA] dns resolve
   ```
   
   # Configure the IP address of the DNS server.
   
   ```
   [*DeviceA] dns server 10.3.1.2
   ```
   
   # Configure a domain name suffix "net".
   
   ```
   [*DeviceA] dns domain net
   ```
   
   # Configure a domain name suffix "com".
   
   ```
   [*DeviceA] dns domain com
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To implement domain name resolution, you must configure a route between Device A and the DNS server for them to communicate. For details about how to configure a route, see *NE40EUniversal Service Router Configuration Guide - IP Routing*.
2. Verify the configuration.
   
   
   
   # Run the **ping huawei** command on Device A. The host with domain name "huawei.com" can be pinged. The destination IP address for the ping operation is 10.2.1.3.
   
   ```
   <DeviceA> ping huawei.com
   ```
   ```
     PING huawei.com (10.2.1.3): 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.2.1.3: bytes=56 Sequence=1 ttl=126 time=6 ms
   ```
   ```
       Reply from 10.2.1.3: bytes=56 Sequence=2 ttl=126 time=4 ms
   ```
   ```
       Reply from 10.2.1.3: bytes=56 Sequence=3 ttl=126 time=4 ms
   ```
   ```
       Reply from 10.2.1.3: bytes=56 Sequence=4 ttl=126 time=4 ms
   ```
   ```
       Reply from 10.2.1.3: bytes=56 Sequence=5 ttl=126 time=4 ms
   
   ```
   ```
     --- huawei.com ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 4/4/6 ms
   
   ```
   
   # Run the **display dns dynamic-host** command on Device A. Dynamic DNS entry information stored in the cache is displayed.
   
   ```
   <DeviceA> display dns dynamic-host
   ```
   ```
   No  Domain Name           IpAddress            TTL       Alias
   ```
   ```
   1   huawei.com            10.2.1.3             3579  
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   TTL indicates how long a DNS entry can exist, in seconds.

#### Configuration Files

* Configuration file of Device A
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
   dns resolve
  ```
  ```
   dns server 10.3.1.2
  ```
  ```
   dns domain net
  ```
  ```
   dns domain com
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.0.0
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   network 10.1.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of Device B
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.0.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.0.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   network 10.1.0.0
  ```
  ```
  network 10.2.0.0
  ```
  ```
   network 1.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of Device C
  
  ```
  #
  ```
  ```
   sysname DeviceC
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.2 255.255.0.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.1 255.255.0.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   network 10.2.0.0
  ```
  ```
   network 10.3.0.0
  ```
  ```
  network 2.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```