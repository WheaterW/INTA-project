Example for Configuring BFD for Static VPN Routes
=================================================

In CE dual-homing networking, after a static route on a CE is bound to a BFD session, the static route can detect link faults or refresh itself based on the BFD session status. This implementation ensures quick VPN traffic convergence.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361690__en-us_task_0172369567_fig_dc_vrp_mpls-l3vpn-v4_cfg_012801), CE1 and CE2 belong to VPNA. Two default routes with the next hops as PE1 and PE2 respectively are configured on CE1. The two routes work in load-balancing mode. The static routes bound to VPNA are configured on PE1 and PE2 separately and are imported into BGP.

BFD sessions are established between PE1 and CE1, and between PE2 and CE1. BFD for VPN static route is configured on PE1 and PE2. In normal situations, the traffic from CE1 to the public network can be forwarded through PE1 and PE2 in load balancing mode. If the link between CE1 and PE1 or PE2 fails, CE1 detects the link fault by tracking BFD session status and updates the route. Then, CE1 switches traffic to the other link for transmission.

**Figure 1** Configuring BFD for VPN static route![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_012801.png "Click to enlarge")

#### Precautions

During the configuration process, note the following:

* VPN instances with different RDs need to be configured on the PEs to which a CE is dual-homed.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF for PEs on the MPLS backbone network to communicate.
2. Establish MPLS LSPs between PEs.
3. Configure VPN instances on PEs and bind each interface that connects a PE to a CE to a VPN instance.
4. Enable Multi-protocol Extensions for Interior Border Gateway Protocol (MP-IBGP) on PEs to exchange VPN routing information.
5. Configure two default routes with the next hops being PE1 and PE2 respectively on CE1 to implement load balancing of VPN data between PE1 and PE2.
6. Configure a static route bound to VPNA on PE1 and PE2 and import the static route into BGP.
7. Configure an MP-EBGP peer relationship between PE3 and CE2.
8. Configure static BFD sessions with automatically negotiated discriminators between PE1 and CE1, and between PE2 and CE1.
9. Configure BFD for VPN static route on PE1 and PE2.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs
* Names, RDs, and VPN targets of the VPN instances on the PEs
* Local and peer IP addresses of the BFD session

#### Procedure

1. Configure IGP on the MPLS backbone network to implement connectivity between the devices on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface loopback 1
   [*PE1-LoopBack1] ip address 2.2.2.2 32
   [*PE1-LoopBack1] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] ip address 11.11.11.1 24
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] ip address 33.33.33.1 24
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] ospf
   [*PE1-ospf-1] area 0
   [*PE1-ospf-1-area-0.0.0.0] network 11.11.11.0 0.0.0.255
   [*PE1-ospf-1-area-0.0.0.0] network 33.33.33.0 0.0.0.255
   [*PE1-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   [*PE1-ospf-1-area-0.0.0.0] commit
   [~PE1-ospf-1-area-0.0.0.0] quit
   [~PE1-ospf-1] quit
   ```
   
   Configure PE2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE2
   [*HUAWEI] commit
   [~PE2] interface loopback 1
   [*PE2-LoopBack1] ip address 3.3.3.3 32
   [*PE2-LoopBack1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] ip address 22.22.22.1 24
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface gigabitethernet 0/2/0 
   [*PE2-GigabitEthernet0/2/0] ip address 33.33.33.2 24
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2] ospf
   [*PE2-ospf-1] area 0
   [*PE2-ospf-1-area-0.0.0.0] network 22.22.22.0 0.0.0.255
   [*PE2-ospf-1-area-0.0.0.0] network 33.33.33.0 0.0.0.255
   [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   [*PE2-ospf-1-area-0.0.0.0] commit
   [~PE2-ospf-1-area-0.0.0.0] quit
   [~PE2-ospf-1] quit
   ```
   Configure PE3.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE3
   [*HUAWEI] commit
   [~PE3] interface loopback 1
   [*PE3-LoopBack1] ip address 4.4.4.4 32
   [*PE3-LoopBack1] quit
   [*PE3] interface gigabitethernet 0/1/0
   [*PE3-GigabitEthernet0/1/0] ip address 11.11.11.2 24
   [*PE3-GigabitEthernet0/1/0] quit
   [*PE3] interface gigabitethernet 0/2/0
   [*PE3-GigabitEthernet0/2/0] ip address 22.22.22.2 24
   [*PE3-GigabitEthernet0/2/0] quit
   [*PE3] ospf
   [*PE3-ospf-1] area 0
   [*PE3-ospf-1-area-0.0.0.0] network 11.11.11.0 0.0.0.255
   [*PE3-ospf-1-area-0.0.0.0] network 22.22.22.0 0.0.0.255
   [*PE3-ospf-1-area-0.0.0.0] network 4.4.4.4 0.0.0.0
   [*PE3-ospf-1-area-0.0.0.0] commit
   [~PE3-ospf-1-area-0.0.0.0] quit
   [~PE3-ospf-1] quit
   ```
   
   After the configurations are complete, OSPF neighbor relationships can be set up between PE1, PE2, and PE3. Run the **display ip routing-table** command. The command output shows that the PEs have learned the routes to each other's Loopback1 interface.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 14       Routes : 15
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
           2.2.2.2/32  Direct 0    0           D  127.0.0.1       LoopBack1
           3.3.3.3/32 OSPF   10   2           D  33.33.33.2      GigabitEthernet0/2/0
           4.4.4.4/32 OSPF   10   2           D  11.11.11.2      GigabitEthernet0/1/0
        11.11.11.0/24  Direct 0    0           D  11.11.11.1      GigabitEthernet0/1/0
        11.11.11.1/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/0
      11.11.11.255/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/0
        22.22.22.0/24  OSPF   10   2           D  11.11.11.2      GigabitEthernet0/1/0
                       OSPF   10   2           D  33.33.33.2      GigabitEthernet0/2/0
        33.33.33.0/24  Direct 0    0           D  33.33.33.1      GigabitEthernet0/2/0
        33.33.33.1/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/2/0
      33.33.33.255/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/2/0
         127.0.0.0/8   Direct 0    0           D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
2. Configure MPLS and MPLS LDP both globally and per interface on each node of the MPLS backbone network and establish LDP LSPs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 2.2.2.2
   [*PE1] mpls
   [*PE1-mpls] quit
   [*PE1] mpls ldp
   [*PE1-mpls-ldp] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] mpls
   [*PE1-GigabitEthernet0/1/0] mpls ldp
   [*PE1-GigabitEthernet0/1/0] commit
   [~PE1-GigabitEthernet0/1/0] quit
   [~PE1] interface gigabitethernet0/2/0
   [~PE1-GigabitEthernet0/2/0] mpls 
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   [*PE1-GigabitEthernet0/2/0] commit
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.3
   [*PE2] mpls
   [*PE2-mpls] quit
   [*PE2] mpls ldp
   [*PE2-mpls-ldp] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] mpls
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   [*PE2-GigabitEthernet0/1/0] commit
   [~PE2-GigabitEthernet0/1/0] quit
   [~PE2] interface gigabitethernet 0/2/0
   [~PE2-GigabitEthernet0/2/0] mpls
   [*PE2-GigabitEthernet0/2/0] mpls ldp
   [*PE2-GigabitEthernet0/2/00] commit
   [~PE2-GigabitEthernet0/2/0] quit
   ```
   
   Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 4.4.4.4
   [*PE3] mpls
   [*PE3-mpls] quit
   [*PE3] mpls ldp
   [*PE3-mpls-ldp] quit
   [*PE3] interface gigabitethernet 0/1/0
   [*PE3-GigabitEthernet0/1/0] mpls
   [*PE3-GigabitEthernet0/1/0] mpls ldp
   [*PE3-GigabitEthernet0/1/0] commit
   [~PE3-GigabitEthernet0/1/0] quit
   [~PE3] interface gigabitethernet 0/2/0
   [~PE3-GigabitEthernet0/2/0] mpls
   [*PE3-GigabitEthernet0/2/0] mpls ldp
   [*PE3-GigabitEthernet0/2/0] commit
   [~PE3-GigabitEthernet0/2/0] quit
   ```
   
   After the configurations are complete, LDP sessions can be set up between PEs. Run the **display mpls ldp session** command. The command output shows that the **Status** field is **Operational**.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display mpls ldp session
   
                  LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   
    ------------------------------------------------------------------------------
    Peer-ID            Status      LAM  SsnRole  SsnAge      KA-Sent/Rcv
    ------------------------------------------------------------------------------
    3.3.3.3:0          Operational DU   Passive  0000:02:22   572/572
    4.4.4.4:0          Operational DU   Passive  0000:02:21   566/566
    ------------------------------------------------------------------------------
    TOTAL: 2 session(s) Found.
   ```
3. Configure VPN instances on PEs and connect CEs to PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance VPNA
   [*PE1-vpn-instance-VPNA] ipv4-family
   [*PE1-vpn-instance-VPNA-af-ipv4] route-distinguisher 100:1
   [*PE1-vpn-instance-VPNA-af-ipv4] vpn-target 111:1 both
   [*PE1-vpn-instance-VPNA-af-ipv4] quit
   [*PE1-vpn-instance-VPNA] quit
   [*PE1] interface gigabitethernet 0/3/0
   [*PE1-GigabitEthernet0/3/0] ip binding vpn-instance VPNA
   [*PE1-GigabitEthernet0/3/0] ip address 10.1.1.2 24
   [*PE1-GigabitEthernet0/3/0] commit
   [~PE1-GigabitEthernet0/3/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance VPNA
   [*PE2-vpn-instance-VPNA] ipv4-family
   [*PE2-vpn-instance-VPNA-af-ipv4] route-distinguisher 100:2
   [*PE2-vpn-instance-VPNA-af-ipv4] vpn-target 111:1 both
   [*PE2-vpn-instance-VPNA-af-ipv4] quit
   [*PE2-vpn-instance-VPNA] quit
   [*PE2] interface gigabitethernet 0/3/0
   [*PE2-GigabitEthernet0/3/0] ip binding vpn-instance VPNA
   [*PE2-GigabitEthernet0/3/0] ip address 10.2.1.2 24
   [*PE2-GigabitEthernet0/3/0] commit
   [~PE2-GigabitEthernet0/3/0] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance VPNA
   [*PE3-vpn-instance-VPNA] ipv4-family
   [*PE3-vpn-instance-VPNA-af-ipv4] route-distinguisher 100:3
   [*PE3-vpn-instance-VPNA-af-ipv4] vpn-target 111:1 both
   [*PE3-vpn-instance-VPNA-af-ipv4] quit
   [*PE3-vpn-instance-VPNA] quit
   [*PE3] interface gigabitethernet 0/3/0
   [*PE3-GigabitEthernet0/3/0] ip binding vpn-instance VPNA
   [*PE3-GigabitEthernet0/3/0] ip address 10.3.1.1 24
   [*PE3-GigabitEthernet0/3/0] commit
   [~PE3-GigabitEthernet0/3/0] quit
   ```
   
   Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet 0/1/0
   [~CE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   [*CE1-GigabitEthernet0/1/0] commit
   [~CE1-GigabitEthernet0/1/0] quit 
   [~CE1] interface gigabitethernet 0/2/0
   [~CE1-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   [*CE1-GigabitEthernet0/2/0] commit
   [~CE1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface gigabitethernet 0/1/0
   [~CE2-GigabitEthernet0/1/0] ip address 10.3.1.2 24
   [*CE2-GigabitEthernet0/1/0] commit
   [~CE2-GigabitEthernet0/1/0] quit
   ```
   
   After the configurations are complete, run the **display ip vpn-instance verbose** command on each PE to check VPN instance configurations. Each PE can successfully ping its connected CE.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display ip vpn-instance verbose
    Total VPN-Instances configured : 1
    Total IPv4 VPN-Instances configured : 1 
    Total IPv6 VPN-Instances configured : 0
    VPN-Instance Name and ID : VPNA, 1
     Interfaces : GigabitEthernet0/3/0
    Address family ipv4
     Create date : 2008/09/21 12:18:46
     Up time : 0 days, 02 hours, 35 minutes and 58 seconds
     Vrf Status : UP
     Route Distinguisher : 100:1
     Export VPN Targets :  111:1
     Import VPN Targets :  111:1
     Label policy : label per instance
     The diffserv-mode Information is : uniform
     The ttl-mode Information is : pipe
   
   ```
   ```
   [~PE1] ping -vpn-instance VPNA 10.1.1.1
   PING 10.1.1.1: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.1: bytes=56 Sequence=1 ttl=255 time=130 ms
       Reply from 10.1.1.1: bytes=56 Sequence=2 ttl=255 time=60 ms
       Reply from 10.1.1.1: bytes=56 Sequence=3 ttl=255 time=40 ms
       Reply from 10.1.1.1: bytes=56 Sequence=4 ttl=255 time=30 ms
       Reply from 10.1.1.1: bytes=56 Sequence=5 ttl=255 time=30 ms
   
     --- 10.1.1.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
   round-trip min/avg/max = 30/58/130 ms
   
   ```
4. Import the VPN routes between PE1, PE2, and CE1.
   
   
   
   Configure two default routes with the next hops being PE1 and PE2 respectively on CE1 to implement load balancing between PE1 and PE2. Configure the static routes to be bound to the VPN instances on PE1 and PE2 and import the static routes into BGP.
   
   # Configure CE1.
   
   ```
   [~CE1] load-balance packet all
   [*CE1] ip route-static 0.0.0.0 0 10.1.1.2 
   [*CE1] ip route-static 0.0.0.0 0 10.2.1.2
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] ip route-static vpn-instance VPNA 1.1.1.1 32 10.1.1.1
   [*PE1] bgp 100
   [*PE1-bgp] ipv4-family vpn-instance VPNA
   [*PE1-bgp-VPNA] import-route direct
   [*PE1-bgp-VPNA] import-route static
   [*PE1-bgp-VPNA] commit
   [~PE1-bgp-VPNA] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip route-static vpn-instance VPNA 1.1.1.1 32 10.2.1.1
   [*PE2] bgp 100
   [*PE2-bgp] ipv4-family vpn-instance VPNA
   [*PE2-bgp-VPNA] import-route direct
   [*PE2-bgp-VPNA] import-route static
   [*PE2-bgp-VPNA] commit
   ```
5. Set up an EBGP peer relationship between PE3 and CE2, and import VPN routes into EBGP.
   
   
   
   # Configure CE2.
   
   ```
   [~CE2] bgp 65410
   [*CE2-bgp] peer 10.3.1.1 as-number 100
   [*CE2-bgp] import-route direct
   [*CE2-bgp] commit
   [~CE2-bgp] quit
   ```
   
   # Configure PE3. # Specify the number of routes for load balancing as 2 on PE3.
   
   ```
   [~PE3] bgp 100
   [*PE3-bgp] ipv4-family vpn-instance VPNA
   [*PE3-bgp-VPNA] peer 10.3.1.2 as-number 65410
   [*PE3-bgp-VPNA] import-route direct
   [*PE3-bgp-VPNA] maximum load-balancing 2
   [*PE3-bgp-VPNA] commit
   [~PE3-bgp-VPNA] quit
   ```
6. Establish an MP-IBGP peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] peer 3.3.3.3 as-number 100
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 1
   [*PE1-bgp] peer 4.4.4.4 as-number 100
   [*PE1-bgp] peer 4.4.4.4 connect-interface loopback 1
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 3.3.3.3 enable
   [*PE1-bgp-af-vpnv4] peer 4.4.4.4 enable
   [*PE1-bgp-af-vpnv4] commit
   [~PE1-bgp-af-vpnv4] quit
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [~PE2-bgp] peer 2.2.2.2 as-number 100
   [*PE2-bgp] peer 2.2.2.2 connect-interface loopback 1
   [*PE2-bgp] peer 4.4.4.4 as-number 100
   [*PE2-bgp] peer 4.4.4.4 connect-interface loopback 1
   [*PE2-bgp] ipv4-family vpnv4
   [*PE2-bgp-af-vpnv4] peer 2.2.2.2 enable
   [*PE2-bgp-af-vpnv4] peer 4.4.4.4 enable
   [*PE2-bgp-af-vpnv4] commit
   [~PE2-bgp-af-vpnv4] quit
   [~PE2-bgp] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   [~PE3-bgp] peer 2.2.2.2 as-number 100
   [*PE3-bgp] peer 2.2.2.2 connect-interface loopback 1
   [*PE3-bgp] peer 3.3.3.3 as-number 100
   [*PE3-bgp] peer 3.3.3.3 connect-interface loopback 1
   [*PE3-bgp] ipv4-family vpnv4
   [*PE3-bgp-af-vpnv4] peer 2.2.2.2 enable
   [*PE3-bgp-af-vpnv4] peer 3.3.3.3 enable
   [*PE3-bgp-af-vpnv4] commit
   [~PE3-bgp-af-vpnv4] quit
   [~PE3-bgp] quit
   ```
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command on the PEs to check whether a BGP peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   ```
   <PE1> display bgp vpnv4 all peer
   
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
   Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down  State PrefRcv
   
   4.4.4.4         4   100      205      202       0 03:05:25 Established       0
   3.3.3.3         4   100      197      254       0 03:06:54 Established       0  
   
   ```
7. Configure static BFD sessions with automatically negotiated discriminators.
   
   
   
   Set up BFD sessions between CE1 and PE1, and between CE1 and PE2.
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   [*PE1-bfd] quit
   [*PE1] bfd pe1_to_ce1 bind peer-ip 10.1.1.1 vpn-instance VPNA interface gigabitethernet 0/3/0 source-ip 10.1.1.2 auto
   [*PE1-bfd-session-pe1_to_ce1] commit
   [~PE1-bfd-session-pe1_to_ce1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   [*PE2-bfd] quit
   [*PE2] bfd pe2_to_ce1 bind peer-ip 10.2.1.1 vpn-instance VPNA interface gigabitethernet 0/3/0 source-ip 10.2.1.2 auto
   [*PE2-bfd-session-pe2_to_ce1] commit
   [~PE2-bfd-session-pe2_to_ce1] quit
   ```
   
   # Configure CE1.
   
   ```
   [~CE1] bfd
   [*CE1-bfd] quit
   [*CE1] bfd ce1_to_pe1 bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/0 source-ip 10.1.1.1 auto
   [*CE1-bfd-session-ce1_to_pe1] quit
   [*CE1] bfd ce1_to_pe2 bind peer-ip 10.2.1.2 interface gigabitethernet 0/2/0 source-ip 10.2.1.1 auto
   [*CE1-bfd-session-ce1_to_pe2] commit
   [~CE1-bfd-session-ce1_to_pe2] quit
   ```
   
   After completing the configurations, run the **display bfd session all verbose** command on each PE and CE. The command output shows that a one-hop auto-negotiation static BFD session has been established, and the session status is **Up**. The local and remote IDs of the BFD session are obtained through auto-negotiation. The following uses PE1 and CE1 as an example.
   
   # The following example uses the command output on PE1.
   
   ```
   <PE1> display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
     (One Hop) State : Up                      Name : pe1_to_ce1
   ------------------------------------------------------------------------------
     Local Discriminator    : 8192             Remote Discriminator   : ce1_to_pe1
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/3/0)
     Bind Session Type      : Static_Auto
     Bind Peer IP Address   : 10.1.1.1
     Bind Interface         : GigabitEthernet0/3/0
     Vpn Instance Name      : vpna
     Bind Source IP Address : 10.1.1.2
     FSM Board Id           : 3                TOS-EXP                : 6
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): -                Actual Rx Interval (ms): -
     Local Detect Multi     : 3                Detect Interval (ms)   : -
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 254  
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Enable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : AUTO
     Session TX TmrID       : -                Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Not Up Reason  : In negotiation 
     Session Description    : - 
     Track Group Name       : -
   ------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 1/0
   
   ```
   
   # The following example uses the command output on CE1.
   
   ```
   <CE1> display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
     (One Hop) State : Up                      Name : ce1_to_pe1
   --------------------------------------------------------------------------------
     Local Discriminator    : 8192             Remote Discriminator   : 8192
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static_Auto
     Bind Peer IP Address   : 10.1.1.2
     Bind Interface         : GigabitEthernet0/1/0
     FSM Board Id           : 3                TOS-EXP                : 6
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): -                Actual Rx Interval (ms): -
     Local Detect Multi     : 3                Detect Interval (ms)   : -
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Enable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : AUTO
     Session TX TmrID       : -                Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     PDT Index              : FSM-5020000 | RCV-0 | IF-5020000 | TOKEN-0
     Session Description    : -
     Track Group Name       : -
   --------------------------------------------------------------------------------
   --------------------------------------------------------------------------------
     (One Hop) State : Up                      Name : ce1_to_pe2                   
   --------------------------------------------------------------------------------
     Local Discriminator    : 8193             Remote Discriminator   : 8193
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/2/0)
     Bind Session Type      : Static_Auto
     Bind Peer IP Address   : 10.2.1.2
     Bind Interface         : GigabitEthernet0/2/0
     FSM Board Id           : 3                TOS-EXP                : 6
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): -                Actual Rx Interval (ms): -
     Local Detect Multi     : 3                Detect Interval (ms)   : -
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Enable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : AUTO
     Session TX TmrID       : -                Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     PDT Index              : FSM-5020000 | RCV-0 | IF-5020000 | TOKEN-0
     Session Description    : -
     Track Group Name       : -
   --------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 2/0
   ```
8. Configure BFD for VPN static route on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip route-static vpn-instance VPNA 1.1.1.1 255.255.255.255 10.1.1.1 track bfd-session pe1_to_ce1
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip route-static vpn-instance VPNA 1.1.1.1 255.255.255.255 10.2.1.1 track bfd-session pe2_to_ce1
   ```
   ```
   [*PE2] commit
   ```
9. Verify the configuration.
   
   
   
   # After completing the configurations, check the VPN routing table information on each PE. The command output shows that a static route exists in the routing table.
   
   ```
   <PE1> display ip routing-table vpn-instance VPNA
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: VPNA
            Destinations : 8        Routes : 8
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
           1.1.1.1/32 Static 60  0         RD 10.1.1.1       GigabitEthernet0/3/0
          10.1.1.0/24  Direct 0    0         D  10.1.1.2        GigabitEthernet0/3/0
          10.1.1.2/32  Direct 0    0         D  127.0.0.1       GigabitEthernet0/3/0
        10.1.1.255/32  Direct 0    0         D  127.0.0.1       GigabitEthernet0/3/0
          10.2.1.0/24  IBGP   255  0         RD 3.3.3.3         GigabitEthernet0/2/0
          10.3.1.0/24  IBGP   255  0         RD 4.4.4.4         GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0         D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0         D  127.0.0.1       InLoopBack0
   ```
   
   # On CE1, run the **tracert** command to ping the gateway through which the packets destined for CE2 pass. The command output shows that load balancing is implemented between PE1 and PE2 at the first hop.
   
   ```
   <CE1> tracert 10.3.1.2
    traceroute to  10.3.1.2(10.3.1.2), max hops: 30 ,packet length: 40
    1 10.1.1.2 20 ms 10.2.1.2 1 ms 10.1.1.2 40 ms
    2 10.3.1.1 40 ms  30 ms  50 ms
    3 10.3.1.2 80 ms  80 ms  60 ms
   
   ```
   
   # Check the routing table information on PE3. The command output shows that there are two routes with next hop addresses 3.3.3.3 and 2.2.2.2 to CE1 (1.1.1.1). The two BGP routes are used to load-balance traffic.
   
   ```
   <PE3> display ip routing-table vpn-instance VPNA
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: VPNA
            Destinations : 7        Routes : 8
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
           1.1.1.1/32  IBGP   255  0          RD  3.3.3.3         GigabitEthernet0/2/0
                       IBGP   255  0          RD  2.2.2.2         GigabitEthernet0/1/0
          10.1.1.0/24  IBGP   255  0          RD  2.2.2.2         GigabitEthernet0/1/0
          10.2.1.0/24  IBGP   255  0          RD  3.3.3.3         GigabitEthernet0/2/0
          10.3.1.0/24  Direct 0    0           D  10.3.1.1        GigabitEthernet0/3/0
          10.3.1.1/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/3/0
        10.3.1.255/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/3/0
   255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   
   # Run the **tracert** command on CE2 to check the traffic destined for CE1. The command output shows that load balancing is performed when the traffic leaves PE3.
   
   ```
   [~CE2] tracert 1.1.1.1
    traceroute to  1.1.1.1(1.1.1.1), max hops: 30 ,packet length: 40
    1 10.3.1.1 9 ms  2 ms  2 ms
    2 10.2.1.2 < AS=100 > 6 ms  5 ms  2 ms
    3 10.2.1.1 < AS=100 > 6 ms  6 ms  5 ms
   
   ```
   
   # Run the **shutdown** command on GE0/1/0 of CE1 to simulate a link fault.
   
   ```
   [~CE1-GigabitEthernet0/1/0] shutdown
   ```
   
   # Check the BFD session status on PE1. The command output shows that the BFD session status is **Down**.
   
   ```
   <PE1> display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
     (One Hop) State : Down                   Name : pe1_to_ce1
   ------------------------------------------------------------------------------
     Local Discriminator    : 8192             Remote Discriminator   : 8192
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/3/0)
     Bind Session Type      : Static_Auto
     Bind Peer IP Address   : 10.1.1.1
     Bind Interface         : GigabitEthernet0/3/0
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): -                Actual Rx Interval (ms): -
     Local Detect Multi     : 3                Detect Interval (ms)   : -
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255  
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Enable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : AUTO
     Session TX TmrID       : -                Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Not Up Reason  : In negotiation 
     Session Description    : - 
     Track Group Name       : -
   ------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 1/0
   ```
   
   # Check the VPN routing table on PE1. The command output shows that the next hop of the route destined for CE1 is only PE2.
   
   ```
   <PE1> display ip routing-table vpn-instance VPNA
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: VPNA
            Destinations : 4        Routes : 4
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
       1.1.1.1/32  EBGP   255  0           RD  3.3.3.3         GigabitEthernet0/2/0
          10.2.1.0/24  IBGP   255  0          RD  3.3.3.3         GigabitEthernet0/2/0
          10.3.1.0/24  IBGP   255  0          RD  4.4.4.4         GigabitEthernet0/1/0
   255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   
   # On CE1, check the gateway through which the packets destined for CE2 pass. The command output shows that load balancing is not carried out between PE1 and PE2 at the first hop, and the traffic flows only through PE2.
   
   ```
   <CE3> tracert 10.3.1.2
    traceroute to  10.3.1.2(10.3.1.2), max hops: 30 ,packet length: 40
    1 10.2.1.2 50 ms  30 ms  10 ms
    2 10.3.1.1 110 ms  70 ms  90 ms
    3 10.3.1.2 60 ms  70 ms  80 ms
   
   ```
   
   # Check the routing table on PE3. The command output shows that there is only one route to CE1 (1.1.1.1), with the next hop being PE2 (3.3.3.3).
   
   ```
   <PE3> display ip routing-table vpn-instance VPNA
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: VPNA
            Destinations : 6        Routes : 6
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
           1.1.1.1/32  IBGP   255  0          RD  3.3.3.3         GigabitEthernet0/2/0
          10.2.1.0/24  IBGP   255  0          RD  3.3.3.3         GigabitEthernet0/2/0
          10.3.1.0/24  Direct 0    0           D  10.3.1.1        GigabitEthernet0/3/0
          10.3.1.1/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/3/0
        10.3.1.255/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/3/0
   255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   
   # Check traffic from CE2 to CE1. The command output shows that traffic going out of PE3 is sent through GE0/2/0 (10.2.1.2).
   
   ```
   [~CE2] tracert 1.1.1.1
    traceroute to  1.1.1.1(1.1.1.1), max hops: 30 ,packet length: 40
    1 10.3.1.1 9 ms  2 ms  2 ms
    2 10.2.1.2 < AS=100 > 6 ms  5 ms  5 ms
    3 10.2.1.1 < AS=100 > 6 ms  5 ms  5 ms
   
   ```
   
   Use a tester to generate traffic and forward the traffic in load-balancing mode. After a link between CE1 and PE1 or a link between CE1 and PE2 fails, you can find that the traffic is switched in less than 50 ms.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  bfd
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 11.11.11.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 33.33.33.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 10.1.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
    import-route static
  #
  ospf 1
   area 0.0.0.0
    network 11.11.11.0 0.0.0.255
    network 33.33.33.0 0.0.0.255
    network 2.2.2.2 0.0.0.0
  #
  ip route-static vpn-instance VPNA 1.1.1.1 255.255.255.255 10.1.1.1 track bfd-session pe1_to_ce1
  #
  bfd pe1_to_ce1 bind peer-ip 10.1.1.1 vpn-instance VPNA interface GigabitEthernet0/3/0 source-ip 10.1.1.2 auto
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  bfd
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 22.22.22.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 33.33.33.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
    import-route static
  #
  ospf 1
   area 0.0.0.0
    network 33.33.33.0 0.0.0.255
    network 22.22.22.0 0.0.0.255
    network 3.3.3.3 0.0.0.0
  #
  ip route-static vpn-instance VPNA 1.1.1.1 255.255.255.255 10.2.1.1 track bfd-session pe2_to_ce1
  #
  bfd pe2_to_ce1 bind peer-ip 10.2.1.1 vpn-instance VPNA interface GigabitEthernet0/3/0 source-ip 10.2.1.2 auto
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 100:3
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 11.11.11.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 22.22.22.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 10.3.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance VPNA
    peer 10.3.1.2 as-number 65410
    import-route direct
    maximum load-balancing 2
  #
  ospf 1
   area 0.0.0.0
    network 11.11.11.0 0.0.0.255
    network 22.22.22.0 0.0.0.255
    network 4.4.4.4 0.0.0.0
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  load-balance packet all
  #
  ip route-static 0.0.0.0 0.0.0.0 10.1.1.2
  ip route-static 0.0.0.0 0.0.0.0 10.2.1.2
  #
  bfd ce1_to_pe1 bind peer-ip 10.1.1.2 interface GigabitEthernet0/1/0 source-ip 10.1.1.1 auto
  #
  bfd ce1_to_pe2 bind peer-ip 10.2.1.2 interface GigabitEthernet0/2/0 source-ip 10.2.1.1 auto
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
   ip address 10.3.1.2 255.255.255.0
  #
  bgp 65410
   peer 10.3.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.3.1.1 enable
  #
  return
  ```