Example for Configuring PW APS for Static MS-PWs
================================================

In PW APS scenarios, MPLS OAM is used to detect the status of static MS-PWs.

#### Networking Requirements

On the public network shown in [Figure 1](#EN-US_TASK_0172369984__fig_dc_vrp_vpws_cfg_603901), static bidirectional co-routed LSPs need to be established between the four PEs. In addition, CE1 and CE2 need to reliably communicate through the four PEs on the public network.

PW redundancy needs to be deployed on PE1 and PE2. For primary and secondary PWs that share the same source and same destination and static bidirectional co-routed LSPs, consider deploying PW APS for static PWs. As the four PEs belong to different IGP domains, the PWs must be MS-PWs.

**Figure 1** Configuring PW APS for static MS-PWs![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1, subinterface1.1, interface2, and interface3 represent GE0/1/0, GE0/1/0.1, GE0/1/1, and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_603901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses and a routing protocol.
2. Configure MPLS and public network tunnels.
   
   In this example, static bidirectional co-routed LSPs are used between PEs and SPEs. The specific configurations include:
   
   * Configure basic MPLS functions and enable MPLS TE.
   * Configure MPLS TE tunnel interfaces.
   * Configure static bidirectional co-routed LSPs.
3. Configure a PW protection group (static MS-PWs are used in this example), which includes:
   
   * Configure a PW protection group on PE1 and PE2.
   * Configure a static switched PW on SPE1 and SPE2.
4. Configure PW APS, which includes:
   
   * Configure a PW APS instance on PE1 and PE2.
   * Bind the PW protection group to the PW APS instance.
5. Configure MPLS OAM to detect PW status.

#### Data Preparation

To complete the configuration, you need the following data:

* PEs' interface numbers, IP addresses and OSPF process IDs
* Each PE's LSR ID, tunnel interface numbers and IP addresses, and tunnel IDs and ingress LSR IDs of reverse RSVP LSPs
* Local and remote IP addresses, VC IDs, and VC types of L2VCs
* APS instance numbers on PE1 and PE2

#### Procedure

1. Configure interface IP addresses and a routing protocol.
   
   
   
   Configure an IP address and mask for each involved interface according to [Figure 1](#EN-US_TASK_0172369984__fig_dc_vrp_vpws_cfg_603901). For detailed configurations, see Configuration Files.
   
   In this example, OSPF is used as the IGP for PE1, PE2, SPE1, and SPE2 to communicate at the network layer. The configuration details are not provided here.
2. Configure MPLS and public network tunnels.
   1. Configure basic MPLS functions and enable MPLS TE.
      
      
      
      Enable MPLS and MPLS TE both globally and per interface on nodes along the TE tunnel.
      
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
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      The configurations of PE2 and SPE1 are similar to that of SPE2. For detailed configurations, see Configuration Files.
   2. Configure MPLS TE tunnel interfaces.
      
      
      
      # On PE1, configure an MPLS TE tunnel from PE1 to SPE1 and from PE1 to SPE2.
      
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
      [*PE1-Tunnel10] mpls te signal-protocol cr-static
      ```
      ```
      [*PE1-Tunnel10] mpls te bidirectional
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
      [*PE1-Tunnel11] mpls te signal-protocol cr-static
      ```
      ```
      [*PE1-Tunnel11] mpls te bidirectional
      ```
      ```
      [*PE1-Tunnel11] quit
      ```
      ```
      [*PE1] commit
      ```
      
      The configurations of PE2 and SPE1 are similar to that of SPE2. For detailed configurations, see Configuration Files.
   3. Configure the ingress and egress for each static bidirectional co-routed LSP.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      A static bidirectional co-routed LSP can go up on the ingress only when the LSP name is the same as the tunnel interface name on the ingress. Note that the first letter of the tunnel interface name must be uppercase. The transit nodes and egress do not have this restriction.
      
      # Configure PE1 as the ingress for the static bidirectional co-routed LSP from PE1 to SPE1 and that from PE1 to SPE2.
      
      ```
      [~PE1] bidirectional static-cr-lsp ingress Tunnel10
      ```
      ```
      [*PE1-bi-static-ingress-Tunnel10] forward outgoing-interface GigabitEthernet0/1/1 nexthop 10.1.2.2 out-label 20
      ```
      ```
      [*PE1-bi-static-ingress-Tunnel10] backward in-label 30 lsrid 2.2.2.2 tunnel-id 100
      ```
      ```
      [*PE1] bidirectional static-cr-lsp ingress Tunnel11
      ```
      ```
      [*PE1-bi-static-ingress-Tunnel11] forward outgoing-interface GigabitEthernet0/1/2 nexthop 10.1.3.2 out-label 40
      ```
      ```
      [*PE1-bi-static-ingress-Tunnel11] backward in-label 50 lsrid 3.3.3.3 tunnel-id 200
      ```
      ```
      [*PE1-bi-static-ingress-Tunnel11] quit
      ```
      ```
      [*PE1] commit
      ```
      
      The configurations of PE2 and SPE1 are similar to that of SPE2. For detailed configurations, see Configuration Files.
   4. Configure reverse tunnel binding on SPE1 and SPE2.
      
      
      
      # Configure SPE1.
      
      ```
      [~SPE1] interface Tunnel10
      ```
      ```
      [*SPE1-Tunnel10] mpls te passive-tunnel
      ```
      ```
      [*SPE1-Tunnel10] mpls te binding bidirectional static-cr-lsp egress Tunnel10
      ```
      ```
      [*SPE1-Tunnel10] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] interface Tunnel11
      ```
      ```
      [*SPE2-Tunnel11] mpls te passive-tunnel
      ```
      ```
      [*SPE2-Tunnel11] mpls te binding bidirectional static-cr-lsp egress Tunnel11
      ```
      ```
      [*SPE2-Tunnel11] quit
      ```
      ```
      [*SPE2] interface Tunnel12
      ```
      ```
      [*SPE2-Tunnel12] mpls te passive-tunnel
      ```
      ```
      [*SPE2-Tunnel12] mpls te binding bidirectional static-cr-lsp egress Tunnel12
      ```
      ```
      [*SPE2-Tunnel12] quit
      ```
      ```
      [*SPE2] commit
      ```
      
      Run the **display mpls te bidirectional static-cr-lsp** command on PE1, PE2, SPE1, and SPE2 to check information about static bidirectional co-routed LSPs. PE1 is used as an example.
      
      ```
      [~PE1] display mpls te bidirectional static-cr-lsp
      ```
      ```
      TOTAL          : 2     STATIC CRLSP(S)
      UP             : 2     STATIC CRLSP(S)
      DOWN           : 0     STATIC CRLSP(S)
      Name                FEC                I/O Label    I/O If                Status
      Tunnel10         2.2.2.2/32         NULL/20      -/GE0/1/1
                                             30/NULL      GE0/1/1/-             Up
      Tunnel11         3.3.3.3/32         NULL/40      -/GE0/1/2
                                             50/NULL      GE0/1/2/-             Up
      ```
      
      Run the **ping lsp** command on PE1, PE2, SPE1, and SPE2 to check LSP connectivity. If the ping operations succeed, the static bidirectional co-routed LSPs have been established. A tunnel on PE1 is used as an example.
      
      ```
      [~PE1] ping lsp -r 4 te Tunnel 11
      ```
      ```
        LSP PING FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel11 : 100  data bytes, press CTRL_C to break
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
   
   
   
   Static MS-PWs are used in this example.
   
   
   
   # Configure the primary and secondary static PWs on PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] tunnel-policy 1
   ```
   ```
   [*PE1-tunnel-policy-1] tunnel binding destination 2.2.2.2 te Tunnel10
   ```
   ```
   [*PE1-tunnel-policy-1] tunnel binding destination 3.3.3.3 te Tunnel11
   ```
   ```
   [*PE1-tunnel-policy-1] quit
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
   [*PE1-GigabitEthernet0/1/0.1] mpls static-l2vc destination 2.2.2.2 1 transmit-vpn-label 100 receive-vpn-label 200 tunnel-policy 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] mpls static-l2vc destination 3.3.3.3 2 transmit-vpn-label 300 receive-vpn-label 400 tunnel-policy 1 secondary
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] mpls l2vpn pw-ttl 2
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] mpls l2vpn pw-ttl 2 secondary
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the primary and secondary static PWs on PE2.
   
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] tunnel-policy 1
   ```
   ```
   [*PE2-tunnel-policy-1] tunnel binding destination 2.2.2.2 te Tunnel11
   ```
   ```
   [*PE2-tunnel-policy-1] tunnel binding destination 3.3.3.3 te Tunnel10
   ```
   ```
   [*PE2-tunnel-policy-1] quit
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
   [*PE2-GigabitEthernet0/1/2.1] mpls static-l2vc destination 2.2.2.2 1 transmit-vpn-label 500 receive-vpn-label 600 tunnel-policy 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/2.1] mpls static-l2vc destination 3.3.3.3 2 transmit-vpn-label 700 receive-vpn-label 800 tunnel-policy 1 secondary
   ```
   ```
   [*PE2-GigabitEthernet0/1/2.1] mpls l2vpn pw-ttl 2
   ```
   ```
   [*PE2-GigabitEthernet0/1/2.1] mpls l2vpn pw-ttl 2 secondary
   ```
   ```
   [*PE2-GigabitEthernet0/1/2.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure a static switched VC on SPE1.
   
   ```
   [~SPE1] mpls l2vpn
   ```
   ```
   [*SPE1-l2vpn] quit
   ```
   ```
   [*SPE1] tunnel-policy 1
   ```
   ```
   [*SPE1-tunnel-policy-1] tunnel binding destination 1.1.1.1 te Tunnel10
   ```
   ```
   [*SPE1-tunnel-policy-1] tunnel binding destination 4.4.4.4 te Tunnel11
   ```
   ```
   [*SPE1-tunnel-policy-1] quit
   ```
   ```
   [*SPE1] mpls switch-l2vc instance-name 1 1.1.1.1 1 trans 200 recv 100 tunnel-policy 1 between 4.4.4.4 1 trans 600 recv 500 tunnel-policy 1 encapsulation vlan control-word
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure a static switched PW on SPE2.
   
   ```
   [*SPE2] mpls l2vpn
   ```
   ```
   [*SPE2-l2vpn] quit
   ```
   ```
   [*SPE2] tunnel-policy 1
   ```
   ```
   [*SPE2-tunnel-policy-1] tunnel binding destination 1.1.1.1 te Tunnel11
   ```
   ```
   [*SPE2-tunnel-policy-1] tunnel binding destination 4.4.4.4 te Tunnel10
   ```
   ```
   [*SPE2-tunnel-policy-1] quit
   ```
   ```
   [*SPE2] mpls switch-l2vc instance-name 1 1.1.1.1 2 trans 400 recv 300 tunnel-policy 1 between 4.4.4.4 1 trans 800 recv 700 tunnel-policy 1 encapsulation vlan control-word
   ```
   ```
   [*SPE2] commit
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
      [*PE2] pw-aps 2
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
      [*PE2] interface gigabitethernet 0/1/2.1
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
   mpls oam                                                                        
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  pw-aps 1                                                                        
  #                                                                               
  bidirectional static-cr-lsp ingress Tunnel10                                 
   forward outgoing-interface GigabitEthernet0/1/1 nexthop 10.1.2.2 out-label 20                      
   backward in-label 30 lsrid 2.2.2.2 tunnel-id 100                                                           
  #                                                                               
  bidirectional static-cr-lsp ingress Tunnel11                                 
   forward outgoing-interface GigabitEthernet0/1/2 nexthop 10.1.3.2 out-label 40                      
   backward in-label 50 lsrid 3.3.3.3 tunnel-id 200                                                           
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 10                                                             
   mpls static-l2vc destination 2.2.2.2 1 transmit-vpn-label 100 receive-vpn-label 200 tunnel-policy 1
   mpls l2vpn pw-ttl 2
   mpls static-l2vc destination 3.3.3.3 2 transmit-vpn-label 300 receive-vpn-label 400 tunnel-policy 1 secondary
   mpls l2vpn pw-ttl 2 secondary
   mpls l2vpn pw-aps 1 admin                                                      
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.2.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                                                                           
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 10.1.3.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                                                                            
  #                                                                               
  interface LoopBack0                                                             
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                                               
  interface Tunnel10                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te signal-protocol cr-static                                              
   mpls te tunnel-id 100                                                          
   mpls te bidirectional                                                          
   mpls te reserved-for-binding                                                   
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te signal-protocol cr-static                                              
   mpls te tunnel-id 200                                                          
   mpls te bidirectional                                                          
   mpls te reserved-for-binding                                                   
  #                                                                               
  ospf 1                                                                          
   area 0.0.0.0                                                                   
    network 10.1.2.0 0.0.0.255                                                    
    network 1.1.1.1 0.0.0.0                                                       
    network 10.1.3.0 0.0.0.255                                                    
  # 
  tunnel-policy 1
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
   mpls oam                                                                       
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  pw-aps 2                                                                        
  #                                                                               
  bidirectional static-cr-lsp egress Tunnel11                                 
   forward outgoing-interface GigabitEthernet0/1/0 in-label 60 lsrid 1.1.1.1 tunnel-id 200
   backward nexthop 10.1.3.1 out-label 70                               
  #                                                                               
  bidirectional static-cr-lsp ingress Tunnel11                                 
   forward outgoing-interface GigabitEthernet0/1/0 in-label 90 lsrid 4.4.4.4 tunnel-id 100
   backward nexthop 10.1.5.2 out-label 80                               
  #                                                                              
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.1.4.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.5.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/2.1                                                
   mpls static-l2vc destination 2.2.2.2 1 transmit-vpn-label 500 receive-vpn-label 600 tunnel-policy 1
   mpls l2vpn pw-ttl 2
   mpls static-l2vc destination 3.3.3.3 2 transmit-vpn-label 700 receive-vpn-label 800 tunnel-policy 1 secondary
   mpls l2vpn pw-ttl 2 secondary
   mpls l2vpn pw-aps 2 admin                                                      
  #                                                                               
  interface LoopBack0                                                             
   ip address 4.4.4.4 255.255.255.255                                             
  #                                                                               
  interface Tunnel10                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te tunnel-id 400                                                          
   mpls te passive-tunnel      
   mpls te binding bidirectional static-cr-lsp egress Tunnel10                 
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 300                                                          
   mpls te passive-tunnel      
   mpls te binding bidirectional static-cr-lsp egress Tunnel10                 
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 10.1.4.0 0.0.0.255                                                    
    network 10.1.5.0 0.0.0.255                                                    
    network 4.4.4.4 0.0.0.0                                                       
    mpls-te enable 
  #
  tunnel-policy 1
   tunnel binding destination 3.3.3.3 te Tunnel10
   tunnel binding destination 2.2.2.2 te Tunnel11
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
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls switch-l2vc instance-name 1 1.1.1.1 1 trans 200 recv 100 tunnel-policy 1 between 4.4.4.4 1 trans 600 recv 500 tunnel-policy 1 encapsulation vlan control-word                                                     
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.1.2.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.4.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface LoopBack0                                                             
   ip address 2.2.2.2 255.255.255.255                                             
  #                                                                               
  interface Tunnel10                                                           
   mpls te passive-tunnel
   mpls te binding bidirectional static-cr-lsp egress Tunnel10                                     
  #
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 10.1.4.0 0.0.0.255                                                    
    network 10.1.2.0 0.0.0.255                                                    
    mpls-te enable                                                                
  # 
  tunnel-policy 1
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
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls switch-l2vc instance-name 1 1.1.1.1 2 trans 400 recv 300 tunnel-policy 1 between 4.4.4.4 1 trans 800 recv 700 tunnel-policy 1 encapsulation vlan control-word
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.1.3.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                             
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.5.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface LoopBack0                                                             
   ip address 3.3.3.3 255.255.255.255                                             
  #                                                                               
  interface Tunnel11                                                           
   mpls te passive-tunnel
   mpls te binding bidirectional static-cr-lsp egress Tunnel11
  #                                                                               
  interface Tunnel12                                                           
   mpls te passive-tunnel
   mpls te binding bidirectional static-cr-lsp egress Tunnel12
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
  tunnel-policy 1
   tunnel binding destination 4.4.4.4 te Tunnel10
   tunnel binding destination 1.1.1.1 te Tunnel11
  #
  mpls te binding bidirectional static-cr-lsp egress Tunnel12
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
  #                                                                               
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 10                                                             
   ip address 10.1.1.2 255.255.255.0                                              
  #                                                                               
  return                 
  ```