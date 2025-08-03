Example for Configuring BD-based EVPN VPLS over MPLS in Ring Network Access Mode
================================================================================

This section provides an example for configuring BD-based EVPN VPLS over MPLS in ring network access mode, with MSTP used as the loop prevention protocol.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001118104816__fig79111962410), to implement EVPN in ring network access mode, configure multi-ring topology isolation and MSTP on the network. To enable PE2 to quickly update MAC route information, ensure that the Ethernet A-D routes carry MAC-Flush and Ring ID extended community attributes. In this manner, route convergence is achieved.

**Figure 1** Configuring BD-based EVPN VPLS over MPLS in ring network access mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, interface3, and interface4 in this example represent GigabitEthernet0/1/1, GigabitEthernet0/1/2, GigabitEthernet0/1/3, and GigabitEthernet0/1/4, respectively.


  
![](figure/en-us_image_0000001187211938.png)

#### Configuration Precautions

During the configuration process, note the following:

* Currently, Eth-Trunk sub-interfaces need to be configured for BD EVPN access.
* The **link-protocol transport bpdu untag-vlan-check** command needs to be configured on PE1 and PE2 to transparently transmit VLAN packets.
* The **stp tc-snooping notify bridge-domain process** command needs to be configured on PE1 and PE2 to enable TC notification on the main interfaces.
* PE1 and PE2 must have different ESIs and the same EVPN STP ring ID configured.
* Using the local loopback interface address of each PE as the source address of the PE is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP for PEs to communicate.
2. Configure basic MPLS functions and MPLS LDP to establish MPLS LSPs.
3. Configure a BD EVPN instance on each PE.
4. Establish BGP EVPN peer relationships.
5. Configure MSTP on PEs and CEs.
6. Configure IP addresses of the same network segment for CEs' VLANIF interfaces. Then perform a ping operation on the network segment to trigger the local and remote PEs to learn CE-side MAC addresses.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name (evpna)
* EVPN instance evpna's RD (1:1) and RTs (1:1) on each PE
* BD ID (1)

#### Procedure

1. Configure interface addresses on the PEs and CEs according to [Figure 1](#EN-US_TASK_0000001118104816__fig79111962410). For detailed configurations, see Configuration Files.
2. Configure PE and CE IP addresses, including their loopback addresses.
   
   
   
   Configure interface IP addresses and masks. For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001118104816__file1).
3. Configure an IGP between PEs and between PEs and CEs. In this example, IS-IS is used.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001118104816__file1).
4. Configure basic MPLS functions and MPLS LDP, and set up LDP LSPs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0000001118104816__file1).
5. Configure an EVPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evpna bd-mode
   ```
   ```
   [*PE1-evpn-instance-evpna] route-distinguisher 1:1
   ```
   ```
   [*PE1-evpn-instance-evpna] vpn-target 1:1
   ```
   ```
   [*PE1-evpn-instance-evpna] quit
   ```
   ```
   [*PE1] bridge-domain 1
   ```
   ```
   [*PE1-bd1] evpn binding vpn-instance evpna
   ```
   ```
   [*PE1-bd1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evpna bd-mode
   ```
   ```
   [*PE2-evpn-instance-evpna] route-distinguisher 1:1
   ```
   ```
   [*PE2-evpn-instance-evpna] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evpna] quit
   ```
   ```
   [*PE2] bridge-domain 1
   ```
   ```
   [*PE2-bd1] evpn binding vpn-instance evpna
   ```
   ```
   [*PE2-bd1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evpna bd-mode
   ```
   ```
   [*PE3-evpn-instance-evpna] route-distinguisher 1:1
   ```
   ```
   [*PE3-evpn-instance-evpna] vpn-target 1:1
   ```
   ```
   [*PE3-evpn-instance-evpna] quit
   ```
   ```
   [*PE3] bridge-domain 1
   ```
   ```
   [*PE3-bd1] evpn binding vpn-instance evpna
   ```
   ```
   [*PE3-bd1] quit
   ```
   ```
   [*PE3] commit
   ```
6. Configure a source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 10.1.1.1
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 10.2.1.1
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 10.3.1.1
   ```
   ```
   [*PE3] commit
   ```
7. Establish BGP EVPN peer relationships.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 10.1.1.1
   ```
   ```
   [*PE1-bgp] group ipv4_i internal
   ```
   ```
   [*PE1-bgp] peer 10.2.1.1 as-number 100
   ```
   ```
   [*PE1-bgp] peer 10.2.1.1 group ipv4_i
   ```
   ```
   [*PE1-bgp] peer 10.2.1.1 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] peer 10.3.1.1 as-number 100
   ```
   ```
   [*PE1-bgp] peer 10.3.1.1 group ipv4_i
   ```
   ```
   [*PE1-bgp] peer 10.3.1.1 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer ipv4_i enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 10.2.1.1 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 10.2.1.1 group ipv4_i
   ```
   ```
   [*PE1-bgp-af-evpn] peer 10.3.1.1 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 10.3.1.1 group ipv4_i
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
   [*PE2-bgp] router-id 10.2.1.1
   ```
   ```
   [*PE2-bgp] group ipv4_i internal
   ```
   ```
   [*PE2-bgp] peer 10.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 10.1.1.1 group ipv4_i
   ```
   ```
   [*PE2-bgp] peer 10.3.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 10.3.1.1 group ipv4_i
   ```
   ```
   [*PE2-bgp] peer ipv4_i connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer ipv4_i enable
   ```
   ```
   [*PE2-bgp-af-evpn] peer 10.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] peer 10.1.1.1 group ipv4_i
   ```
   ```
   [*PE2-bgp-af-evpn] peer 10.3.1.1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] peer 10.3.1.1 group ipv4_i
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
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] router-id 10.3.1.1
   ```
   ```
   [*PE3-bgp] group ipv4_i internal
   ```
   ```
   [*PE3-bgp] peer 10.1.1.1 as-number 100
   ```
   ```
   [*PE3-bgp] peer 10.1.1.1 group ipv4_i
   ```
   ```
   [*PE3-bgp] peer 10.2.1.1 as-number 100
   ```
   ```
   [*PE3-bgp] peer 10.2.1.1 group ipv4_i
   ```
   ```
   [*PE3-bgp] peer ipv4_i connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] l2vpn-family evpn
   ```
   ```
   [*PE3-bgp-af-evpn] peer ipv4_i enable
   ```
   ```
   [*PE3-bgp-af-evpn] peer 10.1.1.1 enable
   ```
   ```
   [*PE3-bgp-af-evpn] peer 10.1.1.1 group ipv4_i
   ```
   ```
   [*PE3-bgp-af-evpn] peer 10.2.1.1 enable
   ```
   ```
   [*PE3-bgp-af-evpn] peer 10.2.1.1 group ipv4_i
   ```
   ```
   [*PE3-bgp-af-evpn] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   After completing the configurations, run the **display bgp evpn peer** command on PE1. The command output shows that BGP peer relationships are in the **Established** state, indicating that BGP peer relationships have been successfully established between PEs.
   
   ```
   [~PE1] display bgp evpn peer
   ```
   ```
    
    BGP local router ID : 10.1.1.1
    Local AS number : 100
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.2.1.1         4         100       10       18     0 00:00:11 Established        6
     10.3.1.1         4         100       10       20     0 00:00:12 Established        6
   ```
8. Configure CEs.
   
   
   
   # Configure CE1 and add it to an MSTP process with the specified ID.
   
   ```
   [~CE1] interface gigabitethernet0/1/1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] stp process 1 instance 1 cost 1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] stp binding process 1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] interface gigabitethernet0/1/2
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port trunk allow-pass vlan 2
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] stp process 2 instance 2 cost 1
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] stp binding process 2
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface gigabitethernet0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] stp process 1 instance 1 cost 4000
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] stp binding process 1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] interface gigabitethernet0/1/2
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] port trunk allow-pass vlan 2
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] stp process 2 instance 2 cost 4000
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] stp binding process 2
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE2] commit
   ```
9. Verify the configuration. 
   
   
   
   After the preceding configurations are complete, CE1 and CE2 can ping each other, and the local and remote PEs are triggered to learn MAC addresses from CEs.
   
   ```
   [~CE1] ping 10.4.1.2
     PING 10.4.1.2: 56  data bytes, press CTRL_C to break         
       Reply from 10.4.1.2: bytes=56 Sequence=1 ttl=253 time=127 ms             
       Reply from 10.4.1.2: bytes=56 Sequence=2 ttl=253 time=19 ms              
       Reply from 10.4.1.2: bytes=56 Sequence=3 ttl=253 time=26 ms              
       Reply from 10.4.1.2: bytes=56 Sequence=4 ttl=253 time=17 ms              
       Reply from 10.4.1.2: bytes=56 Sequence=5 ttl=253 time=16 ms              
   
     --- 10.4.1.2 ping statistics ---                   
       5 packet(s) transmitted                             
       5 packet(s) received                                
       0.00% packet loss                                   
       round-trip min/avg/max = 16/41/127 ms
   [~PE1]display mac-address
   MAC address table of slot 3:
   ----------------------------------------------------------------------------------------------------------------------
   MAC Address    VLAN/BD/                        PEVLAN CEVLAN Port/Peerip                        Type      LSP/LSR-ID
                  VSI/SI/EVPN                                                                                MAC-Tunnel
   ----------------------------------------------------------------------------------------------------------------------
   00e0-fc12-3457 BD 1                            *1     -      -                                  dynamic       3/-         
   00e0-fc12-3456 BD 1                            *1     -      Eth-Trunk10.1                      dynamic       3/-         
   ----------------------------------------------------------------------------------------------------------------------
   Total matching items on slot 3 displayed = 2
   ```
   
   Run the **display bgp evpn all routing-table** **ad-route** command on PE1. The command output shows the A-D route destined for CE1 sent from the remote PE.
   
   ```
   [~PE1]display bgp evpn all routing-table ad-route 0000.1111.0000.0000.0001:0
    BGP local router ID : 10.1.1.1
    Local AS number : 100
    Total routes of Route Distinguisher(1:1): 1
    BGP routing table entry information of 0000.1111.0000.0000.0001:0:
    From: 0.0.0.0 (0.0.0.0)
    Route Duration: 0d00h30m53s
    Direct Out-interface: NULL0
    Original nexthop: 127.0.0.1
    Qos information : 0x0
    Ext-Community: RT <1 : 1>, SoO <1.1.1.1 : 0>, Router ID <10.1.1.1>, MAC Flush <0 : 0 : 3>, Ring ID <0 : 0 : 1>
    AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, pre 255
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
    ESI: 0000.1111.0000.0000.0001, Ethernet Tag ID: 0
    Advertised to such 2 peers:
       10.2.1.1
       10.3.1.1
    EVPN-Instance e1:
    Number of A-D Routes: 1
    BGP routing table entry information of 0000.1111.0000.0000.0001:0:
    Route Distinguisher: 1:1
    Local-Generate route.
    From: 0.0.0.0 (0.0.0.0)
    Route Duration: 0d00h51m09s
    Relay IP Nexthop: 0.0.0.0
    Relay IP Out-Interface: NULL0
    Original nexthop: 127.0.0.1
    Qos information : 0x0
    Ext-Community: Router ID <10.1.1.1>, Ring ID <0 : 0 : 1>
    AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, pre 255
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
    ESI: 0000.1111.0000.0000.0001, Ethernet Tag ID: 0
    Not advertised to any peer yet
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  vlan batch 1 to 100
  #
  l2protocol-tunnel stp group-mac 0100-5e00-0011
  #
  evpn vpn-instance evpna bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  stp process 1
   stp pathcost-standard legacy
   stp region-configuration
    region-name abc1
    instance 1 vlan 1
  #
  stp process 2
   stp pathcost-standard legacy
   stp region-configuration
    region-name abc2
    instance 2 vlan 2
  #
  mpls lsr-id 10.1.1.1
  #
  mpls
   mpls te
  #
  mpls l2vpn
  #
  mpls ldp
   #                                                                              
   ipv4-family 
  # 
  bridge-domain 1
   mac-learn-style qualify
   evpn binding vpn-instance evpna
  # 
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0027.00
   traffic-eng level-2
  #
  interface Eth-Trunk10
   stp tc-snooping enable
   stp tc-snooping notify bridge-domain process 1
   esi 0000.1111.0000.0000.0001
   evpn stp-ring-id 1
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 1
   bridge-domain 1
   link-protocol transport bpdu untag-vlan-check
  #
  interface Eth-Trunk11
   stp tc-snooping enable
   stp tc-snooping notify bridge-domain process 2
   esi 0000.2222.0000.0000.0001
   evpn stp-ring-id 2
  #
  interface Eth-Trunk11.2 mode l2
   encapsulation dot1q vid 2
   bridge-domain 1
   link-protocol transport bpdu untag-vlan-check
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   eth-trunk 10
   dcn
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   eth-trunk 11
   dcn
  #
  interface LoopBack1
   ipv6 enable
   ip address 10.1.1.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   router-id 10.1.1.1
   group ipv4_i internal
   peer 10.2.1.1 as-number 100
   peer 10.2.1.1 group ipv4_i
   peer 10.2.1.1 connect-interface LoopBack1
   peer 10.3.1.1 as-number 100
   peer 10.3.1.1 group ipv4_i
   peer 10.3.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer ipv4_i enable
    peer 10.2.1.1 enable
    peer 10.2.1.1 group ipv4_i
    peer 10.3.1.1 enable
    peer 10.3.1.1 group ipv4_i
   #
   l2vpn-family evpn
    policy vpn-target
    peer ipv4_i enable
    peer 10.2.1.1 enable
    peer 10.2.1.1 group ipv4_i
    peer 10.3.1.1 enable
    peer 10.3.1.1 group ipv4_i
  #
  evpn source-address 10.1.1.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  vlan batch 1 to 100
  #
  l2protocol-tunnel stp group-mac 0100-5e00-0011
  #
  evpn vpn-instance evpna bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  stp process 1
   stp pathcost-standard legacy
   stp region-configuration
    region-name abc1
    instance 1 vlan 1
  #
  stp process 2
   stp pathcost-standard legacy
   stp region-configuration
    region-name abc2
    instance 2 vlan 2
  #
  mpls lsr-id 10.2.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  bridge-domain 1
   mac-learn-style qualify
   evpn binding vpn-instance evpna
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0029.00
   traffic-eng level-2
  #
  interface Eth-Trunk10
   stp tc-snooping enable
   stp tc-snooping notify bridge-domain process 1
   esi 0000.1111.0000.0000.0002
   evpn stp-ring-id 1
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 1
   bridge-domain 1
   link-protocol transport bpdu untag-vlan-check
  #
  interface Eth-Trunk11
   stp tc-snooping enable
   stp tc-snooping notify bridge-domain process 2
   esi 0000.2222.0000.0000.0002
   evpn stp-ring-id 2
  #
  interface Eth-Trunk11.2 mode l2
   encapsulation dot1q vid 2
   bridge-domain 1
   link-protocol transport bpdu untag-vlan-check
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.3.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   eth-trunk 10
   dcn
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   eth-trunk 11
   dcn
  #
  interface LoopBack1
   ip address 10.2.1.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   router-id 10.2.1.1
   group ipv4_i internal
   peer ipv4_i connect-interface LoopBack1
   peer 10.1.1.1 as-number 100
   peer 10.1.1.1 group ipv4_i
   peer 10.3.1.1 as-number 100
   peer 10.3.1.1 group ipv4_i
   #
   ipv4-family unicast
    undo synchronization
    peer ipv4_i enable
    peer 10.1.1.1 enable
    peer 10.1.1.1 group ipv4_i
    peer 10.3.1.1 enable
    peer 10.3.1.1 group ipv4_i
   #
   l2vpn-family evpn
    policy vpn-target
    peer ipv4_i enable
    peer 10.1.1.1 enable
    peer 10.1.1.1 group ipv4_i
    peer 10.3.1.1 enable
    peer 10.3.1.1 group ipv4_i
  #
  evpn source-address 10.2.1.1
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  vlan batch 1 to 100
  #
  evpn vpn-instance evpna bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 10.3.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  bridge-domain 1
   mac-learn-style qualify
   evpn binding vpn-instance evpna
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0028.00
   traffic-eng level-2
  #
  interface Eth-Trunk10
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 1
   bridge-domain 1
  #
  interface Eth-Trunk10.2 mode l2
   encapsulation dot1q vid 2
   bridge-domain 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.3.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
   undo dcn
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
   undo dcn
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   eth-trunk 10
   undo dcn
  #
  interface LoopBack1
   ip address 10.3.1.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   router-id 10.3.1.1
   group ipv4_i internal
   peer ipv4_i connect-interface LoopBack1
   peer 10.1.1.1 as-number 100
   peer 10.1.1.1 group ipv4_i
   peer 10.2.1.1 as-number 100
   peer 10.2.1.1 group ipv4_i
   #
   ipv4-family unicast
    undo synchronization
    peer ipv4_i enable
    peer 10.1.1.1 enable
    peer 10.1.1.1 group ipv4_i
    peer 10.2.1.1 enable
    peer 10.2.1.1 group ipv4_i
   #
   l2vpn-family evpn
    policy vpn-target
    peer ipv4_i enable
    peer 10.1.1.1 enable
    peer 10.1.1.1 group ipv4_i
    peer 10.2.1.1 enable
    peer 10.2.1.1 group ipv4_i
  #
  evpn source-address 10.3.1.1
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan batch 1 to 2
  #
  stp process 1
   stp instance 1 root primary
   stp pathcost-standard legacy
   stp enable
   stp region-configuration
    region-name abc1
    instance 1 vlan 1
  #
  stp process 2
   stp instance 2 root primary
   stp pathcost-standard legacy
   stp enable
   stp region-configuration
    region-name abc2
    instance 2 vlan 2
  #
  isis 1
    is-level level-2
    cost-style wide
    network-entity 10.0000.0000.0030.00
    traffic-eng level-2
  #
  interface Vlanif1
   ip address 10.4.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 1
   stp process 1 instance 1 cost 1
   stp binding process 1
   undo dcn
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
   stp process 2 instance 2 cost 1
   stp binding process 2
   undo dcn
  #
  interface GigabitEthernet0/1/3
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 1
   stp process 1 instance 1 cost 1
   stp binding process 1
   undo dcn
  #
  interface GigabitEthernet0/1/4
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
   stp process 2 instance 2 cost 1
   stp binding process 2
   undo dcn
  #
  interface LoopBack1
    ip address 1.1.1.1 255.255.255.255
    isis enable 1
  #
  return
  ```
* CE2 configuration file
  ```
  #
  sysname CE2
  #
  vlan batch 1 to 2
  #
  stp process 1
   stp pathcost-standard legacy
   stp enable
   stp region-configuration
    region-name abc1
    instance 1 vlan 1
  #
  stp process 2
   stp pathcost-standard legacy
   stp enable
   stp region-configuration
    region-name abc2
    instance 2 vlan 2
  #
  isis 1
    is-level level-2
    cost-style wide
    network-entity 10.0000.0000.0031.00
    traffic-eng level-2
  #
  interface Vlanif1
   ip address 10.4.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 1
   stp process 1 instance 1 cost 4000
   stp binding process 1
   undo dcn
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
   stp process 2 instance 2 cost 4000
   stp binding process 2
   undo dcn
  #
  interface GigabitEthernet0/1/3
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 1
   stp process 1 instance 1 cost 1
   stp binding process 1
   undo dcn
  #
  interface GigabitEthernet0/1/4
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
   stp process 2 instance 2 cost 1
   stp binding process 2
   undo dcn
  #
  interface LoopBack1
    ip address 2.2.2.2 255.255.255.255
    isis enable 1
  #
  return
  ```