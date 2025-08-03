Example for Configuring Dual-Homing Active-Active EVPN VPLS over MPLS (VLAN-Aware Access)
=========================================================================================

The VLAN-aware mode allows different VLANs configured on different physical interfaces to access the same EVPN instance while ensuring that traffic from these VLANs remains isolated.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370639__fig_dc_vrp_evpn_cfg_006601), Layer 2 traffic is transmitted within Site1 and Site2. To allow Site1 and Site2 to communicate at Layer 2 over the backbone network, configure EVPN functions. If sites belong to the same subnet, create an EVPN instance on each PE to store EVPN routes and implement Layer 2 forwarding based on MAC addresses. A route reflector (RR) is configured to reflect EVPN routes. To load-balance unicast traffic destined for CE1 between PE1 and PE2, configure PE1 and PE2 to use Eth-Trunk sub-interfaces to connect to Site1. To allow different VLANs configured on different physical interfaces to access the same EVPN instance while ensuring that traffic from these VLANs remains isolated, configure the CE to access PEs in VLAN-aware mode.

**Figure 1** Configuring dual-homing active-active EVPN VPLS over MPLS (VLAN-aware access)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, and GigabitEthernet0/3/0, respectively.


  
![](images/fig_dc_vrp_evpn_cfg_006601.png)  


#### Configuration Precautions

During the configuration process, note the following:

* For the same EVPN instance, the export VPN target list of one site shares VPN targets with the import VPN target lists of the other sites. Conversely, the import VPN target list of one site shares VPN targets with the export VPN target lists of the other sites.
* Using each PE's local loopback interface address as its EVPN source address is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the backbone network to enable PEs and the RR to communicate.
2. Configure basic MPLS functions and enable MPLS LDP to establish LDP LSPs on the MPLS backbone network.
3. Create a BD EVPN instance and a BD, bind the BD to the EVPN instance, and set the BD tag on each PE.
4. Configure a source address on each PE.
5. Configure the ESI and E-Trunk for dual-homing active-active networking. The E-Trunk uses the default encryption mode **enhanced-hmac-sha256** for authentication.
6. Configure local-remote FRR for MAC routes.
7. On PE1 and PE2, configure one BFD session for Eth-Trunk member interface detection and another BFD session for association with the access-side Eth-Trunk interface.
8. Configure BGP EVPN peer relationships between the PEs and RR, and on the RR, specify the PEs as RR clients.
9. Configure CEs and PEs to communicate.
10. Configure IP addresses of the same network segment for CE1 and CE2. Then perform a ping operation on the network segment to trigger the local and remote PEs to learn CE-side MAC addresses.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* EVPN instance evrf1's RDs (100:1, 200:1, and 300:1) and RTs (1:1) on each PE (PE1, PE2, and PE3)
* Hold-down time on the access-side interface of each PE, which is the time elapsed before a PE waits for the EVPN service on the network side to recover and then responds after the interface goes up: 600000 ms
* UDP port number for EVPN pruning status negotiation between active-active PEs: 1345
* Name of the BFD session for Eth-Trunk member interface detection: PEtoCE; names of BFD sessions for association with access-side Eth-Trunk interfaces: pe1tope2 and pe2tope1

#### Procedure

1. Configure interface addresses on the RR and PEs according to [Figure 1](#EN-US_TASK_0172370639__fig_dc_vrp_evpn_cfg_006601). For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370639__file1).
2. Configure an IGP on the backbone network to enable PEs and the RR to communicate. OSPF is used as an IGP in this example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
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
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
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
   
   # Configure PE3.
   
   ```
   [~PE3] ospf 1
   ```
   ```
   [*PE3-ospf-1] area 0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 4.4.4.4 0.0.0.0
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
   
   # Configure the RR.
   
   ```
   [~RR] ospf 1
   ```
   ```
   [*RR-ospf-1] area 0
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~RR-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~RR-ospf-1] quit
   ```
   
   After the configurations are complete, PE1, PE2, and PE3 can establish OSPF neighbor relationships with the RR. Run the **display ospf peer** command. The command output shows that **State** is **Full**. Run the **display ip routing-table** command. The command output shows that the RR and PEs have learned the routes destined for each other's loopback interfaces.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ospf peer
   ```
   ```
   (M) Indicates MADJ neighbor
   
   
             OSPF Process 1 with Router ID 10.1.1.1
                   Neighbors
   
    Area 0.0.0.0 interface 10.1.1.1 (GE0/2/0)'s neighbors
    Router ID: 10.1.1.2             Address: 10.1.1.2         
      State: Full           Mode:Nbr is Master     Priority: 1
      DR: 10.1.1.1          BDR: 10.1.1.2          MTU: 0
      Dead timer due in  32  sec
      Retrans timer interval: 5
      Neighbor is up for 02h56m15s
      Authentication Sequence: [ 0 ]
   
   ```
   ```
   [~PE1] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 13       Routes : 13        
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  Direct  0    0             D   127.0.0.1       LoopBack0
           2.2.2.2/32  OSPF    10   2             D   10.1.1.2        GigabitEthernet0/2/0
           3.3.3.3/32  OSPF    10   1             D   10.1.1.2        GigabitEthernet0/2/0
           4.4.4.4/32  OSPF    10   2             D   10.1.1.2        GigabitEthernet0/2/0
          10.1.1.0/24  Direct  0    0             D   10.1.1.1        GigabitEthernet0/2/0
          10.1.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
        10.1.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
          10.2.1.0/24  OSPF    10   2             D   10.1.1.2        GigabitEthernet0/2/0
          10.3.1.0/24  OSPF    10   2             D   10.1.1.2        GigabitEthernet0/2/0
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   
   ```
3. Configure basic MPLS functions and enable MPLS LDP to establish LDP LSPs on the MPLS backbone network.
   
   
   
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
   [*PE1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.2
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
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/0] quit
   ```
   
   # Configure the RR.
   
   ```
   [~RR] mpls lsr-id 3.3.3.3
   ```
   ```
   [*RR] mpls
   ```
   ```
   [*RR-mpls] quit
   ```
   ```
   [*RR] mpls ldp
   ```
   ```
   [*RR-mpls-ldp] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/1/0
   ```
   ```
   [*RR-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/2/0
   ```
   ```
   [*RR-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/2/0] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/3/0
   ```
   ```
   [*RR-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/3/0] commit
   ```
   ```
   [~RR-GigabitEthernet0/3/0] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 4.4.4.4
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
   [*PE3] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE3-GigabitEthernet0/1/0] quit
   ```
   
   After the configurations are complete, LDP sessions are established between the PEs (PE1, PE2, and PE3) and RR. Run the **display mpls ldp session** command. The command output shows that **Status** is **Operational**. Run the **display mpls ldp lsp** command. The command output shows that an LDP LSP has been successfully established.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    --------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
    --------------------------------------------------------------------------
    3.3.3.3:0          Operational DU   Passive  0000:02:56   709/709
    --------------------------------------------------------------------------
    TOTAL: 1 Session(s) Found.
   ```
   ```
   [~PE1] display mpls ldp lsp
   ```
   ```
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel    UpstreamPeer    NextHop          OutInterface
    -------------------------------------------------------------------------------
    1.1.1.1/32         3/NULL         3.3.3.3         127.0.0.1        Loop1
   *1.1.1.1/32         Liberal/32828                  DS/3.3.3.3       
    2.2.2.2/32         NULL/32829     -               10.1.1.2         GE0/2/0
    2.2.2.2/32         32829/32829    3.3.3.3         10.1.1.2         GE0/2/0
    3.3.3.3/32         NULL/3         -               10.1.1.2         GE0/2/0
    3.3.3.3/32         32828/3        3.3.3.3         10.1.1.2         GE0/2/0
    4.4.4.4/32         NULL/32830     -               10.1.1.2         GE0/2/0
    4.4.4.4/32         32830/32830    3.3.3.3         10.1.1.2         GE0/2/0
    -------------------------------------------------------------------------------
    TOTAL: 7 Normal LSP(s) Found.
    TOTAL: 1 Liberal LSP(s) Found.
    TOTAL: 0 FRR LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   ```
4. Configure an EVPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] evpn binding vpn-instance evrf1 bd-tag 100
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] bridge-domain 20
   ```
   ```
   [*PE1-bd20] evpn binding vpn-instance evrf1 bd-tag 200
   ```
   ```
   [*PE1-bd20] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] bridge-domain 10
   ```
   ```
   [*PE2-bd10] evpn binding vpn-instance evrf1 bd-tag 100
   ```
   ```
   [*PE2-bd10] quit
   ```
   ```
   [*PE2] bridge-domain 20
   ```
   ```
   [*PE2-bd20] evpn binding vpn-instance evrf1 bd-tag 200
   ```
   ```
   [*PE2-bd20] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE3-evpn-instance-evrf1] route-distinguisher 300:1
   ```
   ```
   [*PE3-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE3-evpn-instance-evrf1] quit
   ```
   ```
   [*PE3] bridge-domain 10
   ```
   ```
   [*PE3-bd10] evpn binding vpn-instance evrf1 bd-tag 100
   ```
   ```
   [*PE3-bd10] quit
   ```
   ```
   [*PE3] bridge-domain 20
   ```
   ```
   [*PE3-bd20] evpn binding vpn-instance evrf1 bd-tag 200
   ```
   ```
   [*PE3-bd20] quit
   ```
   ```
   [*PE3] commit
   ```
5. Configure a source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 2.2.2.2
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 4.4.4.4
   ```
   ```
   [*PE3] commit
   ```
6. Configure the ESI and E-Trunk for dual-homing active-active networking.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are not advised to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] lacp e-trunk system-id 00e0-fc00-0000
   ```
   ```
   [*PE1] lacp e-trunk priority 1
   ```
   ```
   [*PE1] e-trunk 1
   ```
   ```
   [*PE1-e-trunk-1] peer-address 2.2.2.2 source-address 1.1.1.1
   ```
   ```
   [*PE1-e-trunk-1] security-key cipher YsHsjx_202206
   ```
   ```
   [*PE1-e-trunk-1] quit
   ```
   ```
   [*PE1] interface eth-trunk 10
   ```
   ```
   [*PE1-Eth-Trunk10] mode lacp-static
   ```
   ```
   [*PE1-Eth-Trunk10] e-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk10] e-trunk mode force-master
   ```
   ```
   [*PE1-Eth-Trunk10] esi 0000.1111.2222.1111.1111
   ```
   ```
   [*PE1-Eth-Trunk10] timer es-recovery 120
   ```
   ```
   [*PE1-Eth-Trunk10] quit
   ```
   ```
   [*PE1] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE1-Eth-Trunk10.1] encapsulation dot1q vid 100
   ```
   ```
   [*PE1-Eth-Trunk10.1] bridge-domain 10
   ```
   ```
   [*PE1-Eth-Trunk10.1] quit
   ```
   ```
   [*PE1] interface eth-trunk 10.2 mode l2
   ```
   ```
   [*PE1-Eth-Trunk10.2] encapsulation dot1q vid 200
   ```
   ```
   [*PE1-Eth-Trunk10.2] bridge-domain 20
   ```
   ```
   [*PE1-Eth-Trunk10.2] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] eth-trunk 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] carrier up-hold-time 600000
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] evpn enhancement port 1345
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] lacp e-trunk system-id 00e0-fc00-0000
   ```
   ```
   [*PE2] lacp e-trunk priority 1
   ```
   ```
   [*PE2] e-trunk 1
   ```
   ```
   [*PE2-e-trunk-1] peer-address 1.1.1.1 source-address 2.2.2.2
   ```
   ```
   [*PE2-e-trunk-1] security-key cipher YsHsjx_202206
   ```
   ```
   [*PE2-e-trunk-1] quit
   ```
   ```
   [*PE2] interface eth-trunk 10
   ```
   ```
   [*PE2-Eth-Trunk10] mode lacp-static
   ```
   ```
   [*PE2-Eth-Trunk10] e-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk10] e-trunk mode force-master
   ```
   ```
   [*PE2-Eth-Trunk10] esi 0000.1111.2222.1111.1111
   ```
   ```
   [*PE2-Eth-Trunk10] timer es-recovery 120
   ```
   ```
   [*PE2-Eth-Trunk10] quit
   ```
   ```
   [*PE2] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE2-Eth-Trunk10.1] encapsulation dot1q vid 100
   ```
   ```
   [*PE2-Eth-Trunk10.1] bridge-domain 10
   ```
   ```
   [*PE2-Eth-Trunk10.1] quit
   ```
   ```
   [*PE2] interface eth-trunk 10.2 mode l2
   ```
   ```
   [*PE2-Eth-Trunk10.2] encapsulation dot1q vid 200
   ```
   ```
   [*PE2-Eth-Trunk10.2] bridge-domain 20
   ```
   ```
   [*PE2-Eth-Trunk10.2] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] eth-trunk 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] carrier up-hold-time 600000
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] evpn enhancement port 1345
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface eth-trunk 10
   ```
   ```
   [*PE3-Eth-Trunk10] esi 0000.1111.3333.4444.5555
   ```
   ```
   [*PE3-Eth-Trunk10] quit
   ```
   ```
   [*PE3] interface eth-trunk 10.1 mode l2
   [*PE3-Eth-Trunk10.1] encapsulation dot1q vid 100
   [*PE3-Eth-Trunk10.1] bridge-domain 10
   [*PE3-Eth-Trunk10.1] quit
   [*PE3] interface eth-trunk 10.2 mode l2
   [*PE3-Eth-Trunk10.2] encapsulation dot1q vid 200
   [*PE3-Eth-Trunk10.2] bridge-domain 20
   [*PE3-Eth-Trunk10.2] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] eth-trunk 10
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] commit
   ```
7. Configure local-remote FRR for MAC routes.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn
   ```
   ```
   [*PE1-evpn] vlan-extend private enable
   ```
   ```
   [*PE1-evpn] vlan-extend redirect enable
   ```
   ```
   [*PE1-evpn] local-remote frr enable
   ```
   ```
   [*PE1-evpn] quit
   ```
   ```
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] evpn
   ```
   ```
   [*PE2-evpn] vlan-extend private enable
   ```
   ```
   [*PE2-evpn] vlan-extend redirect enable
   ```
   ```
   [*PE2-evpn] local-remote frr enable
   ```
   ```
   [*PE2-evpn] quit
   ```
   ```
   [*PE2] commit
   ```
8. On PE1 and PE2, configure one BFD session for Eth-Trunk member interface detection and another BFD session for association with the access-side Eth-Trunk interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] bfd PE1toCE bind peer-ip default-ip interface GigabitEthernet0/1/0 
   ```
   ```
   [*PE1-bfd-session-PE1toCE] discriminator local 1
   ```
   ```
   [*PE1-bfd-session-PE1toCE] discriminator remote 2
   ```
   ```
   [*PE1-bfd-session-PE1toCE] quit
   ```
   ```
   [*PE1] bfd pe1tope2 bind peer-ip 2.2.2.2
   ```
   ```
   [*PE1-bfd-session-pe1tope2] discriminator local 5
   ```
   ```
   [*PE1-bfd-session-pe1tope2] discriminator remote 6
   ```
   ```
   [*PE1-bfd-session-pe1tope2] quit
   ```
   ```
   [*PE1] bfd pe2tope1 bind peer-ip 2.2.2.2 track-interface interface Eth-Trunk10
   ```
   ```
   [*PE1-bfd-session-pe2tope1] discriminator local 7
   ```
   ```
   [*PE1-bfd-session-pe2tope1] discriminator remote 8
   ```
   ```
   [*PE1-bfd-session-pe2tope1] quit
   ```
   ```
   [*PE1] interface eth-trunk 10
   ```
   ```
   [*PE1-Eth-Trunk10] es track bfd pe1tope2
   ```
   ```
   [*PE1-Eth-Trunk10] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
   ```
   ```
   [*PE2] bfd PE2toCE bind peer-ip default-ip interface GigabitEthernet0/1/0 
   ```
   ```
   [*PE2-bfd-session-PE2toCE] discriminator local 3
   ```
   ```
   [*PE2-bfd-session-PE2toCE] discriminator remote 4
   ```
   ```
   [*PE2-bfd-session-PE2toCE] quit
   ```
   ```
   [*PE2] bfd pe1tope2 bind peer-ip 1.1.1.1 track-interface interface Eth-Trunk10
   ```
   ```
   [*PE2-bfd-session-pe1tope2] discriminator local 6
   ```
   ```
   [*PE2-bfd-session-pe1tope2] discriminator remote 5
   ```
   ```
   [*PE2-bfd-session-pe1tope2] quit
   ```
   ```
   [*PE2] bfd pe2tope1 bind peer-ip 1.1.1.1
   ```
   ```
   [*PE2-bfd-session-pe2tope1] discriminator local 8
   [*PE2-bfd-session-pe2tope1] discriminator remote 7
   [*PE2-bfd-session-pe2tope1] quit
   ```
   ```
   [*PE2] interface eth-trunk 10
   [*PE2-Eth-Trunk10] es track bfd pe2tope1
   [*PE2-Eth-Trunk10] quit
   ```
   ```
   [*PE2] commit
   ```
9. Configure BGP EVPN peer relationships between the PEs and RR, and on the RR, specify the PEs as RR clients.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] timer df-delay 0
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
   [*PE2-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE2-bgp-af-evpn] timer df-delay 0
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
   [*PE3-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE3-bgp] peer 3.3.3.3 connect-interface loopback 0
   ```
   ```
   [*PE3-bgp] l2vpn-family evpn
   ```
   ```
   [*PE3-bgp-af-evpn] peer 3.3.3.3 enable
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
   
   # Configure the RR.
   
   ```
   [~RR] bgp 100
   ```
   ```
   [*RR-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*RR-bgp] peer 1.1.1.1 connect-interface loopback 0
   ```
   ```
   [*RR-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*RR-bgp] peer 2.2.2.2 connect-interface loopback 0
   ```
   ```
   [*RR-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*RR-bgp] peer 4.4.4.4 connect-interface loopback 0
   ```
   ```
   [*RR-bgp] l2vpn-family evpn
   ```
   ```
   [*RR-bgp-af-evpn] undo policy vpn-target
   [*RR-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 1.1.1.1 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 2.2.2.2 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 4.4.4.4 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] quit
   ```
   ```
   [*RR-bgp] quit
   ```
   ```
   [*RR] commit
   ```
   
   After completing the configurations, run the **display bgp evpn peer** command on the RR. The command output shows that BGP peer relationships are in the **Established** state, indicating that BGP peer relationships have been successfully established between the PEs and RR.
   
   ```
   [~RR] display bgp evpn peer
   ```
   ```
    
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     1.1.1.1         4         100      231      253     0 03:07:26 Established        6
     2.2.2.2         4         100      231      256     0 03:07:44 Established        6
     4.4.4.4         4         100      232      254     0 03:07:54 Established        6
   ```
10. Configure CEs and PEs to communicate.
    
    
    
    # Configure CE1.
    
    ```
    [~CE1] interface Eth-Trunk20
    ```
    ```
    [*CE1-Eth-Trunk20] mode lacp-static
    ```
    ```
    [*CE1-Eth-Trunk20] quit
    ```
    ```
    [*CE1] bridge-domain 10
    ```
    ```
    [*CE1-bd10] quit
    ```
    ```
    [*CE1] bridge-domain 20
    ```
    ```
    [*CE1-bd20] quit
    ```
    ```
    [*CE1] interface Eth-Trunk20.1 mode l2
    ```
    ```
    [*CE1-Eth-Trunk20.1] encapsulation dot1q vid 100
    [*CE1-Eth-Trunk20.1] rewrite pop single
    ```
    ```
    [*CE1-Eth-Trunk20.1] bridge-domain 10
    ```
    ```
    [*CE1-Eth-Trunk20.1] quit
    ```
    ```
    [*CE1] interface Eth-Trunk20.2 mode l2
    ```
    ```
    [*CE1-Eth-Trunk20.2] encapsulation dot1q vid 200
    [*CE1-Eth-Trunk20.2] rewrite pop single
    ```
    ```
    [*CE1-Eth-Trunk20.2] bridge-domain 20
    ```
    ```
    [*CE1-Eth-Trunk20.2] quit
    ```
    ```
    [*CE1] interface gigabitethernet0/1/0
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] eth-trunk 20
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] quit
    ```
    ```
    [*CE1] interface gigabitethernet0/2/0
    ```
    ```
    [*CE1-GigabitEthernet0/2/0] eth-trunk 20
    ```
    ```
    [*CE1-GigabitEthernet0/2/0] quit
    [*CE1] bfd CEtoPE1 bind peer-ip default-ip interface GigabitEthernet0/1/0 
    [*CE1-bfd-session-CEtoPE1] discriminator local 2
    [*CE1-bfd-session-CEtoPE1] discriminator remote 1
    [*CE1-bfd-session-CEtoPE1] quit
    [*CE1] bfd CEtoPE2 bind peer-ip default-ip interface GigabitEthernet0/2/0 
    [*CE1-bfd-session-CEtoPE2] discriminator local 4
    [*CE1-bfd-session-CEtoPE2] discriminator remote 3
    [*CE1-bfd-session-CEtoPE2] quit
    ```
    ```
    [*CE1] commit
    ```
    
    # Configure CE2.
    
    ```
    [~CE2] interface Eth-Trunk 10
    ```
    ```
    [*CE2-Eth-Trunk10] quit
    ```
    ```
    [*CE2] bridge-domain 10
    ```
    ```
    [*CE2-bd10] quit
    ```
    ```
    [*CE2] interface Eth-Trunk 10.1 mode l2
    ```
    ```
    [*CE2-Eth-Trunk10.1] encapsulation dot1q vid 100
    [*CE2-Eth-Trunk10.1] rewrite pop single
    ```
    ```
    [*CE2-Eth-Trunk10.1] bridge-domain 10
    ```
    ```
    [*CE2-Eth-Trunk10.1] quit
    ```
    ```
    [*CE2] interface Eth-Trunk 10.2 mode l2
    ```
    ```
    [*CE2-Eth-Trunk10.2] encapsulation dot1q vid 200
    [*CE2-Eth-Trunk10.2] rewrite pop single
    ```
    ```
    [*CE2-Eth-Trunk10.2] bridge-domain 20
    ```
    ```
    [*CE2-Eth-Trunk10.2] quit
    ```
    ```
    [*CE2] interface gigabitethernet0/1/0
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] eth-trunk 10
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] quit
    ```
    ```
    [*CE2] commit
    ```
11. Configure IP addresses on the same network segment on CE1 and CE2 and perform a ping operation on the same network segment.
    
    
    
    # Configure CE1.
    
    ```
    [~CE1] interface vbdif10
    [*CE1-Vbdif10] ip address 192.168.1.11 24
    [*CE1-Vbdif10] quit
    [*CE1] interface vbdif20
    [*CE1-Vbdif20] ip address 192.168.2.11 24
    [*CE1-Vbdif20] quit
    [*CE1] commit
    ```
    
    
    
    # Configure CE2.
    
    ```
    [~CE2] interface vbdif10
    [*CE2-Vbdif10] ip address 192.168.1.12 24
    [*CE2-Vbdif10] quit
    [*CE2] interface vbdif20
    [*CE2-Vbdif20] ip address 192.168.2.12 24
    [*CE2-Vbdif20] quit
    [*CE2] commit
    ```
    
    # Ping CE2 from CE1 (with the source and destination IP addresses being on the same network segment). The following example uses the command output on CE1.
    
    ```
    [~CE1] ping 192.168.1.12 
    ```
    ```
     PING 192.168.1.12: 56 data bytes, press CTRL_C to break
     Reply from 192.168.1.12: bytes=56 Sequence=1 ttl=255 time=1 ms
     Reply from 192.168.1.12: bytes=56 Sequence=2 ttl=255 time=1 ms
     Reply from 192.168.1.12: bytes=56 Sequence=3 ttl=255 time=1 ms
     Reply from 192.168.1.12: bytes=56 Sequence=4 ttl=255 time=1 ms
     Reply from 192.168.1.12: bytes=56 Sequence=5 ttl=255 time=1 ms
    
     --- 192.168.1.12 ping statistics ---
     5 packet(s) transmitted
     5 packet(s) received
     0.00% packet loss
     round-trip min/avg/max = 1/1/1 ms
    ```
    ```
    [~CE1] ping 192.168.2.12
    ```
    ```
     PING 192.168.2.12: 56 data bytes, press CTRL_C to break
     Reply from 192.168.2.12: bytes=56 Sequence=1 ttl=255 time=1 ms
     Reply from 192.168.2.12: bytes=56 Sequence=2 ttl=255 time=1 ms
     Reply from 192.168.2.12: bytes=56 Sequence=3 ttl=255 time=1 ms
     Reply from 192.168.2.12: bytes=56 Sequence=4 ttl=255 time=1 ms
     Reply from 192.168.2.12: bytes=56 Sequence=5 ttl=255 time=1 ms
    
     --- 192.168.2.12 ping statistics ---
     5 packet(s) transmitted
     5 packet(s) received
     0.00% packet loss
     round-trip min/avg/max = 1/1/1 ms
    ```
12. Verify the configuration.
    
    
    
    Run the **display bgp evpn all routing-table** command on PE3. The command output shows that EVPN routes carrying Ethernet tag IDs are received from the remote PEs.
    
    ```
    [~PE3] display bgp evpn all routing-table
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 10.3.1.2
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
    
     EVPN address family:
     Number of A-D Routes: 9
     Route Distinguisher: 100:1
     Network(ESI/EthTagId)                                     NextHop
     *>i 0000.1111.2222.1111.1111:100                          1.1.1.1 
     *>i 0000.1111.2222.1111.1111:200                          1.1.1.1 
     Route Distinguisher: 200:1
     Network(ESI/EthTagId) NextHop
     *>i 0000.1111.2222.1111.1111:100                          2.2.2.2 
     *>i 0000.1111.2222.1111.1111:200                          2.2.2.2 
     Route Distinguisher: 1.1.1.1:0
     Network(ESI/EthTagId)                                     NextHop
     *>i 0000.1111.2222.1111.1111:4294967295                   1.1.1.1 
     Route Distinguisher: 300:1
     Network(ESI/EthTagId)                                     NextHop
     *> 0000.1111.3333.4444.5555:100                           127.0.0.1 
     *> 0000.1111.3333.4444.5555:200                           127.0.0.1 
     Route Distinguisher: 2.2.2.2:0
     Network(ESI/EthTagId)                                     NextHop
     *>i 0000.1111.2222.1111.1111:4294967295                   2.2.2.2 
     Route Distinguisher: 4.4.4.4:0
     Network(ESI/EthTagId)                                     NextHop
     *> 0000.1111.3333.4444.5555:4294967295                    127.0.0.1 
    
    
     EVPN-Instance evrf1:
     Number of A-D Routes: 8
     Network(ESI/EthTagId)                                     NextHop
     *>i 0000.1111.2222.1111.1111:100                          1.1.1.1 
     * i                                                       2.2.2.2 
     *>i 0000.1111.2222.1111.1111:200                          1.1.1.1 
     * i                                                       2.2.2.2 
     *>i 0000.1111.2222.1111.1111:4294967295                   1.1.1.1 
     * i                                                       2.2.2.2 
     *> 0000.1111.3333.4444.5555:100                          127.0.0.1 
     *> 0000.1111.3333.4444.5555:200                          127.0.0.1 
     
     EVPN address family:
     Number of Mac Routes: 4
     Route Distinguisher: 100:1
     Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)     NextHop
     *>i 100:48:2019-0211-3313:0:0.0.0.0                       1.1.1.1 
     *>i 200:48:2019-0211-3313:0:0.0.0.0                       1.1.1.1 
     Route Distinguisher: 300:1
     Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)     NextHop
     *> 100:48:2019-0211-3314:0:0.0.0.0                        0.0.0.0 
     *> 200:48:2019-0211-3314:0:0.0.0.0                        0.0.0.0 
    
    
     EVPN-Instance evrf1:
     Number of Mac Routes: 4
     Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)     NextHop
     *>i 100:48:2019-0211-3313:0:0.0.0.0                       1.1.1.1 
     *>  100:48:2019-0211-3314:0:0.0.0.0                       0.0.0.0 
     *>i 200:48:2019-0211-3313:0:0.0.0.0                       1.1.1.1 
     *>  200:48:2019-0211-3314:0:0.0.0.0                       0.0.0.0 
     
     EVPN address family:
     Number of Inclusive Multicast Routes: 6
     Route Distinguisher: 100:1
     Network(EthTagId/IpAddrLen/OriginalIp)                    NextHop
     *>i 100:32:1.1.1.1                                        1.1.1.1 
     *>i 200:32:1.1.1.1                                        1.1.1.1 
     Route Distinguisher: 200:1
     Network(EthTagId/IpAddrLen/OriginalIp)                    NextHop
     *>i 100:32:2.2.2.2                                        2.2.2.2 
     *>i 200:32:2.2.2.2                                        2.2.2.2 
     Route Distinguisher: 300:1
     Network(EthTagId/IpAddrLen/OriginalIp)                    NextHop
     *> 100:32:4.4.4.4                                         127.0.0.1 
     *> 200:32:4.4.4.4                                         127.0.0.1 
    
    
     EVPN-Instance evrf1:
     Number of Inclusive Multicast Routes: 6
     Network(EthTagId/IpAddrLen/OriginalIp)                    NextHop
     *>i 100:32:1.1.1.1                                        1.1.1.1 
     *>i 100:32:2.2.2.2                                        2.2.2.2 
     *>  100:32:4.4.4.4                                        127.0.0.1 
     *>i 200:32:1.1.1.1                                        1.1.1.1 
     *>i 200:32:2.2.2.2                                        2.2.2.2 
     *>  200:32:4.4.4.4                                        127.0.0.1 
     
     EVPN address family:
     Number of ES Routes: 1
     Route Distinguisher: 4.4.4.4:0
     Network(ESI)                                              NextHop
     *> 0000.1111.3333.4444.5555                               127.0.0.1 
    
    
     EVPN-Instance evrf1:
     Number of ES Routes: 1
     Network(ESI)                                              NextHop
     *> 0000.1111.3333.4444.5555                               127.0.0.1 
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  lacp e-trunk system-id 00e0-fc00-0000
  lacp e-trunk priority 1
  ```
  ```
  #
  evpn enhancement port 1345
  ```
  ```
  #
  evpn
   vlan-extend private enable
   vlan-extend redirect enable
   local-remote frr enable
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  ```
  ```
  #
  bfd
  ```
  ```
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1 bd-tag 100
  #
  bridge-domain 20
   evpn binding vpn-instance evrf1 bd-tag 200
  #
  mpls ldp
  #
  e-trunk 1
   peer-address 2.2.2.2 source-address 1.1.1.1
   security-key cipher %^%#4sTf&{QHhMK"uZMOn>r;3&5~&0,1>:7fGZ9h~@1X%^%#
   authentication-mode enhanced-hmac-sha256
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.1111.2222.1111.1111
   es track bfd pe1tope2
   timer es-recovery 120
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface Eth-Trunk10.2 mode l2
   encapsulation dot1q vid 200
   bridge-domain 20
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   carrier up-hold-time 600000
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  bfd pe1tope2 bind peer-ip 2.2.2.2
   discriminator local 5
   discriminator remote 6
  #
  bfd pe2tope1 bind peer-ip 2.2.2.2 track-interface interface Eth-Trunk10
   discriminator local 7
   discriminator remote 8
  #
  bfd PE1toCE bind peer-ip default-ip interface GigabitEthernet0/1/0
   discriminator local 1
   discriminator remote 2
  ```
  ```
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    policy vpn-target
    timer df-delay 0
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  lacp e-trunk system-id 00e0-fc00-0000
  lacp e-trunk priority 1
  ```
  ```
  #
  evpn enhancement port 1345
  ```
  ```
  #
  evpn
   vlan-extend private enable
   vlan-extend redirect enable
   local-remote frr enable
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  ```
  ```
  #
  bfd
  ```
  ```
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1 bd-tag 100
  #
  bridge-domain 20
   evpn binding vpn-instance evrf1 bd-tag 200
  #
  mpls ldp
  #
  e-trunk 1
   peer-address 1.1.1.1 source-address 2.2.2.2
   security-key cipher %^%#4sTf&{QHhMK"uZMOn>r;3&5~&0,1>:7fGZ9h~@1X%^%#
   authentication-mode enhanced-hmac-sha256
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.1111.2222.1111.1111
   es track bfd pe2tope1
   timer es-recovery 120
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface Eth-Trunk10.2 mode l2
   encapsulation dot1q vid 200
   bridge-domain 20
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   carrier up-hold-time 600000
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.0
  ```
  ```
  #
  bfd pe1tope2 bind peer-ip 1.1.1.1 track-interface interface Eth-Trunk10
   discriminator local 6
   discriminator remote 5
  #
  bfd pe2tope1 bind peer-ip 1.1.1.1
   discriminator local 8
   discriminator remote 7
  #
  bfd PE2toCE bind peer-ip default-ip interface GigabitEthernet0/1/0
   discriminator local 3
   discriminator remote 4
  ```
  ```
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    policy vpn-target
    timer df-delay 0
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  evpn source-address 2.2.2.2
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 300:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1 bd-tag 100
  #
  bridge-domain 20
   evpn binding vpn-instance evrf1 bd-tag 200
  #
  mpls ldp
  #
  interface Eth-Trunk10
   esi 0000.1111.3333.4444.5555
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   bridge-domain 10
  #
  interface Eth-Trunk10.2 mode l2
   encapsulation dot1q vid 200
   bridge-domain 20
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   eth-trunk 10
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #              
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  evpn source-address 4.4.4.4
  #
  return
  ```
* RR configuration file
  
  ```
  #
  sysname RR
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 4.4.4.4 enable
    peer 4.4.4.4 reflect-client
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  bridge-domain 10
  #
  bridge-domain 20
  #
  bfd
  #
  interface Vbdif10
   ip address 192.168.1.11 255.255.255.0
  #
  interface Vbdif20
   ip address 192.168.2.11 255.255.255.0
  #
  interface Eth-Trunk20
   mode lacp-static
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk20.2 mode l2
   encapsulation dot1q vid 200
   rewrite pop single
   bridge-domain 20
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 20
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   eth-trunk 20
  #
  bfd CEtoPE1 bind peer-ip default-ip interface GigabitEthernet0/1/0
   discriminator local 2
   discriminator remote 1
  #
  bfd CEtoPE2 bind peer-ip default-ip interface GigabitEthernet0/2/0
   discriminator local 4
   discriminator remote 3
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  bridge-domain 10
  #
  bridge-domain 20
  #
  interface Vbdif10
   ip address 192.168.1.12 255.255.255.0
  #
  interface Vbdif20
   ip address 192.168.2.12 255.255.255.0
  #
  interface Eth-Trunk10
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk10.2 mode l2
   encapsulation dot1q vid 200
   rewrite pop single
   bridge-domain 20
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  return
  ```