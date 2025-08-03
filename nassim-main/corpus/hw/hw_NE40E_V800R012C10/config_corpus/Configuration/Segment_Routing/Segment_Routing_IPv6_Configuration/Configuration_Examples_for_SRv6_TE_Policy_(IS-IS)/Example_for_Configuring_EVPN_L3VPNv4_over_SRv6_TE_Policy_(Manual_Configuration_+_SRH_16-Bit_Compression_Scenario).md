Example for Configuring EVPN L3VPNv4 over SRv6 TE Policy (Manual Configuration + SRH 16-Bit Compression Scenario)
=================================================================================================================

This section provides an example for configuring an SRv6 TE Policy to carry EVPN L3VPNv4 services in a 16-bit compression scenario.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The SRv6 SRH 16-bit compression function can be used only after the required license is loaded.

On the network shown in [Figure 1](#EN-US_TASK_0000001464484277__fig3691666259), PE1, P1, P2, and PE2 are in the same AS. They need to run IS-IS to achieve IPv6 network connectivity. A bidirectional SRv6 TE Policy needs to be deployed between PE1 and PE2 to carry EVPN L3VPNv4 services. In addition, to reduce the SRv6 header size, SRH compression is required.

**Figure 1** Networking diagram for configuring EVPN L3VPNv4 over SRv6 TE Policy in an SRH 16-bit compression scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and interface2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001464604169.png "Click to enlarge")

#### Precautions

1. SRv6 TE Policy configuration requires End or End.X SIDs. The SIDs can either be configured manually or be generated dynamically using an IGP. In scenarios where SRv6 TE Policies are configured manually, dynamic SIDs used for the SRv6 TE Policies may change after an IGP restart. In this case, you need to manually adjust the SRv6 TE Policies so that they remain up. For this reason, dynamic SIDs are not suitable for large-scale use. You are therefore advised to configure SIDs manually and not to use dynamic SIDs.
2. To implement color-based traffic steering into SRv6 TE Policies, you need to configure the color attribute using an import or export route-policy. In addition, configure a tunnel policy to allow routes to recurse to SRv6 TE Policies.
   
   After the preceding configurations are complete, if the color and next hop of a route are the same as the color and endpoint of an SRv6 TE Policy, respectively, the route can successfully recurse to the SRv6 TE Policy. This enables the traffic forwarded through the route to be steered into the SRv6 TE Policy.
3. When configuring a segment list, you need to run the [**index**](cmdqueryname=index) *index* **sid** **ipv6** *ipv6address* **compress-16** **block** *block-value* command, with the value of *block-value* being the same as the value obtained by subtracting 16 from the value of *mask-length* specified in the [**locator**](cmdqueryname=locator) *locator-name* **compress-16** **ipv6-prefix** *ipv6-address* *mask-length* [ **compress-static** *compress-length* | **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* command.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, P1, P2, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title on PE1, P1, P2, and PE2.
3. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish a BGP EVPN peer relationship between the PEs.
6. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, P1, P2, and PE2. In addition, configure PE1 and PE2 to advertise VPN routes carrying SIDs.
7. Deploy an SRv6 TE Policy between PE1 and PE2.
8. Configure a tunnel policy on PE1 and PE2 to import VPN traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, P1, P2, and PE2
* IS-IS process ID of PE1, P1, P2, and PE2
* IS-IS level of PE1, P1, P2, and PE2
* VPN instance names, RDs, and RTs on PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure PE1. The configurations of P1, P2, and PE2 are similar to the configuration of PE1. For configuration details, see the configuration files.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
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
   [*PE1] interface loopback1
   ```
   ```
   [*PE1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure P1.
   
   ```
   [~P1] isis 1 
   ```
   ```
   [*P1-isis-1] is-level level-1
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
   [*P1-LoopBack1] quit
   ```
   ```
   [*P1] commit
   ```
   
   # Configure P2.
   
   ```
   [~P2] isis 1 
   ```
   ```
   [*P2-isis-1] is-level level-1
   ```
   ```
   [*P2-isis-1] cost-style wide
   ```
   ```
   [*P2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*P2-isis-1] ipv6 enable topology ipv6
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
   [*P2-LoopBack1] quit
   ```
   ```
   [*P2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*PE2-isis-1] ipv6 enable topology ipv6
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
   [*PE2] interface loopback1
   ```
   ```
   [*PE2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured.
   
   # Display IS-IS neighbor information. PE1 is used as an example.
   
   ```
   [~PE1] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
                            
     System Id     Interface         Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0           0000.0000.0002.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
3. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.11.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpna] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.22.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-LoopBack1] ip address 11.1.1.1 32
   ```
   ```
   [*CE1-LoopBack1] quit
   ```
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] router-id 11.1.1.1
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
   [*PE1-bgp] router-id 1.1.1.1
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
   [*CE2-LoopBack1] ip address 22.2.2.2 32
   ```
   ```
   [*CE2-LoopBack1] quit
   ```
   ```
   [*CE2] bgp 65420
   ```
   ```
   [*CE2-bgp] router-id 22.2.2.2
   ```
   ```
   [*CE2-bgp] peer 10.22.1.1 as-number 100
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
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] router-id 4.4.4.4
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
   [*PE2-bgp-vpna] advertise l2vpn evpn
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
     10.11.1.2       4       65410       79       83     0 01:33:24 Established        2 
   ```
5. Establish a BGP EVPN peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:DB8:4::4 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:4::4 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:4::4 enable
   ```
   ```
   [*PE1-bgp-af-evpn] quit
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
   [~PE2-bgp] peer 2001:DB8:1::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs to check whether a BGP EVPN peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationship has been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
   
    BGP local router ID : 1.1.1.1   
    Local AS number : 100         
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:4::4                    4         100      172      176     0 02:25:10 Established        2
   ```
6. Configure SRv6 SIDs and configure the PEs to advertise VPN routes carrying SIDs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] compress-16 enable
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1 compress-16 ipv6-prefix 2001:DB8:100:1:: 64 compress-static 8 static 32
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode compress ::E012 end psp-usd-next
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode ::E000:0:0:55 end-op 
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:4::4 advertise encap-type srv6 advertise-srv6-locator
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE1-bgp-vpna] segment-routing ipv6 locator PE1 compress evpn
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
   ```
   [~PE1] isis 1
   ```
   ```
   [~PE1-isis-1] segment-routing ipv6 locator PE1 auto-sid-disable
   ```
   ```
   [*PE1-isis-1] commit
   ```
   ```
   [~PE1-isis-1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] segment-routing ipv6
   ```
   ```
   [*P1-segment-routing-ipv6] compress-16 enable
   ```
   ```
   [*P1-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*P1-segment-routing-ipv6] locator P1 compress-16 ipv6-prefix 2001:DB8:100:2:: 64 compress-static 8 static 32
   ```
   ```
   [*P1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P1-segment-routing-ipv6] quit
   ```
   ```
   [*P1] isis 1
   ```
   ```
   [*P1-isis-1] segment-routing ipv6 locator P1 auto-sid-disable
   ```
   ```
   [*P1-isis-1] commit
   ```
   ```
   [~P1-isis-1] quit
   ```
   
   # Configure P2.
   
   ```
   [~P2] segment-routing ipv6
   ```
   ```
   [*P2-segment-routing-ipv6] compress-16 enable
   ```
   ```
   [*P2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*P2-segment-routing-ipv6] locator P2 compress-16 ipv6-prefix 2001:DB8:100:3:: 64 compress-static 8 static 32
   ```
   ```
   [*P2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P2-segment-routing-ipv6] quit
   ```
   ```
   [*P2] isis 1
   ```
   ```
   [*P2-isis-1] segment-routing ipv6 locator P2 auto-sid-disable
   ```
   ```
   [*P2-isis-1] commit
   ```
   ```
   [~P2-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] compress-16 enable
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:4::4
   ```
   ```
   [*PE2-segment-routing-ipv6] locator PE2 compress-16 ipv6-prefix 2001:DB8:100:4:: 64 compress-static 8 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode compress ::E045 end psp-usd-next 
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode ::E000:0:0:66 end-op 
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6 advertise-srv6-locator
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE2-bgp-vpna] segment-routing ipv6 locator PE2 compress evpn
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
   ```
   [~PE2] isis 1
   ```
   ```
   [~PE2-isis-1] segment-routing ipv6 locator PE2 auto-sid-disable
   ```
   ```
   [*PE2-isis-1] commit
   ```
   ```
   [~PE2-isis-1] quit
   ```
   
   After the configuration is complete, run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information.
   
   PE1 is used as an example.
   
   ```
   [~PE1] display segment-routing ipv6 locator verbose
   
                           Locator Configuration Table                          
                           ---------------------------                          
   
   LocatorName   : PE1                                       LocatorID     : 1  
   IPv6Prefix    : 2001:DB8:100:1::                          PrefixLength  : 64 
   Block         : 2001:DB8:100::                            BlockLength   : 48 
   NodeID        : 0:0:0:1::                                 NodeIdLength  : 16 
   ComprStaticLen: 8                                         StaticLength  : 32 
   ArgsLength    : 0                                         Reference     : 2  
   Algorithm     : 0                                         ComprDynLength: 8  
   AutoCSIDPoolID: 8194
   AutoCSIDBegin : 2001:DB8:100:1:E100::                                         
   AutoCSIDEnd   : 2001:DB8:100:1:FFFF::                                        
   StaticCSIDBegin: 2001:DB8:100:1:E001::                                          
   StaticCSIDEnd : 2001:DB8:100:1:E0FF::                                          
   AutoSIDPoolID : 8193                                      DynLength     : 16 
   AutoSIDBegin  : 2001:DB8:100:1:E000:1::                                         
   AutoSIDEnd    : 2001:DB8:100:1:E000:FFFF:FFFF:FFFF                              
   StaticSIDBegin: 2001:DB8:100:1:E000::1                                            
   StaticSIDEnd  : 2001:DB8:100:1:E000::FFFF:FFFF
   GIB:LIB       : 14:2                                  
   
   Total Locator(s): 1 
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
   
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:100:1::/64                          FuncType    : End 
   Flavor      : PSP USP USD COC NEXT                         SidCompress : YES                                             
   LocatorName : PE1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2022-12-02 06:53:11.894
                                           
   SID         : 2001:DB8:100:1:E012::/80                     FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : PE1                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-02 12:38:16.946
   
   SID         : 2001:DB8:100:E012::/64                       FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : PE1                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-02 12:38:16.946
   
   Total SID(s): 3
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
   
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:100:4::/64                          FuncType    : End 
   Flavor      : PSP USP USD COC NEXT                         SidCompress : YES           
   LocatorName : PE2                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2022-12-02 06:52:28.547                                        
   
   SID         : 2001:DB8:100:4:E045::/80                     FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : PE2                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-02 12:42:32.865
   
   SID         : 2001:DB8:100:E045::/64                       FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : PE2                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-02 12:42:32.865
   
   Total SID(s): 3
   ```
   ```
   [~P1] display segment-routing ipv6 local-sid end forwarding
   
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:100:2::/64                          FuncType    : End
   Flavor      : PSP USP USD COC NEXT                         SidCompress : YES
   LocatorName : P1                                           LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2022-12-02 05:51:18.247                                        
   
   Total SID(s): 1 
   ```
   ```
   [~P2] display segment-routing ipv6 local-sid end forwarding
   
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:100:3::/64                          FuncType    : End
   Flavor      : PSP USP USD COC NEXT                         SidCompress : YES
   LocatorName : P2                                           LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2022-12-02 05:52:06.106                                        
   
   Total SID(s): 1 
   ```
7. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:100:2:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100:3:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:DB8:100:4:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next
   [*PE1-segment-routing-ipv6-segment-list-list1] index 20 sid ipv6 2001:DB8:100:E045:: compress-16 block 48 node-length 0 function-length 16 compress-flavor next
   [*PE1-segment-routing-ipv6-segment-list-list1] commit
   [~PE1-segment-routing-ipv6-segment-list-list1] quit
   [~PE1-segment-routing-ipv6] srv6-te-policy locator PE1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:4::4 color 101
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
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:100:3:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100:2:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:DB8:100:1:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next
   [*PE2-segment-routing-ipv6-segment-list-list1] index 20 sid ipv6 2001:DB8:100:E012:: compress-16 block 48 node-length 0 function-length 16 compress-flavor next
   [*PE2-segment-routing-ipv6-segment-list-list1] commit
   [~PE2-segment-routing-ipv6-segment-list-list1] quit
   [~PE2-segment-routing-ipv6] srv6-te-policy locator PE2 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
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
   Color                   : 101                            Endpoint             : 2001:DB8:4::4        
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -                    
   Policy State            : Up                             State Change Time    : 2022-12-02 05:55:06  
   Admin State             : Up                             Traffic Statistics   : Disable              
   Backup Hot-Standby      : Disable                        BFD                  : Disable              
   Interface Index         : -                              Interface Name       : -                    
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : -
   Candidate-path Count    : 1            
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary              
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0           
    Discriminator          : 100                            Binding SID          : -                    
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
            2001:DB8:100:2::                       BL: 48   NL: 16   FL: 0    Compress Flavor: coc-next    Compress Length: 16
            2001:DB8:100:3::                       BL: 48   NL: 16   FL: 0    Compress Flavor: coc-next    Compress Length: 16      
            2001:DB8:100:4::                       BL: 48   NL: 16   FL: 0    Compress Flavor: coc-next    Compress Length: 16
            2001:DB8:100:E045::                    BL: 48   NL: 0    FL: 16   Compress Flavor: next        Compress Length: 16
   ```
   
   Run the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy) command on the headend of the SRv6 TE Policy to check the SRv6 TE Policy connectivity by initiating a ping operation. PE1 is used as an example.
   
   ```
   [~PE1] ping srv6-te policy policy-name policy1 end-op 2001:DB8:100:4:E000::66  
     PING srv6-te policy : 100  data bytes, press CTRL_C to break                                                                    
     srv6-te policy's segment list:                                
     Preference: 100; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID: 1; Xcindex: 1; end-op: 2001:DB8:100:4:E000::66                             
       Reply from 2001:DB8:100:4:E000::66                               
       bytes=100 Sequence=1 time=4 ms                              
       Reply from 2001:DB8:100:4:E000::66                               
       bytes=100 Sequence=2 time=3 ms                              
       Reply from 2001:DB8:100:4:E000::66                               
       bytes=100 Sequence=3 time=3 ms                              
       Reply from 2001:DB8:100:4:E000::66                              
       bytes=100 Sequence=4 time=3 ms                              
       Reply from 2001:DB8:100:4:E000::66                               
       bytes=100 Sequence=5 time=3 ms                              
   
     --- srv6-te policy ping statistics ---                        
       5 packet(s) transmitted                                     
       5 packet(s) received                                        
       0.00% packet loss                                           
       round-trip min/avg/max = 3/3/4 ms 
   ```
8. Configure a tunnel policy to import VPN traffic.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] route-policy p1 permit node 10
   [*PE1-route-policy] apply extcommunity color 0:101
   [*PE1-route-policy] quit
   [*PE1] bgp 100
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:4::4 route-policy p1 import 
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
   [*PE2] bgp 100
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 route-policy p1 import 
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
   
   After the configuration is complete, run the **display ip routing-table vpn-instance vpna** command to check the IPv4 routing table of the specified VPN instance. The command output shows that the VPN route has successfully recursed to the SRv6 TE Policy.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpna
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                 
   ------------------------------------------------------------------------------  
   Routing Table : vpna        
            Destinations : 8        Routes : 8                                     
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface    
   
         10.11.1.0/24  Direct  0    0             D   10.11.1.1       GigabitEthernet0/2/0
         10.11.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
       10.11.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
         10.22.1.0/24  IBGP    255  0             RD  2001:DB8:4::4   policy1 
          11.1.1.1/32  EBGP    255  0             RD  10.11.1.2       GigabitEthernet0/2/0
          22.2.2.2/32  IBGP    255  0             RD  2001:DB8:4::4   policy1  
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0  
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0  
   ```
   ```
   [~PE1] display ip routing-table vpn-instance vpna 22.2.2.2 verbose 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------  
   Routing Table : vpna                                        
   Summary Count : 1                                           
   
   Destination: 22.2.2.2/32                                    
        Protocol: IBGP               Process ID: 0             
      Preference: 255                      Cost: 0             
         NextHop: 2001:DB8:4::4       Neighbour: 2001:DB8:4::4 
           State: Active Adv Relied         Age: 02h39m41s     
             Tag: 0                    Priority: low           
           Label: NULL                  QoSInfo: 0x0           
      IndirectID: 0x10000DE            Instance:               
    RelayNextHop: ::                  Interface: policy1       
        TunnelID: 0x000000003400000001    Flags: RD 
      RouteColor: 0                compressType: 1
        Block ID: 0                   Block Len: 48
   ```
9. Verify the configuration.
   
   
   
   Check that CEs belonging to the same VPN instance can ping each other. For example:
   
   ```
   [~CE1] ping -a 11.1.1.1 22.2.2.2                                                 
     PING 22.2.2.2: 56  data bytes, press CTRL_C to break                       
       Reply from 22.2.2.2: bytes=56 Sequence=1 ttl=253 time=4 ms               
       Reply from 22.2.2.2: bytes=56 Sequence=2 ttl=253 time=4 ms               
       Reply from 22.2.2.2: bytes=56 Sequence=3 ttl=253 time=3 ms               
       Reply from 22.2.2.2: bytes=56 Sequence=4 ttl=253 time=4 ms               
       Reply from 22.2.2.2: bytes=56 Sequence=5 ttl=253 time=3 ms               
   
     --- 22.2.2.2 ping statistics ---                                           
       5 packet(s) transmitted                                                  
       5 packet(s) received                                                     
       0.00% packet loss 
       round-trip min/avg/max = 3/3/4 ms 
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
    tnl-policy p1 evpn      
  #               
  segment-routing ipv6                      
   encapsulation source-address 2001:DB8:1::1
   compress-16 enable
   locator PE1 compress-16 ipv6-prefix 2001:DB8:100:1:: 64 compress-static 8 static 32  
    opcode compress ::E012 end psp-usd-next                      
    opcode ::E000:0:0:55 end-op                                      
   srv6-te-policy locator PE1                                
   segment-list list1                                        
    index 5 sid ipv6 2001:DB8:100:2:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next
    index 10 sid ipv6 2001:DB8:100:3:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next
    index 15 sid ipv6 2001:DB8:100:4:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next
    index 20 sid ipv6 2001:DB8:100:E045:: compress-16 block 48 node-length 0 function-length 16 compress-flavor next
   srv6-te policy policy1 endpoint 2001:DB8:4::4 color 101   
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
   peer 2001:DB8:4::4 as-number 100                          
   peer 2001:DB8:4::4 connect-interface LoopBack1            
   #                                                         
   ipv4-family unicast                                       
    undo synchronization                                     
   #                                                         
   ipv4-family vpn-instance vpna                             
    import-route direct                                      
    advertise l2vpn evpn                                     
    segment-routing ipv6 locator PE1 compress evpn                    
    segment-routing ipv6 traffic-engineer best-effort evpn   
    peer 10.11.1.2 as-number 65410                           
   #                                                         
   l2vpn-family evpn                                         
    policy vpn-target                                   
    peer 2001:DB8:4::4 enable                                
    peer 2001:DB8:4::4 route-policy p1 import                
    peer 2001:DB8:4::4 advertise encap-type srv6 advertise-srv6-locator            
  # 
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #               
  return 
  ```
* P1 configuration file
  
  ```
  #
  sysname P1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   compress-16 enable
   locator P1 compress-16 ipv6-prefix 2001:DB8:100:2:: 64 compress-static 8 static 32
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P1 auto-sid-disable
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
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  return 
  ```
* P2 configuration file
  
  ```
  #
  sysname P2
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   compress-16 enable
   locator P2 compress-16 ipv6-prefix 2001:DB8:100:3:: 64 compress-static 8 static 32
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P2 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:30::1/64
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
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
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy p1 evpn        
  #               
  segment-routing ipv6                                      
   encapsulation source-address 2001:DB8:4::4        
   compress-16 enable
   locator PE2 compress-16 ipv6-prefix 2001:DB8:100:4:: 64 compress-static 8 static 32
    opcode compress ::E045 end psp-usd-next                 
    opcode ::E000:0:0:66 end-op                                       
   srv6-te-policy locator PE2                                
   segment-list list1                                        
    index 5 sid ipv6 2001:DB8:100:3:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next    
    index 10 sid ipv6 2001:DB8:100:2:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next  
    index 15 sid ipv6 2001:DB8:100:1:: compress-16 block 48 node-length 16 function-length 0 compress-flavor coc-next
    index 20 sid ipv6 2001:DB8:100:E012:: compress-16 block 48 node-length 0 function-length 16 compress-flavor next
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101   
    candidate-path preference 100                            
     segment-list list1 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:30::2/64
   isis ipv6 enable 1  
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.22.1.1 255.255.255.0 
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:4::4/128
   isis ipv6 enable 1
  #               
  bgp 100                                                    
   router-id 4.4.4.4                                         
   peer 2001:DB8:1::1 as-number 100                          
   peer 2001:DB8:1::1 connect-interface LoopBack1            
   #                                                         
   ipv4-family unicast                                       
    undo synchronization                                     
   #                                                         
   ipv4-family vpn-instance vpna                             
    import-route direct                                      
    advertise l2vpn evpn                                     
    segment-routing ipv6 locator PE2 compress evpn                    
    segment-routing ipv6 traffic-engineer best-effort evpn   
    peer 10.22.1.2 as-number 65420                           
   #                                                         
   l2vpn-family evpn                                         
    policy vpn-target                                   
    peer 2001:DB8:1::1 enable                                
    peer 2001:DB8:1::1 route-policy p1 import                
    peer 2001:DB8:1::1 advertise encap-type srv6 advertise-srv6-locator
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
  interface  GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.11.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 11.1.1.1 32
  #               
  bgp 65410       
   router-id 11.1.1.1
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
   ip address 22.2.2.2 32
  #               
  bgp 65420       
   router-id 22.2.2.2
   peer 10.22.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.22.1.1 enable
  #
  return
  ```