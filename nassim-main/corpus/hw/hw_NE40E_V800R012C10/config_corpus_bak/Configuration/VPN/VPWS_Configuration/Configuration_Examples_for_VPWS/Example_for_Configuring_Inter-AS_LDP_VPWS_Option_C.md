Example for Configuring Inter-AS LDP VPWS Option C
==================================================

Inter-AS LDP VPWS Option C applies to scenarios where each AS requires large numbers of inter-AS PWs. In inter-AS LDP VPWS Option C, PEs in different ASs establish single-segment PWs with each other; ASBRs do not need to create or maintain PWs and therefore will not hinder network expansion.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369935__fig_dc_vrp_vpws_cfg_604701), CE1 and CE2 access the MPLS backbone network through PE1 in AS100 and PE2 in AS200, respectively.

Inter-AS LDP VPWS Option C needs to be deployed for CE1 and CE2 to communicate. In an inter-AS LDP VPWS Option C scenario, SS-PWs are established between PEs in different ASs, and ASBRs do not maintain PW information or perform PW switching.

**Figure 1** Configuring inter-AS LDP VPWS Option C![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_604701.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP on the backbone network to ensure IP connectivity within each AS.
2. Configure basic MPLS functions on the MPLS backbone network and establish a dynamic LSP between the PE and ASBR in the same AS.
3. Establish an IBGP peer relationship between the PE and ASBR in the same AS and an EBGP peer relationship between ASBRs.
4. Configure routing policies and enable label-based routing on ASBRs.
5. Establish a remote MPLS LDP peer relationship between PE1 and PE2.
6. Establish an LDP VPWS PW between PE1 and PE2.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP addresses (loopback interface IP addresses of peers)
* Data for configuring the IGP
* MPLS LSR IDs (local loopback interface IP addresses) of PEs and ASBRs
* L2VC IDs
* Route-policies used by ASBRs

#### Procedure

1. Configure interface IP addresses.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] commit
   ```
   
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
   [~PE1] interface loopback1
   ```
   ```
   [*PE1-Loopback1] ip address 1.1.1.1 32
   ```
   ```
   [*PE1-Loopback1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.10.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname ASBR1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~ASBR1] interface loopback1
   ```
   ```
   [*ASBR1-Loopback1] ip address 2.2.2.2 32
   ```
   ```
   [*ASBR1-Loopback1] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] ip address 10.10.1.2 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] ip address 10.20.1.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname ASBR2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~ASBR2] interface loopback1
   ```
   ```
   [*ASBR2-Loopback1] ip address 3.3.3.3 32
   ```
   ```
   [*ASBR2-Loopback1] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] ip address 10.20.1.2 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] ip address 10.30.1.1 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] commit
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
   [~PE2] interface loopback1
   ```
   ```
   [*PE2-Loopback1] ip address 4.4.4.4 32
   ```
   ```
   [*PE2-Loopback1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.30.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure CE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE2] interface gigabitethernet 0/1/0
   ```
   ```
   [~CE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE2] commit
   ```
2. Configure IGP on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255 
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE1-ospf-1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] ospf 1
   ```
   ```
   [*ASBR1-ospf-1] area 0.0.0.0
   ```
   ```
   [*ASBR1-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*ASBR1-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   ```
   ```
   [*ASBR1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*ASBR1-ospf-1] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [*ASBR2] ospf 1
   ```
   ```
   [*ASBR2-ospf-1] area 0.0.0.0
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] network 10.30.1.0 0.0.0.255
   ```
   ```
   [*ASBR2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*ASBR2-ospf-1] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 4.4.4.4 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.30.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE2-ospf-1] quit
   ```
   ```
   [*PE2] commit
   ```
3. Configure basic MPLS functions and establish LSPs.
   
   
   
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
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [*ASBR1] mpls lsr-id 2.2.2.2
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
   [*ASBR1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] mpls lsr-id 3.3.3.3
   ```
   ```
   [*ASBR2] mpls
   ```
   ```
   [*ASBR2-mpls] quit
   ```
   ```
   [*ASBR2] mpls ldp
   ```
   ```
   [*ASBR2-mpls-ldp] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 4.4.4.4
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
4. Enable inter-AS MPLS on ASBRs.
   
   
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] interface gigabitethernet 0/2/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] interface gigabitethernet 0/1/0
   ```
   ```
   [~ASBR2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR2] commit
   ```
5. Establish an MP-IBGP peer relationship between PE1 and ASBR1 and between PE2 and ASBR2. Configure route-policies on ASBRs, so that an ASBR allocates MPLS labels to routes received from the local PE and to be advertised to the peer ASBR and re-allocates MPLS labels to labeled IPv4 routes to be advertised to the local PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 label-route-capability
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 connect-interface LoopBack 1
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [*ASBR1] route-policy policy1 permit node 1
   ```
   ```
   [*ASBR1-route-policy] if-match mpls-label
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] route-policy policy2 permit node 1
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] network 1.1.1.1 255.255.255.255
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 route-policy policy1 export
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 label-route-capability
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*ASBR1-bgp] peer 10.20.1.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] peer 10.20.1.2 route-policy policy2 export
   ```
   ```
   [*ASBR1-bgp] peer 10.20.1.2 label-route-capability
   ```
   ```
   [*ASBR1-bgp] peer 10.20.1.2 connect-interface gigabitethernet 0/2/0
   ```
   ```
   [*ASBR1-bgp]quit
   ```
   ```
   [*ASBR1]commit
   ```
   
   # Configure ASBR2.
   
   ```
   [*ASBR2] route-policy policy1 permit node 1
   ```
   ```
   [*ASBR2-route-policy] if-match mpls-label
   ```
   ```
   [*ASBR2-route-policy] apply mpls-label
   ```
   ```
   [*ASBR2-route-policy] quit
   ```
   ```
   [*ASBR2] route-policy policy2 permit node 1
   ```
   ```
   [*ASBR2-route-policy] apply mpls-label
   ```
   ```
   [*ASBR2-route-policy] quit
   ```
   ```
   [*ASBR2] bgp 200
   ```
   ```
   [*ASBR2-bgp] network 4.4.4.4 32
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 as-number 200
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 route-policy policy1 export
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 label-route-capability
   ```
   ```
   [*ASBR2-bgp] peer 4.4.4.4 connect-interface loopback 1
   ```
   ```
   [*ASBR2-bgp] peer 10.20.1.1 as-number 100
   ```
   ```
   [*ASBR2-bgp] peer 10.20.1.1 route-policy policy2 export
   ```
   ```
   [*ASBR2-bgp] peer 10.20.1.1 label-route-capability
   ```
   ```
   [*ASBR2-bgp] peer 10.20.1.1 connect-interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR2-bgp] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 as-number 200
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 label-route-capability
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After completing the configurations, run the [**display bgp peer**](cmdqueryname=display+bgp+peer) command on ASBR1 or ASBR2. The command output shows that the status of the IBGP session between the PE and ASBR in the same AS is **Established**, and the status of the EBGP session between ASBRs is also **Established**. The following example uses the command output on ASBR1.
   
   ```
   [~ASBR1] display bgp peer
   ```
   ```
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
    Peer           V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
    1.1.1.1        4   100      111      128     0 00:34:24 Established       0
    10.20.1.2      4   200       75       89     0 00:38:40 Established       1
   ```
   
   Run the **display tunnel-info all** command on ASBR1 or ASBR2. The command output shows that a tunnel with the type being **mpls local ifnet** has been established. The following example uses the command output on ASBR1.
   
   ```
   [~ASBR1] display tunnel-info all
   ```
   ```
   Tunnel ID                     Type                Destination         Status
   -----------------------------------------------------------------------------
   0x0000000001004c4b42          ldp                 1.1.1.1             UP  
   0x000000000c00030000          mpls local ifnet    10.20.1.2           UP 
   ```
   
   After the configuration is complete, run the **display tunnel-info all** command on PEs. The command output shows that inter-AS tunnels have been established. The following example uses the command output on PE1.
   
   ```
   [~PE1] display tunnel-info all
   ```
   ```
   Tunnel ID                     Type                Destination         Status
   -----------------------------------------------------------------------------
   0x0000000001004c8b42          ldp                 2.2.2.2             UP  
   0x000000000201040000          bgp                 4.4.4.4             UP 
   ```
6. Establish a remote MPLS LDP session between PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp remote-peer 4.4.4.4
   ```
   ```
   [*PE1-mpls-ldp-remote-4.4.4.4] remote-ip 4.4.4.4
   ```
   ```
   [*PE1-mpls-ldp-remote-4.4.4.4] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls ldp remote-peer 1.1.1.1
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After completing the configurations, run the **display mpls ldp session** command on PE1 or PE2. The command output shows that an LDP session has been established between PE1 and PE2 and **Status** is **Operational**.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    ------------------------------------------------------------------------------
    PeerID             Status       LAM  SsnRole  SsnAge      KASent/Rcv
    ------------------------------------------------------------------------------
    2.2.2.2:0          Operational  DU   Passive  000:00:21   87/87
    4.4.4.4:0          Operational DU   Passive  000:00:18   75/75
    ------------------------------------------------------------------------------
    TOTAL: 2 session(s) Found.
   ```
7. Configure an LDP VPWS PW between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls l2vc 4.4.4.4 100
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls l2vc 1.1.1.1 100
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
8. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) command on PE1 or PE2. The command output shows that a PW has been established and **VC state** is **up**. The following example uses the command output on PE1.
   
   ```
   <~PE1> display mpls l2vc interface gigabitethernet 0/1/0
   ```
   ```
   *client interface       : GigabitEthernet0/1/0 is up
    Administrator PW             : no
    session state                : up
    AC status                    : up
    VC state                     : up
    Label state                  : 0
    Token state                  : 0
    VC ID                        : 100
    VC type                      : VLAN
    destination                  : 4.4.4.4
    local group ID               : 0         remote group ID      : 0
    local VC label               : 18        remote VC label      : 18
    local AC OAM State           : up
    local PSN OAM State          : up
    local forwarding state       : forwarding
    local status code            : 0x0 (forwarding)
    remote AC OAM State          : up
    remote PSN OAM state         : up
    remote forwarding state      : forwarding
    remote status code           : 0x0 (forwarding)
    ignore standby state         : no
    Dynamic BFD for PW           : enable
    Detect Multiplier             : 3
    Min Transit Interval         : 1000
    Min Receive Interval         : 1000
    Dynamic BFD Session          : built
    BFD for PW                   : available
    BFD sessionIndex             : --  
    BFD state                    : up
    VCCV State                   : --
    manual fault                 : not set
    active state                 : active
    forwarding entry             : exist
    OAM Protocol                 : --
    OAM Status                   : --
    OAM Fault Type               : --
    PW APS ID                    : --
    PW APS Status                : --
    TTL Value                    : 1
    link state                   : up
    local VC MTU                 : 1500      remote VC MTU        : 1500
    local VCCV                   : alert ttl lsp-ping bfd
    remote VCCV                  : alert ttl lsp-ping bfd
    local control word           : disable   remote control word  : disable
    tunnel policy name           : --
    PW template name             : --
    primary or secondary         : primary
    load balance type            : flow
    Access-port                  : false
    Switchover Flag              : false
    VC tunnel info               : 1 tunnels
       NO.0 TNL type             : ldp, TNL ID : 0x0000000001004c4b43
    create time                  : 0 days, 1 hours, 2 minutes, 56 seconds
    up time                      : 0 days, 1 hours, 1 minutes, 48 seconds
    last change time             : 0 days, 1 hours, 1 minutes, 48 seconds
    VC last up time              : 2012/12/05 02:50:41
    VC total up time             : 0 days, 1 hours, 1 minutes, 48 seconds
    CKey                         : 1
    NKey                         : 1493172332
    L2VPN QoS CIR value          : 3888
    L2VPN QoS PIR value          : 3888
    L2VPN QoS qos-profile name   : --
    PW redundancy mode           : frr
    AdminPw interface            : --
    AdminPw link state           : --
    Forward state                : send inactive, receive inactive 
    Diffserv Mode                : uniform
    Service Class                : --
    Color                        : --
    DomainId                     : --
    Domain Name                  : --
   ```
   
   CE1 and CE2 can ping each other. The following example uses the command output on CE1.
   
   ```
   [~CE1] ping 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=430 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=220 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=190 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=190 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=190 ms
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 190/244/430 ms
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
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  mpls ldp remote-peer 4.4.4.4
   remote-ip 4.4.4.4
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   mpls l2vc 4.4.4.4 100
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100         
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 ebgp-max-hop 255
   peer 4.4.4.4 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 2.2.2.2 label-route-capability  
    peer 4.4.4.4 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.10.1.0 0.0.0.255
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
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.20.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 10.20.1.2 as-number 200
   peer 10.20.1.2 connect-interface GigabitEthernet0/2/0
  #
  ipv4-family unicast
   undo synchronization
   network 1.1.1.1 255.255.255.255
   peer 1.1.1.1 enable
   peer 1.1.1.1 route-policy policy1 export
   peer 1.1.1.1 label-route-capability
   peer 10.20.1.2 enable
   peer 10.20.1.2 route-policy policy2 export
   peer 10.20.1.2 label-route-capability
  #
  route-policy policy1 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  route-policy policy2 permit node 1
   apply mpls-label
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.10.1.0 0.0.0.255
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
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.20.1.2 255.255.255.0
   mpls
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.30.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 200
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack1
   peer 10.20.1.1 as-number 100
   peer 10.20.1.1 connect-interface GigabitEthernet0/1/0
  #
  ipv4-family unicast
   undo synchronization
   network 4.4.4.4 255.255.255.255
   peer 4.4.4.4 enable
   peer 4.4.4.4 route-policy policy1 export
   peer 4.4.4.4 label-route-capability
   peer 10.20.1.1 enable
   peer 10.20.1.1 route-policy policy2 export
   peer 10.20.1.1 label-route-capability
  #
  route-policy policy1 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  route-policy policy2 permit node 1
   apply mpls-label
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.30.1.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  mpls ldp remote-peer 1.1.1.1
   remote-ip 1.1.1.1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.30.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   mpls l2vc 1.1.1.1 100
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 200         
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 ebgp-max-hop 255
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 3.3.3.3 label-route-capability  
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.30.1.0 0.0.0.255
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
   ip address 10.1.1.2 255.255.255.0
  #
  return
  ```