Example for Configuring Peer Locator-based IFIT in an EVPN VPWS Service Scenario
================================================================================

This section provides an example for configuring IFIT to implement hop-by-hop packet loss and delay measurement based on the peer locator on an EVPN VPWS over SRv6 network.

#### Networking Requirements

EVPN VPWS over SRv6 uses public network SRv6 tunnels to carry EVPN VPWS VPN services. To meet users' higher requirements on service quality, IFIT is required on an EVPN VPWS over SRv6 network to monitor the packet loss rate and delay of links between PEs in real time. This enables timely responses to service quality deterioration.

On the EVPN VPWS over SRv6 network shown in [Figure 1](#EN-US_TASK_0289208125__fig_dc_vrp_ifit_cfg_001301), service flows enter the network through PE1, traverse the P, and leave the network through PE2.

**Figure 1** Configuring peer locator-based IFIT on an EVPN VPWS over SRv6 network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001379463186.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an EVPN VPWS over SRv6 network on each PE and the P. Specifically:
   1. Enable IPv6 forwarding on each device and configure IPv6 addresses for involved interfaces.
   2. Enable IS-IS, configure a level, and specify a network entity on each device.
   3. Configure EVPN VPWS and EVPL instances on each PE and bind access-side sub-interfaces to the EVPL instances.
   4. Establish a BGP EVPN peer relationship between PEs.
   5. Configure SRv6 BE on PEs.
2. Configure basic 1588v2 functions to synchronize clocks among all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface as listed in [Figure 1](#EN-US_TASK_0289208125__fig_dc_vrp_ifit_cfg_001301)
* EVPN instance name (evrf1)
* RD and RT values of the EVPN instance: 100:1 and 1:1
* IFIT instance ID (1) and measurement interval (10s)
* Peer locator (2001:db8:40::1/64) of the IFIT instance
* NMS's IPv6 address (2001:db8:101::1) and port number (10001), and reachable routes between the NMS and device


#### Procedure

1. Configure an EVPN VPWS over SRv6 network on each PE and the P. For configuration details, see [Configuration Files](#EN-US_TASK_0289208125__section_05).
2. Configure 1588v2 to synchronize the clocks of the P and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0289208125__section_05).
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
   [*PE1-ifit-instance-1] flow unidirectional evpl-instance 1 peer-locator 2001:DB8:40::1 64
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
   Source IP Address/Mask Length           : any
   Destination IP Address/Mask Length      : any
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Gtp                                     : disable
   Gtp TeId                                : --
   Dscp                                    : --
   Interface                               : GigabitEthernet0/2/0
   evpl-instance                           : 1
   Measure State                           : enable
   Loss Measure                            : enable
   Delay Measure                           : enable
   Delay Per packet Measure                : disable
   Disorder Measure                        : disable
   Gtpu Sequence Measure                   : disable
   Single Device Measure                   : disable
   Measure Mode                            : trace
   Interval                                : 10(s)
   Tunnel Type                             : SRv6
   Flow Match Priority                     : 0
   Peer Locator                            : 2001:DB8:40::1/64
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
4. Configure the device to send statistics to the NMS through telemetry. The following uses PE1 as an example.
   
   
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
   [*PE1-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-locator-statistics/flow-locator-statistic
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
  evpn vpn-instance evrf1 vpws
   route-distinguisher 100:1
   segment-routing ipv6 best-effort
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 100 remote-service-id 200
   segment-routing ipv6 locator PE1 
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1 ipv6-prefix 2001:DB8:100::1 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ptp enable
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   evpl instance 1
  #
  interface LoopBack1
   ipv6 enable
   ip address 1.1.1.1 255.255.255.255
   ipv6 address 2001:DB8:1::1/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
  #
  evpn source-address 1.1.1.1
  #
  ifit
   node-id 1                                                               
   instance 1
    measure-mode trace
    interval 10
    flow unidirectional evpl-instance 1 peer-locator 2001:DB8:40::1 64
    binding interface GigabitEthernet0/2/0
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-locator-statistics/flow-locator-statistic
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
   ipv6 address 2001:DB8:10::2/64
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:30::1/64
   ptp enable
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   isis ipv6 enable 1
  #
  ifit
   node-id 3
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-locator-statistics/flow-locator-statistic
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
  evpn vpn-instance evrf1 vpws
   route-distinguisher 100:1
   segment-routing ipv6 best-effort
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 200 remote-service-id 100
   segment-routing ipv6 locator PE2 
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator PE2 ipv6-prefix 2001:DB8:40::1 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ptp enable
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   evpl instance 1
  #
  interface LoopBack1
   ipv6 enable
   ip address 3.3.3.3 255.255.255.255
   ipv6 address 2001:DB8:3::3/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 3.3.3.3
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
  #
  evpn source-address 3.3.3.3
  #
  ifit
   node-id 2
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-locator-statistics/flow-locator-statistic
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