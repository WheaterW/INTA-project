Example for Configuring Inter-AS NG MVPN in Option B Mode
=========================================================

In the scenario where the backbone network spans multiple ASs, ASBRs advertise labeled VPN IPv4 routes through MP-EBGP.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001270153525__fig_dc_vrp_cfg_ngmvpn_007301), the inter-AS NG MVPN is deployed on an Option B network. PE1 connects to the multicast source, and PE2 connects to the multicast receiver. CE1 and CE2 belong to different VPN instances, and devices of the VPN instances communicate across AS100 and AS200. The VPN configuration does not need to be deployed on the ASBRs. The ASBRs only need to forward VPNv4 routes to peer ASBRs. An MP-IBGP relationship is established between each PE and ASBR within an AS domain. An MP-EBGP relationship is established between ASBRs.

**Figure 1** Configuring inter-AS NG MVPN in option B mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, 3, and 4 in this example represent GE 0/1/0, GE 0/1/1, GE 0/1/2, and GE0/1/3, respectively.


  
![](figure/en-us_image_0000001225833660.png)

| Device Name | Interface Name | IP Address |
| --- | --- | --- |
| CE1 | GigabitEthernet0/1/0 | 10.1.4.1/24 |
| GigabitEthernet0/1/2 | 192.168.1.1/24 |
| PE1 | LoopBack0 | 1.1.1.1/32 |
| GigabitEthernet0/1/2 | 192.168.1.2/24 |
| GigabitEthernet0/1/3 | 10.1.1.1/24 |
| ASBR1 | LoopBack0 | 2.2.2.2/32 |
| GigabitEthernet0/1/1 | 10.1.2.1/24 |
| GigabitEthernet0/1/3 | 10.1.1.2/24 |
| ASBR2 | LoopBack0 | 3.3.3.3/32 |
| GigabitEthernet0/1/2 | 10.1.2.2/24 |
| GigabitEthernet0/1/3 | 10.1.3.1/24 |
| PE2 | Loopback1 | 4.4.4.4/32 |
| GigabitEthernet0/1/2 | 10.1.3.2/24 |
| GigabitEthernet0/1/3 | 192.168.2.2/24 |
| CE2 | GigabitEthernet0/1/0 | 10.1.6.1/24 |
| GigabitEthernet0/1/3 | 192.168.2.1/24 |



#### Precautions

During the configuration, pay attention to the following:

* Configure an MP-EBGP peer relationship between the ASBRs in different ASs. Configure an MP-IBGP peer relationship between each PE and ASBR in the same AS.
* The ASBRs do not filter received VPNv4 routes based on VPN targets.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP in each AS for interworking among devices in the same AS; set up an MPLS LDP LSP between the ASBR and PE in the same AS.
2. Set up an MP-EBGP peer relationship between the ASBRs in different ASs; set up an MP-IBGP peer relationship between the PE and ASBR in the same AS.
3. Configure a VPN instance on each PE and bind the interface that connects a PE to a CE to the VPN instance on that PE.
4. Enable MPLS on the interfaces that connect the ASBRs, establish an MP-EBGP peer relationship between the ASBRs, and configure the ASBRs not to filter received VPNv4 routes based on VPN targets.
5. Configure BGP peers.
6. Configure multicast traffic transmission over P2MP tunnels.
7. Configure PIM.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PEs and ASBRs (1.1.1.1, 2.2.2.2, 3.3.3.3, and 4.4.4.4)
* VPN instance names (ng), RDs (100:1 and 200:1), and VPN targets of VPN instances (1:1)

#### Procedure

1. On the MPLS backbone network in each AS, configure an IGP to interconnect the devices in the same AS.
   
   
   
   This example uses OSPF as the IGP. For configuration details, see Configuration Files in this section.
   
   After the configurations are complete, the OSPF neighbor relationship can be established between the devices in the same AS. Run the **display ospf peer** command. The command output shows that the neighbor relationship is in the **Full** state. The devices in the same AS can learn and ping the IP address of each other's loopback interface.
2. Configure basic MPLS functions and MPLS LDP, and set up LDP LSPs on the MPLS backbone network of each AS.
   
   
   
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
   [*PE1] interface GigabitEthernet0/1/3
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/3] quit
   ```
   
   The configuration of PE2 is similar to the configuration of PE1. For configuration details, see Configuration Files in this section.
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls lsr-id 2.2.2.2
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
   [*ASBR1] interface GigabitEthernet0/1/1
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*ASBR1] interface GigabitEthernet0/1/3
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/3] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/1/3] quit
   ```
   
   The configuration of ASBR2 is similar to the configuration of ASBR1. For configuration details, see Configuration Files in this section.
   
   After the configurations are complete, LDP peer relationships can be established between each PE and the corresponding ASBR and between the ASBRs. Run the **display mpls ldp session** command on each router. The command output shows that the **Status** field is **Operational**. The command output on PE1 is used as an example.
   
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
3. Configure automatic mLDP P2MP tunnels on PEs and ASBRs.
   
   
   
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
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls ldp
   ```
   ```
   [~ASBR1-mpls-ldp] mldp p2mp
   ```
   ```
   [*ASBR1-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*ASBR1-mpls-ldp] commit
   ```
   ```
   [~ASBR1-mpls-ldp] quit
   ```
   
   The configuration of ASBR2 is similar to the configuration of ASBR1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153525__example1680602931214042) in this section.
4. Configure BGP areas, and set up an MP-IBGP peer relationship between the PE and ASBR in the same AS.
   
   
   
   # On CE1, configure BGP.
   
   ```
   [~CE1] bgp 65003
   ```
   ```
   [*CE1-bgp] peer 192.168.1.2 as-number 100
   ```
   
   The configuration of CE2 is similar to the configuration of CE1. For configuration details, see Configuration Files in this section.
   
   # On PE1, set up an MP-IBGP peer relationship between the PE and the ASBR in the same AS.
   
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
   [*PE1-bgp] ipv4-family vpnv4
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
   
   # On ASBR1, set up an MP-IBGP peer relationship between it and the PE in the same AS.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 connect-interface loopback 0
   ```
   ```
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 1.1.1.1 enable
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
   
   The configurations of devices in AS200 are similar to the configurations of devices in AS100. For configuration details, see Configuration Files in this section.
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command on the PE or ASBR. The command output shows that an MP-IBGP peer relationship has been established between the PE and ASBR in the same AS. The following example uses the command output on PE1.
   
   ```
   <PE1> display bgp vpnv4 all peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1         Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
   
     2.2.2.2        4         100    18970    19008     0 91:51:24   Established    0
   
   ```
5. Configure VPN instances on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance ng
   ```
   ```
   [*PE1-vpn-instance-ng] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-ng] quit
   ```
   ```
   [*PE1] interface GigabitEthernet0/1/2
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] ip binding vpn-instance ng
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] ip address 192.168.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] quit
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
   [*PE2-vpn-instance-ng-af-ipv4] route-distinguisher 200:1
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
   [*PE2] interface GigabitEthernet0/1/3
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] ip binding vpn-instance ng
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] ip address 192.168.2.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/3] quit
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
    
   ```
   ```
    VPN-Instance Name and ID : ng, 1
   ```
   ```
     Interfaces : GigabitEthernet0/1/2
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
     Route Distinguisher : 100:1
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
6. Set up an MP-EBGP peer relationship between ASBRs across ASs, and disable VPN-target-based filtering on received VPNv4 routes.
   
   
   
   # On ASBR1, enable MPLS on GigabitEthernet0/1/1, which is connected to ASBR2.
   
   ```
   [~ASBR1] interface GigabitEthernet0/1/1
   ```
   ```
   [~ASBR1-GigabitEthernet0/1/1] ip address 10.1.2.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/1/1] quit
   ```
   
   # On ASBR2, enable MPLS on GigabitEthernet0/1/2, which is connected to ASBR1.
   
   ```
   [~ASBR2] interface GigabitEthernet0/1/2
   ```
   ```
   [~ASBR2-GigabitEthernet0/1/2] ip address 10.1.2.2 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/2] commit
   ```
   ```
   [~ASBR2-GigabitEthernet0/1/2] quit
   ```
   
   # On ASBR1, establish an MP-EBGP peer relationship with ASBR2, and disable ASBR1 from filtering received VPNv4 routes based on VPN targets.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [~ASBR1-bgp] peer 10.1.2.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 10.1.2.2 enable
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
   
   # On ASBR2, establish an MP-EBGP peer relationship with ASBR1, and disable ASBR2 from filtering received VPNv4 routes based on VPN targets.
   
   ```
   [~ASBR2] bgp 200
   ```
   ```
   [~ASBR2-bgp] peer 10.1.2.1 as-number 100
   ```
   ```
   [*ASBR2-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR2-bgp-af-vpnv4] peer 10.1.2.1 enable
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
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command. The command output shows that an MP-EBGP peer relationship has been established between the ASBRs. The following example uses the command output on ASBR1.
   
   ```
   <ASBR1> display bgp vpnv4 all peer
   
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Total number of peers : 2         Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
   
     1.1.1.1        4         100    17533    17554     0 127:24:5 Established    1
     3.3.3.3        4         200    12343    34554     0 127:24:5 Established    1
   ```
7. Configure a unicast peer and a BGP MVPN peer relationship.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] bgp 65003
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
   [*CE1-bgp-af-ipv4] peer 192.168.1.2 enable
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
   
   The configuration of CE2 is similar to the configuration of CE1. For configuration details, see Configuration Files in this section.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family unicast
   ```
   ```
   [~PE1-bgp-af-ipv4] undo synchronization
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
   [~PE1-bgp] ipv4-family vpn-instance ng
   ```
   ```
   [~PE1-bgp-af-vpn-ng] import-route direct
   ```
   ```
   [*PE1-bgp-af-vpn-ng] peer 192.168.1.1 as-number 65003
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
   
   The configuration of PE2 is similar to the configuration of PE1. For configuration details, see Configuration Files in this section.
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [~ASBR1-bgp] ipv4-family unicast
   ```
   ```
   [~ASBR1-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 10.1.2.2 enable
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 1.1.1.1 enable
   ```
   ```
   [*ASBR1-bgp-af-ipv4] commit
   ```
   ```
   [~ASBR1-bgp-af-ipv4] quit
   ```
   ```
   [~ASBR1-bgp] ipv4-family mvpn
   ```
   ```
   [~ASBR1-bgp-af-mvpn] undo policy vpn-target
   ```
   ```
   [*ASBR1-bgp-af-mvpn] peer 10.1.2.2 enable
   ```
   ```
   [*ASBR1-bgp-af-mvpn] peer 1.1.1.1 enable
   ```
   ```
   [*ASBR1-bgp-af-mvpn] commit
   ```
   ```
   [~ASBR1-bgp-af-mvpn] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   The configuration of ASBR2 is similar to the configuration of ASBR1. For configuration details, see Configuration Files in this section.
8. Configure MSDP peers on CEs and PEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] msdp
   ```
   ```
   [~CE1-msdp] peer 192.168.1.2 connect-interface GigabitEthernet0/1/2
   ```
   ```
   [*CE1-msdp] commit
   ```
   ```
   [~CE1-msdp] quit
   ```
   
   The configuration of CE2 is similar to the configuration of CE1. For configuration details, see Configuration Files in this section.
   
   # Configure PE1.
   
   ```
   [~PE1] msdp vpn-instance ng
   ```
   ```
   [~PE1-msdp-ng] peer 192.168.1.1 connect-interface GigabitEthernet0/1/2
   ```
   ```
   [*PE1-msdp-ng] commit
   ```
   ```
   [~PE1-msdp-ng] quit
   ```
   
   The configuration of PE2 is similar to the configuration of PE1. For configuration details, see Configuration Files in this section.
9. Configure PEs to use P2MP tunnels to carry multicast traffic.
   
   
   
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
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] spt-only mode
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] import msdp
   ```
   ```
   [*PE1-vpn-instance-ng-af-ipv4-mvpn] auto-discovery inter-as
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
   [~PE2] multicast mvpn 4.4.4.4
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
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] spt-only mode
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] export msdp
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] auto-discovery inter-as
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn] ipmsi-tunnel
   ```
   ```
   [*PE2-vpn-instance-ng-af-ipv4-mvpn-ipmsi] quit
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
10. Configure PIM.
    
    
    
    # Configure CE1.
    
    ```
    [~CE1] pim
    ```
    ```
    [~CE1-pim] static-rp 192.168.1.1
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
    [*CE1] interface GigabitEthernet0/1/0
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
    [~CE1] interface GigabitEthernet0/1/2
    ```
    ```
    [~CE1-GigabitEthernet0/1/2] pim sm
    ```
    ```
    [*CE1-GigabitEthernet0/1/2] commit
    ```
    ```
    [~CE1-GigabitEthernet0/1/2] quit
    ```
    
    # Configure CE2.
    
    ```
    [~CE2] pim
    ```
    ```
    [~CE2-pim] static-rp 192.168.2.1
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
    [*CE2] interface GigabitEthernet0/1/0
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] pim sm
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] igmp enable
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] commit
    ```
    ```
    [~CE2-GigabitEthernet0/1/0] quit
    ```
    ```
    [~CE2] interface GigabitEthernet0/1/3
    ```
    ```
    [~CE1-GigabitEthernet0/1/3] pim sm
    ```
    ```
    [*CE1-GigabitEthernet0/1/3] commit
    ```
    ```
    [~CE1-GigabitEthernet0/1/3] quit
    ```
    
    # Configure PE1.
    
    ```
    [~PE1] pim vpn-instance ng
    ```
    ```
    [*PE1-pim-ng] static-rp 192.168.1.2
    ```
    ```
    [*PE1-pim-ng] source-lifetime 60
    ```
    ```
    [*PE1-pim-ng] commit
    ```
    ```
    [~PE1-pim-ng] quit
    ```
    ```
    [~PE1] interface GigabitEthernet0/1/2
    ```
    ```
    [~PE1-GigabitEthernet0/1/2] pim sm
    ```
    ```
    [*PE1-GigabitEthernet0/1/2] commit
    ```
    ```
    [~PE1-GigabitEthernet0/1/2] quit
    ```
    
    The configuration of PE2 is similar to the configuration of PE1. For configuration details, see Configuration Files in this section.
11. Verify the configuration.
    
    
    
    After completing the configurations, CE1 and CE2 can ping each other.
    
    The following example uses the command output on CE1.
    
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
    Routing Tables _public_
    ```
    ```
             Destinations : 9        Routes : 9
    ```
    ```
    Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
    ```
    ```
           192.168.1.0/24  Direct 0    0           D   192.168.1.1       GigabitEthernet0/1/2
    ```
    ```
           192.168.1.1/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/2
    ```
    ```
         192.168.1.255/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/2
    ```
    ```
          192.168.2.0/24  EBGP   255  0           D  192.168.1.2        GigabitEthernet0/1/2
    ```
    ```
          127.0.0.0/8   Direct 0    0           D  127.0.0.1       InLoopBack0
    ```
    ```
          127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
    ```
    ```
    127.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
    ```
    ```
    255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
    ```
    ```
    <CE1> ping -a 192.168.1.1 192.168.2.1
    ```
    ```
      PING 192.168.2.1: 56  data bytes, press CTRL_C to break
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=1 ttl=252 time=120 ms
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=2 ttl=252 time=73 ms
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=3 ttl=252 time=111 ms
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=4 ttl=252 time=86 ms
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=5 ttl=252 time=110 ms
    ```
    ```
      --- 192.168.2.1 ping statistics ---
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
        round-trip min/avg/max = 73/100/120 ms 
    ```
    
    Run the **display bgp vpnv4 all routing-table** command on ASBRs to see the VPNv4 routes.
    
    The following example uses the command output on ASBR1.
    
    ```
    <ASBR1> display bgp vpnv4 all routing-table
    ```
    ```
     BGP Local router ID is 2.2.2.2
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
     RPKI validation codes: V - valid, I - invalid, N - not-found
    
    
     Total number of routes from all PE: 2
     Route Distinguisher: 100:1
    
    
          Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
    
     *>i  192.168.1.1/32        1.1.1.1       0          100        0      ?
     Route Distinguisher: 200:1
    
    
          Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
    
     *>   192.168.2.1/32       10.1.2.2                             0      200?
    ```
    
    If CE2 has multicast users, CE2 can receive multicast data from CE1.

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
   ip address 10.1.4.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  bgp 65003
   peer 192.168.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 192.168.1.2 enable
  #
  pim
   static-rp 192.168.1.1
  #
  msdp
   peer 192.168.1.2 connect-interface GigabitEthernet0/1/2
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
    route-distinguisher 100:1
    apply-label per-instance 
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     import msdp
     spt-only mode
     auto-discovery inter-as
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
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance ng
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
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
    import-route direct
    peer 192.168.1.1 as-number 65003
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 1.1.1.1 0.0.0.0
  #
  pim vpn-instance ng
   static-rp 192.168.1.2
   source-lifetime 60
  #
  msdp vpn-instance ng
   peer 192.168.1.1 connect-interface GigabitEthernet0/1/2
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
   sysname ASBR1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
   mldp p2mp
   mldp recursive-fec
  #
  interface GigabitEthernet0/1/1 
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  bgp 100
   peer 10.1.2.2 as-number 200
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.2.2 enable
    peer 1.1.1.1 enable
   #
   ipv4-family mvpn
    undo policy vpn-target
    peer 10.1.2.2 enable
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 10.1.2.2 enable
    peer 1.1.1.1 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 2.2.2.2 0.0.0.0
  #
  ip route-static 3.3.3.3 255.255.255.255 10.1.2.2
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
   sysname ASBR2
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
   mldp p2mp
   mldp recursive-fec
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  bgp 200
   peer 10.1.2.1 as-number 100
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.2.1 enable
    peer 4.4.4.4 enable
   #
   ipv4-family mvpn
    undo policy vpn-target
    peer 10.1.2.1 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 10.1.2.1 enable
    peer 4.4.4.4 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 3.3.3.3 0.0.0.0
  #
  ip route-static 2.2.2.2 255.255.255.255 10.1.2.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast mvpn 4.4.4.4
  #
  ip vpn-instance ng
   #
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     export msdp
     spt-only mode
     auto-discovery inter-as
     ipmsi-tunnel
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls ldp
   mldp p2mp
   mldp recursive-fec
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip binding vpn-instance ng
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 200
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance ng
    import-route direct
    peer 192.168.2.1 as-number 65004
  #
  ospf 1
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 4.4.4.4 0.0.0.0
  #
  pim vpn-instance ng
   static-rp 192.168.2.2
   source-lifetime 60
  #
  msdp vpn-instance ng
   peer 192.168.2.1 connect-interface GigabitEthernet0/1/3
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
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.6.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface GigabitEthernet0/1/3
    undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  bgp 65004
   peer 192.168.2.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 192.168.2.2 enable
  #
  pim
   static-rp 192.168.2.1
  #
  msdp
   peer 192.168.2.2 connect-interface GigabitEthernet0/1/3
  #
  return
  ```