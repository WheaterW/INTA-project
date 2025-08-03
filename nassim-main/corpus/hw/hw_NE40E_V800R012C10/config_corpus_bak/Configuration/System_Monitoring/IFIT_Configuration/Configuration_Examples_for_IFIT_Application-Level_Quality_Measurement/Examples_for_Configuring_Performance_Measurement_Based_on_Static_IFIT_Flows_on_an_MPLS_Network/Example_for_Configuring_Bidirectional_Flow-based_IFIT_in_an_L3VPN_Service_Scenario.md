Example for Configuring Bidirectional Flow-based IFIT in an L3VPN Service Scenario
==================================================================================

This section provides an example for configuring IFIT to implement hop-by-hop packet loss and delay measurement based on bidirectional flows on an L3VPN over MPLS network.

#### Networking Requirements

To meet users' higher requirements on service quality, IFIT is required on an L3VPN to monitor the packet loss rate and delay on links between PEs in real time. This enables timely responses to service quality deterioration. IFIT supports bidirectional flow-based performance measurement. A reverse flow instance is automatically generated based on the forward flow created on one device. On a live network, there are a large number of access devices but only few core-layer devices. Creating bidirectional flows on core-layer devices greatly reduces the configuration and maintenance workload.

On the L3VPN shown in [Figure 1](#EN-US_TASK_0293652551__fig_dc_vrp_ifit_cfg_001301), PE1 is a core-layer device, and PE2 is an access-layer device.

**Figure 1** Configuring bidirectional flow-based IFIT on an L3VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0293652554.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an L3VPN on each PE and the P. Specifically:
   1. Configure an IP address and a routing protocol for each involved interface so that all devices can communicate at the network layer. This example uses IS-IS as the routing protocol.
   2. Configure MPLS and public network tunnels to carry L3VPN services. In this example, SR-MPLS TE tunnels are used.
   3. Configure a VPN instance on each PE, enable the IPv4 address family for the instance, and bind the instance to the interface connecting the PE to a CE.
   4. Establish an MP-IBGP peer relationship between the PEs.
   5. Establish an EBGP peer relationship between each CE and PE pair for them to exchange routing information.
2. Configure basic 1588v2 functions to synchronize the clocks across all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0293652551__fig_dc_vrp_ifit_cfg_001301)
* MPLS LSR IDs on the PEs and P
* SRGB ranges on the PEs and P
* Name, VPN target, and RD of the VPN instance on each PE
* IFIT instance ID (1) and measurement interval (10s)
* Target flow's source IP address (10.11.1.1) and destination IP address (10.22.2.2) in the IFIT instance
* NMS's IPv4 address (192.168.100.100) and port number (10001), and reachable routes between the NMS and devices


#### Procedure

1. Configure an L3VPN on each PE and the P. For configuration details, see [Configuration Files](#EN-US_TASK_0293652551__section_05).
2. Configure 1588v2 to synchronize the clocks of the P and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0293652551__section_05).
3. Configure bidirectional flow-based IFIT for the link between PE1 and PE2.
   
   
   
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
   [*PE1-ifit-instance-1] measure-mode trace
   ```
   ```
   [*PE1-ifit-instance-1] interval 10
   ```
   ```
   [*PE1-ifit-instance-1] flow bidirectional source 10.11.1.1 destination 10.22.2.2 dscp 63 vpn-instance vpna
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
   Flow Type                               : bidirectional
   Source IP Address/Mask Length           : 10.11.1.1/32
   Destination IP Address/Mask Length      : 10.22.2.2/32
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Gtp                                     : disable
   Gtp TeId                                : --
   Dscp                                    : 63
   Interface                               : GigabitEthernet0/1/0
   vpn-instance                            : vpna
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
   [*PE2-ifit] encapsulation nexthop 1.1.1.9
   ```
   ```
   [*PE2-ifit] commit
   ```
   ```
   [~PE2-ifit] quit
   ```
   
   # Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) command to check the configuration and status of PE2.
   
   ```
   [~PE2] display ifit dynamic
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic
   Instance Id                             : 100
   Instance Type                           : instance
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Source IP Address/Mask Length           : 10.22.2.2/32
   Destination IP Address/Mask Length      : 10.11.1.1/32
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Gtp                                     : disable
   Gtp TeId                                : --
   Dscp                                    : 63
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
   Tunnel Type                             : --
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
   instance 1
    measure-mode trace
    interval 10
    flow bidirectional source 10.11.1.1 destination 10.22.2.2 dscp 63 vpn-instance vpna
    binding interface GigabitEthernet0/1/0 
  #
  tunnel-policy p1
   tunnel select-seq sr-te load-balance-number 1
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
    peer 10.2.1.1 as-number 65420
  #
  ifit
   node-id 2
   encapsulation nexthop 1.1.1.9
  #
  tunnel-policy p1
   tunnel select-seq sr-te load-balance-number 1
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