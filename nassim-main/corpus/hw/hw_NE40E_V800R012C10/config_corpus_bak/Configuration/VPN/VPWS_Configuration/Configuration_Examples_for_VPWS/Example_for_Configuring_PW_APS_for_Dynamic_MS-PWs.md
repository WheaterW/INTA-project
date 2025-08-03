Example for Configuring PW APS for Dynamic MS-PWs
=================================================

In PW APS scenarios, MPLS OAM is used to detect the status of dynamic MS-PWs.

#### Networking Requirements

On the public network shown in [Figure 1](#EN-US_TASK_0172369990__fig_dc_vrp_vpws_cfg_604101), dynamic associated bidirectional LSPs need to be established between the four PEs. In addition, CE1 and CE2 need to reliably communicate through the four PEs on the public network.

PW redundancy needs to be deployed on PE1 and PE2. For primary and secondary PWs that share the same source and same destination and dynamic associated bidirectional LSPs, consider deploying PW APS for dynamic PWs. As the four PEs belong to different IGP domains, the PWs must be MS-PWs.

**Figure 1** Configuring PW APS for dynamic MS-PWs![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1, subinterface1.1, interface2, and interface3 represent GE0/1/0, GE0/1/0.1, GE0/1/1, and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_604101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses and a routing protocol.
2. Configure MPLS and public network tunnels.
   
   In this example, dynamic associated bidirectional LSPs are used between PEs and SPEs. The specific configurations include:
   
   * Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and CSPF.
   * Configure OSPF TE.
   * Configure dynamic associated bidirectional LSPs.
3. Configure a PW protection group (dynamic MS-PWs are used in this example), which includes:
   
   * Configure a PW protection group on PE1 and PE2.
   * Configure a dynamic switched PW on SPE1 and SPE2.
4. Configure PW APS, which includes:
   
   * Configure a PW APS instance on PE1 and PE2.
   * Bind the PW protection group to the PW APS instance.
5. Configure MPLS OAM to detect PW status.
6. Configure CEs to access the L2VPN through VLANs on the AC side.

#### Data Preparation

To complete the configuration, you need the following data:

* PEs' interface numbers, IP addresses and OSPF process IDs
* Each PE's LSR ID, tunnel interface numbers and IP addresses, and tunnel IDs and ingress LSR IDs of reverse RSVP LSPs
* Local and remote IP addresses, VC IDs, and VC types of L2VCs
* APS instance numbers on PE1 and PE2

#### Procedure

1. Configure interface IP addresses and a routing protocol.
   
   
   
   Configure an IP address and mask for each involved interface according to [Figure 1](#EN-US_TASK_0172369990__fig_dc_vrp_vpws_cfg_604101). For detailed configurations, see Configuration Files.
   
   In this example, OSPF is used as the IGP for PE1, PE2, SPE1, and SPE2 to communicate at the network layer. The configuration details are not provided here.
2. Configure MPLS and public network tunnels.
   
   
   
   In this example, dynamic associated bidirectional LSPs are used between PEs (PE1 and PE2) and SPEs (SPE1 and SPE2).
   
   
   
   1. Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and CSPF.
      
      
      
      Enable MPLS, MPLS TE, and CSPF globally for each node and enable MPLS, MPLS TE, and RSVP-TE on each interface along the TE tunnel.
      
      # Configure PE1.
      
      ```
      [~PE1] mpls lsr-id 1.1.1.1
      ```
      ```
      [*PE1] mpls
      ```
      ```
      [*PE1-mpls] mpls te
      ```
      ```
      [*PE1-mpls] mpls rsvp-te
      ```
      ```
      [*PE1-mpls] mpls te cspf
      ```
      ```
      [*PE1-mpls] label advertise non-null
      ```
      ```
      [*PE1-mpls] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      The configurations of PE2 and SPE1 are similar to that of SPE2. For detailed configurations, see Configuration Files.
   2. Configure OSPF TE.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] ospf 1
      ```
      ```
      [*PE1-ospf-1] opaque-capability enable
      ```
      ```
      [*PE1-ospf-1] area 0
      ```
      ```
      [*PE1-ospf-1-area-0.0.0.0] mpls-te enable
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
      
      The configurations of PE2 and SPE1 are similar to that of SPE2. For detailed configurations, see Configuration Files.
   3. Configure an MPLS TE explicit path.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] explicit-path 1to2
      ```
      ```
      [*PE1-explicit-path-1to2] next hop 10.1.2.2
      ```
      ```
      [*PE1-explicit-path-1to2] next hop 2.2.2.2
      ```
      ```
      [*PE1-explicit-path-1to2] quit
      ```
      ```
      [*PE1] explicit-path 1to3
      ```
      ```
      [*PE1-explicit-path-1to3] next hop 10.1.3.2
      ```
      ```
      [*PE1-explicit-path-1to3] next hop 3.3.3.3
      ```
      ```
      [*PE1-explicit-path-1to3] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] explicit-path 2to1
      ```
      ```
      [*SPE1-explicit-path-2to1] next hop 10.1.2.1
      ```
      ```
      [*SPE1-explicit-path-2to1] next hop 1.1.1.1
      ```
      ```
      [*SPE1-explicit-path-2to1] quit
      ```
      ```
      [*SPE1] explicit-path 2to4
      ```
      ```
      [*SPE1-explicit-path-2to4] next hop 10.1.4.2
      ```
      ```
      [*SPE1-explicit-path-2to4] next hop 4.4.4.4
      ```
      ```
      [*SPE1-explicit-path-2to4] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] explicit-path 3to1
      ```
      ```
      [*SPE2-explicit-path-3to1] next hop 10.1.3.1
      ```
      ```
      [*SPE2-explicit-path-3to1] next hop 1.1.1.1
      ```
      ```
      [*SPE2-explicit-path-3to1] quit
      ```
      ```
      [*SPE2] explicit-path 3to4
      ```
      ```
      [*SPE2-explicit-path-3to4] next hop 10.1.5.2
      ```
      ```
      [*SPE2-explicit-path-3to4] next hop 4.4.4.4
      ```
      ```
      [*SPE2-explicit-path-3to4] quit
      ```
      ```
      [*SPE2] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] explicit-path 4to2
      ```
      ```
      [*PE2-explicit-path-4to2] next hop 10.1.4.1
      ```
      ```
      [*PE2-explicit-path-4to2] next hop 2.2.2.2
      ```
      ```
      [*PE2-explicit-path-4to2] quit
      ```
      ```
      [*PE2] explicit-path 4to3
      ```
      ```
      [*PE2-explicit-path-4to3] next hop 10.1.5.1
      ```
      ```
      [*PE2-explicit-path-4to3] next hop 3.3.3.3
      ```
      ```
      [*PE2-explicit-path-4to3] quit
      ```
      ```
      [*PE2] commit
      ```
   4. Configure dynamic associated bidirectional LSPs.
      
      
      
      The following example shows how to configure a dynamic associated bidirectional LSP between PE1 and SPE1. Repeat this step to configure a dynamic associated bidirectional LSP between PE1 and SPE2, between PE2 and SPE1, and between PE2 and SPE2. For detailed configurations, see Configuration Files.
      
      # Configure an LSP from PE1 to SPE1 and bind it to the LSP from SPE1 to PE1.
      
      ```
      [~PE1] interface Tunnel10
      ```
      ```
      [*PE1-Tunnel10] ip address unnumbered interface loopback 0
      ```
      ```
      [*PE1-Tunnel10] tunnel-protocol mpls te
      ```
      ```
      [*PE1-Tunnel10] destination 2.2.2.2
      ```
      ```
      [*PE1-Tunnel10] mpls te tunnel-id 100
      ```
      ```
      [*PE1-Tunnel10] mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 2.2.2.2 tunnel-id 100
      ```
      ```
      [*PE1-Tunnel10] mpls te path explicit-path 1to2
      ```
      ```
      [*PE1-Tunnel10] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure an LSP from SPE1 to PE1 and bind it to the LSP from PE1 to SPE1.
      
      ```
      [~SPE1] interface Tunnel10
      ```
      ```
      [*SPE1-Tunnel10] ip address unnumbered interface loopback 0
      ```
      ```
      [*SPE1-Tunnel10] tunnel-protocol mpls te
      ```
      ```
      [*SPE1-Tunnel10] destination 1.1.1.1
      ```
      ```
      [*SPE1-Tunnel10] mpls te tunnel-id 100
      ```
      ```
      [*SPE1-Tunnel10] mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 100
      ```
      ```
      [*SPE1-Tunnel10] mpls te path explicit-path 2to1
      ```
      ```
      [*SPE1-Tunnel10] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      Run the **display mpls te reverse-lsp** command on PE1, PE2, SPE1, and SPE2 to check information about the dynamic associated bidirectional LSPs. PE1 is used as an example.
      
      ```
      [~PE1] display mpls te reverse-lsp tunnel-interface Tunnel 10 verbose
      ```
      ```
      -------------------------------------------------------------------------------
                       LSP Information: RSVP LSP
      -------------------------------------------------------------------------------
        Obverse Tunnel           :  Tunnel10
        Reverse LSP IngressLsrID :  2.2.2.2
        Reverse LSP SessionID    :  100
        Signalled Tunnel Name    :  Tunnel10
        Reverse LSP State        :  Up
        Incoming Label           :  3
         Incoming Interface      :  GE0/1/1
         LSP-id                  :  2
      ```
      
      Run the **ping lsp** command on PE1, PE2, SPE1, and SPE2 to check LSP connectivity. If the ping operations succeed, the dynamic associated bidirectional LSPs have been established. A tunnel on PE1 is used as an example.
      
      ```
      [~PE1] ping lsp -r 4 te Tunnel 11
      ```
      ```
        LSP PING FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel11 : 100  data bytes, pres
      s CTRL_C to break
          Reply from 3.3.3.3: bytes=100 Sequence=1 time=90 ms
          Reply from 3.3.3.3: bytes=100 Sequence=2 time=90 ms
          Reply from 3.3.3.3: bytes=100 Sequence=3 time=90 ms
          Reply from 3.3.3.3: bytes=100 Sequence=4 time=480 ms
          Reply from 3.3.3.3: bytes=100 Sequence=5 time=70 ms
      
        --- FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel11 ping statistics ---
          5 packet(s) transmitted
          5 packet(s) received
          0.00% packet loss
          round-trip min/avg/max = 70/164/480 ms  
      ```
3. Configure a PW protection group.
   
   
   
   Dynamic MS-PWs are used in this example.
   
   
   
   1. Configure VPN tunnel binding.
      
      
      
      In this example, the dynamic PWs are carried over dynamic associated bidirectional LSPs. A tunnel policy is required to bind LSPs to the L2VPN.
      
      # Configure PE1.
      
      ```
      [~PE1] interface Tunnel10
      ```
      ```
      [*PE1-Tunnel10] mpls te reserved-for-binding
      ```
      ```
      [*PE1-Tunnel10] quit
      ```
      ```
      [*PE1] interface Tunnel11
      ```
      ```
      [*PE1-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*PE1-Tunnel11] quit
      ```
      ```
      [*PE1] tunnel-policy policy1
      ```
      ```
      [*PE1-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel10
      ```
      ```
      [*PE1-tunnel-policy-policy1] tunnel binding destination 3.3.3.3 te Tunnel11
      ```
      ```
      [*PE1-tunnel-policy-policy1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] interface Tunnel10
      ```
      ```
      [*SPE1-Tunnel10] mpls te reserved-for-binding
      ```
      ```
      [*SPE1-Tunnel10] quit
      ```
      ```
      [*SPE1] interface Tunnel11
      ```
      ```
      [*SPE1-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*SPE1-Tunnel11] quit
      ```
      ```
      [*SPE1] tunnel-policy policy1
      ```
      ```
      [*SPE1-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel10
      ```
      ```
      [*SPE1-tunnel-policy-policy1] tunnel binding destination 4.4.4.4 te Tunnel11
      ```
      ```
      [*SPE1-tunnel-policy-policy1] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] interface Tunnel10
      ```
      ```
      [*SPE2-Tunnel10] mpls te reserved-for-binding
      ```
      ```
      [*SPE2-Tunnel10] quit
      ```
      ```
      [*SPE2] interface Tunnel11
      ```
      ```
      [*SPE2-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*SPE2-Tunnel11] quit
      ```
      ```
      [*SPE2] tunnel-policy policy1
      ```
      ```
      [*SPE2-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel10
      ```
      ```
      [*SPE2-tunnel-policy-policy1] tunnel binding destination 4.4.4.4 te Tunnel11
      ```
      ```
      [*SPE2-tunnel-policy-policy1] quit
      ```
      ```
      [*SPE2] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface Tunnel10
      ```
      ```
      [*PE2-Tunnel10] mpls te reserved-for-binding
      ```
      ```
      [*PE2-Tunnel10] quit
      ```
      ```
      [*PE2] interface Tunnel11
      ```
      ```
      [*PE2-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*PE2-Tunnel11] quit
      ```
      ```
      [*PE2] tunnel-policy policy1
      ```
      ```
      [*PE2-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel10
      ```
      ```
      [*PE2-tunnel-policy-policy1] tunnel binding destination 3.3.3.3 te Tunnel11
      ```
      ```
      [*PE2-tunnel-policy-policy1] quit
      ```
      ```
      [*PE2] commit
      ```
   2. Configure remote MPLS LDP sessions.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] mpls ldp
      ```
      ```
      [*PE1-mpls-ldp] quit
      ```
      ```
      [*PE1] mpls ldp remote-peer 2.2.2.2
      ```
      ```
      [*PE1-mpls-ldp-remote-2.2.2.2] remote-ip 2.2.2.2
      ```
      ```
      [*PE1-mpls-ldp-remote-2.2.2.2] quit
      ```
      ```
      [*PE1] mpls ldp remote-peer 3.3.3.3
      ```
      ```
      [*PE1-mpls-ldp-remote-3.3.3.3] remote-ip 3.3.3.3
      ```
      ```
      [*PE1-mpls-ldp-remote-3.3.3.3] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] mpls ldp
      ```
      ```
      [*PE2-mpls-ldp] quit
      ```
      ```
      [*PE2] mpls ldp remote-peer 2.2.2.2
      ```
      ```
      [*PE2-mpls-ldp-remote-2.2.2.2] remote-ip 2.2.2.2
      ```
      ```
      [*PE2-mpls-ldp-remote-2.2.2.2] quit
      ```
      ```
      [*PE2] mpls ldp remote-peer 3.3.3.3
      ```
      ```
      [*PE2-mpls-ldp-remote-3.3.3.3] remote-ip 3.3.3.3
      ```
      ```
      [*PE2-mpls-ldp-remote-3.3.3.3] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] mpls ldp
      ```
      ```
      [*SPE1-mpls-ldp] quit
      ```
      ```
      [*SPE1] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*SPE1-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
      ```
      ```
      [*SPE1-mpls-ldp-remote-1.1.1.1] quit
      ```
      ```
      [*SPE1] mpls ldp remote-peer 4.4.4.4
      ```
      ```
      [*SPE1-mpls-ldp-remote-4.4.4.4] remote-ip 4.4.4.4
      ```
      ```
      [*SPE1-mpls-ldp-remote-4.4.4.4] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] mpls ldp
      ```
      ```
      [*SPE2-mpls-ldp] quit
      ```
      ```
      [*SPE2] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*SPE2-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
      ```
      ```
      [*SPE2-mpls-ldp-remote-1.1.1.1] quit
      ```
      ```
      [*SPE2] mpls ldp remote-peer 4.4.4.4
      ```
      ```
      [*SPE2-mpls-ldp-remote-4.4.4.4] remote-ip 4.4.4.4
      ```
      ```
      [*SPE2-mpls-ldp-remote-4.4.4.4] quit
      ```
      ```
      [*SPE2] commit
      ```
   3. Configure dynamic PWs.
      
      
      
      # Configure the primary and secondary dynamic PWs on PE1.
      
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
      [*PE1-GigabitEthernet0/1/0] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc 2.2.2.2 1 tunnel-policy policy1 control-word
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc 3.3.3.3 2 tunnel-policy policy1 control-word secondary
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vpn stream-dual-receiving
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure the primary and secondary dynamic PWs on PE2.
      
      ```
      [~PE2] mpls l2vpn
      ```
      ```
      [*PE2-l2vpn] quit
      ```
      ```
      [*PE2] interface gigabitethernet0/1/2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE2] interface gigabitethernet0/1/2.1
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] vlan-type dot1q 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] mpls l2vc 2.2.2.2 3 tunnel-policy policy1 control-word
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] mpls l2vc 3.3.3.3 4 tunnel-policy policy1 control-word secondary
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] mpls l2vpn stream-dual-receiving
      ```
      ```
      [*PE2-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure a dynamic switched PW on SPE1.
      
      ```
      [~SPE1] mpls l2vpn
      ```
      ```
      [*SPE1-l2vpn] quit
      ```
      ```
      [*SPE1] mpls switch-l2vc 4.4.4.4 3 tunnel-policy policy1 between 1.1.1.1 1 tunnel-policy policy1 encapsulation vlan control-word-transparent
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure a dynamic switched PW on SPE2.
      
      ```
      [~SPE2] mpls l2vpn
      ```
      ```
      [*SPE2-l2vpn] quit
      ```
      ```
      [*SPE2] mpls switch-l2vc 4.4.4.4 4 tunnel-policy policy1 between 1.1.1.1 2 tunnel-policy policy1 encapsulation vlan control-word-transparent
      ```
      ```
      [*SPE2] commit
      ```
      
      Run the **display mpls l2vc brief** command on PE1 and PE2. The command output shows dynamic PW information. PE1 is used as an example.
      
      ```
      [~PE1] display mpls l2vc brief
      ```
      ```
       Total ldp vc : 2     2 up       0 down
      
       *Client Interface     : GigabitEthernet0/1/0.1
        Administrator PW     : no
        AC status            : up
        VC State             : up
        Label state          : 0
        Token state          : 0
        VC ID                : 1
        VC Type              : VLAN
        session state        : up
        Destination          : 2.2.2.2
        link state           : up
      
       *Client Interface     : GigabitEthernet0/1/0.1
        Administrator PW     : no
        AC status            : up
        VC State             : up
        Label state          : 0
        Token state          : 0
        VC ID                : 2
        VC Type              : VLAN
        session state        : up
        Destination          : 3.3.3.3
        link state           : up
      
      ```
      
      Run the **display mpls switch-l2vc brief** command on SPE1 and SPE2. The command output shows dynamic PW information. SPE1 is used as an example.
      
      ```
      [~SPE1] display mpls switch-l2vc brief
      ```
      ```
       Total Switch VC : 1, 1 up, 0 down
      
      *Switch-l2vc type             : LDP<---->LDP
       Peer IP Address              : 4.4.4.4, 1.1.1.1
       VC ID                        : 3, 1
       VC Type                      : VLAN
       VC State                     : up
       Session State                : up, up  
      ```
4. Configure PW APS.
   1. Configure PW APS instances.
      
      
      
      Configure a PW APS instance on PE1 and PE2.
      
      # Configure PE1.
      
      ```
      [~PE1] pw-aps 1
      ```
      ```
      [*PE1-pw-aps-1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] pw-aps 2
      ```
      ```
      [*PE2-pw-aps-2] quit
      ```
      ```
      [*PE2] commit
      ```
   2. Bind PWs to PW APS instances.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vpn pw-aps 1 admin
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface gigabitethernet 0/1/2.1
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] mpls l2vpn pw-aps 2 admin
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      Run the **display mpls l2vpn pw-aps verbose** command on PE1 and PE2. The command output shows information about PW APS instances and their associated PWs. PE1 and PE2 are used as examples.
      
      ```
      [~PE1] display mpls l2vpn pw-aps verbose
      ```
      ```
       APS Information:
         Description            :--
         Local Id               : 1
         Status                 : NR
         Work Path Status       : NoDefect
         Protect Path Status    : NoDefect
         Far End Status         : NR
         Request Result         : Work
         Wtr Interval(s)        : 300
         HoldOff Interval(ms)   : 0
         Operation Type         : Revertive
         Role                   : --
         Remote Id              : --
         Alarm Info             : None
         Total VPN Number       : 1
       ----------------------------------------
       PW Information:
         Number                 : 1
         Client Interface       : GigabitEthernet0/1/0.1
         Bind Type              : admin
        Primary PW:
          VC ID                 : 1
          VC Type               : VLAN
          Destination           : 2.2.2.2
          VC State              : up
        Secondary PW:
          VC ID                 : 2
          VC Type               : VLAN
          Destination           : 3.3.3.3
          VC State              : up  
      ```
      ```
      [~PE2] display mpls l2vpn pw-aps verbose
      ```
      ```
       APS Information:
         Description            :--
         Local Id               : 1
         Work Path Status       : NoDefect
         Protect Path Status    : NoDefect
         Far End Status         : NR
         Request Result         : Work
         Wtr Interval(s)        : 300
         HoldOff Interval(ms)   : 0
         Operation Type         : Revertive
         Role                   : --
         Remote Id              : --
         Alarm Info             : None
         Total VPN Number       : 0
       ----------------------------------------
       PW Information:
         Number                 : 1
         Client Interface       : GigabitEthernet0/1/2.1
         Bind Type              : admin
        Primary PW:
          VC ID                 : 3
          VC Type               : VLAN
          Destination           : 2.2.2.2
          VC State              : up
        Secondary PW:
          VC ID                 : 4
          VC Type               : VLAN
          Destination           : 3.3.3.3
          VC State              : up     
      ```
5. Configure MPLS OAM to detect PW status.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls
   ```
   ```
   [*PE1-mpls] mpls oam
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] mpls-oam
   ```
   ```
   [*PE1-mpls-oam] mpls oam l2vc peer-ip 2.2.2.2 vc-id 1 vc-type vlan remote-peer-ip 4.4.4.4 remote-vc-id 3 remote-vc-type vlan type cv auto-protocol
   ```
   ```
   [*PE1-mpls-oam] mpls oam l2vc peer-ip 3.3.3.3 vc-id 2 vc-type vlan remote-peer-ip 4.4.4.4 remote-vc-id 4 remote-vc-type vlan type cv auto-protocol
   ```
   ```
   [*PE1-mpls-oam] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls
   ```
   ```
   [*PE2-mpls] mpls oam
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] mpls-oam
   ```
   ```
   [*PE2-mpls-oam] mpls oam l2vc peer-ip 2.2.2.2 vc-id 3 vc-type vlan remote-peer-ip 1.1.1.1 remote-vc-id 1 remote-vc-type vlan type cv auto-protocol
   ```
   ```
   [*PE2-mpls-oam] mpls oam l2vc peer-ip 3.3.3.3 vc-id 4 vc-type vlan remote-peer-ip 1.1.1.1 remote-vc-id 2 remote-vc-type vlan type cv auto-protocol
   ```
   ```
   [*PE2-mpls-oam] quit
   ```
   ```
   [*PE2] commit
   ```
   
   Check MPLS OAM information on PE1.
   
   ```
   [~PE1] display mpls oam l2vc all
   ```
   ```
   --------------------------------------------------------------------------------
   
   Total Oam Num:                    2
   Total Start Oam Num:              2
   Total Defect Oam Num:             0
   --------------------------------------------------------------------------------
   
   No.  Peer IP        VC Type             VC ID          Status
   --------------------------------------------------------------------------------
   
   1    2.2.2.2        vlan                3              Start/Non-defect
   2    3.3.3.3        vlan                4              Start/Non-defect     
   ```
6. Verify the configuration.
   
   
   
   # Ping a GE sub-interface of CE2 from CE1.
   
   ```
   [~CE1] ping 10.1.1.2
   ```
   ```
   PING 10.1.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=40 ms
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=30 ms
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=40 ms
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=1 ms
   
     --- 10.1.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/22/40 ms  
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #                                                                               
  sysname CE1                                                                     
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 10                                                             
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
   mpls te                                                                        
   label advertise non-null                                                       
   mpls rsvp-te                                                                   
   mpls oam                                                                       
   mpls te cspf                                                                   
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  pw-aps 1                                                                        
  #                                                                               
  explicit-path 1to2                                                              
   next hop 10.1.2.2                                                              
   next hop 2.2.2.2                                                               
  #                                                                               
  explicit-path 1to3                                                              
   next hop 10.1.3.2                                                              
   next hop 3.3.3.3                                                               
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 2.2.2.2                                                    
   remote-ip 2.2.2.2                                                              
  #                                                                               
  mpls ldp remote-peer 3.3.3.3                                                    
   remote-ip 3.3.3.3                                                                                                                           
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 10                                                             
   mpls l2vc 2.2.2.2 1 tunnel-policy policy1 control-word                         
   mpls l2vc 3.3.3.3 2 tunnel-policy policy1 control-word secondary
   mpls l2vpn stream-dual-receiving               
   mpls l2vpn pw-aps 1 admin                                                      
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.2.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 10.1.3.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface LoopBack0                                                             
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                                               
  interface Tunnel10                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 100                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 2.2.2.2 tunnel-id 100      
   mpls te path explicit-path 1to2                                                
   mpls te reserved-for-binding                                                   
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te tunnel-id 200                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 3.3.3.3 tunnel-id 200      
   mpls te path explicit-path 1to3                                                
   mpls te reserved-for-binding                                                   
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 10.1.2.0 0.0.0.255                                                    
    network 1.1.1.1 0.0.0.0                                                       
    network 10.1.3.0 0.0.0.255                                                    
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel10                              
   tunnel binding destination 3.3.3.3 te Tunnel11                              
  #                                                                               
  mpls-oam                                                                        
   mpls oam l2vc peer-ip 2.2.2.2 vc-id 1 vc-type vlan remote-peer-ip 4.4.4.4 remote-vc-id 3 remote-vc-type vlan type cv auto-protocol
   mpls oam l2vc peer-ip 3.3.3.3 vc-id 2 vc-type vlan remote-peer-ip 4.4.4.4 remote-vc-id 4 remote-vc-type vlan type cv auto-protocol
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
   mpls te                                                                        
   label advertise non-null                                                       
   mpls rsvp-te                                                                   
   mpls oam                                                                       
   mpls te cspf                                                                   
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  pw-aps 2                                                                        
  #                                                                               
  explicit-path 4to2                                                              
   next hop 10.1.4.1                                                              
   next hop 2.2.2.2                                                               
  #                                                                               
  explicit-path 4to3                                                              
   next hop 10.1.5.1                                                              
   next hop 3.3.3.3                                                               
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 2.2.2.2                                                    
   remote-ip 2.2.2.2                                                              
  #                                                                               
  mpls ldp remote-peer 3.3.3.3                                                    
   remote-ip 3.3.3.3                                                              
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.1.4.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
   mpls ldp                                                                       
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.5.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/2.1                                                
   vlan-type dot1q 10                                                             
   mpls l2vc 2.2.2.2 3 tunnel-policy policy1 control-word                         
   mpls l2vc 3.3.3.3 4 tunnel-policy policy1 control-word secondary
   mpls l2vpn stream-dual-receiving               
   mpls l2vpn pw-aps 2 admin                                                      
  #                                                                               
  interface LoopBack0                                                             
   ip address 4.4.4.4 255.255.255.255                                             
  # 
  interface Tunnel10                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 300                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 2.2.2.2 tunnel-id 300      
   mpls te path explicit-path 4to2                                                
   mpls te reserved-for-binding                                                   
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te tunnel-id 400                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 3.3.3.3 tunnel-id 400      
   mpls te path explicit-path 4to3                                                
   mpls te reserved-for-binding                                                   
  #                                                                            
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 10.1.4.0 0.0.0.255                                                    
    network 10.1.5.0 0.0.0.255                                                    
    network 4.4.4.4 0.0.0.0                                                       
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel10                              
   tunnel binding destination 3.3.3.3 te Tunnel11                              
  #                                                                               
  mpls-oam                                                                        
   mpls oam l2vc peer-ip 2.2.2.2 vc-id 3 vc-type vlan remote-peer-ip 1.1.1.1 remote-vc-id 1 remote-vc-type vlan type cv auto-protocol
   mpls oam l2vc peer-ip 3.3.3.3 vc-id 4 vc-type vlan remote-peer-ip 1.1.1.1 remote-vc-id 2 remote-vc-type vlan type cv auto-protocol
  #                                                                               
  return 
  ```
* SPE1 configuration file
  
  ```
  #                                                                               
  sysname SPE1                                                                    
  #                                                                               
  mpls lsr-id 2.2.2.2
  #                                                             
  mpls                                                                            
   mpls te                                                                        
   label advertise non-null                                                       
   mpls rsvp-te                                                                   
   mpls te cspf                                                                   
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls switch-l2vc 4.4.4.4 3 tunnel-policy policy1 between 1.1.1.1 1 tunnel-policy policy1 encapsulation vlan control-word-transparent         
  #                                                                               
  explicit-path 2to1                                                              
   next hop 10.1.2.1                                                              
   next hop 1.1.1.1                                                               
  #                                                                               
  explicit-path 2to4                                                              
   next hop 10.1.4.2                                                              
   next hop 4.4.4.4                                                               
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                    
   remote-ip 1.1.1.1                                                              
  #                                                                               
  mpls ldp remote-peer 4.4.4.4                                                    
   remote-ip 4.4.4.4                                                              
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.1.2.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.4.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface LoopBack0                                                             
   ip address 2.2.2.2 255.255.255.255                                             
  #                                                                               
  interface Tunnel10                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 1.1.1.1                                                            
   mpls te tunnel-id 100                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 100      
   mpls te path explicit-path 2to1                                                
   mpls te reserved-for-binding                                                   
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 4.4.4.4                                                            
   mpls te tunnel-id 300                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 4.4.4.4 tunnel-id 300      
   mpls te path explicit-path 2to4                                                
   mpls te reserved-for-binding                                                   
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 10.1.4.0 0.0.0.255                                                    
    network 10.1.2.0 0.0.0.255                                                    
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel10                              
   tunnel binding destination 4.4.4.4 te Tunnel11                              
  #                                                                               
  return   
  ```
* SPE2 configuration file
  
  ```
  #                                                                               
  sysname SPE2                                                                    
  #                                                                               
  mpls lsr-id 3.3.3.3
  #                                                             
  mpls                                                                            
   mpls te                                                                        
   label advertise non-null                                                       
   mpls rsvp-te                                                                   
   mpls te cspf                                                                   
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls switch-l2vc 4.4.4.4 4 tunnel-policy policy1 between 1.1.1.1 2 tunnel-policy policy1 encapsulation vlan control-word-transparent
  #                                                                                       
  explicit-path 3to1                                                              
   next hop 10.1.3.1                                                              
   next hop 1.1.1.1                                                               
  #                                                                               
  explicit-path 3to4                                                              
   next hop 10.1.5.2                                                              
   next hop 4.4.4.4                                                               
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                    
   remote-ip 1.1.1.1                                                              
  #                                                                               
  mpls ldp remote-peer 4.4.4.4                                                    
   remote-ip 4.4.4.4                                                              
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.1.3.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.5.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface LoopBack0                                                             
   ip address 3.3.3.3 255.255.255.255                                             
  #                                                                              
  interface Tunnel10                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 1.1.1.1                                                            
   mpls te tunnel-id 200                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 300      
   mpls te path explicit-path 3to1                                                
   mpls te reserved-for-binding                                                   
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 4.4.4.4                                                            
   mpls te tunnel-id 400                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 4.4.4.4 tunnel-id 400      
   mpls te path explicit-path 3to4                                                
   mpls te reserved-for-binding                                               
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 3.3.3.3 0.0.0.0                                                       
    network 10.1.3.0 0.0.0.255                                                    
    network 10.1.4.0 0.0.0.255                                                    
    network 10.1.5.0 0.0.0.255                                                    
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel10                              
   tunnel binding destination 4.4.4.4 te Tunnel11                              
  #                                                                               
  return    
  ```
* CE2 configuration file
  
  ```
  #                                                                               
  sysname CE2
  #                                                                               
  vlan batch 10
  #                                                                               
  interface Vlanif10                                                              
   ip address 10.1.1.2 255.255.255.0                                              
  #                                                                               
  interface Eth-Trunk10                                                          
   portswitch                                                                     
   port trunk allow-pass vlan 10                                                  
   mode lacp-static                                                               
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   eth-trunk 10                                                                   
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   eth-trunk 10                                                                   
  #                                                                               
  return 
  ```