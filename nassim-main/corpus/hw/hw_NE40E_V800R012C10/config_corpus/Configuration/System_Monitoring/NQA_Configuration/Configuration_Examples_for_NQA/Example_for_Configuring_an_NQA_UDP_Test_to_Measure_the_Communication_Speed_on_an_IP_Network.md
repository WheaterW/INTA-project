Example for Configuring an NQA UDP Test to Measure the Communication Speed on an IP Network
===========================================================================================

This section provides an example for configuring a UDP test to measure the speed of communication through UDP between an NQA client and an NQA server.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001869046124__fig_dc_vrp_cfg_00214301), DeviceA functions as an NQA client and sends constructed UDP packets to DeviceB. This example measures the speed of communication through UDP between the source and destination devices.

**Figure 1** Configuring an NQA UDP test to measure the speed of communication through UDP on an IP network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.


  
![](figure/en-us_image_0000001869046160.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as the NQA client and DeviceB as the NQA server. Configure a UDP test instance on DeviceA.
2. Start a test instance.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of DeviceA and DeviceB.

#### Procedure

1. Configure DeviceB as the NQA server.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] nqa-server udpecho 10.1.1.2 4000
   ```
   ```
   [*DeviceB] commit
   ```
2. Configure DeviceA as the NQA client, create a UDP test instance, and set the destination IP address to the IP address of DeviceB.
   
   
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
   [~DeviceA] nqa test-instance admin udp
   ```
   ```
   [*DeviceA-nqa-admin-udp] test-type udp
   ```
   ```
   [*DeviceA-nqa-admin-udp] destination-address ipv4 10.1.1.2
   ```
   ```
   [*DeviceA-nqa-admin-udp] destination-port 4000
   ```
3. Start the test instance immediately.
   
   
   ```
   [*DeviceA-nqa-admin-udp] start now
   ```
   ```
   [*DeviceA-nqa-admin-udp] commit
   ```
4. Verify the test result. The test result shows the speed of communication through UDP between devices on the network based on fields such as **Min/Max/Average Completion Time**.
   
   
   ```
   [~DeviceA-nqa-admin-udp] display nqa results test-instance admin udp
   ```
   ```
   NQA entry(admin, udp) :testflag is inactive ,testtype is udp
     1 . Test 1 result   The test is finished
      Send operation times: 3                Receive response times: 3             
      Completion:success                     RTD OverThresholds number:0           
      Attempts number:1                      Drop operation number:0               
      Disconnect operation number:0          Operation timeout number:0            
      System busy operation number:0         Connection fail number:0              
      Operation sequence errors number:0     RTT Status errors number:0            
      Destination ip address:10.1.1.2
      Min/Max/Average Completion Time: 2/38/14
      Sum/Square-Sum  Completion Time: 42/1452
      Last Good Probe Time: 2024-02-19 08:44:41.3
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
  nqa test-instance admin udp
   test-type udp
   destination-address ipv4 10.1.1.2
   destination-port 4000
  #
  return
  ```
* DeviceB configuration file
  ```
  #
  sysname DeviceB
  #
  nqa server udpecho 10.1.1.2 4000
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```