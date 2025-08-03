Example for Configuring EVPN VPLS over OSPFv3 SRv6 BE
=====================================================

This section provides an example for configuring SRv6 BE to carry EVPN E-LAN services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001188606213__fig_dc_vrp_srv6_cfg_all_002201), PE1, the P, and PE2 are in the same AS and need to run OSPFv3 to implement IPv6 network connectivity. In addition, a bidirectional SRv6 BE path needs to be deployed between PE1 and PE2 to carry EVPN E-LAN services.

**Figure 1** EVPN VPLS over SRv6 BE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001142846132.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable OSPFv3 on PE1, the P, and PE2.
3. Configure an EVPN instance working in BD mode on each PE and bind the instance to an access-side sub-interface.
4. Establish a BGP EVPN peer relationship between the PEs.
5. Configure SRv6 BE on the PEs and enable OSPFv3 SRv6.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* RD and RT of the EVPN instance
* BD ID: 100
* Names of locators on PE1: PE1\_ARG and PE1; names of locators on PE2: PE2\_ARG and PE2; dynamically generated opcodes
* Length of the locators PE1\_ARG and PE2\_ARG: 10 (as specified in the **args** parameter)

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](dc_vrp_srv6_cfg_all_1012.html#EN-US_TASK_0000001188726049__section_dc_vrp_srv6_cfg_all_002205) in this section.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   An IPv4 address needs to be configured for the loopback interface, because the EVPN source address needs to be an IPv4 address. The preceding example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](dc_vrp_srv6_cfg_all_1012.html#EN-US_TASK_0000001188726049__section_dc_vrp_srv6_cfg_all_002205) in this section.
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
   
   # Display OSPFv3 neighbor information. PE1 is used as an example.
   
   ```
   [~PE1] display ospfv3 peer
   
   OSPFv3 Process (1)
   Total number of peer(s): 1 
    Peer(s) in full state: 1 
   OSPFv3 Area (0.0.0.0)                   
   Neighbor ID      Pri State            Dead Time  Interface          Instance ID       
   2.2.2.2            1 Full/Backup      00:00:37   GE0/1/0               0 
   ```
3. Configure an EVPN instance working in BD mode on each PE and bind the instance to an access-side sub-interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] bridge-domain 100
   ```
   ```
   [*PE1-bd100] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-bd100] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] rewrite pop single
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] bridge-domain 100
   ```
   ```
   [*PE1-GigabitEthernet 0/2/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 3.3.3.3
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] bridge-domain 100
   ```
   ```
   [*PE2-bd100] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-bd100] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] rewrite pop single
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] bridge-domain 100
   ```
   ```
   [*PE2-GigabitEthernet 0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
4. Configure the CEs and PEs to communicate.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 172.16.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 172.16.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] commit
   ```
5. Establish a BGP EVPN peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
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
   [*PE2-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 as-number 100
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
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
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
6. Configure SRv6 BE on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:DB8:11:: 64
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] locator PE1_ARG ipv6-prefix 2001:DB8:12:: 64 args 10
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] ospfv3 1
   [*PE1-ospfv3-1] segment-routing ipv6 locator PE1
   [*PE1-ospfv3-1] segment-routing ipv6 locator PE1_ARG auto-sid-disable
   [*PE1-ospfv3-1] quit
   [*PE1] evpn vpn-instance evrf1 bd-mode
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 locator PE1_ARG unicast-locator PE1
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE1-evpn-instance-evrf1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:DB8:21:: 64
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] locator PE2_ARG ipv6-prefix 2001:DB8:22:: 64 args 10
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] ospfv3 1
   [*PE2-ospfv3-1] segment-routing ipv6 locator PE2
   [*PE2-ospfv3-1] segment-routing ipv6 locator PE2_ARG auto-sid-disable
   [*PE2-ospfv3-1] quit
   [*PE2] evpn vpn-instance evrf1 bd-mode
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 locator PE2_ARG unicast-locator PE2
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE2-evpn-instance-evrf1] quit
   [*PE2] commit
   ```
7. Verify the configuration.
   
   
   
   Run the **display segment-routing ipv6 local-sid** { **end-dt2u** | **end-dt2ul** | **end-dt2m** } **forwarding** command on each PE to check information about the SRv6 BE local SID table. PE1 is used as an example.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt2m forwarding
   
                       My Local-SID End.DT2M Forwarding Table                                                                          
                       --------------------------------------                                                                          
   
   SID             : 2001:DB8:12::7C00/118                        FuncType    : End.DT2M                
   Bridge-domain ID: 100                                                                                       
   LocatorName     : PE1_ARG                                      LocatorID   : 4                                    
   Flavor          : NO-FLAVOR                                    SidCompress : NO
   UpdateTime      : 2023-05-10 01:46:05.713
   
   Total SID(s): 1 
   ```
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt2u forwarding
   
                       My Local-SID End.DT2U Forwarding Table                                                                          
                       --------------------------------------                                                                          
   
   SID             : 2001:DB8:11::3D/128                          FuncType    : End.DT2U                                     
   Bridge-domain ID: 100                                                                                       
   LocatorName     : PE1                                          LocatorID   : 3   
   Flavor          : NO-FLAVOR                                    SidCompress : NO                                           
   UpdateTime      : 2023-05-10 01:46:05.713
   
   Total SID(s): 1 
   ```
   
   Run the **display bgp evpn all routing-table** command on each PE. The command output shows EVPN route information sent from the peer end. PE1 is used as an example.
   
   ```
   [~PE1] display bgp evpn all routing-table
   
    Local AS number : 100                                                                                                              
   
    BGP Local router ID is 1.1.1.1                                                                                                     
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,                                                    
                  h - history,  i - internal, s - suppressed, S - Stale                                                                
                  Origin : i - IGP, e - EGP, ? - incomplete                                                                            
   
   
    EVPN address family:                                                                                                               
    Number of Mac Routes: 2                                                                                                            
    Route Distinguisher: 100:1                                                                                                         
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop                                                               
    *>    0:48:00e0-fc00-0002:0:0.0.0.0                          0.0.0.0                                                               
    *>i   0:48:00e0-fc00-0003:0:0.0.0.0                          2001:DB8:3::3                                                         
   
   
    EVPN-Instance evrf1:                                                                                                               
    Number of Mac Routes: 2                                                                                                            
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop                                                               
    *>    0:48:00e0-fc00-0002:0:0.0.0.0                          0.0.0.0                                                               
    *>i   0:48:00e0-fc00-0003:0:0.0.0.0                          2001:DB8:3::3
   
    EVPN address family:                                                                                                               
    Number of Inclusive Multicast Routes: 2                                                                                            
    Route Distinguisher: 100:1                                                                                                         
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop                                                               
    *>    0:32:1.1.1.1                                           127.0.0.1                                                             
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3                                                         
   
   
    EVPN-Instance evrf1:                                                                                                               
    Number of Inclusive Multicast Routes: 2                                                                                            
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop                                                               
    *>    0:32:1.1.1.1                                           127.0.0.1                                                             
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3 
   ```
   ```
   [~PE1] display bgp evpn all routing-table inclusive-route 0:32:3.3.3.3 
   
    BGP local router ID : 1.1.1.1                                                                                                      
    Local AS number : 100                                                                                                              
    Total routes of Route Distinguisher(200:1): 1                                                                                      
    BGP routing table entry information of 0:32:3.3.3.3:                                                                               
    Label information (Received/Applied): 3/NULL                                                                                       
    From: 2001:DB8:3::3 (3.3.3.3)                                                                                                      
    Route Duration: 0d00h09m23s                                                                                                        
    Relay IP Nexthop: FE80::3AB0:9EFF:FE31:307                                                                                         
    Relay IP Out-Interface: GigabitEthernet0/1/0                                                                                              
    Relay Tunnel Out-Interface:                                                                                                        
    Original nexthop: 2001:DB8:3::3                                                                                                    
    Qos information : 0x0                                                                                                              
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>                                                                                           
    Prefix-sid: 2001:DB8:22::7C00, Endpoint Behavior: DT2M(24)                                                                                                   
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2                      
    PMSI: Flags 0, Ingress Replication, Label 0:0:0(3), Tunnel Identifier:3.3.3.3                                                      
    Route Type: 3 (Inclusive Multicast Route)                                                                                          
    Ethernet Tag ID: 0, Originator IP:3.3.3.3/32                                                                                       
    Not advertised to any peer yet                                                                                                     
   
   
   
    EVPN-Instance evrf1:                                                                                                               
    Number of Inclusive Multicast Routes: 1                                                                                            
    BGP routing table entry information of 0:32:3.3.3.3:                                                                               
    Route Distinguisher: 200:1                                                                                                         
    Remote-Cross route                                                                                                                 
    Label information (Received/Applied): 3/NULL                                                                                       
    From: 2001:DB8:3::3 (3.3.3.3)                                                                                                      
    Route Duration: 0d00h09m24s                                                                                                        
    Relay IP Nexthop: FE80::3AB0:9EFF:FE31:307                                                                                         
    Relay IP Out-Interface: GigabitEthernet0/1/0                                                                                              
    Relay Tunnel Out-Interface:                                                                                                        
    Original nexthop: 2001:DB8:3::3                                                                                                    
    Qos information : 0x0                                                                                                              
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>                                                                                                          
    Prefix-sid: 2001:DB8:22::7C00, Endpoint Behavior: DT2M(24)                                                                                                      
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2                      
    PMSI: Flags 0, Ingress Replication, Label 0:0:0(3), Tunnel Identifier:3.3.3.3                                                      
    Route Type: 3 (Inclusive Multicast Route)                                                                                          
    Ethernet Tag ID: 0, Originator IP:3.3.3.3/32 
    Not advertised to any peer yet 
   ```
   ```
   [~PE1] display bgp evpn all routing-table mac-route 0:48:00e0-fc00-0003:0:0.0.0.0
   
    BGP local router ID : 1.1.1.1                                                                                                      
    Local AS number : 100                                                                                                              
    Total routes of Route Distinguisher(200:1): 1                                                                                      
    BGP routing table entry information of 0:48:00e0-fc00-0003:0:0.0.0.0:                                                              
    Label information (Received/Applied): 3/NULL                                                                                       
    From: 2001:DB8:3::3 (3.3.3.3)                                                                                                      
    Route Duration: 0d00h00m05s                                                                                                        
    Relay IP Nexthop: FE80::3AB0:9EFF:FE31:307                                                                                         
    Relay IP Out-Interface: GigabitEthernet0/1/0                                                                                              
    Relay Tunnel Out-Interface:                                                                                                        
    Original nexthop: 2001:DB8:3::3                                                                                                    
    Qos information : 0x0                                                                                                              
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>                                                                                                          
    Prefix-sid: 2001:DB8:21::3D, Endpoint Behavior: DT2U(23)
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2                      
    Route Type: 2 (MAC Advertisement Route)                                                                                            
    Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc00-0003/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0000.0000.0000.0000                    
    Not advertised to any peer yet
   
   
   
    EVPN-Instance evrf1:                                                                                                               
    Number of Mac Routes: 1                                                                                                            
    BGP routing table entry information of 0:48:00e0-fc00-0003:0:0.0.0.0:                                                              
    Route Distinguisher: 200:1                                                                                                         
    Remote-Cross route                                                                                                                 
    Label information (Received/Applied): 3/NULL                                                                                       
    From: 2001:DB8:3::3 (3.3.3.3)                                                                                                      
    Route Duration: 0d00h00m05s                                                                                                        
    Relay IP Nexthop: FE80::3AB0:9EFF:FE31:307                                                                                         
    Relay IP Out-Interface: GigabitEthernet0/1/0                                                                                              
    Relay Tunnel Out-Interface:                                                                                                        
    Original nexthop: 2001:DB8:3::3                                                                                                    
    Qos information : 0x0                                                                                                              
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>                                                                                                          
    Prefix-sid: 2001:DB8:21::3D, Endpoint Behavior: DT2U(23)                                                            
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2                      
    Route Type: 2 (MAC Advertisement Route)                                                                                            
    Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc00-0003/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0000.0000.0000.0000                    
    Not advertised to any peer yet 
   ```
   
   Run the **ping** command on the CEs. The command output shows that the CEs belonging to the same VPN instance can ping each other. For example:
   
   ```
   [~CE1] ping -a 172.16.1.1 172.16.1.2    
     PING 172.16.1.2: 56  data bytes, press CTRL_C to break                                                                            
       Reply from 172.16.1.2: bytes=56 Sequence=1 ttl=255 time=2 ms                                                                    
       Reply from 172.16.1.2: bytes=56 Sequence=2 ttl=255 time=2 ms                                                                    
       Reply from 172.16.1.2: bytes=56 Sequence=3 ttl=255 time=3 ms                                                                    
       Reply from 172.16.1.2: bytes=56 Sequence=4 ttl=255 time=3 ms                                                                    
       Reply from 172.16.1.2: bytes=56 Sequence=5 ttl=255 time=2 ms                                                                    
   
     --- 172.16.1.2 ping statistics ---                                                                                                
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
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE1_ARG unicast-locator PE1 
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bridge-domain 100
   evpn binding vpn-instance evrf1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:1::1
   locator PE1 ipv6-prefix 2001:DB8:11:: 64
   locator PE1_ARG ipv6-prefix 2001:DB8:12:: 64 args 10
  #               
  ospfv3 1                                         
   router-id 1.1.1.1                  
   segment-routing ipv6 locator PE1                
   segment-routing ipv6 locator PE1_ARG auto-sid-disable      
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
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 100
  #
  interface LoopBack1
   ipv6 enable    
   ip address 1.1.1.1 255.255.255.255
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
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
  #
  evpn source-address 1.1.1.1
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
   ip address 2.2.2.2 255.255.255.255
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
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE2_ARG unicast-locator PE2 
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bridge-domain 100
   evpn binding vpn-instance evrf1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:3::3
   locator PE2 ipv6-prefix 2001:DB8:21:: 64
   locator PE2_ARG ipv6-prefix 2001:DB8:22:: 64 args 10
  #               
  ospfv3 1
   router-id 3.3.3.3
   segment-routing ipv6 locator PE2
   segment-routing ipv6 locator PE2_ARG auto-sid-disable
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
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 100
  #
  interface LoopBack1
   ipv6 enable    
   ip address 3.3.3.3 255.255.255.255
   ipv6 address 2001:DB8:3::3/128
   ospfv3 1 area 0.0.0.0
  #               
  bgp 100         
   router-id 3.3.3.3
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
  # 
  evpn source-address 3.3.3.3
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
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   ip address 172.16.1.1 255.255.255.0
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
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   ip address 172.16.1.2 255.255.255.0
  #
  return
  ```