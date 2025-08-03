Example for Configuring Peer IP Address-based IFIT in an EVPN L3VPN Service Scenario
====================================================================================

This section provides an example for configuring IFIT to implement end-to-end packet loss and delay measurement based on the peer IP address on an EVPN L3VPN over MPLS network.

#### Networking Requirements

To transmit both Layer 2 and Layer 3 services on a network, deploy an EVPN to carry Layer 3 service traffic. The EVPN is called an EVPN Layer 3 virtual private network (L3VPN). To meet users' higher requirements on service quality, IFIT is required on an EVPN L3VPN to monitor the packet loss rate and delay on links between PEs in real time. This enables timely responses to service quality deterioration.

On the EVPN L3VPN shown in [Figure 1](#EN-US_TASK_0218010599__fig_dc_vrp_ifit_cfg_001301), service flows enter the network through PE1, traverse the P, and leave the network through PE2.

**Figure 1** Configuring peer IP address-based IFIT on an EVPN L3VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0218010600.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an EVPN L3VPN on each PE and the P. Specifically:
   1. Configure an IP address and a routing protocol for each involved interface so that all devices can communicate at the network layer. This example uses IS-IS as the routing protocol.
   2. Configure MPLS and public network tunnels to carry EVPN L3VPN services. In this example, MPLS LDP tunnels are used.
   3. Configure a VPN instance on each PE, enable the IPv4 address family for the instance, and bind the instance to the interface connecting the PE to a CE.
   4. Establish a BGP EVPN peer relationship between PEs.
   5. Establish an EBGP peer relationship between each PE and its connected CE.
2. Configure basic 1588v2 functions to synchronize the clocks across all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0218010599__fig_dc_vrp_ifit_cfg_001301)
* MPLS LSR IDs on the PEs and P
* Name, VPN target, and RD of the VPN instance on each PE
* IFIT instance ID (1) and measurement interval (10s)
* Peer IP address (3.3.3.9) of the IFIT instance
* NMS's IPv4 address (192.168.100.100) and port number (10001), and reachable routes between the NMS and devices


#### Procedure

1. Configure an EVPN L3VPN on each PE and the P. For configuration details, see [Configuration Files](#EN-US_TASK_0218010599__section_05).
2. Configure 1588v2 to synchronize the clocks of the P and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0218010599__section_05).
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
   [*PE1-ifit] encapsulation nexthop 3.3.3.9
   ```
   ```
   [*PE1-ifit] instance 1
   ```
   ```
   [*PE1-ifit-instance-1] measure-mode e2e
   ```
   ```
   [*PE1-ifit-instance-1] interval 10
   ```
   ```
   [*PE1-ifit-instance-1] flow unidirectional source any destination any vpn-instance vpna peer-ip 3.3.3.9
   ```
   ```
   [*PE1-ifit-instance-1] binding interface gigabitethernet 0/1/0
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
   Source IP Address/Mask Length           : any(IPv4)
   Destination IP Address/Mask Length      : any(IPv4)
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
   Interval                                : 10(s)
   Tunnel Type                             : MPLS
   Flow Match Priority                     : 0
   Peer IP                                 : 3.3.3.9
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
   [*PE1-telemetry-destination-group-ifit] ipv4-address 192.168.100.100 port 10001 protocol grpc
   ```
   ```
   [*PE1-telemetry-destination-group-ifit] quit
   ```
   ```
   [*PE1-telemetry] sensor-group ifit
   ```
   ```
   [*PE1-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-peer-ip-statistics/flow-peer-ip-statistic
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
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 1.1.1.9
  #               
  mpls
  #
  mpls ldp          
  #               
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
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
   mpls
   mpls ldp
   ptp enable
  #              
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 1
  #               
  bgp 100
   router-id 1.1.1.9         
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv4-family vpn-instance vpna
    peer 10.1.1.1 as-number 65410
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.9 enable
    peer 3.3.3.9 advertise irb 
  #
  ifit
   node-id 1
   encapsulation nexthop 3.3.3.9
   instance 1
    interval 10
    flow unidirectional source any destination any vpn-instance vpna peer-ip 3.3.3.9
    binding interface GigabitEthernet0/1/0 
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-peer-ip-statistics/flow-peer-ip-statistic
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
  #
  mpls ldp
  #               
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 172.16.1.2 255.255.255.0
   isis enable 1 
   mpls
   mpls ldp
   ptp enable 
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 172.17.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
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
    tnl-policy p1 evpn
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 3.3.3.9
  #               
  mpls            
  #
  mpls ldp
  #               
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
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
   mpls
   mpls ldp
   ptp enable
  #               
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1
  #               
  bgp 100 
   router-id 3.3.3.9        
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #                           
   ipv4-family vpn-instance vpna
    import-route direct 
    peer 10.2.1.1 as-number 65420
    advertise l2vpn evpn
  #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.9 enable
    peer 1.1.1.9 advertise irb
  #
  ifit
   node-id 2
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-peer-ip-statistics/flow-peer-ip-statistic
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