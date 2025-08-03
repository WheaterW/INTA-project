Example for Configuring an NQA Test to Measure the DNS Resolution Speed on an IP Network
========================================================================================

This section provides an example for configuring an NQA test to measure the performance of interaction between a client and the DNS server.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0139427963__fig_dc_vrp_cfg_00214301), DeviceA needs to access HostA using the domain name **Server.com**. A DNS test instance can be configured on DeviceA to measure the performance of interaction between DeviceA and the DNS server.

**Figure 1** Measuring the DNS resolution speed![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.


  
![](images/fig_dc_vrp_nqa_cfg_203604.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure reachable routes between DeviceA, the DNS server, and HostA at the network layer.
2. Configure a DNS test instance on DeviceA and start the test instance to measure the DNS resolution speed on the IP network.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the DNS server
* Domain name and IP address of HostA

#### Procedure

1. Configure reachable routes between DeviceA, the DNS server, and HostA at the network layer. (Omitted)
2. Configure a DNS test instance and start it.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] dns resolve
   ```
   ```
   [*DeviceA] dns server 10.3.1.1
   ```
   ```
   [*DeviceA] dns server source-ip 10.1.1.1
   ```
   ```
   [*DeviceA] nqa test-instance admin dns
   ```
   ```
   [*DeviceA-nqa-admin-dns] test-type dns
   ```
   ```
   [*DeviceA-nqa-admin-dns] dns-server ipv4 10.3.1.1
   ```
   ```
   [*DeviceA-nqa-admin-dns] destination-address url Server.com
   ```
   ```
   [*DeviceA-nqa-admin-dns] commit
   ```
   ```
   [~DeviceA-nqa-admin-dns] start now
   ```
   ```
   [*DeviceA-nqa-admin-dns] commit
   ```
3. Verify the test result. **Min/Max/Average Completion Time** indicates the delay between the time when a DNS request packet is sent and the time when a DNS response packet is received. In this example, the delay is 208 ms.
   
   
   ```
   [~DeviceA-nqa-admin-dns] display nqa results test-instance admin dns
   ```
   ```
   NQA entry(admin, dns) :testflag is inactive ,testtype is dns
     1 . Test 1 result   The test is finished
      Send operation times: 1                Receive response times: 1             
      Completion:success                     RTD OverThresholds number:0           
      Attempts number:1                      Drop operation number:0               
      Disconnect operation number:0          Operation timeout number:0            
      System busy operation number:0         Connection fail number:0              
      Operation sequence errors number:0     RTT Status errors number:0            
      Destination ip address:10.3.1.1
      Min/Max/Average Completion Time: 208/208/208
      Sum/Square-Sum  Completion Time: 208/43264
      Last Good Probe Time: 2018-01-25 09:18:22.6
      Lost packet ratio: 0 %
   ```

#### Configuration Files

DeviceA configuration file

```
#
sysname DeviceA
#
dns resolve
dns server 10.3.1.1
dns server source-ip 10.1.1.1
#
nqa test-instance admin dns
 test-type dns
 destination-address url Server.com
 dns-server ipv4 10.3.1.1
#
return
```