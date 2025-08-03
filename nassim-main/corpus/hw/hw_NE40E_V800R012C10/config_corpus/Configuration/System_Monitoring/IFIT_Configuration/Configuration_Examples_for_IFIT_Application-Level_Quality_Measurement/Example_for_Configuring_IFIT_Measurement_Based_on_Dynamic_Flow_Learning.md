Example for Configuring IFIT Measurement Based on Dynamic Flow Learning
=======================================================================

This section uses an L3VPN as an example to describe how to implement end-to-end packet loss and delay measurement through IFIT dynamic flow learning.

#### Networking Requirements

To meet users' higher requirements on service quality, IFIT is required on an L3VPN to monitor the packet loss rate and delay on links between PEs in real time. This enables timely responses to service quality deterioration. IFIT supports automatic learning of dynamic flows on the ingress by using the mask or exact match of the source or destination address. In addition, IFIT can flexibly monitor service quality in real time by configuring a learning whitelist.

[Figure 1](#EN-US_TASK_0319067886__fig_dc_vrp_ifit_cfg_001301) shows an L3VPN where service flows enter the network through PE1, traverse the P, and leave the network through PE2.

**Figure 1** Configuring IFIT measurement based on dynamic flow learning![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0319067887.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an L3VPN on the P and each PE. Specifically:
   1. Configure an IP address and a routing protocol for each interface so that all devices can communicate at the network layer. This example uses IS-IS as the routing protocol.
   2. Configure MPLS and public network tunnels to carry L3VPN services. In this example, SR-MPLS TE tunnels are used.
   3. Configure a VPN instance on each PE, enable the IPv4 address family for the instance, and bind the instance to the interface connecting the PE to a CE.
   4. Establish an MP-IBGP peer relationship between the PEs for them to exchange routing information.
   5. Establish an EBGP peer relationship between each CE and PE pair for them to exchange routing information.
2. Configure basic 1588v2 functions to synchronize the clocks across all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0319067886__fig_dc_vrp_ifit_cfg_001301)
* MPLS LSR IDs on the PEs and P
* SRGB ranges on the PEs and P
* Name, VPN target, and RD of the VPN instance on each PE
* Whitelist group (1) for IFIT performance measurement
* Source IP address (10.11.1.1) and destination IP address (10.22.2.2) of dynamic flows learned by IFIT
* NMS's IPv4 address (192.168.100.100) and port number (10001), and reachable routes between the NMS and devices


#### Procedure

1. Configure an L3VPN on each PE and the P. For configuration details, see [Configuration Files](#EN-US_TASK_0319067886__section_05).
2. Configure 1588v2 to synchronize the clocks of the P and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0319067886__section_05).
3. Configure IFIT dynamic flow learning on PE1.
   
   
   
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
   [*PE1-ifit] encapsulation nexthop 3.3.3.9
   ```
   ```
   [*PE1-ifit] whitelist-group 1
   ```
   ```
   [*PE1-ifit-whitelist-group-1] rule rule1 ipv4 source 10.11.1.1 32 destination 10.22.2.2 32
   ```
   ```
   [*PE1-ifit-whitelist-group-1] commit
   ```
   ```
   [~PE1-ifit-whitelist-group-1] quit
   ```
   ```
   [~PE1-ifit] flow-learning vpn-instance vpna
   ```
   ```
   [*PE1-ifit-vpn-instance-vpna] flow-learning unidirectional
   ```
   ```
   [*PE1-ifit-vpn-instance-vpna] flow-learning interface all whitelist-group 1
   ```
   ```
   [*PE1-ifit-vpn-instance-vpna] commit 
   ```
   ```
   [~PE1-ifit-vpn-instance-vpna] quit
   ```
   ```
   [~PE1-ifit] quit
   ```
   # Run the [**display ifit dynamic**](cmdqueryname=display+ifit+dynamic) command to check statistics about dynamic flows learned on PE1.
   ```
   [~PE1] display ifit dynamic
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic
   Instance Id                             : 10
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Source IP Address/Mask Length           : 10.11.1.1/32
   Destination IP Address/Mask Length      : 10.22.2.2/32
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Gtp                                     : disable
   Gtp TeId                                : --
   Dscp                                    : --
   Interface                               : GigabitEthernet0/1/0
   vpn-instance                            : vpna
   Measure State                           : enable 
   Loss Measure                            : enable
   Delay Measure                           : enable
   Delay Per packet Measure                : disable
   Disorder Measure                        : disable
   Gtpu Sequence Measure                   : disable
   Single Device Measure                   : disable
   Measure Mode                            : e2e
   Interval                                : 60(s)
   Tunnel Type                             : --
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
   Interface                               : GigabitEthernet0/1/0
   Direction                               : egress
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 60(s)
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
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.9
  #               
  mpls            
   mpls te
  #             
  explicit-path pe2
   next sid label 16200 type prefix
   next sid label 16300 type prefix
  #               
  segment-routing 
  #               
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 16000 20000
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
   ptp enable
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   isis enable 1
   ptp enable
  #              
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 16100 
  #               
  bgp 100         
   peer 3.3.3.9 as-number 100
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
   ipv4-family vpn-instance vpna
    import-route direct
    peer 10.1.1.1 as-number 65410
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.9
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path pe2
  #
  ifit
   node-id 1
   encapsulation nexthop 3.3.3.9
   whitelist-group 1
    rule rule1 ipv4 source 10.11.1.1 32 destination 10.22.2.2 32
   flow-learning vpn-instance vpna
    flow-learning unidirectional
    flow-learning interface all whitelist-group 1
  #
  tunnel-policy p1
   tunnel select-seq sr-te load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
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
  mpls lsr-id 2.2.2.9
  #               
  mpls            
   mpls te        
  #               
  segment-routing 
  #               
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 16000 20000
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 172.16.1.2 255.255.255.0
   isis enable 1 
   ptp enable 
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 172.17.1.1 255.255.255.0
   isis enable 1
   ptp enable  
  # 
  interface GigabitEthernet0/3/0                                                  
   undo shutdown                                                                  
   ip address 172.18.1.1 255.255.255.0                                             
   ptp enable
  # 
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 16200 
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
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.9
  #               
  mpls            
   mpls te  
  #
  explicit-path pe1
   next sid label 16200 type prefix
   next sid label 16100 type prefix
  #               
  segment-routing 
  #               
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0003.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 16000 20000
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.2 255.255.255.0
   ptp enable
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 172.17.1.2 255.255.255.0
   isis enable 1  
   ptp enable
  #               
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 16300
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.9
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path pe1 
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
   ipv4-family vpn-instance vpna
    import-route direct 
    peer 10.2.1.1 as-number 65420
  #
  ifit
   node-id 2
  #
  tunnel-policy p1
   tunnel select-seq sr-te load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
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
  interface LoopBack1
   ip address 10.11.1.1 255.255.255.255
  #
  bgp 65410
   peer 10.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.2 enable
    network 10.11.1.1 255.255.255.255
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
  interface LoopBack1
   ip address 10.22.2.2 255.255.255.255
  #
  bgp 65420
   peer 10.2.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 10.2.1.2 enable
    network 10.22.2.2 255.255.255.255
  #
  return
  ```