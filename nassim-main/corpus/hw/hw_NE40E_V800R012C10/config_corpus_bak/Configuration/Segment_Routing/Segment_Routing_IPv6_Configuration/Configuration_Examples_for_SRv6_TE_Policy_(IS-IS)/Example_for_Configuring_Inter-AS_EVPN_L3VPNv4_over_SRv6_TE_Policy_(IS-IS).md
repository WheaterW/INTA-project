Example for Configuring Inter-AS EVPN L3VPNv4 over SRv6 TE Policy (IS-IS)
=========================================================================

This section provides an example for configuring an inter-AS SRv6 TE Policy to carry EVPN L3VPNv4 services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001180939086__fig_dc_vrp_srv6_cfg_all_001101):

* PE1 and ASBR1 belong to AS 100, and PE2 and ASBR2 belong to AS 200. Intra-AS IPv6 connectivity needs to be achieved for AS 100 and AS 200 through IS-IS.
* PE1 and ASBR1 belong to IS-IS process 1, and PE2 and ASBR2 belong to IS-IS process 10. PE1, ASBR1, PE2, and ASBR2 are all Level-1 devices.

It is required that a bidirectional inter-AS SRv6 TE Policy be deployed between PE1 and PE2 to carry EVPN L3VPNv4 services.

**Figure 1** Inter-AS EVPN L3VPNv4 over SRv6 TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001225940355.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, PE2, ASBR1, and ASBR2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title on PE1, PE2, ASBR1, and ASBR2.
3. Configure an EVPN L3VPN instance on both PE1 and PE2 and bind the EVPN L3VPN instance to an access-side interface.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Configure the PEs to advertise SRv6 locator routes through IS-IS and allocate intra-AS static End.X SIDs to the PEs.
6. Configure BGP EPEv6 on ASBR1 and ASBR2, and allocate inter-AS static End.X SIDs.
7. Establish a BGP EVPN peer relationship between the PEs, and configure the PEs to exchange BGP EVPN routes carrying SIDs through this peer relationship.
8. Deploy an SRv6 TE Policy between PE1 and PE2.
9. Configure a tunnel policy on PE1 and PE2 to import VPN traffic.

#### Precautions

During the configuration process, note the following:

* When configuring BGP EPEv6, you need to enable the BGP-LS address family peer relationship so that BGP EPEv6 can take effect.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IPv6 addresses on each device
* AS numbers of the PEs and ASBRs
* IS-IS process IDs, levels, and network entity titles of the PEs and ASBRs

* VPN instance names, RDs, and RTs on PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure PE1. The configurations of PE2, ASBR1, and ASBR2 are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001180939086__section_dc_vrp_srv6_cfg_all_001105) in this section.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:1::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:11::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   [*PE1-isis-1] is-level level-1
   [*PE1-isis-1] cost-style wide
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   [*PE1-isis-1] ipv6 enable topology ipv6
   [*PE1-isis-1] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] isis 1 
   [*ASBR1-isis-1] is-level level-1
   [*ASBR1-isis-1] cost-style wide
   [*ASBR1-isis-1] network-entity 10.0000.0000.0002.00
   [*ASBR1-isis-1] ipv6 enable topology ipv6
   [*ASBR1-isis-1] quit
   [*ASBR1] interface gigabitethernet 0/1/0
   [*ASBR1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*ASBR1-GigabitEthernet0/1/0] quit
   [*ASBR1] interface loopback1
   [*ASBR1-LoopBack1] isis ipv6 enable 1
   [*ASBR1-LoopBack1] commit
   [~ASBR1-LoopBack1] quit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] isis 10 
   [*ASBR2-isis-10] is-level level-1
   [*ASBR2-isis-10] cost-style wide
   [*ASBR2-isis-10] network-entity 10.0000.0000.0003.00
   [*ASBR2-isis-10] ipv6 enable topology ipv6
   [*ASBR2-isis-10] quit
   [*ASBR2] interface gigabitethernet 0/1/0
   [*ASBR2-GigabitEthernet0/1/0] isis ipv6 enable 10
   [*ASBR2-GigabitEthernet0/1/0] quit
   [*ASBR2] interface loopback1
   [*ASBR2-LoopBack1] isis ipv6 enable 10
   [*ASBR2-LoopBack1] commit
   [~ASBR2-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 10
   [*PE2-isis-10] is-level level-1
   [*PE2-isis-10] cost-style wide
   [*PE2-isis-10] network-entity 10.0000.0000.0004.00
   [*PE2-isis-10] ipv6 enable topology ipv6
   [*PE2-isis-10] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 10
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 10
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. PE1 is used as an example.
   
   ```
   [~PE1] display isis peer
   
                             Peer information for ISIS(1)
                            
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0            0000.0000.0002.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
3. Configure a VPN instance on each PE, enable the IPv4 address family for the instance, and bind the interface that connects each PE to a CE to the VPN instance on that PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv4-family
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both evpn
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   [*PE1-vpn-instance-vpna] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] ipv4-family
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both evpn
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   [*PE2-vpn-instance-vpna] quit
   [*PE2] interface gigabitethernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2] commit
   ```
   
   # Configure an IP address for each interface on the CEs, as shown in [Figure 1](#EN-US_TASK_0000001180939086__fig_dc_vrp_srv6_cfg_all_001101). For configuration details, see the configuration files.
   
   After the configuration is complete, run the **display ip vpn-instance verbose** command on the PEs to check VPN instance configurations. The command output shows that each PE can successfully ping its connected CE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a PE has multiple interfaces bound to the same VPN instance, specify a source IP address using the **-a** *source-ip-address* parameter in the **ping -vpn-instance** *vpn-instance-name* **-a** *source-ip-address dest-ip-address* command to ping the CE that is connected to the remote PE. If the source IP address is not specified, the ping operation may fail.
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   [*CE1-LoopBack1] ip address 11.11.11.11 32
   [*CE1-LoopBack1] quit
   [*CE1] bgp 65410
   [*CE1-bgp] peer 10.1.1.1 as-number 100
   [*CE1-bgp] network 11.11.11.11 32
   [*CE1-bgp] quit
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] ipv4-family vpn-instance vpna
   [*PE1-bgp-vpna] peer 10.1.1.2 as-number 65410
   [*PE1-bgp-vpna] import-route direct
   [*PE1-bgp-vpna] advertise l2vpn evpn
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface loopback 1
   [*CE2-LoopBack1] ip address 22.22.22.22 32
   [*CE2-LoopBack1] quit
   [*CE2] bgp 65420
   [*CE2-bgp] peer 10.2.1.1 as-number 200
   [*CE2-bgp] network 22.22.22.22 32
   [*CE2-bgp] quit
   [*CE2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   [*PE2-bgp] router-id 4.4.4.4
   [*PE2-bgp] ipv4-family vpn-instance vpna
   [*PE2-bgp-vpna] peer 10.2.1.2 as-number 65420  
   [*PE2-bgp-vpna] import-route direct
   [*PE2-bgp-vpna] advertise l2vpn evpn
   [*PE2-bgp-vpna] commit
   [~PE2-bgp-vpna] quit
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on each PE to check whether a BGP peer relationship has been established between the PE and its connected CE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpna peer
    BGP local router ID : 1.1.1.1
    Local AS number : 100
   
    VPN-Instance vpna, Router ID 1.1.1.1:
    Total number of peers : 1            Peers in established state : 1
   
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     10.1.1.2        4   65410  11     9          0     00:06:37   Established  1
   ```
5. Configure the PEs to advertise SRv6 locator routes through IS-IS and allocate intra-AS static End.X SIDs to the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:11::1
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] opcode ::100 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:1::2 no-flavor 
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] ipv6 enable topology ipv6 
   [*PE1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE1-isis-1] commit
   [~PE1-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:14::4
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:40:: 64 static 32
   [*PE2-segment-routing-ipv6-locator] opcode ::200 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:2::1 no-flavor
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 10
   [*PE2-isis-10] ipv6 enable topology ipv6 
   [*PE2-isis-10] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE2-isis-10] commit
   [~PE2-isis-10] quit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-x** **forwarding** command to check information about the SRv6 local SID table. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-x forwarding
   
                               My Local-SID End.X Forwarding Table       
                               -----------------------------------                 
   
   SID         : 2001:DB8:10::100/128                                            FuncType : End.X                   
   Flavor      : --                                                              SidCompress : NO 
   LocatorName : as1                                                             LocatorID: 1 
   ProtocolType: STATIC                                                          ProcessID: --
   UpdateTime  : 2021-08-30 01:49:44.292                                         NextHopCount: 1 
   NextHop     :                              Interface :                        ExitIndex:                        
   2001:DB8:1::2                              GigabitEthernet0/1/0               0x0000000e     
   TeFrrFlags  : --                                                              DelayTimerRemain: - 
   
   Total SID(s): 1
   ```
6. Configure BGP EPEv6 on ASBR1 and ASBR2, and allocate inter-AS static End.X SIDs.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   When configuring BGP EPEv6, you need to enable the BGP-LS address family peer relationship so that BGP EPEv6 can take effect.
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] segment-routing ipv6
   [*ASBR1-segment-routing-ipv6] encapsulation source-address 2001:DB8:12::2
   [*ASBR1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32
   [*ASBR1-segment-routing-ipv6-locator] opcode ::200 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:1::1 no-flavor
   [*ASBR1-segment-routing-ipv6-locator] quit
   [*ASBR1-segment-routing-ipv6] quit
   [*ASBR1] isis 1
   [*ASBR1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*ASBR1-isis-1] ipv6 import-route bgp level-1
   [*ASBR1-isis-1] commit
   [~ASBR1-isis-1] quit
   [~ASBR1] bgp 100 
   [*ASBR1-bgp] router-id 2.2.2.2
   [*ASBR1-bgp] segment-routing ipv6 egress-engineering locator as1 
   [*ASBR1-bgp] peer 2001:DB8:3::2 as-number 200 
   [*ASBR1-bgp] peer 2001:DB8:3::2 ebgp-max-hop 255
   [*ASBR1-bgp] peer 2001:DB8:3::2 egress-engineering srv6 inherit-global-locator
   [*ASBR1-bgp] peer 2001:DB8:3::2 egress-engineering srv6 static-sid no-flavor 2001:DB8:20::100
   [*ASBR1-bgp] ipv6-family unicast
   [*ASBR1-bgp-af-ipv6] peer 2001:DB8:3::2 enable
   [*ASBR1-bgp-af-ipv6] network 2001:DB8:11::1 128 
   [*ASBR1-bgp-af-ipv6] network 2001:DB8:10:: 64 
   [*ASBR1-bgp-af-ipv6] import-route direct
   [*ASBR1-bgp-af-ipv6] quit 
   [*ASBR1-bgp] link-state-family unicast 
   [*ASBR1-bgp-af-ls] peer 2001:DB8:3::2 enable 
   [*ASBR1-bgp-af-ls] quit 
   [*ASBR1-bgp] quit
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] segment-routing ipv6
   [*ASBR2-segment-routing-ipv6] encapsulation source-address 2001:DB8:13::3
   [*ASBR2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32
   [*ASBR2-segment-routing-ipv6-locator] opcode ::100 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:2::2 no-flavor
   [*ASBR2-segment-routing-ipv6-locator] quit
   [*ASBR2-segment-routing-ipv6] quit
   [*ASBR2] isis 10
   [*ASBR2-isis-10] segment-routing ipv6 locator as1 auto-sid-disable
   [*ASBR2-isis-10] ipv6 import-route bgp level-1
   [*ASBR2-isis-10] commit
   [~ASBR2-isis-10] quit
   [~ASBR2] bgp 200 
   [*ASBR2-bgp] router-id 3.3.3.3
   [*ASBR2-bgp] segment-routing ipv6 egress-engineering locator as1 
   [*ASBR2-bgp] peer 2001:DB8:3::1 as-number 100
   [*ASBR2-bgp] peer 2001:DB8:3::1 ebgp-max-hop 255
   [*ASBR2-bgp] peer 2001:DB8:3::1 egress-engineering srv6 inherit-global-locator
   [*ASBR2-bgp] peer 2001:DB8:3::1 egress-engineering srv6 static-sid no-flavor 2001:DB8:30::200  
   [*ASBR2-bgp] ipv6-family unicast
   [*ASBR2-bgp-af-ipv6] peer 2001:DB8:3::1 enable 
   [*ASBR2-bgp-af-ipv6] network 2001:DB8:14::4 128 
   [*ASBR2-bgp-af-ipv6] network 2001:DB8:40:: 64 
   [*ASBR2-bgp-af-ipv6] import-route direct
   [*ASBR2-bgp-af-ipv6] quit 
   [*ASBR2-bgp] link-state-family unicast 
   [*ASBR2-bgp-af-ls] peer 2001:DB8:3::1 enable 
   [*ASBR2-bgp-af-ls] quit 
   [*ASBR2-bgp] quit
   [*ASBR2] commit
   ```
   
   After the configuration is complete, run the **display bgp egress-engineering** command to check BGP EPE information. The command output shows SRv6 SID information. The following example uses the command output on ASBR1.
   
   ```
   [~ASBR1] display bgp egress-engineering 
                    
    Peer Node                     : 2001:DB8:3::2                  
    Peer Adj Num                  : 0                              
    Local ASN                     : 100                            
    Remote ASN                    : 200                            
    Local Router Id               : 2.2.2.2                        
    Remote Router Id              : 3.3.3.3                        
    Local Interface Address       : 2001:DB8:3::1                  
    Remote Interface Address      : 2001:DB8:3::2
    Usable Locator                : as1
    SRv6 SID                      : 2001:DB8:20::100               
    SRv6 SID (PSP)                : 2001:DB8:20::1:0:0             
    SRv6 SID (PSP,USP,USD)        : 2001:DB8:20::1:0:1             
    SRv6 SID (PSP,USP,USD,COC)    : -(ONLY SUPPORT COMPRESS TYPE)  
    Nexthop                       : 2001:DB8:3::2                  
    Out Interface                 : GigabitEthernet0/2/0  
   ```
7. Establish a BGP EVPN peer relationship between the PEs, and configure the PEs to exchange BGP EVPN routes carrying SIDs through this peer relationship.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] peer 2001:DB8:14::4 as-number 200
   [*PE1-bgp] peer 2001:DB8:14::4 ebgp-max-hop 255
   [*PE1-bgp] peer 2001:DB8:14::4 connect-interface loopback 1
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:14::4 enable
   [*PE1-bgp-af-evpn] peer 2001:DB8:14::4 advertise encap-type srv6
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] ipv4-family vpn-instance vpna
   [*PE1-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   [*PE1-bgp-vpna] segment-routing ipv6 locator as1 evpn
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   [~PE2-bgp] peer 2001:DB8:11::1 as-number 100
   [*PE2-bgp] peer 2001:DB8:11::1 ebgp-max-hop 255
   [*PE2-bgp] peer 2001:DB8:11::1 connect-interface loopback 1
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:11::1 enable
   [*PE2-bgp-af-evpn] peer 2001:DB8:11::1 advertise encap-type srv6
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] ipv4-family vpn-instance vpna
   [*PE2-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   [*PE2-bgp-vpna] segment-routing ipv6 locator as1 evpn
   [*PE2-bgp-vpna] commit
   [~PE2-bgp-vpna] quit
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs to check whether the BGP peer relationship has been established. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
                           
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   	
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:14::4                   4         200       76       74     0 01:01:32 Established        2
   ```
8. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:10::100
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:20::100
   [*PE1-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:DB8:30::100 
   [*PE1-segment-routing-ipv6-segment-list-list1] commit
   [~PE1-segment-routing-ipv6-segment-list-list1] quit
   [~PE1-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:14::4 color 101
   [*PE1-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:10::1000
   [*PE1-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE1-segment-routing-ipv6-policy-policy1-path] commit
   [~PE1-segment-routing-ipv6-policy-policy1-path] quit
   [~PE1-segment-routing-ipv6-policy-policy1] quit
   [~PE1-segment-routing-ipv6] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6 
   [~PE2-segment-routing-ipv6] segment-list list1 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:40::200          
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:30::200         
   [*PE2-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:DB8:20::200 
   [*PE2-segment-routing-ipv6-segment-list-list1] commit
   [~PE2-segment-routing-ipv6-segment-list-list1] quit
   [~PE2-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:11::1 color 101
   [*PE2-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:40::1000
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy1-path] commit
   [~PE2-segment-routing-ipv6-policy-policy1-path] quit
   [~PE2-segment-routing-ipv6-policy-policy1] quit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   After the configuration is complete, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy 
   PolicyName : policy1                                    
   Color                   : 101                            Endpoint             : 2001:DB8:14::4         
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -            
   Policy State            : Up                             State Change Time    : 2020-02-17 11:16:30
   Admin State             : Up                             Traffic Statistics   : Disable   
   Backup Hot-Standby      : Disable                        BFD                  : Disable   
   Interface Index         : -                              Interface Name       : - 
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : 2001:DB8:10::1000(Insert, preferred)
   Candidate-path Count    : 1                                
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary      
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0   
    Discriminator          : 100                            Binding SID          : 2001:DB8:10::1000     
    GroupId                : 1                              Policy Name          : policy1
    Template ID            : 0                              Path Verification    : Disable
    DelayTimerRemain       : -                              Network Slice ID     : -
    Segment-List Count     : 1            
     Segment-List          : list1                            
      Segment-List ID      : 1                              XcIndex              : 1            
      List State           : Up                             DelayTimerRemain     : -    
      Verification State   : -                              SuppressTimeRemain   : -
      PMTU                 : 9600                           Active PMTU          : 9600    
      Weight               : 1                              BFD State            : -
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -
      Binding SID          : -
      Reverse Binding ID   : -
      SID :        
            2001:DB8:10::100                                        
            2001:DB8:20::100                                        
            2001:DB8:30::100
   ```
9. Configure a tunnel policy to import VPN traffic.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] route-policy p1 permit node 10
   [*PE1-route-policy] apply extcommunity color 0:101
   [*PE1-route-policy] quit
   [*PE1] bgp 100
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:14::4 route-policy p1 import 
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] tunnel-policy p1
   [*PE1-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE1-tunnel-policy-p1] quit
   [*PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv4-family
   [*PE1-vpn-instance-vpna-af-ipv4] tnl-policy p1 evpn
   [*PE1-vpn-instance-vpna-af-ipv4] commit
   [~PE1-vpn-instance-vpna-af-ipv4] quit
   [~PE1-vpn-instance-vpna] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] route-policy p1 permit node 10
   [*PE2-route-policy] apply extcommunity color 0:101
   [*PE2-route-policy] quit
   [*PE2] bgp 200
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:11::1 route-policy p1 import 
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] tunnel-policy p1
   [*PE2-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE2-tunnel-policy-p1] quit
   [*PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] ipv4-family
   [*PE2-vpn-instance-vpna-af-ipv4] tnl-policy p1 evpn
   [*PE2-vpn-instance-vpna-af-ipv4] commit
   [~PE2-vpn-instance-vpna-af-ipv4] quit
   [~PE2-vpn-instance-vpna] quit
   ```
   
   After the configuration is complete, run the **display ip routing-table vpn-instance vpna** command to check the routing table of the specified VPN instance. The command output shows that the VPN route has successfully recursed to the SRv6 TE Policy.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpna 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                                              
   ------------------------------------------------------------------------------  
   Routing Table : vpna                                    
            Destinations : 8        Routes : 8             
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface    
   
          10.1.1.0/24  Direct  0    0             D   10.1.1.1        GigabitEthernet0/1/0
          10.1.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0 
        10.1.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0  
          10.2.1.0/24  EBGP    255  0             RD  2001:DB8:14::4  policy1   
       11.11.11.11/32  EBGP    255  0             RD  10.1.1.2        GigabitEthernet0/1/0  
       22.22.22.22/32  EBGP    255  0             RD  2001:DB8:14::4  policy1                    
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0                       
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
   ```
   ```
   [~PE1] display ip routing-table vpn-instance vpna 22.22.22.22 verbose 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                                              
   ------------------------------------------------------------------------------                                                      
   Routing Table : vpna                                    
   Summary Count : 1                                       
   
   Destination: 22.22.22.22/32                             
        Protocol: EBGP               Process ID: 0         
      Preference: 255                      Cost: 0         
         NextHop: 2001:DB8:14::4      Neighbour: 2001:DB8:14::4      
           State: Active Adv Relied         Age: 00h00m01s 
             Tag: 0                    Priority: low       
           Label: 3                     QoSInfo: 0x0       
      IndirectID: 0x10000E5            Instance:           
    RelayNextHop: ::                  Interface: policy1   
        TunnelID: 0x000000003400000001    Flags: RD  
      RouteColor: 0
   ```
10. Verify the configuration.
    
    
    
    Check that CEs belonging to the same VPN instance can ping each other. For example:
    
    ```
    [~CE1] ping -a 11.11.11.11 22.22.22.22
      PING 22.22.22.22: 56  data bytes, press CTRL_C to break         
        Reply from 22.22.22.22: bytes=56 Sequence=1 ttl=251 time=7 ms 
        Reply from 22.22.22.22: bytes=56 Sequence=2 ttl=251 time=3 ms 
        Reply from 22.22.22.22: bytes=56 Sequence=3 ttl=251 time=3 ms 
        Reply from 22.22.22.22: bytes=56 Sequence=4 ttl=251 time=3 ms 
        Reply from 22.22.22.22: bytes=56 Sequence=5 ttl=251 time=3 ms 
    
      --- 22.22.22.22 ping statistics ---                             
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
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
    tnl-policy p1 evpn
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:11::1                      
   locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32             
    opcode ::100 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:1::2 no-flavor        
   srv6-te-policy locator as1                             
   segment-list list1                                     
    index 5 sid ipv6 2001:DB8:10::100                              
    index 10 sid ipv6 2001:DB8:20::100                             
    index 15 sid ipv6 2001:DB8:30::100                             
   srv6-te policy policy1 endpoint 2001:DB8:14::4 color 101         
    binding-sid 2001:DB8:10::1000                                  
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
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:11::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:14::4 as-number 200
   peer 2001:DB8:14::4 ebgp-max-hop 255
   peer 2001:DB8:14::4 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn 
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.1.1.2 as-number 65410
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:14::4 enable
    peer 2001:DB8:14::4 route-policy p1 import 
    peer 2001:DB8:14::4 advertise encap-type srv6
  #
  route-policy p1 permit node 10                          
   apply extcommunity color 0:101 
  #
  tunnel-policy p1                                        
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1 
  #              
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1        
  #
  segment-routing ipv6 
   encapsulation source-address 2001:DB8:12::2                                   
   locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32             
    opcode ::200 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:1::1 no-flavor 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   ipv6 import-route bgp level-1
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
   ipv6 address 2001:DB8:3::1/96  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/128
   isis ipv6 enable 1
  #
  bgp 100                                                 
   router-id 2.2.2.2                                      
   segment-routing ipv6 egress-engineering locator as1    
   peer 2001:DB8:3::2 as-number 200                             
   peer 2001:DB8:3::2 ebgp-max-hop 255    
   peer 2001:DB8:3::2 egress-engineering srv6 inherit-global-locator                      
   peer 2001:DB8:3::2 egress-engineering srv6 static-sid no-flavor 2001:DB8:20::100          
   # 
   ipv4-family unicast                                    
    undo synchronization  
   #         
   link-state-family unicast                              
    peer 2001:DB8:3::2 enable
   #        
   ipv6-family unicast                                    
    undo synchronization                                    
    network 2001:DB8:10:: 64 
    network 2001:DB8:11::1 128                                     
    import-route direct                                   
    peer 2001:DB8:3::2 enable 
  #               
  return 
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2 
  #
  segment-routing ipv6  
   encapsulation source-address 2001:DB8:13::3                                  
   locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32             
    opcode ::100 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:2::2 no-flavor 
  #               
  isis 10          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   ipv6 import-route bgp level-1
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:2::1/96
   isis ipv6 enable 10 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:3::2/96  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:13::3/128
   isis ipv6 enable 10
  #
  bgp 200                                                 
   router-id 3.3.3.3                                      
   segment-routing ipv6 egress-engineering locator as1    
   peer 2001:DB8:3::1 as-number 100                             
   peer 2001:DB8:3::1 ebgp-max-hop 255   
   peer 2001:DB8:3::1 egress-engineering srv6 inherit-global-locator                       
   peer 2001:DB8:3::1 egress-engineering srv6 static-sid no-flavor 2001:DB8:30::200          
   #
   ipv4-family unicast                                    
    undo synchronization  
   #    
   link-state-family unicast                              
    peer 2001:DB8:3::1 enable
   # 
   ipv6-family unicast                                    
    undo synchronization                                  
    network 2001:DB8:14::4 128   
    network 2001:DB8:40:: 64                                   
    import-route direct                                   
    peer 2001:DB8:3::1 enable 
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
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
    tnl-policy p1 evpn
  #               
  segment-routing ipv6                                    
   encapsulation source-address 2001:DB8:14::4                      
   locator as1 ipv6-prefix 2001:DB8:40:: 64 static 32             
    opcode ::200 end-x interface GigabitEthernet0/1/0 nexthop 2001:DB8:2::1 no-flavor                 
   srv6-te-policy locator as1                             
   segment-list list1                                     
    index 5 sid ipv6 2001:DB8:40::200                              
    index 10 sid ipv6 2001:DB8:30::200                             
    index 15 sid ipv6 2001:DB8:20::200                             
   srv6-te policy policy1 endpoint 2001:DB8:11::1 color 101         
    binding-sid 2001:DB8:40::1000                                  
    candidate-path preference 100                         
     segment-list list1 
  #               
  isis 10          
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
   ipv6 address 2001:DB8:2::2/96
   isis ipv6 enable 10
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:14::4/128
   isis ipv6 enable 10
  #               
  bgp 200                                                 
   router-id 4.4.4.4                                      
   peer 2001:DB8:11::1 as-number 100                                
   peer 2001:DB8:11::1 ebgp-max-hop 255                             
   peer 2001:DB8:11::1 connect-interface LoopBack1                  
   # 
   ipv4-family unicast                                    
    undo synchronization                                  
   #              
   ipv6-family unicast                                    
    undo synchronization                                                                   
   #
   ipv4-family vpn-instance vpna                          
    import-route direct   
    advertise l2vpn evpn                                
    segment-routing ipv6 locator as1 evpn                      
    segment-routing ipv6 traffic-engineer best-effort evpn     
    peer 10.2.1.2 as-number 65420
   # 
   l2vpn-family evpn                                      
    policy vpn-target                                     
    peer 2001:DB8:11::1 enable                                      
    peer 2001:DB8:11::1 route-policy p1 import                      
    peer 2001:DB8:11::1 advertise encap-type srv6 
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
   peer 10.2.1.1 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    network 22.22.22.22 255.255.255.255
    peer 10.2.1.1 enable
  #
  return
  ```