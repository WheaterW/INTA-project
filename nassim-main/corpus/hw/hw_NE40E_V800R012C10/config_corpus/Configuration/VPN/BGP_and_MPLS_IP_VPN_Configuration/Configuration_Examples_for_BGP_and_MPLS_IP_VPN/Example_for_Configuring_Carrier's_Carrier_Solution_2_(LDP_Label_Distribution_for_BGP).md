Example for Configuring Carrier's Carrier Solution 2 (LDP Label Distribution for BGP)
=====================================================================================

If a Level 1 carrier and Level 2 carriers belong to different ASs and no MP-IBGP peer relationships are established between the Level 1 carrier CEs and Level 2 carrier PEs, you can configure LDP to distribute labels to BGP routes so that the Level 2 carriers can provide BGP/MPLS IP VPN services.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172369532__fig_dc_vrp_mpls-l3vpn-v4_cfg_204401), the Level 1 carrier and Level 2 carrier are in the different ASs, and the Level 2 carrier provides BGP/MPLS IP VPN services for its clients.

After learning the labeled BGP routes of the public network from the Level 1 carrier's devices, the Level 2 carrier imports these routes to the IGP routing table. In this manner, LDP can distribute labels for these routes, and establish a complete LDP LSP between the Level 2 carrier PEs. The solution of inter-AS carrier's carrier can then be realized.

**Figure 1** Carrier's carrier solution 2![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_204401.png)

#### Deployment Roadmap

The configuration roadmap is as follows:

1. The two types of routes are exchanged as follows:
   
   * Exchange of the internal routes of the Level 2 carrier on the backbone network of Level 1 carrier: Configure the Level 2 carrier to access the Level 1 carrier as the Level 1 carrier CE.
   * Exchange of the external routes of the Level 2 carrier between Level 2 carrier PEs: Set up an MP-EBGP peer relationship between Level 2 carrier PEs (PE3 and PE4).
2. Carrier's carrier is configured across different ASs. In this case, the Level 1 carrier PEs and CEs are in different ASs. To distribute labels for the routes exchanged between PEs and CEs, the labeled MP-EBGP peer relationship needs to be established between CEs and PEs.
3. On the Level 1 carrier CE, import BGP routes to the IGP routing table.
4. On the Level 1 carrier CE, configure LDP to distribute labels to the labeled BGP routes of the public network.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the Level 1 carrier PEs and CEs and Level 2 carrier PEs
* Data required for configuring IGP
* Name, RD, and VPN target of the VPN instance created on the PEs
* Two route-policies on the Level 1 carrier CEs

#### Procedure

1. Configure BGP/MPLS IP VPN on the Level 1 carrier backbone network and configure IS-IS as IGP of the backbone network. Enable LDP between PE1 and PE2, and establish an MP-IBGP peer relationship.
   
   
   
   # Configure PE1.
   
   ```
   <~HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface loopback 1
   [*PE1-LoopBack1] ip address 3.3.3.9 32
   [*PE1-LoopBack1] quit
   [*PE1] mpls lsr-id 3.3.3.9
   [*PE1] mpls
   [*PE1-mpls] quit
   [*PE1] mpls ldp
   [*PE1-mpls-ldp] quit
   [*PE1] isis 1
   [*PE1-isis-1] network-entity 10.0000.0000.0004.00
   [*PE1-isis-1] quit
   [*PE1] interface loopback 1
   [*PE1-LoopBack1] isis enable 1
   [*PE1-LoopBack1] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-Gigabitethernet0/2/0] ip address 30.1.1.1 24
   [*PE1-Gigabitethernet0/2/0] isis enable 1
   [*PE1-Gigabitethernet0/2/0] mpls
   [*PE1-Gigabitethernet0/2/0] mpls ldp
   [*PE1-Gigabitethernet0/2/0] quit
   [*PE1] bgp 100
   [*PE1-bgp] peer 4.4.4.9 as-number 100
   [*PE1-bgp] peer 4.4.4.9 connect-interface loopback 1
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 4.4.4.9 enable
   [*PE1-bgp-af-vpnv4] commit
   [~PE1-bgp-af-vpnv4] quit
   [~PE1-bgp] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of PE2 is similar to that of PE1. For configuration details, see the configuration file.
   
   After PE1 and PE2 are configured, run the **display mpls ldp session** command on either of them. The command output shows that the LDP session has been set up successfully. Run the **display bgp peer** command on either of them. The command output shows that the BGP peer relationship has been established. Run the **display isis peer** command on either of them. The command output shows that the IS-IS neighbor relationship is **Up**.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls ldp session
   
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    ----------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
    ----------------------------------------------------------------
    4.4.4.9:0          Operational DU   Active   0000:00:01  8/8
    ----------------------------------------------------------------
    TOTAL: 1 session(s) Found
   
   
   ```
   ```
   [~PE1] display bgp peer
   
    BGP local router ID : 3.3.3.9
    Local AS number : 100
    Total number of peers : 1          Peers in established state : 1
   
     Peer        V   AS  MsgRcvd  MsgSent  OutQ  Up/Down    State         PrefRcv
     4.4.4.9     4   100    7        8        0  00:02:47   Established   0
   ```
   ```
   [~PE1] display isis peer
   ```
   ```
                             Peer information for ISIS (1)
   
     System Id     Interface          Circuit Id       State HoldTime Type     PRI
   -------------------------------------------------------------------------------
   0000.0000.0005 Gigabitethernet 0000.0000.0005.01 Up 7s L1 (L1L2) 64
   0000.0000.0005 Gigabitethernet 0000.0000.0005.01 Up 7s L2 (L1L2) 64
   
   Total Peer(s): 2
   ```
2. Configure the Level 2 carrier network. Specifically, use OSPF as IGP and enable LDP between PE3 and CE1 and between PE4 and CE2.
   
   
   
   # Configure PE3.
   
   ```
   <~HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE3] interface loopback 1
   ```
   ```
   [*PE3-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*PE3-LoopBack1] quit
   ```
   ```
   [*PE3] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE3] mpls
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] mpls ldp
   ```
   ```
   [*PE3-mpls-ldp] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip address 40.1.1.1 24
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [~PE3] ospf 1
   ```
   ```
   [*PE3-ospf-1] area 0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 40.1.1.0 0.0.0.255
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 1.1.1.9 0.0.0.0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE3-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE3-ospf-1] quit
   ```
   
   # Configure CE1.
   
   ```
   <~HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*CE1-LoopBack1] quit
   ```
   ```
   [*CE1] mpls lsr-id 2.2.2.9
   ```
   ```
   [*CE1] mpls
   ```
   ```
   [*CE1-mpls] quit
   ```
   ```
   [*CE1] mpls ldp
   ```
   ```
   [*CE1-mpls-ldp] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE1-Gigabitethernet0/1/0] ip address 40.1.1.2 24
   ```
   ```
   [*CE1-Gigabitethernet0/1/0] mpls
   ```
   ```
   [*CE1-Gigabitethernet0/1/0] mpls ldp
   ```
   ```
   [*CE1-Gigabitethernet0/1/0] commit
   ```
   ```
   [~CE1-Gigabitethernet0/1/0] quit
   ```
   ```
   [~CE1] ospf 1
   ```
   ```
   [*CE1-ospf-1] area 0
   ```
   ```
   [*CE1-ospf-1-area-0.0.0.0] network 40.1.1.0 0.0.0.255
   ```
   ```
   [*CE1-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
   ```
   ```
   [*CE1-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~CE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~CE1-ospf-1] quit
   ```
   
   After the configurations are complete, PE3 and CE1 can establish an LDP peer relationship and an OSPF neighbor relationship.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of the connection between PE4 and CE2 is similar to that of the connection between PE3 and CE1. For configuration details, see the configuration files.
3. Configure the Level 1 carrier CE to access the Level 1 carrier PE. Configure the exchange of labeled IPv4 routes between them.
   
   
   
   # Configure CE1 to exchange labeled IPv4 routes with PE1.
   
   ```
   <~CE1> system-view
   ```
   ```
   [~CE1] interface gigabitethernet 0/2/0
   [*CE1-Gigabitethernet0/2/0] ip address 11.1.1.1 24
   [*CE1-Gigabitethernet0/2/0] mpls
   [*CE1-Gigabitethernet0/2/0] quit
   [*CE1] route-policy policy1 permit node 1
   [*CE1-route-policy] apply mpls-label
   [*CE1-route-policy] quit
   [*CE1] bgp 200
   [*CE1-bgp] peer 11.1.1.2 as-number 100
   [*CE1-bgp] peer 11.1.1.2 route-policy policy1 export
   [*CE1-bgp] peer 11.1.1.2 label-route-capability
   [*CE1-bgp] import-route ospf 1
   [*CE1-bgp] commit
   [~CE1-bgp] quit
   [~CE1] ospf 1
   [*CE1-ospf-1] area 0
   [*CE1-ospf-1-area-0.0.0.0] network 11.1.1.0 0.0.0.255
   [*CE1-ospf-1-area-0.0.0.0] commit
   [~CE1-ospf-1-area-0.0.0.0] quit
   [~CE1-ospf-1] quit
   ```
   
   # Configure PE1 to exchange labeled IPv4 routes with CE1.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To ensure normal forwarding, configure only the per-route per-label mode in a VPN instance.
   
   ```
   <~PE1> system-view
   ```
   ```
   [~PE1] ip vpn-instance vpn1
   [*PE1-vpn-instance-vpn1] ipv4-family
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 200:1
   [*PE1-vpn-instance-vpn1-af-ipv4] apply-label per-route
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-Gigabitethernet0/1/0] ip binding vpn-instance vpn1
   [*PE1-Gigabitethernet0/1/0] ip address 11.1.1.2 24
   [*PE1-Gigabitethernet0/1/0] mpls
   [*PE1-Gigabitethernet0/1/0] quit
   [*PE1] route-policy policy1 permit node 1
   [*PE1-route-policy] apply mpls-label
   [*PE1-route-policy] quit
   [*PE1] bgp 100
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   [*PE1-bgp-vpn1] peer 11.1.1.1 as-number 200
   [*PE1-bgp-vpn1] peer 11.1.1.1 route-policy policy1 export
   [*PE1-bgp-vpn1] peer 11.1.1.1 label-route-capability
   [*PE1-bgp-vpn1] import-route direct
   [*PE1-bgp-vpn1] commit
   [~PE1-bgp-vpn1] quit
   [~PE1-bgp] quit
   ```
   
   After the configuration, the BGP peer relationship is set up between CE1 and PE1, and between CE2 and PE2.
   
   ```
   [~CE1] display bgp peer
   
    BGP local router ID : 2.2.2.9
    Local AS number : 200
    Total number of peers : 1                 Peers in established state : 1
   
     Peer         V   AS   MsgRcvd  MsgSent  OutQ  Up/Down    State        PrefRcv
     11.1.1.2     4   100     210      225     0   03:31:49   Established      7
   
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of the connection between CE2 and PE2 is similar to that between CE1 and PE1. For configuration details, see the configuration files.
4. On the Level 1 carrier CE, import BGP routes to the IGP routing table.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] ospf 1
   [*CE1-ospf-1] import-route bgp
   [*CE1-ospf-1] commit
   [~CE1-ospf-1] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] ospf 1
   [*CE2-ospf-1] import-route bgp
   [*CE2-ospf-1] commit
   [~CE2-ospf-1] quit
   ```
   
   After completing the configurations, run the **display ip routing-table** command on PE3 and PE4. The command output shows that the PEs can learn routes destined for each other.
   
   The following example uses the command output on PE3.
   
   ```
   [~PE3] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 12       Routes : 12
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
       1.1.1.9/32      Direct 0    0           D  127.0.0.1       LoopBack1
       2.2.2.9/32      OSPF   10   1           D   40.1.1.2       Gigabitethernet0/2/0
       5.5.5.9/32      O_ASE  150  1           D   40.1.1.2       Gigabitethernet0/2/0
       6.6.6.9/32      O_ASE  150  1           D   40.1.1.2       Gigabitethernet0/2/0
      11.1.1.0/32      OSPF   10   2           D   40.1.1.2       Gigabitethernet0/2/0
      40.1.1.0/24      Direct 0    0           D   40.1.1.1       Gigabitethernet0/2/0
      40.1.1.1/32      Direct 0    0           D  127.0.0.1       Gigabitethernet0/2/0
      40.1.1.2/32      Direct 0    0           D   40.1.1.2       Gigabitethernet0/2/0
      20.1.1.0/24      O_ASE  150  1           D   40.1.1.2       Gigabitethernet0/2/0
      21.1.1.0/24      O_ASE  150  1           D   40.1.1.2       Gigabitethernet0/2/0
      21.1.1.2/32      OSPF   10   5           D   40.1.1.2       Gigabitethernet0/2/0
     127.0.0.0/8       Direct 0    0           D  127.0.0.1       InLoopBack0
     127.0.0.1/32      Direct 0    0           D  127.0.0.1       InLoopBack0
   
   ```
5. On the Level 1 carrier CE, configure LDP to distribute labels to the labeled BGP routes of the public network.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] mpls
   [*CE1-mpls] lsp-trigger bgp-label-route
   [*CE1-mpls] commit
   [~CE1-mpls] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] mpls
   [*CE2-mpls] lsp-trigger bgp-label-route
   [*CE2-mpls] commit
   [~CE2-mpls] quit
   ```
   
   After the configuration, run the **display ip routing-table** *dest-ip-address* **verbose** command on PE1. The command output shows that the routes from CE1 to PE4 are labeled BGP routes of the public network: The routing table is **Public**, the protocol type is **BGP**, and the label has a non-zero value.
   
   The following example uses the command output on CE1.
   
   ```
   [~CE1] display ip routing-table 6.6.6.9 verbose
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : Public
   Summary Count : 1
   
   Destination: 6.6.6.9/32
        Protocol: EBGP            Process ID: 0
      Preference: 255                   Cost: 0
         NextHop: 11.1.1.2         Neighbour: 11.1.1.2
           State: Active Adv             Age: 00h38m36s
             Tag: 0                 Priority: low
           Label: 3079               QoSInfo: 0x0
      IndirectID: 0x0
    RelayNextHop: 0.0.0.0          Interface: Gigabitethernet0/2/0
        TunnelID: 0x1408007            Flags:  D 
   
   ```
   ```
      IndirectID: 0x0  
   ```
   ```
    RelayNextHop: 0.0.0.0          Interface: Gigabitethernet0/2/0
        TunnelID: 0x6002006            Flags: D
   ```
   
   Run the **display mpls lsp protocol ldp include** *dest-ip-address mask-length* **verbose** command on CE1 and PE4. The command output shows that an LDP egress LSP and an LDP ingress LSP are established on CE1 and PE4, respectively.
   
   ```
   [~CE1] display mpls lsp protocol ldp include 6.6.6.9 32 verbose
   ----------------------------------------------------------------------
                    LSP Information: LDP LSP
   ----------------------------------------------------------------------
     No                  :  1
     VrfIndex            :
     Fec                 :  6.6.6.9/32
     Nexthop             :  11.1.1.2
     In-Label            :  1027
     Out-Label           :  NULL
     In-Interface        :  ----------
     Out-Interface       :  ----------
     LspIndex            :  10247
     Token               :  0x0
     FrrToken            :  0x0
     LsrType             :  Egress
     Outgoing token      :  0x6002006
     Label Operation     :  POPGO
     Mpls-Mtu            :  ------
     TimeStamp           :  6130sec
     Bfd-State           :  ---
     BGPKey              :  ---
   [PE4] display mpls lsp protocol ldp include 2.2.2.9 32 verbose
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
     No                  :  1
     VrfIndex            :
     Fec                 :  2.2.2.9/32
     Nexthop             :  20.1.1.1
     In-Label            :  NULL
     Out-Label           :  1024
     In-Interface        :  ----------
     Out-Interface       :  Gigabitethernet0/2/0
     LspIndex            :  123904
     Token               :  0x100800f
     FrrToken            :  0x0
     LsrType             :  Ingress
     Outgoing token      :  0x0
     Label Operation     :  PUSH
     Mpls-Mtu            :  1500
     TimeStamp           :  105sec
     Bfd-State           :  ---
     BGPKey              :  ---
   
     No                  :  2
     VrfIndex            :
     Fec                 :  2.2.2.9/32
     Nexthop             :  20.1.1.1
     In-Label            :  1024
     Out-Label           :  1024
     In-Interface        :  ----------
     Out-Interface       :  Gigabitethernet0/2/0
     LspIndex            :  123905
     Token               :  0x1008010
     FrrToken            :  0x0
     LsrType             :  Transit
     Outgoing token      :  0x0
     Label Operation     :  SWAP
     Mpls-Mtu            :  1500
     TimeStamp           :  105sec
     Bfd-State           :  --- 
     BGPKey              :  ---
   
   ```
6. Establish an MP-EBGP peer relationship between the Level 2 carrier PEs to exchange VPN routes of the Level 2 carrier's customers.
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 200
   [*PE3-bgp] peer 6.6.6.9 as-number 300
   [*PE3-bgp] peer 6.6.6.9 connect-interface loopback 1
   [*PE3-bgp] peer 6.6.6.9 ebgp-max-hop 10
   [*PE3-bgp] ipv4-family vpnv4
   [*PE3-bgp-af-vpnv4] peer 6.6.6.9 enable
   [*PE3-bgp-af-vpnv4] commit
   [~PE3-bgp-af-vpnv4] quit
   [~PE3-bgp] quit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] bgp 300
   [*PE4-bgp] peer 1.1.1.9 as-number 200
   [*PE4-bgp] peer 1.1.1.9 connect-interface loopback 1
   [*PE4-bgp] peer 1.1.1.9 ebgp-max-hop 10
   [*PE4-bgp] ipv4-family vpnv4
   [*PE4-bgp-af-vpnv4] peer 1.1.1.9 enable
   [*PE4-bgp-af-vpnv4] commit
   [~PE4-bgp-af-vpnv4] quit
   [~PE4-bgp] quit
   ```
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command on PE3 and PE4. The command output shows that the BGP peer relationship between the PEs of the Level 2 carriers has been established. The following example uses the command output on PE3.
   
   ```
   [~PE3] display bgp vpnv4 all peer
   
    BGP local router ID : 1.1.1.9
    Local AS number : 200
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
   
     6.6.6.9         4         300        4        6     0 00:02:19 Established   2
   
     Peer of IPv4-family for vpn instance :
    VPN-Instance vpn1, Router ID 1.1.1.9:
     172.16.1.1      4       65410       84       79     0 01:02:32 Established   3
   
   ```
7. Configure the Level 2 carrier's customers to access the Level 2 carrier PE.
   
   
   
   # Configure CE3.
   
   ```
   [~CE3] interface gigabitethernet 0/1/0
   [*CE3-GigabitEthernet0/1/0] ip address 172.16.1.1 24
   [*CE3-GigabitEthernet0/1/0] quit
   [*CE3] bgp 65410
   [*CE3-bgp] peer 172.16.1.2 as-number 200
   [*CE3-bgp] import-route direct
   [*CE3-bgp] commit
   [~CE3-bgp] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance vpn1
   [*PE3-vpn-instance-vpn1] ipv4-family
   [*PE3-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   [*PE3-vpn-instance-vpn1-af-ipv4] apply-label per-route
   [*PE3-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   [*PE3-vpn-instance-vpn1-af-ipv4] quit
   [*PE3-vpn-instance-vpn1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/1/0
   [*PE3-GigabitEthernet0/1/0] ip binding vpn-instance vpn1
   [*PE3-GigabitEthernet0/1/0] ip address 172.16.1.2 24
   [*PE3-GigabitEthernet0/1/0] quit
   [*PE3] bgp 200
   [*PE3-bgp] ipv4-family vpn-instance vpn1
   [*PE3-bgp-vpn1] peer 172.16.1.1 as-number 65410
   [*PE3-bgp-vpn1] import-route direct
   [*PE3-bgp-vpn1] commit
   [~PE3-bgp-vpn1] quit
   [~PE3-bgp] quit
   ```
   
   After the configurations are complete, a BGP peer relationship is set up between CE3 and PE3, and the status is **Established**.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of the connection between PE4 and CE4 is similar to that of the connection between PE3 and CE3. For configuration details, see the configuration files.
8. Verify the configuration.
   
   
   
   After completing all configurations, run the **display ip routing-table** command on PE1 and PE2. The command output shows that only routes from the Level 1 carrier's network exist in the public routing tables on PE1 and PE2. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 7        Routes : 7
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
       3.3.3.9/32      Direct 0    0           D  127.0.0.1       LoopBack1
       4.4.4.9/32      ISIS   15   10          D   30.1.1.2       Gigabitethernet0/2/0
      30.1.1.0/24      Direct 0    0           D   30.1.1.1       Gigabitethernet0/2/0
      30.1.1.1/32      Direct 0    0           D  127.0.0.1       Gigabitethernet0/2/0
      30.1.1.2/32      Direct 0    0           D   30.1.1.2       Gigabitethernet0/2/0
     127.0.0.0/8       Direct 0    0           D  127.0.0.1       InLoopBack0
     127.0.0.1/32      Direct 0    0           D  127.0.0.1       InLoopBack0
   
   ```
   
   Run the **display ip routing-table vpn-instance** command on PE1 and PE2. The command output shows that the Level 2 carriers' internal routes instead of the Level 2 carriers' external routes exist in the VPN instances of PE1 and PE2. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpn1
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: vpn1
            Destinations : 11       Routes : 11
   Destination/Mask    Proto  Pre  Cost     Flags  NextHop         Interface
       1.1.1.9/32      EBGP   255  10          D   11.1.1.1        Gigabitethernet0/1/0
       2.2.2.9/32      EBGP   255  0           D   11.1.1.1        Gigabitethernet0/1/0
       5.5.5.9/32      IBGP   255  0           RD   4.4.4.9        Gigabitethernet0/2/0
       6.6.6.9/32      IBGP   255  10          RD   4.4.4.9        Gigabitethernet0/2/0
      40.1.1.0/24      EBGP   255  0           D   11.1.1.1        Gigabitethernet0/1/0
      11.1.1.0/24      Direct 0    0           D   11.1.1.2        Gigabitethernet0/1/0
      11.1.1.1/32      Direct 0    0           D   11.1.1.1        Gigabitethernet0/1/0
      11.1.1.2/32      Direct 0    0           D  127.0.0.1        Gigabitethernet0/1/0
      20.1.1.0/24      IBGP   255  0           RD   4.4.4.9        Gigabitethernet0/2/0
      21.1.1.0/24      IBGP   255  0           RD   4.4.4.9        Gigabitethernet0/2/0
      21.1.1.2/32      IBGP   255  0           RD   4.4.4.9        Gigabitethernet0/2/0
   ```
   
   Run the **display ip routing-table** command on CE1 and CE2. The command output shows that the Level 2 carriers' internal routes instead of the Level 2 carriers' external routes exist in the public routing tables of CE1 and CE2. The following example uses the command output on CE1.
   
   ```
   [~CE1] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 15       Routes : 15
   Destination/Mask    Proto  Pre  Cost     Flags  NextHop         Interface
       1.1.1.9/32      OSPF   10   1           D   40.1.1.1        Gigabitethernet0/1/0
       2.2.2.9/32      Direct 0    0           D  127.0.0.1        LoopBack1
       5.5.5.9/32      EBGP   255  0           D   11.1.1.2        Gigabitethernet0/2/0
       6.6.6.9/32      EBGP   255  0           D   11.1.1.2        Gigabitethernet0/2/0
      40.1.1.0/24      Direct 0    0           D   40.1.1.2        Gigabitethernet0/1/0
      40.1.1.1/32      Direct 0    0           D   40.1.1.1        Gigabitethernet0/1/0
      40.1.1.2/32      Direct 0    0           D  127.0.0.1        Gigabitethernet0/1/0
      11.1.1.0/24      Direct 0    0           D   11.1.1.1        Gigabitethernet0/2/0
      11.1.1.1/32      Direct 0    0           D  127.0.0.1        Gigabitethernet0/2/0
      11.1.1.2/32      Direct 0    0           D   11.1.1.2        Gigabitethernet0/2/0
      20.1.1.0/24      EBGP   255  0           D   11.1.1.2        Gigabitethernet0/2/0
      21.1.1.0/24      EBGP   255  0           D   11.1.1.2        Gigabitethernet0/2/0
      21.1.1.2/32      EBGP   255  0           D   11.1.1.2        Gigabitethernet0/2/0
     127.0.0.0/8       Direct 0    0           D  127.0.0.1        InLoopBack0
     127.0.0.1/32      Direct 0    0           D  127.0.0.1        InLoopBack0
   ```
   
   Run the **display ip routing-table vpn-instance** command on PE3 and PE4. The command output shows that the Level 2 carriers' external routes exist in the VPN instances of PE3 and PE4. The following example uses the command output on PE3.
   
   ```
   [~PE3] display ip routing-table vpn-instance vpn1
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: vpn1
            Destinations : 3        Routes : 3
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
     172.16.1.0/24     Direct 0    0           D  172.16.1.2      GigabitEthernet0/1/0
     172.16.1.2/32     Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/0
     172.16.2.0/24     EBGP   255  0           RD   6.6.6.9       Gigabitethernet0/2/0
   ```
   
   PE3 and PE4 can ping each other.
   
   ```
   [~PE3] ping 20.1.1.2
     PING 20.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 20.1.1.2: bytes=56 Sequence=1 ttl=251 time=116 ms
       Reply from 20.1.1.2: bytes=56 Sequence=2 ttl=251 time=92 ms
       Reply from 20.1.1.2: bytes=56 Sequence=3 ttl=251 time=118 ms
       Reply from 20.1.1.2: bytes=56 Sequence=4 ttl=251 time=103 ms
       Reply from 20.1.1.2: bytes=56 Sequence=5 ttl=251 time=121 ms
     --- 20.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 92/110/121 ms
   ```
   
   CE3 and CE4 can ping each other.
   
   ```
   [~CE3] ping 172.16.2.1
     PING 172.16.2.1: 56  data bytes, press CTRL_C to break
       Reply from 172.16.2.1: bytes=56 Sequence=1 ttl=251 time=65 ms
       Reply from 172.16.2.1: bytes=56 Sequence=2 ttl=251 time=114 ms
       Reply from 172.16.2.1: bytes=56 Sequence=3 ttl=251 time=80 ms
       Reply from 172.16.2.1: bytes=56 Sequence=4 ttl=251 time=88 ms
       Reply from 172.16.2.1: bytes=56 Sequence=5 ttl=251 time=105 ms
     --- 172.16.2.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
   round-trip min/avg/max = 65/90/114 ms
   ```

#### Configuration Files

* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
  #
  bgp 65410
   peer 172.16.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 172.16.1.2 enable
  #
  Return
  
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-route
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 172.16.1.2 255.255.255.0
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 40.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  bgp 200
   peer 6.6.6.9 as-number 300
   peer 6.6.6.9 ebgp-max-hop 10
   peer 6.6.6.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 6.6.6.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 6.6.6.9 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    peer 172.16.1.1 as-number 65410
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 40.1.1.0 0.0.0.255
  #
  return
  
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  mpls lsr-id 2.2.2.9
   mpls
    lsp-trigger bgp-label-route
  #
  mpls ldp
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 40.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 11.1.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  bgp 200
   peer 11.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route ospf 1
    peer 11.1.1.2 enable
    peer 11.1.1.2 route-policy policy1 export
    peer 11.1.1.2 label-route-capability
  #
  ospf 1
   import-route bgp
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 40.1.1.0 0.0.0.255
    network 11.1.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:1
    apply-label per-route
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 11.1.1.2 255.255.255.0
   mpls
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 30.1.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 4.4.4.9 as-number 100
   peer 4.4.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.9 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    peer 11.1.1.1 as-number 200
    peer 11.1.1.1 route-policy policy1 export
    peer 11.1.1.1 label-route-capability
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:2
    apply-label per-route
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0005.00
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 30.1.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 21.1.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
   isis enable 1
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
   ipv4-family vpn-instance vpn1
    import-route direct
    peer 21.1.1.2 as-number 300
    peer 21.1.1.2 route-policy policy1 export
    peer 21.1.1.2 label-route-capability
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  mpls lsr-id 5.5.5.9
   mpls
    lsp-trigger bgp-label-route
  #
  mpls ldp
  #
  interface Gigabitethernet0/1/0
    undo shutdown
   ip address 21.1.1.2 255.255.255.0
   mpls
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 20.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 5.5.5.9 255.255.255.255
  #
  bgp 300
   peer 21.1.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route ospf 1
    peer 21.1.1.1 enable
    peer 21.1.1.1 route-policy policy1 export
    peer 21.1.1.1 label-route-capability
  #
  ospf 1
   import-route bgp
   area 0.0.0.0
    network 5.5.5.9 0.0.0.0
    network 20.1.1.0 0.0.0.255
    network 21.1.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  
  ```
* PE4 configuration file
  
  ```
  #
  sysname PE4
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:2
    apply-label per-route
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 6.6.6.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 172.16.2.2 255.255.255.0
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 20.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 6.6.6.9 255.255.255.255
  #
  bgp 300
   peer 1.1.1.9 as-number 200
   peer 1.1.1.9 ebgp-max-hop 10
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
   ipv4-family vpn-instance vpn1
    import-route direct
    peer 172.16.2.1 as-number 65420
  #
  ospf 1
   area 0.0.0.0
    network 6.6.6.9 0.0.0.0
    network 20.1.1.0 0.0.0.255
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
   ip address 172.16.2.1 255.255.255.0
  #
  bgp 65420
   peer 172.16.2.2 as-number 300
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 172.16.2.2 enable
  #
  return
  
  ```