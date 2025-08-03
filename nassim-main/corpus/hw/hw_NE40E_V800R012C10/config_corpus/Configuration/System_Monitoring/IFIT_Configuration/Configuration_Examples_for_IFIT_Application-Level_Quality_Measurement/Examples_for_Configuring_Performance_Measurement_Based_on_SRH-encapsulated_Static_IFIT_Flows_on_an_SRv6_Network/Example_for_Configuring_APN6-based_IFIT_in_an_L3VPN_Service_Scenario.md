Example for Configuring APN6-based IFIT in an L3VPN Service Scenario
====================================================================

This section provides an example for configuring IFIT to implement end-to-end packet loss and delay measurement based on the APN6 instance on an L3VPN over SRv6 network.

#### Networking Requirements

Application-aware IPv6 Networking (APN6) is a new network architecture. It conveys application information (APN attributes), including application identities (APN IDs) and network performance requirements (APN parameters) to a network by leveraging the programming space of IPv6 packets, providing fine-granularity network services and accurate network operations and maintenance (O&M). After APN IDs identify key applications or users, IFIT can be used to monitor the performance of key services in real time. On the network shown in [Figure 1](#EN-US_TASK_0000001346249721__fig184238288365), a bidirectional SRv6 TE flow group is deployed between PE1 and PE2 to carry L3VPNv4 services.

**Figure 1** Configuring APN6-based IFIT on an L3VPN over SRv6 network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001293411546.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an APN6-based L3VPNv4 over SRv6 TE Policy on PE1, P1, P2, and PE2. Specifically:
   1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, P1, P2, and PE2.
   2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on PE1, P1, P2, and PE2.
   3. Configure VPN instances on PE1 and PE2.
   4. Establish an EBGP peer relationship between each PE and its connected CE.
   5. Set up an MP-IBGP peer relationship between the PEs.
   6. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, P1, P2, and PE2. In addition, configure PE1 and PE2 to advertise VPN routes carrying SIDs.
   7. Deploy an SRv6 TE Policy between PE1 and PE2.
   8. Configure APN6 instances on PE1 and PE2.
   9. Configure APN IDs for service flows on PE1 and PE2.
   10. Configure an SRv6 mapping policy on PE1 and PE2.
   11. Configure a tunnel policy on PE1 and PE2 to preferentially use the SRv6 TE flow group for VPN traffic import.
2. Configure basic 1588v2 functions to synchronize the clocks across all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

APN6-based IFIT performance measurement applies only to unidirectional flows. In this example, the direction PE1 -> P1 -> PE2 is used.




#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0000001346249721__fig184238288365)
* IPv6 address of each interface on PE1, P1, P2, and PE2
* IS-IS process ID of each device (PE1, P1, P2, and PE2)
* IS-IS level of each device (PE1, P1, P2, and PE2)
* VPN instance names, RDs, and RTs on PE1 and PE2
* APN6 template and instance names on PE1 and PE2, and the name and length of the app-group field in the template
* IFIT instance ID (1) and measurement interval (10s)
* IFIT performance measurement instance generated based on the APN6 instance named **APN6-instance1**
* NMS's IPv6 address (2001:db8:101::1) and port number (10001), and reachable routes between the NMS and device


#### Procedure

1. Configure APN6-based L3VPNv4 over SRv6 TE Policy on PE1, P1, P2, and PE2. For configuration details, see [Configuration Files](#EN-US_TASK_0000001346249721__section_05).
2. Configure 1588v2 to synchronize the clocks of P1 and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001346249721__section_05).
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
   [*PE1-ifit] instance 1
   ```
   ```
   [*PE1-ifit-instance-1] measure-mode trace
   ```
   ```
   [*PE1-ifit-instance-1] interval 10
   ```
   ```
   [*PE1-ifit-instance-1] flow unidirectional apn-id-ipv6 instance APN6-instance1
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
   Flow Id                                 : 1572865
   Instance Type                           : instance 
   Flow Type                               : unidirectional
   Apn-id-ipv6 Instance                    : APN6-instance1
   Interface                               : GigabitEthernet0/2/0
   Loss Measure                            : enable
   Delay Measure                           : enable
   Delay Per packet Measure                : disable
   Disorder Measure                        : disable
   Measure Mode                            : trace
   Interval                                : 10(s)
   Flow Match Priority                     : 0
   Flow InstType Priority                  : 2
   ```
   ```
   [~PE1] display ifit dynamic-hop
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
   Direction                               : transitOutput
   Loss Measure                            : enable
   Delay Measure                           : enable
   Disorder Measure                        : disable
   Interval                                : 10(s)
   ```
   
   # Enable IFIT on P1 and PE2. The configuration on P1 is used as an example.
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
   [*PE1-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-apn-statistics/flow-apn-statistic
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
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  apn
   ipv6
    apn-id template tmplt1 length 64 app-group 16
     app-group index 1 app-group1 length 16
    apn-id instance APN6-instance1
     template tmplt1
     apn-field app-group1 1
  #
  acl number 3333
   rule 5 permit ip source 11.11.11.11 0 destination 22.22.22.22 0
  #
  traffic classifier c1
   if-match acl 3333
  #
  traffic behavior b1
   remark apn-id-ipv6 instance APN6-instance1
  #        
  traffic policy p1
   share-mode
   statistics enable
   classifier c1 behavior b1 precedence 1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1                                              
   locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32                                     
    opcode ::100 end psp      
    opcode ::200 end no-flavor
   srv6-te-policy locator as1 
   segment-list list1         
    index 5 sid ipv6 2001:DB8:200::100  
    index 10 sid ipv6 2001:DB8:300::100 
   segment-list list2         
    index 5 sid ipv6 2001:DB8:400::100  
    index 10 sid ipv6 2001:DB8:300::100 
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 10                                  
    binding-sid 2001:DB8:100::900       
    candidate-path preference 100     
     segment-list list1       
   srv6-te policy policy2 endpoint 2001:DB8:3::3 color 20                                  
    binding-sid 2001:DB8:100::901       
    candidate-path preference 100 
     segment-list list2       
   mapping-policy p1 color 101     
    match-type apn-id-ipv6 
     index 10 instance APN6-instance1 match srv6-te-policy color 10
     default match srv6-te-policy color 20
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:11::1/96
   isis ipv6 enable 1
   ptp enable
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
   traffic-policy p1 inbound
   ptp enable
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:13::1/96
   isis ipv6 enable 1
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/128
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
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy p1 import
    peer 2001:DB8:3::3 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
    peer 10.1.1.2 as-number 65410
  #
  ifit
   node-id 1
   instance 1
    measure-mode trace
    interval 10
    flow unidirectional apn-id-ipv6 instance APN6-instance1
    binding interface GigabitEthernet0/2/0 
  #
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-apn-statistics/flow-apn-statistic
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
   locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
    opcode ::100 end psp
    opcode ::200 end no-flavor
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:11::2/96
   isis ipv6 enable 1
   ptp enable
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::1/96
   isis ipv6 enable 1
   ptp enable
  #
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::3/64
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
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-apn-statistics/flow-apn-statistic
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
   encapsulation source-address 2001:DB8:4::4
   locator as1 ipv6-prefix 2001:DB8:400::1 64 static 32
    opcode ::100 end psp
    opcode ::200 end no-flavor
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:13::2/96
   isis ipv6 enable 1
   ptp enable
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:14::1/96
   isis ipv6 enable 1
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:4::4/128
   isis ipv6 enable 1
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
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  apn
   ipv6
    apn-id template tmplt1 length 64 app-group 16
     app-group index 1 app-group1 length 16
    apn-id instance APN6-instance1
     template tmplt1
     apn-field app-group1 1
  #
  acl number 3333
   rule 5 permit ip source 22.22.22.22 0 destination 11.11.11.11 0
  #
  traffic classifier c1
   if-match acl 3333
  #
  traffic behavior b1
   remark apn-id-ipv6 instance APN6-instance1
  #        
  traffic policy p1
   share-mode
   statistics enable
   classifier c1 behavior b1 precedence 1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3                                              
   locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32                                     
    opcode ::100 end psp          
    opcode ::200 end no-flavor 
   srv6-te-policy locator as1 
   segment-list list1         
    index 5 sid ipv6 2001:DB8:200::100  
    index 10 sid ipv6 2001:DB8:100::100 
   segment-list list2         
    index 5 sid ipv6 2001:DB8:400::100  
    index 10 sid ipv6 2001:DB8:100::100 
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 10                                  
    binding-sid 2001:DB8:300::900       
    candidate-path preference 100     
     segment-list list1       
   srv6-te policy policy2 endpoint 2001:DB8:1::1 color 20                                  
    binding-sid 2001:DB8:300::901       
    candidate-path preference 100          
     segment-list list2       
   mapping-policy p1 color 101     
    match-type apn-id-ipv6 
     index 10 instance APN6-instance1 match srv6-te-policy color 10
     default match srv6-te-policy color 20
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable  
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/96
   isis ipv6 enable 1
   ptp enable
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
   traffic-policy p1 inbound
   ptp enable
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:14::2/96
   isis ipv6 enable 1
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
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
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
    peer 10.2.1.2 as-number 65420
  #
  ifit
   node-id 2
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-apn-statistics/flow-apn-statistic
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
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 11.11.11.11 255.255.255.255
  #               
  bgp 65410       
   peer 10.1.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    network 11.11.11.11 255.255.255.255
    peer 10.1.1.1 enable
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
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65420
   peer 10.2.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 22.22.22.22 255.255.255.255
    peer 10.2.1.1 enable
  #
  return
  ```