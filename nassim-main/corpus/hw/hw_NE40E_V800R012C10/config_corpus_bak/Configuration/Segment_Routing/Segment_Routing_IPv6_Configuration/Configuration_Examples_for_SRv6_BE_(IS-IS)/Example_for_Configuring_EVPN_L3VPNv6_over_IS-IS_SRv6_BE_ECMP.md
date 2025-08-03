Example for Configuring EVPN L3VPNv6 over IS-IS SRv6 BE ECMP
============================================================

This section provides an example for configuring EVPN L3VPNv6 over SRv6 BE ECMP.

#### Networking Requirements

On the network shown in [Figure 1](dc_vrp_srv6_cfg_all_0030.html#EN-US_TASK_0193291221__fig_dc_vrp_srv6_cfg_all_001101):

* PE1, PE2, P1, and P2 are in the same AS and run IS-IS to implement IPv6 network connectivity.
* PE1, P1, P2, and PE2 are Level-2 devices that belong to IS-IS process 1.

It is required that a bidirectional SRv6 BE path be deployed between PE1 and PE2 to carry EVPN L3VPNv6 services. In addition, to maximize network resource utilization, it is required that ECMP be performed for EVPN L3VPNv6 services carried by the SRv6 BE path between PE1 and PE2.

**Figure 1** EVPN L3VPNv6 over SRv6 BE ECMP networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0193610399.png)

#### Precautions

During the configuration process, note the following:

* SRv6 BE ECMP depends on equal-cost routes on the network. To ensure successful configuration, you need to properly plan IGP costs for links. In this example, each link uses the default cost value 10.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, P1, P2, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity on PE1, P1, P2, and PE2. In addition, configure dynamic BFD for IPv6 IS-IS.
3. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish a BGP EVPN peer relationship between PEs.
6. Configure SRv6 on PE1 and PE2, and enable IS-IS SRv6.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, P1, P2, and PE2
* IS-IS process ID of PE1, P1, P2, and PE2
* IS-IS level of PE1, P1, P2, and PE2
* VPN instance name, RD, and RT on PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0193594064__section_dc_vrp_srv6_cfg_all_001105) in this section.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] ipv6 enable
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:db8:3::1 96
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:db8:11::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   
   
   When configuring IS-IS, enable dynamic BFD to speed up IS-IS convergence in the case of a link status change.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-2
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE1-isis-1] ipv6 bfd all-interfaces enable
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] interface loopback1
   ```
   ```
   [*PE1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE1-LoopBack1] commit
   ```
   ```
   [~PE1-LoopBack1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] bfd
   ```
   ```
   [*P1-bfd] quit
   ```
   ```
   [*P1] isis 1 
   ```
   ```
   [*P1-isis-1] is-level level-2
   ```
   ```
   [*P1-isis-1] cost-style wide
   ```
   ```
   [*P1-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P1-isis-1] ipv6 bfd all-interfaces enable
   ```
   ```
   [*P1-isis-1] quit
   ```
   ```
   [*P1] interface gigabitethernet 0/1/0
   ```
   ```
   [*P1-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P1] interface gigabitethernet 0/2/0
   ```
   ```
   [*P1-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P1] interface loopback1
   ```
   ```
   [*P1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P1-LoopBack1] commit
   ```
   ```
   [~P1-LoopBack1] quit
   ```
   
   # Configure P2.
   
   ```
   [~P2] bfd
   ```
   ```
   [*P2-bfd] quit
   ```
   ```
   [*P2] isis 1 
   ```
   ```
   [*P2-isis-1] is-level level-2
   ```
   ```
   [*P2-isis-1] cost-style wide
   ```
   ```
   [*P2-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*P2-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P2-isis-1] ipv6 bfd all-interfaces enable
   ```
   ```
   [*P2-isis-1] quit
   ```
   ```
   [*P2] interface gigabitethernet 0/1/0
   ```
   ```
   [*P2-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P2] interface gigabitethernet 0/2/0
   ```
   ```
   [*P2-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P2] interface loopback1
   ```
   ```
   [*P2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P2-LoopBack1] commit
   ```
   ```
   [~P2-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-2
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*PE2-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE2-isis-1] ipv6 bfd all-interfaces enable
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] interface loopback1
   ```
   ```
   [*PE2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE2-LoopBack1] commit
   ```
   ```
   [~PE2-LoopBack1] quit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   
                             Peer information for ISIS(1)
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0004* GE0/2/0            0000.0000.0004.02  Up   7s       L2       64 
   0000.0000.0002* GE0/1/0            0000.0000.0002.02  Up   9s       L2       64 
   
   Total Peer(s): 2
   ```
   
   # Display IS-IS routing table information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis route
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-2 Forwarding Table
                           --------------------------------
   
    IPV6 Dest.        ExitInterface      NextHop                    Cost     Flags    
   --------------------------------------------------------------------------------
   2001:DB8:11::/128  Loop1              Direct                     0        D/-/L/-  
   2001:DB8:12::/128  GE0/1/0            FE80::3A92:6CFF:FE31:307   10       A/-/-/-  
   2001:DB8:13::/128  GE0/1/0            FE80::3A92:6CFF:FE31:307   20       A/-/-/-  
                      GE0/2/0            FE80::3A92:6CFF:FE41:305                     
   2001:DB8:14::/128  GE0/2/0            FE80::3A92:6CFF:FE41:305   10       A/-/-/-  
   2001:DB8:1::/96    GE0/1/0            Direct                     10       D/-/L/-  
   2001:DB8:2::/96    GE0/1/0            FE80::3A92:6CFF:FE31:307   20       A/-/-/-  
   2001:DB8:3::/96    GE0/2/0            Direct                     10       D/-/L/-  
   2001:DB8:4::/96    GE0/2/0            FE80::3A92:6CFF:FE41:305   20       A/-/-/-  
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut, 
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv6-family
   [*PE1-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
   [*PE1-vpn-instance-vpna-af-ipv6] vpn-target 111:1 evpn
   [*PE1-vpn-instance-vpna-af-ipv6] quit
   [*PE1-vpn-instance-vpna] quit
   [*PE1] interface gigabitethernet0/3/0
   [*PE1-GigabitEthernet0/3/0] ip binding vpn-instance vpna
   [*PE1-GigabitEthernet0/3/0] ipv6 enable
   [*PE1-GigabitEthernet0/3/0] ipv6 address 2001:DB8:21::1 64
   [*PE1-GigabitEthernet0/3/0] quit
   [*PE1] bgp 100
   [*PE1-bgp] ipv6-family vpn-instance vpna
   [*PE1-bgp-6-vpna] import-route direct
   [*PE1-bgp-6-vpna] advertise l2vpn evpn
   [*PE1-bgp-6-vpna] quit
   [*PE1-bgp] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] ipv6-family
   [*PE2-vpn-instance-vpna-af-ipv6] route-distinguisher 200:1
   [*PE2-vpn-instance-vpna-af-ipv6] vpn-target 111:1 evpn
   [*PE2-vpn-instance-vpna-af-ipv6] quit
   [*PE2-vpn-instance-vpna] quit
   [*PE2] interface gigabitethernet0/3/0
   [*PE2-GigabitEthernet0/3/0] ip binding vpn-instance vpna
   [*PE2-GigabitEthernet0/3/0] ipv6 enable
   [*PE2-GigabitEthernet0/3/0] ipv6 address 2001:DB8:22::1 64
   [*PE2-GigabitEthernet0/3/0] quit
   [*PE2] bgp 100
   [*PE2-bgp] ipv6-family vpn-instance vpna
   [*PE2-bgp-6-vpna] import-route direct
   [*PE2-bgp-6-vpna] advertise l2vpn evpn
   [*PE2-bgp-6-vpna] quit
   [*PE2-bgp] quit
   [*PE2] commit
   ```
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface LoopBack1
   [*CE1-LoopBack1] ipv6 enable
   [*CE1-LoopBack1] ipv6 address 2001:DB8:111::111 128
   [*CE1-LoopBack1] quit               
   [*CE1] bgp 65410   
   [*CE1-bgp] router-id 10.11.1.1    
   [*CE1-bgp] peer 2001:DB8:21::1 as-number 100
   [*CE1-bgp] ipv6-family unicast
   [*CE1-bgp-af-ipv6] import-route direct
   [*CE1-bgp-af-ipv6] peer 2001:DB8:21::1 enable
   [*CE1-bgp-af-ipv6] commit
   [~CE1-bgp-af-ipv6] quit
   [~CE1-bgp] quit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] ipv6-family vpn-instance vpna
   [*PE1-bgp-6-vpna] peer 2001:DB8:21::2 as-number 65410
   [*PE1-bgp-6-vpna] import-route direct
   [*PE1-bgp-6-vpna] commit
   [~PE1-bgp-6-vpna] quit
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface LoopBack1
   [*CE2-LoopBack1] ipv6 enable
   [*CE2-LoopBack1] ipv6 address 2001:DB8:222::222 128
   [*CE2-LoopBack1] quit               
   [*CE2] bgp 65420   
   [*CE2-bgp] router-id 10.12.1.1    
   [*CE2-bgp] peer 2001:DB8:22::1 as-number 100
   [*CE2-bgp] ipv6-family unicast
   [*CE2-bgp-af-ipv6] import-route direct
   [*CE2-bgp-af-ipv6] peer 2001:DB8:22::1 enable
   [*CE2-bgp-af-ipv6] commit
   [~CE2-bgp-af-ipv6] quit
   [~CE2-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [~PE2-bgp] router-id 2.2.2.2
   [*PE2-bgp] ipv6-family vpn-instance vpna
   [*PE2-bgp-6-vpna] peer 2001:DB8:22::2 as-number 65420
   [*PE2-bgp-6-vpna] import-route direct
   [*PE2-bgp-6-vpna] commit
   [~PE2-bgp-6-vpna] quit
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv6 vpn-instance peer** command on the PEs and check whether BGP peer relationships have been established between the PEs and CEs. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv6 vpn-instance vpna peer
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     VPN-Instance vpna, Router ID 1.1.1.1:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:21::2  4       65410       98      103     0 01:22:02 Established        2
   ```
5. Establish a BGP EVPN peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] peer 2001:DB8:13::3 as-number 100
   [*PE1-bgp] peer 2001:DB8:13::3 connect-interface loopback 1
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:13::3 enable
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [~PE2-bgp] peer 2001:DB8:11::1 as-number 100
   [*PE2-bgp] peer 2001:DB8:11::1 connect-interface loopback 1
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:11::1 enable
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs and check whether BGP EVPN peer relationships have been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationships have been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:13::3                   4         100      100      100     0 01:22:17 Established        2
   ```
6. Establish an SRv6 BE path between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:11::1
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] segment-routing ipv6 locator as1
   [*PE1-isis-1] quit
   [*PE1] bgp 100
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:13::3 advertise encap-type srv6
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] ipv6-family vpn-instance vpna
   [*PE1-bgp-6-vpna] segment-routing ipv6 locator as1 evpn
   [*PE1-bgp-6-vpna] segment-routing ipv6 best-effort evpn
   [*PE1-bgp-6-vpna] quit
   [*PE1-bgp] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:13::3
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 1
   [*PE2-isis-1] segment-routing ipv6 locator as1
   [*PE2-isis-1] quit
   [*PE2] bgp 100
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:11::1 advertise encap-type srv6
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] ipv6-family vpn-instance vpna
   [*PE2-bgp-6-vpna] segment-routing ipv6 locator as1 evpn
   [*PE2-bgp-6-vpna] segment-routing ipv6 best-effort evpn
   [*PE2-bgp-6-vpna] quit
   [*PE2-bgp] quit
   [*PE2] commit
   ```
7. Verify the configuration.
   
   
   
   Run the [**display ipv6 routing-table vpn-instance vpna**](cmdqueryname=display+ipv6+routing-table+vpn-instance+vpna) *ipv6-address* **verbose** command to check VPN routing information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ipv6 routing-table vpn-instance vpna 2001:DB8:222::222 verbose 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
   Summary Count : 1
   
   Destination  : 2001:DB8:222::222                       PrefixLength : 128
   NextHop      : 2001:DB8:30::1:0:20                     Preference   : 255
   Neighbour    : 2001:DB8:13::3                          ProcessID    : 0
   Label        : NULL                                    Protocol     : IBGP
   State        : Active Adv Relied                       Cost         : 0
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   Priority     : low                                     Age          : 89sec
   IndirectID   : 0x100011B                               Instance     : 
   RelayNextHop : FE80::3A00:10FF:FE03:5                  TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                   Flags        : RD
   RouteColor   : 0                                       QoSInfo      : 0x0
   RelayNextHop : FE80::2200:10FF:FE03:4                  TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                   Flags        : RD
   ```
   
   The preceding command output shows that the VPN route **2001:DB8:222::222/128** has recursed to an SRv6 BE path.
   
   Display details about the IPv6 route using the next-hop address **2001:DB8:30::1:0:20** as the destination address.
   
   ```
   [~PE1] display ipv6 routing-table 2001:DB8:30::1:0:20 verbose  
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route 
   ------------------------------------------------------------------------------  
   Routing Table : _public_    
   Summary Count : 2           
   
   Destination  : 2001:DB8:30::                           PrefixLength : 64        
   NextHop      : FE80::3A00:10FF:FE03:5                  Preference   : 15        
   Neighbour    : ::                                      ProcessID    : 1         
   Label        : NULL                                    Protocol     : ISIS-L2   
   State        : Active Adv                              Cost         : 20        
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0         
   Priority     : medium                                  Age          : 132sec    
   IndirectID   : 0x100011B                               Instance     :           
   RelayNextHop : ::                                      TunnelID     : 0x0       
   Interface    : GigabitEthernet0/1/0                    Flags        : D         
   RouteColor   : 0                                       QoSInfo      : 0x0
   
   Destination  : 2001:DB8:30::                           PrefixLength : 64        
   NextHop      : FE80::3A00:10FF:FE03:4                  Preference   : 15        
   Neighbour    : ::                                      ProcessID    : 1         
   Label        : NULL                                    Protocol     : ISIS-L2   
   State        : Active Adv                              Cost         : 20        
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0         
   Priority     : medium                                  Age          : 132sec    
   IndirectID   : 0x100011C                               Instance     :           
   RelayNextHop : ::                                      TunnelID     : 0x0       
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   RouteColor   : 0                                       QoSInfo      : 0x0
   ```
   
   The preceding command output shows that the route **2001:DB8:30::1:0:20** has two outbound interfaces. These interfaces work in ECMP mode during packet forwarding.
   
   Check that CEs belonging to the same VPN instance can ping each other. The following example uses the command output on CE1.
   
   ```
   [~CE1] ping ipv6 -a 2001:DB8:111::111 2001:DB8:222::222
     PING 2001:DB8:222::222 : 56  data bytes, press CTRL_C to break
       Reply from 2001:DB8:222::222 
       bytes=56 Sequence=1 hop limit=62 time=690 ms
       Reply from 2001:DB8:222::222 
       bytes=56 Sequence=2 hop limit=62 time=5 ms
       Reply from 2001:DB8:222::222 
       bytes=56 Sequence=3 hop limit=62 time=4 ms
       Reply from 2001:DB8:222::222 
       bytes=56 Sequence=4 hop limit=62 time=6 ms
       Reply from 2001:DB8:222::222 
       bytes=56 Sequence=5 hop limit=62 time=3 ms
   
     --- 2001:DB8:222::222 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=3/141/690 ms
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
  #
  bfd
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:11::1
   locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
  #               
  isis 1          
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   ipv6 bfd all-interfaces enable
   segment-routing ipv6 locator as1
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:3::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip binding vpn-instance vpna
   ipv6 enable    
   ipv6 address 2001:DB8:21::1/64
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:11::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:13::3 as-number 100
   peer 2001:DB8:13::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv6-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 best-effort evpn
    peer 2001:DB8:21::2 as-number 65410
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:13::3 enable
    peer 2001:DB8:13::3 advertise encap-type srv6
  #               
  return
  ```
* P1 configuration file
  ```
  #
  sysname P1
  #
  bfd
  #               
  isis 1          
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   ipv6 bfd all-interfaces enable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::2/96
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:2::1/96
   isis ipv6 enable 1  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/128
   isis ipv6 enable 1
  #               
  return 
  ```
* P2 configuration file
  
  ```
  #
  sysname P2
  #
  bfd
  #               
  isis 1          
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #              
   ipv6 enable topology ipv6
   ipv6 bfd all-interfaces enable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:3::2/96
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:4::1/96
   isis ipv6 enable 1  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:14::4/128
   isis ipv6 enable 1
  #               
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
  #
  bfd
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:13::3
   locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32
  #               
  isis 1          
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   ipv6 bfd all-interfaces enable
   segment-routing ipv6 locator as1
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:4::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip binding vpn-instance vpna
   ipv6 enable    
   ipv6 address 2001:DB8:22::1/64
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:13::3/128
   isis ipv6 enable 1
  #
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:11::1 as-number 100
   peer 2001:DB8:11::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv6-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 best-effort evpn
    peer 2001:DB8:22::2 as-number 65420
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:11::1 enable
    peer 2001:DB8:11::1 advertise encap-type srv6
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
   ipv6 enable    
   ipv6 address 2001:DB8:21::2/64
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:111::111/128
  #               
  bgp 65410       
   router-id 10.11.1.1
   peer 2001:DB8:21::1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
    import-route direct
    peer 2001:DB8:21::1 enable
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
   ipv6 enable    
   ipv6 address 2001:DB8:22::2/64
  #
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:222::222/128
  #
  bgp 65420       
   router-id 10.12.1.1
   peer 2001:DB8:22::1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
    import-route direct
    peer 2001:DB8:22::1 enable
  #
  return
  ```