Example for Configuring a Generalflow Test in a Native Ethernet Scenario (RFC 2544)
===================================================================================

This section describes how to configure a generalflow test to measure the performance of a native Ethernet network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373147__fig_dc_vrp_nqa_cfg_005001), the performance of the Ethernet virtual connection (EVC) between DeviceA and DeviceB is measured.

**Figure 1** Generalflow test in a native Ethernet scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_nqa_cfg_005001.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceB as the reflector and configure it to reflect traffic with a specified destination MAC address through GE0/1/1 (reflector interface) to the initiator.
2. Configure DeviceA as the initiator and configure it to perform throughput, delay, and packet loss rate tests.
3. Add the interfaces of DeviceC (intermediate device) to a specified VLAN.

#### Data Preparation

To complete the configuration, you need the following data:

* Configurations on DeviceB (reflector): MAC address of UNI-B (00e0-fc12-3456)
* Configurations on DeviceA (initiator):
  
  + Destination MAC address: 00e0-fc12-3456 (MAC address of UNI-B)
  + Throughput test parameters: upper and lower thresholds of the packet sending rate (100000 kbit/s and 10000 kbit/s, respectively), throughput precision (1000 kbit/s), packet loss precision (81/10000), timeout period of each packet sending rate (5s), packet sending size (70 bytes), and test instance execution duration (100s)
  + Delay test parameters: packet rate (99000 Kbit/s), test duration (100s), and interval (5s) at which the initiator sends test packets
  + Packet loss rate test parameters: packet rate (99000 Kbit/s), and test duration (100s)

#### Procedure

1. Configure reachable Layer 2 links between the initiator and reflector and add Layer 2 interfaces to VLAN 10.
2. Configure the reflector.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] nqa reflector 1 interface gigabitethernet 0/1/1 mac 00e0-fc12-3456 vlan 10
   ```
3. Configure the initiator to perform a throughput test and check the test results.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa test-instance admin throughput
   ```
   ```
   [*DeviceA-nqa-admin-throughput] test-type generalflow
   ```
   ```
   [*DeviceA-nqa-admin-throughput] measure throughput
   ```
   ```
   [*DeviceA-nqa-admin-throughput] destination-address mac 00e0-fc12-3456
   ```
   ```
   [*DeviceA-nqa-admin-throughput] forwarding-simulation inbound-interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-nqa-admin-throughput] rate 10000 100000
   ```
   ```
   [*DeviceA-nqa-admin-throughput] interval seconds 5
   ```
   ```
   [*DeviceA-nqa-admin-throughput] precision 1000
   ```
   ```
   [*DeviceA-nqa-admin-throughput] fail-ratio 81
   ```
   ```
   [*DeviceA-nqa-admin-throughput] datasize 70
   ```
   ```
   [*DeviceA-nqa-admin-throughput] duration 100
   ```
   ```
   [*DeviceA-nqa-admin-throughput] vlan 10
   ```
   ```
   [*DeviceA-nqa-admin-throughput] start now
   ```
   ```
   [*DeviceA-nqa-admin-throughput] commit
   ```
   ```
   [~DeviceA-nqa-admin-throughput] display nqa results test-instance admin throughput
   
   NQA entry(admin, throughput) :testflag is inactive ,testtype is generalflow
     1 . Test 1 result: The test is finished, test mode is throughput
      Total time:17s, path-learning time:1s, test time:13s
      Ethernet frame rate: utilized line rate(L1 rate)
      ID Size Throughput(Kbps) Precision(Kbps) LossRatio    Completion
      1  70   100000           1000            0.0000000%   success
      Start time: 2023-09-04 18:25:02.6
      End   time: 2023-09-04 18:25:19.9
   ```
4. Configure the initiator to perform a delay test and check the test results.
   
   
   ```
   [*DeviceA] nqa test-instance admin delay
   ```
   ```
   [*DeviceA-nqa-admin-delay] test-type generalflow
   ```
   ```
   [*DeviceA-nqa-admin-delay] measure delay
   ```
   ```
   [*DeviceA-nqa-admin-delay] destination-address mac 00e0-fc12-3456
   ```
   ```
   [*DeviceA-nqa-admin-delay] forwarding-simulation inbound-interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-nqa-admin-delay] datasize 64
   ```
   ```
   [*DeviceA-nqa-admin-delay] rate 99000
   ```
   ```
   [*DeviceA-nqa-admin-delay] interval seconds 5
   ```
   ```
   [*DeviceA-nqa-admin-delay] duration 100
   ```
   ```
   [*DeviceA-nqa-admin-delay] vlan 10
   ```
   ```
   [*DeviceA-nqa-admin-delay] start now
   ```
   ```
   [*DeviceA-nqa-admin-delay] commit
   ```
   ```
   [~DeviceA-nqa-admin-delay] display nqa results test-instance admin delay
   NQA entry(admin, delay) :testflag is inactive ,testtype is generalflow
     1 . Test 1 result: The test is finished, test mode is delay
      Total time:110s, path-learning time:1s, test time:106s
      ID Size Min/Max/Avg RTT(us)     Min/Max/Avg Jitter(us)  Completion
      1  64   149/162/154             0/11/3                  finished
      Start time: 2023-09-04 19:55:30.5
      End   time: 2023-09-04 19:57:20.6
   ```
5. Configure the initiator to perform a packet loss rate test and check the test results.
   
   
   ```
   [*DeviceA] nqa test-instance admin loss
   ```
   ```
   [*DeviceA-nqa-admin-loss] test-type generalflow
   ```
   ```
   [*DeviceA-nqa-admin-loss] measure loss
   ```
   ```
   [*DeviceA-nqa-admin-loss] destination-address mac 00e0-fc12-3456
   ```
   ```
   [*DeviceA-nqa-admin-loss] forwarding-simulation inbound-interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-nqa-admin-loss] datasize 64
   ```
   ```
   [*DeviceA-nqa-admin-loss] rate 99000
   ```
   ```
   [*DeviceA-nqa-admin-loss] duration 100
   ```
   ```
   [*DeviceA-nqa-admin-loss] vlan 10
   ```
   ```
   [*DeviceA-nqa-admin-loss] start now
   ```
   ```
   [*DeviceA-nqa-admin-loss] commit
   ```
   ```
   [~DeviceA-nqa-admin-loss] display nqa results test-instance admin loss
   
   NQA entry(admin, loss) :testflag is inactive ,testtype is generalflow
     1 . Test 1 result: The test is finished, test mode is loss
      Total time:112s, path-learning time:1s, test time:108s
      Ethernet frame rate: utilized line rate(L1 rate)
      ID Size TxRate/RxRate(Kbps) TxCount/RxCount             LossRatio    Completion
      1  64   99000/99000         29464286/29464286           0.0000000%   finished
      Start time: 2023-09-04 19:29:37.0
      End   time: 2023-09-04 19:31:28.6
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
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
  nqa test-instance admin throughput
   test-type generalflow
   duration 100
   measure throughput
   fail-ratio 81
   destination-address mac 00e0-fc12-3456
   datasize 70
   rate 10000 100000
   precision 1000
   forwarding-simulation inbound-interface GigabitEthernet0/1/1
   vlan 10
  nqa test-instance admin loss
   test-type generalflow
   duration 100
   measure loss
   destination-address mac 00e0-fc12-3456
   datasize 64
   rate 99000
   forwarding-simulation inbound-interface GigabitEthernet0/1/1
   vlan 10
  nqa test-instance admin delay
   test-type generalflow
   duration 100
   measure delay
   interval seconds 5
   destination-address mac 00e0-fc12-3456
   datasize 64
   rate 99000
   forwarding-simulation inbound-interface GigabitEthernet0/1/1
   vlan 10
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  # 
  vlan 10
  nqa reflector 1 interface gigabitethernet 0/1/1 mac 00e0-fc12-3456 vlan 10
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