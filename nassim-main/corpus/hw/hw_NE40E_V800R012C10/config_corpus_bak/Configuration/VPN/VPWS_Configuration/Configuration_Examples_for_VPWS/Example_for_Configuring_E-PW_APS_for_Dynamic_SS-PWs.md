Example for Configuring E-PW APS for Dynamic SS-PWs
===================================================

In E-PW APS scenarios, MPLS OAM is used to detect the status of dynamic SS-PWs.

#### Networking Requirements

On the public network show in [Figure 1](#EN-US_TASK_0172369987__fig_dc_vrp_vpws_cfg_604001), three PEs belong to the same IGP domain and two dynamic associated bidirectional LSPs are deployed. In addition, CE1 and CE2 need to reliably communicate through the three PEs on the public network.

To meet this requirement, configure E-PW APS for dynamic PWs. As the three PEs belong to the same IGP domain, the PWs can be SS-PWs.

**Figure 1** Configuring E-PW APS for dynamic SS-PWs![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1, subinterface1.1, interface2, and interface3 represent GE0/1/0, GE0/1/0.1, GE0/1/1, and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_604001.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses and a routing protocol.
2. Configure MPLS and public network tunnels.
   
   In this example, dynamic associated bidirectional LSPs are used between PE1 and PE2, between PE1 and PE3, and between PE2 and PE3. The specific configurations include:
   
   * Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and CSPF.
   * Configure OSPF TE.
   * Configure dynamic associated bidirectional LSPs.
3. Configure a PW protection group, which includes:
   
   * Configure a primary PW between PE1 and PE2.
   * Configure a secondary PW between PE1 and PE3.
   * Configure a bypass PW between PE2 and PE3.
4. Configure E-PW APS, which includes:
   
   * Configure a PW APS instance on PE1.
   * Configure an E-PW APS instance on PE2 and PE3.
   * Bind PWs to PW APS instances.
5. Configure MPLS OAM to detect PW status.
6. Configure CEs to access the L2VPN through VLANs on the AC side.

#### Data Preparation

To complete the configuration, you need the following data:

* PEs' interface numbers, IP addresses and OSPF process IDs
* Each PE's LSR ID, tunnel interface numbers and IP addresses, and tunnel IDs and ingress LSR IDs of reverse RSVP LSPs
* Destination IP addresses, VC IDs, and VC types of L2VCs and transmit/receive labels of dynamic PWs
* APS instance numbers and the master/slave roles, local numbers, and remote numbers of the E-PW APS instances on PEs (the E-PW APS role is slave for PE2 and master for PE3)

#### Procedure

1. Configure interface IP addresses and a routing protocol.
   
   
   
   Configure an IP address and mask for each involved interface. For detailed configurations, see Configuration Files.
   
   In this example, OSPF is used as the IGP for PE1, PE2, and PE3 to communicate at the network layer. The configuration details are not provided here.
2. Configure MPLS and public network tunnels.
   
   
   
   In this example, dynamic associated bidirectional LSPs are used between PE1, PE2, and PE3.
   
   
   
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
      
      The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see Configuration Files.
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
      
      The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see Configuration Files.
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
      
      The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see Configuration Files.
   4. Configure dynamic associated bidirectional LSPs.
      
      
      
      # Configure an LSP from PE1 to PE2 and bind it to the LSP from PE2 to PE1, and configure an LSP from PE1 to PE3 and bind it to the LSP from PE3 to PE1.
      
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
      [*PE1] interface Tunnel11
      ```
      ```
      [*PE1-Tunnel11] ip address unnumbered interface loopback 0
      ```
      ```
      [*PE1-Tunnel11] tunnel-protocol mpls te
      ```
      ```
      [*PE1-Tunnel11] destination 3.3.3.3
      ```
      ```
      [*PE1-Tunnel11] mpls te tunnel-id 200
      ```
      ```
      [*PE1-Tunnel11] mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 3.3.3.3 tunnel-id 200
      ```
      ```
      [*PE1-Tunnel11] mpls te path explicit-path 1to3
      ```
      ```
      [*PE1-Tunnel11] quit
      ```
      ```
      [*PE1] commit
      ```
      
      The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see Configuration Files.
      
      Run the **display mpls te reverse-lsp** command on PE1, PE2, and PE3 to check information about the dynamic associated bidirectional LSPs. PE1 is used as an example.
      
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
3. Configure a dynamic PW protection group.
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
      [*PE2] interface Tunnel12
      ```
      ```
      [*PE2-Tunnel12] mpls te reserved-for-binding
      ```
      ```
      [*PE2-Tunnel12] quit
      ```
      ```
      [*PE2] tunnel-policy policy1
      ```
      ```
      [*PE2-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel10
      ```
      ```
      [*PE2-tunnel-policy-policy1] tunnel binding destination 3.3.3.3 te Tunnel12
      ```
      ```
      [*PE2-tunnel-policy-policy1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface Tunnel11
      ```
      ```
      [*PE3-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*PE3-Tunnel11] quit
      ```
      ```
      [*PE3] interface Tunnel12
      ```
      ```
      [*PE3-Tunnel12] mpls te reserved-for-binding
      ```
      ```
      [*PE3-Tunnel12] quit
      ```
      ```
      [*PE3] tunnel-policy policy1
      ```
      ```
      [*PE3-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel11
      ```
      ```
      [*PE3-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel12
      ```
      ```
      [*PE3-tunnel-policy-policy1] quit
      ```
      ```
      [*PE3] commit
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
      [*PE2] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*PE2-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
      ```
      ```
      [*PE2-mpls-ldp-remote-1.1.1.1] quit
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
      
      # Configure PE3.
      
      ```
      [~PE3] mpls ldp
      ```
      ```
      [*PE3-mpls-ldp] quit
      ```
      ```
      [*PE3] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*PE3-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
      ```
      ```
      [*PE3-mpls-ldp-remote-1.1.1.1] quit
      ```
      ```
      [*PE3] mpls ldp remote-peer 2.2.2.2
      ```
      ```
      [*PE3-mpls-ldp-remote-2.2.2.2] remote-ip 2.2.2.2
      ```
      ```
      [*PE3-mpls-ldp-remote-2.2.2.2] quit
      ```
      ```
      [*PE3] commit
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
      
      # Configure the primary and bypass PWs on PE2.
      
      ```
      [~PE2] mpls l2vpn
      ```
      ```
      [*PE2-l2vpn] quit
      ```
      ```
      [*PE2] interface eth-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] quit
      ```
      ```
      [*PE2] interface eth-trunk 10.1
      ```
      ```
      [*PE2-Eth-Trunk10.1] vlan-type dot1q 10
      ```
      ```
      [*PE2-Eth-Trunk10.1] mpls l2vc 1.1.1.1 1 tunnel-policy policy1 control-word
      ```
      ```
      [*PE2-Eth-Trunk10.1] mpls l2vc 3.3.3.3 3 tunnel-policy policy1 control-word bypass
      ```
      ```
      [*PE2-Eth-Trunk10.1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure the primary and bypass PWs on PE3.
      
      ```
      [~PE3] mpls l2vpn
      ```
      ```
      [*PE3-l2vpn] quit
      ```
      ```
      [*PE3] interface eth-trunk 10
      ```
      ```
      [*PE3-Eth-Trunk10] quit
      ```
      ```
      [*PE3] interface eth-trunk 10.1
      ```
      ```
      [*PE3-Eth-Trunk10.1] vlan-type dot1q 10
      ```
      ```
      [*PE3-Eth-Trunk10.1] mpls l2vc 1.1.1.1 2 tunnel-policy policy1 control-word
      ```
      ```
      [*PE3-Eth-Trunk10.1] mpls l2vc 2.2.2.2 3 tunnel-policy policy1 control-word bypass
      ```
      ```
      [*PE3-Eth-Trunk10.1] quit
      ```
      ```
      [*PE3] commit
      ```
4. Configure E-PW APS.
   1. Configure PW APS instances.
      
      
      
      Configure a PW APS instance on PE1 and an E-PW APS instance on PE2 and PE3.
      
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
      [*PE2-pw-aps-2] role slave
      ```
      ```
      [*PE2-pw-aps-2] remote-aps 3
      ```
      ```
      [*PE2-pw-aps-2] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] pw-aps 3
      ```
      ```
      [*PE3-pw-aps-3] role master
      ```
      ```
      [*PE3-pw-aps-3] remote-aps 2
      ```
      ```
      [*PE3-pw-aps-3] quit
      ```
      ```
      [*PE3] commit
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
      [~PE2] interface eth-trunk 10.1
      ```
      ```
      [*PE2-Eth-Trunk10.1] mpls l2vpn pw-aps 2 admin
      ```
      ```
      [*PE2-Eth-Trunk10.1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface eth-trunk 10.1
      ```
      ```
      [*PE3-Eth-Trunk10.1] mpls l2vpn pw-aps 3 admin
      ```
      ```
      [*PE3-Eth-Trunk10.1] quit
      ```
      ```
      [*PE3] commit
      ```
      
      Run the **display mpls l2vpn pw-aps verbose** command on PE1, PE2, and PE3. The command output shows information about PW APS instances and their associated PWs.
      
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
         Status                 : --
         Work Path Status       : --
         Protect Path Status    : --
         Far End Status         : --
         Request Result         : Work
         Wtr Interval(s)        : 300
         HoldOff Interval(ms)   : 0
         Operation Type         : Revertive
         Role                   : Slave
         Remote Id              : 3
         Alarm Info             : None
         Total VPN Number       : 1
       ----------------------------------------
       PW Information:
         Number                 : 1
         Client Interface       : Eth-Trunk10.1
         Bind Type              : admin
        Primary PW:
          VC ID                 : 1
          VC Type               : VLAN
          Destination           : 1.1.1.1
          VC State              : up
        Secondary PW:
          VC ID                 : 3
          VC Type               : VLAN
          Destination           : 3.3.3.3
          VC State              : up  
      ```
      ```
      [~PE3] display mpls l2vpn pw-aps verbose
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
         Role                   : Master
         Remote Id              : 2
         Alarm Info             : None
         Total VPN Number       : 1
       ----------------------------------------
       PW Information:
         Number                 : 1
         Client Interface       : Eth-Trunk10.1
         Bind Type              : admin
        Primary PW:
          VC ID                 : 2
          VC Type               : VLAN
          Destination           : 1.1.1.1
          VC State              : up
        Secondary PW:
          VC ID                 : 3
          VC Type               : VLAN
          Destination           : 2.2.2.2
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
   [*PE1-mpls-oam] mpls oam l2vc peer-ip 2.2.2.2 vc-id 1 vc-type vlan type cv
   ```
   ```
   [*PE1-mpls-oam] mpls oam l2vc peer-ip 3.3.3.3 vc-id 2 vc-type vlan type cv
   ```
   ```
   [*PE1-mpls-oam] mpls oam l2vc enable receive peer-ip 2.2.2.2 vc-id 1 vc-type vlan
   ```
   ```
   [*PE1-mpls-oam] mpls oam l2vc enable send peer-ip 2.2.2.2 vc-id 1 vc-type vlan
   ```
   ```
   [*PE1-mpls-oam] mpls oam l2vc enable receive peer-ip 3.3.3.3 vc-id 2 vc-type vlan
   ```
   ```
   [*PE1-mpls-oam] mpls oam l2vc enable send peer-ip 3.3.3.3 vc-id 2 vc-type vlan
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
   [*PE2-mpls-oam] mpls oam l2vc peer-ip 1.1.1.1 vc-id 3 vc-type vlan type cv
   ```
   ```
   [*PE2-mpls-oam] mpls oam l2vc peer-ip 3.3.3.3 vc-id 6 vc-type vlan type cv
   ```
   ```
   [*PE2-mpls-oam] mpls oam l2vc enable receive peer-ip 1.1.1.1 vc-id 3 vc-type vlan
   ```
   ```
   [*PE2-mpls-oam] mpls oam l2vc enable send peer-ip 1.1.1.1 vc-id 3 vc-type vlan
   ```
   ```
   [*PE2-mpls-oam] mpls oam l2vc enable receive peer-ip 3.3.3.3 vc-id 6 vc-type vlan
   ```
   ```
   [*PE2-mpls-oam] mpls oam l2vc enable send peer-ip 3.3.3.3 vc-id 6 vc-type vlan
   ```
   ```
   [*PE2-mpls-oam] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls
   ```
   ```
   [*PE3-mpls] mpls oam
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] mpls-oam
   ```
   ```
   [*PE3-mpls-oam] mpls oam l2vc peer-ip 1.1.1.1 vc-id 4 vc-type vlan type cv
   ```
   ```
   [*PE3-mpls-oam] mpls oam l2vc peer-ip 2.2.2.2 vc-id 5 vc-type vlan type cv
   ```
   ```
   [*PE3-mpls-oam] mpls oam l2vc enable receive peer-ip 1.1.1.1 vc-id 4 vc-type vlan
   ```
   ```
   [*PE3-mpls-oam] mpls oam l2vc enable send peer-ip 1.1.1.1 vc-id 4 vc-type vlan
   ```
   ```
   [*PE3-mpls-oam] mpls oam l2vc enable receive peer-ip 2.2.2.2 vc-id 5 vc-type vlan
   ```
   ```
   [*PE3-mpls-oam] mpls oam l2vc enable send peer-ip 2.2.2.2 vc-id 5 vc-type vlan
   ```
   ```
   [*PE3-mpls-oam] quit
   ```
   ```
   [*PE3] commit
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
   
   1    2.2.2.2        vlan                1              Start/Non-defect
   2    3.3.3.3        vlan                2              Start/Non-defect     
   ```
6. Configure dual-homing protection on the AC side.
   1. Configure Eth-Trunk interfaces.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE2] interface eth-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] mode lacp-static
      ```
      ```
      [*PE2-Eth-Trunk10] trunkport gigabitethernet 0/1/2
      ```
      ```
      [*PE2-Eth-Trunk10] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE3-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE3-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE3] interface eth-trunk 10
      ```
      ```
      [*PE3-Eth-Trunk10] mode lacp-static
      ```
      ```
      [*PE3-Eth-Trunk10] trunkport gigabitethernet 0/1/2
      ```
      ```
      [*PE3-Eth-Trunk10] quit
      ```
      ```
      [*PE3] commit
      ```
      
      # Configure CE2.
      
      ```
      [~CE2] interface gigabitethernet 0/1/0
      ```
      ```
      [~CE2-GigabitEthernet0/1/0] undo shutdown
      ```
      ```
      [*CE2-GigabitEthernet0/1/0] quit
      ```
      ```
      [*CE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*CE2-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*CE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*CE2] interface eth-trunk 10
      ```
      ```
      [*CE2-Eth-Trunk10] portswitch
      ```
      ```
      [*CE2-Eth-Trunk10] mode lacp-static
      ```
      ```
      [*CE2-Eth-Trunk10] port trunk allow-pass vlan 10
      ```
      ```
      [*CE2-Eth-Trunk10] trunkport gigabitethernet 0/1/0 to 0/1/1
      ```
      ```
      [*CE2-Eth-Trunk10] quit
      ```
      ```
      [*CE2] vlan 10
      ```
      ```
      [*CE2-vlan10] quit
      ```
      ```
      [*CE2] commit
      ```
   2. Configure E-Trunk.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] lacp e-trunk system-id 00e0-fc00-0000
      ```
      ```
      [*PE2] lacp e-trunk priority 100
      ```
      ```
      [*PE2] e-trunk 10
      ```
      ```
      [*PE2-e-trunk-10] security-key cipher YsHsjx_202206
      ```
      ```
      [*PE2-e-trunk-10] priority 10
      ```
      ```
      [*PE2-e-trunk-10] peer-address 3.3.3.3 source-address 2.2.2.2
      ```
      ```
      [*PE2-e-trunk-10] quit
      ```
      ```
      [*PE2] interface eth-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] e-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] quit
      ```
      ```
      [*PE2] commit
      ```
      
      # Configure PE3.
      
      ```
      [~PE3] lacp e-trunk system-id 00e0-fc00-0000
      ```
      ```
      [*PE3] lacp e-trunk priority 100
      ```
      ```
      [*PE3] e-trunk 10
      ```
      ```
      [*PE3-e-trunk-10] security-key cipher YsHsjx_202206
      ```
      ```
      [*PE3-e-trunk-10] priority 20
      ```
      ```
      [*PE3-e-trunk-10] peer-address 2.2.2.2 source-address 3.3.3.3
      ```
      ```
      [*PE3-e-trunk-10] quit
      ```
      ```
      [*PE3] interface eth-trunk 10
      ```
      ```
      [*PE3-Eth-Trunk10] e-trunk 10
      ```
      ```
      [*PE3-Eth-Trunk10] quit
      ```
      ```
      [*PE3] commit
      ```
7. Verify the configuration.
   
   
   
   Ping the address of the VLANIF interface on CE2 from CE1.
   
   # Configure CE2.
   
   ```
   [~CE2]interface Vlanif 10
   ```
   ```
   [*CE2-Vlanif10] ip address 10.1.1.2 24
   ```
   ```
   [*CE2-Vlanif10] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Perform the ping operation.
   
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
   mpls oam l2vc peer-ip 2.2.2.2 vc-id 1 vc-type vlan type cv
   mpls oam l2vc peer-ip 3.3.3.3 vc-id 2 vc-type vlan type cv
   mpls oam l2vc enable receive peer-ip 2.2.2.2 vc-id 1 vc-type vlan
   mpls oam l2vc enable send peer-ip 2.2.2.2 vc-id 1 vc-type vlan
   mpls oam l2vc enable receive peer-ip 3.3.3.3 vc-id 2 vc-type vlan
   mpls oam l2vc enable send peer-ip 3.3.3.3 vc-id 2 vc-type vlan
  #                                                                               
  return   
  ```
* PE2 configuration file
  
  ```
  #                                                                               
  sysname PE2                                                                     
  #                                                                               
  lacp e-trunk system-id 00e0-fc00-0000                                           
  lacp e-trunk priority 100                                                       
  #                                                                               
  mpls lsr-id 2.2.2.2 
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
   role slave                                                                     
   remote-aps 3                                                                   
  #                                                                               
  explicit-path 2to1                                                              
   next hop 10.1.2.1                                                              
   next hop 1.1.1.1                                                               
  #                                                                               
  explicit-path 2to3                                                              
   next hop 10.1.4.2                                                              
   next hop 3.3.3.3                                                               
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                    
   remote-ip 1.1.1.1                                                              
  #                                                                               
  mpls ldp remote-peer 3.3.3.3                                                    
   remote-ip 3.3.3.3                                                              
  #
  e-trunk 10    
   security-key cipher YsHsjx_202206                                                                  
   priority 10                                                                    
   peer-address 3.3.3.3 source-address 2.2.2.2                                    
  #                                                                               
  interface Eth-Trunk10                                                           
   mode lacp-static                                                               
   e-trunk 10                                                                     
  #                                                                               
  interface Eth-Trunk10.1                                                         
   vlan-type dot1q 10                                                             
   mpls l2vc 1.1.1.1 1 tunnel-policy policy1 control-word
   mpls l2vc 3.3.3.3 3 tunnel-policy policy1 control-word bypass
   mpls l2vpn pw-aps 2 admin                                                      
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
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   eth-trunk 10                                                                   
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
  interface Tunnel12                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te tunnel-id 300                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 3.3.3.3 tunnel-id 300
   mpls te path explicit-path 2to3
   mpls te reserved-for-binding                                                   
  #                                                                               
  ospf 1                                                                          
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 10.1.4.0 0.0.0.255                                                    
    network 10.1.2.0 0.0.0.255  
    mpls-te enable                                                  
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel10                              
   tunnel binding destination 3.3.3.3 te Tunnel12                              
  #                                                                               
  mpls-oam                                                                        
   mpls oam l2vc peer-ip 1.1.1.1 vc-id 3 vc-type vlan type cv
   mpls oam l2vc peer-ip 3.3.3.3 vc-id 6 vc-type vlan type cv
   mpls oam l2vc enable receive peer-ip 1.1.1.1 vc-id 3 vc-type vlan
   mpls oam l2vc enable send peer-ip 1.1.1.1 vc-id 3 vc-type vlan
   mpls oam l2vc enable receive peer-ip 3.3.3.3 vc-id 6 vc-type vlan
   mpls oam l2vc enable send peer-ip 3.3.3.3 vc-id 6 vc-type vlan
  #
  return
  ```
* PE3 configuration file
  
  ```
  #                                                                               
  sysname PE3                                                                     
  #                                                                               
  lacp e-trunk system-id 00e0-fc00-0000                                           
  lacp e-trunk priority 100                                                       
  #                                                                               
  mpls lsr-id 3.3.3.3
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
  pw-aps 3                                                                        
   role master                                                                    
   remote-aps 2                                                                   
  #                                                                               
  explicit-path 3to1                                                              
   next hop 10.1.3.1                                                              
   next hop 1.1.1.1                                                               
  #                                                                               
  explicit-path 3to2                                                              
   next hop 10.1.4.1                                                              
   next hop 2.2.2.2                                                               
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                    
   remote-ip 1.1.1.1                                                              
  #                                                                               
  mpls ldp remote-peer 2.2.2.2                                                    
   remote-ip 2.2.2.2                                                              
  #                                                                               
  e-trunk 10     
   security-key cipher YsHsjx_202206                                                                 
   priority 20                                                                    
   peer-address 2.2.2.2 source-address 3.3.3.3                                    
  #                                                                               
  interface Eth-Trunk10                                                           
   mode lacp-static                                                               
   e-trunk 10                                                                     
  #                                                                               
  interface Eth-Trunk10.1
   vlan-type dot1q 10
   mpls l2vc 1.1.1.1 2 tunnel-policy policy1 control-word
   mpls l2vc 2.2.2.2 3 tunnel-policy policy1 control-word bypass
   mpls l2vpn pw-aps 3 admin                                                      
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
   ip address 10.1.4.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                              
  #
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   eth-trunk 10                                                                   
  #                                                                               
  interface LoopBack0                                                             
   ip address 3.3.3.3 255.255.255.255                                             
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 1.1.1.1                                                            
   mpls te tunnel-id 200                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 200
   mpls te path explicit-path 3to1                 
   mpls te reserved-for-binding                                                   
  #                                                                               
  interface Tunnel12                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 300                                                          
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 2.2.2.2 tunnel-id 300 
   mpls te path explicit-path 3to2                 
   mpls te reserved-for-binding                                                   
  #                                                                               
  ospf 1                                                                          
   area 0.0.0.0                                                                   
    network 3.3.3.3 0.0.0.0                                                       
    network 10.1.3.0 0.0.0.255                                                    
    network 10.1.4.0 0.0.0.255       
    mpls-te enable                                             
  #                                                                               
  static-cr-lsp egress 1to2 incoming-interface GigabitEthernet0/1/1 in-label 20   
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel11                              
   tunnel binding destination 2.2.2.2 te Tunnel12                              
  #                                                                               
  mpls-oam                                                                        
   mpls oam l2vc peer-ip 1.1.1.1 vc-id 4 vc-type vlan type cv
   mpls oam l2vc peer-ip 2.2.2.2 vc-id 5 vc-type vlan type cv
   mpls oam l2vc enable receive peer-ip 2.2.2.2 vc-id 5 vc-type vlan
   mpls oam l2vc enable send peer-ip 2.2.2.2 vc-id 5 vc-type vlan
   mpls oam l2vc enable receive peer-ip 1.1.1.1 vc-id 4 vc-type vlan
   mpls oam l2vc enable send peer-ip 1.1.1.1 vc-id 4 vc-type vlan
  #
  return
  ```
* CE2 configuration file
  
  ```
  #                                                                               
  sysname CE2                                                                     
  #    
  vlan 10
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