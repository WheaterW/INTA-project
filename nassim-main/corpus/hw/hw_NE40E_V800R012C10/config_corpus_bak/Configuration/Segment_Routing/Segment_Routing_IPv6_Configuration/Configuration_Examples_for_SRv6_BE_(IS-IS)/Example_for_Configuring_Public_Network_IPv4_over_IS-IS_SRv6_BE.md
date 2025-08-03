Example for Configuring Public Network IPv4 over IS-IS SRv6 BE
==============================================================

This section provides an example for configuring SRv6 BE to carry public network IPv4 services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0227330333__fig_dc_vrp_srv6_cfg_all_001101), PE1, the P, and PE2 are in the same AS. They need to run IS-IS to implement IPv6 network connectivity. PE1, the P, and PE2 are Level-1 devices that belong to IS-IS process 1. An IBGP peer relationship needs to be established between PE1 and PE2, and EBGP peer relationships need to be established between PE1 and DeviceA and between PE2 and DeviceB.

A bidirectional SRv6 BE path needs to be deployed between PE1 and PE2 to carry public network IPv4 services.

**Figure 1** Public network IPv4 over SRv6 BE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0228398155.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on PE1, the P, and PE2.
3. Establish an EBGP peer relationship between PE1 and DeviceA and another one between PE2 and DeviceB.
4. Establish an MP-IBGP peer relationship between the PEs.
5. Configure SRv6 on PE1 and PE2, and enable IS-IS SRv6.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, the P, and PE2
* IS-IS process ID of PE1, the P, and PE2
* IS-IS level of PE1, the P, and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0227330333__example682311373210) in this section.
   
   
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
   [*PE1-isis-1] import-route direct
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
   [*P-isis-1] import-route direct
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
   [*P-GigabitEthernet0/2/0] commit
   ```
   ```
   [~P-GigabitEthernet0/2/0] quit
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
   [*PE2-isis-1] import-route direct
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
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   
                             Peer information for ISIS(1)
                            
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0            0000.0000.0002.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
   
   # Display IS-IS routing table information. The following example uses the command output on PE1.
   
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
   2001:DB8:10::/96       GE0/1/0            Direct                     10       D/-/L/-  
   2001:DB8:20::/96       GE0/1/0            FE80::3A92:6CFF:FE21:10    20       A/-/-/-                       
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut, 
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Establish an EBGP peer relationship between PE1 and DeviceA and another one between PE2 and DeviceB.
   
   
   
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
   
   After the configuration is complete, run the **display bgp peer** command on the PEs to check whether the BGP peer relationships have been established. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the command output on PE1 to show that a BGP peer relationship has been established between PE1 and DeviceA.
   
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
   [~PE1-bgp] peer 2001:DB8:2::2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:2::2 connect-interface loopback1
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:DB8:2::2 enable
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
     2001:DB8:2::2   4         100       10       11     0 00:05:15 Established        2                                             
   ```
5. Establish an SRv6 BE path between the PEs.
   
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
   [*PE1-segment-routing-ipv6] locator aa ipv6-prefix 2001:DB8:100:: 64 static 32
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
   [*PE1-isis-1] commit
   ```
   ```
   [~PE1-isis-1] quit
   ```
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:DB8:2::2 prefix-sid
   ```
   ```
   [*PE1-bgp-af-ipv4] segment-routing ipv6 best-effort
   ```
   ```
   [*PE1-bgp-af-ipv4] segment-routing ipv6 locator aa
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
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*PE2-segment-routing-ipv6] locator aa ipv6-prefix 2001:DB8:200:: 64 static 32
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
   [*PE2-isis-1] commit
   ```
   ```
   [~PE2-isis-1] quit
   ```
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] ipv4-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 2001:DB8:1::1 prefix-sid
   ```
   ```
   [*PE2-bgp-af-ipv4] segment-routing ipv6 best-effort
   ```
   ```
   [*PE2-bgp-af-ipv4] segment-routing ipv6 locator aa
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
6. Verify the configuration.
   
   
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end-dt4 forwarding** command to check information about the SRv6 local SID table. The following example uses the command output on PE1.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt4 forwarding
                       My Local-SID End.DT4 Forwarding Table
                       -------------------------------------
   
   SID        : 2001:DB8:100::1:0:1/128                 FuncType    : End.DT4  
   VPN Name   : _public_                                VPN ID      : 0
   LocatorName: aa                                      LocatorID   : 1
   Flavor     : NO-FLAVOR                               SidCompress : NO
   UpdateTime : 2023-05-10 01:46:05.713
   
   Total SID(s): 1
   ```
   
   Run the **display bgp routing-table** command to check information about the BGP routing table. The following example uses the command output on PE2.
   
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
    Original nexthop: 2001:DB8:1::1
    Qos information : 0x0
    Prefix-sid: 2001:DB8:100::1:0:1
    AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 20
    Advertised to such 1 peers:
       192.168.2.1
   ```
   
   Check that DeviceA and DeviceB can ping each other. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] ping 192.168.2.1
     PING 192.168.2.1: 56  data bytes, press CTRL_C to break
       Reply from 192.168.2.1: bytes=56 Sequence=1 ttl=253 time=7 ms
       Reply from 192.168.2.1: bytes=56 Sequence=2 ttl=253 time=5 ms
       Reply from 192.168.2.1: bytes=56 Sequence=3 ttl=253 time=4 ms
       Reply from 192.168.2.1: bytes=56 Sequence=4 ttl=253 time=5 ms
       Reply from 192.168.2.1: bytes=56 Sequence=5 ttl=253 time=5 ms
   
     --- 192.168.2.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 4/5/7 ms
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1        
  # 
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator aa ipv6-prefix 2001:DB8:100:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   import-route direct
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
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    network 192.168.1.0 255.255.255.0
    segment-routing ipv6 locator aa
    segment-routing ipv6 best-effort
    peer 192.168.1.1 enable
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 prefix-sid
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P        
  #
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   import-route direct
   #              
   ipv6 enable topology ipv6
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
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator aa ipv6-prefix 2001:DB8:200:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   import-route direct
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
   ipv6 address 2001:DB8:2::2/128
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
    segment-routing ipv6 locator aa
    segment-routing ipv6 best-effort
    peer 192.168.2.1 enable
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 prefix-sid
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