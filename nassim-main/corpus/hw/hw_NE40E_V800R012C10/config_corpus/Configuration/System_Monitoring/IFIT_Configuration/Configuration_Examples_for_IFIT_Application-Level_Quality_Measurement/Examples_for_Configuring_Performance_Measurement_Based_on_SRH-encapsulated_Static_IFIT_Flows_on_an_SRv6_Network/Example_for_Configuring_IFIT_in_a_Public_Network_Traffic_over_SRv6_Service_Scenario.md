Example for Configuring IFIT in a Public Network Traffic over SRv6 Service Scenario
===================================================================================

This section provides an example for configuring IFIT to implement hop-by-hop packet loss and delay measurement in a public network IPv4 over SRv6 scenario.

#### Networking Requirements

To meet users' higher requirements on service quality, IFIT is required on a public network to monitor the packet loss rate and delay of links between PEs in real time. This enables timely responses to service quality deterioration. In the public network IPv4 over SRv6 scenario shown in [Figure 1](#EN-US_TASK_0310283453__fig_dc_vrp_srv6_cfg_all_001101), PE1, the P, and PE2 belong to the same AS and need to run IS-IS to implement IPv6 network connectivity. PE1, the P, and PE2 are Level-1 devices that belong to IS-IS process 1. An IBGP peer relationship needs to be established between PE1 and PE2, and EBGP peer relationships need to be established between the PEs and devices. A bidirectional SRv6 TE Policy needs to be established between PE1 and PE2 to carry public network IPv4 services. Service flows enter the network through PE1, traverses the P, and leaves the network through PE2.

**Figure 1** Configuring IFIT in public network traffic over SRv6 scenarios![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0310433153.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure public network IPv4 over SRv6 TE Policy on each PE and the P. Specifically:
   1. Enable IPv6 forwarding on each device and configure IPv6 addresses for involved interfaces.
   2. Enable IS-IS, configure a level, and specify a network entity on each device.
   3. Establish an EBGP peer relationship between the PEs and devices.
   4. Set up an MP-IBGP peer relationship between the PEs.
   5. Deploy an SRv6 TE Policy between PE1 and PE2, and enable IS-IS SRv6.
2. Configure basic 1588v2 functions to synchronize clocks among all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0310283453__fig_dc_vrp_srv6_cfg_all_001101)
* IS-IS process IDs of the PEs and P
* IS-IS levels on the PEs and P
* IFIT instance ID (1) and measurement interval (10s)
* Target flow's source IP address (10.1.1.1) and destination IP address (10.2.1.1)
* NMS's IPv6 address (2001:db8:101::1) and port number (10001), and reachable routes between the NMS and device


#### Procedure

1. Configure a public network IPv4 over SRv6 TE Policy on each PE and the P. For configuration details, see [Configuration Files](#EN-US_TASK_0310283453__section_05).
2. Configure 1588v2 to synchronize the clocks of the P and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0310283453__section_05).
3. Configure IFIT for the link between PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] ifit
   ```
   ```
   [*PE1-ifit] node-id 1
   ```
   ```
   [*PE1-ifit] instance 1
   ```
   ```
   [*PE1-ifit-instance-1] measure-mode trace
   ```
   ```
   [*PE1-ifit-instance-1] interval 10
   ```
   ```
   [*PE1-ifit-instance-1] flow unidirectional source 10.1.1.1 destination 10.2.1.1 dscp 63
   ```
   ```
   [*PE1-ifit-instance-1] binding interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-ifit-instance-1] commit
   ```
   ```
   [~PE1-ifit-instance-1] quit
   ```
   ```
   [~PE1-ifit] quit
   ```
   # Run the [**display ifit static**](cmdqueryname=display+ifit+static) command to check the configuration and status of PE1.
   ```
   [~PE1] display ifit static instance 1
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : static
   Instance Id                             : 1
   Instance Name                           : 1 
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Source IP Address/Mask Length           : 10.1.1.1/32
   Destination IP Address/Mask Length      : 10.2.1.1/32
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Gtp                                     : disable
   Gtp TeId                                : --
   Dscp                                    : 63
   Interface                               : GigabitEthernet0/2/0
   vpn-instance                            : --
   Measure State                           : enable 
   Loss Measure                            : enable
   Delay Measure                           : enable
   Delay Per packet Measure                : disable
   Disorder Measure                        : disable
   Gtpu Sequence Measure                   : disable
   Single Device Measure                   : disable
   Measure Mode                            : trace
   Interval                                : 10(s)
   Tunnel Type                             : --
   Flow Match Priority                     : 0
   Flow InstType Priority                  : 9
   ```
   
   # Configure the P.
   
   ```
   <P> system-view
   ```
   ```
   [~P] ifit
   ```
   ```
   [*P-ifit] node-id 3
   ```
   ```
   [*P-ifit] commit
   ```
   ```
   [~P-ifit] quit
   ```
   
   # Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) command to view the configuration and status of the P.
   
   ```
   [~P] display ifit dynamic-hop
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 514
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : GigabitEthernet0/2/0
   Direction                               : transitOutput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 513
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : GigabitEthernet0/1/0
   Direction                               : transitInput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   ```
   # Configure PE2.
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] ifit
   ```
   ```
   [*PE2-ifit] node-id 2
   ```
   ```
   [*PE2-ifit] commit
   ```
   ```
   [~PE2-ifit] quit
   ```
   
   # Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) command to check the configuration and status of PE2.
   
   ```
   [~PE2] display ifit dynamic-hop
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 514
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : GigabitEthernet0/2/0
   Direction                               : egress
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 513
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : GigabitEthernet0/1/0
   Direction                               : transitInput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   ```
   # Configure the device to send statistics to the NMS through telemetry. The following uses PE1 as an example.
   ```
   [~PE1] telemetry
   ```
   ```
   [~PE1-telemetry] destination-group ifit
   ```
   ```
   [*PE1-telemetry-destination-group-ifit] ipv6-address 2001:DB8:101::1 port 10001 protocol grpc
   ```
   ```
   [*PE1-telemetry-destination-group-ifit] quit
   ```
   ```
   [*PE1-telemetry] sensor-group ifit
   ```
   ```
   [*PE1-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
   ```
   ```
   [*PE1-telemetry-sensor-group-ifit-path] quit
   ```
   ```
   [*PE1-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   ```
   ```
   [*PE1-telemetry-sensor-group-ifit-path] quit
   ```
   ```
   [*PE1-telemetry-sensor-group-ifit] quit
   ```
   ```
   [*PE1-telemetry] subscription ifit
   ```
   ```
   [*PE1-telemetry-subscription-ifit] sensor-group ifit sample-interval 0
   ```
   ```
   [*PE1-telemetry-subscription-ifit] destination-group ifit
   ```
   ```
   [*PE1-telemetry-subscription-ifit] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure devices to send data using a secure TLS encryption mode. For details, see *Telemetry Configuration*.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  #
  tunnel-selector p1 permit node 1
   apply tunnel-policy p1
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator aa ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::100 end psp 
   segment-list list1
    index 5 sid ipv6 2001:DB8:200::100
   srv6-te policy policy1 endpoint 2001:DB8:2::2 color 101
    candidate-path preference 100
     segment-list list1
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator aa
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/96
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   ptp enable
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 1.1.1.1
   peer 192.168.1.1 as-number 200
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    network 192.168.1.0 255.255.255.0
    unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
    segment-routing ipv6 locator aa
    segment-routing ipv6 traffic-engineer
    peer 192.168.1.1 enable
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 route-policy color export
    peer 2001:DB8:2::2 advertise-ext-community
    peer 2001:DB8:2::2 prefix-sid
  #
  ifit
   node-id 1
   instance 1
    measure-mode trace
    interval 10
    flow unidirectional source 10.1.1.1 destination 10.2.1.1 dscp 63
    binding interface GigabitEthernet0/2/0 
  #
  route-policy color permit node 10
   apply extcommunity color 0:101
  #
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv6-address 2001:DB8:101::1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  #
  clock source bits0 synchronization enable
  clock source bits0 priority 1
  clock source ptp synchronization enable
  clock source ptp priority 1
  clock bits-type bits0 2mhz
  #
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   #
  #  
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::2/96
   isis ipv6 enable 1
   ptp enable
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/96
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:30::3/96
   ptp enable
  #
  ifit
   node-id 3
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv6-address 2001:DB8:101::1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  #
  tunnel-selector p1 permit node 1
   apply tunnel-policy p1
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator aa ipv6-prefix 2001:DB8:200:: 64 static 32
    opcode ::100 end psp
   segment-list list1
    index 5 sid ipv6 2001:DB8:100::100
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    candidate-path preference 100
     segment-list list1
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator aa
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::2/96
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   ptp enable
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 2.2.2.2
   peer 192.168.2.1 as-number 300
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    network 192.168.2.0 255.255.255.0
    unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
    segment-routing ipv6 locator aa
    segment-routing ipv6 traffic-engineer
    peer 192.168.2.1 enable
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy color export
    peer 2001:DB8:1::1 advertise-ext-community
    peer 2001:DB8:1::1 prefix-sid
  #
  ifit
   node-id 2
  #
  route-policy color permit node 10
   apply extcommunity color 0:101
  #
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv6-address 2001:DB8:101::1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #
  return
  ```
* DeviceA configuration file
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
  #
  bgp 200
   router-id 4.4.4.4
   peer 192.168.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.2 enable
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
   ip address 192.168.2.1 255.255.255.0
  #
  bgp 300
   router-id 5.5.5.5
   peer 192.168.2.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.2.2 enable
  #
  return
  ```