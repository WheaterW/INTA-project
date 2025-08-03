Example for Configuring Interworking Between EVPN L3VPN over SRv6 TE Policy and Common L3VPN over MPLS in Option B Mode
=======================================================================================================================

This section describes how to configure interworking between EVPN L3VPN over SRv6 TE Policy and common L3VPN over MPLS in Option B mode.

#### Networking Requirements

Many metro networks deployed with L3VPN are evolving towards EVPN. If a metro network involves a large number of devices, E2E evolution may not be completed at one time. If this is the case, co-existence of L3VPN and EVPN arises. On the network shown in [Figure 1](#EN-US_TASK_0000001206731903__fig3691666259), EVPN is deployed between PE1 and the ASBR, and L3VPN is deployed between the ASBR and PE2. To allow communication between the L3VPN and EVPN, configure the boundary device ASBR for the two networks. The configuration of L3VPNv4 is similar to that of L3VPNv6. For details about the differences, see [Configuring Interworking Between EVPN L3VPN over SRv6 TE Policy and Common L3VPN over MPLS in Option B Mode](dc_vrp_evpn_cfg_0176.html). This section uses L3VPNv4 as an example.

**Figure 1** Configuring interworking between EVPN L3VPN over SRv6 TE Policy and L3VPN over MPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001161493404.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Deploy an IGP between PE1 and the ASBR and between the ASBR and PE2. IS-IS is used in this example.
2. Configure an IPv4 L3VPN instance on each PE and bind the local access-side interface to the IPv4 L3VPN instance.
3. Configure EVPN L3VPN over SRv6 TE Policy on PE1 and the ASBR.
4. Configure MPLS LDP on the ASBR and PE2.
5. Configure L3VPN instances and BGP VPNv4 on the ASBR and PE2.
6. Establish an EBGP peer relationship between each PE and its connected CE.
7. Configure route import between address families and a tunnel selector on the ASBR.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces on PE1, the ASBR, and PE2.
* IS-IS process ID on PE1, the ASBR, and PE2
* IS-IS level of PE1, the ASBR, and PE2
* VPN instance names, RDs, and RTs on PE1 and PE2

#### Procedure

1. Configure interface IP addresses, including loopback interface addresses, on PE1, the ASBR, PE2, CE1, and CE2.
   
   
   
   Configure interface IP addresses and masks. For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001206731903__example121226172748).
2. Deploy an IGP between PE1 and the ASBR and between the ASBR and PE2. IS-IS is used in this example.
   
   
   
   Configure IS-ISv6 between PE1 and the ASBR (EVPN) to ensure IPv6 route reachability, and configure IS-IS between the ASBR and PE2 (L3VPN) to ensure IPv4 route reachability. For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001206731903__example121226172748).
3. Configure IPv4 L3VPN instances on PE1 and PE2 and bind physical interfaces to these instances for the access of Layer 3 services.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001206731903__example121226172748).
4. Perform the following steps on PE1 and the ASBR to configure EVPN L3VPN over SRv6 TE Policy.
   
   
   1. Configure BGP EVPN and establish a BGP EVPN peer relationship between PE1 and the ASBR.
   2. Configure SRv6 SIDs and IS-IS SRv6 capabilities, and configure VPN routes to carry SIDs.
   3. Configure an SRv6 TE Policy and then a tunnel policy to import VPN traffic.
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001206731903__example121226172748).
5. Configure MPLS LDP on the ASBR and PE2.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001206731903__example121226172748).
6. Configure L3VPN instances and BGP VPNv4 on the ASBR and PE2.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001206731903__example121226172748).
7. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-LoopBack1] ip address 10.1.1.1 32
   ```
   ```
   [*CE1-LoopBack1] quit
   ```
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] peer 10.11.1.1 as-number 100
   ```
   ```
   [*CE1-bgp] import-route direct
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] peer 10.11.1.2 as-number 65410
   ```
   ```
   [*PE1-bgp-vpna] import-route direct
   ```
   ```
   [*PE1-bgp-vpna] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-vpna] commit
   ```
   ```
   [~PE1-bgp-vpna] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface loopback 1
   ```
   ```
   [*CE2-LoopBack1] ip address 10.1.4.1 32
   ```
   ```
   [*CE2-LoopBack1] quit
   ```
   ```
   [*CE2] bgp 65420
   ```
   ```
   [*CE2-bgp] peer 10.22.1.1 as-number 200
   ```
   ```
   [*CE2-bgp] import-route direct
   ```
   ```
   [*CE2-bgp] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] peer 10.22.1.2 as-number 65420
   ```
   ```
   [*PE2-bgp-vpna] import-route direct
   ```
   ```
   [*PE2-bgp-vpna] commit
   ```
   ```
   [~PE2-bgp-vpna] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on each PE to check whether a BGP peer relationship has been established between the PE and its connected CE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpna peer
    BGP local router ID : 1.1.1.1                                                  
    Local AS number : 100      
   
    VPN-Instance vpna, Router ID 1.1.1.1:                                          
    Total number of peers : 1                 Peers in established state : 1       
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv          
     10.11.1.2       4       65410       48       51     0 00:39:40 Established        2 
   ```
8. Configure route import between address families and a tunnel selector on the ASBR.
   
   
   
   # Configuring route import between address families.
   
   ```
   [~ASBR] bgp 100
   ```
   ```
   [*ASBR-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR-bgp-af-vpnv4] import-rib evpn srv6 ip-prefix
   ```
   ```
   [*ASBR-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*ASBR-bgp-af-vpnv4] quit
   ```
   ```
   [*ASBR-bgp] l2vpn-family evpn
   ```
   ```
   [*ASBR-bgp-af-evpn] import-rib vpnv4 mpls
   ```
   ```
   [*ASBR-bgp-af-evpn] undo policy vpn-target
   ```
   ```
   [*ASBR-bgp-af-evpn] segment-routing ipv6 locator ASBR
   ```
   ```
   [*ASBR-bgp-af-evpn] segment-routing ipv6 apply-sid per-route import-rib vpnv4
   ```
   ```
   [*ASBR-bgp-af-evpn] quit
   ```
   ```
   [*ASBR-bgp] quit
   ```
   ```
   [*ASBR] commit
   ```
   
   # Configure and apply a tunnel selector.
   
   ```
   [~ASBR] tunnel-policy tp1
   ```
   ```
   [*ASBR-tunnel-policy-tp1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   ```
   ```
   [*ASBR-tunnel-policy-tp1] quit
   ```
   ```
   [*ASBR] tunnel-selector ts1 permit node 1
   ```
   ```
   [*ASBR-tunnel-selector] apply tunnel-policy tp1
   ```
   ```
   [*ASBR-tunnel-selector] apply segment-routing ipv6 traffic-engineer
   ```
   ```
   [*ASBR-tunnel-selector] quit
   ```
   ```
   [*ASBR] bgp 100
   ```
   ```
   [*ASBR-bgp] l2vpn-family evpn
   ```
   ```
   [*ASBR-bgp-af-evpn] tunnel-selector ts1 
   ```
   ```
   [*ASBR-bgp-af-evpn] quit
   ```
   ```
   [*ASBR-bgp] quit
   ```
   ```
   [*ASBR] commit
   ```
9. Verify the configuration.
   
   
   
   Check that CEs belonging to the same VPN instance can ping each other. For example:
   
   ```
   [~CE1] ping -a 10.1.1.1 10.1.4.1                                                 
     PING 10.1.4.1: 56  data bytes, press CTRL_C to break                          
       Reply from 10.1.4.1: bytes=56 Sequence=1 ttl=253 time=32 ms                 
       Reply from 10.1.4.1: bytes=56 Sequence=2 ttl=253 time=24 ms                 
       Reply from 10.1.4.1: bytes=56 Sequence=3 ttl=253 time=27 ms                 
       Reply from 10.1.4.1: bytes=56 Sequence=4 ttl=253 time=35 ms                 
       Reply from 10.1.4.1: bytes=56 Sequence=5 ttl=253 time=28 ms                 
   
     --- 10.1.4.1 ping statistics ---                                              
       5 packet(s) transmitted 
       5 packet(s) received    
       0.00% packet loss       
       round-trip min/avg/max = 24/29/35 ms 
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
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy tp1 evpn
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::10 end psp
   srv6-te-policy locator PE1
   segment-list list1
    index 10 sid ipv6 2001:DB8:130::30
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
    binding-sid 2001:DB8:100::450
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
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.11.1.1 255.255.255.0
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1 
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   private-4-byte-as enable
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE1 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.11.1.2 as-number 65410
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy p1 export
    peer 2001:DB8:3::3 advertise encap-type srv6
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy tp1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #               
  return 
  ```
* ASBR configuration file
  
  ```
  #
  sysname ASBR
  #
  tunnel-selector ts1 permit node 1
   apply tunnel-policy tp1
   apply segment-routing ipv6 traffic-engineer
  #
  mpls lsr-id 10.1.3.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator ASBR ipv6-prefix 2001:DB8:130:: 64 static 32
    opcode ::30 end psp
   srv6-te-policy locator ASBR
   segment-list list1
    index 10 sid ipv6 2001:DB8:100::10
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    binding-sid 2001:DB8:130::350
    candidate-path preference 100
     segment-list list1
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator ASBR auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:10::2/64
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #
  interface LoopBack2
   ip address 10.1.3.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   private-4-byte-as enable
   peer 10.1.5.1 as-number 200
   peer 10.1.5.1 ebgp-max-hop 255
   peer 10.1.5.1 connect-interface LoopBack2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    undo peer 10.1.5.1 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    bestroute nexthop-resolved tunnel
    import-rib evpn srv6 ip-prefix
    peer 10.1.5.1 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    tunnel-selector ts1
    segment-routing ipv6 locator ASBR
    segment-routing ipv6 apply-sid per-route import-rib vpnv4
    import-rib vpnv4 mpls
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy rp1 export
    peer 2001:DB8:1::1 advertise encap-type srv6
  #
  route-policy rp1 permit node 1
   apply extcommunity color 0:101
  #
  tunnel-policy tp1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
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
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 10.1.5.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0005.00
   #              
   ipv6 enable topology ipv6
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.22.1.1 255.255.255.0 
  #               
  interface LoopBack1
   ip address 10.1.5.1 255.255.255.255
   isis enable 1
  #
  bgp 200
   private-4-byte-as enable
   peer 10.1.3.1 as-number 100
   peer 10.1.3.1 ebgp-max-hop 255
   peer 10.1.3.1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 10.1.3.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.1.3.1 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    peer 10.22.1.2 as-number 65420
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
   ip address 10.1.1.1 255.255.255.255
  #               
  bgp 65410
   private-4-byte-as enable
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
   ip address 10.1.4.1 32
  #               
  bgp 65420
   private-4-byte-as enable
   peer 10.22.1.1 as-number 200
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.22.1.1 enable
  #
  return
  ```