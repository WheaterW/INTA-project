Example for Configuring an NQA TCP Test to Measure the Response Time on an IP Network
=====================================================================================

This section provides an example for configuring an NQA TCP test to measure the response time on an IP network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373134__fig_dc_vrp_nqa_cfg_002601), the headquarters and a subsidiary often need to use TCP to exchange files with each other. The time taken to respond to a TCP transmission request must be less than 800 ms. An NQA TCP test can be configured to measure the TCP response time between RouterDeviceA and RouterDeviceD on the edge of the enterprise network.

**Figure 1** Configuring an NQA TCP test to measure the response time on an IP network![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface 1 represents GE0/1/0.

  
![](images/fig_dc_vrp_nqa_cfg_002601.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceD as the NQA client and DeviceA as the NQA server, and create a TCP test instance.
2. Configure the client to perform the test at 10:00 o'clock every day and start the test instance.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of DeviceA and DeviceD on the edge of the enterprise network
* Number of the port used to monitor TCP services

#### Procedure

1. Configure DeviceA (NQA server).
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa-server tcpconnect 10.1.1.1 4000
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure DeviceD (NQA client). Create a TCP test instance, and set the destination IP address to the IP address of DeviceA.
   
   
   ```
   <DeviceD> system-view
   ```
   ```
   [*DeviceD] nqa test-instance admin tcp
   ```
   ```
   [*DeviceD-nqa-admin-tcp] test-type tcp
   ```
   ```
   [*DeviceD-nqa-admin-tcp] destination-address ipv4 10.1.1.1
   ```
   ```
   [*DeviceD-nqa-admin-tcp] destination-port 4000
   ```
   ```
   [*DeviceD-nqa-admin-tcp] commit 
   ```
3. Start the test instance immediately.
   
   
   ```
   [*DeviceD-nqa-admin-tcp] start now
   ```
   ```
   [*DeviceD-nqa-admin-tcp] commit
   ```
4. Verify the test result. The command output shows that the TCP response time is less than 800 ms.
   
   
   ```
   [~DeviceD-nqa-admin-tcp] display nqa results test-instance admin tcp
   
   NQA entry(admin, tcp) :testflag is active ,testtype is tcp 
   1 . Test 1 result   The test is finished
      Send operation times: 3                Receive response times: 3
      Completion:success                     RTD OverThresholds number:0
      Attempts number:1                      Drop operation number:0
      Disconnect operation number:0          Operation timeout number:0
      System busy operation number:0         Connection fail number:0
      Operation sequence errors number:0     RTT Stats errors number:0
      Destination ip address:10.1.1.1
      Min/Max/Average Completion Time: 600/610/603
      Sum/Square-Sum  Completion Time: 1810/1092100
      Last Good Probe Time: 2011-01-16 02:59:41.6
      Lost packet ratio: 0 %                         
   ```
5. Configure the client to perform the test at 10:00 every day.
   
   
   ```
   [~DeviceD-nqa-admin-tcp] stop
   ```
   ```
   [*DeviceD-nqa-admin-tcp] start daily 10:00:00 to 10:30:00  
   ```
   ```
   [*DeviceD-nqa-admin-tcp] commit
   ```

#### Configuration Files

* DeviceA configuration file
  
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
   nqa-server tcpconnect 10.1.1.1 4000
  ```
  ```
  #
  ```
  ```
  isis 1
   network-entity 00.0000.0000.0001.00
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
   ip address 10.1.1.1 255.255.255.0
   isis enable 1 
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceD
  ```
  ```
  #
  ```
  ```
  isis 1
   network-entity 00.0000.0000.0002.00  
  #
  ```
  ```
   interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.2.1 255.255.255.0
   isis enable 1 
  ```
  ```
  #
  ```
  ```
  nqa test-instance admin tcp
   test-type tcp
   destination-address ipv4 10.1.1.1
   destination-port 4000
   start daily 10:00:00 to 10:30:00     
  ```
  ```
  #
  ```
  ```
  return
  ```