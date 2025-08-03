Example for Configuring a Generalflow Test in an IP Gateway Scenario (RFC 2544)
===============================================================================

This section describes how to configure a generalflow test to measure the performance of an Ethernet network in an IP gateway scenario.

#### Usage Scenario

A generalflow test needs to be configured to measure the performance of the Ethernet network shown in [Figure 1](#EN-US_TASK_0172373150__fig_dc_vrp_nqa_cfg_005101) between DeviceA and DeviceB (IP gateway).

**Figure 1** Configuring a generalflow test in a Layer 2 accessing Layer 3 scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_nqa_cfg_005101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA as the reflector.
2. Configure DeviceB as the initiator and configure it to perform a delay test.

#### Data Preparation

To complete the configuration, you need the following data:

* Configurations on DeviceA (reflector): simulated IP address 10.1.1.1 (CE's IP address) and reflector interface (GE0/1/1).
* Configurations on DeviceB (initiator):
  
  + Destination IP address: 10.1.1.1 (IP address of the CE interface connected to reflector's GE0/1/1
  + Source IP address: an address that resides on the same network segment as the IP address of the initiator
  + Delay test parameters: packet rate (99000 kbit/s), test duration (100s), and interval (5s) for sending test packets

#### Procedure

1. Configure the CE and DeviceB to communicate through the Layer 2 device between them and ensure that the Layer 3 link is reachable.
2. Configure the reflector.
   
   
   ```
   [*DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
   ```
   [~DeviceA] nqa reflector 1 interface GigabitEthernet 0/1/1 ipv4 10.1.1.1 vlan 10 
   ```
   ```
   [*DeviceA] commit
   ```
3. Configure the initiator to perform a delay test and check the test results.
   
   
   ```
   [*DeviceB] vlan 10
   ```
   ```
   [*DeviceB-vlan10] commit
   ```
   ```
   [~DeviceB-vlan10] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/2.1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2.1] vlan-type dot1q 10
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2.1] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2.1] quit
   ```
   ```
   [*DeviceB] arp static 10.1.1.1 00e0-fc12-3456 vid 10 interface GigabitEthernet 0/1/2.1
   ```
   ```
   [*DeviceB] nqa test-instance admin delay
   ```
   ```
   [*DeviceB-nqa-admin-delay] test-type generalflow
   ```
   ```
   [*DeviceB-nqa-admin-delay] measure delay
   ```
   ```
   [*DeviceB-nqa-admin-delay] destination-address ipv4 10.1.1.1
   ```
   ```
   [*DeviceB-nqa-admin-delay] source-address ipv4 10.1.1.2
   ```
   ```
   [*DeviceB-nqa-admin-delay] source-interface gigabitethernet 0/1/2.1
   ```
   ```
   [*DeviceB-nqa-admin-delay] rate 99000
   ```
   ```
   [*DeviceB-nqa-admin-delay] interval seconds 5
   ```
   ```
   [*DeviceB-nqa-admin-delay] datasize 64
   ```
   ```
   [*DeviceB-nqa-admin-delay] duration 100
   ```
   ```
   [*DeviceB-nqa-admin-delay] start now
   ```
   ```
   [*DeviceB-nqa-admin-delay] commit
   ```
   ```
   [~DeviceB-nqa-admin-delay] display nqa results test-instance admin delay
   
   NQA entry(admin, delay) :testflag is inactive ,testtype is generalflow
     1 . Test 1 result: The test is finished, test mode is delay
      Total time:751s, path-learning time:1s, test time:747s
      ID Size Min/Max/Avg RTT(us)     Min/Max/Avg Jitter(us)  Completion
      1  64   97/107/102              0/6/3                   finished
      2  128  97/106/100              0/6/2                   finished
      3  256  96/103/100              0/6/2                   finished
      4  512  98/109/102              0/8/2                   finished
      5  1024 100/106/103             0/4/1                   finished
      6  1280 103/109/105             0/5/2                   finished
      7  1518 105/110/107             0/3/1                   finished
      Start time: 2024-02-21 15:06:54.8
      End   time: 2024-02-21 15:19:26.2
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  # 
  vlan 10
  #
  nqa reflector 1 interface GigabitEthernet 0/1/1 ipv4 10.1.1.1 vlan 10
  #
  interface GigabitEthernet 0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet 0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  vlan 10
  #
  interface GigabitEthernet 0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet 0/1/2.1
   vlan-type dot1q 10
   ip address 10.1.1.2 255.255.255.0
  #
  arp static 10.1.1.1 00e0-fc12-3456 vid 10 interface GigabitEthernet 0/1/2.1
  nqa test-instance admin delay
   test-type generalflow
   destination-address ipv4 10.1.1.1
   source-address ipv4 10.1.1.2
   duration 100
   measure delay
   interval seconds 5
   datasize 64
   rate 99000
   source-interface GigabitEthernet 0/1/2.1
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  # 
  vlan 10
  #
  interface GigabitEthernet 0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet 0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```