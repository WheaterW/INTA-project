Example for Configuring an Inter-Area Seamless MPLS NG MVPN
===========================================================

The backbone network is in an AS. PE and ABR advertise routes through MP-IBGP.

#### Networking Requirements

As shown in the [Figure 1](#EN-US_TASK_0000001270313537__fig_dc_vrp_cfg_ngmvpn_007701), CE1 is in AS 65003 and CE2 is in AS 65004. CEs communicate with each other spanning AS 65535.65535. An MP-IBGP peer relationship is established between each PE and the corresponding ABR. ABRs are configured as RRs.

**Figure 1** Configuring inter-area seamless NG MVPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, 3, and 4 in this example represent GE 0/1/0, GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](figure/en-us_image_0000001270193849.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| CE1 | GigabitEthernet0/1/0 | 192.168.3.1/24 |
| GigabitEthernet0/1/2 | 192.168.1.1/24 |
| PE1 | LoopBack0 | 1.1.1.1/32 |
| GigabitEthernet0/1/2 | 192.168.1.2/24 |
| GigabitEthernet0/1/3 | 10.1.1.1/24 |
| ABR1 | LoopBack0 | 2.2.2.2/32 |
| GigabitEthernet0/1/1 | 10.1.2.1/24 |
| GigabitEthernet0/1/3 | 10.1.1.2/24 |
| ABR2 | LoopBack0 | 3.3.3.3/32 |
| GigabitEthernet0/1/2 | 10.1.2.2/24 |
| GigabitEthernet0/1/3 | 10.1.3.1/24 |
| PE2 | Loopback0 | 4.4.4.4/32 |
| GigabitEthernet0/1/2 | 10.1.3.2/24 |
| GigabitEthernet0/1/3 | 192.168.2.2/24 |
| CE2 | GigabitEthernet0/1/0 | 192.168.4.1/24 |
| GigabitEthernet0/1/3 | 192.168.2.1/24 |



#### Precautions

During the configuration, pay attention to the following points:

* Set up MP-IBGP peer relationship between PE and ABR and between ABRs.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP in each AS for interworking among devices in the same AS; set up an MPLS LDP LSP between the ABR and PE in the same AS.
2. Configure the automatic mLDP P2MP tunnel function on the PEs and ABR.
3. Configure BGP and establish MP-IBGP peer relationships between the PEs and ABR in the same AS.
4. Configure VPN instances on PEs.
5. Configure a routing policy to control label distribution for a BGP LSP to be established on PEs and ABRs.
6. Configure ABR as an RR to reflect the loopback routes of PE1 and PE2 to each other.
7. Configure BGP peers.
8. Configure multicast traffic transmission over P2MP tunnels.
9. Configure PIM.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PEs and ABRs: 1.1.1.1, 2.2.2.2, 3.3.3.3, and 4.4.4.4

#### Procedure

1. Configure an IGP on the MPLS backbone network, so that the PEs and ABRs can communicate.
   
   
   
   This example uses OSPF as the IGP. For configuration details, see Configuration Files in this section.
   
   After the configurations are complete, OSPF neighbor relationship is established for each node in the AS.
2. Configure basic MPLS functions and MPLS LDP, and set up LDP LSPs on the MPLS backbone network of the AS.
   
   
   
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
   [*PE1] interface GigabitEthernet 0/1/3
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
   
   # Configure ABR1.
   
   ```
   [~ABR1] mpls lsr-id 2.2.2.2
   ```
   ```
   [*ABR1] mpls
   ```
   ```
   [*ABR1-mpls] quit
   ```
   ```
   [*ABR1] mpls ldp
   ```
   ```
   [*ABR1-mpls-ldp] quit
   ```
   ```
   [*ABR1] interface GigabitEthernet 0/1/1
   ```
   ```
   [*ABR1-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*ABR1-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*ABR1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~ABR1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*ABR1] interface GigabitEthernet 0/1/3
   ```
   ```
   [*ABR1-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*ABR1-Ethernet0/1/3] mpls ldp
   ```
   ```
   [*ABR1-Ethernet0/1/3] commit
   ```
   ```
   [~ABR1-Ethernet0/1/3] quit
   ```
   
   The configuration of ABR2 is similar to the configuration of ABR1. For configuration details, see Configuration Files in this section.
   
   After the configurations are complete, the LDP sessions can be established between each PE and the corresponding ABR and between the ABRs. Run the **display mpls ldp session** command on each Router. The command output shows that the **Status** field is **Operational**. The command output on PE1 is used as an example.
   
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
   
   # Configure ABR1.
   
   ```
   [~ABR1] mpls ldp
   ```
   ```
   [~ABR1-mpls-ldp] mldp p2mp
   ```
   ```
   [*ABR1-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*ABR1-mpls-ldp] commit
   ```
   ```
   [~ABR1-mpls-ldp] quit
   ```
   
   The configuration of ABR2 is similar to the configuration of ABR1. For configuration details, see Configuration Files in this section.
4. Configure BGP and establish MP-IBGP peer relationships between the PEs and ABR in the same AS.
   
   
   
   # On CE1, configure BGP.
   
   ```
   [~CE1] bgp 65003
   ```
   ```
   [*CE1-bgp] peer 192.168.1.2 as-number 65535.65535
   ```
   
   The configuration of CE2 is similar to the configuration of CE1. For configuration details, see Configuration Files in this section.
   
   # Configure PE1 to establish an MP-IBGP peer relationship between the ABR.
   
   ```
   [~PE1] bgp 65535.65535
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 65535.65535
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
   [*PE1-bgp-af-ipv4] peer 2.2.2.2 label-route-capability
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
   
   The configuration of PE2 is similar to the configuration of PE1. For configuration details, see Configuration Files in this section.
   
   # Configure ABR1 to establish an MP-IBGP peer relationship with the corresponding PE.
   
   ```
   [~ABR1] bgp 65535.65535
   ```
   ```
   [*ABR1-bgp] peer 1.1.1.1 as-number 65535.65535
   ```
   ```
   [*ABR1-bgp] peer 1.1.1.1 connect-interface loopback 0
   ```
   ```
   [*ABR1-bgp] peer 3.3.3.3 as-number 65535.65535
   ```
   ```
   [*ABR1-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*ABR1-bgp] ipv4-family unicast
   ```
   ```
   [*ABR1-bgp-af-mvpn] undo synchronization
   ```
   ```
   [*ABR1-bgp-af-mvpn] peer 1.1.1.1 enable
   ```
   ```
   [*ABR1-bgp-af-mvpn] peer 1.1.1.1 label-route-capability
   ```
   ```
   [*ABR1-bgp-af-mvpn] peer 3.3.3.3 enable
   ```
   ```
   [*ABR1-bgp-af-mvpn] peer 3.3.3.3 label-route-capability
   ```
   ```
   [*ABR1-bgp-af-mvpn] quit
   ```
   ```
   [*ABR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ABR1-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*ABR1-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*ABR1-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*ABR1-bgp-af-vpnv4] quit
   ```
   ```
   [*ABR1-bgp] commit
   ```
   ```
   [~ABR1-bgp] quit
   ```
   
   The configuration of ABR2 is similar to the configuration of ABR1. For configuration details, see Configuration Files in this section.
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command on the PE or ABR. The command output shows that an MP-IBGP peer relationship has been established between the PE and ABR and between the ABRs. The following example uses the command output on PE1.
   
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
   [*PE1-vpn-instance-ng-af-ipv4] route-distinguisher 1.2.3.4:1
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
   [*PE1] interface GigabitEthernet 0/1/2
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
   [*PE1] bgp 65535.65535
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance ng
   ```
   ```
   [*PE1-bgp-af-vpn-ng] import-route direct
   ```
   ```
   [*PE1-bgp-af-vpn-ng] peer 192.168.1.1 as-number 65003
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
   [*PE2-vpn-instance-ng-af-ipv4] route-distinguisher 2:3
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
   [*PE2] interface GigabitEthernet 0/1/3
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] ip binding vpn-instance ng
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] ip address 192.168.2.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE2] bgp 65535.65535
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance ng
   ```
   ```
   [*PE2-bgp-af-vpn-ng] import-route direct
   ```
   ```
   [*PE2-bgp-af-vpn-ng] peer 192.168.2.1 as-number 65004
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
   [~PE1] bgp 65535.65535
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
   
   # Configure ABR1.
   
   ```
   [~ABR1] bgp 65535.65535
   ```
   ```
   [~ABR1-bgp] ipv4-family mvpn
   ```
   ```
   [~ABR1-bgp-af-mvpn] undo policy vpn-target
   ```
   ```
   [*ABR1-bgp-af-mvpn] peer 1.1.1.1 enable
   ```
   ```
   [*ABR1-bgp-af-mvpn] peer 3.3.3.3 enable
   ```
   ```
   [*ABR1-bgp-af-mvpn] commit
   ```
   ```
   [~ABR1-bgp-af-mvpn] quit
   ```
   ```
   [~ABR1-bgp] quit
   ```
   
   The configuration of ABR2 is similar to the configuration of ABR1. For configuration details, see Configuration Files in this section.
7. Configure the ABR as an RR to reflect routes so that PE1 and PE2 can obtain the route destined for each other's loopback interface.
   
   
   
   # Configure ABR1.
   
   ```
   [~ABR1] bgp 65535.65535
   ```
   ```
   [*ABR1-bgp] ipv4-family unicast
   ```
   ```
   [*ABR1-bgp-af-ipv4] peer 1.1.1.1 reflect-client
   ```
   ```
   [*ABR1-bgp-af-ipv4] peer 1.1.1.1 next-hop-local
   ```
   ```
   [*ABR1-bgp-af-ipv4] peer 3.3.3.3 reflect-client
   ```
   ```
   [*ABR1-bgp-af-ipv4] peer 3.3.3.3 next-hop-local
   ```
   ```
   [*ABR1-bgp-af-ipv4] quit
   ```
   ```
   [*ABR1-bgp] ipv4-family mvpn
   ```
   ```
   [*ABR1-bgp-af-mvpn] peer 1.1.1.1 reflect-client
   ```
   ```
   [*ABR1-bgp-af-mvpn] peer 3.3.3.3 reflect-client
   ```
   ```
   [*ABR1-bgp-af-mvpn] quit
   ```
   ```
   [*ABR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ABR1-bgp-af-vpnv4] peer 1.1.1.1 reflect-client
   ```
   ```
   [*ABR1-bgp-af-vpnv4] peer 3.3.3.3 reflect-client
   ```
   ```
   [*ABR1-bgp-af-vpnv4] quit
   ```
   ```
   [*ABR1-bgp] quit
   ```
   ```
   [*ABR1] commit
   ```
   
   The configuration of ABR2 is similar to the configuration of ABR1. For configuration details, see Configuration Files in this section.
8. Configure a route-policy on PEs and ABRs to establish a BGP LSP.
   
   
   
   # Create a route-policy on PE1 and apply the route-policy to the routes to be advertised to a specified peer.
   
   ```
   [~PE1] route-policy policy1 permit node 1
   ```
   ```
   [*PE1-route-policy] apply mpls-label
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] bgp 65535.65535
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2.2.2.2 route-policy policy1 export
   ```
   ```
   [*PE1-bgp-af-ipv4] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration of PE2 is similar to the configuration of PE1. For configuration details, see Configuration Files in this section.
   
   # Create a route-policy on the ABR and apply the route-policy to the routes to be advertised to specified peers.
   
   ```
   [~ABR1] route-policy policy1 permit node 1
   ```
   ```
   [*ABR1-route-policy] apply mpls-label
   ```
   ```
   [*ABR1-route-policy] quit
   ```
   ```
   [*ABR1] 65535.65535
   ```
   ```
   [*ABR1-bgp] ipv4-family unicast
   ```
   ```
   [*ABR1-bgp-af-ipv4] peer 1.1.1.1 route-policy policy1 export
   ```
   ```
   [*ABR1-bgp-af-ipv4] peer 3.3.3.3 route-policy policy1 export
   ```
   ```
   [*ABR1-bgp-af-ipv4] quit
   ```
   ```
   [*ABR1-bgp] quit
   ```
   ```
   [*ABR1] commit
   ```
   
   The configuration of ABR2 is similar to the configuration of ABR1. For configuration details, see Configuration Files in this section.
9. Configure MSDP peer relationship between CEs and PEs.
   
   
   
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
10. Configure PEs to use P2MP tunnels to carry multicast traffic.
    
    
    
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
11. Configure PIM.
    
    
    
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
    [~CE1] interface GigabitEthernet 0/1/2
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
    [~CE2] interface GigabitEthernet 0/1/3
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
    [*PE1-msdp-ng] commit
    ```
    ```
    [~PE1-msdp-ng] quit
    ```
    ```
    [~PE1] interface GigabitEthernet 0/1/2
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
12. Verify the configuration.
    
    
    
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
           192.168.1.0/24  Direct 0    0             D  192.168.1.1        GigabitEthernet0/1/0
    ```
    ```
           192.168.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
    ```
    ```
         192.168.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
    ```
    ```
           192.168.1.1/24  Direct 0    0             D  127.0.0.1       LoopBack1
    ```
    ```
         192.168.2.0/24  IBGP   255  0             D  192.168.1.2       GigabitEthernet0/1/0
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
    <CE1> ping -a 192.168.1.1 192.168.2.1
    ```
    ```
      PING 192.168.2.1: 56  data bytes, press CTRL_C to break
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=1 ttl=252 time=109 ms
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=2 ttl=252 time=89 ms
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=3 ttl=252 time=71 ms
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=4 ttl=252 time=116 ms
    ```
    ```
        Reply from 192.168.2.1: bytes=56 Sequence=5 ttl=252 time=70 ms
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
        round-trip min/avg/max = 70/91/116 ms 
    ```
    
    Run the **display bgp vpnv4 all routing-table** command on ABR to display the VPNv4 routes information.
    
    The following example uses the command output on ABR1.
    
    ```
    <ABR1> display bgp vpnv4 all routing-table
    ```
    ```
     BGP Local router ID is 2.2.2.2
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
     RPKI validation codes: V - valid, I - invalid, N - not-found
    
    
     Total number of routes from all PE: 2
     Route Distinguisher: 1.2.3.4:1
    
    
          Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
    
     *>i  192.168.1.1/32       1.1.1.1         0          100        0      ?
     Route Distinguisher: 2:3
    
    
          Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
    
     *>   192.168.2.1/32      4.4.4.4                               0      200?
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
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface Virtual-Template0
   ppp authentication-mode auto
  #
  bgp 65003
   peer 192.168.1.2 as-number 65535.65535
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
    route-distinguisher 1.2.3.4:1
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
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance ng
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet 0/1/3
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 65535.65535
   peer 2.2.2.2 as-number 65535.65535
   peer 2.2.2.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    network 1.1.1.1 255.255.255.255
    peer 2.2.2.2 enable
    peer 2.2.2.2 route-policy policy1 export
    peer 2.2.2.2 label-route-capability
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
  route-policy policy1 permit node 1
   apply mpls-label
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
* ABR1 configuration file
  
  ```
  #
  sysname ABR1
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
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet 0/1/3
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 65535.65535
   peer 1.1.1.1 as-number 65535.65535
   peer 1.1.1.1 connect-interface LoopBack0
   peer 3.3.3.3 as-number 65535.65535
   peer 3.3.3.3 connect-interface LoopBack0
   #  
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 1.1.1.1 route-policy policy1 export
    peer 1.1.1.1 reflect-client
    peer 1.1.1.1 next-hop-local
    peer 1.1.1.1 label-route-capability
    peer 3.3.3.3 enable
    peer 3.3.3.3 route-policy policy1 export
    peer 3.3.3.3 reflect-client
    peer 3.3.3.3 next-hop-local
    peer 3.3.3.3 label-route-capability
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
    network 10.1.1.0 0.0.0.255
    network 2.2.2.2 0.0.0.0
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  ```
* ABR2 configuration file
  
  ```
  #
  sysname ABR2
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
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet 0/1/3
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 65535.65535
   peer 2.2.2.2 as-number 65535.65535
   peer 2.2.2.2 connect-interface LoopBack0
   peer 4.4.4.4 as-number 65535.65535
   peer 4.4.4.4 connect-interface LoopBack0
   #  
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 2.2.2.2 route-policy policy1 export
    peer 2.2.2.2 reflect-client
    peer 2.2.2.2 next-hop-local
    peer 2.2.2.2 label-route-capability
    peer 4.4.4.4 enable
    peer 4.4.4.4 route-policy policy1 export
    peer 4.4.4.4 reflect-client
    peer 4.4.4.4 next-hop-local
    peer 4.4.4.4 label-route-capability
   #
   ipv4-family mvpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 4.4.4.4 enable
    peer 4.4.4.4 reflect-client
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 4.4.4.4 enable
    peer 4.4.4.4 reflect-client
  #
  ospf 2
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 3.3.3.3 0.0.0.0
  #
  route-policy policy1 permit node 1
   apply mpls-label
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
    route-distinguisher 2:3 
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     export msdp
     spt-only mode
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
  interface GigabitEthernet 0/1/3
   undo shutdown
   ip binding vpn-instance ng
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 65535.65535
   peer 3.3.3.3 as-number 65535.65535
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    network 4.4.4.4 255.255.255.255
    peer 3.3.3.3 enable
    peer 3.3.3.3 route-policy policy1 export
    peer 3.3.3.3 label-route-capability
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
  ospf 2
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 4.4.4.4 0.0.0.0
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  pim vpn-instance ng
   static-rp 192.168.2.2
   source-lifetime 60
  #
  msdp vpn-instance ng
   peer 192.168.2.1 connect-interface GigabitEthernet 0/1/3
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
   ip address 192.168.4.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface GigabitEthernet 0/1/3
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  bgp 65004
   peer 192.168.2.2 as number 65535.65535
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
   peer 192.168.2.2 connect-interface GigabitEthernet 0/1/3
  #
  return
  ```