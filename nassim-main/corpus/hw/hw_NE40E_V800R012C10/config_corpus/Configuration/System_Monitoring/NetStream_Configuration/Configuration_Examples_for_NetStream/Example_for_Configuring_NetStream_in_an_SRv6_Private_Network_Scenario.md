Example for Configuring NetStream in an SRv6 Private Network Scenario
=====================================================================

This section uses the SRv6 private network scenario as an example to describe how to configure NetStream to monitor VPN service traffic and collect private network information.

#### Networking Requirements

NetStream can be deployed in an SRv6 private network scenario to provide traffic analysis for forwarding paths between PEs and collect private network information. This helps users adjust network parameters to better meet service requirements.

In the SRv6 private network scenario shown in [Figure 1](#EN-US_TASK_0253120420__fig182651292378):

* Configure the P to collect statistics about inner IPv4 packets in IPv6 original flows and send the statistics to the NSC and NDA.
* Analyze traffic on the NSC and NDA to obtain user traffic between PEs and collect private network information.**Figure 1** Configuring NetStream in an SRv6 private network scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.
    
  ![](figure/en-us_image_0255015171.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each involved interface.
2. Configure an L3VPN over SRv6 TE Policy.
3. Configure NetStream on the P to collect statistics about inner IPv4 packets in IPv6 original flows.

#### Data Preparation

To complete the configuration, you need the following data:

* Version for outputting NetStream packets and sampling interval
* Destination address, destination port number, and source address of the output NetStream flows
* ID of the slot in which the NetStream service processing board resides (In this example, the NetStream service processing board is in slot 3.)

#### Procedure

1. Assign an IP address to each involved interface.
   
   
   
   Assign an IP address and a mask to each interface (including loopback interfaces) according to [Figure 1](#EN-US_TASK_0253120420__fig182651292378). For configuration details, see [Configuration Files](#EN-US_TASK_0253120420__example1157617426214103).
2. Configure an L3VPN over SRv6 TE Policy.
   
   
   
   For the configuration roadmap, see [Segment Routing IPv6 Configuration](../vrp/dc_vrp_srv6_cfg_all_0000.html). For configuration details, see [Configuration Files](#EN-US_TASK_0253120420__example1157617426214103).
3. Configure NetStream on the P to collect statistics about inner IPv4 packets in IPv6 original flows.
   
   # Configure the board on the P to process NetStream services in distributed mode.
   ```
   [*P] slot 3
   ```
   ```
   [*P-slot-3] ipv6 netstream sampler to slot self
   ```
   ```
   [*P-slot-3] quit 
   ```
   
   # Collect statistics about incoming and outgoing packets on GigabitEthernet 0/1/0 of the P.
   ```
   [*P] interface GigabitEthernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] ipv6 netstream inbound
   ```
   ```
   [*P-GigabitEthernet0/1/0] ipv6 netstream outbound
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream enabled on a main interface cannot collect traffic statistics about its sub-interface.
   
   
   
   # Configure the output format of IPv6 packets, and the source address, destination address, and destination port of the output packets.
   ```
   [*P] ipv6 netstream export version 9
   ```
   ```
   [*P] ipv6 netstream export host ipv6 2001:DB8:111::1 9001
   ```
   ```
   [*P] ipv6 netstream export source ipv6 2001:DB8:30::1
   ```
   
   # Configure NetStream to sample the outer IPv6 packets and set the mode to fixed packet sampling.
   ```
   [*P] ipv6 netstream sampler fix-packets 10000 inbound
   ```
   ```
   [*P] ipv6 netstream sampler fix-packets 10000 outbound
   ```
   ```
   [*P] quit
   ```
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After completing the preceding configuration, the device samples outer IPv6 packets. You can run the [**display ipv6 netstream cache origin slot**](cmdqueryname=display+ipv6+netstream+cache+origin+slot) *slot-id* command to check sampling information about outer packets.
   
   To sample inner IPv4 packets, you need to configure NetStream IPv4.
   
   
   # Configure the output format of IPv4 packets, and the source address, destination address, and destination port of the output packets.
   ```
   [*P] ip netstream export version 9
   ```
   ```
   [*P] ip netstream export host ipv6 2001:DB8:111::1 9001
   ```
   ```
   [*P] ip netstream export source ipv6 2001:DB8:30::1
   ```
   
   # Configure NetStream to sample inner IPv4 packets.
   ```
   [*P] ipv6 netstream srv6-aware inner-header
   ```
   ```
   [*P] commit
   ```
4. Verify the configuration.
   
   
   
   # Run the [**display ip netstream cache origin slot**](cmdqueryname=display+ip+netstream+cache+origin+slot) **3** command on the P after completing the configuration. The command output shows information about inner IPv4 packets in the NetStream flow buffer.
   
   ```
   [~P] display ip netstream cache origin slot 3
   
   
    DstIf                         
    SrcIf                           
    DstP                          Msk          Pro            Tos 
    SrcP                          Msk          Flags          Ttl
    Packets                                                   Bytes
    NextHop                                                   Direction
    DstIP                                                     DstAs
    SrcIP                                                     SrcAs
    BGP: BGP NextHop                                          TopLabelType
    Label1                        Exp1         Bottom1
    Label2                        Exp2         Bottom2
    Label3                        Exp3         Bottom3
    TopLabelIpAddress                          VlanId         VniId
    CreateFlowTime                LastRefreshTime             VPN(direct)
    FlowLabel                     Rdvalue
    ForwardStatus
    --------------------------------------------------------------------------
   
    GigabitEthernet0/2/0                                                         
    GigabitEthernet0/1/0                                            
    0                             64            253            0
    0                             128            0             60
    3                                                          384       
    2001:DB8:20::2                                             in
    10.1.1.2                                                   0         
    10.2.1.2                                                   0         
    ::                                                         UNKNOWN             
    0                             0            0         
    0                             0            0         
    0                             0            0         
    0.0.0.0                                    0               0        
    2020-05-09 11:38:07           2020-05-09 11:40:30          --
    --                            -:-
    66(Forwarded Not Fragmented)
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::111 end
   srv6-te-policy locator as1
   segment-list list1
    index 5 sid ipv6 2001:DB8:200::222
    index 10 sid ipv6 2001:DB8:300::333
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
    binding-sid 2001:DB8:100::100
    candidate-path preference 100
     segment-list list1 
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
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/96
   isis ipv6 enable 1
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
    peer 2001:DB8:3::3 route-policy p1 import
    peer 2001:DB8:3::3 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
    peer 10.1.1.2 as-number 65410
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #               
  return 
  ```
* P configuration file
  
  ```
  #
  sysname P        
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
    opcode ::222 end
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
   ipv6 address 2001:DB8:10::2/96
   isis ipv6 enable 1
   ipv6 netstream inbound
   ipv6 netstream outbound 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/96
   isis ipv6 enable 1  
  #
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:30::1/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/64
   isis ipv6 enable 1
  #
  slot 3
   ipv6 netstream sampler to slot self
  #
  ip netstream export version 9
  ip netstream export host ipv6 2001:DB8:111::1 9001 
  ip netstream export source ipv6 2001:DB8:30::1
  #
  ipv6 netstream srv6-aware inner-header
  ipv6 netstream export version 9 
  ipv6 netstream export host ipv6 2001:DB8:111::1 9001 
  ipv6 netstream export source ipv6 2001:DB8:30::1
  ipv6 netstream sampler fix-packets 10000 inbound
  ipv6 netstream sampler fix-packets 10000 outbound
  #               
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32
    opcode ::333 end
   srv6-te-policy locator as1
   segment-list list1
    index 5 sid ipv6 2001:DB8:200::222
    index 10 sid ipv6 2001:DB8:100::111
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    binding-sid 2001:DB8:300::300
    candidate-path preference 100
     segment-list list1 
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
   ipv6 address 2001:DB8:20::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
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
    peer 2001:DB8:1::1 route-policy p1 import
    peer 2001:DB8:1::1 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
    peer 10.2.1.2 as-number 65420
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
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