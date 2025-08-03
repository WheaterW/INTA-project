Example for Configuring an Inter-area NG MVPN
=============================================

The backbone network belongs to an AS. PEs and ABRs advertise labeled routes through MP-IBGP.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001270193565__fig_dc_vrp_cfg_ngmvpn_010301), CE1 and CE2 belong to AS65003 and AS65004, respectively. The CEs communicate across AS100. An MP-IBGP peer relationship needs to be established between each PE and the ABR.

**Figure 1** Configuring an inter-area NG MVPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

IF1 and IF2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0000001225833736.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| CE1 | GE0/1/0 | 10.0.6.6/24 |
| GE0/1/1 | 10.0.5.6/24 |
| PE1 | Loopback 0 | 1.1.1.1/32 |
| GE0/1/0 | 10.0.2.3/24 |
| GE0/1/1 | 10.0.6.3/24 |
| ABR | Loopback 0 | 2.2.2.2/32 |
| GE0/1/0 | 10.0.2.5/24 |
| GE0/1/1 | 10.0.16.1/24 |
| PE2 | Loopback 0 | 3.3.3.3/32 |
| GE0/1/0 | 10.0.14.4/24 |
| GE0/1/1 | 10.0.16.2/24 |
| CE2 | GE0/1/0 | 10.0.14.1/24 |
| GE0/1/1 | 10.0.3.1/24 |



#### Precautions

When you configure an inter-area NG MVPN, note the following:

* An MP-IBGP peer relationship needs to be established between each PE and the ABR.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP in each AS for interworking among devices in the same AS; set up an MPLS LDP LSP between the ABR and PE in the same AS.
2. Configure the automatic mLDP P2MP tunnel function on the PEs and ABR.
3. Configure BGP and establish MP-IBGP peer relationships between the PEs and ABR in the same AS.
4. Configure a VPN instance on each PE.
5. Configure multicast traffic transmission over P2MP tunnels.
6. Configure PIM.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs on PE1, ABR, and PE2: 1.1.1.1, 2.2.2.2, and 3.3.3.3

#### Procedure

1. On the MPLS backbone network in the AS, configure an IGP to interconnect the PEs and ABR.
   
   
   
   In this example, OSPF and IS-IS are used as IGPs. For configuration details, see Configuration Files in this section.
   
   After the configuration is complete, OSPF or IS-IS neighbor relationships are established between nodes.
2. Configure basic MPLS functions, enable MPLS LDP, and establish LDP LSPs on the MPLS backbone network in the AS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
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
   [*PE1] interface GigabitEthernet 0/1/0
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
   
   The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
   
   # Configure the ABR.
   
   ```
   [~ABR] mpls lsr-id 2.2.2.2
   ```
   ```
   [*ABR] mpls
   ```
   ```
   [*ABR-mpls] quit
   ```
   ```
   [*ABR] mpls ldp
   ```
   ```
   [*ABR-mpls-ldp] quit
   ```
   ```
   [*ABR] interface GigabitEthernet 0/1/0
   ```
   ```
   [*ABR-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ABR-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*ABR-GigabitEthernet0/1/0] commit
   ```
   ```
   [~ABR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ABR] interface GigabitEthernet0/1/1
   ```
   ```
   [*ABR-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*ABR-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*ABR-GigabitEthernet0/1/1] commit
   ```
   ```
   [~ABR-GigabitEthernet0/1/1] quit
   ```
   
   After the configuration is complete, an LDP peer relationship is set up between each PE and the ABR. Run the **display mpls ldp session** command on each Router. The command output shows that **Status** is **Operational**. The command output on PE1 is used as an example.
   
   ```
   <PE1> display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   
   ```
   ```
    -------------------------------------------------------------------------
   ```
   ```
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
   ```
   ```
    -------------------------------------------------------------------------
   ```
   ```
    2.2.2.2          Operational DU   Passive  0000:00:01  5/5
   ```
   ```
    -------------------------------------------------------------------------
   ```
   ```
    TOTAL: 1 session(s) Found.
   ```
3. Configure the automatic mLDP P2MP tunnel function on the PEs and ABR.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp
   ```
   ```
   [~PE1-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE1-mpls-ldp] commit
   ```
   ```
   [~PE1-mpls-ldp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls ldp
   ```
   ```
   [~PE2-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE2-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*PE2-mpls-ldp] commit
   ```
   ```
   [~PE2-mpls-ldp] quit
   ```
   
   # Configure the ABR.
   
   ```
   [~ABR] mpls ldp
   ```
   ```
   [~ABR-mpls-ldp] mldp p2mp
   ```
   ```
   [*ABR-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*ABR-mpls-ldp] commit
   ```
   ```
   [~ABR-mpls-ldp] quit
   ```
4. Configure BGP and establish MP-IBGP peer relationships between the PEs and ABR in the same AS.
   
   
   
   # On CE1, configure BGP.
   
   ```
   [~CE1] bgp 65503
   ```
   ```
   [*CE1-bgp] peer 10.0.6.3 as-number 100
   ```
   
   The configuration of CE2 is similar to that of CE1. For configuration details, see Configuration Files in this section.
   
   # Configure PE1 to establish an MP-IBGP peer relationship with the ABR.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 connect-interface loopback 0
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*PE1-bgp-af-ipv4] network 1.1.1.1 32
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] commit
   ```
   ```
   [~PE1-bgp-af-ipv4] quit
   ```
   ```
   [~PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2.2.2.2 enable
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
   
   The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
   
   # Configure the ABR to establish an MP-IBGP peer relationship with the corresponding PE.
   
   ```
   [~ABR] bgp 100
   ```
   ```
   [*ABR-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*ABR-bgp] peer 1.1.1.1 connect-interface loopback 0
   ```
   ```
   [*ABR-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*ABR-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*ABR-bgp] ipv4-family unicast
   ```
   ```
   [*ABR-bgp-af-mvpn] undo synchronization
   ```
   ```
   [*ABR-bgp-af-mvpn] peer 1.1.1.1 enable
   ```
   ```
   [*ABR-bgp-af-mvpn] peer 3.3.3.3 enable
   ```
   ```
   [*ABR-bgp-af-mvpn] quit
   ```
   ```
   [*ABR-bgp] ipv4-family vpnv4
   ```
   ```
   [*ABR-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*ABR-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*ABR-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*ABR-bgp-af-vpnv4] quit
   ```
   ```
   [*ABR-bgp] commit
   ```
   ```
   [~ABR-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 all peer** command on each PE or the ABR. The command output shows that an MP-IBGP peer relationship has been established between the PE and ABR and between the ABRs. The following example uses the command output on PE1.
   
   ```
   <PE1> display bgp vpnv4 all peer
   
    BGP local router ID : 1.1.1.9
    Local AS number : 100
    Total number of peers : 1         Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
   
     2.2.2.2        4         100    18970    19008     0 91:51:24   Established    0
   
   ```
5. Create a VPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance ng
   ```
   ```
   [*PE1-vpn-instance-ng] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] route-distinguisher 1:1
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] vpn-target 1:1
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-ng] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] ip binding vpn-instance ng
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] ip address 10.0.6.3 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance ng
   ```
   ```
   [*PE1-bgp-af-vpn-ng] import-route direct
   ```
   ```
   [*PE1-bgp-af-vpn-ng] peer 10.0.6.6 as-number 65003
   ```
   ```
   [*PE1-bgp-af-vpn-ng] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance ng
   ```
   ```
   [*PE2-vpn-instance-ng] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4] route-distinguisher 2:2
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-ng] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip binding vpn-instance ng
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.0.14.4 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance ng
   ```
   ```
   [*PE2-bgp-af-vpn-ng] import-route direct
   ```
   ```
   [*PE2-bgp-af-vpn-ng] peer 10.0.14.1 as-number 65004
   ```
   ```
   [*PE2-bgp-af-vpn-ng] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display ip vpn-instance verbose** command on the PEs to check VPN instance configurations.
   
   ```
   <PE1> display ip vpn-instance verbose
   ```
   ```
    Total VPN-Instances configured : 1
   ```
   ```
    Total IPv4 VPN-Instances configured : 1 
    Total IPv6 VPN-Instances configured : 0
   ```
   ```
    VPN-Instance Name and ID : ng, 1
   ```
   ```
     Interfaces : GigabitEthernet0/1/0
   ```
   ```
    Address family ipv4 
   ```
   ```
     Create date : 2017/03/18 11:30:35
   ```
   ```
     Up time : 0 days, 00 hours, 05 minutes and 19 seconds
   ```
   ```
     Route Distinguisher : 1.2.3.4:1
   ```
   ```
     Export VPN Targets :  1:1
   ```
   ```
     Import VPN Targets :  1:1
   ```
   ```
     Label policy: label per route
   ```
   ```
     The diffserv-mode Information is : uniform
   ```
   ```
     The ttl-mode Information is : pipe
   ```
6. Configure a unicast peer and a BGP MVPN peer relationship.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] bgp 65503
   ```
   ```
   [~CE1-bgp] ipv4-family unicast
   ```
   ```
   [~CE1-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*CE1-bgp-af-ipv4] import-route direct
   ```
   ```
   [*CE1-bgp-af-ipv4] peer 10.0.6.3 enable
   ```
   ```
   [*CE1-bgp-af-ipv4] commit
   ```
   ```
   [~CE1-bgp-af-ipv4] quit
   ```
   ```
   [~CE1-bgp] quit
   ```
   
   The configuration of CE2 is similar to that of CE1. For configuration details, see Configuration Files in this section.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family vpn-instance ng
   ```
   ```
   [~PE1-bgp-af-vpn-ng] import-route direct
   ```
   ```
   [*PE1-bgp-af-vpn-ng] peer 10.0.6.6 as-number 65003
   ```
   ```
   [*PE1-bgp-af-vpn-ng] commit
   ```
   ```
   [~PE1-bgp-af-vpn-ng] quit
   ```
   ```
   [~PE1-bgp] ipv4-family mvpn
   ```
   ```
   [~PE1-bgp-af-mvpn] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-mvpn] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-mvpn] commit
   ```
   ```
   [~PE1-bgp-af-mvpn] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
   
   # Configure the ABR.
   
   ```
   [~ABR] bgp 100
   ```
   ```
   [~ABR-bgp] ipv4-family mvpn
   ```
   ```
   [~ABR-bgp-af-mvpn] undo policy vpn-target
   ```
   ```
   [*ABR-bgp-af-mvpn] peer 1.1.1.1 enable
   ```
   ```
   [*ABR-bgp-af-mvpn] peer 3.3.3.3 enable
   ```
   ```
   [*ABR-bgp-af-mvpn] commit
   ```
   ```
   [~ABR-bgp-af-mvpn] quit
   ```
   ```
   [~ABR-bgp] quit
   ```
7. Configure PEs to use P2MP tunnels to carry multicast traffic.
   
   
   
   # Configure PE1 as a sender PE.
   
   ```
   [~PE1] multicast mvpn 1.1.1.1
   ```
   ```
   [~PE1] ip vpn-instance ng
   ```
   ```
   [~PE1-vpn-instance-ng] ipv4-family
   ```
   ```
   [~PE1-vpn-instance-ng-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] mvpn
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] sender-enable
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] import msdp
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] spt-only mode
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] ipmsi-tunnel
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn-ipmsi] mldp
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn-ipmsi] quit
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] quit
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-ng] commit
   ```
   ```
   [~PE1-vpn-instance-ng] quit
   ```
   
   # Configure PE2 as a receiver PE.
   
   ```
   [~PE2] multicast mvpn 3.3.3.3
   ```
   ```
   [~PE2] ip vpn-instance ng
   ```
   ```
   [~PE2-vpn-instance-ng] ipv4-family
   ```
   ```
   [~PE2-vpn-instance-ng-af-ipv4] multicast routing-enable
   ```
   ```
   [~PE2-vpn-instance-ng-af-ipv4] mvpn
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] export msdp
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] spt-only mode
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] quit
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-ng] commit
   ```
   ```
   [~PE2-vpn-instance-ng] quit
   ```
8. Configure PIM.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] pim
   ```
   ```
   [~CE1-pim] static-rp 10.0.6.6
   ```
   ```
   [*CE1-pim] commit
   ```
   ```
   [~CE1-pim] quit
   ```
   ```
   [~CE1] multicast routing-enable
   ```
   ```
   [*CE1] interface GigabitEthernet 0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [~CE1] interface GigabitEthernet 0/1/1
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] pim
   ```
   ```
   [~CE2-pim] static-rp 10.0.14.1
   ```
   ```
   [*CE2-pim] commit
   ```
   ```
   [~CE2-pim] quit
   ```
   ```
   [~CE2] multicast routing-enable
   ```
   ```
   [*CE2] interface GigabitEthernet 0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [~CE2] interface GigabitEthernet 0/1/1
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] igmp enable
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] quit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] pim vpn-instance ng
   ```
   ```
   [*PE1-pim-ng] static-rp 10.0.6.3
   ```
   ```
   [*PE1-pim-ng] source-lifetime 60
   ```
   ```
   [*PE1-msdp-ng] commit
   ```
   ```
   [~PE1-msdp-ng] quit
   ```
   ```
   [~PE1] interface GigabitEthernet 0/1/1
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] quit
   ```
   
   The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
9. Verify the configuration.
   
   
   
   After the configuration is complete, CE1 and CE2 can ping each other.
   
   The command output on CE1 is used as an example.
   
   ```
   <CE1> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ```
   ```
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: _public_
   ```
   ```
            Destinations : 9        Routes : 9
   ```
   ```
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   ```
   ```
          10.0.6.0/24  Direct 0    0             D  10.0.6.6        GigabitEthernet0/1/0
   ```
   ```
          10.0.6.6/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
   ```
   ```
        10.0.6.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
   ```
   ```
          10.0.6.6/24  Direct 0    0             D  127.0.0.1       LoopBack1
   ```
   ```
        10.0.14.0/24  IBGP   255  0             D  10.0.6.3        GigabitEthernet0/1/0
   ```
   ```
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   <CE1> ping -a 10.0.6.6 10.0.14.1
   ```
   ```
     PING 10.0.14.1: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.0.14.1: bytes=56 Sequence=1 ttl=252 time=109 ms
   ```
   ```
       Reply from 10.0.14.1: bytes=56 Sequence=2 ttl=252 time=89 ms
   ```
   ```
       Reply from 10.0.14.1: bytes=56 Sequence=3 ttl=252 time=71 ms
   ```
   ```
       Reply from 10.0.14.1: bytes=56 Sequence=4 ttl=252 time=116 ms
   ```
   ```
       Reply from 10.0.14.1: bytes=56 Sequence=5 ttl=252 time=70 ms
   ```
   ```
     --- 10.0.14.1 ping statistics ---
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
       round-trip min/avg/max = 70/91/116 ms 
   ```
   
   Run the **display bgp vpnv4 all routing-table** command on the ABR. The command output shows the VPNv4 routes on the ABR.
   
   The command output on the ABR is used as an example.
   
   ```
   <ABR> display bgp vpnv4 all routing-table
   ```
   ```
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total number of routes from all PE: 2
    Route Distinguisher: 1:1
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  10.0.6.6/32       1.1.1.1         0          100        0      ?
    Route Distinguisher: 2:3
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   10.0.14.1/32      3.3.3.3                               0      200?
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.0.6.6 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.5.6 255.255.255.0
   pim sm
  #
  bgp 65503
   peer 10.0.6.3 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.0.6.3 enable
  #
  ospf 2
   area 0.0.0.1
    network 10.0.5.0 0.0.0.255
    network 10.0.6.0 0.0.0.255
  #
  pim
   static-rp 10.0.6.6
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
   sysname PE1
  #
  multicast mvpn 1.1.1.1
  #
  ip vpn-instance ng
   ipv4-family
    route-distinguisher 1:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     import msdp
     spt-only mode
     ipmsi-tunnel
      mldp
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown 
   ip address 10.0.2.3 255.255.255.0
   mpls 
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown 
   ip binding vpn-instance ng
   ip address 10.0.6.3 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    network 1.1.1.1 255.255.255.255
    peer 2.2.2.2 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance ng
    peer 10.0.6.6 as-number 65003
    import-route ospf 2
  #
  ospf 1
   area 0.0.0.0
    network 10.0.2.0 0.0.0.255
    network 1.1.1.1 0.0.0.0
  #
  ospf 2 vpn-instance ng
   area 0.0.0.1
    network 10.0.6.0 0.0.0.255
  #
  pim vpn-instance ng
   static-rp 10.0.6.3
   source-lifetime 60
  #
  return
  ```
* ABR configuration file
  
  ```
  #
  sysname ABR
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
   mldp p2mp
   mldp recursive-fec
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.000c.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.0.2.5 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.16.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #  
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
   #
   ipv4-family mvpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
  #
  ospf 1
   area 0.0.0.0
    network 10.0.2.0 0.0.0.255
    network 2.2.2.2 0.0.0.0
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast mvpn 3.3.3.3
  #
  ip vpn-instance ng
   #
   ipv4-family
    route-distinguisher 2:2
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     export msdp
     spt-only mode
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
   mldp p2mp
   mldp recursive-fec
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.000d.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance ng
   ip address 10.0.14.4 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.16.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    network 3.3.3.3 255.255.255.255
    peer 2.2.2.2 enable
   #
   ipv4-family mvpn
    undo policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance ng
    peer 10.0.14.1 as-number 65004
    import-route ospf 2
  #
  ospf 2 vpn-instance ng
   area 0.0.0.1
    network 3.3.3.3 0.0.0.0
    network 10.0.14.0 0.0.0.255
  #
  pim vpn-instance ng
   static-rp 10.0.14.4
   source-lifetime 60
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.3.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.0.14.1 255.255.255.0
   pim sm
  #
  bgp 65504
   peer 10.0.14.4 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.0.14.4 enable
  #
  ospf 2
   area 0.0.0.1
    network 10.0.3.0 0.0.0.255
    network 10.0.14.0 0.0.0.255
  #
  pim
   static-rp 10.0.14.1
  #
  return
  ```