Example for Configuring Peer Locator-based IFIT in an L3VPN Service Scenario
============================================================================

This section provides an example for configuring IFIT to implement end-to-end packet loss and delay measurement based on the peer locator on an L3VPN over SRv6 network.

#### Networking Requirements

L3VPN over SRv6 uses public network SRv6 tunnels to carry L3VPN services. To meet users' higher requirements on service quality, IFIT is required on an L3VPN over SRv6 network to monitor the packet loss rate and delay of links between PEs in real time. This enables timely responses to service quality deterioration.

On the L3VPN over SRv6 network shown in [Figure 1](#EN-US_TASK_0203265102__fig_dc_vrp_ifit_cfg_001301), service flows enter the network through PE1, traverse the P, and leave the network through PE2.

**Figure 1** Configuring peer locator-based IFIT on an L3VPN over SRv6 network![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0217893802.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an L3VPN over SRv6 network on each PE and the P. Specifically:
   1. Enable IPv6 forwarding on each device and configure IPv6 addresses for involved interfaces.
   2. Enable IS-IS, configure an IS-IS level, and specify a network entity on each device.
   3. Configure the IS-IS SRv6 capability on each device.
   4. Configure a VPN instance on the PEs.
   5. Establish an EBGP peer relationship between each PE and its connected CE.
   6. Establish an MP-IBGP peer relationship between the PEs.
   7. Configure SRv6 BE on PEs.
2. Configure basic 1588v2 functions to synchronize clocks among all devices.
3. Configure packet loss and delay measurement on the PEs to collect packet loss rate and delay statistics at intervals.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface as listed in [Figure 1](#EN-US_TASK_0203265102__fig_dc_vrp_ifit_cfg_001301)
* Area numbers of the PEs and P
* Levels on the PEs and P
* Name, RD, and RT of the VPN instance on each PE
* IFIT instance ID (1) and measurement interval (10s)
* Peer locator (2001:db8:40::1/64) of the IFIT instance
* NMS's IPv6 address (2001:db8:101::1) and port number (10001), and reachable routes between the NMS and device


#### Procedure

1. Configure an L3VPN over SRv6 network on each PE and the P. For configuration details, see [Configuration Files](#EN-US_TASK_0203265102__section_05).
2. Configure 1588v2 to synchronize the clocks of the P and PEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0203265102__section_05).
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
   [*PE1-ifit-instance-1] measure-mode e2e
   ```
   ```
   [*PE1-ifit-instance-1] interval 10
   ```
   ```
   [*PE1-ifit-instance-1] flow unidirectional source any destination any vpn-instance vpna peer-locator 2001:DB8:40::1 64
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
   Source IP Address/Mask Length           : any(IPv4)
   Destination IP Address/Mask Length      : any(IPv4)
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Gtp                                     : disable
   Gtp TeId                                : --
   Dscp                                    : --
   Interface                               : GigabitEthernet0/2/0
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
   Tunnel Type                             : SRv6
   Flow Match Priority                     : 0
   Peer Locator:                           : 2001:DB8:40::1/64
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
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator as1 ipv6-prefix 2001:DB8:100::1 64 static 32
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1              
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
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
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
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.1.1.2 as-number 65410
  #
  ifit
   node-id 1
   instance 1
    interval 10                                                          
    flow unidirectional source any destination any vpn-instance vpna peer-locator 2001:DB8:40::1 64
    binding interface GigabitEthernet0/2/0
  #
  telemetry
   #
   sensor-group ifit
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
   ipv6 address 2001:DB8:30::1/96
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/64
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
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator as1 ipv6-prefix 2001:DB8:40::1 64 static 32
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1              
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
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
   ptp enable
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/64
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
    peer 2001:DB8:1::1 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.2.1.2 as-number 65420
  #
  ifit
   node-id 2
  #
  telemetry
   #
   sensor-group ifit
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