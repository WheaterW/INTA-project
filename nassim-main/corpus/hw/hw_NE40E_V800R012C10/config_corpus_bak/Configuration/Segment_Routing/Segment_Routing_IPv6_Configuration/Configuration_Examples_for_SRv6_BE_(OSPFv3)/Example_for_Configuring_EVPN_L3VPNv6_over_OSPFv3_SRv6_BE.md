Example for Configuring EVPN L3VPNv6 over OSPFv3 SRv6 BE
========================================================

This section provides an example for configuring SRv6 BE to carry EVPN L3VPNv6 services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001142686298__fig_dc_vrp_evpn_cfg_015101), PE1, the P, and PE2 are in the same AS and need to run OSPFv3 to implement IPv6 network connectivity. In addition, a bidirectional SRv6 BE path needs to be deployed between PE1 and PE2 to carry EVPN L3VPNv6 services.

**Figure 1** EVPN L3VPNv6 over SRv6 BE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001142846130.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable OSPFv3 on PE1, the P, and PE2.
3. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
4. Establish a BGP EVPN peer relationship between the PEs.
5. Configure SRv6 BE on the PEs and enable OSPFv3 SRv6.

#### Data Preparation

To complete the configuration, you need the following data:

* L3VPN instance name: vpn1
* RD and RT values of the L3VPN instance: 100:1 and 1:1

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001142686298__section_dc_vrp_evpn_cfg_015105) in this section.
   
   
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
3. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv6] vpn-target 1:1 evpn
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:DB8:11::1 64
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-6-vpn1] import-route direct
   ```
   ```
   [*PE1-bgp-6-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-6-vpn1] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpn1
   ```
   ```
   [*PE2-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv6] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv6] vpn-target 1:1 evpn
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ipv6 address 2001:DB8:22::1 64
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-6-vpn1] import-route direct
   ```
   ```
   [*PE2-bgp-6-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE2-bgp-6-vpn1] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
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
   [*CE1-bgp] router-id 11.11.11.11    
   [*CE1-bgp] peer 2001:DB8:11::1 as-number 100
   [*CE1-bgp] ipv6-family unicast
   [*CE1-bgp-af-ipv6] import-route direct
   [*CE1-bgp-af-ipv6] peer 2001:DB8:11::1 enable
   [*CE1-bgp-af-ipv6] commit
   [~CE1-bgp-af-ipv6] quit
   [~CE1-bgp] quit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] ipv6-family vpn-instance vpn1
   [*PE1-bgp-6-vpn1] peer 2001:DB8:11::2 as-number 65410
   [*PE1-bgp-6-vpn1] import-route direct
   [*PE1-bgp-6-vpn1] commit
   [~PE1-bgp-6-vpn1] quit
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface LoopBack1
   [*CE2-LoopBack1] ipv6 enable
   [*CE2-LoopBack1] ipv6 address 2001:DB8:222::222 128
   [*CE2-LoopBack1] quit               
   [*CE2] bgp 65420   
   [*CE2-bgp] router-id 22.22.22.22    
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
   [~PE2-bgp] router-id 3.3.3.3
   [*PE2-bgp] ipv6-family vpn-instance vpn1
   [*PE2-bgp-6-vpn1] peer 2001:DB8:22::2 as-number 65420
   [*PE2-bgp-6-vpn1] import-route direct
   [*PE2-bgp-6-vpn1] commit
   [~PE2-bgp-6-vpn1] quit
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv6 vpn-instance peer** command on each PE to check whether a BGP peer relationship has been established between the PE and its connected CE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv6 vpn-instance vpn1 peer
   
    BGP local router ID : 1.1.1.1          
    Local AS number : 100                  
    Total number of peers : 1                 Peers in established state : 1             
   
     VPN-Instance vpn1, Router ID 1.1.1.1:
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                              
     2001:DB8:11::2                   4       65410      868      873     0 12:34:11 Established        2 
   ```
5. Establish a BGP EVPN peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
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
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp evpn peer
   
    BGP local router ID : 1.1.1.1          
    Local AS number : 100                  
    Total number of peers : 1                 Peers in established state : 1             
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                              
     2001:DB8:3::3                    4         100      921      921     0 13:16:00 Established        4 
   ```
6. Configure SRv6 BE on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
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
   [*PE1-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-6-vpn1] segment-routing ipv6 locator PE1 evpn
   ```
   ```
   [*PE1-bgp-6-vpn1] segment-routing ipv6 best-effort evpn
   ```
   ```
   [*PE1-bgp-6-vpn1] quit
   ```
   ```
   [*PE1-bgp] quit
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
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:DB8:130:: 64 static 32
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
   [*PE2-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-6-vpn1] segment-routing ipv6 locator PE2 evpn
   ```
   ```
   [*PE2-bgp-6-vpn1] segment-routing ipv6 best-effort evpn
   ```
   ```
   [*PE2-bgp-6-vpn1] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
7. Verify the configuration.
   
   
   
   Run the **display bgp evpn all routing-table prefix-route** command on each PE. The command output shows IP prefix route information sent from the peer end. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn all routing-table prefix-route
    Local AS number : 100                  
   
    BGP Local router ID is 1.1.1.1         
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,      
                  h - history,  i - internal, s - suppressed, S - Stale                  
                  Origin : i - IGP, e - EGP, ? - incomplete                              
   
   
    EVPN address family:                   
    Number of Ip Prefix Routes: 5          
    Route Distinguisher: 100:1             
          Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop               
    *>    0:[2001:DB8:11::]:64                                   ::                      
    *                                                            2001:DB8:11::2         
    *>    0:[2001:DB8:111::111]:128                              2001:DB8:11::2    
    Route Distinguisher: 200:1           
          Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop               
    *>i   0:[2001:DB8:22::]:64                                   2001:DB8:3::3   
    *>i   0:[2001:DB8:222::222]:128                              2001:DB8:3::3  
   ```
   
   Run the **display ipv6 routing-table vpn-instance vpn1** command on each PE. The command output shows VPN route information sent from the peer end. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ipv6 routing-table vpn-instance vpn1
   Routing Table : vpn1                    
            Destinations : 6        Routes : 6                                           
   
   Destination  : 2001:DB8:111::111                       PrefixLength : 128             
   NextHop      : 2001:DB8:11::2                          Preference   : 255             
   Cost         : 0                                       Protocol     : EBGP            
   RelayNextHop : 2001:DB8:11::2                          TunnelID     : 0x0             
   Interface    : GigabitEthernet0/2/0                    Flags        : RD              
   
   Destination  : 2001:DB8:222::222                       PrefixLength : 128             
   NextHop      : 2001:DB8:130::1:0:3C                    Preference   : 255             
   Cost         : 0                                       Protocol     : IBGP            
   RelayNextHop : 2001:DB8:130::1:0:3C                    TunnelID     : 0x0             
   Interface    : GigabitEthernet0/1/0                    Flags        : RD              
   
   Destination  : 2001:DB8:11::                           PrefixLength : 64              
   NextHop      : 2001:DB8:11::1                          Preference   : 0               
   Cost         : 0                                       Protocol     : Direct          
   RelayNextHop : ::                                      TunnelID     : 0x0             
   Interface    : GigabitEthernet0/2/0                    Flags        : D               
   
   Destination  : 2001:DB8:11::1                          PrefixLength : 128             
   NextHop      : ::1                                     Preference   : 0 
   Cost         : 0                                       Protocol     : Direct          
   RelayNextHop : ::                                      TunnelID     : 0x0             
   Interface    : GigabitEthernet0/2/0                    Flags        : D               
   
   Destination  : 2001:DB8:22::                           PrefixLength : 64              
   NextHop      : 2001:DB8:130::1:0:3C                    Preference   : 255             
   Cost         : 0                                       Protocol     : IBGP            
   RelayNextHop : 2001:DB8:130::1:0:3C                    TunnelID     : 0x0             
   Interface    : GigabitEthernet0/1/0                    Flags        : RD 
   
   Destination  : FE80::                                  PrefixLength : 10              
   NextHop      : ::                                      Preference   : 0               
   Cost         : 0                                       Protocol     : Direct          
   RelayNextHop : ::                                      TunnelID     : 0x0             
   Interface    : NULL0                                   Flags        : DB  
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dt6** **forwarding** command to check information about the SRv6 local SID table. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt6 forwarding
   
                       My Local-SID End.DT6 Forwarding Table
                       -------------------------------------                             
   
   SID        : 2001:DB8:100::1:0:3C/128                     FuncType    : End.DT6          
   VPN Name   : vpn1                                         VPN ID      : 3                
   LocatorName: PE1                                          LocatorID   : 1
   Flavor     : NO-FLAVOR                                    SidCompress : NO
   UpdateTime : 2023-05-10 01:46:05.713
   
   Total SID(s): 1 
   ```
   
   Check that CEs belonging to the same VPN instance can ping each other. For example:
   
   ```
   [~CE1] ping ipv6 -a 2001:DB8:111::111 2001:DB8:222::222
     PING 2001:DB8:222::222 : 56  data bytes, press CTRL_C to break                                 
       Reply from 2001:DB8:222::222                   
       bytes=56 Sequence=1 hop limit=62 time=3 ms                                        
       Reply from 2001:DB8:222::222                   
       bytes=56 Sequence=2 hop limit=62 time=2 ms                                        
       Reply from 2001:DB8:222::222                   
       bytes=56 Sequence=3 hop limit=62 time=2 ms                                        
       Reply from 2001:DB8:222::222                   
       bytes=56 Sequence=4 hop limit=62 time=3 ms                                        
       Reply from 2001:DB8:222::222                   
       bytes=56 Sequence=5 hop limit=62 time=3 ms                                        
   
     --- 2001:DB8:222::222 ping statistics---         
       5 packet(s) transmitted             
       5 packet(s) received                
       0.00% packet loss                   
       round-trip min/avg/max=2/2/3 ms  
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
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
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:11::1/64
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
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE1 evpn
    segment-routing ipv6 best-effort evpn
    peer 2001:DB8:11::2 as-number 65410
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
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
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator PE2 ipv6-prefix 2001:DB8:130:: 64 static 32
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
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:22::1/64
  #
  interface LoopBack1
   ipv6 enable
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
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE2 evpn
    segment-routing ipv6 best-effort evpn
    peer 2001:DB8:22::2 as-number 65420
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
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
   ipv6 address 2001:DB8:11::2/64
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:111::111/128
  #               
  bgp 65410       
   router-id 11.11.11.11
   peer 2001:DB8:11::1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
    import-route direct
    peer 2001:DB8:11::1 enable
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
   router-id 22.22.22.22
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