Example for Configuring an NQA ICMP Test to Check IP Network Reachability
=========================================================================

This section provides an example for configuring an ICMP test to check network reachability between an NQA client and an NQA server.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001868886284__fig_dc_vrp_cfg_00214301), DeviceA serves as an NQA client to check whether DeviceB is reachable.

**Figure 1** Configuring an NQA ICMP test to check IP network reachability![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.


  
![](figure/en-us_image_0000001914925505.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as the NQA client and DeviceB as the NQA server. Configure an ICMP test instance on DeviceA.
2. Start a test instance.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of DeviceA and DeviceD

#### Procedure

1. Configure DeviceA (NQA client). Create an ICMP test instance, and set the destination IP address to the IP address of DeviceB.
   
   
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
   [~DeviceA] nqa test-instance admin icmp
   ```
   ```
   [*DeviceA-nqa-admin-icmp] test-type icmp
   ```
   ```
   [*DeviceA-nqa-admin-icmp] destination-address ipv4 10.1.1.2
   ```
2. Start the test instance immediately.
   
   
   ```
   [*DeviceA-nqa-admin-icmp] start now
   ```
   ```
   [*DeviceA-nqa-admin-icmp] commit
   ```
3. Verify the test result. The command output shows that there is a reachable route between the NQA client and server (DeviceB).
   
   
   ```
   [~DeviceA-nqa-admin-icmp] display nqa results test-instance admin icmp
   ```
   ```
   NQA entry(admin, icmp) :testflag is inactive ,testtype is icmp
     1 . Test 1 result   The test is finished
      Send operation times: 3                Receive response times: 3             
      Completion:success                     RTD OverThresholds number:0           
      Attempts number:1                      Drop operation number:0               
      Disconnect operation number:0          Operation timeout number:0            
      System busy operation number:0         Connection fail number:0              
      Operation sequence errors number:0     RTT Status errors number:0            
      Destination ip address:10.1.1.2
      Min/Max/Average Completion Time: 31/46/36
      Sum/Square-Sum  Completion Time: 108/4038
      Last Good Probe Time: 2024-4-8 10:7:11.4 
      Lost packet ratio: 0 %
   ```

#### Configuration Files

DeviceA configuration file

```
#
sysname DeviceA
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 10.1.1.1 255.255.255.0
#
nqa test-instance admin icmp
 test-type icmp
 destination-address ipv4 10.1.1.2
#
return
```