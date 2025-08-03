Example for Configuring an NQA LSP Ping Test to Check MPLS Network Connectivity
===============================================================================

This section provides an example for configuring an NQA LSP ping test to check MPLS network connectivity.

#### Networking Requirements

On the MPLS network shown in [Figure 1](#EN-US_TASK_0172373141__fig_dc_vrp_nqa_cfg_003001), DeviceA and DeviceC are PEs. It is required that the connectivity between DeviceA and DeviceC be checked periodically.

**Figure 1** Configuring an NQA LSP ping test to check MPLS network connectivity![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.

  
![](images/fig_dc_vrp_nqa_cfg_003001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an LSP ping test instance on DeviceA.
2. Start the test instance.

#### Data Preparation

To complete the configuration, you need the IP addresses of DeviceA and DeviceC.


#### Procedure

1. Create an LSP ping test instance.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa test-instance admin lspping
   ```
   ```
   [*DeviceA-nqa-admin-lspping] test-type lspping
   ```
   ```
   [*DeviceA-nqa-admin-lspping] lsp-type ipv4
   ```
   ```
   [*DeviceA-nqa-admin-lspping] destination-address ipv4 3.3.3.9 lsp-masklen 32
   ```
2. Start the test instance.
   
   
   ```
   [*DeviceA-nqa-admin-lspping] start now
   ```
   ```
   [*DeviceA-nqa-admin-lspping] commit
   ```
3. Verify the test result.
   
   
   ```
   [~DeviceA-nqa-admin-lspping] display nqa results test-instance admin lspping
   ```
   ```
    NQA entry(admin, lspping) :testFlag is inactive ,testtype is  lspping
     1 . Test 1 result   The test is finished
      Send operation times: 3              Receive response times: 3
      Completion:success                   RTD OverThresholds number: 0
      Attempts number:1                    Drop operation number:0
      Disconnect operation number:0        Operation timeout number:0
      System busy operation number:0       Connection fail number:0
      Operation sequence errors number:0   RTT Stats errors number:0
      Destination ip address:3.3.3.9
      Min/Max/Average Completion Time: 1/1/1
      Sum/Square-Sum  Completion Time: 3/3
      Last Good Probe Time: 2007-1-30 15:32:56.1
      Lost packet ratio:0% 
   ```
4. Configure the device to perform the test at 10:00 every day.
   
   
   ```
   [*DeviceA-nqa-admin-lspping] stop
   ```
   ```
   [*DeviceA-nqa-admin-lspping] start daily 10:00:00 to 10:30:00  
   ```
   ```
   [*DeviceA-nqa-admin-lspping] commit
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
  mpls lsr-id 1.1.1.9
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
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
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.9 255.255.255.255
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 1.1.1.9 0.0.0.0
  #
  ```
  ```
  nqa test-instance admin lspping
  ```
  ```
   test-type lspping
  ```
  ```
   destination-address ipv4 3.3.3.9 lsp-masklen 32
  ```
  ```
   start daily 10:00:00 to 10:30:00  
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
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
  mpls lsr-id 2.2.2.9
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
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
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 2.2.2.9 255.255.255.255
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 2.2.2.9 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.2.1.0 0.0.0.255
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
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
  mpls lsr-id 3.3.3.9
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
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
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 3.3.3.9 255.255.255.255
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 3.3.3.9 0.0.0.0
  ```
  ```
    network 10.2.1.0 0.0.0.255
  #
  ```
  ```
  return
  ```