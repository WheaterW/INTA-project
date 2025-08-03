Example for Configuring L3VPNv4 over OSPFv3 SRv6 BE
===================================================

This section provides an example for configuring SRv6 BE to carry L3VPNv4 services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001188606211__fig_dc_vrp_srv6_cfg_all_001101):

* PE1, the P, and PE2 are in the same AS and need to run OSPFv3 to implement IPv6 network connectivity.
* PE1, the P, and PE2 are Area 0 devices that belong to OSPFv3 process 1.

It is required that a bidirectional SRv6 BE path be deployed between PE1 and PE2 to carry L3VPNv4 services.

**Figure 1** L3VPNv4 over SRv6 BE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001142846128.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable OSPFv3 on PE1, the P, and PE2.
3. Configure VPN instances on PE1 and PE2.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish an MP-IBGP peer relationship between the PEs.
6. Configure SRv6 on PE1 and PE2, and enable OSPFv3 SRv6.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, the P, and PE2
* OSPFv3 process IDs of PE1, the P, and PE2
* OSPFv3 area IDs of PE1, P, and PE2
* VPN instance names, RDs, and RTs on PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001188606211__section_dc_vrp_srv6_cfg_all_001105) in this section.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
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
3. Configure a VPN instance on each PE, enable the IPv4 address family for the instance, and bind the interface that connects each PE to a CE to the VPN instance on that PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpn1
   ```
   ```
   [*PE2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure an IP address for each interface on the CEs, as shown in [Figure 1](#EN-US_TASK_0000001188606211__fig_dc_vrp_srv6_cfg_all_001101). For configuration details, see [Configuration Files](#EN-US_TASK_0000001188606211__section_dc_vrp_srv6_cfg_all_001105) in this section.
   
   After the configuration is complete, run the **display ip vpn-instance verbose** command on the PEs to check VPN instance configurations. The command output shows that each PE can successfully ping its connected CE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a PE has multiple interfaces bound to the same VPN instance, specify a source IP address using the **-a** *source-ip-address* parameter in the **ping -vpn-instance** *vpn-instance-name* **-a** *source-ip-address dest-ip-address* command to ping the CE that is connected to the remote PE. If the source IP address is not specified, the ping operation may fail.
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-LoopBack1] ip address 11.11.11.11 32
   ```
   ```
   [*CE1-LoopBack1] quit
   ```
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] peer 10.1.1.1 as-number 100
   ```
   ```
   [*CE1-bgp] network 11.11.11.11 32
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
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] peer 10.1.1.2 as-number 65410
   ```
   ```
   [*PE1-bgp-vpn1] import-route direct
   ```
   ```
   [*PE1-bgp-vpn1] commit
   ```
   ```
   [~PE1-bgp-vpn1] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface loopback 1
   ```
   ```
   [*CE2-LoopBack1] ip address 22.22.22.22 32
   ```
   ```
   [*CE2-LoopBack1] quit
   ```
   ```
   [*CE2] bgp 65420
   ```
   ```
   [*CE2-bgp] peer 10.2.1.1 as-number 100
   ```
   ```
   [*CE2-bgp] network 22.22.22.22 32
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
   [*PE2-bgp] router-id 2.2.2.2
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-vpn1] peer 10.2.1.2 as-number 65420
   ```
   ```
   [*PE2-bgp-vpn1] import-route direct
   ```
   ```
   [*PE2-bgp-vpn1] commit
   ```
   ```
   [~PE2-bgp-vpn1] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on each PE to check whether a BGP peer relationship has been established between the PE and its connected CE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpn1 peer
    BGP local router ID : 1.1.1.1
    Local AS number : 100
   
    VPN-Instance vpn1, Router ID 1.1.1.1:
    Total number of peers : 1            Peers in established state : 1
   
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     10.1.1.2        4   65410  11     9          0     00:06:37   Established  1
   ```
5. Establish an MP-IBGP peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] commit
   ```
   ```
   [~PE1-bgp-af-vpnv4] quit
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
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] commit
   ```
   ```
   [~PE2-bgp-af-vpnv4] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 all peer** command on the PEs to check whether a BGP peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp vpnv4 all peer                        
   
    BGP local router ID : 1.1.1.1                          
    Local AS number : 100                                  
    Total number of peers : 2                 Peers in established state : 2    
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                                               
     2001:DB8:3::3   4         100       10       11     0 00:05:15 Established        2                                               
   
     Peer of IPv4-family for vpn instance :                
   
     VPN-Instance vpn1, Router ID 1.1.1.1:                 
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                                               
     10.1.1.2        4       65410       10       13     0 00:06:18 Established        1   
   ```
6. Establish an SRv6 BE path between the PEs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An End.DT4 SID can be either dynamically allocated through BGP or manually configured. If a dynamically allocated SID and a manually configured SID both exist, the latter takes effect. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT4 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, you do not need to run the **opcode** *func-opcode* **end-dt4** **vpn-instance** *vpn-instance-name* or **opcode** *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name* command to configure an opcode for static SIDs.
   
   In this example, SIDs are dynamically allocated through BGP.
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
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
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:3::3 prefix-sid
   ```
   ```
   [*PE1-bgp-af-vpnv4] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] segment-routing ipv6 best-effort
   ```
   ```
   [*PE1-bgp-vpn1] segment-routing ipv6 locator as1
   ```
   ```
   [*PE1-bgp-vpn1] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] ospfv3 1
   ```
   ```
   [*PE1-ospfv3-1] segment-routing ipv6 locator as1
   ```
   ```
   [*PE1-ospfv3-1] commit
   ```
   ```
   [~PE1-ospfv3-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32
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
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:1::1 prefix-sid
   ```
   ```
   [*PE2-bgp-af-vpnv4] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-vpn1] segment-routing ipv6 best-effort
   ```
   ```
   [*PE2-bgp-vpn1] segment-routing ipv6 locator as1
   ```
   ```
   [*PE2-bgp-vpn1] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] ospfv3 1
   ```
   ```
   [*PE2-ospfv3-1] segment-routing ipv6 locator as1
   ```
   ```
   [*PE2-ospfv3-1] commit
   ```
   ```
   [~PE2-ospfv3-1] quit
   ```
7. Verify the configuration.
   
   
   
   Run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) [ *locator-name* ] **verbose** command to check SRv6 locator information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 locator verbose
                           Locator Configuration Table                          
                           ---------------------------                          
   
   LocatorName   : as1                                       LocatorID     : 1  
   IPv6Prefix    : 2001:DB8:100::                            PrefixLength  : 64 
   Block         : --                                        BlockLength   : 0  
   NodeID        : --                                        NodeIdLength  : 0  
   ComprStaticLen: 0                                         StaticLength  : 32 
   ArgsLength    : 0                                         Reference     : 0  
   Algorithm     : 0                                         ComprDynLength: 0  
   AutoCSIDPoolID: 0
   AutoCSIDBegin : --    
   AutoCSIDEnd   : --    
   StaticCSIDBegin: --   
   StaticCSIDEnd : --    
   AutoSIDPoolID : 8193                                      DynLength     : 32 
   AutoSIDBegin  : 2001:DB8:100::1:0:0                                          
   AutoSIDEnd    : 2001:DB8:100:0:FFFF:FFFF:FFFF:FFFF                           
   StaticSIDBegin: 2001:DB8:100::1                                              
   StaticSIDEnd  : 2001:DB8:100::FFFF:FFFF
   GIB:LIB       : --                                    
   
   Total Locator(s): 1 
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dt4** **forwarding** command to check information about the SRv6 local SID table. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt4 forwarding
                       My Local-SID End.DT4 Forwarding Table
                       -------------------------------------
   
   SID        : 2001:DB8:100::1:0:3D/128                     FuncType    : End.DT4
   VPN Name   : vpn1                                         VPN ID      : 3 
   LocatorName: as1                                          LocatorID   : 1 
   Flavor     : NO-FLAVOR                                    SidCompress : NO
   UpdateTime : 2023-05-10 01:46:05.713
   
   Total SID(s): 1
   ```
   
   Run the **display bgp vpnv4 all routing-table** command on the PEs to check BGP VPNv4 routing information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp vpnv4 all routing-table
   
    BGP Local router ID is 1.1.1.1                                                                                                     
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,                                                    
                  h - history,  i - internal, s - suppressed, S - Stale                                                                
                  Origin : i - IGP, e - EGP, ? - incomplete                                                                            
    RPKI validation codes: V - valid, I - invalid, N - not-found                                                                       
   
   
    Total number of routes from all PE: 6                                                                                              
    Route Distinguisher: 100:1                                                                                                         
   
   
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn                                      
   
    *>     10.1.1.0/24        0.0.0.0                        0                     0       ?                                           
    *>     10.1.1.1/32        0.0.0.0                        0                     0       ?                                           
    *>     11.11.11.11/32     10.1.1.2                       0                     0      65410i                                       
    *>     127.0.0.0/8        0.0.0.0                        0                     0       ?                                           
    Route Distinguisher: 200:1                                                                                                         
   
   
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>i    10.2.1.0/24        2001:DB8:3::3                  0          100        0       ?                                           
    *>i    22.22.22.22/32     2001:DB8:3::3                  0          100        0      65420i                                       
   
    VPN-Instance vpn1, Router ID 1.1.1.1:                                                                                              
   
    Total Number of Routes: 6                                                                                                          
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn                                      
   
    *>     10.1.1.0/24        0.0.0.0                        0                     0       ?                                           
    *>     10.1.1.1/32        0.0.0.0                        0                     0       ?                                           
    *>i    10.2.1.0/24        2001:DB8:3::3                  0          100        0       ?                                           
    *>     11.11.11.11/32     10.1.1.2                       0                     0      65410i                                       
    *>i    22.22.22.22/32     2001:DB8:3::3                  0          100        0      65420i                                       
    *>     127.0.0.0/8        0.0.0.0                        0                     0       ?  
   ```
   
   Run the **display ip routing-table** **vpn-instance vpn1** command on the PEs to check VPN routing table information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpn1    
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                                              
   ------------------------------------------------------------------------------                                                      
   Routing Table : vpn1                                                                                                                
            Destinations : 8        Routes : 8                                                                                         
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop              Interface                                                        
   
          10.1.1.0/24  Direct  0    0             D   10.1.1.1             GigabitEthernet0/2/0      
          10.1.1.1/32  Direct  0    0             D   127.0.0.1            GigabitEthernet0/2/0      
        10.1.1.255/32  Direct  0    0             D   127.0.0.1            GigabitEthernet0/2/0      
          10.2.1.0/24  IBGP    255  0             RD  2001:DB8:130::1:0:3D GigabitEthernet0/1/0                                                     
       11.11.11.11/32  EBGP    255  0             RD  10.1.1.2             GigabitEthernet0/2/0      
       22.22.22.22/32  IBGP    255  0             RD  2001:DB8:130::1:0:3D GigabitEthernet0/1/0                                                     
         127.0.0.0/8   Direct  0    0             D   127.0.0.1            InLoopBack0                                                      
   255.255.255.255/32  Direct  0    0             D   127.0.0.1            InLoopBack0 
   ```
   
   Run the [**display ip routing-table vpn-instance vpn1**](cmdqueryname=display+ip+routing-table+vpn-instance+vpn1) *ip-address* **verbose** command on the PEs to check detailed VPN routing table information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpn1 22.22.22.22 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                                              
   ------------------------------------------------------------------------------                                                      
   Routing Table : vpn1                                                                                                                
   Summary Count : 1                                                                                                                   
   
   Destination: 22.22.22.22/32                                                                                                         
        Protocol: IBGP               Process ID: 0                                                                                     
      Preference: 255                      Cost: 0                                                                                     
         NextHop: 2001:DB8:130::1:0:3D Neighbour: 2001:DB8:3::3                                                                        
           State: Active Adv Relied         Age: 00h01m15s                                                                             
             Tag: 0                    Priority: low                                                                                   
           Label: 3                     QoSInfo: 0x0                                                                                   
      IndirectID: 0x1000095            Instance:                                                                                       
    RelayNextHop: 2001:DB8:130::1:0:3D Interface: GigabitEthernet0/1/0                                                                              
        TunnelID: 0x0                     Flags: RD
      RouteColor: 0 
   ```
   
   Check that CEs belonging to the same VPN instance can ping each other. For example:
   
   ```
   [~CE1] ping -a 11.11.11.11 22.22.22.22
     PING 22.22.22.22: 56  data bytes, press CTRL_C to break                                                                           
       Reply from 22.22.22.22: bytes=56 Sequence=1 ttl=253 time=2 ms                                                                   
       Reply from 22.22.22.22: bytes=56 Sequence=2 ttl=253 time=2 ms                                                                   
       Reply from 22.22.22.22: bytes=56 Sequence=3 ttl=253 time=3 ms                                                                   
       Reply from 22.22.22.22: bytes=56 Sequence=4 ttl=253 time=3 ms                                                                   
       Reply from 22.22.22.22: bytes=56 Sequence=5 ttl=253 time=3 ms                                                                   
   
     --- 22.22.22.22 ping statistics ---                                                                                               
       5 packet(s) transmitted                                                                                                         
       5 packet(s) received                                                                                                            
       0.00% packet loss                                                                                                               
       round-trip min/avg/max = 2/2/3 ms 
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
  #               
  ospfv3 1
   router-id 1.1.1.1
   segment-routing ipv6 locator as1
   area 0.0.0.0
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/96
   ospfv3 1 area 0.0.0.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/128
   ospfv3 1 area 0.0.0.0
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 prefix-sid
   #              
   ipv4-family vpn-instance vpn1
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.1.1.2 as-number 65410
  #               
  return
  ```
* P configuration file
  
  ```
  #
  sysname P        
  #               
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::2/96
   ospfv3 1 area 0.0.0.0 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/96
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32
  #   
  ospfv3 1
   router-id 3.3.3.3
   segment-routing ipv6 locator as1
   area 0.0.0.0             
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::2/96
   ospfv3 1 area 0.0.0.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   ospfv3 1 area 0.0.0.0
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 prefix-sid
   #              
   ipv4-family vpn-instance vpn1
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.2.1.2 as-number 65420
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
   peer 10.2.1.1 as-number 100
  #
   ipv4-family unicast
    undo synchronization
    network 22.22.22.22 255.255.255.255
    peer 10.2.1.1 enable
  #
  return
  ```