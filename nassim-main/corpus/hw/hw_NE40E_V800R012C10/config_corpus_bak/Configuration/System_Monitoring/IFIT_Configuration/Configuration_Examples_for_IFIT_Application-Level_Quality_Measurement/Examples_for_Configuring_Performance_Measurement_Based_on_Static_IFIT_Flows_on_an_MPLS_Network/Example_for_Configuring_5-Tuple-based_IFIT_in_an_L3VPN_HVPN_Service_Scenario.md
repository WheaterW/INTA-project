Example for Configuring 5-Tuple-based IFIT in an L3VPN HVPN Service Scenario
============================================================================

This section provides an example for configuring IFIT to implement hop-by-hop packet loss and delay measurement based on 5-tuple information on an L3VPN HVPN over MPLS network.

#### Networking Requirements

The L3VPN HVPN shown in [Figure 1](#EN-US_TASK_0203265099__fig_dc_vrp_ifit_cfg_001301) transmits voice services. Voice flows are symmetrical and bidirectional, and therefore one voice flow can be divided into two unidirectional service flows. The upstream service flow enters the network through the UPE, travels across the SPE, and leaves the network through the NPE. The downstream service flow enters the network through the NPE, also travels across the SPE, and leaves the network through the UPE.

To meet users' higher requirements on service quality, it is required that the packet loss rate and delay of the links between the UPE and NPE be monitored in real time so that the carrier can promptly respond to network issues if service quality deteriorates.

**Figure 1** Configuring 5-Tuple-based IFIT on an L3VPN HVPN  
![](figure/en-us_image_0217640939.png)

**Table 1** Interfaces connecting devices and their IP addresses
| Device (Role) | Interface Name | Interface | Remote Device (Role) | IP Address |
| --- | --- | --- | --- | --- |
| UPE | - | Loopback1 | - | 1.1.1.1/32 |
| interface1 | GE 0/1/0 | eNodeB | 192.168.2.1/24 |
| interface2 | GE 0/1/1 | SPE1 | 172.16.1.1/24 |
| interface3 | GE 0/1/2 | SPE2 | 172.16.2.1/24 |
| SPE1 | - | Loopback1 | - | 2.2.2.2/32 |
| interface1 | GE 0/1/1 | UPE | 172.16.1.2/24 |
| interface2 | GE 0/1/2 | NPE | 172.16.4.1/24 |
| interface3 | GE 0/1/3 | SPE2 | 172.16.3.1/24 |
| interface4 | GE 0/1/4 | BITS | 172.16.6.1/24 |
| SPE2 | - | Loopback1 | - | 3.3.3.3/32 |
| interface1 | GE 0/1/1 | NPE | 172.16.5.1/24 |
| interface2 | GE 0/1/2 | UPE | 172.16.2.2/24 |
| interface3 | GE 0/1/3 | SPE1 | 172.16.3.2/24 |
| NPE | - | Loopback1 | - | 4.4.4.4/32 |
| interface1 | GE 0/1/1 | SPE2 | 172.16.5.2/24 |
| interface2 | GE 0/1/2 | SPE1 | 172.16.4.2/24 |
| interface3 | GE 0/1/3 | EPC | 192.168.2.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an L3VPN HVPN on the UPE, SPE1, SPE2, and NPE. Specifically:
   1. Configure an IP address and a routing protocol for each involved interface so that all devices can communicate at the network layer. This example uses OSPF as the routing protocol.
   2. Configure MPLS and public network tunnels to carry L3VPN services. In this example, SR-MPLS TE tunnels are established between the UPE and each SPE, between SPEs, and between each SPE and the NPE.
   3. Create a VPN instance on the UPE and NPE and import the local direct routes on the UPE and NPE to their respective VPN instance routing tables.
   4. Establish MP-IBGP peer relationships between the UPE and each SPE and between the NPE and each SPE.
   5. Configure the SPEs as RRs and specify the UPE and NPE as RR clients.
   6. Configure VPN FRR on the UPE and NPE to improve network reliability.
2. Configure 1588v2 to synchronize the clocks of the UPE, SPEs, and NPE.
3. Configure packet loss and delay measurement on the UPE and NPE to collect packet loss rate and delay statistics at intervals. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * For upstream traffic in the HoVPN over MPLS scenario, an SPE functions as the ingress, and a VPN instance needs to be configured for the static IFIT flow.
   * For downstream traffic in the HoVPN over MPLS scenario or upstream/downstream traffic in the H-VPN over MPLS scenario, an SPE functions as the ingress, and no VPN instance needs to be configured for the static IFIT flow.
   * For upstream/downstream traffic in the HoVPN over SRv6 scenario, an SPE functions as the ingress, and a VPN instance needs to be configured for the static IFIT flow.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface listed in [Table 1](#EN-US_TASK_0203265099__tab_dc_vrp_ifit_cfg_001301)
* IGP type (OSPF), process ID (1), and area ID (0)
* Label switching router (LSR) IDs of the UPE (1.1.1.1), SPE1 (2.2.2.2), and SPE2 (3.3.3.3)
* Tunnel interface names (Tunnel11), tunnel IDs (100), and tunnel interface addresses (loopback interface addresses) for the tunnel interfaces between the UPE and SPE1
* Tunnel interface names (Tunnel12), tunnel IDs (200), and tunnel interface addresses (loopback interface addresses) for the tunnel interfaces between the UPE and SPE2
* Tunnel policy names (policy1) for the tunnels between the UPE and SPEs and tunnel selector names (BindTE) on the SPEs
* Names (vpna), RDs (100:1), and VPN targets (1:1) of the VPN instances on the UPE and NPE
* IFIT instance ID (1) and measurement interval (10s)
* Target flow's source IP address (10.1.1.1) and destination IP address (10.2.1.1)
* NMS's IPv4 address (192.168.100.100) and port number (10001), and reachable routes between the NMS and devices


#### Procedure

1. Configure an L3VPN HVPN on the UPE, SPE1, SPE2, and NPE. For configuration details, see [Configuration Files](#EN-US_TASK_0203265099__section_05).
2. Configure 1588v2 to synchronize the clocks of the UPE, SPE1, and NPE. For detailed configurations, see [Configuration Files](#EN-US_TASK_0203265099__section_05).
3. Configure hop-by-hop IFIT measurement for the link between the UPE and NPE.
   
   # Configure the UPE.
   ```
   <UPE> system-view
   ```
   ```
   [~UPE] ifit
   ```
   ```
   [*UPE-ifit] node-id 1
   ```
   ```
   [*UPE-ifit] encapsulation nexthop 2.2.2.2
   ```
   ```
   [*UPE-ifit] instance 1
   ```
   ```
   [*UPE-ifit-instance-1] measure-mode trace
   ```
   ```
   [*UPE-ifit-instance-1] interval 10
   ```
   ```
   [*UPE-ifit-instance-1] flow unidirectional source 10.1.1.1 destination 10.2.1.1 dscp 63 vpn-instance vpna
   ```
   ```
   [*UPE-ifit-instance-1] binding interface gigabitethernet 0/1/0
   ```
   ```
   [*UPE-ifit-instance-1] commit
   ```
   ```
   [~UPE-ifit-instance-1] quit
   ```
   ```
   [~UPE-ifit] quit
   ```
   
   # Run the [**display ifit static**](cmdqueryname=display+ifit+static) and [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) commands to check the UPE configuration and status.
   ```
   [~UPE] display ifit static instance 1
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
   ```
   [~UPE] display ifit dynamic-hop
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
   Interface                               : GigabitEthernet0/1/1
   Direction                               : transitOutput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable 
   Interval                                : 10(s)
   ```
   
   # Configure SPE1.
   ```
   <SPE1> system-view
   ```
   ```
   [~SPE1] ifit
   ```
   ```
   [*SPE1-ifit] node-id 3
   ```
   ```
   [*SPE1-ifit] encapsulation nexthop 4.4.4.4
   ```
   ```
   [*SPE1-ifit] commit
   ```
   ```
   [~SPE1-ifit] quit
   ```
   
   # Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) command to check the SPE1 configuration and status.
   ```
   [~SPE1] display ifit dynamic-hop
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
   Interface                               : GigabitEthernet0/1/2
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
   Interface                               : GigabitEthernet0/1/1
   Direction                               : transitInput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   ```
   
   # Configure the NPE.
   ```
   <NPE> system-view
   ```
   ```
   [~NPE] ifit
   ```
   ```
   [*NPE-ifit] node-id 2
   ```
   ```
   [*NPE-ifit] commit
   ```
   ```
   [~NPE-ifit] quit
   ```
   
   # Run the [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) command to check the NPE configuration and status.
   
   ```
   [~NPE] display ifit dynamic-hop
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
   Interface                               : GigabitEthernet0/1/3
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
   Interface                               : GigabitEthernet0/1/2
   Direction                               : transitInput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   ```
4. Configure the device to send statistics to the NMS through telemetry. The following uses the UPE as an example.
   
   
   ```
   [~UPE] telemetry
   ```
   ```
   [~UPE-telemetry] destination-group ifit
   ```
   ```
   [*UPE-telemetry-destination-group-ifit] ipv4-address 192.168.100.100 port 10001 protocol grpc
   ```
   ```
   [*UPE-telemetry-destination-group-ifit] quit
   ```
   ```
   [*UPE-telemetry] sensor-group ifit
   ```
   ```
   [*UPE-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
   ```
   ```
   [*UPE-telemetry-sensor-group-ifit-path] quit
   ```
   ```
   [*UPE-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   ```
   ```
   [*UPE-telemetry-sensor-group-ifit-path] quit
   ```
   ```
   [*UPE-telemetry-sensor-group-ifit] quit
   ```
   ```
   [*UPE-telemetry] subscription ifit
   ```
   ```
   [*UPE-telemetry-subscription-ifit] sensor-group ifit sample-interval 0
   ```
   ```
   [*UPE-telemetry-subscription-ifit] destination-group ifit
   ```
   ```
   [*UPE-telemetry-subscription-ifit] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure devices to send data using a secure TLS encryption mode. For details, see *Telemetry Configuration*.

#### Configuration Files

* UPE configuration file
  
  ```
  #                                                                               
  sysname UPE                                                                 
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
    tnl-policy policy1                                                            
    vpn-target 1:1 export-extcommunity                                            
    vpn-target 1:1 import-extcommunity                                            
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te                                        
   label advertise non-null                                        
  #
  segment-routing
  #
  interface GigabitEthernet0/1/0                                                 
   undo shutdown                                                                  
   ip binding vpn-instance vpna                                                   
   ip address 192.168.2.1 255.255.255.0                                             
   ptp enable
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 172.16.1.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
   ptp enable
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 172.16.2.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface LoopBack1                                                             
   ip address 1.1.1.1 255.255.255.255                                             
   ospf enable area 0.0.0.0                                        
   ospf prefix-sid absolute 16100
  #                                                                               
  explicit-path spe1
   next sid label 16300 type adjacency
  #
  explicit-path spe2
   next sid label 16400 type adjacency
  #
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 100                                                          
   mpls te reserved-for-binding                                                   
   mpls te signal-protocol segment-routing
   mpls te path explicit-path spe1
  #                                                                               
  interface Tunnel12                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te tunnel-id 200                                                          
   mpls te reserved-for-binding                                                   
   mpls te signal-protocol segment-routing
   mpls te path explicit-path spe2
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.1                                                              
   peer 2.2.2.2 as-number 100                                                     
   peer 2.2.2.2 connect-interface LoopBack1                                       
   peer 3.3.3.3 as-number 100                                                     
   peer 3.3.3.3 connect-interface LoopBack1                                       
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization
    peer 2.2.2.2 enable                                                           
    peer 3.3.3.3 enable                                                           
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2.2.2.2 enable                                                           
    peer 3.3.3.3 enable                                                           
   #                                                                              
   ipv4-family vpn-instance vpna                                                  
    import-route direct                                                           
    auto-frr                                                                      
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   segment-routing mpls
   segment-routing global-block 16000 20000
   area 0.0.0.0                                                                   
    network 1.1.1.1 0.0.0.0                                                       
    network 172.16.1.0 0.0.0.255                                                   
    network 172.16.2.0 0.0.0.255                                                   
    mpls-te enable                                                                
  #                                                                               
  ifit 
   node-id 1
   encapsulation nexthop 2.2.2.2                                                             
   instance 1
    measure-mode trace
    interval 10
    flow unidirectional source 10.1.1.1 destination 10.2.1.1 dscp 63 vpn-instance vpna
    binding interface GigabitEthernet0/1/0
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel11                              
   tunnel binding destination 3.3.3.3 te Tunnel12                              
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
* SPE1 configuration file
  
  ```
  #                                                                               
  sysname SPE1                                                                 
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
  tunnel-selector bindTE permit node 10                                           
   apply tunnel-policy policy1                                                    
  #                                                                               
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   label advertise non-null
  #
  segment-routing
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 172.16.1.2 255.255.255.0                                             
   mpls                                                                           
   mpls te  
   ptp enable
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 172.16.4.1 255.255.255.0                                             
   mpls
   mpls te
   ptp enable
  #                                                                               
  interface GigabitEthernet0/1/3                                                  
   undo shutdown                                                                  
   ip address 172.16.3.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                       
  #                                                                               
  interface GigabitEthernet0/1/4                                                  
   undo shutdown                                                                  
   ip address 172.16.6.1 255.255.255.0                                             
   ptp enable
  #                                                                               
  interface LoopBack1                                                             
   ip address 2.2.2.2 255.255.255.255
   ospf enable area 0.0.0.0
   ospf prefix-sid absolute 16200
  #
  explicit-path upe
   next sid label 16200 type adjacency
  #
  explicit-path npe
   next sid label 16400 type adjacency
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 1.1.1.1                                                            
   mpls te tunnel-id 100                                                          
   mpls te reserved-for-binding                                                   
   mpls te signal-protocol segment-routing
   mpls te path explicit-path upe
  #
  interface Tunnel12                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 4.4.4.4                                                            
   mpls te tunnel-id 200                                                          
   mpls te reserved-for-binding                                                   
   mpls te signal-protocol segment-routing
   mpls te path explicit-path npe
  #                                
  bgp 100                                                                         
   router-id 2.2.2.2                                                              
   peer 1.1.1.1 as-number 100                                                     
   peer 1.1.1.1 connect-interface LoopBack1                                       
   peer 3.3.3.3 as-number 100                                                     
   peer 3.3.3.3 connect-interface LoopBack1                                       
   peer 4.4.4.4 as-number 100                                                     
   peer 4.4.4.4 connect-interface LoopBack1                                       
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization
    peer 1.1.1.1 enable                                                           
    peer 3.3.3.3 enable                                                           
    peer 4.4.4.4 enable                                                           
   #                                                                              
   ipv4-family vpnv4                                                              
    undo policy vpn-target                                                        
    tunnel-selector bindTE                                                        
    peer 1.1.1.1 enable                                                           
    peer 1.1.1.1 reflect-client                                                   
    peer 1.1.1.1 next-hop-local                                                   
    peer 3.3.3.3 enable                                                           
    peer 4.4.4.4 enable                                                           
    peer 4.4.4.4 reflect-client                                                   
    peer 4.4.4.4 next-hop-local                                                   
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 172.16.1.0 0.0.0.255                                                   
    network 172.16.3.0 0.0.0.255                                                   
    network 172.16.4.0 0.0.0.255                                                   
    segment-routing mpls
    segment-routing global-block 16000 20000
  #                                                                               
  ifit
   node-id 3
   encapsulation nexthop 4.4.4.4
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel11 
   tunnel binding destination 4.4.4.4 te Tunnel12                             
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
* SPE2 configuration file
  
  ```
  #                                                                               
  sysname SPE2                                                                 
  #                                                                               
  tunnel-selector bindTE permit node 10                                           
   apply tunnel-policy policy1                                                    
  #                                                                               
  mpls lsr-id 3.3.3.3
  #                                        
  mpls                                                                            
   mpls te                                                                        
   label advertise non-null
  #
  segment-routing
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 172.16.5.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                       
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 172.16.2.2 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface GigabitEthernet0/1/3                                                  
   undo shutdown                                                                  
   ip address 172.16.3.2 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface LoopBack1                                                             
   ip address 3.3.3.3 255.255.255.255                                             
   ospf enable area 0.0.0.0
   ospf prefix-sid absolute 16200
  #
  explicit-path upe
   next sid label 16300 type adjacency
  #
  explicit-path npe
   next sid label 16400 type adjacency
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 1.1.1.1                                                            
   mpls te tunnel-id 100                                                          
   mpls te reserved-for-binding                                                   
   mpls te signal-protocol segment-routing
   mpls te path explicit-path upe
  #                                                                               
  interface Tunnel12                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 4.4.4.4                                                            
   mpls te tunnel-id 200                                                          
   mpls te reserved-for-binding                                                   
   mpls te signal-protocol segment-routing
   mpls te path explicit-path npe
  #                                                                               
  bgp 100                                                                         
   router-id 3.3.3.3                                                              
   peer 1.1.1.1 as-number 100                                                     
   peer 1.1.1.1 connect-interface LoopBack1                                       
   peer 2.2.2.2 as-number 100                                                     
   peer 2.2.2.2 connect-interface LoopBack1                                       
   peer 4.4.4.4 as-number 100                                                     
   peer 4.4.4.4 connect-interface LoopBack1                                       
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization
    peer 1.1.1.1 enable                                                           
    peer 2.2.2.2 enable                                                           
    peer 4.4.4.4 enable                                                           
   #                                                                              
   ipv4-family vpnv4                                                              
    undo policy vpn-target                                                        
    tunnel-selector bindTE                                                        
    peer 1.1.1.1 enable                                                           
    peer 1.1.1.1 reflect-client                                                   
    peer 1.1.1.1 next-hop-local                                                   
    peer 2.2.2.2 enable                                                           
    peer 4.4.4.4 enable                                                           
    peer 4.4.4.4 reflect-client                                                   
    peer 4.4.4.4 next-hop-local                                                   
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   segment-routing mpls
   segment-routing global-block 16000 20000
   area 0.0.0.0                                                                   
    network 3.3.3.3 0.0.0.0                                                       
    network 172.16.2.0 0.0.0.255                                                   
    network 172.16.3.0 0.0.0.255                                                   
    network 172.16.5.0 0.0.0.255                                                   
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1
   tunnel binding destination 1.1.1.1 te Tunnel11
   tunnel binding destination 4.4.4.4 te Tunnel12                              
  #                                                                               
  return
  ```
* NPE configuration file
  
  ```
  #
  sysname NPE
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
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
   mpls te
   label advertise non-null
  #
  segment-routing
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.5.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.4.2 255.255.255.0
   mpls
   mpls te
   ptp enable
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip binding vpn-instance vpna
   ip address 192.168.2.2 255.255.255.0
   mpls
   mpls te
   ptp enable
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   ospf enable area 0.0.0.0                                        
   ospf prefix-sid absolute 16300
  #                                                                               
  explicit-path spe1
   next sid label 16100 type adjacency
  #
  explicit-path spe2
   next sid label 16200 type adjacency
  #
  interface Tunnel11
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 100
   mpls te path explicit-path spe1
  #
  interface Tunnel12
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 200
   mpls te path explicit-path spe2
  # 
  bgp 100
   router-id 4.4.4.4
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    auto-frr
  #
  ospf 1
   area 0.0.0.0
   segment-routing mpls
   segment-routing global-block 16000 20000
    network 4.4.4.4 0.0.0.0
    network 172.16.4.0 0.0.0.255
    network 172.16.5.0 0.0.0.255
    mpls-te enable
  #
  ifit
   node-id 2
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel11                              
   tunnel binding destination 3.3.3.3 te Tunnel12                             
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