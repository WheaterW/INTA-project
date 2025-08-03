Example for Configuring Public Network IPv4 over IS-IS SRv6 TE Policy (SRH 16-bit Compression Scenario)
=======================================================================================================

This section provides an example for configuring an SRv6 TE Policy to carry public network IPv4 services in a 16-bit compression scenario.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001468189421__fig1558715115394), PE1, the P, and PE2 belong to the same AS and need to run IS-IS to implement IPv6 network connectivity. PE1, the P, and PE2 are Level-1 devices that belong to IS-IS process 1. An IBGP peer relationship needs to be established between PE1 and PE2, and EBGP peer relationships need to be established between the PEs and Devices.

In addition, a bidirectional SRv6 TE Policy needs to be deployed between PE1 and PE2 to carry public network IPv4 services.

**Figure 1** Public network IPv4 over SRv6 TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and interface2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001417952478.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title on PE1, the P, and PE2.
3. Establish an EBGP peer relationship between each PE and its connected Device.
4. Establish an MP-IBGP peer relationship between the PEs.
5. Deploy an SRv6 TE Policy between PE1 and PE2 and enable IS-IS SRv6.
6. Configure a tunnel policy on PE1 and PE2 to import public network traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, the P, and PE2
* IS-IS process ID of PE1, the P, and PE2
* IS-IS level of PE1, the P, and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see the configuration files.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
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
   [*PE1-LoopBack1] commit
   ```
   ```
   [~PE1-LoopBack1] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] isis 1 
   ```
   ```
   [*P-isis-1] is-level level-1
   ```
   ```
   [*P-isis-1] cost-style wide
   ```
   ```
   [*P-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] interface loopback1
   ```
   ```
   [*P-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P-LoopBack1] commit
   ```
   ```
   [~P-LoopBack1] quit
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
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
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
   [*PE2-LoopBack1] commit
   ```
   ```
   [~PE2-LoopBack1] quit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured.
   
   # Display IS-IS neighbor information. PE1 is used as an example.
   
   ```
   [~PE1] display isis peer
   
                             Peer information for ISIS(1)
                            
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002  GE0/1/0            0000.0000.0002.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
   
   # Display IS-IS routing table information. PE1 is used as an example.
   
   ```
   [~PE1] display isis route
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
    IPV6 Dest.            ExitInterface      NextHop                    Cost     Flags    
   --------------------------------------------------------------------------------
   2001:DB8:1::1/128      Loop1              Direct                     0        D/-/L/-  
   2001:DB8:2::2/128      GE0/1/0            FE80::3A92:6CFF:FE21:10    10       A/-/-/-  
   2001:DB8:3::3/128      GE0/1/0            FE80::3A92:6CFF:FE21:10    20       A/-/-/- 
   2001:DB8:10::/96       GE0/1/0            Direct                     10       D/-/L/-  
   2001:DB8:20::/96       GE0/1/0            FE80::3A92:6CFF:FE21:10    20       A/-/-/-                       
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut, 
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Establish an EBGP peer relationship between each PE and its connected Device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ip address 192.168.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] bgp 200
   ```
   ```
   [*DeviceA-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceA-bgp] peer 192.168.1.2 as-number 100
   ```
   ```
   [*DeviceA-bgp] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] ip address 192.168.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] peer 192.168.1.1 as-number 200
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 192.168.1.1 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] network 192.168.1.0 24
   ```
   ```
   [*PE1-bgp-af-ipv4] commit
   ```
   ```
   [~PE1-bgp-af-ipv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ip address 192.168.2.1 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] bgp 300
   ```
   ```
   [*DeviceB-bgp] router-id 5.5.5.5
   ```
   ```
   [*DeviceB-bgp] peer 192.168.2.2 as-number 100
   ```
   ```
   [*DeviceB-bgp] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [~PE2-GigabitEthernet0/2/0] ip address 192.168.2.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] router-id 2.2.2.2
   ```
   ```
   [*PE2-bgp] peer 192.168.2.1 as-number 300
   ```
   ```
   [*PE2-bgp] ipv4-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 192.168.2.1 enable
   ```
   ```
   [*PE2-bgp-af-ipv4] network 192.168.2.0 24
   ```
   ```
   [*PE2-bgp-af-ipv4] commit
   ```
   ```
   [~PE2-bgp-af-ipv4] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp peer** command on the PEs to check whether the BGP peer relationships have been established between the PEs and Devices. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the peer relationship between PE1 and DeviceA.
   
   ```
   [~PE1] display bgp peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1            Peers in established state : 1
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down           State  PrefRcv
     192.168.1.1     4    200    1624     1622       0 00:06:37   Established        1
   ```
4. Establish an MP-IBGP peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback1
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:DB8:3::3 next-hop-local
   ```
   ```
   [*PE1-bgp-af-ipv4] commit
   ```
   ```
   [~PE1-bgp-af-ipv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] peer 2001:DB8:1::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback1
   ```
   ```
   [*PE2-bgp] ipv4-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 2001:DB8:1::1 next-hop-local
   ```
   ```
   [*PE2-bgp-af-ipv4] commit
   ```
   ```
   [~PE2-bgp-af-ipv4] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp peer** command on the PEs to check whether the BGP peer relationship has been established. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp peer                
   
    BGP local router ID : 1.1.1.1                  
    Local AS number : 100                          
    Total number of peers : 2                 Peers in established state : 2       
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                                               
     192.168.1.1     4         200       10       11     0 00:05:15 Established        2   
     2001:DB8:3::3   4         100       10       11     0 00:05:15 Established        2 
   ```
5. Configure each PE to carry color and SID attributes in public network routes to be advertised.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A compressed End.DT4 SID can be either dynamically allocated through BGP or manually configured. If a dynamically allocated SID and a manually configured SID both exist, the latter takes effect. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **compress** command to enable dynamic allocation of compressed End.DT4 SIDs through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **compress** [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic allocation of compressed End.DT46 SIDs through BGP in the future, you do not need to run the **opcode** **compress** *func-opcode* **end-dt4** [ **vpn-instance** *vpn-instance-name* ] { next | coc-next } command or the **opcode** **compress** *func-opcode* **end-dt46** [ **vpn-instance** *vpn-instance-name* ] { next | coc-next } command to configure an opcode for static SIDs.
   
   In this example, dynamic allocation through BGP is adopted.
   
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
   [*PE1-segment-routing-ipv6] locator aa compress-16 ipv6-prefix 2001:DB8:100:: 48 compress-static 8 static 32
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode compress ::E010 end psp-usd-next
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] segment-routing ipv6 locator aa
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1]  route-policy color permit node 10
   ```
   ```
   [*PE1-route-policy] apply extcommunity color 0:101
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:DB8:3::3 route-policy color export
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:DB8:3::3 advertise-ext-community
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:DB8:3::3 prefix-sid advertise-srv6-locator
   ```
   ```
   [*PE1-bgp-af-ipv4] segment-routing ipv6 locator aa compress
   ```
   ```
   [*PE1-bgp-af-ipv4] commit
   ```
   ```
   [~PE1-bgp-af-ipv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] segment-routing ipv6
   ```
   ```
   [*P-segment-routing-ipv6] compress-16 enable
   ```
   ```
   [*P-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*P-segment-routing-ipv6] locator aa compress-16 ipv6-prefix 2001:DB8:200:: 48 compress-static 8 static 32
   ```
   ```
   [*P-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P-segment-routing-ipv6] quit
   ```
   ```
   [*P] isis 1
   ```
   ```
   [*P-isis-1] segment-routing ipv6 locator aa
   ```
   ```
   [*P-isis-1] commit
   ```
   ```
   [~P-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] compress-16 enable
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*PE2-segment-routing-ipv6] locator aa compress-16 ipv6-prefix 2001:DB8:300:: 48 compress-static 8 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode compress ::E010 end psp-usd-next
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] segment-routing ipv6 locator aa
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] route-policy color permit node 10
   ```
   ```
   [*PE2-route-policy] apply extcommunity color 0:101
   ```
   ```
   [*PE2-route-policy] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 2001:DB8:1::1 route-policy color export
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 2001:DB8:1::1 advertise-ext-community 
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 2001:DB8:1::1 prefix-sid advertise-srv6-locator
   ```
   ```
   [*PE2-bgp-af-ipv4] segment-routing ipv6 locator aa compress
   ```
   ```
   [*PE2-bgp-af-ipv4] commit
   ```
   ```
   [~PE2-bgp-af-ipv4] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:100::/48                            FuncType    : End
   Flavor      : PSP USP USD COC NEXT                         SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-05 13:39:48.628
   
   SID         : 2001:DB8:100:E010::/64                       FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-05 13:40:01.713
   
   SID         : 2001:DB8:100:E103::/64                       FuncType    : End
   Flavor      : PSP USP USD COC                              SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:27.429
   
   SID         : 2001:DB8:100:E104::/64                       FuncType    : End
   Flavor      : NO-FLAVOR                                    SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:27.429
   
   SID         : 2001:DB8:100:E105::/64                       FuncType    : End
   Flavor      : PSP                                          SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:27.429
   
   SID         : 2001:DB8:100:E106::/64                       FuncType    : End
   Flavor      : PSP USP USD                                  SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:27.429
   
   SID         : 2001:DB8:E010::/48                           FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-05 13:40:01.713
   
   SID         : 2001:DB8:E103::/48                           FuncType    : End
   Flavor      : PSP USP USD COC                              SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:27.429
   
   SID         : 2001:DB8:E104::/48                           FuncType    : End
   Flavor      : NO-FLAVOR                                    SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:27.429
   
   SID         : 2001:DB8:E105::/48                           FuncType    : End
   Flavor      : PSP                                          SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:27.429
   
   SID         : 2001:DB8:E106::/48                           FuncType    : End
   Flavor      : PSP USP USD                                  SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:27.429
   
   Total SID(s): 11 
   ```
   ```
   [~P] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
                                          
   SID         : 2001:DB8:200::/48                            FuncType    : End
   Flavor      : PSP USP USD COC NEXT                         SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-05 13:40:56.120
   
   SID         : 2001:DB8:200:E103::/64                       FuncType    : End
   Flavor      : PSP USP USD COC                              SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:200:E104::/64                       FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:200:E105::/64                       FuncType    : End
   Flavor      : NO-FLAVOR                                    SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:200:E106::/64                       FuncType    : End
   Flavor      : PSP                                          SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:200:E107::/64                       FuncType    : End
   Flavor      : PSP USP USD                                  SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:E103::/48                           FuncType    : End
   Flavor      : PSP USP USD COC                              SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:E104::/48                           FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:E105::/48                           FuncType    : End
   Flavor      : NO-FLAVOR                                    SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:E106::/48                           FuncType    : End
   Flavor      : PSP                                          SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   SID         : 2001:DB8:E107::/48                           FuncType    : End
   Flavor      : PSP USP USD                                  SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:36:52.146
   
   Total SID(s): 11
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
                                          
   SID         : 2001:DB8:300::/48                            FuncType    : End
   Flavor      : PSP USP USD COC NEXT                         SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-05 13:41:45.862
   
   SID         : 2001:DB8:300:E010::/64                       FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-05 13:41:52.600
   
   SID         : 2001:DB8:300:E103::/64                       FuncType    : End
   Flavor      : PSP USP USD COC                              SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:34:24.670
   
   SID         : 2001:DB8:300:E104::/64                       FuncType    : End
   Flavor      : NO-FLAVOR                                    SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:34:24.670
   
   SID         : 2001:DB8:300:E105::/64                       FuncType    : End
   Flavor      : PSP                                          SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:34:24.670
   
   SID         : 2001:DB8:300:E106::/64                       FuncType    : End
   Flavor      : PSP USP USD                                  SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:34:24.670
   
   SID         : 2001:DB8:E010::/48                           FuncType    : End
   Flavor      : PSP USD NEXT                                 SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-12-05 13:41:52.600
   
   SID         : 2001:DB8:E103::/48                           FuncType    : End
   Flavor      : PSP USP USD COC                              SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:34:24.670
   
   SID         : 2001:DB8:E104::/48                           FuncType    : End
   Flavor      : NO-FLAVOR                                    SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:34:24.670
   
   SID         : 2001:DB8:E105::/48                           FuncType    : End
   Flavor      : PSP                                          SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:34:24.670
   
   SID         : 2001:DB8:E106::/48                           FuncType    : End
   Flavor      : PSP USP USD                                  SidCompress : YES
   LocatorName : aa                                           LocatorID   : 2
   ProtocolType: ISIS                                         ProcessID   : 1
   UpdateTime  : 2022-12-06 02:34:24.670
   
   Total SID(s): 11
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dt4 forwarding** command to check information about the SRv6 local SID table. PE1 is used as an example.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt4 forwarding
                       My Local-SID End.DT4 Forwarding Table
                       -------------------------------------
   
   SID        : 2001:DB8:100:E13F::/64                       FuncType    : End.DT4
   VPN Name   : _public_                                     VPN ID      : 0
   LocatorName: aa                                           LocatorID   : 2
   Flavor     : COC NEXT                                     SidCompress : YES
   UpdateTime : 2023-05-10 01:46:05.713
   
   SID        : 2001:DB8:E13F::/48                           FuncType    : End.DT4
   VPN Name   : _public_                                     VPN ID      : 0
   LocatorName: aa                                           LocatorID   : 2
   Flavor     : COC NEXT                                     SidCompress : YES
   UpdateTime : 2023-05-10 01:46:05.713
   
   Total SID(s): 2
   ```
   
   Run the **display bgp routing-table** command to check BGP routing table information. The following example uses the command output on PE2.
   
   ```
   [~PE2] display bgp routing-table 192.168.1.0  
   
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
    BGP routing table entry information of 192.168.1.0/24:
    From: 2001:DB8:1::1 (1.1.1.1)
    Route Duration: 2d02h11m33s
    Relay IP Nexthop: FE80::3ABD:6CFF:FE31:300
    Relay IP Out-Interface: GigabitEthernet0/1/0
    Relay Tunnel Out-Interface: policy1(srv6tepolicy)
    Original nexthop: 2001:DB8:1::1
    Qos information : 0x0
    Ext-Community: Color <0 : 101>
    Prefix-sid: 2001:DB8:100:E13F::, Endpoint Behavior: 219, SRv6-sid-structure: 32-16-16-0-0-0
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Advertised to such 1 peers:
       192.168.2.1
   ```
6. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200:: compress-16 block 32 node-length 16 function-length 0 compress-flavor coc-next
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:300:: compress-16 block 32 node-length 16 function-length 0 compress-flavor coc-next
   [*PE1-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:DB8:E010:: compress-16 block 32 node-length 0 function-length 16 compress-flavor next
   [*PE1-segment-routing-ipv6-segment-list-list1] quit
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
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
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200:: compress-16 block 32 node-length 16 function-length 0 compress-flavor coc-next
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100:: compress-16 block 32 node-length 16 function-length 0 compress-flavor coc-next
   [*PE2-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:DB8:E010:: compress-16 block 32 node-length 0 function-length 16 compress-flavor next
   [*PE2-segment-routing-ipv6-segment-list-list1] quit
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy1-path] commit
   [~PE2-segment-routing-ipv6-policy-policy1-path] quit
   [~PE2-segment-routing-ipv6-policy-policy1] quit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   Run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy
   PolicyName : policy1
   Color                   : 101                            Endpoint             : 2001:DB8:3::3
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -
   Policy State            : Up                             State Change Time    : 2022-12-05 13:13:36
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
      Segment-List ID      : 2                              XcIndex              : 1
      List State           : Up                             DelayTimerRemain     : -
      Verification State   : -                              SuppressTimeRemain   : -
      PMTU                 : 9600                           Active PMTU          : 9600
      Weight               : 1                              BFD State            : -
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -
      Binding SID          : -
      Reverse Binding ID   : -
      SID :
            2001:DB8:200::                               BL: 32   NL: 16   FL: 0    Compress Flavor: coc-next    Compress Length: 16
            2001:DB8:300::                               BL: 32   NL: 16   FL: 0    Compress Flavor: coc-next    Compress Length: 16
            2001:DB8:E010::                              BL: 32   NL: 0    FL: 16   Compress Flavor: next        Compress Length: 16
   ```
7. Configure a tunnel policy to import public network traffic.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] tunnel-policy p1
   [*PE1-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE1-tunnel-policy-p1] quit
   [*PE1] tunnel-selector p1 permit node 1
   [*PE1-tunnel-selector] apply tunnel-policy p1
   [*PE1-tunnel-selector] quit
   [*PE1] bgp 100
   [*PE1-bgp] ipv4-family unicast
   [*PE1-bgp-af-ipv4] unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
   [*PE1-bgp-af-ipv4] segment-routing ipv6 traffic-engineer
   [*PE1-bgp-af-ipv4] commit
   [~PE1-bgp-af-ipv4] quit
   [~PE1-bgp] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] tunnel-policy p1
   [*PE2-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE2-tunnel-policy-p1] quit
   [*PE2] tunnel-selector p1 permit node 1
   [*PE2-tunnel-selector] apply tunnel-policy p1
   [*PE2-tunnel-selector] quit
   [*PE2] bgp 100
   [*PE2-bgp] ipv4-family unicast
   [*PE2-bgp-af-ipv4] unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
   [*PE2-bgp-af-ipv4] segment-routing ipv6 traffic-engineer
   [*PE2-bgp-af-ipv4] commit
   [~PE2-bgp-af-ipv4] quit
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp routing-table** command to check BGP routing table information. The following example uses the command output on PE2.
   
   ```
   [~PE2] display bgp routing-table 192.168.1.0  
   
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
    BGP routing table entry information of 192.168.1.0/24:
    From: 2001:DB8:1::1 (1.1.1.1)
    Route Duration: 0d00h39m53s
    Relay IP Nexthop: FE80::3A08:24FF:FE31:300
    Relay IP Out-Interface: GigabitEthernet0/1/0
    Relay Tunnel Out-Interface: policy1(srv6tepolicy)
    Original nexthop: 2001:DB8:1::1
    Qos information : 0x0
    Ext-Community: Color <0 : 101>
    Prefix-sid: 2001:DB8:100:E13F::, Endpoint Behavior: 219, SRv6-sid-structure: 32-16-16-0-0-0
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Advertised to such 1 peers:
       192.168.2.1
   ```
   
   Run the **display ip routing-table** command to check IP routing table information. The command output shows that the public network IPv4 route has successfully recursed to the SRv6 TE Policy.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 4        Routes : 4
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
       
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
         127.0.0.1/8   Direct  0    0             D   127.0.0.1       InLoopBack0
   127.255.255.255/8   Direct  0    0             D   127.0.0.1       InLoopBack0
       192.168.1.0/24  Direct  0    0             D   192.168.1.2     GigabitEthernet0/2/0
       192.168.1.2/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
     192.168.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
       192.168.2.0/24  IBGP    255  0             RD  2001:DB8:3::3   policy1
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   ```
   
   Check that DeviceA and DeviceB can ping each other. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] ping -a 192.168.1.1 192.168.2.1
     PING 192.168.2.1: 56  data bytes, press CTRL_C to break
       Reply from 192.168.2.1: bytes=56 Sequence=1 ttl=253 time=19 ms
       Reply from 192.168.2.1: bytes=56 Sequence=2 ttl=253 time=18 ms
       Reply from 192.168.2.1: bytes=56 Sequence=3 ttl=253 time=19 ms
       Reply from 192.168.2.1: bytes=56 Sequence=4 ttl=253 time=20 ms
       Reply from 192.168.2.1: bytes=56 Sequence=5 ttl=253 time=22 ms
   
     --- 192.168.2.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 18/19/22 ms
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1        
  #
  tunnel-selector p1 permit node 1
   apply tunnel-policy p1
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   compress-16 enable
   locator aa compress-16 ipv6-prefix 2001:DB8:100:: 48 compress-static 8 static 32
    opcode compress ::E010 end psp-usd-next
   segment-list list1
    index 5 sid ipv6 2001:DB8:200:: compress-16 block 32 node-length 16 function-length 0 compress-flavor coc-next
    index 10 sid ipv6 2001:DB8:300:: compress-16 block 32 node-length 16 function-length 0 compress-flavor coc-next
    index 15 sid ipv6 2001:DB8:E010:: compress-16 block 32 node-length 0 function-length 16 compress-flavor next
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
    candidate-path preference 100
     segment-list list1
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator aa
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/96
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 1.1.1.1
   peer 192.168.1.1 as-number 200
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    network 192.168.1.0 255.255.255.0
    unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
    segment-routing ipv6 locator aa compress
    segment-routing ipv6 traffic-engineer
    peer 192.168.1.1 enable
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy color export
    peer 2001:DB8:3::3 next-hop-local
    peer 2001:DB8:3::3 advertise-ext-community
    peer 2001:DB8:3::3 prefix-sid advertise-srv6-locator
  #
  route-policy color permit node 10
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
   compress-16 enable
   locator aa compress-16 ipv6-prefix 2001:DB8:200:: 48 compress-static 8 static 32
  #
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator aa
   #
  #  
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/96
   isis ipv6 enable 1          
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  # 
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  tunnel-selector p1 permit node 1
   apply tunnel-policy p1
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   compress-16 enable
   locator aa compress-16 ipv6-prefix 2001:DB8:300:: 48 compress-static 8 static 32
    opcode compress ::E010 end psp-usd-next
   segment-list list1
    index 5 sid ipv6 2001:DB8:200:: compress-16 block 32 node-length 16 function-length 0 compress-flavor coc-next
    index 10 sid ipv6 2001:DB8:100:: compress-16 block 32 node-length 16 function-length 0 compress-flavor coc-next
    index 15 sid ipv6 2001:DB8:E010:: compress-16 block 32 node-length 0 function-length 16 compress-flavor next
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    candidate-path preference 100
     segment-list list1
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator aa
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
   ip address 192.168.2.2 255.255.255.0
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 2.2.2.2
   peer 192.168.2.1 as-number 300
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    network 192.168.2.0 255.255.255.0
    unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
    segment-routing ipv6 locator aa compress
    segment-routing ipv6 traffic-engineer
    peer 192.168.2.1 enable
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy color export
    peer 2001:DB8:1::1 next-hop-local
    peer 2001:DB8:1::1 advertise-ext-community
    peer 2001:DB8:1::1 prefix-sid advertise-srv6-locator
  #
  route-policy color permit node 10
   apply extcommunity color 0:101
  #
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  return
  ```
* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
  #
  bgp 200
   router-id 4.4.4.4
   peer 192.168.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.2 enable
  #               
  return 
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
  #
  bgp 300
   router-id 5.5.5.5
   peer 192.168.2.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.2.2 enable
  #
  return
  ```