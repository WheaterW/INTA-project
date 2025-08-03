Example for Configuring the MPLS DiffServ Mode
==============================================

Example_for_Configuring_the_MPLS_DiffServ_Mode

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371593__fig_dc_ne_qos_cfg_200601), CE1 and CE3 belong to VPN-A, and CE2 and CE4 belong to VPN-B. The VPN-target attribute used by VPN-A is 111:1, and that used by VPN-B is 222:2. Users in different VPNs cannot communicate with each other. It is required to set the MPLS DiffServ mode to Pipe on PE1 and PE2 so that data services in the VPN are forwarded based on the priority configured by the carrier on the MPLS network, and the P node also needs to schedule the data services based on the priority.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


**Figure 1** Networking diagram of the MPLS DiffServ mode  
![](images/fig_dc_ne_qos_cfg_200601.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure Open Shortest Path First (OSPF) on the backbone network to implement interworking between PEs.
2. Configure basic MPLS functions and MPLS LDP, and establish MPLS LSP.
3. Configure MP-IBGP between PEs to exchange VPN routing information.
4. Configure VPN instances on PEs and bind each interface that connects a PE to a CE to a VPN instance.
5. Configure EBGP between CEs and PEs to exchange VPN routing information.
6. Enable the Pipe mode on VPN-A and VPN-B, and apply different DiffServ domains to different VPN instances.
7. Configure BA classification on the P node.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs and P
* Route distinguishers (RDs) of VPN-A and VPN-B
* VPN targets of the routes sent and received by VPN-A and VPN-B
* Different DiffServ domains configured on PE1 and PE2

#### Procedure

1. Configure an IGP on the MPLS backbone network so that PEs on the backbone network can communicate with the P.
   
   
   
   # Configure PE1.
   
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
   [~PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*PE1-LoopBack1] commit
   ```
   ```
   [~PE1-LoopBack1] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/3/0
   ```
   ```
   [~PE1-GigabitEthernet0/3/0] ip address 172.21.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [~PE1] ospf
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 172.21.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.9 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE1-ospf-1] quit
   ```
   
   # Configure the P.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*P-LoopBack1] commit
   ```
   ```
   [~P-LoopBack1] quit
   ```
   ```
   [~P] interface gigabitethernet 0/1/0
   ```
   ```
   [~P-GigabitEthernet0/1/0] ip address 172.21.1.2 24
   ```
   ```
   [*P-GigabitEthernet0/1/0] commit
   ```
   ```
   [~P-GigabitEthernet0/1/0] quit
   ```
   ```
   [~P] interface gigabitethernet 0/2/0
   ```
   ```
   [~P-GigabitEthernet0/2/0] ip address 172.22.1.1 24
   ```
   ```
   [*P-GigabitEthernet0/2/0] commit
   ```
   ```
   [~P-GigabitEthernet0/2/0] quit
   ```
   ```
   [~P] ospf
   ```
   ```
   [*P-ospf-1] area 0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 172.21.1.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 172.22.1.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~P-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~P-ospf-1] quit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] ip address 3.3.3.9 32
   ```
   ```
   [*PE2-LoopBack1] commit
   ```
   ```
   [~PE2-LoopBack1] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/3/0
   ```
   ```
   [~PE2-GigabitEthernet0/3/0] ip address 172.22.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [~PE2] ospf
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 172.22.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.9 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE2-ospf-1] quit
   ```
   
   After the configuration is complete, OSPF neighbor relationship is set up between PE1, the P, and PE2. Run the **display ospf peer** command. The command output shows that the neighbor status is **Full**. Run the **display ip routing-table** command. The command output shows that the PEs have learned the Loopback1 route of each other.
   
   The command output on PE1 is used as an example.
   
   ```
   [~PE1] display ospf peer
   (M) Indicates MADJ neighbor
             OSPF Process 1 with Router ID 1.1.1.9
                     Neighbors
    Area 0.0.0.0 interface 172.21.1.1(GigabitEthernet0/3/0)'s neighbors
    Router ID: 2.2.2.9           Address: 172.21.1.2
      State: Full       Mode:Nbr is  Master    Priority: 1
      DR: 172.21.1.1     BDR: 172.21.1.2       MTU: 0
      Dead timer due in 38  sec
      Retrans timer interval: 5
      Neighbor is up for 00h02m45s
      Neighbor Up Time : 2020-08-15 01:41:57
      Authentication Sequence: [ 0 ] 
   
   [~PE1] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 8       Routes : 8
   
   Destination/Mask  Proto  Pre  Cost             Flags NextHop         Interface
         1.1.1.9/32  Direct 0    0                D  127.0.0.1          LoopBack1
         2.2.2.9/32  OSPF   10   1                D  172.21.1.2         GigabitEthernet0/3/0
         3.3.3.9/32  OSPF   10   2                D  172.21.1.2         GigabitEthernet0/3/0
       127.0.0.0/8   Direct 0    0                D  127.0.0.1          InLoopBack0
       127.0.0.1/32  Direct 0    0                D  127.0.0.1          InLoopBack0
      172.21.1.0/24  Direct 0    0                D  172.21.1.1         GigabitEthernet0/3/0
      172.21.1.1/32  Direct 0    0                D  127.0.0.1          InLoopBack0
      172.22.1.0/24  OSPF   10   2                D  172.21.1.2         GigabitEthernet0/3/0
   ```
2. Configure basic MPLS functions, enable MPLS LDP, and establish LDP LSPs on the MPLS backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] commit
   ```
   ```
   [~PE1-mpls] quit
   ```
   ```
   [~PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] commit
   ```
   ```
   [~PE1-mpls-ldp] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/3/0
   ```
   ```
   [~PE1-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/3/0] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] mpls lsr-id 2.2.2.9
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls] commit
   ```
   ```
   [~P-mpls] quit
   ```
   ```
   [~P] mpls ldp
   ```
   ```
   [*P-mpls-ldp] commit
   ```
   ```
   [~P-mpls-ldp] quit
   ```
   ```
   [~P] interface gigabitethernet 0/1/0
   ```
   ```
   [~P-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/1/0] commit
   ```
   ```
   [~P-GigabitEthernet0/1/0] quit
   ```
   ```
   [~P] interface gigabitethernet 0/2/0
   ```
   ```
   [~P-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/2/0] commit
   ```
   ```
   [~P-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.9
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] commit
   ```
   ```
   [~PE2-mpls] quit
   ```
   ```
   [~PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] commit
   ```
   ```
   [~PE2-mpls-ldp] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/3/0
   ```
   ```
   [~PE2-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/3/0] quit
   ```
   
   After the configurations are complete, LDP sessions are set up between PE1 and the P and between PE2 and the P. Run the **display mpls ldp session** command. The command output shows that the LDP session status is **Operational**. Run the **display mpls ldp lsp** command. The command output shows LDP establishment.
   
   The command output on PE1 is used as an example.
   
   ```
   [~PE1] display mpls ldp session
   
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    -------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
    -------------------------------------------------------------------------
    2.2.2.9:0          Operational DU  Passive  0000:00:01  5/5
    -------------------------------------------------------------------------
    TOTAL: 1 Session(s) Found.
   
   [~PE1] display mpls ldp lsp
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel   UpstreamPeer   NextHop         OutInterface
    -------------------------------------------------------------------------------
    1.1.1.9/32         3/NULL        2.2.2.9        127.0.0.1       Loopback1 
   *1.1.1.9/32         Liberal/48061                DS/2.2.2.9
    2.2.2.9/32         NULL/3        -              172.21.1.2      GigabitEthernet0/3/0
    2.2.2.9/32        48061/3        2.2.2.9        172.21.1.2      GigabitEthernet0/3/0
    3.3.3.9/32         NULL/48062    -              172.21.1.2      GigabitEthernet0/3/0
    3.3.3.9/32       48062/48062     2.2.2.9        172.21.1.2      GigabitEthernet0/3/0
    -------------------------------------------------------------------------------
    TOTAL: 5 Normal LSP(s) Found.
    TOTAL: 1 Liberal LSP(s) Found.
    TOTAL: 0 FRR LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   ```
3. Set up an MP-IBGP peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.9 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.9 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 3.3.3.9 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
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
   [*PE2-bgp] peer 1.1.1.9 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 1.1.1.9 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
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
   
   After the configurations are complete, run the **display bgp peer** or **display bgp vpnv4 all peer** command on the PEs. The command outputs show that the BGP peer relationship have been established between the PEs and are in the **Established** state.
   
   ```
   [~PE1] display bgp vpnv4 all peer
   ```
   ```
   BGP local router ID : 1.1.1.9
   ```
   ```
    Local AS number : 100
   ```
   ```
    Total number of peers : 1                 Peers in established state : 1
   ```
   ```
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
   ```
   ```
     3.3.3.9         4   100   12      18         0     00:09:38   Established  0
   ```
4. Configure a VPN instance on each PE for the access of the corresponding CE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE1-vpn-instance-vpna] quit
   ```
   ```
   [~PE1] ip vpn-instance vpnb
   ```
   ```
   [*PE1-vpn-instance-vpnb] route-distinguisher 100:2
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 both
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] commit
   ```
   ```
   [~PE1-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [~PE1-vpn-instance-vpnb] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpnb
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.2.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE2-vpn-instance-vpna] quit
   ```
   ```
   [~PE2] ip vpn-instance vpnb
   ```
   ```
   [*PE2-vpn-instance-vpnb] route-distinguisher 200:2
   ```
   ```
   [*PE2-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 both
   ```
   ```
   [*PE2-vpn-instance-vpnb-af-ipv4] commit
   ```
   ```
   [~PE2-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [~PE2-vpn-instance-vpnb] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.3.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [~PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpnb
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.4.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/0] quit
   ```
   
   # Assign interface IP addresses to each CE according to [Figure 1](#EN-US_TASK_0172371593__fig_dc_ne_qos_cfg_200601). The configuration procedure is not described here.
   
   After the configurations are complete, run the **display ip vpn-instance verbose** command on the PEs to view the configurations of VPN instances. Each PE can ping its connected CE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a PE has multiple interfaces bound to the same VPN instance, specify a source IP address using the **-a** *source-ip-address* parameter in the **ping -vpn-instance** *vpn-instance-name* **-a** *source-ip-address dest-ip-address* command to ping the CE that is connected to the remote PE. If the source IP address is not specified, the ping operation fails.
   
   PE1 and CE1 are used as examples.
   
   ```
   [~PE1] display ip vpn-instance verbose
     Total VPN-Instances configured : 2
     Total IPv4 VPN-Instances configured : 2
     Total IPv6 VPN-Instances configured : 0
   
     VPN-Instance Name and ID : vpna, 4
     Interfaces : GigabitEthernet0/1/0 
   Address family ipv4
     Create date : 2020/09/21 11:30:35
     Up time : 0 days, 00 hours, 05 minutes and 19 seconds
     Vrf Status : UP
     Route Distinguisher : 100:1
     Export VPN Targets :  111:1
     Import VPN Targets :  111:1
     Label Policy : label per route
     The diffserv-mode Information is : uniform
     The ttl-mode Information is : pipe
     Log Interval : 5
     Interfaces : GigabitEthernet0/1/0
   
     VPN-Instance Name and ID : vpnb, 5
     Interfaces : GigabitEthernet0/2/0 
   Address family ipv4
     Create date : 2020/09/21 11:31:18
     Up time : 0 days, 00 hours, 04 minutes and 36 seconds
     Vrf Status : UP
     Route Distinguisher : 100:2
     Export VPN Targets :  222:2
     Import VPN Targets :  222:2
     Label Policy : label per route
     The diffserv-mode Information is : uniform
     The ttl-mode Information is : pipe
     Log Interval : 5
     Interfaces : GigabitEthernet0/2/0
   
   [~PE1] ping -vpn-instance vpna 10.1.1.1
     PING 10.1.1.1: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.1: bytes=56 Sequence=1 ttl=255 time=56 ms
       Reply from 10.1.1.1: bytes=56 Sequence=2 ttl=255 time=4 ms
       Reply from 10.1.1.1: bytes=56 Sequence=3 ttl=255 time=4 ms
       Reply from 10.1.1.1: bytes=56 Sequence=4 ttl=255 time=52 ms
       Reply from 10.1.1.1: bytes=56 Sequence=5 ttl=255 time=3 ms
   
     --- 10.1.1.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 3/23/56 ms
   ```
5. Establish EBGP peer relationships between the PEs and CEs and import VPN routes.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] peer 10.1.1.2 as-number 100
   ```
   ```
   [*CE1-bgp] import-route direct
   ```
   ```
   [*CE1-bgp] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations of CE2, CE3, and CE4 are similar to that of CE1, and the configuration procedure is not described here.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] peer 10.1.1.1 as-number 65410
   ```
   ```
   [*PE1-bgp-vpna] import-route direct
   ```
   ```
   [*PE1-bgp-vpna] commit
   ```
   ```
   [~PE1-bgp-vpna] quit
   ```
   ```
   [~PE1-bgp] ipv4-family vpn-instance vpnb
   ```
   ```
   [*PE1-bgp-vpnb] peer 10.2.1.1 as-number 65420
   ```
   ```
   [*PE1-bgp-vpnb] import-route direct
   ```
   ```
   [*PE1-bgp-vpnb] commit
   ```
   ```
   [~PE1-bgp-vpnb] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of PE2 is similar to that of PE1, and the configuration procedure is not described here.
   
   After the configurations are complete, run the **display bgp vpnv4 vpn-instance peer** command on the PEs. The command outputs show that BGP peer relationships have been established between the PEs and CEs and are in the **Established** state.
   
   The peer relationship between PE1 and CE1 is used as an example.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpna peer
   
    BGP local router ID : 1.1.1.9
    Local AS number : 100
    VPN-Instance vpna, Router ID 1.1.1.9:
    Total number of peers : 1            Peers in established state : 1
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     10.1.1.1        4   65410  11     9          0     00:06:37   Established 1
   ```
6. Verify the configuration.
   
   
   
   Run the **display ip routing-table vpn-instance** command on the PEs to view the routes to peer CEs.
   
   The command output on PE1 is used as an example.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpna
   Route Flags: R - relay, D - download to fib
   ------------------------------------------------------------------------------
   Routing Table: vpna
            Destinations : 3        Routes : 3
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
        10.1.1.0/24    Direct 0    0        D     10.1.1.2        GigabitEthernet0/1/0
        10.1.1.2/32    Direct 0    0        D     127.0.0.1       GigabitEthernet0/1/0
        10.3.1.0/24   IBGP   255  0        RD    3.3.3.9         GigabitEthernet0/3/0
   [~PE1] display ip routing-table vpn-instance vpnb
   Route Flags: R - relay, D - download to fib
   ------------------------------------------------------------------------------
   Routing Table: vpnb
            Destinations : 3        Routes : 3
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
        10.2.1.0/24    Direct 0    0        D     10.2.1.2        GigabitEthernet0/2/0
        10.2.1.2/32    Direct 0    0        D     127.0.0.1       GigabitEthernet0/2/0
        10.4.1.0/24   IBGP   255  0        RD    3.3.3.9         GigabitEthernet0/3/0
   ```
   
   CEs in the same VPN can ping each other, but CEs in different VPNs cannot.
   
   For example, CE1 can ping CE3 (10.3.1.1/24) but cannot ping CE4 (10.4.1.1/24).
   
   ```
   [~CE1] ping 10.3.1.1
   ```
   ```
     PING 10.3.1.1: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.3.1.1: bytes=56 Sequence=1 ttl=253 time=72 ms
   ```
   ```
       Reply from 10.3.1.1: bytes=56 Sequence=2 ttl=253 time=34 ms
   ```
   ```
       Reply from 10.3.1.1: bytes=56 Sequence=3 ttl=253 time=50 ms
   ```
   ```
       Reply from 10.3.1.1: bytes=56 Sequence=4 ttl=253 time=50 ms
   ```
   ```
       Reply from 10.3.1.1: bytes=56 Sequence=5 ttl=253 time=34 ms
   ```
   ```
     --- 10.3.1.1 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 34/48/72 ms  
   ```
   ```
   [~CE1] ping 10.4.1.1
   ```
   ```
     PING 10.4.1.1: 56  data bytes, press CTRL_C to break
   ```
   ```
       Request time out
   ```
   ```
       Request time out
   ```
   ```
       Request time out
   ```
   ```
       Request time out
   ```
   ```
       Request time out
   ```
   ```
     --- 10.4.1.1 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       0 packet(s) received
   ```
   ```
       100.00% packet loss
   ```
7. Configure the DiffServ mode on PE1 and PE2, and apply DiffServ domains to different VPN instances.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] diffserv-mode pipe af1 green
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE1-vpn-instance-vpna] quit
   ```
   ```
   [~PE1] ip vpn-instance vpnb
   ```
   ```
   [*PE1-vpn-instance-vpnb]ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] diffserv-mode pipe be yellow
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] commit
   ```
   ```
   [~PE1-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [~PE1-vpn-instance-vpnb] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] diffserv-mode pipe af1 green
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE2-vpn-instance-vpna] quit
   ```
   ```
   [~PE2] ip vpn-instance vpnb
   ```
   ```
   [*PE2-vpn-instance-vpnb] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpnb-af-ipv4] diffserv-mode pipe be yellow
   ```
   ```
   [*PE2-vpn-instance-vpnb-af-ipv4] commit
   ```
   ```
   [~PE2-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [~PE2-vpn-instance-vpnb] quit
   ```
8. Configure BA classification on the P node.
   
   
   
   # Configure the P.
   
   ```
   [~P] interface gigabitethernet 0/1/0
   [~P-GigabitEthernet0/1/0] trust upstream default
   [*P-GigabitEthernet0/1/0] quit
   [*P] interface gigabitethernet 0/2/0
   [*P-GigabitEthernet0/2/0] trust upstream default
   [*P-GigabitEthernet0/2/0] quit
   [*P] commit
   ```
9. Verify the configuration.
   
   
   
   Run the **display ip vpn-instance verbose vpna** command on a PE to view the DiffServ mode configured for the VPN instance.
   
   The command output on PE1 is used as an example.
   
   ```
   [~PE1] display ip vpn-instance verbose vpna
   ```
   ```
   VPN-Instance Name and ID : vpna, 23
   Address family ipv4
     Create date : 2020/09/21 11:08:12
     Up time : 0 days, 00 hours, 06 minutes and 32 seconds
     Vrf Status : UP
     Label Policy : label per route
     The diffserv-mode Information is : pipe af1 green
     The ttl-mode Information is : pipe
     Log Interval : 5
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
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
    diffserv-mode pipe af1 green
  #
  ip vpn-instance vpnb
    ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
    diffserv-mode pipe be yellow
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpnb
   ip address 10.2.1.2 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.21.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  bgp 100
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.9 enable
  #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.9 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    peer 10.1.1.1 as-number 65410
  #
   ipv4-family vpn-instance vpnb
    import-route direct
    peer 10.2.1.1 as-number 65420
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 172.21.1.0 0.0.0.255
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.21.1.2 255.255.255.0
   mpls
   mpls ldp
   trust upstream default
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 172.22.1.1 255.255.255.0
   mpls
   mpls ldp
   trust upstream default
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 172.21.1.0 0.0.0.255
    network 172.22.1.0 0.0.0.255
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
    diffserv-mode pipe af1 green
  #
  ip vpn-instance vpnb
    ipv4-family
    route-distinguisher 200:2
    apply-label per-instance
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
    diffserv-mode pipe be yellow
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.3.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpnb
   ip address 10.4.1.2 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.22.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
  #
  bgp 100
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.9 enable
   #
   ipv4-family vpn-instance vpna
    peer 10.3.1.1 as-number 65430
    import-route direct
   #
   ipv4-family vpn-instance vpnb
    peer 10.4.1.1 as-number 65440
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 172.22.1.0 0.0.0.255
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
   ip address 10.1.1.1 255.255.255.0
  #
  bgp 65410
   peer 10.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.1.1.2 enable
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
  bgp 65420
   peer 10.2.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.2.1.2 enable
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
  #
  bgp 65430
   peer 10.3.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.3.1.2 enable
  #
  return
  ```
* CE4 configuration file
  
  ```
  #
  sysname CE4
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
  #
  bgp 65440
   peer 10.4.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.4.1.2 enable
  #
  return
  ```