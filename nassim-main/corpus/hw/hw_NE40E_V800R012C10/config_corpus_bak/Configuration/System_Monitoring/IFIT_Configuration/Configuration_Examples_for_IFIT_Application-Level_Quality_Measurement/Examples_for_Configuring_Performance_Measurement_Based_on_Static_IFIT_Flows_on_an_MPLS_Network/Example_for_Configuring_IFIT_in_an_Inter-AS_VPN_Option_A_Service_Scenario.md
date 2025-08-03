Example for Configuring IFIT in an Inter-AS VPN Option A Service Scenario
=========================================================================

This section provides an example for configuring IFIT to implement hop-by-hop packet loss and delay measurement in an inter-AS VPN Option A scenario.

#### Networking Requirements

To meet users' higher requirements on service quality, IFIT is required in the inter-AS Option A scenario to monitor the packet loss rate and delay of links between PEs in real time. This enables timely responses to service quality deterioration. As a basic BGP/MPLS IP VPN application in inter-AS scenarios, Option A does not require special inter-AS configuration, nor does it require MPLS to run between ASBRs. In this mode, the ASBRs of two ASs directly connect to each other and function as PEs in their own ASs. Each ASBR views the peer ASBR as its CE, creates a VPN instance for each VPN, and advertises IPv4 routes to the peer ASBR through EBGP.

In the inter-AS VPN Option A scenario shown in [Figure 1](#EN-US_TASK_0000001158610113__fig_dc_vrp_mpls-l3vpn-v4_cfg_011101), CE1 and CE2 belong to the same VPN. CE1 is connected to PE1 in AS 100, and CE2 is connected to PE2 in AS 200. Inter-AS BGP/MPLS IP VPN is implemented through Option A. Service flows enter the network through PE1, traverse ASBR1 and ASBR2, and leave the network through PE2.

**Figure 1** Configuring IFIT in inter-AS VPN Option A scenarios![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0000001112631530.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure inter-AS VPN Option A. Specifically:
   1. Establish an EBGP peer relationship between each PE and its connected CE.
   2. Establish an MP-IBGP peer relationship between the ASBR and PE in the same AS.
   3. Create a VPN instance on each ASBR, bind the VPN instance to the interface connecting each ASBR to the other ASBR, and establish an EBGP peer relationship between ASBRs.
2. Configure basic 1588v2 functions to synchronize the clocks across all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0000001158610113__fig_dc_vrp_mpls-l3vpn-v4_cfg_011101)
* MPLS LSR IDs of the PEs and ASBRs
* Name, VPN target, and RD of the VPN instance on each PE and ASBR
* IFIT instance ID (1) and measurement interval (10s)
* Target flow's source IP address (11.11.11.11) and destination IP address (22.22.22.22) in the IFIT instance
* NMS's IPv4 address (192.168.100.100) and port number (10001), and reachable routes between the NMS and devices


#### Procedure

1. Configure inter-AS VPN Option A. For configuration details, see [Configuration Files](#EN-US_TASK_0000001158610113__section_05).
2. Configure 1588v2 to synchronize the clocks of devices. For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001158610113__section_05).
3. Configure hop-by-hop IFIT measurement for the inter-AS Option A link between PE1 and PE2.
   
   
   
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
   [*PE1-ifit] encapsulation nexthop 2.2.2.9
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
   [*PE1-ifit-instance-1] flow unidirectional source 11.11.11.11 destination 22.22.22.22 dscp 63 vpn-instance vpn1
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
   # Run the [**display ifit static**](cmdqueryname=display+ifit+static) and [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) commands to check the configuration and status of PE1.
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
   Source IP Address/Mask Length           : 11.11.11.11/32
   Destination IP Address/Mask Length      : 22.22.22.22/32
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Gtp                                     : disable
   Gtp TeId                                : --
   Dscp                                    : 63
   Interface                               : GigabitEthernet0/2/0
   vpn-instance                            : vpn1
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
   ```
   [~PE1] display ifit dynamic-hop
   ```
   ```
   2020-01-14 17:24:39.28 +08:00
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 514
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : GigabitEthernet0/1/0
   Direction                               : transitOutput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   ```
   
   # Enable IFIT on ASBR1.
   ```
   <ASBR1> system-view
   ```
   ```
   [~ASBR1] ifit
   ```
   ```
   [*ASBR1-ifit] node-id 3
   ```
   ```
   [*ASBR1-ifit] commit
   ```
   ```
   [~ASBR1-ifit] quit
   ```
   
   # Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) command to check the configuration and status of ASBR1.
   
   ```
   [~ASBR1] display ifit dynamic-hop
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 6
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
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 7
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
   ```
   # Enable IFIT and IFIT mapping in the inbound direction on ASBR2.
   ```
   <ASBR2> system-view
   ```
   ```
   [~ASBR2] ifit
   ```
   ```
   [*ASBR2-ifit] node-id 2
   ```
   ```
   [*ASBR2-ifit] encapsulation nexthop 4.4.4.9
   ```
   ```
   [*ASBR2-ifit] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/2/0
   ```
   ```
   [~ASBR2-GigabitEthernet0/2/0] ifit ingress mapping enable
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] commit
   ```
   ```
   [~ASBR2-GigabitEthernet0/2/0] quit
   ```
   
   # Enable IFIT mapping in the outbound direction on ASBR1.
   ```
   [~ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] ifit egress mapping enable
   Warning: If the IFIT ingress mapping is not configured on the peer end, this operation could cause the abnormal data reception on the receiving end. Continue? [Y/N]:y
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * You are advised to configure IFIT mapping in the inbound direction and then in the outbound direction. Otherwise, traffic may be interrupted.
   * After IFIT mapping in the outbound direction is configured, the instance in the egress direction starts to age.
   
   # Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) command to check the configuration and status of ASBR1.
   
   ```
   [~ASBR1] display ifit dynamic-hop
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 6
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
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 8
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
   Instance Id                             : 7
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
   ```
   # Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) command to check the configuration and status of ASBR2.
   ```
   [~ASBR2] display ifit dynamic-hop
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 5
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : GigabitEthernet0/1/0
   Direction                               : transitOutput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 4
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : GigabitEthernet0/2/0
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
   [*PE2-ifit] node-id 4
   ```
   ```
   [*PE2-ifit] commit
   ```
   ```
   [~PE2-ifit] quit
   ```
4. Configure the device to send statistics to the NMS through telemetry. The following uses PE1 as an example.
   
   
   ```
   [~PE1] telemetry
   ```
   ```
   [~PE1-telemetry] destination-group ifit
   ```
   ```
   [*PE1-telemetry-destination-group-ifit] ipv4-address 192.168.100.100 port 10001 protocol grpc
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
   mpls
   mpls ldp
   ptp enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.1.1.2 255.255.255.0
   ptp enable
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  bgp 100
   peer 2.2.2.9 as-number 100
   peer 2.2.2.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.9 enable
  #
   ipv4-family vpn-instance vpn1
    peer 10.1.1.1 as-number 65001
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 10.10.1.0 0.0.0.255
  #
  ifit 
   node-id 1
   encapsulation nexthop 2.2.2.9                                                             
   instance 1
    measure-mode trace
    interval 10
    flow unidirectional source 11.11.11.11 destination 22.22.22.22 dscp 63 vpn-instance vpn1
    binding interface GigabitEthernet0/2/0
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv4-address 192.168.100.100 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
   mpls
   mpls ldp
   ptp enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 12.12.12.1 255.255.255.0
   ptp enable
   ifit egress mapping enable
  # 
  interface GigabitEthernet0/3/0                                                  
   undo shutdown                                                                  
   ip address 12.12.12.3 255.255.255.0                                             
   ptp enable
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  bgp 100
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.9 enable
  #
   ipv4-family vpn-instance vpn1
    peer 12.12.12.2 as-number 200
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 10.10.1.0 0.0.0.255
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
    ipv4-address 192.168.100.100 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:2
    apply-label per-instance
    vpn-target 2:2 export-extcommunity
    vpn-target 2:2 import-extcommunity
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.40.1.1 255.255.255.0
   mpls
   mpls ldp
   ptp enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 12.12.12.2 255.255.255.0
   ptp enable
   ifit ingress mapping enable
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
  #
  bgp 200
   peer 4.4.4.9 as-number 200
   peer 4.4.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.9 enable
  #
   ipv4-family vpn-instance vpn1
    peer 12.12.12.1 as-number 100
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 10.40.1.0 0.0.0.255
  #
  ifit
   node-id 2
   encapsulation nexthop 4.4.4.9
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv4-address 192.168.100.100 port 10001 protocol grpc
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 2:2 export-extcommunity
    vpn-target 2:2 import-extcommunity
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.2.1.2 255.255.255.0
   ptp enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.40.1.2 255.255.255.0
   mpls
   mpls ldp
   ptp enable
  #
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
  #
  bgp 200
   peer 3.3.3.9 as-number 200
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.9 enable
  #
   ipv4-family vpn-instance vpn1
    peer 10.2.1.1 as-number 65002
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.9 0.0.0.0
    network 10.40.1.0 0.0.0.255
  #
  ifit
   node-id 4
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv4-address 192.168.100.100 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface Loopback 1
   undo shutdown
   ip address 11.11.11.11 255.255.255.255
  #
  bgp 65001
   peer 10.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.2 enable
    network 11.11.11.11 255.255.255.255
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
   sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
  #
  interface Loopback 1
   undo shutdown
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65002
   peer 10.2.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    peer 10.2.1.2 enable
    network 22.22.22.22 255.255.255.255
  #
  return
  ```