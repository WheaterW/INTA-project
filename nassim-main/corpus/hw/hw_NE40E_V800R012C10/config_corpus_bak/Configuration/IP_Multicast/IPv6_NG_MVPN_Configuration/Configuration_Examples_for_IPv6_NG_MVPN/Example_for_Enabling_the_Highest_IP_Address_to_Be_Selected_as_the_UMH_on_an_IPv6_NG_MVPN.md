Example for Enabling the Highest IP Address to Be Selected as the UMH on an IPv6 NG MVPN
========================================================================================

This section provides an example for enabling the highest IP address to be selected as the UMH on an IPv6 NG MVPN.

#### Networking Requirements

On an IPv6 NG MVPN, when multiple sender PEs exist, receiver PEs select routes based on preferred unicast routes by default. On the network shown in [Figure 1](#EN-US_TASK_0172367602__fig_dc_vrp_cfg_ngmvpn_001301), the receiver PE is PE3, and the sender PEs are PE1 and PE2. By default, the path to the source that PE3 selects based on preferential unicast routes is PE3-PE1-CE1. If the function of enabling the highest IP address to be selected as the UMH is enabled on PE3, the path selected is PE3-PE2-CE1.

**Figure 1** Enabling the highest IP address to be selected as the UMH on an IPv6 NG MVPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example are GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](images/route-ip-max_ipv6.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP MPLS/IP VPN to ensure that unicast VPN services are properly transmitted. (In this example, ensure that the source and user can communicate.)
2. Enable mLDP on all PEs globally and ensure that the PEs can use mLDP to establish P2MP tunnels.
3. Enable all PEs to establish BGP MVPN peer relationships and configure BGP to transmit A-D and C-multicast routes.
4. Configure PE1 and PE2 to use mLDP to establish an I-PMSI tunnel so that an mLDP P2MP LSP can be triggered.
5. Configure PIM on PE1 and PE2 interfaces bound to VPN instances and on the CE interfaces connecting to PEs to allow a VPN multicast routing table to be established to guide multicast traffic forwarding.
6. Enable the highest IP address to be selected as the UMH in the VPN instance IPv6 address family MVPN view of PE3.
7. Enable MLD on the multicast device's interface that is connected to users, implementing multicast group member management on the local network.

#### Data Preparation

To complete the configuration, you need the following data:

* Public network OSPF process ID: 1; area ID: 0
* VPN instance name on PE1, PE2, and PE3: VPNA, and data shown in [Figure 1](#EN-US_TASK_0172367602__fig_dc_vrp_cfg_ngmvpn_001301)

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Configure the VPN backbone network and the IP address of each interface in each VPN site.
      
      
      
      Configure an IP address for each interface. For detailed configurations, see [Figure 1](#EN-US_TASK_0172367602__fig_dc_vrp_cfg_ngmvpn_001301). For configuration details, see [Configuration Files](#EN-US_TASK_0172367602__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   2. Configure an IGP to interconnect devices on the BGP MPLS/IP VPN backbone network.
      
      
      
      OSPF is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0172367602__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   3. Configure basic MPLS functions and MPLS Label Distribution Protocol (LDP) on the backbone network to establish LDP label switch paths (LSPs).
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] mpls lsr-id 1.1.1.1
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
      [*PE1] interface GigabitEthernet0/1/0
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
      
      # Configure PE2.
      
      ```
      [~PE2] mpls lsr-id 2.2.2.2
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
      [*PE2] interface GigabitEthernet0/1/1
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls ldp
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] mpls lsr-id 3.3.3.3
      ```
      ```
      [*PE3] mpls
      ```
      ```
      [*PE3-mpls] quit
      ```
      ```
      [*PE3] mpls ldp
      ```
      ```
      [*PE3-mpls-ldp] quit
      ```
      ```
      [*PE3] interface GigabitEthernet0/1/0
      ```
      ```
      [*PE3-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*PE3-GigabitEthernet0/1/0] mpls ldp
      ```
      ```
      [*PE3-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE3] commit
      ```
      ```
      [*PE3] interface GigabitEthernet0/1/1
      ```
      ```
      [*PE3-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*PE3-GigabitEthernet0/1/1] mpls ldp
      ```
      ```
      [*PE3-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE3] commit
      ```
   4. Establish a Multiprotocol Internal Border Gateway Protocol (MP-IBGP) peer relationship between PEs.
      
      
      
      # Configure PE1.
      
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
      
      # Configure PE2.
      
      ```
      [~PE2] bgp 100
      ```
      ```
      [*PE2-bgp] peer 3.3.3.3 as-number 100
      ```
      ```
      [*PE2-bgp] peer 3.3.3.3 connect-interface LoopBack0
      ```
      ```
      [*PE2-bgp] ipv6-family vpnv6
      ```
      ```
      [*PE2-bgp-af-vpnv6] peer 3.3.3.3 enable
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
      
      # Configure PE3.
      
      ```
      [~PE3] bgp 100
      ```
      ```
      [*PE3-bgp] peer 2.2.2.2 as-number 100
      ```
      ```
      [*PE3-bgp] peer 2.2.2.2 connect-interface LoopBack0
      ```
      ```
      [*PE3-bgp] peer 1.1.1.1 as-number 100
      ```
      ```
      [*PE3-bgp] peer 1.1.1.1 connect-interface LoopBack0
      ```
      ```
      [*PE3-bgp] ipv6-family vpnv6
      ```
      ```
      [*PE3-bgp-af-vpnv6] peer 2.2.2.2 enable
      ```
      ```
      [*PE3-bgp-af-vpnv6] peer 1.1.1.1 enable
      ```
      ```
      [*PE3-bgp-af-vpnv6] quit
      ```
      ```
      [*PE3-bgp] quit
      ```
      ```
      [*PE3] commit
      ```
   5. Configure a VPN instance on each PE and bind the VPN instance on each PE to its interface connecting to CE1.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] ip vpn-instance VPNA
      ```
      ```
      [*PE1-vpn-instance-VPNA] ipv6-family
      ```
      ```
      [*PE1-vpn-instance-VPNA-af-ipv6] route-distinguisher 300:1
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
      [*PE1] interface GigabitEthernet0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] ipv6 enable
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] ipv6 address 2001:db8:3::1 64
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] ip vpn-instance VPNA
      ```
      ```
      [*PE2-vpn-instance-VPNA] ipv6-family
      ```
      ```
      [*PE2-vpn-instance-VPNA-af-ipv6] route-distinguisher 300:1
      ```
      ```
      [*PE2-vpn-instance-VPNA-af-ipv6] vpn-target 4:4
      ```
      ```
      [*PE2-vpn-instance-VPNA-af-ipv6] quit
      ```
      ```
      [*PE2-vpn-instance-VPNA] quit
      ```
      ```
      [*PE2] interface GigabitEthernet0/1/0
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] ip binding vpn-instance VPNA
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] ipv6 enable
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] ipv6 address 2001:db8:4::1 64
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] ip vpn-instance VPNA
      ```
      ```
      [*PE3-vpn-instance-VPNA] ipv6-family
      ```
      ```
      [*PE3-vpn-instance-VPNA-af-ipv6] route-distinguisher 300:1
      ```
      ```
      [*PE3-vpn-instance-VPNA-af-ipv6] vpn-target 3:3 4:4
      ```
      ```
      [*PE3-vpn-instance-VPNA-af-ipv6] quit
      ```
      ```
      [*PE3-vpn-instance-VPNA] quit
      ```
      ```
      [*PE3] interface GigabitEthernet0/1/2
      ```
      ```
      [*PE3-GigabitEthernet0/1/2] ip binding vpn-instance VPNA
      ```
      ```
      [*PE3-GigabitEthernet0/1/2] ipv6 enable
      ```
      ```
      [*PE3-GigabitEthernet0/1/2] ipv6 address 2001:db8:2::1 64
      ```
      ```
      [*PE3-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE3] commit
      ```
   6. Configure a static route to the source 2001:DB8:1::2 in the VPN instance on each PE, and import the static route to the VPN instance.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] ipv6 route-static vpn-instance VPNA 2001:db8:1:: 64 2001:db8:3::2
      ```
      ```
      [*PE1] bgp 100
      ```
      ```
      [*PE1-bgp] ipv6-family vpn-instance VPNA
      ```
      ```
      [*PE1-bgp-6-VPNA] import-route static
      ```
      ```
      [*PE1-bgp-6-VPNA] quit
      ```
      ```
      [*PE1-bgp] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] ipv6 route-static vpn-instance VPNA 2001:db8:1:: 64 2001:db8:4::2
      ```
      ```
      [*PE2] bgp 100
      ```
      ```
      [*PE2-bgp] ipv6-family vpn-instance VPNA
      ```
      ```
      [*PE2-bgp-6-VPNA] import-route static
      ```
      ```
      [*PE2-bgp-6-VPNA] quit
      ```
      ```
      [*PE2-bgp] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [*PE3] bgp 100
      ```
      ```
      [*PE3-bgp] ipv6-family vpn-instance VPNA
      ```
      ```
      [*PE3-bgp-6-VPNA] network 2001:db8:2:: 64
      ```
      ```
      [*PE3-bgp-6-VPNA] quit
      ```
      ```
      [*PE3-bgp] quit
      ```
      ```
      [*PE3] commit
      ```
   7. Check the route to the source 2001:DB8:1::2 on PE3.
      
      
      
      Run the [**display ipv6 routing-table vpn-instance VPNA**](cmdqueryname=display+ipv6+routing-table+vpn-instance+VPNA) command on PE3. The command output shows that there are routes to the source network segment and the selected path is PE3 -> PE1 -> CE1 -> Source.
      
      ```
      [~PE3] display ipv6 routing-table vpn-instance VPNA
       Routing Table : VPNA
                Destinations : 3        Routes : 3         
       Destination  : 2001:DB8:1::                         PrefixLength : 64
       NextHop      : ::FFFF:1.1.1.1                          Preference   : 255
       Cost         : 0                                       Protocol     : IBGP
       RelayNextHop : ::FFFF:10.1.1.1                         TunnelID     : 0x0000000001004c4bc3
       Interface    : Ethernet0/1/0                           Flags        : RD
      
       Destination  : 2001:DB8:3::                            PrefixLength : 64
       NextHop      : ::FFFF:1.1.1.1                          Preference   : 255
       Cost         : 0                                       Protocol     : IBGP
       RelayNextHop : ::FFFF:10.1.1.1                         TunnelID     : 0x0000000001004c4bc3
       Interface    : Ethernet0/1/0                           Flags        : RD
      
       Destination  : 2001:DB8:4::                            PrefixLength : 64
       NextHop      : ::FFFF:2.2.2.2                          Preference   : 255
       Cost         : 0                                       Protocol     : IBGP
       RelayNextHop : ::FFFF:10.1.4.1                         TunnelID     : 0x0000000001004c4b43
       Interface    : Ethernet0/1/1                           Flags        : RD
      ```
2. Enable mLDP globally.
   
   
   
   # Configure PE1.
   
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
   
   # Configure PE2.
   
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
   
   # Configure PE3.
   
   ```
   [~PE3] mpls ldp
   ```
   ```
   [*PE3-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE3-mpls-ldp] commit
   ```
   ```
   [~PE3-mpls-ldp] quit
   ```
3. Establish a BGP MVPN peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv6-family mvpn
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
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv6-family mvpn
   ```
   ```
   [*PE2-bgp-af-mvpnv6] peer 3.3.3.3 enable
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
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] ipv6-family mvpn
   ```
   ```
   [*PE3-bgp-af-mvpnv6] peer 1.1.1.1 enable
   ```
   ```
   [*PE3-bgp-af-mvpnv6] peer 2.2.2.2 enable
   ```
   ```
   [*PE3-bgp-af-mvpnv6] commit
   ```
   ```
   [~PE3-bgp-af-mvpnv6] quit
   ```
   ```
   [~PE3-bgp] quit
   ```
   
   After the configuration is complete, run the [**display bgp mvpn vpnv6 all peer**](cmdqueryname=display+bgp+mvpn+vpnv6+all+peer) command on the PEs. The command output shows that PE1 has established a BGP MVPN peer relationship with PE2 and PE3. The following example uses the command output on PE3.
   
   ```
   [~PE3] display bgp mvpn vpnv6 all peer
   ```
   ```
   BGP local router ID : 10.1.4.2
     Local AS number : 100
     Total number of peers : 2                 Peers in established state : 2
   
      Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
      1.1.1.1         4         100       44       43     0 00:31:58 Established        1    2.2.2.2         4         100       45       43     0 00:31:58 Established        1
   ```
4. Configure the device to use mLDP to establish an I-PMSI tunnel.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] multicast ipv6 mvpn 1.1.1.1
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
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] rpt-spt mode
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
   
   # Configure PE2.
   
   ```
   [~PE2] multicast ipv6 mvpn 2.2.2.2
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
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] sender-enable
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] rpt-spt mode
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] ipmsi-tunnel
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] mldp
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] quit
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
   
   # Configure PE3.
   
   ```
   [~PE3] multicast ipv6 mvpn 3.3.3.3
   ```
   ```
   [*PE3] ip vpn-instance VPNA
   ```
   ```
   [*PE3-vpn-instance-VPNA] ipv6-family
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] mvpn
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] rpt-spt mode
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA] quit
   ```
   ```
   [*PE3] commit
   ```
   
   After the configuration is complete, run the [**display mvpn ipv6 vpn-instance ipmsi**](cmdqueryname=display+mvpn+ipv6+vpn-instance+ipmsi) command on the PEs to check I-PMSI tunnel information. The following example uses the command output on PE3.
   
   ```
   [~PE3] display mvpn ipv6 vpn-instance VPNA ipmsi
   ```
   ```
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: mLDP P2MP LSP
   Tunnel state: --
   Root-ip: 1.1.1.1
   Opaque value: 0x01000400008002
   Root: 1.1.1.1 Leaf:   1: 3.3.3.3 (local)  
   Tunnel type: mLDP P2MP LSP
   Tunnel state: --
   Root-ip: 2.2.2.2
   Opaque value: 0x01000400008002
   Root: 2.2.2.2 Leaf:   1: 3.3.3.3 (local)
   ```
   
   The command outputs show that two mLDP P2MP LSPs have been established, with PE1 and PE2 as the root nodes respectively and PE3 as the leaf node.
5. Configure PIM.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] interface GigabitEthernet0/1/1
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
   
   # Configure PE2.
   
   ```
   [*PE2] interface GigabitEthernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [*PE3] interface GigabitEthernet0/1/2
   ```
   ```
   [*PE3-GigabitEthernet0/1/2] pim ipv6 sm
   ```
   ```
   [*PE3-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure CE1.
   
   ```
   [~CE1] multicast ipv6 routing-enable
   ```
   ```
   [*CE1] interface GigabitEthernet0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] interface GigabitEthernet0/1/1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] interface GigabitEthernet0/1/2
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] pim ipv6 sm
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] quit
   ```
6. Enable the highest IP address to be selected as the UMH in the VPN instance IPv6 address family MVPN view of PE3.
   
   
   ```
   [*PE3] ip vpn-instance VPNA
   ```
   ```
   [*PE3-vpn-instance-VPNA] ipv6-family
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] mvpn
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] umh-select highest-ip
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA] quit
   ```
7. Enable MLD on PE3.
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] interface GigabitEthernet0/1/2
   ```
   ```
   [*PE3-GigabitEthernet0/1/2] mld enable
   ```
   ```
   [*PE3-GigabitEthernet0/1/2] commit
   ```
   ```
   [~PE3-GigabitEthernet0/1/2] quit
   ```
8. Verifying the Configuration
   
   
   
   Run the [**display ipv6 routing-table vpn-instance VPNA**](cmdqueryname=display+ipv6+routing-table+vpn-instance+VPNA) command on PE3. The command output shows that the next hop of the optimal unicast path is PE1.
   
   ```
   [~PE3] display ipv6 routing-table vpn-instance VPNA
   ```
   ```
   Routing Table : VPNA
             Destinations : 3        Routes : 3         
   
    Destination  : 2001:DB8:1::                            PrefixLength : 64
    NextHop      : ::FFFF:1.1.1.1                          Preference   : 255
    Cost         : 0                                       Protocol     : IBGP
   RelayNextHop : ::FFFF:10.1.1.1                         TunnelID     : 0x0000000001004c4bc3
   Interface    : GigabitEthernet0/1/0                           Flags        : RD 
    Destination  : 2001:DB8:3::                            PrefixLength : 64
    NextHop      : ::FFFF:1.1.1.1                          Preference   : 255
    Cost         : 0                                       Protocol     : IBGP
    RelayNextHop : ::FFFF:10.1.1.1                         TunnelID     : 0x0000000001004c4bc3
    Interface    : GigabitEthernet0/1/0                           Flags        : RD
   
    Destination  : 2001:DB8:4::                            PrefixLength : 64
    NextHop      : ::FFFF:2.2.2.2                          Preference   : 255
    Cost         : 0                                       Protocol     : IBGP
    RelayNextHop : ::FFFF:10.1.4.1                         TunnelID     : 0x0000000001004c4b43
    Interface    : GigabitEthernet0/1/1                           Flags        : RD
   ```
   
   The next hop of the route selected in the scenario where the highest IP address is used as the UMH is used for User1 (S, G) join. Run the [**display pim ipv6 vpn-instance VPNA routing-table**](cmdqueryname=display+pim+ipv6+vpn-instance+VPNA+routing-table) command on PE3. The command output shows that the outbound interface to the next hop of the route is PE2. When the source sends multicast traffic to the (S, G), the user can receive the multicast traffic, and the traffic travels along the path PE3 -> PE2 -> CE1.
   
   ```
   [~PE3] display pim ipv6 vpn-instance VPNA routing-table
   ```
   ```
   VPN-Instance: VPNA
    Total 1 (S, G) entry
    
    (2001:DB8:1::2, FF3E::1)
        Protocol: pim-ssm, Flag: SG_RCVR 
        UpTime: 00:01:06
        Upstream interface: through-BGP, Refresh time: 00:01:06
            Upstream neighbor: ::FFFF:2.2.2.2          RPF prime neighbor: ::FFFF:2.2.2.2      Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/2
                Protocol: static, UpTime: 00:01:06, Expires: - 
   
   ```

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
    ipv6 address 2001:DB8:3::2/64
   pim ipv6 sm
  #
   interface GigabitEthernet0/1/2
    undo shutdown
    ipv6 enable
    ipv6 address 2001:DB8:1::1/64
    pim ipv6 sm
   #
   interface GigabitEthernet0/1/1
    undo shutdown
    ipv6 enable
    ipv6 address 2001:DB8:4::2/64
    pim ipv6 sm
   #
   return
  
  ```
  
  PE1 configuration file
  
  ```
  #
   sysname PE1
   #
   multicast ipv6 mvpn 1.1.1.1
   #
   ip vpn-instance VPNA
    ipv6-family
     route-distinguisher 300:1
    apply-label per-instance
     vpn-target 33:33 export-extcommunity
     vpn-target 33:33 import-extcommunity
     multicast ipv6 routing-enable
     mvpn
      sender-enable
      c-multicast signaling bgp
      rpt-spt mode
      ipmsi-tunnel
       mldp
   #
   mpls lsr-id 1.1.1.1
   #
   mpls
   #
   mldp-p2mp-tunnel p2mp-lsp
   #
   mpls ldp
    mldp p2mp
    #
    ipv4-family
   #
   interface GigabitEthernet0/1/1
    undo shutdown
    ip binding vpn-instance VPNA
    ipv6 enable
    ipv6 address 2001:DB8:3::1/64
    pim ipv6 sm
  #
   interface GigabitEthernet0/1/0
    undo shutdown
    ip address 10.1.1.1 255.255.255.0
    mpls
    mpls ldp
   #
   interface LoopBack0
    ip address 1.1.1.1 255.255.255.255
   #
   bgp 100
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
     import-route direct
     import-route static
   #
   ospf 1
    area 0.0.0.0
     network 1.1.1.1 0.0.0.0
     network 10.1.1.0 0.0.0.255
  #
  ipv6 route-static vpn-instance VPNA 2001:db8:1:: 64 2001:db8:3::2
  #
   return
  ```
* PE2 configuration file
  
  ```
  #
   sysname PE2
   #
   multicast ipv6 mvpn 2.2.2.2
   #
   ip vpn-instance VPNA
    ipv6-family
     route-distinguisher 300:1
   apply-label per-instance
     vpn-target 44:44 export-extcommunity
     vpn-target 44:44 import-extcommunity
     multicast ipv6 routing-enable
     mvpn
      sender-enable
      c-multicast signaling bgp
      rpt-spt mode
      ipmsi-tunnel
       mldp
   #
   mpls lsr-id 2.2.2.2
   #
   mpls
   #
   mldp-p2mp-tunnel p2mp-lsp
   #
   mpls ldp
    mldp p2mp
    #
    ipv4-family
   #
   interface GigabitEthernet0/1/1
    undo shutdown
    ip address 10.1.4.1 255.255.255.0
    mpls
    mpls ldp
  #
   interface GigabitEthernet0/1/0
    undo shutdown
    ip binding vpn-instance VPNA
    ipv6 enable    
    ip address 10.1.3.1 255.255.255.0
    ipv6 address 2001:DB8:4::1/64
    pim ipv6 sm
   #
   interface LoopBack0
    ip address 2.2.2.2 255.255.255.255
   #
   bgp 100
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
     import-route direct
     import-route static
   #
   ospf 1
    area 0.0.0.0
     network 2.2.2.2 0.0.0.0
     network 10.1.4.0 0.0.0.255
  #
  ipv6 route-static vpn-instance VPNA 2001:db8:1:: 64 2001:db8:4::2
  #
   return
  
  ```
* PE3 configuration file
  
  ```
  #
   sysname PE3
   #
   multicast ipv6 routing-enable
   #
   multicast ipv6 mvpn 3.3.3.3
   #
   ip vpn-instance VPNA
    ipv6-family
     route-distinguisher 300:1
    apply-label per-instance
     vpn-target 33:33 export-extcommunity
     vpn-target 44:44 export-extcommunity
     vpn-target 33:33 import-extcommunity
     vpn-target 44:44 import-extcommunity
     multicast ipv6 routing-enable
     mvpn
      c-multicast signaling bgp
      rpt-spt mode
      umh-select highest-ip
   #
   mpls lsr-id 3.3.3.3
   #
   mpls            
   #
   mpls ldp
    mldp p2mp
    #
    ipv4-family
   #
   interface GigabitEthernet0/1/1
   undo shutdown
    ipv6 enable
    ip address 10.1.4.2 255.255.255.0
    mpls
    mpls ldp
  #
   interface GigabitEthernet0/1/0
    undo shutdown
    ip address 10.1.1.2 255.255.255.0
    mpls
    mpls ldp
   #
   interface GigabitEthernet0/1/2
    undo shutdown  
    ip binding vpn-instance VPNA
    ipv6 enable
    ipv6 address 2001:DB8:2::1/64
     pim ipv6 sm
    mld enable
   #
   interface LoopBack0
    ip address 3.3.3.3 255.255.255.255
   #
   bgp 100
    peer 1.1.1.1 as-number 100
    peer 1.1.1.1 connect-interface LoopBack0
    peer 2.2.2.2 as-number 100
    peer 2.2.2.2 connect-interface LoopBack0
    #
    ipv4-family unicast
     undo synchronization
     peer 1.1.1.1 enable
     peer 2.2.2.2 enable
    #
    ipv6-family mvpn
     policy vpn-target
     peer 1.1.1.1 enable
     peer 2.2.2.2 enable
    #
    ipv6-family vpnv6
     policy vpn-target
     peer 1.1.1.1 enable
     peer 2.2.2.2 enable
    #
    ipv6-family vpn-instance VPNA
     network 2001:DB8:2:: 64
   #
   ospf 1
    area 0.0.0.0
     network 3.3.3.3 0.0.0.0
     network 10.1.1.0 0.0.0.255
     network 10.1.4.0 0.0.0.255
   #
   return
  
  ```