Example for Configuring an NQA DNS Test to Measure the DNS Resolution Time on an IP Network
===========================================================================================

Example for Configuring an NQA DNS Test to Measure the DNS Resolution Time on an IP Network

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130782080__fig_dc_vrp_cfg_00214301), DeviceA is connected to the DNS server and HostA through a network.

DeviceA needs to access HostA using the domain name server.com. In this process, the DNS server needs to resolve the domain name into an IP address. A DNS test instance can be configured on DeviceA to measure the time that the DNS server takes to resolve the domain name.

**Figure 1** Network diagram for an NQA DNS test to measure the DNS resolution time on an IP network![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001130782096.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure reachable routes between DeviceA, the DNS server, and HostA at the network layer.
2. Configure a DNS test instance on DeviceA and start the test instance to measure the DNS resolution time.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the DNS server
* Domain name and IP address of HostA

#### Procedure

1. Configure the name of DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA]
   ```
2. Configure reachable routes between DeviceA, the DNS server, and HostA at the network layer. The configuration is not provided here.
3. Configure a DNS test instance and start it.
   
   
   ```
   [~DeviceA] dns resolve
   [*DeviceA] dns server 10.3.1.1
   [*DeviceA] nqa test-instance admin dns
   [*DeviceA-nqa-admin-dns] test-type dns
   [*DeviceA-nqa-admin-dns] dns-server ipv4 10.3.1.1
   [*DeviceA-nqa-admin-dns] destination-address url server.com
   [*DeviceA-nqa-admin-dns] start now
   [*DeviceA-nqa-admin-dns] commit
   ```

#### Verifying the Configuration

Verify the test result. In the command output, **Min/Max/Average Completion Time** indicates the delay between the time when a DNS request packet is sent and the time when a DNS response packet is received, which is 208 ms.

```
[~DeviceA-nqa-admin-dns] display nqa results test-instance admin dns

NQA entry(admin, dns) :test flag is inactive, test type is DNS
  1 . Test 1 result   The test is finished
   Send operation times: 1                Receive response times: 1             
   Completion: success                    RTD over thresholds number: 0           
   Attempts number: 1                     Drop operation number: 0               
   Disconnect operation number: 0         Operation timeout number: 0            
   System busy operation number: 0        Connection fail number: 0              
   Operation sequence errors number: 0    RTT Status errors number: 0            
   Destination IP address:10.3.1.1
   Min/Max/Average completion time: 208/208/208
   Sum/Square-Sum  completion time: 208/43264
   Last response packet receiving time: 2018-01-25 09:18:22.6
   Lost packet ratio: 0 %
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
dns resolve
dns server 10.3.1.1
#
nqa test-instance admin dns
 test-type dns
 destination-address url server.com
 dns-server ipv4 10.3.1.1
#
return
```