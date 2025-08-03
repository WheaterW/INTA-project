Example for Configuring 5-Tuple-based IFIT on a G-SRv6 Network
==============================================================

This section provides an example for configuring IFIT to implement hop-by-hop packet loss and delay measurement on a G-SRv6 network.

#### Networking Requirements

G-SRv6 allows SRHs to carry shorter G-SIDs to optimize SRv6 header overheads, optimizing SRv6 performance and facilitating large-scale SRv6 deployment. To meet users' higher requirements on service quality, IFIT is required on a G-SRv6 network to monitor the packet loss rate and delay on links between PEs in real time. This enables timely responses to service quality deterioration. On the network shown in [Figure 1](#EN-US_TASK_0000001277072981__fig3691666259), PE1, P1, P2, and PE2 are in the same AS. It is required that IS-IS be configured for these devices to achieve IPv6 network connectivity, a bidirectional SRv6 TE Policy be deployed between PE1 and PE2 to carry L3VPNv4 services, and SRH compression be performed to reduce the SRv6 header size.

**Figure 1** Configuring IFIT on a G-SRv6 network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001430598013.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an L3VPNv4 over SRv6 TE Policy on PE1, P1, P2, and PE2. Specifically:
   1. Enable IPv6 forwarding and configure an IPv6 address for each involved interface on PE1, P1, P2, and PE2.
   2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on PE1, P1, P2, and PE2.
   3. Configure an IPv4 L3VPN instance on each PE and bind the IPv4 L3VPN instance to an access-side interface.
   4. Establish an EBGP peer relationship between each PE and its connected CE.
   5. Establish a BGP VPNv4 peer relationship between the PEs.
   6. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, P1, P2, and PE2. In addition, configure PE1 and PE2 to advertise VPN routes carrying SIDs.
   7. Deploy an SRv6 TE Policy between PE1 and PE2.
   8. Configure a tunnel policy on PE1 and PE2 to import VPN traffic.
2. Configure basic 1588v2 functions to synchronize clocks among all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0000001277072981__fig3691666259)
* IPv6 address of each interface on PE1, P1, P2, and PE2
* IS-IS process ID of each device (PE1, P1, P2, and PE2)
* IS-IS level of each device (PE1, P1, P2, and PE2)
* VPN instance names, RDs, and RTs on PE1 and PE2
* IFIT instance ID (1) and measurement interval (10s)
* Target flow's source IP address (10.1.1.1) and destination IP address (10.2.1.1)
* NMS's IPv6 address (2001:db8:101::1) and port number (10001), and reachable routes between the NMS and device


#### Procedure

1. Configure L3VPNv4 over SRv6 TE Policy on PE1, P1, P2, and PE2. For configuration details, see [Configuration Files](#EN-US_TASK_0000001277072981__section_05).
2. Configure 1588v2 to synchronize the clocks of the P and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001277072981__section_05).
3. Configure hop-by-hop IFIT measurement for the link between PE1 and PE2.
   
   
   
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
   [*PE1-ifit] instance-ht16 1
   ```
   ```
   [*PE1-ifit-instance-ht16-1] measure-mode trace
   ```
   ```
   [*PE1-ifit-instance-ht16-1] interval 10
   ```
   ```
   [*PE1-ifit-instance-ht16-1] flow unidirectional source 10.1.1.1 destination 10.2.1.1 dscp 63 vpn-instance vpna
   ```
   ```
   [*PE1-ifit-instance-ht16-1] binding interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-ifit-instance-ht16-1] delay-measure enable
   ```
   ```
   [*PE1-ifit-instance-ht16-1] commit
   ```
   ```
   [~PE1-ifit-instance-ht16-1] quit
   ```
   ```
   [~PE1-ifit] quit
   ```
   # Run the [**display ifit static**](cmdqueryname=display+ifit+static) and [**display ifit dynamic-hop**](cmdqueryname=display+ifit+dynamic-hop) commands to check the configuration and status of PE1.
   ```
   [~PE1] display ifit static instance-ht16 1
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : static
   Instance Id                             : 1
   Instance Name                           : 1
   Instance Type                           : instance-ht16 
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1 
   Flow Type                               : unidirectional
   Source IP Address/Mask Length           : 10.1.1.1/32
   Destination IP Address/Mask Length      : 10.2.1.1/32
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Dscp                                    : 63
   Interface                               : GigabitEthernet0/2/0
   vpn-instance                            : vpna
   Measure State                           : enable
   Loss Measure                            : enable
   Delay Measure                           : enable
   Measure Mode                            : trace
   Interval                                : 10(s)
   Tunnel Type                             : SRv6
   ```
   ```
   [~PE1] display ifit dynamic-hop
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : dynamic-hop
   Instance Id                             : 4
   Instance Type                           : instance-ht16
   Flow Id                                 : 1572865
   Flow Monitor Id                         : 524289
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : GigabitEthernet0/1/0
   Direction                               : transitOutput
   Loss Measure                            : enable
   Delay Measure                           : enable 
   Interval                                : 10(s)
   ```
   
   # Enable IFIT on P1, P2, and PE2. The configuration on P1 is used as an example.
   ```
   <P1> system-view
   ```
   ```
   [~P1] ifit
   ```
   ```
   [*P1-ifit] node-id 3
   ```
   ```
   [*P1-ifit] commit
   ```
   ```
   [~P1-ifit] quit
   ```
4. Configure the device to send statistics to the NMS through telemetry. The following uses PE1 as an example.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The sampling interval configured using the [**sensor-group**](cmdqueryname=sensor-group) command must be a non-zero value. If the sampling interval is set to a value greater than 10 times the instance measurement interval, sampling is performed at an interval that is 10 times the instance measurement interval.
   
   
   
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
   [*PE1-telemetry-sensor-group-ifit] sensor-path insuitoam:flow-info/flow-entry
   ```
   ```
   [*PE1-telemetry-sensor-group-ifit-path] quit
   ```
   ```
   [*PE1-telemetry-sensor-group-ifit] sensor-path insuitoam:measure-report/report
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
   [*PE1-telemetry-subscription-ifit] sensor-group ifit sample-interval 10
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
    tnl-policy p1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity     
  #               
  segment-routing ipv6                                       
   encapsulation source-address 2001:DB8:1::1                
   locator PE1 ipv6-prefix 2001:DB8:100:1:: 64 compress block 48 compress-static 8 static 32 
    opcode compress ::12 end psp-usp-usd                     
    opcode ::55 end-op                                       
   srv6-te-policy locator PE1                                
   segment-list list1                                        
    index 5 sid ipv6 2001:DB8:100:2:22:: compress block 48   
    index 10 sid ipv6 2001:DB8:100:3:33:: compress block 48  
    index 15 sid ipv6 2001:DB8:100:4:45:: compress block 48  
   srv6-te policy policy1 endpoint 2001:DB8:4::4 color 101   
    candidate-path preference 100                            
     segment-list list1 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1 auto-sid-disable
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
   ip binding vpn-instance vpna
   ip address 10.11.1.1 255.255.255.0
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #               
  bgp 100                                                    
   router-id 1.1.1.1                                         
   peer 2001:DB8:4::4 as-number 100                          
   peer 2001:DB8:4::4 connect-interface LoopBack1            
   #                                                         
   ipv4-family unicast                                       
    undo synchronization                                     
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:4::4 enable
    peer 2001:DB8:4::4 route-policy p1 import
    peer 2001:DB8:4::4 prefix-sid
   #
   ipv4-family vpn-instance vpna                             
    import-route direct
    segment-routing ipv6 locator PE1                    
    segment-routing ipv6 traffic-engineer best-effort  
    peer 10.11.1.2 as-number 65410                                     
  #
  ifit
   node-id 1
   instance-ht16 1
    measure-mode trace
    interval 10
    flow unidirectional source 10.1.1.1 destination 10.2.1.1 dscp 63 vpn-instance vpna
    binding interface Gigabitethernet0/2/0
    delay-measure enable
  # 
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
    sensor-path insuitoam:flow-info/flow-entry
    sensor-path insuitoam:measure-report/report
   #
   destination-group ifit
    ipv6-address 2001:DB8:101::1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 10
    destination-group ifit
  #               
  return 
  ```
* P1 configuration file
  
  ```
  #
  sysname P1
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
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator P1 ipv6-prefix 2001:DB8:100:2:: 64 compress block 48 compress-static 8 static 32
    opcode compress ::22 end psp-usp-usd-coc 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P1 auto-sid-disable
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
   ipv6 address 2001:DB8:20::3/64
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #
  ifit
   node-id 3
  #
  telemetry
   #
   sensor-group ifit
    sensor-path insuitoam:flow-info/flow-entry
    sensor-path insuitoam:measure-report/report
   #
   destination-group ifit
    ipv6-address 2001:DB8:101::1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 10
    destination-group ifit
  #               
  return 
  ```
* P2 configuration file
  ```
  #
  sysname P2
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator P2 ipv6-prefix 2001:DB8:100:3:: 64 compress block 48 compress-static 8 static 32
    opcode compress ::33 end psp-usp-usd-coc 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P2 auto-sid-disable
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
   ipv6 enable    
   ipv6 address 2001:DB8:30::1/64
   isis ipv6 enable 1
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #
  ifit
   node-id 4
  #
  telemetry
   #
   sensor-group ifit
    sensor-path insuitoam:flow-info/flow-entry
    sensor-path insuitoam:measure-report/report
   #
   destination-group ifit
    ipv6-address 2001:DB8:101::1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 10
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
    tnl-policy p1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity     
  #               
  segment-routing ipv6                                       
   encapsulation source-address 2001:DB8:4::4                
   locator PE2 ipv6-prefix 2001:DB8:100:4:: 64 compress block 48 compress-static 8 static 32
    opcode compress ::45 end psp-usp-usd                     
    opcode ::66 end-op                                       
   srv6-te-policy locator PE2                                
   segment-list list1                                        
    index 5 sid ipv6 2001:DB8:100:3:33:: compress block 48   
    index 10 sid ipv6 2001:DB8:100:2:22:: compress block 48  
    index 15 sid ipv6 2001:DB8:100:1:12:: compress block 48  
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101   
    candidate-path preference 100                            
     segment-list list1 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:30::2/64
   isis ipv6 enable 1
   ptp enable
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.22.1.1 255.255.255.0
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:4::4/128
   isis ipv6 enable 1
  #               
  bgp 100                                                    
   router-id 4.4.4.4                                         
   peer 2001:DB8:1::1 as-number 100                          
   peer 2001:DB8:1::1 connect-interface LoopBack1            
   #                                                         
   ipv4-family unicast                                       
    undo synchronization                                     
   # 
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy p1 import
    peer 2001:DB8:1::1 prefix-sid
   #
   ipv4-family vpn-instance vpna                             
    import-route direct
    segment-routing ipv6 locator PE2                   
    segment-routing ipv6 traffic-engineer best-effort   
    peer 10.22.1.2 as-number 65420
  #
  ifit
   node-id 2
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
    sensor-path insuitoam:flow-info/flow-entry
    sensor-path insuitoam:measure-report/report
   #
   destination-group ifit
    ipv6-address 2001:DB8:101::1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 10
    destination-group ifit
  #               
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #               
  interface  GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.11.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 11.1.1.1 32
  #               
  bgp 65410       
   router-id 11.1.1.1
   peer 10.11.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.11.1.1 enable
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
   ip address 10.22.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 22.2.2.2 32
  #               
  bgp 65420       
   router-id 22.2.2.2
   peer 10.22.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.22.1.1 enable
  #
  return
  ```