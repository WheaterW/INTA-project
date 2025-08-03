Example for Configuring IFIT Based on Multicast Source +Multicast Group on a BIERv6 Network
===========================================================================================

This section provides an example for configuring IFIT to implement end-to-end packet loss and delay measurement on an MVPNv4 over BIERv6 network.

#### Networking Requirements

MVPNv4 over BIERv6 uses BIERv6 as a bearer tunnel, encapsulates VPN IP multicast traffic using BIERv6, and transmits the traffic over a VPN in multicast mode. To meet users' higher requirements on service quality, IFIT is required on a BIERv6 network to monitor the packet loss rate and delay on links between PEs in real time. This enables timely responses to service quality deterioration. [Figure 1](#EN-US_TASK_0000001384483196__fig35284409229) shows the networking.

**Figure 1** Configuring IFIT on an MVPNv4 over BIERv6 network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 4 represent GE0/1/0, GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](figure/en-us_image_0000001434894569.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure MVPNv4 over BIERv6 on PE1, the P, PE2, and PE3. Specifically:
   1. (Optional) Configure L3VPNv4 over SRv6 and ensure that the unicast VPN runs properly. If the unicast network has been configured, skip this step.
   2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on PE1, PE2, PE3, and the P.
   3. Establish BGP MVPN peer relationships between PEs.
   4. Configure multicast traffic forwarding over a BIERv6 I-PMSI tunnel.
   5. Enable the BIERv6 S-PMSI tunnel function and configure switching criteria.
   6. Enable PIM on PEs.
2. Configure basic 1588v2 functions to synchronize the clocks across all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0000001384483196__fig35284409229)
* ID (1) of the public network IS-IS process, in a Level-2 area
* VPN instance name (vpna) on PE1, PE2, and PE3
* PE2's BFR-ID (2), PE3's BFR-ID (3), sub-domain ID (0), BSL (256), and Max-SI (0)
* IFIT instance ID (1) and measurement interval (10s)
* Multicast source address (192.168.11.0) and multicast group address (225.1.1.0) of the target flow in the IFIT instance
* NMS's IPv6 address (2001:db8:101::1) and port number (10001), and reachable routes between the NMS and device


#### Procedure

1. Configure L3VPNv4 over SRv6 on PE1, the P, PE2, and PE3. For configuration details, see [Configuration Files](#EN-US_TASK_0000001384483196__section_05).
2. Configure 1588v2 to synchronize the clocks of the P and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001384483196__section_05).
3. Configure end-to-end IFIT measurement for the link between PE1 and PE2.
   
   
   
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
   [*PE1-ifit-instance-ht16-1] interval 10
   ```
   ```
   [*PE1-ifit-instance-ht16-1] flow unidirectional source 192.168.11.0 group 225.1.1.0 vpn-instance vpna
   ```
   ```
   [*PE1-ifit-instance-ht16-1] binding interface gigabitethernet 0/1/1
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
   # Run the [**display ifit multicast**](cmdqueryname=display+ifit+multicast) command to check the configuration and status of PE1.
   ```
   [~PE1] display ifit multicast source 192.168.11.0 group 225.1.1.0
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : static
   Instance Id                             : 1
   Instance Name                           : 1
   Instance Type                           : instance-ht16
   Flow Id                                 : 1310721
   Flow Monitor Id                         : 262145
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Multicast Source Address                : 192.168.11.0
   Multicast Group Address                 : 225.1.1.0
   Interface                               : GigabitEthernet0/1/1
   Vpn-instance                            : vpna
   Measure State                           : enable
   Loss Measure                            : enable
   Delay Measure                           : enable
   Measure Mode                            : e2e
   Interval                                : 10(s)
   ```
   
   # Enable IFIT on PE2.
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
   Instance Id                             : 4
   Instance Type                           : instance-ht16
   Flow Id                                 : 1310721
   Flow Monitor Id                         : 262145
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Interface                               : --
   Direction                               : egress
   Loss Measure                            : enable
   Delay Measure                           : enable 
   Interval                                : 10(s)
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
  multicast mvpn ipv6-underlay 2001:DB8:10::1                                     
  #                                                                               
  ip vpn-instance vpna
   ipv4-family                                                                    
    route-distinguisher 100:1                                                     
    apply-label per-instance                                                      
    vpn-target 111:1 export-extcommunity                                          
    vpn-target 111:1 import-extcommunity                                          
    multicast routing-enable                                                      
    mvpn                                                                          
     ipv6 underlay enable                                                         
     sender-enable                                                                
     src-dt4 locator PE1 sid 2001:DB8:100::2
     rpt-spt mode                                     
     ipmsi-tunnel                                                                 
      bier                                                                        
     spmsi-tunnel                                                                 
      holddown-time 80                                                            
      switch-delay 20                                                             
      group 225.1.1.0 255.255.255.0 source 192.168.11.0 255.255.255.0 threshold 10 bier
  #                                                                               
  segment-routing ipv6                                                            
   encapsulation source-address 2001:DB8:10::1 
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32                            
    opcode ::111 end psp                                                       
  #                                                                               
  isis 1                                                                          
   is-level level-2                                                               
   cost-style wide                                                                
   network-entity 10.0000.0000.0001.00                                            
   bier enable
   #
   ipv6 enable topology ipv6                                                      
   segment-routing ipv6 locator PE1 auto-sid-disable                              
   #
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:1::2/96                                                  
   isis ipv6 enable 1
   ptp enable                                                             
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip binding vpn-instance vpna                                                   
   ip address 192.168.1.1 255.255.255.0                                           
   pim sm
   ptp enable
  #
  interface LoopBack2
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.255
   pim sm                                                                      
  #
  pim vpn-instance vpna
   static-rp 10.1.1.1
  #                                                                               
  interface LoopBack1                                                             
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:10::1/128                                                
   isis ipv6 enable 1                                                             
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.1 
   peer 2001:DB8:20::1 as-number 100                                              
   peer 2001:DB8:20::1 connect-interface LoopBack1                                
   peer 2001:DB8:30::1 as-number 100                                              
   peer 2001:DB8:30::1 connect-interface LoopBack1                                
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                          
   #                                                                              
   ipv4-family mvpn                                                               
    policy vpn-target                                                             
    peer 2001:DB8:20::1 enable                                                    
    peer 2001:DB8:30::1 enable                                                    
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2001:DB8:20::1 enable                                                    
    peer 2001:DB8:20::1 prefix-sid                                                
    peer 2001:DB8:30::1 enable                                                    
    peer 2001:DB8:30::1 prefix-sid  
   #                                                                              
   ipv4-family vpn-instance vpna                                                  
    import-route direct                                                           
    segment-routing ipv6 locator PE1                                              
    segment-routing ipv6 best-effort                             
    peer 192.168.1.2 as-number 65410                                              
  #
  bier                                                                            
   sub-domain 0 ipv6
    bfr-id 1                                                              
    bfr-prefix interface LoopBack1                                                
    protocol isis                                                                 
    end-bier locator PE1 sid 2001:DB8:100::1                                      
    encapsulation-type ipv6 bsl 256 max-si 0                                      
  #
  ifit
   node-id 1
   instance-ht16 1
    interval 10
    flow unidirectional source 192.168.11.0 group 225.1.1.0 vpn-instance vpna
    binding interface Gigabitethernet0/1/1
    delay-measure enable
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
  segment-routing ipv6                                                            
   encapsulation source-address 2001:DB8:40::1                                    
   locator P ipv6-prefix 2001:DB8:400:: 64 static 32                              
    opcode ::444 end psp                                                       
  #                                                                               
  isis 1                                                                          
   is-level level-2                                                               
   cost-style wide                                                                
   network-entity 10.0000.0000.0004.00                                            
   bier enable                                                                    
   #
   ipv6 enable topology ipv6                                                      
   segment-routing ipv6 locator P auto-sid-disable                                
   #
  #                                                                               
  interface GigabitEthernet0/1/0
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:1::1/96        
   isis ipv6 enable 1
   ptp enable                                                             
  #                                                                               
  interface GigabitEthernet0/1/1
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:2::1/96                                                  
   isis ipv6 enable 1
   ptp enable                                                             
  #                                                                               
  interface GigabitEthernet0/1/2 
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:3::1/96                                                  
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/1/3
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:4::1/96
   ptp enable
  #                                                                               
  interface LoopBack1                                                             
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:40::1/128                                                
   isis ipv6 enable 1                                                             
  #                                                                               
  bier                                                                            
   sub-domain 0 ipv6                                                              
    bfr-prefix interface LoopBack1                                                
    protocol isis                                                                 
    end-bier locator P sid 2001:DB8:400::1                                        
    encapsulation-type ipv6 bsl 256 max-si 0                                    
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
  multicast mvpn ipv6-underlay 2001:DB8:20::1                                     
  #                                                                               
  ip vpn-instance vpna                                                            
   ipv4-family                                                                    
    route-distinguisher 100:1                                                     
    apply-label per-instance                                                      
    vpn-target 111:1 export-extcommunity  
    vpn-target 111:1 import-extcommunity                                          
    multicast routing-enable                                                      
    mvpn                                                                          
     ipv6 underlay enable
     c-multicast signaling bgp
     rpt-spt mode                                                    
  #                                                                               
  segment-routing ipv6                                                            
   encapsulation source-address 2001:DB8:20::1                                    
   locator PE2 ipv6-prefix 2001:DB8:200:: 64 static 32                            
    opcode ::222 end psp                                                       
  #                        
  isis 1                                                                          
   cost-style wide                                                                
   network-entity 10.0000.0000.0002.00                                            
   bier enable                                                                    
   #
   ipv6 enable topology ipv6                                                      
   segment-routing ipv6 locator PE2 auto-sid-disable                              
   #
  #                                                                               
  interface GigabitEthernet0/1/0                                                          
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:2::2/96                                                  
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/1/1                                                         
   undo shutdown                                                                  
   ip binding vpn-instance vpna                                                   
   ip address 192.168.2.1 255.255.255.0  
   pim sm
   ptp enable
  #
  pim vpn-instance vpna
   static-rp 10.1.1.1
  #
  interface LoopBack1                                                             
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:20::1/128                                                
   isis ipv6 enable 1                                                             
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.2                                                              
   peer 2001:DB8:10::1 as-number 100                                              
   peer 2001:DB8:10::1 connect-interface LoopBack1                                
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                          
   #                      
   ipv4-family mvpn                                                               
    policy vpn-target                                                             
    peer 2001:DB8:10::1 enable                                                    
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2001:DB8:10::1 enable                                                    
    peer 2001:DB8:10::1 prefix-sid                                                
   #                                                                              
   ipv4-family vpn-instance vpna                                                  
    import-route direct                                                           
    segment-routing ipv6 locator PE2                                              
    segment-routing ipv6 best-effort                             
    peer 192.168.2.2 as-number 65411                                              
  #                                      
  bier                                                                            
   sub-domain 0 ipv6                                                              
    bfr-id 2                                                                      
    bfr-prefix interface LoopBack1                                                
    protocol isis                                                                 
    end-bier locator PE2 sid 2001:DB8:200::1                                      
    encapsulation-type ipv6 bsl 256 max-si 0                                      
  #
  ifit
   node-id 2
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
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  #                                                                               
  multicast mvpn ipv6-underlay 2001:DB8:30::1                                     
  #                                                                               
  ip vpn-instance vpna                                                            
   ipv4-family                                                                    
    route-distinguisher 100:1                                                     
    apply-label per-instance                                                      
    vpn-target 111:1 export-extcommunity  
    vpn-target 111:1 import-extcommunity                                          
    multicast routing-enable                                                      
    mvpn                                                                          
     ipv6 underlay enable
     c-multicast signaling bgp
     rpt-spt mode                                                    
  #                                                                               
  segment-routing ipv6                                                            
   encapsulation source-address 2001:DB8:30::1                                    
   locator PE2 ipv6-prefix 2001:DB8:300:: 64 static 32                            
    opcode ::333 end psp                                                       
  #                        
  isis 1                                                                          
   cost-style wide                                                                
   network-entity 10.0000.0000.0003.00                                            
   bier enable                                                                                        
   #
   ipv6 enable topology ipv6                                                      
   segment-routing ipv6 locator PE3 auto-sid-disable                              
   #
  #                                                                               
  interface GigabitEthernet0/1/0                                                          
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:3::2/96                                                  
   isis ipv6 enable 1
   ptp enable
  #                                                                               
  interface GigabitEthernet0/1/1                                                         
   undo shutdown                                                                  
   ip binding vpn-instance vpna                                                   
   ip address 192.168.3.1 255.255.255.0  
   pim sm
   ptp enable
  #
  pim vpn-instance vpna
   static-rp 10.1.1.1
  #
  interface LoopBack1                                                             
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:30::1/128                                                
   isis ipv6 enable 1                                                             
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.3                                                              
   peer 2001:DB8:10::1 as-number 100                                              
   peer 2001:DB8:10::1 connect-interface LoopBack1                                
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                          
   #                      
   ipv4-family mvpn                                                               
    policy vpn-target                                                             
    peer 2001:DB8:10::1 enable                                                    
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2001:DB8:10::1 enable                                                    
    peer 2001:DB8:10::1 prefix-sid                                                
   #                                                                              
   ipv4-family vpn-instance vpna                                                  
    import-route direct                                                           
    segment-routing ipv6 locator PE3                                              
    segment-routing ipv6 best-effort                             
    peer 192.168.3.2 as-number 65412                                              
  #                                      
  bier                                                                            
   sub-domain 0 ipv6                                                              
    bfr-id 3                                                                      
    bfr-prefix interface LoopBack1                                                
    protocol isis                                                                 
    end-bier locator PE3 sid 2001:DB8:300::1                                      
    encapsulation-type ipv6 bsl 256 max-si 0                                      
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
   ip address 192.168.1.2 255.255.255.0
   pim sm
  # 
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.11.2 255.255.255.0
   pim sm
  #
  bgp 65410
   router-id 11.11.11.11
   peer 192.168.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.1 enable
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
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.4.2 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
  #
  bgp 65411
   router-id 12.12.12.12
   peer 192.168.2.1 as-number 100 
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.2.1 enable
  #
  return
  ```
* CE3 configuration file
  ```
  # 
  sysname CE3 
  # 
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   pim sm
  # 
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.5.2 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
  #
  bgp 65412
   router-id 13.13.13.13
   peer 192.168.3.1 as-number 100 
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.3.1 enable
  #
  return
  ```