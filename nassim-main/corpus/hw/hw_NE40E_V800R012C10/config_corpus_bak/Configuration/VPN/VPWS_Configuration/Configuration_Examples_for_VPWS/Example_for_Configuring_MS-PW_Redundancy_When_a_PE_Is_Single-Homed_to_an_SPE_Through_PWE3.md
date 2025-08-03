Example for Configuring MS-PW Redundancy When a PE Is Single-Homed to an SPE Through PWE3
=========================================================================================

This section provides an example for configuring MS-PW redundancy when a PE is single-homed to an SPE. PW label switching is configured on the SPE to implement MS-PWs in primary/secondary mode.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172369993__fig_dc_vrp_cfg_01900601), PE1 is dual-homed to PE2 and PE3 through an SPE. Even if a public network link fails, PE2 or PE3 encounters a fault, or an AC link goes down, CE1 and CE2 can still communicate with each other.

**Figure 1** Configuring MS-PW redundancy when a PE is single-homed to an SPE  
![](images/fig_dc_vrp_cfg_01924301.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 and interface1.1 represent GE0/1/0, GE0/1/1, GE0/1/2, and GE0/1/0.1, respectively.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and routes, including:
   
   * IP addresses of interfaces on the PEs and SPE
   * IGP running on the PEs and SPE
2. Configure MPLS and public network tunnels, including:
   
   * Basic MPLS functions on the PEs and SPE
   * Public network tunnels
   * OSPF TE on the PEs and SPE
3. Configure MS-PWs.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface numbers, interface IP addresses, and OSPF process numbers on PEs and SPE
* LSR IDs of the PEs and SPE
* L2VC's destination IP addresses, VC IDs, and VC types

#### Procedure

1. Assign an IP address to each interface and configure a routing protocol.
   
   
   
   Configure an IP address and mask for each involved interface according to [Figure 1](#EN-US_TASK_0172369993__fig_dc_vrp_cfg_01900601). For detailed configurations, see Configuration Files.
   
   OSPF is used in this example. For detailed configurations, see Configuration Files.
2. Configure basic MPLS capabilities. Configure an MPLS TE tunnel between the SPE and each of PE1, PE2, and PE3. Configure an LDP LSP between PE2 and PE3.
   1. Enable MPLS, MPLS TE, and RSVP-TE globally on PE1, P, and PE2, and on all interfaces along the tunnel. Enable CSPF in the system view on the ingress of the tunnel.
      
      
      
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
      
      # Configure the SPE.
      
      ```
      [~SPE] mpls lsr-id 2.2.2.2
      ```
      ```
      [*SPE] mpls
      ```
      ```
      [*SPE-mpls] mpls te
      ```
      ```
      [*SPE-mpls] mpls rsvp-te
      ```
      ```
      [*SPE-mpls] mpls te cspf
      ```
      ```
      [*SPE-mpls] quit
      ```
      ```
      [*SPE] interface gigabitethernet 0/1/0
      ```
      ```
      [*SPE-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*SPE-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*SPE-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*SPE-GigabitEthernet0/1/0] quit
      ```
      ```
      [*SPE] interface gigabitethernet 0/1/1
      ```
      ```
      [*SPE-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*SPE-GigabitEthernet0/1/1] mpls te
      ```
      ```
      [*SPE-GigabitEthernet0/1/1] mpls rsvp-te
      ```
      ```
      [*SPE-GigabitEthernet0/1/1] quit
      ```
      ```
      [*SPE] interface gigabitethernet 0/1/2
      ```
      ```
      [*SPE-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*SPE-GigabitEthernet0/1/2] mpls te
      ```
      ```
      [*SPE-GigabitEthernet0/1/2] mpls rsvp-te
      ```
      ```
      [*SPE-GigabitEthernet0/1/2] quit
      ```
      ```
      [*SPE] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] mpls lsr-id 3.3.3.3
      ```
      ```
      [*PE2] mpls
      ```
      ```
      [*PE2-mpls] mpls te
      ```
      ```
      [*PE2-mpls] mpls rsvp-te
      ```
      ```
      [*PE2-mpls] mpls te cspf
      ```
      ```
      [*PE2-mpls] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/0
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls te
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls rsvp-te
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      The configuration of PE3 is similar to that of PE2. For detailed configurations, see Configuration Files.
   2. Configure OSPF TE.
      
      
      
      # Configure the SPE.
      
      ```
      [~SPE] ospf
      ```
      ```
      [*SPE-ospf-1] opaque-capability enable
      ```
      ```
      [*SPE-ospf-1] area 0
      ```
      ```
      [*SPE-ospf-1-area-0.0.0.0] mpls-te enable
      ```
      ```
      [*SPE-ospf-1-area-0.0.0.0] quit
      ```
      ```
      [*SPE-ospf-1] quit
      ```
      ```
      [*SPE] commit
      ```
      
      The configurations of PE1, PE2, and PE3 are similar to that of the SPE. For detailed configurations, see Configuration Files.
   3. Configure MPLS TE explicit paths.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] explicit-path tospe
      ```
      ```
      [*PE1-explicit-path-toupe] next hop 10.1.2.2
      ```
      ```
      [*PE1-explicit-path-toupe] next hop 2.2.2.2
      ```
      ```
      [*PE1-explicit-path-toupe] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure the SPE.
      
      ```
      [~SPE] explicit-path tope1
      ```
      ```
      [*SPE-explicit-path-tonpe1] next hop 10.1.2.1
      ```
      ```
      [*SPE-explicit-path-tonpe1] next hop 1.1.1.1
      ```
      ```
      [*SPE-explicit-path-tonpe1] quit
      ```
      ```
      [*SPE] explicit-path tope2
      ```
      ```
      [*SPE-explicit-path-tonpe2] next hop 10.1.3.2
      ```
      ```
      [*SPE-explicit-path-tonpe2] next hop 3.3.3.3
      ```
      ```
      [*SPE-explicit-path-tonpe2] quit
      ```
      ```
      [*SPE] explicit-path tope3
      ```
      ```
      [*SPE-explicit-path-tonpe2] next hop 10.1.4.2
      ```
      ```
      [*SPE-explicit-path-tonpe2] next hop 4.4.4.4 
      ```
      ```
      [*SPE-explicit-path-tonpe2] quit
      ```
      ```
      [*SPE] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] explicit-path tospe
      ```
      ```
      [*PE2-explicit-path-toupe] next hop 10.1.3.1
      ```
      ```
      [*PE2-explicit-path-toupe] next hop 2.2.2.2
      ```
      ```
      [*PE2-explicit-path-toupe] quit
      ```
      ```
      [*PE2] commit
      ```
      
      The configuration of PE3 is similar to that of PE2. For detailed configurations, see Configuration Files.
   4. Configure MPLS TE tunnel interfaces.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] interface Tunnel 101
      ```
      ```
      [*PE1-Tunnel101] ip address unnumbered interface loopback 0
      ```
      ```
      [*PE1-Tunnel101] tunnel-protocol mpls te
      ```
      ```
      [*PE1-Tunnel101] destination 2.2.2.2
      ```
      ```
      [*PE1-Tunnel101] mpls te tunnel-id 100
      ```
      ```
      [*PE1-Tunnel101] mpls te path explicit-path tospe
      ```
      ```
      [*PE1-Tunnel101] mpls te reserved-for-binding
      ```
      ```
      [*PE1-Tunnel101] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure the SPE.
      
      ```
      [~SPE] interface Tunnel 100
      ```
      ```
      [*SPE-Tunnel100] ip address unnumbered interface loopback 0
      ```
      ```
      [*SPE-Tunnel100] tunnel-protocol mpls te
      ```
      ```
      [*SPE-Tunnel100] destination 1.1.1.1
      ```
      ```
      [*SPE-Tunnel100] mpls te tunnel-id 100
      ```
      ```
      [*SPE-Tunnel100] mpls te path explicit-path tope1
      ```
      ```
      [*SPE-Tunnel100] mpls te reserved-for-binding
      ```
      ```
      [*SPE-Tunnel100] quit
      ```
      ```
      [*SPE] interface tunnel 101
      ```
      ```
      [*SPE-Tunnel101] ip address unnumbered interface loopback 0
      ```
      ```
      [*SPE-Tunnel101] tunnel-protocol mpls te
      ```
      ```
      [*SPE-Tunnel101] destination 3.3.3.3
      ```
      ```
      [*SPE-Tunnel101] mpls te tunnel-id 200
      ```
      ```
      [*SPE-Tunnel101] mpls te path explicit-path tope2
      ```
      ```
      [*SPE-Tunnel101] mpls te reserved-for-binding
      ```
      ```
      [*SPE-Tunnel101] quit
      ```
      ```
      [*SPE] interface tunnel 102
      ```
      ```
      [*SPE-Tunnel102] ip address unnumbered interface loopback 0
      ```
      ```
      [*SPE-Tunnel102] tunnel-protocol mpls te
      ```
      ```
      [*SPE-Tunnel102] destination 4.4.4.4
      ```
      ```
      [*SPE-Tunnel102] mpls te tunnel-id 300
      ```
      ```
      [*SPE-Tunnel102] mpls te path explicit-path tope3
      ```
      ```
      [*SPE-Tunnel102] mpls te reserved-for-binding
      ```
      ```
      [*SPE-Tunnel102] quit
      ```
      ```
      [*SPE] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface Tunnel 100
      ```
      ```
      [*PE2-Tunnel100] ip address unnumbered interface loopback 0
      ```
      ```
      [*PE2-Tunnel100] tunnel-protocol mpls te
      ```
      ```
      [*PE2-Tunnel100] destination 2.2.2.2
      ```
      ```
      [*PE2-Tunnel100] mpls te tunnel-id 200
      ```
      ```
      [*PE2-Tunnel100] mpls te path explicit-path tospe
      ```
      ```
      [*PE2-Tunnel100] mpls te reserved-for-binding
      ```
      ```
      [*PE2-Tunnel100] quit
      ```
      ```
      [*PE2] commit
      ```
      
      The configuration of PE3 is similar to that of PE2. For detailed configurations, see Configuration Files.
   5. Configure a tunnel policy on each device.
      
      
      
      # Configure PE1.
      
      ```
      [PE1] tunnel-policy policy1
      ```
      ```
      [*PE1-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel101
      ```
      ```
      [*PE1-tunnel-policy-policy1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure the SPE.
      
      ```
      [~SPE] tunnel-policy policy1
      ```
      ```
      [*SPE-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel100
      ```
      ```
      [*SPE-tunnel-policy-policy1] tunnel binding destination 3.3.3.3 te Tunnel101
      ```
      ```
      [*SPE-tunnel-policy-policy1] tunnel binding destination 4.4.4.4 te Tunnel102
      ```
      ```
      [*SPE-tunnel-policy-policy1] quit
      ```
      ```
      [*SPE] commit
      ```
      
      # Configure PE2.
      
      ```
      [PE2] tunnel-policy policy1
      ```
      ```
      [*PE2-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel100
      ```
      ```
      [*PE2-tunnel-policy-policy1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      The configuration of PE3 is similar to that of PE2. For detailed configurations, see Configuration Files.
   6. Configure an LDP LSP between PE2 and PE3.
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] mpls ldp
      ```
      ```
      [*PE2-mpls-ldp] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls ldp
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      The configuration of PE3 is similar to that of PE2. For detailed configurations, see Configuration Files.
      
      # Verify the configuration. Run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session) command on PE2 and PE3 to check whether the LDP session status is **Operational**. The following example uses the command output on PE2.
      
      ```
      [~PE2] display mpls ldp session
      ```
      ```
       LDP Session(s) in Public Network
       Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
       An asterisk '*' before a session means the session is being deleted.
       ------------------------------------------------------------------------------
       PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
       ------------------------------------------------------------------------------
       4.4.4.4:0          Operational DU   Passive  0000:00:46  187/187
       ------------------------------------------------------------------------------
       TOTAL: 1 session(s) Found.   
      ```
3. Configure service PWs over the public network.
   1. Configure a remote MPLS LDP session between the SPE and each of the PEs.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] mpls ldp remote-peer 2.2.2.2
      ```
      ```
      [*PE1-mpls-ldp-remote-2.2.2.2] remote-ip 2.2.2.2
      ```
      ```
      [*PE1-mpls-ldp-remote-2.2.2.2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure the SPE.
      
      ```
      [~SPE] mpls ldp
      ```
      ```
      [*SPE-mpls-ldp] quit
      ```
      ```
      [*SPE] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*SPE-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
      ```
      ```
      [*SPE-mpls-ldp-remote-1.1.1.1] quit
      ```
      ```
      [*SPE] mpls ldp remote-peer 4.4.4.4
      ```
      ```
      [*SPE-mpls-ldp-remote-4.4.4.4] remote-ip 4.4.4.4
      ```
      ```
      [*SPE-mpls-ldp-remote-4.4.4.4] quit
      ```
      ```
      [*SPE] mpls ldp remote-peer 3.3.3.3
      ```
      ```
      [*SPE-mpls-ldp-remote-3.3.3.3] remote-ip 3.3.3.3
      ```
      ```
      [*SPE-mpls-ldp-remote-3.3.3.3] quit
      ```
      ```
      [*SPE] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] mpls ldp remote-peer 2.2.2.2
      ```
      ```
      [*PE2-mpls-ldp-remote-2.2.2.2] remote-ip 2.2.2.2
      ```
      ```
      [*PE2-mpls-ldp-remote-2.2.2.2] quit
      ```
      ```
      [*PE2] commit
      ```
      
      The configuration of PE3 is similar to that of PE2. For detailed configurations, see Configuration Files.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Pseudo wire emulation edge-to-edge (PWE3) uses extended LDP signaling to distribute VPN labels. Because PE1 and the SPE communicate over an MPLS TE tunnel instead of an MPLS LDP LSP, you must establish a remote MPLS LDP session between them.
      
      PE2 and PE3 are directly connected over an LDP LSP, and therefore do not need to establish a remote LDP session.
   2. Configure service PWs.
      
      
      
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
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc 2.2.2.2 1 tunnel-policy policy1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure the SPE.
      
      ```
      [~SPE] mpls l2vpn
      ```
      ```
      [*SPE-l2vpn] quit
      ```
      ```
      [*SPE] mpls switch-l2vc 1.1.1.1 1 tunnel-policy policy1 between 3.3.3.3 2 tunnel-policy policy1 backup 4.4.4.4 3 tunnel-policy policy1 encapsulation vlan
      ```
      ```
      [*SPE] commit
      ```
      
      # Configure PE2.
      
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
      [*PE2-Eth-Trunk10.1] mpls l2vc 2.2.2.2 2 tunnel-policy policy1
      ```
      ```
      [*PE2-Eth-Trunk10.1] mpls l2vc 4.4.4.4 4 bypass
      ```
      ```
      [*PE2-Eth-Trunk10.1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      The configuration of PE3 is similar to that of PE2. For detailed configurations, see Configuration Files.
4. Configure Eth-Trunk interfaces.
   
   
   
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
   [*PE2] lacp e-trunk system-id 00e0-fc00-0000
   ```
   ```
   [*PE2] lacp e-trunk priority 100
   ```
   ```
   [*PE2] e-trunk 10
   ```
   ```
   [*PE2-e-trunk-10] priority 10
   ```
   ```
   [*PE2-e-trunk-10] peer-address 4.4.4.4 source-address 3.3.3.3
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
   
   The configuration of PE3 is similar to that of PE2. For detailed configurations, see Configuration Files.
5. Verify the configuration.
   
   
   
   # For configurations on CE1 and CE2, see "Configuration Files" in this section.
   
   Configure CE1 to ping the VLANIF interface address of CE2.
   
   ```
   [*CE1] ping 10.1.1.2
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

#### Configuration files

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
   mpls rsvp-te
   mpls te cspf                                                                  
  #                                                                               
  mpls l2vpn                                                                     
  #                                                                               
  explicit-path tospe                                                            
   next hop 10.1.2.2                                                             
   next hop 2.2.2.2                                                              
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 2.2.2.2                                                   
   remote-ip 2.2.2.2                                                              
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 10                                                             
   mpls l2vc 2.2.2.2 1 tunnel-policy policy1                                      
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.2.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #  
  interface LoopBack0                                                             
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                                               
  interface Tunnel101                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 100                                                          
   mpls te path explicit-path tospe                                               
   mpls te reserved-for-binding                                                   
  #                                                                                    
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 1.1.1.1 0.0.0.0                                                       
    network 10.1.2.0 0.0.0.255                                                    
    mpls-te enable                                                                
  #    
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel101                              
  #                                                                                
  return                                           
  ```
* SPE configuration file
  
  ```
  #                                                                               
  sysname SPE                                                                    
  #
  mpls lsr-id 2.2.2.2 
  #                                                            
  mpls                                                                           
   mpls te                                                                       
   mpls rsvp-te                                                                  
   mpls te cspf                                                                  
  #                                                                               
  mpls l2vpn                                                                     
  #                                                                               
  mpls switch-l2vc 1.1.1.1 1 tunnel-policy policy1 between 3.3.3.3 2 tunnel-policy policy1 backup 4.4.4.4 3 tunnel-policy policy1 encapsulation vlan 
  #                                                                               
  explicit-path tope1                                                            
   next hop 10.1.2.1                                                             
   next hop 1.1.1.1                                                              
  #                                                                               
  explicit-path tope2                                                            
   next hop 10.1.3.2                                                             
   next hop 3.3.3.3                                                              
  #                                                                               
  explicit-path tope3                                                            
   next hop 10.1.4.2                                                             
   next hop 4.4.4.4                                                              
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                   
   remote-ip 1.1.1.1                                                              
  #                                                                               
  mpls ldp remote-peer 3.3.3.3                                                   
   remote-ip 3.3.3.3                                                              
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
   ip address 10.1.3.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 10.1.4.1 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te        
  #                                                                               
  interface LoopBack0                                                             
   ip address 2.2.2.2 255.255.255.255                                             
  #
  interface Tunnel100                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 1.1.1.1                                                            
   mpls te tunnel-id 100                                                          
   mpls te path explicit-path tope1                                               
   mpls te reserved-for-binding                                                   
  # 
  interface Tunnel101                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te tunnel-id 200                                                          
   mpls te path explicit-path tope2                                               
   mpls te reserved-for-binding                                                                                                                  
  #
  interface Tunnel102                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 4.4.4.4                                                            
   mpls te tunnel-id 300                                                          
   mpls te path explicit-path tope3                                               
   mpls te reserved-for-binding                                                                                                                  
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 10.1.2.0 0.0.0.255                                                    
    network 10.1.3.0 0.0.0.255                                                    
    network 10.1.4.0 0.0.0.255                                                    
    mpls-te enable          
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel100                              
   tunnel binding destination 3.3.3.3 te Tunnel101                              
   tunnel binding destination 4.4.4.4 te Tunnel102                                                             
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
  mpls lsr-id 3.3.3.3 
  #                                                            
  mpls                                                                           
   mpls te                                                                       
   mpls rsvp-te                                                                  
   mpls te cspf                                                                  
  #                                                                               
  mpls l2vpn                                                                     
  #                                                                               
  explicit-path tospe                                                            
   next hop 10.1.3.1                                                             
   next hop 2.2.2.2                                                              
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 2.2.2.2                                                   
   remote-ip 2.2.2.2                                                              
  #       
  e-trunk 10                                                                     
   priority 10                                                                    
   peer-address 4.4.4.4 source-address 3.3.3.3                                                 
  #                                                                                      
  interface Eth-Trunk10                                                           
   mode lacp-static                                                               
   e-trunk 10                                                                    
  #                                                                               
  interface Eth-Trunk10.1                                                         
   vlan-type dot1q 10                                                             
   mpls l2vc 2.2.2.2 2 tunnel-policy policy1                                      
   mpls l2vc 4.4.4.4 4 bypass                                                     
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
   mpls ldp                                                                       
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   eth-trunk 10                                                                   
  #       
  interface LoopBack0                                                             
   ip address 3.3.3.3 255.255.255.255                                             
  #                                                                               
  interface Tunnel100
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 200                                                          
   mpls te path explicit-path tospe                                               
   mpls te reserved-for-binding
  #                                                                                  
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 3.3.3.3 0.0.0.0                                                       
    network 10.1.3.0 0.0.0.255                                                    
    network 10.1.5.0 0.0.0.255                                                    
    mpls-te enable                                                                
  #        
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel100                             
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
  mpls lsr-id 4.4.4.4 
  #                                                            
  mpls                                                                           
   mpls te                                                                       
   mpls rsvp-te                                                                  
   mpls te cspf                                                                  
  #                                                                               
  mpls l2vpn                                                                     
  #                                                                               
  explicit-path tospe                                                            
   next hop 10.1.4.1                                                             
   next hop 2.2.2.2                                                              
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 2.2.2.2                                                   
   remote-ip 2.2.2.2                                                              
  #                                                                               
  e-trunk 10                                                                     
   priority 20                                                                    
   peer-address 3.3.3.3 source-address 4.4.4.4                                    
  #                                                                               
  interface Eth-Trunk10                                                           
   mode lacp-static                                                               
   e-trunk 10                                                                    
  #                                                                               
  interface Eth-Trunk10.1                                                         
   vlan-type dot1q 10                                                             
   mpls l2vc 2.2.2.2 3 tunnel-policy policy1                                      
   mpls l2vc 3.3.3.3 4 bypass                                                     
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.1.4.2 255.255.255.0                                              
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.1.5.2 255.255.255.0                                              
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   eth-trunk 10                                                                   
  #                                                                               
  interface LoopBack0                                                             
   ip address 4.4.4.4 255.255.255.255                                             
  #                                                                               
  interface Tunnel100                                                           
   ip address unnumbered interface LoopBack0                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 300                                                          
   mpls te path explicit-path tospe                                               
   mpls te reserved-for-binding                                                   
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 4.4.4.0 0.0.0.255                                                     
    network 10.1.4.0 0.0.0.255                                                    
    network 10.1.5.0 0.0.0.255                                                    
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel100                              
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