Example for Configuring EVPN VPWS over OSPFv3 SRv6 BE
=====================================================

This section provides an example for configuring SRv6 BE to carry EVPN VPWSs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001188726049__fig_dc_vrp_srv6_cfg_all_002201), PE1, the P, and PE2 are in the same AS and need to run OSPFv3 to implement IPv6 network connectivity. In addition, a bidirectional SRv6 BE path needs to be deployed between PE1 and PE2 to carry EVPN VPWSs.

**Figure 1** EVPN VPWS over SRv6 BE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001188726085.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable OSPFv3 on PE1, the P, and PE2.
3. Configure EVPN VPWS and EVPL instances on each PE and bind the EVPL instance to an access-side sub-interface.
4. Establish a BGP EVPN peer relationship between the PEs.
5. Configure SRv6 BE on the PEs and enable OSPFv3 SRv6.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* RD and RT of the EVPN instance

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001188726049__section_dc_vrp_srv6_cfg_all_002205) in this section.
   
   
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
   
   An IPv4 address needs to be configured for the loopback interface, because the EVPN source address needs to be an IPv4 address. The preceding example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001188726049__section_dc_vrp_srv6_cfg_all_002205) in this section.
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
3. Configure EVPN and EVPL instances on each PE and bind the EVPL instance to an access-side sub-interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] evpl instance 1
   ```
   ```
   [*PE1-evpl1] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-evpl1] local-service-id 100 remote-service-id 200
   ```
   ```
   [*PE1-evpl1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] encapsulation dot1q vid 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] evpl instance 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 3.3.3.3
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] evpl instance 1
   ```
   ```
   [*PE2-evpl1] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-evpl1] local-service-id 200 remote-service-id 100
   ```
   ```
   [*PE2-evpl1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] encapsulation dot1q vid 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] evpl instance 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure CE1.
   
   ```
   <CE1> system-view
   [~CE1] vlan 1 
   [*CE1-vlan1] quit           
   [*CE1] interface gigabitethernet 0/1/0
   [*CE1-GigabitEthernet0/1/0] portswitch
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   [*CE1-GigabitEthernet0/1/0] port link-type trunk
   [*CE1-GigabitEthernet0/1/0] port trunk allow-pass vlan 1
   [*CE1-GigabitEthernet0/1/0] commit
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure CE2.
   
   ```
   <CE2> system-view
   [~CE2] vlan 1
   [*CE2-vlan1] quit           
   [*CE2] interface gigabitethernet 0/1/0
   [*CE2-GigabitEthernet0/1/0] portswitch
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   [*CE2-GigabitEthernet0/1/0] port link-type trunk
   [*CE2-GigabitEthernet0/1/0] port trunk allow-pass vlan 1
   [*CE2-GigabitEthernet0/1/0] commit
   [~CE2-GigabitEthernet0/1/0] quit
   ```
4. Establish a BGP EVPN peer relationship between the PEs.
   
   
   
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
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs to check whether a BGP EVPN peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationship has been established successfully.
5. Configure SRv6 BE on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:DB8:11:: 64 static 32
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
   [*PE1-ospfv3-1] segment-routing ipv6 locator PE1
   ```
   ```
   [*PE1-ospfv3-1] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
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
   [*PE1] evpl instance 1
   ```
   ```
   [*PE1-evpl1] segment-routing ipv6 locator PE1
   ```
   ```
   [*PE1-evpl1] quit
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] segment-routing ipv6 best-effort
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:DB8:30:: 64 static 32
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
   [*PE2-ospfv3-1] segment-routing ipv6 locator PE2
   ```
   ```
   [*PE2-ospfv3-1] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
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
   [*PE2] evpl instance 1
   ```
   ```
   [*PE2-evpl1] segment-routing ipv6 locator PE2
   ```
   ```
   [*PE2-evpl1] quit
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] segment-routing ipv6 best-effort
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] commit
   ```
6. Verify the configuration.
   
   
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end****-dx2** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dx2 forwarding
   
                       My Local-SID End.DX2 Forwarding Table                                                                           
                       -------------------------------------                                                                           
   
   SID        : 2001:DB8:11::7B/128                          FuncType : End.DX2                                                  
   EVPL ID    : 1                                                                                                                
   LocatorName: PE1                                          LocatorID: 3        
   Flavor     : NO-FLAVOR                                    SidCompress : NO                                               
   UpdateTime : 2023-05-10 01:46:05.713
   
   Total SID(s): 1   
   ```
   
   Run the **display bgp evpn evpl** command on each PE. The command output shows the EVPL status. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn evpl
   Total EVPLs: 1      1 Up     0 Down                                                                                                 
   
   EVPL ID : 1
   State : up
   EVPL Down Causes : --
   Evpl Type : none                                                                                                             
   Interface : GigabitEthernet0/2/0.1
   Interface Status : up
   Ignore AcState : disable                                                                                                            
   Local MTU : 1500                                                                                                                    
   Local Control Word : false                                                                                                          
   Local Redundancy Mode : all-active                                                                                                  
   Local DF State : primary(-)                                                                                                         
   Local ESI : 0000.0000.0000.0000.0000                                                                                                
   Remote Redundancy Mode : all-active                                                                                                 
   Remote Primary DF Number : 1                                                                                                        
   Remote Backup DF Number : 0                                                                                                         
   Remote None DF Number : 0                                                                                                           
   Peer IP : 2001:DB8:3::3                                                                                                             
    Origin Nexthop IP : 2001:DB8:3::3                                                                                                  
    DF State : primary                                                                                                                 
    Eline Role : primary                                                                                                               
    Remote MTU : 1500                                                                                                                  
    Remote Control Word : false                                                                                                        
    Remote ESI : 0000.0000.0000.0000.0000 
    Tunnel info : 1 tunnels                                                                                                            
     NO.0   Tunnel Type : srv6-be, Tunnel ID :                                                                                         
   Last Interface UP Timestamp: 2021-03-02 02:56:11+00:00                                                                              
   Last Designated Primary Timestamp: 2021-03-02 02:56:32+00:00                                                                        
   Last Designated Backup Timestamp: --
   Last EVPL UP Timestamp: --
   Last EVPL DOWN Timestamp: --
   ```
   
   Run the **display bgp evpn all routing-table** command on each PE. The command output shows EVPN route information sent from the peer end. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn all routing-table
   
    Local AS number : 100                                                                                                              
   
    BGP Local router ID is 1.1.1.1                                                                                                     
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,                                                    
                  h - history,  i - internal, s - suppressed, S - Stale                                                                
                  Origin : i - IGP, e - EGP, ? - incomplete                                                                            
   
   
    EVPN address family:                                                                                                               
    Number of A-D Routes: 2                                                                                                            
    Route Distinguisher: 100:1                                                                                                         
          Network(ESI/EthTagId)                                  NextHop                                                               
    *>    0000.0000.0000.0000.0000:100                           127.0.0.1                                                             
    *>i   0000.0000.0000.0000.0000:200                           2001:DB8:3::3                                                         
   
   
    EVPN-Instance evrf1:                                                                                                               
    Number of A-D Routes: 2                                                                                                            
          Network(ESI/EthTagId)                                  NextHop                                                               
    *>    0000.0000.0000.0000.0000:100                           127.0.0.1                                                             
    *>i   0000.0000.0000.0000.0000:200                           2001:DB8:3::3 
   ```
   
   Run the **display bgp evpn all routing-table ad-route** command on PE1. The command output shows detailed EVPN route information sent from the peer end.
   
   ```
   [~PE1] display bgp evpn all routing-table ad-route 0000.0000.0000.0000.0000:200 
   
    BGP local router ID : 1.1.1.1                                                                                                      
    Local AS number : 100                                                                                                              
    Total routes of Route Distinguisher(200:1): 1                                                                                      
    BGP routing table entry information of 0000.0000.0000.0000.0000:200:                                                               
    Label information (Received/Applied): 3/NULL                                                                                       
    From: 2001:DB8:3::3 (3.3.3.3)                                                                                                      
    Route Duration: 0d00h02m13s                                                                                                        
    Relay IP Nexthop: FE80::3AB0:9EFF:FE31:307                                                                                         
    Relay IP Out-Interface: GigabitEthernet0/1/0                                                                                              
    Relay Tunnel Out-Interface:                                                                                                        
    Original nexthop: 2001:DB8:3::3                                                                                                    
    Qos information : 0x0                                                                                                              
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>                                                               
    Prefix-sid: 2001:DB8:21::7B, Endpoint Behavior: DX2(21)                                                                                                        
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2                      
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)                                                                                
    ESI: 0000.0000.0000.0000.0000, Ethernet Tag ID: 200                                                                                
    Not advertised to any peer yet                                                                                                     
   
   
   
    EVPN-Instance evrf1:                                                                                                               
    Number of A-D Routes: 1                                                                                                            
    BGP routing table entry information of 0000.0000.0000.0000.0000:200:                                                               
    Route Distinguisher: 200:1                                                                                                         
    Remote-Cross route                                                                                                                 
    Label information (Received/Applied): 3/NULL                                                                                       
    From: 2001:DB8:3::3 (3.3.3.3)                                                                                                      
    Route Duration: 0d00h02m13s                                                                                                        
    Relay IP Nexthop: FE80::3AB0:9EFF:FE31:307                                                                                         
    Relay IP Out-Interface: GigabitEthernet0/1/0                                                                                              
    Relay Tunnel Out-Interface:                                                                                                        
    Original nexthop: 2001:DB8:3::3                                                                                                    
    Qos information : 0x0                                                                                                              
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>                                                               
    Prefix-sid: 2001:DB8:21::7B, Endpoint Behavior: DX2(21)                                                                                                        
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2                      
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)                                                                                
    ESI: 0000.0000.0000.0000.0000, Ethernet Tag ID: 200                                                                                
    Not advertised to any peer yet 
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 vpws
   route-distinguisher 100:1
   segment-routing ipv6 best-effort
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 100 remote-service-id 200
   segment-routing ipv6 locator PE1 
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1 ipv6-prefix 2001:DB8:11:: 64 static 32
  #
  ospfv3 1
   router-id 1.1.1.1
   segment-routing ipv6 locator PE1
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   evpl instance 1
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
  evpn vpn-instance evrf1 vpws
   route-distinguisher 200:1
   segment-routing ipv6 best-effort
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 200 remote-service-id 100
   segment-routing ipv6 locator PE2 
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator PE2 ipv6-prefix 2001:DB8:30:: 64 static 32
  #
  ospfv3 1
   router-id 3.3.3.3
   segment-routing ipv6 locator PE2
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   evpl instance 1
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
  sysname CE1
  #   
  vlan batch 1 
  #           
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 1
  # 
  return 
  ```
* CE2 configuration file
  
  ```
  sysname CE2
  #   
  vlan batch 1 
  #               
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 1
  #               
  return
  ```