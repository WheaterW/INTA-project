Example for Configuring Inter-AS NG MVPN in Option C Mode in an Independent Labeled Address Family
==================================================================================================

After a multi-hop MP-EBGP peer relationship is established between PEs in different ASs, inter-AS NG MVPN can be implemented in Option C mode.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001870498613__fig_dc_vrp_cfg_ngmvpn_007401), CE1 and CE2 belong to the same VPN. CE1 accesses PE1 in AS 100, and CE2 accesses PE2 in AS 200.

**Figure 1** Configuring inter-AS NG MVPN in Option C mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0000001823659008.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set up an MP-EBGP peer relationship between PEs in different ASs and configure the maximum number of hops between the PEs.
2. Configure the PE and ASBR in the same AS to exchange labeled IPv4 routes.
3. Configure the ASBRs to exchange labeled IPv4 routes.
4. Configure NG MVPN.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PEs and ASBRs (1.1.1.1, 2.2.2.2, 3.3.3.3, and 4.4.4.4)
* PE configurations: VPN instance name (ng), RDs (1:3 and 192.168.122.15:1), and import and export VPN targets of VPN instances (1:1)
* Routing policies used by ASBRs

#### Procedure

1. Configure an IGP on the MPLS backbone networks in AS 100 and AS 200, so that the PE and ASBR on the same backbone network can communicate.
   
   
   
   This example uses IS-IS as the IGP. For detailed configurations, see Configuration Files.
2. Configure basic MPLS functions and MPLS LDP on each node of the MPLS backbone networks in AS 100 and AS 200 and set up LDP LSPs.
   
   
   
   For detailed configurations, see Configuration Files.
3. Configure automatic mLDP P2MP tunnels on PEs and ASBRs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp
   ```
   ```
   [~PE1-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE1-mpls-ldp] commit
   ```
   ```
   [~PE1-mpls-ldp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls ldp
   ```
   ```
   [~PE2-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE2-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*PE2-mpls-ldp] commit
   ```
   ```
   [~PE2-mpls-ldp] quit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls ldp
   ```
   ```
   [~ASBR1-mpls-ldp] mldp p2mp
   ```
   ```
   [*ASBR1-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*ASBR1-mpls-ldp] commit
   ```
   ```
   [~ASBR1-mpls-ldp] quit
   ```
   
   The configuration of ASBR2 is similar to the configuration of ASBR1. For detailed configurations, see Configuration Files.
4. Configure BGP and establish IBGP peer relationships for AS 100 and AS 200 in the IPv4 address family view.
   
   
   
   For detailed configurations, see Configuration Files.
5. Configure a VPN instance on each PE and bind the interface that connects a PE to a CE to the VPN instance on that PE.
   
   
   
   For detailed configurations, see Configuration Files.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The import VPN target configured on PE1 must be the same as the export VPN target configured on PE2; the export VPN target configured on PE1 must be the same as the import VPN target configured on PE2.
6. Configure the function to exchange labeled IPv4 routes.
   
   
   
   # On PE1, enable the capability of exchanging labeled IPv4 routes with ASBR1 and advertise the loopback route to ASBR2.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family labeled-unicast
   ```
   ```
   [~PE1-bgp-af-ipv4] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] network 1.1.1.1 255.255.255.255
   ```
   ```
   [*PE1-bgp-af-ipv4] commit
   ```
   ```
   [~PE1-bgp-af-ipv4] quit
   ```
   
   # On ASBR1, enable MPLS on GigabitEthernet 0/1/1, which is connected to ASBR2.
   
   ```
   [~ASBR1] interface GigabitEthernet0/1/1
   ```
   ```
   [~ASBR1-GigabitEthernet0/1/1] ip address 10.1.3.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Enable ASBR1 to exchange labeled IPv4 routes with PE1 and import labeled routes.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [~ASBR1-bgp] import-rib public labeled-unicast
   ```
   ```
   [~ASBR1-bgp] ipv4-family labeled-unicast
   ```
   ```
   [~ASBR1-bgp-af-ipv4] peer 1.1.1.1 enable
   ```
   ```
   [*ASBR1-bgp-af-ipv4] quit
   ```
   
   # On ASBR1, enable the capability of exchanging labeled IPv4 routes with ASBR2.
   
   ```
   [*ASBR1-bgp] peer 10.1.3.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] ipv4-family labeled-unicast
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 10.1.3.2 enable
   ```
   ```
   [*ASBR1-bgp-af-ipv4] quit
   ```
   
   The configurations of PE2 and ASBR2 are similar to the configurations of PE1 and ASBR1, respectively. For detailed configurations, see Configuration Files.
7. Establish an MP-EBGP peer relationship between PE1 and PE2. Configure PEs to filter received VPNv4 routes based on VPN targets and import labeled routes.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 as-number 200
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 connect-interface LoopBack0
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 ebgp-max-hop 10
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 enable
   ```
   ```
   [*PE1-bgp] import-rib public labeled-unicast
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 4.4.4.4 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-vpnv4] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface LoopBack0
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 ebgp-max-hop 10
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp] import-rib public labeled-unicast
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] policy vpn-target
   ```
   ```
   [*PE2-bgp-af-vpnv4] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
8. Establish unicast peer relationships and BGP MVPN peer relationships.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] bgp 65003
   ```
   ```
   [~CE1-bgp] ipv4-family unicast
   ```
   ```
   [~CE1-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*CE1-bgp-af-ipv4] import-route direct
   ```
   ```
   [*CE1-bgp-af-ipv4] peer 192.168.1.2 enable
   ```
   ```
   [*CE1-bgp-af-ipv4] commit
   ```
   ```
   [~CE1-bgp-af-ipv4] quit
   ```
   ```
   [~CE1-bgp] quit
   ```
   
   The configuration of CE2 is similar to the configuration of CE1. For detailed configurations, see Configuration Files.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family unicast
   ```
   ```
   [~PE1-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 4.4.4.4 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] commit
   ```
   ```
   [~PE1-bgp-af-ipv4] quit
   ```
   ```
   [~PE1-bgp] ipv4-family vpn-instance ng
   ```
   ```
   [~PE1-bgp-af-vpn-ng] import-route direct
   ```
   ```
   [*PE1-bgp-af-vpn-ng] peer 192.168.1.1 as-number 65003
   ```
   ```
   [*PE1-bgp-af-vpn-ng] commit
   ```
   ```
   [~PE1-bgp-af-vpn-ng] quit
   ```
   ```
   [~PE1-bgp] ipv4-family mvpn
   ```
   ```
   [~PE1-bgp-af-mvpn] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-mvpn] peer 4.4.4.4 enable
   ```
   ```
   [*PE1-bgp-af-mvpn] commit
   ```
   ```
   [~PE1-bgp-af-mvpn] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   The configuration on PE2 is similar to the configuration on PE1. For detailed configurations, see Configuration Files.
9. Configure PEs to use P2MP tunnels to carry multicast traffic.
   
   
   
   # Configure PE1 as a sender PE.
   
   ```
   [~PE1] multicast mvpn 1.1.1.1
   ```
   ```
   [~PE1] ip vpn-instance ng
   ```
   ```
   [~PE1-vpn-instance-ng] ipv4-family
   ```
   ```
   [~PE1-vpn-instance-ng-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] mvpn
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] sender-enable
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] auto-discovery inter-as
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] spt-only mode
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] ipmsi-tunnel
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn-ipmsi] mldp
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn-ipmsi] commit
   ```
   ```
   [~PE1-vpn-instance-ng-af-ipv4-mvpn-ipmsi] quit
   ```
   ```
   [~PE1-vpn-instance-ng-af-ipv4-mvpn] quit
   ```
   ```
   [~PE1-vpn-instance-ng-af-ipv4] quit
   ```
   ```
   [~PE1-vpn-instance-ng] quit
   ```
   
   # Configure PE2 as a receiver PE.
   
   ```
   [~PE2] multicast mvpn 4.4.4.4
   ```
   ```
   [~PE2] ip vpn-instance ng
   ```
   ```
   [~PE2-vpn-instance-ng] ipv4-family
   ```
   ```
   [~PE2-vpn-instance-ng-af-ipv4] multicast routing-enable
   ```
   ```
   [~PE2-vpn-instance-ng-af-ipv4] mvpn
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] auto-discovery inter-as
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] spt-only mode
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] ipmsi-tunnel
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn-ipmsi] commit
   ```
   ```
   [~PE2-vpn-instance-ng-af-ipv4-mvpn-ipmsi] quit
   ```
   ```
   [~PE2-vpn-instance-ng-af-ipv4-mvpn] quit
   ```
   ```
   [~PE2-vpn-instance-ng-af-ipv4] quit
   ```
   ```
   [~PE2-vpn-instance-ng] quit
   ```
10. Configure PIM.
    
    
    
    # Configure CE1.
    
    ```
    [~CE1] pim
    ```
    ```
    [~CE1-pim] static-rp 192.168.3.1
    ```
    ```
    [*CE1-pim] commit
    ```
    ```
    [~CE1-pim] quit
    ```
    ```
    [~CE1] multicast routing-enable
    ```
    ```
    [*CE1] interface GigabitEthernet0/1/0
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] pim sm
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] commit
    ```
    ```
    [~CE1-GigabitEthernet0/1/0] quit
    ```
    ```
    [~CE1] interface GigabitEthernet0/1/1
    ```
    ```
    [~CE1-GigabitEthernet0/1/1] pim sm
    ```
    ```
    [*CE1-GigabitEthernet0/1/1] commit
    ```
    ```
    [~CE1-GigabitEthernet0/1/1] quit
    ```
    
    # Configure CE2.
    
    ```
    [~CE2] pim
    ```
    ```
    [~CE2-pim] static-rp 192.168.3.1
    ```
    ```
    [*CE2-pim] commit
    ```
    ```
    [~CE2-pim] quit
    ```
    ```
    [~CE2] multicast routing-enable
    ```
    ```
    [*CE2] interface GigabitEthernet0/1/0
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] pim sm
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] igmp enable
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] commit
    ```
    ```
    [~CE2-GigabitEthernet0/1/0] quit
    ```
    ```
    [~CE2] interface GigabitEthernet0/1/1
    ```
    ```
    [~CE1-GigabitEthernet0/1/1] pim sm
    ```
    ```
    [*CE1-GigabitEthernet0/1/1] commit
    ```
    ```
    [~CE1-GigabitEthernet0/1/1] quit
    ```
    
    # Configure PE1.
    
    ```
    [~PE1] pim vpn-instance ng
    ```
    ```
    [*PE1-pim-ng] static-rp 192.168.3.1
    ```
    ```
    [*PE1-pim-ng] commit
    ```
    ```
    [~PE1-pim-ng] quit
    ```
    ```
    [~PE1] interface GigabitEthernet0/1/1
    ```
    ```
    [~PE1-GigabitEthernet0/1/1] pim sm
    ```
    ```
    [*PE1-GigabitEthernet0/1/1] commit
    ```
    ```
    [~PE1-GigabitEthernet0/1/1] quit
    ```
    
    The configuration on PE2 is similar to the configuration on PE1. For detailed configurations, see Configuration Files.
11. Verify the configuration.
    
    
    
    After the configuration is complete, CE1 and CE2 can learn routes to interfaces on each other and ping each other successfully.
    
    The command output on CE1 is used as an example.
    
    ```
    [~CE1] display ip routing-table
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ```
    ```
    ------------------------------------------------------------------------------
    ```
    ```
    Routing Tables Public
    ```
    ```
             Destinations : 8        Routes : 8
    ```
    ```
    Destination/Mask    Proto  Pre  Cost       Flags  NextHop         Interface
    ```
    ```
    192.168.1.0/24      Direct 0    0           D     192.168.1.1     GigabitEthernet0/1/0
    ```
    ```
    192.168.1.1/32      Direct 0    0           D     127.0.0.1       GigabitEthernet0/1/0
    ```
    ```
    192.168.1.255/32    Direct 0    0           D     127.0.0.1       GigabitEthernet0/1/0
    ```
    ```
    192.168.2.0/24     EBGP   255  0           D     192.168.1.2     GigabitEthernet0/1/0
    ```
    ```
    127.0.0.0/8         Direct 0    0           D     127.0.0.1       InLoopBack0
    ```
    ```
    127.0.0.1/32        Direct 0    0           D     127.0.0.1       InLoopBack0
    ```
    ```
    127.255.255.255/32  Direct 0    0           D     127.0.0.1       InLoopBack0
    ```
    ```
    255.255.255.255/32  Direct 0    0           D     127.0.0.1       InLoopBack0
    ```
    ```
    [~CE1] ping 192.168.2.2
    ```
    ```
      PING 192.168.2.2: 56  data bytes, press CTRL_C to break
    ```
    ```
        Reply from 192.168.2.2: bytes=56 Sequence=1 ttl=252 time=102 ms
    ```
    ```
        Reply from 192.168.2.2: bytes=56 Sequence=2 ttl=252 time=89 ms
    ```
    ```
        Reply from 192.168.2.2: bytes=56 Sequence=3 ttl=252 time=106 ms
    ```
    ```
        Reply from 192.168.2.2: bytes=56 Sequence=4 ttl=252 time=104 ms
    ```
    ```
        Reply from 192.168.2.2: bytes=56 Sequence=5 ttl=252 time=56 ms
    ```
    ```
      --- 192.168.2.2 ping statistics ---
    ```
    ```
        5 packet(s) transmitted
    ```
    ```
        5 packet(s) received
    ```
    ```
        0.00% packet loss
    ```
    ```
        round-trip min/avg/max = 56/91/106 ms
    ```
    
    ASBRs do not have VPNv4 routes. Run the **display bgp labeled routing-table label** command on an ASBR. The command output shows the label information of the routes.
    
    The following example uses the command output on ASBR1.
    
    ```
    [~ASBR1] display bgp labeled routing-table label
    ```
    ```
     BGP Local router ID is 2.2.2.2
    ```
    ```
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
    ```
    ```
                   h - history,  i - internal, s - suppressed, S - Stale
    ```
    ```
                   Origin : i - IGP, e - EGP, ? - incomplete
    ```
    ```
     Total Number of Routes: 2
    ```
    ```
            Network           NextHop           In/Out Label           Path Label
    ```
    ```
     *>i    1.1.1.1           1.1.1.1           48071/48061            NULL
    ```
    ```
     *>     4.4.4.4           10.1.3.2          48072/48074            NULL
    ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  bgp 65003
   peer 192.168.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 192.168.1.2 enable
  pim
   static-rp 192.168.3.1
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  multicast mvpn 1.1.1.1
  #
  ip vpn-instance ng
   ipv4-family
    route-distinguisher 1:3
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     spt-only mode
     auto-discovery inter-as
     ipmsi-tunnel
      mldp
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
   mldp p2mp 
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.000b.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance ng
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 ebgp-max-hop 10
   peer 4.4.4.4 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    import-rib public labeled-unicast
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   ipv4-family labeled-unicast
    network 1.1.1.1 255.255.255.255
    peer 2.2.2.2 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance ng
    import-route direct
    peer 192.168.1.1 as-number 65003
  #
  pim vpn-instance ng
   static-rp 192.168.3.1
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
   mldp p2mp
   mldp recursive-fec
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.000c.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 10.1.3.2 as-number 200
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    import-rib public labeled-unicast
    peer 10.1.3.2 enable
    peer 1.1.1.1 enable
   #
   ipv4-family labeled-unicast
    peer 1.1.1.1 enable
    peer 10.1.3.2 enable
  #
  ip route-static 3.3.3.3 255.255.255.255 10.1.3.2
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
   mldp p2mp
   mldp recursive-fec
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.000d.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  bgp 200
   peer 10.1.3.1 as-number 100
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    import-rib public labeled-unicast
    peer 10.1.3.1 enable
    peer 4.4.4.4 enable
   #
   ipv4-family labeled-unicast
    peer 4.4.4.4 enable
    peer 10.1.3.1 enable
  #
  ip route-static 2.2.2.2 255.255.255.255 10.1.3.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast mvpn 4.4.4.4
  #
  ip vpn-instance ng
   ipv4-family
    route-distinguisher 192.168.122.15:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     spt-only mode
     auto-discovery inter-as
     ipmsi-tunnel
      mldp
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls ldp
   mldp p2mp
   mldp recursive-fec
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.000e.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance ng
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
   isis enable 1
  #
  bgp 200
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 ebgp-max-hop 10
   peer 1.1.1.1 connect-interface LoopBack0
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    import-rib public labeled-unicast
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #
   ipv4-family labeled-unicast
    network 4.4.4.4 255.255.255.255
    peer 3.3.3.3 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance ng
    import-route direct
    peer 192.168.2.2 as-number 65004
  #
  pim vpn-instance ng
   static-rp 192.168.3.1
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.4.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  bgp 65004
   peer 192.168.2.1 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 192.168.2.1 enable
  #
  pim
   static-rp 192.168.3.1
  #
  return
  ```