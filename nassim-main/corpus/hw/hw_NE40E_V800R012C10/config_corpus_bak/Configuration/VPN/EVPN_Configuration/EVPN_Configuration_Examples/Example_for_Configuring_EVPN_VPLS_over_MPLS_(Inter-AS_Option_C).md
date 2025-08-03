Example for Configuring EVPN VPLS over MPLS (Inter-AS Option C)
===============================================================

This section provides an example for configuring inter-AS EVPN Option C when multi-hop EBGP EVPN peer relationships are established between PEs in different ASs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370621__fig129981348132316), Site1 and Site2 belong to the same VPN. Site1 accesses an MPLS backbone network over PE1 in AS100, and Site2 accesses another MPLS backbone network over PE2 in AS200. Inter-AS EVPN Option C is configured. Specifically, MPLS LDP and inter-AS BGP LSPs are configured to construct a tunnel between PEs, and an EBGP EVPN peer relationship is established between the PEs so that the PEs can carry Layer 2 and Layer 3 EVPN services over the same tunnel.

**Figure 1** Configuring EVPN VPLS over MPLS (inter-AS Option C)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001230306379.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for all interfaces on the PEs and ASBRs as well as the loopback interface address.
2. Configure an IGP on the MPLS backbone networks in AS100 and AS200 so that the PE and ASBR on the same MPLS backbone network can communicate with each other.
3. Configure basic MPLS capabilities and MPLS LDP on the MPLS backbone networks in AS100 and AS200 to establish LDP LSPs.
4. Configure IBGP peer relationships between PEs and ASBRs, configure an EBGP peer relationship between ASBRs, and enable these devices to exchange labeled routes.
5. Configure and apply a route-policy on each ASBR.
6. Configure a VPN instance and an EVPN instance on each PE.
7. Configure an EVPN source address on each PE.
8. Establish an EBGP EVPN peer relationship between PEs in different ASs.
9. Configure access-side interfaces on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs and ASBRs: 1.1.1.1, 2.2.2.2, 3.3.3.3, and 4.4.4.4
* Name (vpn1), RD (100:1), and export and import VPN targets (1:1) of the VPN instance on each PE
* Name (evrf1), RD (200:1), and export and import VPN targets (2:2) of the EVPN instance on each PE
* Name of the route-policies configured on ASBRs: policy1 and policy2

#### Procedure

1. Configure IP addresses for all interfaces on the PEs and ASBRs as well as the loopback interface address.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370621__file1).
2. Configure an IGP on the MPLS backbone networks in AS100 and AS200 so that the PE and ASBR on the same MPLS backbone network can communicate with each other.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370621__file1).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configure OSPF to advertise the 32-bit loopback interface addresses used as LSR IDs.
3. Configure basic MPLS capabilities and MPLS LDP on the MPLS backbone networks in AS100 and AS200 to establish LDP LSPs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370621__file1).
4. Configure IBGP peer relationships between PEs and ASBRs, configure an EBGP peer relationship between ASBRs, and enable these devices to exchange labeled routes.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370621__file1).
5. Configure and apply a route-policy on each ASBR.
   
   
   
   # Configure ASBR1: Enable MPLS on GE0/2/0 connected to ASBR2.
   
   ```
   [~ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR1: Create a routing policy.
   
   ```
   [~ASBR1] route-policy policy1 permit node 1
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] route-policy policy2 permit node 1
   ```
   ```
   [*ASBR1-route-policy] if-match mpls-label
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR1: Apply the routing policy to the routes advertised to PE1 and enable ASBR1 to exchange labeled IPv4 routes with PE1.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 route-policy policy2 export
   ```
   
   # Configure ASBR1: Apply the routing policy to the routes advertised to ASBR2 and enable ASBR1 to exchange labeled IPv4 routes with ASBR2.
   
   ```
   [*ASBR1-bgp] peer 10.2.1.2 route-policy policy1 export
   ```
   
   # Configure ASBR1: Advertise the loopback routes from PE1 to ASBR2 and then to PE2.
   
   ```
   [*ASBR1-bgp] network 1.1.1.1 32
   ```
   ```
   [*ASBR1-bgp] network 10.1.1.0 24
   ```
   ```
   [*ASBR1-bgp] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   The configurations of PE2 and ASBR2 are similar to those of PE1 and ASBR1, respectively. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370621__file1).
6. Configure a VPN instance and an EVPN instance on each PE.
   
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 2:2
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-ipv4] vpn-target 1:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] evpn mpls routing-enable
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration of PE2 is similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370621__file1).
7. Configure an EVPN source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 4.4.4.4
   ```
   ```
   [*PE2] commit
   ```
8. Establish an EBGP EVPN peer relationship between PEs in different ASs.
   
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 as-number 200
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 ebgp-max-hop 255
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 connect-interface LoopBack1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] commit
   ```
   
   The configuration of PE2 is similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370621__file1).
9. Configure the access interfaces connecting PEs to CEs.
   
   
   ```
   [~PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] import-route direct
   ```
   ```
   [*PE1-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-vpn1] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] interface GigabitEthernet0/2/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] rewrite pop single
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] bridge-domain 10
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] interface Vbdif10
   ```
   ```
   [*PE1-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-Vbdif10] ip address 192.168.1.1 24
   ```
   ```
   [*PE1-Vbdif10] arp collect host enable
   ```
   ```
   [*PE1-Vbdif10] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration of PE2 is similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370621__file1).
10. Verify the configuration.
    
    
    
    After the preceding configurations are complete, you can find the EVPN routes and IP VPN routes sent from the peer PE on the local PE.
    
    The following example uses the command output on PE1.
    ```
    [~PE1] display bgp evpn all routing-table
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 1.1.1.1
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of Mac Routes: 3
     Route Distinguisher: 200:1
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>    0:48:00e0-fc12-3456:0:0.0.0.0                          0.0.0.0
     *>    0:48:00e0-fc12-3456:32:192.168.1.1                     0.0.0.0
     *>    0:48:00e0-fc12-7890:0:0.0.0.0                          4.4.4.4
        
    
     EVPN-Instance evrf1:
     Number of Mac Routes: 3
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>    0:48:00e0-fc12-3456:0:0.0.0.0                          0.0.0.0
     *>    0:48:00e0-fc12-3456:32:192.168.1.1                     0.0.0.0
     *>    0:48:00e0-fc12-7890:0:0.0.0.0                          4.4.4.4
     
     EVPN address family:
     Number of Inclusive Multicast Routes: 2
     Route Distinguisher: 200:1
           Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
     *>    0:32:1.1.1.1                                           127.0.0.1
     *>    0:32:4.4.4.4                                           4.4.4.4
        
    
     EVPN-Instance evrf1:
     Number of Inclusive Multicast Routes: 2
           Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
     *>    0:32:1.1.1.1                                           127.0.0.1
     *>    0:32:4.4.4.4                                           4.4.4.4
     
     EVPN address family:
     Number of Ip Prefix Routes: 2
     Route Distinguisher: 100:1
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
     *>    0:192.168.1.0:24                                       0.0.0.0
     *>    0:192.168.2.0:24                                       4.4.4.4
                    
    ```
    ```
    [~PE1] display ip routing-table vpn-instance vpn1
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ```
    ```
    ------------------------------------------------------------------------------
    Routing Table : vpn1
             Destinations : 6        Routes : 6         
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
    
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
        192.168.1.0/24  Direct  0    0             D   192.168.1.1     Vbdif10
        192.168.1.1/32  Direct  0    0             D   127.0.0.1       Vbdif10
      192.168.1.255/32  Direct  0    0             D   127.0.0.1       Vbdif10
        192.168.2.0/24  EBGP    255  0             RD  4.4.4.4         GigabitEthernet0/1/0
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```
    ```
    [~PE1] ping -vpn-instance vpn1 192.168.2.1
    ```
    ```
      PING 192.168.2.1: 56  data bytes, press CTRL_C to break
        Reply from 192.168.2.1: bytes=56 Sequence=1 ttl=253 time=7 ms
        Reply from 192.168.2.1: bytes=56 Sequence=2 ttl=253 time=3 ms
        Reply from 192.168.2.1: bytes=56 Sequence=3 ttl=253 time=3 ms
        Reply from 192.168.2.1: bytes=56 Sequence=4 ttl=253 time=3 ms
        Reply from 192.168.2.1: bytes=56 Sequence=5 ttl=253 time=3 ms
    
      --- 192.168.2.1 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 3/3/7 ms
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  mpls ldp
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 192.168.1.1 255.255.255.0
   arp collect host enable
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 ebgp-max-hop 255
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 2.2.2.2 label-route-capability
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 4.4.4.4 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 10.2.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    network 1.1.1.1 255.255.255.255
    network 10.1.1.0 255.255.255.0
    peer 1.1.1.1 enable
    peer 1.1.1.1 route-policy policy2 export
    peer 1.1.1.1 label-route-capability
    peer 10.2.1.2 enable
    peer 10.2.1.2 route-policy policy1 export
    peer 10.2.1.2 label-route-capability
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  route-policy policy2 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 200
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack1
   peer 10.2.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 4.4.4.4 255.255.255.255
    network 10.3.1.0 255.255.255.0
    peer 4.4.4.4 enable
    peer 4.4.4.4 route-policy policy2 export
    peer 4.4.4.4 label-route-capability
    peer 10.2.1.1 enable
    peer 10.2.1.1 route-policy policy1 export
    peer 10.2.1.1 label-route-capability
  #
  ospf 2
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  route-policy policy2 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  mpls ldp
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 192.168.2.1 255.255.255.0
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp       
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 200
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 ebgp-max-hop 255
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 3.3.3.3 label-route-capability
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
  #
  ospf 2
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  evpn source-address 4.4.4.4
  #
  return
  ```