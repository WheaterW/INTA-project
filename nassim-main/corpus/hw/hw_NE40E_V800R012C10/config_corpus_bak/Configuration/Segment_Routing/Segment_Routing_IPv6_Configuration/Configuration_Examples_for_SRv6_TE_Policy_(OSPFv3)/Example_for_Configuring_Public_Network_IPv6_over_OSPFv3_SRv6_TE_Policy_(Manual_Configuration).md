Example for Configuring Public Network IPv6 over OSPFv3 SRv6 TE Policy (Manual Configuration)
=============================================================================================

This section provides an example for configuring an SRv6 TE Policy to carry public network IPv6 services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001216518411__fig_dc_vrp_srv6_cfg_all_001101), PE1, the P, and PE2 are in the same AS and need to run OSPFv3 to implement IPv6 network connectivity. PE1, the P, and PE2 are Area 0 devices that belong to OSPFv3 process 1. An IBGP peer relationship needs to be established between PE1 and PE2, and EBGP peer relationships need to be established between the PEs and Devices.

It is required that a bidirectional SRv6 TE Policy be established between PE1 and PE2 to carry public network IPv6 services.

**Figure 1** Public network IPv6 over SRv6 TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001216518425.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable OSPFv3 and configure area IDs on PE1, P, and PE2.
3. Establish an EBGP peer relationship between each PE and its connected Device.
4. Establish an MP-IBGP peer relationship between the PEs.
5. Deploy an SRv6 TE Policy between PE1 and PE2, and enable OSPFv3 SRv6. In addition, use BGP to dynamically allocate End.DT6 SIDs.
6. Configure a tunnel policy on PE1 and PE2 to import public network traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, the P, and PE2
* OSPFv3 process IDs of PE1, the P, and PE2
* OSPFv3 area IDs of PE1, P, and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001216518411__example682311373210) in this section.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:DB8:11::2 64
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] interface loopback1
   ```
   ```
   [*PE1-LoopBack1] ipv6 enable
   ```
   ```
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   ```
   ```
   [*PE1-LoopBack1] commit
   ```
   ```
   [~PE1-LoopBack1] quit
   ```
2. Configure OSPFv3.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospfv3 1
   [*PE1-ospfv3-1] router-id 1.1.1.1
   [*PE1-ospfv3-1] area 0 
   [*PE1-ospfv3-1-area-0.0.0.0] quit
   [*PE1-ospfv3-1] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] ospfv3 1 area 0.0.0.0
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] ospfv3 1 area 0.0.0.0
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] ospfv3 1
   [*P-ospfv3-1] router-id 2.2.2.2
   [*P-ospfv3-1] area 0 
   [*P-ospfv3-1-area-0.0.0.0] quit
   [*P-ospfv3-1] quit
   [*P] interface gigabitethernet 0/1/0
   [*P-GigabitEthernet0/1/0] ospfv3 1 area 0.0.0.0
   [*P-GigabitEthernet0/1/0] quit
   [*P] interface gigabitethernet 0/2/0
   [*P-GigabitEthernet0/2/0] ospfv3 1 area 0.0.0.0
   [*P-GigabitEthernet0/2/0] quit
   [*P] interface loopback1
   [*P-LoopBack1] ospfv3 1 area 0.0.0.0
   [*P-LoopBack1] quit
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospfv3 1
   [*PE2-ospfv3-1] router-id 3.3.3.3
   [*PE2-ospfv3-1] area 0 
   [*PE2-ospfv3-1-area-0.0.0.0] quit
   [*PE2-ospfv3-1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] ospfv3 1 area 0.0.0.0
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] ospfv3 1 area 0.0.0.0
   [*PE2-LoopBack1] quit
   [*PE2] commit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether OSPFv3 is successfully configured:
   
   # Display OSPFv3 neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ospfv3 peer
   
   OSPFv3 Process (1)
   Total number of peer(s): 1 
    Peer(s) in full state: 1 
   OSPFv3 Area (0.0.0.0)                   
   Neighbor ID      Pri State            Dead Time  Interface          Instance ID       
   2.2.2.2            1 Full/Backup      00:00:37   GE0/1/0               0 
   ```
3. Establish an EBGP peer relationship between each PE and its connected Device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 200
   ```
   ```
   [*DeviceA-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceA-bgp] peer 2001:DB8:11::2 as-number 100
   ```
   ```
   [*DeviceA-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv6] peer 2001:DB8:11::2 enable
   ```
   ```
   [*DeviceA-bgp-af-ipv6] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv6] quit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:11::1 as-number 200
   ```
   ```
   [*PE1-bgp] ipv6-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 2001:DB8:11::1 enable
   ```
   ```
   [*PE1-bgp-af-ipv6] network 2001:DB8:11::1 64
   ```
   ```
   [*PE1-bgp-af-ipv6] commit
   ```
   ```
   [~PE1-bgp-af-ipv6] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 300
   ```
   ```
   [*DeviceB-bgp] router-id 5.5.5.5
   ```
   ```
   [*DeviceB-bgp] peer 2001:DB8:22::2 as-number 100
   ```
   ```
   [*DeviceB-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:22::2 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv6] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:22::1 as-number 300
   ```
   ```
   [*PE2-bgp] ipv6-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 2001:DB8:22::1 enable
   ```
   ```
   [*PE2-bgp-af-ipv6] network 2001:DB8:22::1 64
   ```
   ```
   [*PE2-bgp-af-ipv6] commit
   ```
   ```
   [~PE2-bgp-af-ipv6] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp ipv6 peer** command on the PEs to check whether the BGP peer relationships have been established between the PEs and Devices. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the peer relationship between PE1 and DeviceA.
   
   ```
   [~PE1] display bgp ipv6 peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1            Peers in established state : 1
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down           State  PrefRcv
     2001:DB8:11::1  4    200    1624     1622       0 00:06:37   Established        1
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
   [*PE1-bgp] ipv6-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 2001:DB8:3::3 next-hop-local
   ```
   ```
   [*PE1-bgp-af-ipv6] commit
   ```
   ```
   [~PE1-bgp-af-ipv6] quit
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
   [*PE2-bgp] ipv6-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 2001:DB8:1::1 next-hop-local
   ```
   ```
   [*PE2-bgp-af-ipv6] commit
   ```
   ```
   [~PE1-bgp-af-ipv6] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp ipv6 peer** command on the PEs to check whether the BGP peer relationship has been established. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp ipv6 peer                
   
    BGP local router ID : 1.1.1.1                  
    Local AS number : 100                          
    Total number of peers : 2                 Peers in established state : 2       
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                                               
     2001:DB8:11::1  4         200       10       11     0 00:05:15 Established        2  
     2001:DB8:3::3   4         100       10       11     0 00:05:15 Established        2   
   ```
5. Configure each PE to carry color and SID attributes in public network routes to be advertised.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An End.DT6 SID can be either dynamically allocated through BGP or manually configured. If a dynamically allocated SID and a manually configured SID both exist, the latter takes effect. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT6 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, you do not need to run the **opcode** *func-opcode* **end-dt6** or **opcode** *func-opcode* **end-dt46** command to configure an opcode for static SIDs.
   
   In this example, SIDs are dynamically allocated through BGP.
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator aa ipv6-prefix 2001:DB8:100:: 64 static 32
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode ::100 end psp
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] ospfv3 1
   ```
   ```
   [*PE1-ospfv3-1] segment-routing ipv6 locator aa
   ```
   ```
   [*PE1-ospfv3-1] quit
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
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv6-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 2001:DB8:3::3 route-policy color export
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 2001:DB8:3::3 advertise-ext-community
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 2001:DB8:3::3 prefix-sid
   ```
   ```
   [*PE1-bgp-af-ipv6] segment-routing ipv6 locator aa
   ```
   ```
   [*PE1-bgp-af-ipv6] commit
   ```
   ```
   [~PE1-bgp-af-ipv6] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] segment-routing ipv6
   ```
   ```
   [*P-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*P-segment-routing-ipv6] locator aa ipv6-prefix 2001:DB8:200:: 64 static 32
   ```
   ```
   [*P-segment-routing-ipv6-locator] opcode ::100 end psp
   ```
   ```
   [*P-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P-segment-routing-ipv6] quit
   ```
   ```
   [*P] ospfv3 1
   ```
   ```
   [*P-ospfv3-1] segment-routing ipv6 locator aa
   ```
   ```
   [*P-ospfv3-1] commit
   ```
   ```
   [~P-ospfv3-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*PE2-segment-routing-ipv6] locator aa ipv6-prefix 2001:DB8:300:: 64 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode ::100 end psp
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] quit
   ```
   ```
   [*PE2] ospfv3 1
   ```
   ```
   [*PE2-ospfv3-1] segment-routing ipv6 locator aa
   ```
   ```
   [*PE2-ospfv3-1] quit
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
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] ipv6-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 2001:DB8:1::1 route-policy color export
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 2001:DB8:1::1 advertise-ext-community
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 2001:DB8:1::1 prefix-sid
   ```
   ```
   [*PE2-bgp-af-ipv6] segment-routing ipv6 locator aa
   ```
   ```
   [*PE2-bgp-af-ipv6] commit
   ```
   ```
   [~PE2-bgp-af-ipv6] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:100::100/128                        FuncType    : End 
   Flavor      : PSP                                          SidCompress : NO  
   LocatorName : aa                                           LocatorID   : 2   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-08-30 03:57:38.782                                        
   
   SID         : 2001:DB8:100::1:0:1/128                      FuncType    : End 
   Flavor      : NO-FLAVOR                                    SidCompress : NO                   
   LocatorName : aa                                           LocatorID   : 2   
   ProtocolType: OSPFv3                                       ProcessID   : 1   
   UpdateTime  : 2021-08-30 04:02:38.500                                        
   
   SID         : 2001:DB8:100::1:0:2/128                      FuncType    : End 
   Flavor      : PSP USP USD                                  SidCompress : NO                   
   LocatorName : aa                                           LocatorID   : 2   
   ProtocolType: OSPFv3                                       ProcessID   : 1   
   UpdateTime  : 2021-08-30 04:02:38.500                                        
   
   Total SID(s): 3 
   ```
   ```
   [~P] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:200::100/128                        FuncType    : End 
   Flavor      : PSP                                          SidCompress : NO  
   LocatorName : aa                                           LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-08-30 03:58:56.659                                        
   
   SID         : 2001:DB8:200::1:0:0/128                      FuncType    : End 
   Flavor      : NO-FLAVOR                                    SidCompress : NO                   
   LocatorName : aa                                           LocatorID   : 1   
   ProtocolType: OSPFv3                                       ProcessID   : 1   
   UpdateTime  : 2021-08-30 03:58:58.649                                        
   
   SID         : 2001:DB8:200::1:0:1/128                      FuncType    : End 
   Flavor      : PSP USP USD                                  SidCompress : NO                 
   LocatorName : aa                                           LocatorID   : 1   
   ProtocolType: OSPFv3                                       ProcessID   : 1   
   UpdateTime  : 2021-08-30 03:58:58.649                                        
   
   Total SID(s): 3 
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:200::100/128                        FuncType    : End 
   Flavor      : PSP                                          SidCompress : NO  
   LocatorName : aa                                           LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-08-30 03:58:56.659                                        
   
   SID         : 2001:DB8:200::1:0:0/128                      FuncType    : End 
   Flavor      : NO-FLAVOR                                    SidCompress : NO                   
   LocatorName : aa                                           LocatorID   : 1   
   ProtocolType: OSPFv3                                       ProcessID   : 1   
   UpdateTime  : 2021-08-30 03:58:58.649                                        
   
   SID         : 2001:DB8:200::1:0:1/128                      FuncType    : End 
   Flavor      : PSP USP USD                                  SidCompress : NO                
   LocatorName : aa                                           LocatorID   : 1   
   ProtocolType: OSPFv3                                       ProcessID   : 1   
   UpdateTime  : 2021-08-30 03:58:58.649                                        
   
   Total SID(s): 3
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dt6 forwarding** command to check information about the SRv6 local SID table. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt6 forwarding
                       My Local-SID End.DT6 Forwarding Table
                       -------------------------------------
   
   SID        : 2001:DB8:100::1:0:3E/128                     FuncType    : End.DT6
   VPN Name   : _public_                                     VPN ID      : 0
   LocatorName: aa                                           LocatorID   : 1
   Flavor     : NO-FLAVOR                                    SidCompress : NO 
   UpdateTime : 2023-05-10 01:46:05.713
   
   Total SID(s): 1
   ```
   
   Run the **display bgp ipv6 routing-table** command to check information about the BGP routing table. The following example uses the command output on PE2.
   
   ```
   [~PE2] display bgp ipv6 routing-table 2001:DB8:11::1  
   
    BGP local router ID : 3.3.3.3
    Local AS number : 100
    Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
    BGP routing table entry information of 2001:DB8:11::0/64:
    From: 2001:DB8:1::1 (1.1.1.1)
    Route Duration: 0d00h02m24s
    Relay IP Nexthop: FE80::3ABD:6CFF:FE31:300
    Relay IP Out-Interface: GigabitEthernet0/1/0
    Relay Tunnel Out-Interface:
    Original nexthop: 2001:DB8:1::1
    Qos information : 0x0
    Ext-Community: Color <0 : 101>
    Prefix-sid: 2001:DB8:100::1:0:3E
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Advertised to such 1 peers:
       2001:DB8:22::1
   ```
6. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200::100
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:300::100
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
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200::100
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100::100
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
   Policy State            : Up                             State Change Time    : 2021-03-25 13:13:36
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
      Segment-List ID      : 2                              XcIndex              : 2
      List State           : Up                             DelayTimerRemain     : -
      Verification State   : -                              SuppressTimeRemain   : -
      PMTU                 : 9600                           Active PMTU          : 9600
      Weight               : 1                              BFD State            : -
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -    
      Binding SID          : -    
      Reverse Binding SID  : -
      SID :
            2001:DB8:200::100
            2001:DB8:300::100
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
   [*PE1-bgp] ipv6-family unicast
   [*PE1-bgp-af-ipv6] unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
   [*PE1-bgp-af-ipv6] segment-routing ipv6 traffic-engineer
   [*PE1-bgp-af-ipv6] commit
   [~PE1-bgp-af-ipv6] quit
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
   [*PE2-bgp] ipv6-family unicast
   [*PE2-bgp-af-ipv6] unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
   [*PE2-bgp-af-ipv6] segment-routing ipv6 traffic-engineer
   [*PE2-bgp-af-ipv6] commit
   [~PE2-bgp-af-ipv6] quit
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp ipv6 routing-table** command to check information about the BGP routing table. The following example uses the command output on PE2.
   
   ```
   [~PE2] display bgp ipv6 routing-table 2001:DB8:11::1  
   
    BGP local router ID : 3.3.3.3
    Local AS number : 100
    Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
    BGP routing table entry information of 2001:DB8:11::0/64:
    From: 2001:DB8:1::1 (1.1.1.1)
    Route Duration: 0d00h39m53s
    Relay IP Nexthop: FE80::3A83:DEFF:FE21:301
    Relay IP Out-Interface: GigabitEthernet0/1/0
    Relay Tunnel Out-Interface: policy1(srv6tepolicy)
    Original nexthop: 2001:DB8:1::1
    Qos information : 0x0
    Ext-Community: Color <0 : 101>
    Prefix-sid: 2001:DB8:100::1:0:3E
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Advertised to such 1 peers:
      2001:DB8:22::1
   ```
   
   Run the **display ipv6 routing-table** command to check IPv6 routing table information. The command output shows that the public network IPv6 route has successfully recursed to the SRv6 TE Policy.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ipv6 routing-table
   Routing Table : _public_
            Destinations : 10       Routes : 10
   
   Destination  : 2001:DB8:1::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : LoopBack1                               Flags        : D
   
   Destination  : 2001:DB8:2::2                           PrefixLength : 128
   NextHop      : FE80::3A03:6DFF:FE21:300                Preference   : 15
   Cost         : 20                                      Protocol     : OSPFv3
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:10::                           PrefixLength : 96
   NextHop      : 2001:DB8:10::1                          Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:10::1                          PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:11::                           PrefixLength : 64
   NextHop      : 2001:DB8:11::2                          Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:DB8:11::2                          PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:DB8:20::                           PrefixLength : 96
   NextHop      : FE80::3A03:6DFF:FE21:300                Preference   : 15
   Cost         : 20                                      Protocol     : OSPFv3
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:DB8:22::                           PrefixLength : 64
   NextHop      : 2001:DB8:2::2                           Preference   : 255
   Cost         : 0                                       Protocol     : IBGP
   RelayNextHop : ::                                      TunnelID     : 0x000000003400000001
   Interface    : policy1                                 Flags        : RD
   
   Destination  : 2001:DB8:100::                          PrefixLength : 64
   NextHop      : ::                                      Preference   : 15
   Cost         : 0                                       Protocol     : OSPFv3
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : DB
   
   Destination  : 2001:DB8:200::                          PrefixLength : 64
   NextHop      : FE80::3A03:6DFF:FE21:300                Preference   : 15
   Cost         : 20                                      Protocol     : OSPFv3
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   ```
   
   Check that DeviceA and DeviceB can ping each other. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] ping ipv6 -a 2001:DB8:11::1 2001:DB8:22::1
     PING 2001:DB8:22::1 : 56  data bytes, press CTRL_C to break
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=1 hop limit=62 time=166 ms
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=2 hop limit=62 time=10 ms
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=3 hop limit=62 time=9 ms
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=4 hop limit=62 time=11 ms
       Reply from 2001:DB8:22::1
       bytes=56 Sequence=5 hop limit=62 time=14 ms
   
     --- 2001:DB8:22::1 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=9/42/166 ms
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
   locator aa ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::100 end psp
   segment-list list1
    index 5 sid ipv6 2001:DB8:200::100
    index 10 sid ipv6 2001:DB8:300::100
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
    candidate-path preference 100
     segment-list list1
  #
  ospfv3 1
   router-id 1.1.1.1
   segment-routing ipv6 locator aa
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:11::2/64
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:1::1/128
   ospfv3 1 area 0.0.0.0
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:DB8:11::1 as-number 200
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #
   ipv6-family unicast
    undo synchronization
    network 2001:DB8:11:: 64
    unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
    segment-routing ipv6 locator aa
    segment-routing ipv6 traffic-engineer
    peer 2001:DB8:11::1 enable
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy color export
    peer 2001:DB8:3::3 next-hop-local
    peer 2001:DB8:3::3 advertise-ext-community
    peer 2001:DB8:3::3 prefix-sid
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
   locator aa ipv6-prefix 2001:DB8:200:: 64 static 32
    opcode ::100 end psp
  #
  ospfv3 1          
   router-id 2.2.2.2
   segment-routing ipv6 locator aa
   area 0.0.0.0
  #  
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::2/64
   ospfv3 1 area 0.0.0.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
   ospfv3 1 area 0.0.0.0   
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   ospfv3 1 area 0.0.0.0
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
   locator aa ipv6-prefix 2001:DB8:300:: 64 static 32
    opcode ::100 end psp
   segment-list list1
    index 5 sid ipv6 2001:DB8:200::100
    index 10 sid ipv6 2001:DB8:100::100
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    candidate-path preference 100
     segment-list list1
  #
  ospfv3 1
   router-id 3.3.3.3
   segment-routing ipv6 locator aa
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:22::2/64
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:3::3/128
   ospfv3 1 area 0.0.0.0
  #
  bgp 100
   router-id 3.3.3.3
   peer 2001:DB8:22::1 as-number 300
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #
   ipv6-family unicast
    undo synchronization
    network 2001:DB8:22:: 64
    unicast-route recursive-lookup tunnel-v6 tunnel-selector p1
    segment-routing ipv6 locator aa
    segment-routing ipv6 traffic-engineer
    peer 2001:DB8:22::1 enable
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy color export
    peer 2001:DB8:1::1 next-hop-local
    peer 2001:DB8:1::1 advertise-ext-community
    peer 2001:DB8:1::1 prefix-sid
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
   ipv6 enable
   ipv6 address 2001:DB8:11::1/64
  #
  bgp 200
   router-id 4.4.4.4
   peer 2001:DB8:11::2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    peer 2001:DB8:11::2 enable
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
   ipv6 enable
   ipv6 address 2001:DB8:22::1/64
  #
  bgp 300
   router-id 5.5.5.5
   peer 2001:DB8:22::2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    peer 2001:DB8:22::2 enable
  #
  return
  ```