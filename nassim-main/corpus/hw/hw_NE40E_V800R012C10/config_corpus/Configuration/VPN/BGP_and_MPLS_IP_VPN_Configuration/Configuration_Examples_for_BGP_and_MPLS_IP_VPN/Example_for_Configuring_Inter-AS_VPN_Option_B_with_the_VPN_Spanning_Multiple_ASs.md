Example for Configuring Inter-AS VPN Option B with the VPN Spanning Multiple ASs
================================================================================

In the scenario where the backbone network spans multiple ASs, ASBRs advertise labeled VPN-IPv4 routes through MP-EBGP.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172369515__fig_dc_vrp_mpls-l3vpn-v4_cfg_011901), CE1 and CE2 belong to vpna and need to communicate across across AS 100, AS 200, and AS 300. Like in basic inter-AS VPN Option B, you do not need to create a VPN instance on each ASBR. You only need to configure each ASBR to receive VPNv4 routes and advertise them to the peer ASBR. In addition, an MP-IBGP peer relationship needs to be established between ASBRs in AS 200.

**Figure 1** Configuring inter-AS VPN Option B (with the VPN spanning multiple ASs)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0249477987.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| CE1 | Loopback1 | 10.11.11.11/32 |
| GE0/1/0 | 10.1.1.1/24 |
| PE1 | Loopback1 | 10.31.1.9/32 |
| GE0/1/0 | 172.16.1.2/24 |
| GE0/2/0 | 10.1.1.2/24 |
| ASBR1 | Loopback1 | 10.32.2.9/32 |
| GE0/1/0 | 172.16.1.1/24 |
| GE0/2/0 | 192.168.1.1/24 |
| ASBR2 | Loopback1 | 10.33.3.9/32 |
| GE0/1/0 | 10.162.1.1/24 |
| GE0/2/0 | 192.168.1.2/24 |
| ASBR3 | Loopback1 | 10.34.4.9/32 |
| GE0/1/0 | 10.162.1.2/24 |
| GE0/2/0 | 192.168.2.1/24 |
| ASBR4 | Loopback1 | 10.35.5.9/32 |
| GE0/1/0 | 10.152.1.1/24 |
| GE0/2/0 | 192.168.2.2/24 |
| PE2 | Loopback1 | 10.36.6.9/32 |
| GE0/1/0 | 10.152.1.2/24 |
| GE0/2/0 | 10.2.1.2/24 |
| CE2 | Loopback1 | 10.22.22.22/32 |
| GE0/1/0 | 10.2.1.1/24 |



#### Precautions

During the configuration process, note the following:

* Configure an MP-EBGP peer relationship between the ASBRs in different ASs. Configure an MP-IBGP peer relationship between the ASBRs or the PE and ASBR in the same AS.
* The ASBRs do not filter received VPNv4 routes based on VPN targets.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP in each AS for communication between devices in the same AS; set up an MPLS LDP LSP between the ASBRs or the ASBR and PE in the same AS.
2. Configure an MP-EBGP peer relationship between the ASBRs in different ASs. Configure an MP-IBGP peer relationship between the ASBRs or the PE and ASBR in the same AS.
3. Configure VPN instances on PEs and bind the interfaces connected to CEs to the VPN instances.
4. Enable MPLS on the interconnection interfaces between ASBRs and establish an MP-EBGP peer relationship between the ASBRs. Configure the ASBRs not to filter received VPNv4 routes based on VPN targets.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs and ASBRs: 10.31.1.9, 10.32.2.9, 10.33.3.9, 10.34.4.9, 10.35.5.9, and 10.36.6.9
* Name (vpna), RD (100:1/200:1), and export and import VPN targets (111:1) of the VPN instance on each PE

#### Procedure

1. On the MPLS backbone network in each AS, configure IGP for IP connectivity between devices on each network.
   
   
   
   This example uses OSPF as IGP. For configuration details, see the configuration files.
   
   After the configurations are complete, the OSPF neighbor relationship can be established between the devices in the same AS. Run the **display ospf peer** command. The command output shows that the neighbor relationship is in the **Full** state. The devices in the same AS can learn and successfully ping the address of each other's loopback interface.
2. Configure basic MPLS capabilities and MPLS LDP on the MPLS backbone network in each AS to establish LDP LSPs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 10.31.1.9
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   
   The configuration of PE2 is similar to the configuration of PE1. For configuration details, see the configuration file.
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls lsr-id 10.32.2.9
   ```
   ```
   [*ASBR1] mpls
   ```
   ```
   [*ASBR1-mpls] quit
   ```
   ```
   [*ASBR1] mpls ldp
   ```
   ```
   [*ASBR1-mpls-ldp] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/1/0] quit
   ```
   
   The configurations of ASBR2, ASBR3, and ASBR4 are similar to the configuration of ASBR1. For detailed configurations, see the configuration files.
   
   After the configurations are complete, LDP peer relationships can be established between the PE and ASBR and between the ASBRs. Run the **display mpls ldp session** command on each device. The command output shows that the session status is **Operational**. The following example uses the command output on PE1.
   
   ```
   <PE1> display mpls ldp session
   
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted. 
    -------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
    -------------------------------------------------------------------------
    10.32.2.9:0        Operational DU   Passive 0000:00:01  5/5
    -------------------------------------------------------------------------
    TOTAL: 1 session(s) Found.
   ```
3. Establish an MP-IBGP peer relationship between the PE and ASBR or between the ASBRs in the same AS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 10.32.2.9 as-number 100
   ```
   ```
   [*PE1-bgp] peer 10.32.2.9 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 10.32.2.9 enable
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
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 10.31.1.9 as-number 100
   ```
   ```
   [*ASBR1-bgp] peer 10.31.1.9 connect-interface loopback 1
   ```
   ```
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 10.31.1.9 enable
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] commit
   ```
   ```
   [~ASBR1-bgp-af-vpnv4] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   The configurations of devices in AS 200 and AS 300 are similar to the configurations of devices in AS 100. For configuration details, see the configuration files.
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command on the PE or ASBR. The command output shows that an MP-IBGP peer relationship has been established between the PE and ASBR or between the ASBRs in the same AS. The following example uses the command output on PE1.
   
   ```
   <PE1> display bgp vpnv4 all peer
   
    BGP local router ID : 10.31.1.9
    Local AS number : 100
    Total number of peers : 1         Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
   
     10.32.2.9       4         100    18970    19008     0 91:51:24   Established    0
   
   ```
4. Create a VPN instance on each PE.
   
   
   
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
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.2 24
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
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpna] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/0] quit
   ```
   
   After completing the configurations, run the **display ip vpn-instance verbose** command on each PE to check VPN instance configurations.
   
   ```
   <PE1> display ip vpn-instance verbose
    Total VPN-Instances configured : 1
    Total IPv4 VPN-Instances configured : 1 
    Total IPv6 VPN-Instances configured : 0
    
    VPN-Instance Name and ID : vpna, 1
     Interfaces : GigabitEthernet0/2/0
    Address family ipv4 
     Create date : 2009/09/18 11:30:35
     Up time : 0 days, 00 hours, 05 minutes and 19 seconds
     Vrf Status : UP
     Route Distinguisher : 100:1
     Export VPN Targets :  111:1
     Import VPN Targets :  111:1
     Label policy: label per route
     The diffserv-mode Information is : uniform
     The ttl-mode Information is : pipe
   ```
5. Establish EBGP peer relationships between PEs and CEs, and import loopback routes from CEs into BGP.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-Loopback1] ip address 10.11.11.11 32
   ```
   ```
   [*CE1-Loopback1] quit
   ```
   ```
   [*CE1] bgp 65001
   ```
   ```
   [*CE1-bgp] peer 10.1.1.2 as-number 100
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   
   The configuration of CE2 is similar to the configuration of CE1. For configuration details, see the configuration file.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] peer 10.1.1.1 as-number 65001
   ```
   ```
   [*PE1-bgp-vpna] commit
   ```
   ```
   [~PE1-bgp-vpna] quit
   ```
   
   The configuration of PE2 is similar to the configuration of PE1. For configuration details, see the configuration file.
   
   After completing the configurations, run the **display bgp vpnv4 vpn-instance peer** command on PEs to check whether BGP peer relationships have been established between the PEs and CEs. The command output shows that the BGP peer relationships have been established between the PEs and CEs and are in the **Established** state.
   
   The following example uses the command output on PE1 to show that a BGP peer relationship has been established between PE1 and CE1.
   
   ```
   <PE1> display bgp vpnv4 vpn-instance vpna peer
   
    BGP local router ID : 10.31.1.9
    Local AS number : 100
    Total number of peers : 1            Peers in established state : 1
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     10.1.1.1        4   65001  11     9          0     00:06:37   Established  1
   ```
6. Set up an MP-EBGP peer relationship between ASBRs in different ASs, and disable VPN-target-based filtering for received VPNv4 routes.
   
   
   
   # On ASBR1, enable MPLS on GE0/2/0 connected to ASBR2.
   
   ```
   [~ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] ip address 192.168.1.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] quit
   ```
   
   # On ASBR2, enable MPLS on GE0/2/0 that connects ASBR2 to ASBR1.
   
   ```
   [~ASBR2] interface gigabitethernet 0/2/0
   ```
   ```
   [~ASBR2-GigabitEthernet0/2/0] ip address 192.168.1.2 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] commit
   ```
   ```
   [~ASBR2-GigabitEthernet0/2/0] quit
   ```
   
   # Configure ASBR1 to establish an MP-EBGP peer with ASBR2, and disable ASBR1 from filtering received VPNv4 routes based on VPN targets.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [~ASBR1-bgp] peer 192.168.1.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 192.168.1.2 enable
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] commit
   ```
   ```
   [~ASBR1-bgp-af-vpnv4] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   # On ASBR2, set up an MP-EBGP peer relationship with ASBR1, and disable ASBR2 from filtering received VPNv4 routes based on VPN targets.
   
   ```
   [~ASBR2] bgp 200
   ```
   ```
   [~ASBR2-bgp] peer 192.168.1.1 as-number 100
   ```
   ```
   [*ASBR2-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR2-bgp-af-vpnv4] peer 192.168.1.1 enable
   ```
   ```
   [*ASBR2-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*ASBR2-bgp-af-vpnv4] commit
   ```
   ```
   [~ASBR2-bgp-af-vpnv4] quit
   ```
   ```
   [~ASBR2-bgp] quit
   ```
   
   The configurations of ASBR3 and ASBR4 are similar to the configurations of ASBR1 and ASBR2.
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command. The command output shows that an MP-EBGP peer relationship has been established between the ASBRs. The following example uses the command output on ASBR1.
   
   ```
   <PE1> display bgp vpnv4 all peer
   
    BGP local router ID : 10.32.2.9
    Local AS number : 100
    Total number of peers : 2         Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
   
     10.31.1.9       4         100    17533    17554     0 127:24:5 Established    1
     10.33.3.9       4         200    12343    34554     0 127:24:5 Established    1
   ```
7. Verify the configuration.
   
   
   
   After the configurations are complete, the CEs can learn routes to the loopback interface of each other, and can ping each other.
   
   The following example uses the command output on CE1.
   
   ```
   <CE1> display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 9        Routes : 9
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
          10.1.1.0/24  Direct 0    0             D  10.1.1.1        GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
        10.1.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
       10.11.11.11/32  Direct 0    0             D  127.0.0.1       LoopBack1
      10.22.22.22/32  EBGP   255  0             D  10.1.1.2        GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   <CE1> ping -a 10.11.11.11 10.22.22.22
     PING 10.22.22.22: 56  data bytes, press CTRL_C to break
       Reply from 10.22.22.22: bytes=56 Sequence=1 ttl=252 time=120 ms
       Reply from 10.22.22.22: bytes=56 Sequence=2 ttl=252 time=73 ms
       Reply from 10.22.22.22: bytes=56 Sequence=3 ttl=252 time=111 ms
       Reply from 10.22.22.22: bytes=56 Sequence=4 ttl=252 time=86 ms
       Reply from 10.22.22.22: bytes=56 Sequence=5 ttl=252 time=110 ms
     --- 10.22.22.22 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 73/100/120 ms 
   ```
   
   Run the **display bgp vpnv4 all routing-table** command on an ASBR to check VPNv4 routes.
   
   The following example uses the command output on ASBR1.
   
   <ASBR1> **display bgp vpnv4 all routing-table**
   
   ```
    BGP Local router ID is 10.32.2.9
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total number of routes from all PE: 2
    Route Distinguisher: 100:1
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  10.11.11.11/32     10.31.1.9       0          100        0      65001i
    Route Distinguisher: 200:1
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   10.22.22.22/32     192.168.1.2                             0   300 65002i
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface Loopback 1
   ip address 10.11.11.11 255.255.255.255
  #
  bgp 65001
   peer 10.1.1.2 as-number 100
   network 10.11.11.11 255.255.255.255
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.2 enable
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 10.31.1.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 10.31.1.9 255.255.255.255
  #
  bgp 100
   peer 10.32.2.9 as-number 100
   peer 10.32.2.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 10.32.2.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.32.2.9 enable
  #
   ipv4-family vpn-instance vpna
    peer 10.1.1.1 as-number 65001
  #
  ospf 1
   area 0.0.0.0
    network 10.31.1.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 10.32.2.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 10.32.2.9 255.255.255.255
  #
  bgp 100
   peer 192.168.1.2 as-number 200
   peer 10.31.1.9 as-number 100
   peer 10.31.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.2 enable
    peer 10.31.1.9 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 10.31.1.9 enable
    peer 192.168.1.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.32.2.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 10.33.3.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.162.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 10.33.3.9 255.255.255.255
  #
  bgp 200
   peer 192.168.1.1 as-number 100
   peer 10.34.4.9 as-number 200
   peer 10.34.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.1 enable
    peer 10.34.4.9 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 10.34.4.9 enable
    peer 192.168.1.1 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.33.3.9 0.0.0.0
    network 10.162.1.0 0.0.0.255
  #
  return
  ```
* ASBR3 configuration file
  
  ```
  #
  sysname ASBR3
  #
  mpls lsr-id 10.34.4.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.162.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 10.34.4.9 255.255.255.255
  #
  bgp 200
   peer 192.168.2.2 as-number 300
   peer 10.33.3.9 as-number 200
   peer 10.33.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.2.2 enable
    peer 10.33.3.9 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 10.33.3.9 enable
    peer 192.168.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.34.4.9 0.0.0.0
    network 10.162.1.0 0.0.0.255
  #
  return
  ```
* ASBR4 configuration file
  
  ```
  #
  sysname ASBR4
  #
  mpls lsr-id 10.35.5.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.152.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 10.35.5.9 255.255.255.255
  #
  bgp 300
   peer 192.168.2.1 as-number 200
   peer 10.36.6.9 as-number 300
   peer 10.36.6.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.2.1 enable
    peer 10.36.6.9 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 10.36.6.9 enable
    peer 192.168.2.1 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.35.5.9 0.0.0.0
    network 10.152.1.0 0.0.0.255
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
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 10.36.6.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.152.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 10.36.6.9 255.255.255.255
  #
  bgp 300
   peer 10.35.5.9 as-number 300
   peer 10.35.5.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 10.35.5.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.35.5.9 enable
  #
   ipv4-family vpn-instance vpna
    peer 10.2.1.1 as-number 65002
  #
  ospf 1
   area 0.0.0.0
    network 10.36.6.9 0.0.0.0
    network 10.152.1.0 0.0.0.255
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
   ip address 10.2.1.1 255.255.255.0
  #
  interface Loopback 1
   ip address 10.22.22.22 255.255.255.255
  #
  bgp 65002
   peer 10.2.1.2 as-number 300
   network 10.22.22.22 255.255.255.255
   #
   ipv4-family unicast
    undo synchronization
    peer 10.2.1.2 enable
  #
  return
  ```