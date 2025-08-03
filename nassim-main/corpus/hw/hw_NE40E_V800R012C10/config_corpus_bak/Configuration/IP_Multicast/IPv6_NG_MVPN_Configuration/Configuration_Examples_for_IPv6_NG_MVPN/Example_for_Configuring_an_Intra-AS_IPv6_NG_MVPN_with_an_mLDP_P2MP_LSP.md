Example for Configuring an Intra-AS IPv6 NG MVPN with an mLDP P2MP LSP
======================================================================

This section provides an example for configuring an intra-AS IPv6 NG MVPN to carry multicast traffic over an mLDP P2MP LSP.

#### Networking Requirements

A next-generation multicast virtual private network (NG MVPN) is deployed on the service provider's backbone network to solve multicast service issues related to traffic congestion, transmission reliability, and data security. On the IPv6 NG MVPN networking shown in [Figure 1](#EN-US_TASK_0172367584__fig_dc_vrp_cfg_ngmvpn_021301), MPLS LDP LSPs have been deployed to carry BGP MPLS/IP VPN services. The service provider wants to provide MVPN services for users based on the existing IPv6 network. To meet this requirement, configure an intra-AS NG MVPN to carry multicast traffic over a Multipoint extensions for LDP (mLDP) point-to-multipoint (P2MP) LSP.

**Figure 1** Intra-AS NG MVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example are GE 0/1/0, GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_cfg_ngmvpn_021301.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP MPLS/IP VPN to ensure that unicast VPN services are properly transmitted. In this example, configure CE1 to communicate with CE2.
2. Enable mLDP globally on the provider edges (PEs) so that the PEs can use mLDP to establish a P2MP LSP.
3. Establish BGP MVPN peer relationships between the PEs so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.
4. Configure PE1 to use mLDP to establish an Inclusive-Provider Multicast Service Interface (I-PMSI) tunnel.
5. Configure PE1 to use mLDP to establish a Selective-Provider Multicast Service Interface (S-PMSI) tunnel so that an mLDP P2MP LSP can be triggered.
6. Configure PIM on the PE interfaces bound to VPN instances and on the CE interfaces connecting to PEs to allow a VPN multicast routing table to be established to guide multicast traffic forwarding.
7. Configure MLD on the interfaces connecting a multicast device to a user network segment to allow the device to manage multicast group members on the network segment.
8. Configure the interface connecting a user network segment to statically join an IPv6 multicast group.

#### Data Preparation

To complete the configuration, you need the following data:

* IS-IS process ID: 1
* VPN instance name on PE1 and PE2: VPNA (as shown in [Table 1](#EN-US_TASK_0172367584__table_dc_vrp_cfg_ngmvpn_021301))
  
  **Table 1** Data needed for each device
  | Device | IP Address of Loopback0 | MPLS LSR-ID | MVPN ID | RD | VPN-Target | AS Number |
  | --- | --- | --- | --- | --- | --- | --- |
  | CE1 | 1.1.1.1 | - | - | - | - | â |
  | PE1 | 2.2.2.2 | 2.2.2.2 | 2.2.2.2 | 2:2 | 3:3 | AS100 |
  | PE2 | 3.3.3.3 | 3.3.3.3 | 3.3.3.3 | 3:3 | 3:3 | AS100 |
  | CE2 | 4.4.4.4 | - | - | - | - | â |

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Configure the VPN backbone network and the IP address of each interface in each VPN site.
      
      
      
      Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0172367584__fig_dc_vrp_cfg_ngmvpn_021301). For configuration details, see [Configuration Files](#EN-US_TASK_0172367584__example_dc_vrp_cfg_ngmvpn_021301) in this section.
   2. Configure an IGP to interconnect devices on the BGP MPLS/IP VPN backbone network.
      
      
      
      IS-IS is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0172367584__example_dc_vrp_cfg_ngmvpn_021301) in this section.
   3. Configure basic MPLS functions, enable MPLS Label Distribution Protocol (LDP), and establish LDP Label Switch Paths (LSPs) on the backbone network.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] mpls lsr-id 2.2.2.2
        ```
        ```
        [*PE1] mpls
        ```
        ```
        [*PE1-mpls] quit
        ```
        ```
        [*PE1] mpls ldp
        ```
        ```
        [*PE1-mpls-ldp] quit
        ```
        ```
        [*PE1] interface gigabitethernet0/1/0
        ```
        ```
        [*PE1-GigabitEthernet0/1/0] mpls
        ```
        ```
        [*PE1-GigabitEthernet0/1/0] mpls ldp
        ```
        ```
        [*PE1-GigabitEthernet0/1/0] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] mpls lsr-id 3.3.3.3
        ```
        ```
        [*PE2] mpls
        ```
        ```
        [*PE2-mpls] quit
        ```
        ```
        [*PE2] mpls ldp
        ```
        ```
        [*PE2-mpls-ldp] quit
        ```
        ```
        [*PE2] interface gigabitethernet0/1/0
        ```
        ```
        [*PE2-GigabitEthernet0/1/0] mpls
        ```
        ```
        [*PE2-GigabitEthernet0/1/0] mpls ldp
        ```
        ```
        [*PE2-GigabitEthernet0/1/0] quit
        ```
        ```
        [*PE2] commit
        ```
   4. Establish a Multiprotocol Internal Border Gateway Protocol (MP-IBGP) peer relationship between PEs.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] bgp 100
        ```
        ```
        [*PE1-bgp] peer 3.3.3.3 as-number 100
        ```
        ```
        [*PE1-bgp] peer 3.3.3.3 connect-interface LoopBack0
        ```
        ```
        [*PE1-bgp] ipv6-family vpnv6
        ```
        ```
        [*PE1-bgp-af-vpnv6] peer 3.3.3.3 enable
        ```
        ```
        [*PE1-bgp-af-vpnv6] quit
        ```
        ```
        [*PE1-bgp] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] bgp 100
        ```
        ```
        [*PE2-bgp] peer 2.2.2.2 as-number 100
        ```
        ```
        [*PE2-bgp] peer 2.2.2.2 connect-interface LoopBack0
        ```
        ```
        [*PE2-bgp] ipv6-family vpnv6
        ```
        ```
        [*PE2-bgp-af-vpnv6] peer 2.2.2.2 enable
        ```
        ```
        [*PE2-bgp-af-vpnv6] quit
        ```
        ```
        [*PE2-bgp] quit
        ```
        ```
        [*PE2] commit
        ```
   5. Configure a VPN instance on each PE and bind the VPN instance on each PE to its interface connecting to a CE.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] ip vpn-instance VPNA
        ```
        ```
        [*PE1-vpn-instance-VPNA] ipv6-family
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv6] route-distinguisher 2:2
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv6] vpn-target 3:3
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv6] quit
        ```
        ```
        [*PE1-vpn-instance-VPNA] quit
        ```
        ```
        [*PE1] interface gigabitethernet0/1/1
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ipv6 enable
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ipv6 address 2001:db8:1::1 64
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] ip vpn-instance VPNA
        ```
        ```
        [*PE2-vpn-instance-VPNA] ipv6-family
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv6] route-distinguisher 3:3
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv6] vpn-target 3:3
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv6] quit
        ```
        ```
        [*PE2-vpn-instance-VPNA] quit
        ```
        ```
        [*PE2] interface gigabitethernet0/1/1
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] ipv6 enable
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] ipv6 address 2001:db8:2::1 64
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE2] commit
        ```
   6. Configure ISIS on each PE to import VPN routes.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] isis 1 vpn-instance VPNA
        ```
        ```
        [*PE1-isis-1] is-level level-1-2
        ```
        ```
        [*PE1-isis-1] network-entity 10.0000.0000.0002.00
        ```
        ```
        [*PE1-isis-1] ipv6 enable topology ipv6
        ```
        ```
        [*PE1-isis-1] ipv6 import-route bgp
        ```
        ```
        [*PE1-isis-1] quit
        ```
        ```
        [*PE1] interface gigabitethernet0/1/1
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] isis ipv6 enable 1
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE1] bgp 100
        ```
        ```
        [*PE1-bgp] ipv6-family vpn-instance VPNA
        ```
        ```
        [*PE1-bgp-VPNA] import-route isis 1
        ```
        ```
        [*PE1-bgp-VPNA] quit
        ```
        ```
        [*PE1-bgp] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] isis 1 vpn-instance VPNA
        ```
        ```
        [*PE2-isis-1] is-level level-1-2
        ```
        ```
        [*PE2-isis-1] network-entity 10.0000.0000.0003.00
        ```
        ```
        [*PE2-isis-1] ipv6 enable topology ipv6
        ```
        ```
        [*PE2-isis-1] ipv6 import-route bgp
        ```
        ```
        [*PE2-isis-1] quit
        ```
        ```
        [*PE2] interface gigabitethernet0/1/1
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] isis ipv6 enable 1
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE2] bgp 100
        ```
        ```
        [*PE2-bgp] ipv6-family vpn-instance VPNA
        ```
        ```
        [*PE2-bgp-VPNA] import-route isis 1
        ```
        ```
        [*PE2-bgp-VPNA] quit
        ```
        ```
        [*PE2-bgp] quit
        ```
        ```
        [*PE2] commit
        ```
   7. # Configure IS-IS on each CE.
      
      
      * # Configure CE1.
        
        ```
        [~CE1] isis 1
        ```
        ```
        [*CE1-isis-1] is-level level-2
        ```
        ```
        [*CE1-isis-1] network-entity 10.0000.0000.0001.00
        ```
        ```
        [*CE1-isis-1] ipv6 enable topology ipv6
        ```
        ```
        [*CE1-isis-1] quit
        ```
        ```
        [*CE1] interface gigabitethernet0/1/0
        ```
        ```
        [*CE1-GigabitEthernet0/1/0] isis ipv6 enable 1
        ```
        ```
        [*CE1-GigabitEthernet0/1/0] quit
        ```
        ```
        [*CE1] interface gigabitethernet0/1/1
        ```
        ```
        [*CE1-GigabitEthernet0/1/1] isis ipv6 enable 1
        ```
        ```
        [*CE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*CE1] commit
        ```
      * # Configure CE2.
        
        ```
        [~CE2] isis 1
        ```
        ```
        [*CE2-isis-1] is-level level-2
        ```
        ```
        [*CE2-isis-1] network-entity 10.0000.0000.0004.00
        ```
        ```
        [*CE2-isis-1] ipv6 enable topology ipv6
        ```
        ```
        [*CE2-isis-1] quit
        ```
        ```
        [*CE2] interface gigabitethernet0/1/0
        ```
        ```
        [*CE2-GigabitEthernet0/1/0] isis ipv6 enable 1
        ```
        ```
        [*CE2-GigabitEthernet0/1/0] quit
        ```
        ```
        [*CE2] interface gigabitethernet0/1/1
        ```
        ```
        [*CE2-GigabitEthernet0/1/1] isis ipv6 enable 1
        ```
        ```
        [*CE2-GigabitEthernet0/1/1] quit
        ```
        ```
        [*CE2] commit
        ```
      
      After the configurations are complete, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command on CE2. The command outputs show that CE2 has a route to CE1. Run the [**ping**](cmdqueryname=ping) command on CE2 to ping CE1. The command output shows that the ping operation is successful. The following example uses the command output on CE2:
      
      ```
      [~CE2] display ipv6 routing-table
      ```
      ```
      Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
      ------------------------------------------------------------------------------
      Routing Table : _Public_
               Destinations : 2        Routes : 2
      
       Destination  : 2001:DB8:1::2                   PrefixLength : 64
       NextHop      : 2001:DB8:2::1                   Preference   : 0
       Cost         : 0                               Protocol     : IS-IS
       RelayNextHop : ::                              TunnelID     : 0x0
       Interface    : GigabitEthernet0/1/0            Flags        : D
      
       Destination  : 2001:DB8:4::2                   PrefixLength : 64
       NextHop      : 2001:DB8:4::2                   Preference   : 0
       Cost         : 0                               Protocol     : Direct
       RelayNextHop : ::                              TunnelID     : 0x0
       Interface    : GigabitEthernet0/1/1            Flags        : D
      ```
      ```
      [~CE2] ping ipv6 2001:db8:1::2
      ```
      ```
        PING 2001:DB8:1::2: 56  data bytes, press CTRL_C to break
          Reply from 2001:DB8:1::2: bytes=56 Sequence=1 ttl=253 time=118 ms
          Reply from 2001:DB8:1::2: bytes=56 Sequence=2 ttl=253 time=3 ms
          Reply from 2001:DB8:1::2: bytes=56 Sequence=3 ttl=253 time=4 ms
          Reply from 2001:DB8:1::2: bytes=56 Sequence=4 ttl=253 time=3 ms
          Reply from 2001:DB8:1::2: bytes=56 Sequence=5 ttl=253 time=3 ms
      
        --- 2001:DB8:1::2 ping statistics ---
          5 packet(s) transmitted
          5 packet(s) received
          0.00% packet loss
          round-trip min/avg/max = 3/26/118 ms                     
      ```
2. Enable mLDP globally.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] mpls ldp
     ```
     ```
     [*PE1-mpls-ldp] mldp p2mp
     ```
     ```
     [*PE1-mpls-ldp] commit
     ```
     ```
     [~PE1-mpls-ldp] quit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] mpls ldp
     ```
     ```
     [*PE2-mpls-ldp] mldp p2mp
     ```
     ```
     [*PE2-mpls-ldp] commit
     ```
     ```
     [~PE2-mpls-ldp] quit
     ```
3. Establish a BGP MVPN peer relationship between the PEs.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] bgp 100
     ```
     ```
     [~PE1-bgp] ipv6-family mvpn
     ```
     ```
     [*PE1-bgp-af-mvpnv6] peer 3.3.3.3 enable
     ```
     ```
     [*PE1-bgp-af-mvpnv6] commit
     ```
     ```
     [~PE1-bgp-af-mvpnv6] quit
     ```
     ```
     [~PE1-bgp] quit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] bgp 100
     ```
     ```
     [~PE2-bgp] ipv6-family mvpn
     ```
     ```
     [*PE2-bgp-af-mvpnv6] peer 2.2.2.2 enable
     ```
     ```
     [*PE2-bgp-af-mvpnv6] commit
     ```
     ```
     [~PE2-bgp-af-mvpnv6] quit
     ```
     ```
     [~PE2-bgp] quit
     ```
   
   After the configurations are complete, run the [**display bgp mvpn vpnv6 all peer**](cmdqueryname=display+bgp+mvpn+vpnv6+all+peer) command on the PEs. The command output shows that PE1 has established a BGP MVPN peer relationship with PE2. The following example uses the command output on PE1:
   
   ```
   [~PE1] display bgp mvpn vpnv6 all peer
   ```
   ```
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.3         4         100      107      112     0 01:22:50 Established        3
   ```
4. Configure each PE to use mLDP to establish an I-PMSI tunnel, and configure S-PMSI.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] multicast ipv6 mvpn 2.2.2.2
     ```
     ```
     [*PE1] ip vpn-instance VPNA
     ```
     ```
     [*PE1-vpn-instance-VPNA] ipv6-family
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6] mvpn
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] sender-enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] ipmsi-tunnel
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] mldp
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] spmsi-tunnel
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-spmsi] group FF15:: 64 source 2001:DB8:3::9 64 mldp limit 1
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-spmsi] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] multicast ipv6 mvpn 3.3.3.3
     ```
     ```
     [*PE2] ip vpn-instance VPNA
     ```
     ```
     [*PE2-vpn-instance-VPNA] ipv6-family
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6] mvpn
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA] quit
     ```
     ```
     [*PE2] commit
     ```
5. Configure PIM.
   
   
   * # Configure PE1.
     
     ```
     [*PE1] interface gigabitethernet0/1/1
     ```
     ```
     [*PE1-GigabitEthernet0/1/1] pim ipv6 sm
     ```
     ```
     [*PE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure CE1.
     
     ```
     [~CE1] multicast ipv6 routing-enable
     ```
     ```
     [*CE1] interface gigabitethernet0/1/0
     ```
     ```
     [*CE1-GigabitEthernet0/1/0] pim ipv6 sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE1] interface gigabitethernet0/1/1
     ```
     ```
     [*CE1-GigabitEthernet0/1/1] pim ipv6 sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE1] commit
     ```
   * # Configure PE2.
     
     ```
     [*PE2] interface gigabitethernet0/1/1
     ```
     ```
     [*PE2-GigabitEthernet0/1/1] pim ipv6 sm
     ```
     ```
     [*PE2-GigabitEthernet0/1/1] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure CE2.
     
     ```
     [~CE2] multicast ipv6 routing-enable
     ```
     ```
     [*CE2] interface gigabitethernet0/1/0
     ```
     ```
     [*CE2-GigabitEthernet0/1/0] pim ipv6 sm
     ```
     ```
     [*CE2-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE2] interface gigabitethernet0/1/1
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] pim ipv6 sm
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE2] commit
     ```
6. Configure MLD.
   
   
   * # Configure CE2.
     
     ```
     [~CE2] interface gigabitethernet0/1/1
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] mld enable
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] mld static-group FF3E::1 source 2001:DB8:3::2
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] commit
     ```
     ```
     [~CE2-GigabitEthernet0/1/1] quit
     ```
7. Verify the configuration.
   
   
   
   After the configurations are complete, IPv6 NG MVPN functions have been configured. If CE2 has access users, CE1 can use the BGP MPLS/IP VPN to forward multicast data to the users. After a static multicast entry is configured users of CE2 to join the multicast group FF3E::1 and the multicast source 2001:DB8:3::2 to send multicast data, check multicast routing entries to verify whether the IPv6 NG MVPN is configured successfully.
   
   Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) command on CE2 and CE1 to check their PIM routing tables.
   
   ```
   [~CE2] display pim ipv6 routing-table
   ```
   ```
    VPN-Instance: public net
    Total 1 (S, G) entry
   
    (2001:DB8:3::2, FF3E::1)
        Protocol: pim-ssm, Flag: SG_RCVR
        UpTime: 00:24:07
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:24:07
            Upstream neighbor: 2001:DB8:2::1
            RPF prime neighbor: 2001:DB8:2::1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: static, UpTime: 00:24:07, Expires: -
   
   ```
   ```
   [~PE2] display pim ipv6 vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 1 (S, G) entry
   
    (2001:DB8:3::2, FF3E::1)
        Protocol: pim-ssm, Flag:
        UpTime: 00:24:09
        Upstream interface: through-BGP, Refresh time: 00:24:09
            Upstream neighbor: ::FFFF:2.2.2.2
            RPF prime neighbor: ::FFFF:2.2.2.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-ssm, UpTime: 00:24:09, Expires: 00:02:35
   
   ```
   ```
   [~CE1] display pim ipv6 routing-table
   ```
   ```
    VPN-Instance: public net
    Total 1 (S, G) entry
   
    (2001:DB8:3::2, FF3E::1)
         Protocol: pim-ssm, Flag: LOC
        UpTime: 00:24:09
        Upstream interface: GigabitEthernet0/1/1, Refresh time: 00:24:09
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                Protocol: pim-ssm, UpTime: 00:24:09, Expires: -
   
   ```
   
   The command outputs show that the CE connected to the multicast source has received PIM Join messages from the CE connected to multicast receivers and that PIM routing entries are generated.

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  multicast ipv6 routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
   isis ipv6 enable 1
   pim ipv6 sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   isis ipv6 enable 1
   pim ipv6 sm
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  isis 1
   is-level level-2
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0001.00
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  multicast ipv6 mvpn 2.2.2.2
  #
  ip vpn-instance VPNA
   ipv6-family
    route-distinguisher 2:2
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast ipv6 routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     ipmsi-tunnel
      mldp
     spmsi-tunnel
      group FF15:: 64 source 2001:DB8:3:: 64 mldp limit 1
  #
  mpls lsr-id 2.2.2.2
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  isis 1 vpn-instance VPNA
   is-level level-1-2
   network-entity 10.0000.0000.0002.00
   ipv6 enable topology ipv6
   ipv6 import-route bgp
  #
  isis 2
   is-level level-2
   network-entity 49.0002.0010.0010.1023.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 2
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   isis ipv6 enable 1
   pim ipv6 sm
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 2
  #
  bgp 100
   router-id 2.2.2.2
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   ipv6-family mvpn
    policy vpn-target
    peer 3.3.3.3 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 3.3.3.3 enable
   #
   ipv6-family vpn-instance VPNA
    import-route isis 1
  #
  return
  
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  multicast ipv6 routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   isis ipv6 enable 1
   pim ipv6 sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   isis ipv6 enable 1
   mld enable
   mld static-group FF3E::1 source 2001:DB8:3::2
   pim ipv6 sm
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  isis 1
   is-level level-2
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0004.00
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast ipv6 mvpn 3.3.3.3
  #
  ip vpn-instance VPNA
   ipv6-family
    route-distinguisher 3:3
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast ipv6 routing-enable
    mvpn
     c-multicast signaling bgp
  #
  mpls lsr-id 3.3.3.3
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  isis 1 vpn-instance VPNA
   is-level level-1-2
   network-entity 10.0000.0000.0003.00
   ipv6 enable topology ipv6
   ipv6 import-route bgp
  #
  isis 2
   is-level level-2
   network-entity 49.0002.0010.0010.1024.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   isis enable 2
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   isis ipv6 enable 1
   pim ipv6 sm
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   isis enable 2
  #
  bgp 100
   router-id 3.3.3.3
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   ipv6-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv6-family vpn-instance VPNA
    import-route isis 1
  #
  return
  
  ```