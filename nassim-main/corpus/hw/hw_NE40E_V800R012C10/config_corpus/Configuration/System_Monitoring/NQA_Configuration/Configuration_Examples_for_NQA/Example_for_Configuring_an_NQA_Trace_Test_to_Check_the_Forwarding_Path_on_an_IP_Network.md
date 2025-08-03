Example for Configuring an NQA Trace Test to Check the Forwarding Path on an IP Network
=======================================================================================

This section provides an example for configuring a trace test to check the forwarding path between an NQA client and an NQA server.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001915005809__fig_dc_vrp_cfg_00214301), DeviceA serves as an NQA client in a test used to check the forwarding path between DeviceA and DeviceC.

**Figure 1** Configuring an NQA trace test to check the forwarding path on an IP network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001914925513.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as the NQA client and DeviceC as the NQA server. Configure a trace test instance on DeviceA.
2. Start a test instance.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of DeviceA and DeviceC.

#### Procedure

1. Configure DeviceA (NQA client). Create a trace test instance, and set the destination IP address to the IP address of DeviceC.
   
   
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
   [~DeviceA] nqa test-instance admin trace
   ```
   ```
   [*DeviceA-nqa-admin-trace] test-type trace
   ```
   ```
   [*DeviceA-nqa-admin-trace] destination-address ipv4 10.2.1.2
   ```
2. Start the test instance immediately.
   
   
   ```
   [*DeviceA-nqa-admin-trace] start now
   ```
   ```
   [*DeviceA-nqa-admin-trace] commit
   ```
3. Verify the test result. You can view information about each hop between DeviceC and the NQA server.
   
   
   ```
   [~DeviceA-nqa-admin-trace] display nqa results test-instance admin trace
   ```
   ```
   NQA entry(admin, trace) :testflag is inactive ,testtype is trace
     1 . Test 1 result   The test is finished
      Completion:success                     Attempts number:1
      Disconnect operation number:0          Operation timeout number:0
      System busy operation number:0         Connection fail number:0
      Operation sequence errors number:0     RTT Status errors number:0
      Drop operation number:0
      Last good path Time: 2024-05-06 06:58:15.9
      1 . Hop 1
       Send operation times: 3              Receive response times: 3
       Min/Max/Average Completion Time: 1/4/2
       Sum/Square-Sum  Completion Time: 6/18
       RTD OverThresholds number:0
       Last Good Probe Time: 2024-05-06 06:58:15.9
       Destination ip address:10.1.1.2
       Lost packet ratio: 0 %
      2 . Hop 2
       Send operation times: 3              Receive response times: 3
       Min/Max/Average Completion Time: 1/3/1
       Sum/Square-Sum  Completion Time: 5/11
       RTD OverThresholds number:0
       Last Good Probe Time: 2024-05-06 06:58:15.9
       Destination ip address:10.2.1.2
       Lost packet ratio: 0 %
   ```

#### Configuration Files

* DeviceA configuration file
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  ip route-static 10.2.1.0 255.255.255.0 10.1.1.2
  #
  nqa test-instance admin trace
   test-type trace
   destination-address ipv4 10.2.1.2
  #
  return
  ```
* DeviceB configuration file
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
  #
  return
  ```
* DeviceC configuration file
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  ip route-static 10.1.1.0 255.255.255.0 10.2.1.1
  #
  return
  ```