Example for Configuring VLL-based CFM Through Sub-interfaces for QinQ VLAN Tag Termination
==========================================================================================

This section provides an example for configuring virtual leased line (VLL)-based connectivity fault management (CFM).

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361977__fig_dc_vrp_cfm_cfg_00002501), CE1's GE 0/1/0.1 and CE2's GE 0/1/0.1 are connected to PE1 and PE2, respectively. 802.1Q in 802.1Q (QinQ) is deployed on each switch so that the switch adds Tag 100 to the packets sent by the CE the switch is connected to. That is, the packets sent from the switch to the PE it is connected to carry double virtual local area network (VLAN) tags. QinQ reduces public VLAN ID resources needed. Label Distribution Protocol (LDP) VLL runs on the backbone network, and the LDP is used to establish pseudo wires (PWs). To improve network reliability, bind a sub-interface for QinQ VLAN tag termination on the attachment circuit (AC) interface of each PE to a Layer 2 virtual circuit (L2VC) interface and deploy VLL-based CFM to quickly detect faults on the VLL link between PEs.

**Figure 1** VLL-based CFM![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_cfm_cfg_00002501.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the interface mode on PE1 and PE2 to the user termination mode.
2. Configure an Interior Gateway Protocol (IGP) on the backbone network to enable communication between devices on the backbone network.
3. Enable basic Multiprotocol Label Switching (MPLS) capabilities on the backbone network and establish a label switched path (LSP).
4. Establish a remote MPLS LDP peer relationship between PEs at both ends of the PW.
5. Configure a sub-interface for QinQ VLAN tag termination on the AC interface of each PE.
6. Create an MPLS L2VC on each PE and bind the sub-interface to the L2VC.
7. Configure VLL-based CFM on each PE.
8. Enable Layer 2 forwarding and QinQ on each UPE.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface name of each PE connected to each CE
* Interface IP addresses
* L2VC IDs at both ends of the PW (must be the same)
* MPLS LSR IDs of the PEs and P
* IP address of the remote peer of each PE
* Tag value that is terminated on the sub-interface for QinQ VLAN tag termination
* MD name, MA name, MEP ID and type, and name of the interface on which the MEP resides

#### Procedure

1. Set the interface mode on each PE to the user termination mode.
   
   
   
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
   [~PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
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
   [~PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
2. Configure an IGP on the backbone network. This example uses Open Shortest Path First (OSPF).
   
   
   
   Assign IP addresses to interfaces on the PEs and P using information in [Figure 1](#EN-US_TASK_0172361977__fig_dc_vrp_cfm_cfg_00002501). After OSPF is enabled, the 32-bit loopback addresses of PE1, P, and PE2 must be advertised.
   
   # Configure PE1.
   
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] ospf
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.9 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE1-ospf-1] quit
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
   [~P] interface LoopBack 1
   ```
   ```
   [*P-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*P-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] ip address 10.1.2.1 24
   ```
   ```
   [*P-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit 
   ```
   ```
   [*P] ospf
   ```
   ```
   [*P-ospf-1] area 0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*P-ospf-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] ip address 3.3.3.9 32
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.1.2.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] ospf
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.9 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE2-ospf-1] quit
   ```
   
   After the configuration is complete, run the **display ip routing-table** command. The command output shows that an OSPF route exists between Loopback1 interfaces of PE1 and PE2.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display ip routing-table
   ```
   ```
   Route Flags: R - relied, D - download to fib
   ```
   ```
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: Public
   ```
   ```
            Destinations : 9        Routes : 9
   
   ```
   ```
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
   ```
   ```
           1.1.1.9/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
           2.2.2.9/32  OSPF   10   2           D  10.1.1.2       GigabitEthernet0/1/0
   ```
   ```
           3.3.3.9/32  OSPF   10   3           D  10.1.1.2       GigabitEthernet0/1/0
   ```
   ```
         10.1.1.0/24  Direct 0    0           D  10.1.1.1       GigabitEthernet0/1/0
   ```
   ```
         10.1.1.1/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/0
   ```
   ```
         10.1.1.2/32  Direct 0    0           D  10.1.1.2       GigabitEthernet0/1/0
   ```
   ```
         10.1.2.0/24  OSPF   10   2           D  10.1.1.2       GigabitEthernet0/1/0
   ```
   ```
         127.0.0.0/8   Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
         127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
   <PE1> ping 10.1.2.2
   ```
   ```
     PING 10.1.2.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.1.2.2: bytes=56 Sequence=1 ttl=254 time=200 ms
   ```
   ```
       Reply from 10.1.2.2: bytes=56 Sequence=2 ttl=254 time=60 ms
   ```
   ```
       Reply from 10.1.2.2: bytes=56 Sequence=3 ttl=254 time=90 ms
   ```
   ```
       Reply from 10.1.2.2: bytes=56 Sequence=4 ttl=254 time=90 ms
   ```
   ```
       Reply from 10.1.2.2: bytes=56 Sequence=5 ttl=254 time=90 ms
   
   ```
   ```
     --- 10.1.2.2 ping statistics ---
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
       round-trip min/avg/max = 60/106/200 ms
   ```
3. Enable basic MPLS functions and LDP on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] mpls lsr-id 1.1.1.9 
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
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure the P.
   
   ```
   [*P] mpls lsr-id 2.2.2.9
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls] quit
   ```
   ```
   [*P] mpls ldp
   ```
   ```
   [*P-mpls-ldp] quit
   ```
   ```
   [*P] interface gigabitethernet0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] mpls lsr-id 3.3.3.9 
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
   
   After the configurations are complete, LDP sessions are established between PE1 and the P and between PE2 and the P. Run the **display mpls ldp session** command. The command output shows that the LDP session status is **Operational**.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display mpls ldp session
   ```
   ```
   LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    ------------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
    ------------------------------------------------------------------------------
    2.2.2.9:0          Operational DU   Active   0000:03:01  726/726
    ------------------------------------------------------------------------------
    TOTAL: 1 session(s) Found.
   ```
4. Establish a remote LDP session between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] mpls ldp remote-peer 3.3.3.9
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.9] remote-ip 3.3.3.9
   ```
   ```
   [*PE1-mpls-ldp-remote-3.3.3.9] quit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] mpls ldp remote-peer 1.1.1.9
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.9] remote-ip 1.1.1.9
   ```
   ```
   [*PE2-mpls-ldp-remote-1.1.1.9] quit
   ```
   
   After the configuration is complete, run the **display mpls ldp session** command. The command output shows that an LDP session has been established between PE1 and PE2 and its state is **Operational**.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display mpls ldp session
   ```
   ```
   LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    ------------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
    ------------------------------------------------------------------------------
    2.2.2.9:0          Operational DU   Passive  0000:00:09  37/37
    3.3.3.9:0          Operational DU   Passive  0000:00:03  13/13
    ------------------------------------------------------------------------------
    TOTAL: 2 session(s) Found.
   ```
5. Enable MPLS L2VPN, create a VC, and configure a sub-interface for QinQ VLAN tag termination.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] control-vid 1 qinq-termination
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] qinq termination l2 symmetry 
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] qinq termination pe-vid 100 ce-vid 10
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] mpls l2vc 3.3.3.9 101
   ```
   ```
   [*PE1-GigabitEthernet0/2/0.1] quit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] control-vid 1 qinq-termination
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] qinq termination l2 symmetry
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] qinq termination pe-vid 100 ce-vid 10
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] mpls l2vc 1.1.1.9 101
   ```
   ```
   [*PE2-GigabitEthernet0/2/0.1] quit
   ```
6. Configure Ethernet CFM on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] cfm enable
   ```
   ```
   [*PE1] cfm version standard
   ```
   ```
   [*PE1] cfm md md1
   ```
   ```
   [*PE1-md-md1] ma ma1
   ```
   ```
   [*PE1-md-md1-ma-ma1] ccm-interval 30
   ```
   ```
   [*PE1-md-md1-ma-ma1] map mpls l2vc 101 tagged
   ```
   ```
   [*PE1-md-md1-ma-ma1] mep mep-id 1 interface gigabitethernet 0/2/0.1 pe-vid 100 ce-vid 10 inward
   ```
   ```
   [*PE1-md-md1-ma-ma1] remote-mep mep-id 2
   ```
   ```
   [*PE1-md-md1-ma-ma1] mep ccm-send mep-id 1 enable
   ```
   ```
   [*PE1-md-md1-ma-ma1] remote-mep ccm-receive mep-id 2 enable
   ```
   ```
   [*PE1-md-md1-ma-ma1] quit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] cfm enable
   ```
   ```
   [*PE2] cfm version standard
   ```
   ```
   [*PE2] cfm md md1
   ```
   ```
   [*PE2-md-md1] ma ma1
   ```
   ```
   [*PE2-md-md1-ma-ma1] ccm-interval 30
   ```
   ```
   [*PE2-md-md1-ma-ma1] map mpls l2vc 101 tagged
   ```
   ```
   [*PE2-md-md1-ma-ma1] mep mep-id 2 interface gigabitethernet 0/2/0.1 pe-vid 100 ce-vid 10 inward
   ```
   ```
   [*PE2-md-md1-ma-ma1] remote-mep mep-id 1
   ```
   ```
   [*PE2-md-md1-ma-ma1] mep ccm-send mep-id 2 enable
   ```
   ```
   [*PE2-md-md1-ma-ma1] remote-mep ccm-receive mep-id 1 enable
   ```
   ```
   [*PE2-md-md1-ma-ma1] quit
   ```
7. Enable QinQ so that each switch can send packets with double VLAN tags to the PE it is connected to.
   
   
   
   # Configure UPE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~UPE1] vlan 100
   ```
   ```
   [*UPE1-vlan100] quit
   ```
   ```
   [*UPE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*UPE1-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*UPE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*UPE1-GigabitEthernet0/1/0] port trunk allow-pass vlan 100
   ```
   ```
   [*UPE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*UPE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*UPE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*UPE1-GigabitEthernet0/1/1] port vlan-stacking vlan 10 stack-vlan 100
   ```
   ```
   [*UPE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*UPE1-GigabitEthernet0/1/1] quit
   ```
   
   # Configure UPE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~UPE2] vlan 100
   ```
   ```
   [~*UPE2-vlan100] quit
   ```
   ```
   [*UPE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [UPE2-GigabitEthernet0/1/0] port trunk allow-pass vlan 100
   ```
   ```
   [UPE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [UPE2] interface gigabitethernet 0/1/1
   ```
   ```
   [UPE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [UPE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [UPE2-GigabitEthernet0/1/1] port vlan-stacking vlan 10 stack-vlan 100
   ```
   ```
   [UPE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*UPE2-GigabitEthernet0/1/2] quit
   ```
   
   # Assign IP addresses to each CE's sub-interfaces (as shown in [Figure 1](#EN-US_TASK_0172361977__fig_dc_vrp_cfm_cfg_00002501)) so that packets sent from each CE to the switch connected to it carry a single tag.
   
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
   [~CE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 10.1.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
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
   [~CE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 10.1.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
8. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display cfm mep** and **display cfm remote-mep** commands on PE1, PE2, or PE3. The command output shows that VLL-based CFM has been established. Ethernet CFM can rapidly detect faults in the link between the PEs and notify an NMS of the faults.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display cfm mep md md1
   ```
   ```
   The total number of MEPs is : 1
   --------------------------------------------------
    MD Name            : md1
    MD Name Format     : string
    Level              : 0
    MA Name            : ma1
    MEP ID             : 1
    VLAN ID            : -- 
    VSI Name           : --
    L2VC ID            : 101 tagged 
    L2VPN Name         : --  CE ID              : --  CE Offset          : --
     L2TPV3 Tunnel Name            : --
    L2TPV3 Local Connection Name  : --
    Interface Name     : GigabitEthernet0/2/0.1
    CCM Send           : enabled
    Direction          : inward
    MAC Address        : 00e0-fc12-7880
    MEP Pe-vid         : --
    MEP Ce-vid         : --
    MEP Vid            : -- 
    Alarm Status       : none
    Alarm RDI          : enabled
    Bandwidth Receive  : false
    Bandwidth          : --
   ```
   ```
   <PE1> display cfm remote-mep md md1
   ```
   ```
   The total number of RMEPs is : 1
   The status of RMEPs : 1 up, 0 down, 0 disable
   --------------------------------------------------
    MD Name            : md1
    Level              : 0
    MA Name            : ma1
    RMEP ID            : 2
    VLAN ID            : -- 
    VSI Name           : --
    L2VC ID            : 101 tagged
    L2VPN Name         : --  CE ID              : --  CE Offset          : --
     L2TPV3 Tunnel Name            : --
    L2TPV3 Local Connection Name  : --
    MAC                : 00e0-fc12-7890
    CCM Receive        : enabled
    Trigger-If-Down    : enabled
    CFM Status         : up
    Alarm Status       : none
    Interface TLV      : --
    Port Status TLV    : --
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  ```
  ```
   sysname PE1
  ```
  ```
  #
  ```
  ```
  cfm version standard
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 1.1.1.9
  ```
  ```
   mpls
  ```
  ```
  #
  ```
  ```
   mpls l2vpn
  ```
  ```
  #
  ```
  ```
  mpls ldp remote-peer 3.3.3.9
  ```
  ```
   remote-ip 3.3.3.9
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   control-vid 1 qinq-termination
  ```
  ```
   qinq termination l2 symmetry
  ```
  ```
   qinq termination pe-vid 100 ce-vid 10
  ```
  ```
   mpls l2vc 3.3.3.9 101
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  cfm md md1
  ```
  ```
    ma ma1
  ```
  ```
     map mpls l2vc 101 tagged
  ```
  ```
     ccm-interval 30
  ```
  ```
     mep mep-id 1 interface gigabitethernet 0/2/0.1 pe-vid 100 ce-vid 10 inward
  ```
  ```
     mep ccm-send mep-id 1 enable
  ```
  ```
     remote-mep mep-id 2
  ```
  ```
     remote-mep ccm-receive mep-id 2 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 1.1.1.9 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE2 configuration file
  
  ```
  #
  ```
  ```
   sysname PE2
  ```
  ```
  #
  ```
  ```
  cfm version standard
  ```
  ```
  cfm enable
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 3.3.3.9
  ```
  ```
   mpls
  ```
  ```
  #
  ```
  ```
   mpls l2vpn
  ```
  ```
  #
  ```
  ```
  mpls ldp remote-peer 1.1.1.9
  ```
  ```
   remote-ip 1.1.1.9
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   control-vid 1 qinq-termination
  ```
  ```
   qinq termination l2 symmetry
  ```
  ```
   qinq termination pe-vid 100 ce-vid 10
  ```
  ```
   mpls l2vc 1.1.1.9 101
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 3.3.3.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  cfm md md1
  ```
  ```
    ma ma1
  ```
  ```
     map mpls l2vc 101 tagged
  ```
  ```
     ccm-interval 30
  ```
  ```
     mep mep-id 2 interface gigabitethernet 0/2/0.1 pe-vid 100 ce-vid 10 inward
  ```
  ```
     mep ccm-send mep-id 2 enable
  ```
  ```
     remote-mep mep-id 1
  ```
  ```
     remote-mep ccm-receive mep-id 1 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 3.3.3.9 0.0.0.0
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* P configuration file
  
  ```
  #
  ```
  ```
   sysname P
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 2.2.2.9
  ```
  ```
   mpls
  ```
  ```
  #
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 2.2.2.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 2.2.2.9 0.0.0.0
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE1 configuration file
  
  ```
  #
  ```
  ```
   sysname CE1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   vlan-type dot1q 10
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE2 configuration file
  
  ```
  #
  ```
  ```
   sysname CE2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   vlan-type dot1q 10
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* UPE1 configuration file
  
  ```
  #
  ```
  ```
   sysname UPE1
  ```
  ```
  #
  ```
  ```
   vlan batch 100
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   port trunk allow-pass vlan 100
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   port vlan-stacking vlan 10 stack-vlan 100
  ```
  ```
  #
  ```
  ```
  return
  ```
* UPE2 configuration file
  
  ```
  #
  ```
  ```
   sysname UPE2
  ```
  ```
  #
  ```
  ```
   vlan batch 100
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   port trunk allow-pass vlan 100
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   port vlan-stacking vlan 10 stack-vlan 100
  ```
  ```
  #
  ```
  ```
  return
  ```