Example for Configuring an IP-SDH Hybrid Network to Bear the GSM-R Service
==========================================================================

Example_for_Configuring_an_IP-SDH_Hybrid_Network_to_Bear_the_GSM-R_Service

#### Networking Requirements

The Global System for Mobile Communications - Railway (GSM-R) is a railway communication system based on the GSM communication standard. On the network shown in [Figure 1](#EN-US_TASK_0172364261__fig_01), both IP and SDH devices are deployed, a BTS is connected to a UPE through two E1 interfaces, the UPE is dual-homed to SPEs, and the SPEs are connected to SDH devices. To bear the GSM-R service in this scenario, implement the communication between the IP and SDH devices, configure primary and secondary PWs between the UPE and SPEs, and configure hard pipe to bear the PWs. In addition, configure service protection on the BTS-BSC side to improve service reliability. Tunnel protection for the PWs is not required.

**Figure 1** Configuring an IP-SDH hybrid network to bear the GSM-R service![](../../../../public_sys-resources/note_3.0-en-us.png) 

On the example network, the device models of SPE1 and SPE2 are NE40Es.

interface 1, interface 2, and interface 3, Interface 4, Interface 5 stand for GE 0/1/1, GE 0/1/2, CPOS 0/2/1, serial 0/2/1:0 and serial 0/2/2:0 respectively.


  
![](images/fig_dc_ne_tdm_cfg_002501.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| UPE | GE 0/1/1  GE 0/1/2  Loopback0 | 10.1.1.1/24  10.1.2.1/24  1.1.1.1/32 |
| SPE1 | GE 0/1/1  Loopback0 | 10.1.1.2/24  2.2.2.2/32 |
| SPE2 | GE 0/1/2  Loopback0 | 10.1.2.2/24  3.3.3.3/32 |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each interface on the UPE, SPE1, and SPE2, allowing the devices to communicate at the network layer. This example uses OSPF as the routing protocol.
2. Configure MPLS TE tunnels to bear PWs.
3. Configure remote MPLS LDP sessions and PWs between the UPE and SPEs.
4. Enable each SPE to send alarm bit streams to the peer device when specific faults are detected on the SPE.
5. Configure each SPE to send the 0xFF bit stream to notify an idle E1 channel timeslot on a subcard, so that the subcard can quickly and continuously send AIS bit streams to the AC-side device if network-side PW faults occur.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses for interfaces on the UPE, SPE1, and SPE2
* LSR IDs for the UPE, SPE1, and SPE2
* L2VC IDs for each PW (must be the same on the two ends of the PW)

#### Procedure

1. Configure an IP address and a routing protocol for each interface on the UPE, SPE1, and SPE2, allowing the devices to communicate at the network layer. For configuration details, see "[Configuration Files](#EN-US_TASK_0172364261__section_05)" in this section.
2. Configure basic MPLS functions and public network tunnels.
   1. Enable MPLS TE.
      
      
      
      # Configure the UPE.
      
      ```
      <UPE> system-view
      ```
      ```
      [~UPE] mpls lsr-id 1.1.1.1
      ```
      ```
      [*UPE] mpls
      ```
      ```
      [*UPE-mpls] mpls te
      ```
      ```
      [*UPE-mpls] quit
      ```
      ```
      [*UPE] interface gigabitethernet 0/1/1
      ```
      ```
      [*UPE-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*UPE-GigabitEthernet0/1/1] mpls te
      ```
      ```
      [*UPE-GigabitEthernet0/1/1] quit
      ```
      ```
      [*UPE] interface gigabitethernet 0/1/2
      ```
      ```
      [*UPE-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*UPE-GigabitEthernet0/1/2] mpls te
      ```
      ```
      [*UPE-GigabitEthernet0/1/2] quit
      ```
      ```
      [*UPE] ospf 100
      ```
      ```
      [*UPE-ospf-100] opaque-capability enable
      ```
      ```
      [*UPE-ospf-100] area 0
      ```
      ```
      [*UPE-ospf-100-area-0.0.0.0] mpls-te enable
      ```
      ```
      [*UPE-ospf-100-area-0.0.0.0] quit
      ```
      ```
      [*UPE-ospf-100] quit
      ```
      ```
      [*UPE] commit
      ```
      
      The configurations of SPE1 and SPE2 are similar to the configuration of the UPE. For configuration details, see "[Configuration Files](#EN-US_TASK_0172364261__section_05)" in this section.
   2. Configure TE tunnels.
      
      
      
      # Configure the UPE.
      
      ```
      [~UPE] interface tunnel 1
      ```
      ```
      [*UPE-Tunnel1] ip address unnumbered interface loopback 0
      ```
      ```
      [*UPE-Tunnel1] tunnel-protocol mpls te
      ```
      ```
      [*UPE-Tunnel1] mpls te signal-protocol cr-static
      ```
      ```
      [*UPE-Tunnel1] destination 2.2.2.2
      ```
      ```
      [*UPE-Tunnel1] mpls te tunnel-id 100
      ```
      ```
      [*UPE-Tunnel1] mpls te reserved-for-binding
      ```
      ```
      [*UPE-Tunnel1] mpls te bidirectional
      ```
      ```
      [*UPE-Tunnel1] quit
      ```
      ```
      [*UPE] interface tunnel 2
      ```
      ```
      [*UPE-Tunnel2] ip address unnumbered interface loopback 0
      ```
      ```
      [*UPE-Tunnel2] tunnel-protocol mpls te
      ```
      ```
      [*UPE-Tunnel2] mpls te signal-protocol cr-static
      ```
      ```
      [*UPE-Tunnel2] destination 3.3.3.3
      ```
      ```
      [*UPE-Tunnel2] mpls te tunnel-id 200
      ```
      ```
      [*UPE-Tunnel2] mpls te reserved-for-binding
      ```
      ```
      [*UPE-Tunnel2] mpls te bidirectional
      ```
      ```
      [*UPE-Tunnel2] quit
      ```
      ```
      [~UPE] tunnel-policy policy1
      ```
      ```
      [*UPE-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel 1
      ```
      ```
      [*UPE-tunnel-policy-policy1] tunnel binding destination 3.3.3.3 te Tunnel 2
      ```
      ```
      [*UPE-tunnel-policy-policy1] quit
      ```
      ```
      [*UPE] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] interface tunnel 1
      ```
      ```
      [*SPE1-Tunnel1] ip address unnumbered interface loopback 0
      ```
      ```
      [*SPE1-Tunnel1] tunnel-protocol mpls te
      ```
      ```
      [*SPE1-Tunnel1] destination 1.1.1.1
      ```
      ```
      [*SPE1-Tunnel1] mpls te tunnel-id 100
      ```
      ```
      [*SPE1-Tunnel1] mpls te reserved-for-binding
      ```
      ```
      [*SPE1-Tunnel1] mpls te signal-protocol cr-static
      ```
      ```
      [*SPE1-Tunnel1] mpls te passive-tunnel
      ```
      ```
      [*SPE1-Tunnel1] mpls te binding bidirectional static-cr-lsp egress Tunnel 1
      ```
      ```
      [*SPE1-Tunnel1] quit
      ```
      ```
      [~SPE1] tunnel-policy policy1
      ```
      ```
      [*SPE1-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel 1
      ```
      ```
      [*SPE1-tunnel-policy-policy1] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] interface tunnel 2
      ```
      ```
      [*SPE2-Tunnel2] ip address unnumbered interface loopback 0
      ```
      ```
      [*SPE2-Tunnel2] tunnel-protocol mpls te
      ```
      ```
      [*SPE2-Tunnel2] destination 1.1.1.1
      ```
      ```
      [*SPE2-Tunnel2] mpls te tunnel-id 200
      ```
      ```
      [*SPE2-Tunnel2] mpls te reserved-for-binding
      ```
      ```
      [*SPE2-Tunnel2] mpls te signal-protocol cr-static
      ```
      ```
      [*SPE2-Tunnel2] mpls te passive-tunnel
      ```
      ```
      [*SPE2-Tunnel2] mpls te binding bidirectional static-cr-lsp egress Tunnel 2
      ```
      ```
      [*SPE2-Tunnel2] quit
      ```
      ```
      [~SPE2] tunnel-policy policy1
      ```
      ```
      [*SPE2-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel 2
      ```
      ```
      [*SPE2-tunnel-policy-policy1] quit
      ```
      ```
      [*SPE2] commit
      ```
   3. Configure static bidirectional co-routed CR-LSPs.
      
      
      
      # Configure the UPE.
      
      ```
      [~UPE] bidirectional static-cr-lsp ingress Tunnel 1
      ```
      ```
      [*UPE-Tunnel1] forward outgoing-interface GigabitEthernet 0/1/1 nexthop 10.1.1.2 out-label 40
      ```
      ```
      [*UPE-Tunnel1] backward in-label 43
      ```
      ```
      [*UPE-Tunnel1] hard-pipe enable
      ```
      ```
      [*UPE-Tunnel1] quit
      ```
      ```
      [~UPE] bidirectional static-cr-lsp ingress Tunnel 2
      ```
      ```
      [*UPE-Tunnel2] forward outgoing-interface GigabitEthernet 0/1/2 nexthop 10.1.2.2 out-label 41
      ```
      ```
      [*UPE-Tunnel2] backward in-label 42
      ```
      ```
      [*UPE-Tunnel2] hard-pipe enable
      ```
      ```
      [*UPE-Tunnel2] quit
      ```
      ```
      [*UPE] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] bidirectional static-cr-lsp egress Tunnel 1
      ```
      ```
      [*SPE1-Tunnel1] forward in-label 40 lsrid 1.1.1.1 tunnel-id 100
      ```
      ```
      [*SPE1-Tunnel1] backward outgoing-interface GigabitEthernet 0/1/1 nexthop 10.1.1.1 out-label 43
      ```
      ```
      [*SPE1-Tunnel1] hard-pipe enable
      ```
      ```
      [*UPE-Tunnel1] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] bidirectional static-cr-lsp egress Tunnel 2
      ```
      ```
      [*SPE2-Tunnel2] forward in-label 41 lsrid 1.1.1.1 tunnel-id 200
      ```
      ```
      [*SPE2-Tunnel2] backward outgoing-interface GigabitEthernet 0/1/2 nexthop 10.1.2.1 out-label 42
      ```
      ```
      [*SPE2-Tunnel2] hard-pipe enable
      ```
      ```
      [*SPE2-Tunnel2] quit
      ```
      ```
      [*SPE2] commit
      ```
3. Configure remote MPLS LDP sessions and PWs.
   1. Configure a remote MPLS LDP session between the UPE and each SPE.
      
      
      
      # Configure the UPE.
      
      ```
      [~UPE] mpls ldp remote-peer 2.2.2.2
      ```
      ```
      [*UPE-mpls-ldp-remote-2.2.2.2] remote-ip 2.2.2.2
      ```
      ```
      [*UPE-mpls-ldp-remote-2.2.2.2] quit
      ```
      ```
      [*UPE] mpls ldp remote-peer 3.3.3.3
      ```
      ```
      [*UPE-mpls-ldp-remote-3.3.3.3] remote-ip 3.3.3.3
      ```
      ```
      [*UPE-mpls-ldp-remote-3.3.3.3] quit
      ```
      ```
      [*UPE] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*SPE1-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
      ```
      ```
      [*SPE1-mpls-ldp-remote-1.1.1.1] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*SPE2-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
      ```
      ```
      [*SPE2-mpls-ldp-remote-1.1.1.1] quit
      ```
      ```
      [*SPE2] commit
      ```
   2. Configure PWs.
      
      
      
      # Configure the UPE.
      
      ```
      [~UPE] mpls l2vpn
      ```
      ```
      [*UPE-l2vpn] quit
      ```
      ```
      [~UPE] pw-template pw_ces
      ```
      ```
      [*UPE-pw-template-pw_ces] quit
      ```
      ```
      [*UPE] controller e1 0/2/1
      ```
      ```
      [*UPE-E1 0/2/1] channel-set 0 timeslot-list 1-31
      ```
      ```
      [*UPE-E1 0/2/1] quit
      ```
      ```
      [*UPE] interface serial 0/2/1:0
      ```
      ```
      [*UPE-Serial0/2/1:0] link-protocol tdm
      ```
      ```
      [*UPE-Serial0/2/1:0] mpls static-l2vc destination 2.2.2.2 pw-template pw_ces 10 transmit-vpn-label 100 receive-vpn-label 100 tunnel-policy policy1 control-word
      ```
      ```
      [*UPE-Serial0/2/1:0] mpls l2vpn hard-pipe expand-ratio 20
      ```
      ```
      [*UPE-Serial0/2/1:0] quit
      ```
      ```
      [*UPE] controller e1 0/2/2
      ```
      ```
      [*UPE-E1 0/2/2] channel-set 0 timeslot-list 1-31
      ```
      ```
      [*UPE-E1 0/2/2] quit
      ```
      ```
      [*UPE] interface serial 0/2/2:0
      ```
      ```
      [*UPE-Serial0/2/2:0] link-protocol tdm
      ```
      ```
      [*UPE-Serial0/2/2:0] mpls static-l2vc destination 3.3.3.3 pw-template pw_ces 10 transmit-vpn-label 100 receive-vpn-label 100 tunnel-policy policy1 control-word
      ```
      ```
      [*UPE-Serial0/2/2:0] mpls l2vpn hard-pipe expand-ratio 20
      ```
      ```
      [*UPE-Serial0/2/2:0] quit
      ```
      ```
      [*UPE] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] mpls l2vpn
      ```
      ```
      [*SPE1-l2vpn] quit
      ```
      ```
      [~SPE1] pw-template pw_ces
      ```
      ```
      [*SPE1-pw-template-pw_ces] quit
      ```
      ```
      [*SPE1] controller cpos 0/2/1
      ```
      ```
      [*SPE1-Cpos0/2/1] e1 1 channel-set 0 timeslot-list 1-31
      ```
      ```
      [*SPE1-Cpos0/2/1] quit
      ```
      ```
      [*SPE1] interface serial 0/2/1/1:0
      ```
      ```
      [*SPE1-Serial0/2/1/1:0] link-protocol tdm
      ```
      ```
      [*SPE1-Serial0/2/1/1:0] mpls static-l2vc destination 1.1.1.1 pw-template pw_ces 10 transmit-vpn-label 100 receive-vpn-label 100 tunnel-policy policy1 control-word
      ```
      ```
      [*SPE1-Serial0/2/1/1:0] mpls l2vpn hard-pipe expand-ratio 20
      ```
      ```
      [*SPE1-Serial0/2/1/1:0] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure SPE2.
      
      ```
      [~SPE2] mpls l2vpn
      ```
      ```
      [*SPE2-l2vpn] quit
      ```
      ```
      [~SPE2] pw-template pw_ces
      ```
      ```
      [*SPE2-pw-template-pw_ces] quit
      ```
      ```
      [*SPE2] controller cpos 0/2/1
      ```
      ```
      [*SPE2-Cpos0/2/1] e1 1 channel-set 0 timeslot-list 1-31
      ```
      ```
      [*SPE2-Cpos0/2/1] quit
      ```
      ```
      [*SPE2] interface serial 0/2/1/1:0
      ```
      ```
      [*SPE2-Serial0/2/1/1:0] link-protocol tdm
      ```
      ```
      [*SPE2-Serial0/2/1/1:0] mpls static-l2vc destination 1.1.1.1 pw-template pw_ces 10 transmit-vpn-label 100 receive-vpn-label 100 tunnel-policy policy1 control-word
      ```
      ```
      [*SPE2-Serial0/2/1/1:0] mpls l2vpn hard-pipe expand-ratio 20
      ```
      ```
      [*SPE2-Serial0/2/1/1:0] quit
      ```
      ```
      [*SPE2] commit
      ```
4. Enable each SPE to send alarm bit streams to the peer device when specific faults are detected on the SPE.
   
   
   
   # Configure SPE1.
   
   ```
   [~SPE1] controller cpos 0/2/1
   ```
   ```
   [~SPE1-Cpos0/2/1] sdh-alarm nni-ais lrdi enable
   ```
   ```
   [*SPE1-Cpos0/2/1] sdh-alarm uni-tuais ces-underrun enable
   ```
   ```
   [*SPE1-Cpos0/2/1] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure SPE2.
   
   ```
   [~SPE2] controller cpos 0/2/1
   ```
   ```
   [~SPE2-Cpos0/2/1] sdh-alarm nni-ais lrdi enable
   ```
   ```
   [*SPE2-Cpos0/2/1] sdh-alarm uni-tuais ces-underrun enable
   ```
   ```
   [*SPE2-Cpos0/2/1] quit
   ```
   ```
   [*SPE2] commit
   ```
5. Configure each SPE to send the 0xFF bit stream to notify an idle E1 channel timeslot on a subcard, so that the subcard can quickly and continuously send AIS bit streams to the AC-side device if network-side PW faults occur.
   
   
   
   # Configure SPE1.
   
   ```
   [~SPE1] slot 1
   ```
   ```
   [~SPE1-slot-1] idle-code-e1 ff card 2
   ```
   ```
   [*SPE1-slot-1] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure SPE2.
   
   ```
   [~SPE2] slot 1
   ```
   ```
   [~SPE2-slot-1] idle-code-e1 ff card 2
   ```
   ```
   [*SPE2-slot-1] quit
   ```
   ```
   [*SPE2] commit
   ```

#### Configuration Files

* UPE configuration file
  
  ```
  #                                                                               
  sysname UPE                                                                     
  #                                                                               
  mpls lsr-id 1.1.1.1
  #                                                                               
  mpls
    mpls te
  #                                                                               
  mpls l2vpn
  #
  pw-template pw_ces
  #
  mpls ldp remote-peer 2.2.2.2                                                    
   remote-ip 2.2.2.2
  #                                                                               
  mpls ldp remote-peer 3.3.3.3                                                    
   remote-ip 3.3.3.3
  #
  bidirectional static-cr-lsp ingress Tunnel1
   forward outgoing-interface GigabitEthernet0/1/1 nexthop 10.1.1.2 out-label 40
   backward in-label 43
   hard-pipe enable                                                                       
  #
  bidirectional static-cr-lsp ingress Tunnel2
   forward outgoing-interface GigabitEthernet0/1/2 nexthop 10.1.2.2 out-label 41
   backward in-label 42
   hard-pipe enable                                                                                         
  #    
  controller e10/2/1
   channel-set 0 timeslot-list 1-31                                                                          
  # 
  interface serial0/2/1:0 
   link-protocol tdm
   mpls static-l2vc destination 2.2.2.2 pw-template pw_ces 10 transmit-vpn-label 100 receive-vpn-label 100 tunnel-policy policy1 control-word
   mpls l2vpn hard-pipe expand-ratio 20
  #    
  controller e10/2/2
   channel-set 0 timeslot-list 1-31                                                                          
  # 
  interface serial0/2/2:0 
   link-protocol tdm
   mpls static-l2vc destination 3.3.3.3 pw-template pw_ces 10 transmit-vpn-label 100 receive-vpn-label 100 tunnel-policy policy1 control-word
   mpls l2vpn hard-pipe expand-ratio 20
  #                                                                          
  interface GigabitEthernet0/1/1                                            
   undo shutdown                                                                  
   ip address 10.1.1.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface GigabitEthernet0/1/2 
   undo shutdown                                                                  
   ip address 10.1.2.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
  # 
  interface LoopBack0                                                             
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                                               
  interface Tunnel1                                                     
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te signal-protocol cr-static
   mpls te reserved-for-binding
   mpls te tunnel-id 100
   mpls te bidirectional 
  #                                                                               
  ospf 100                                                                        
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 1.1.1.1 0.0.0.0                                                       
    network 10.1.1.0 0.0.0.255                                                   
    network 10.1.2.0 0.0.0.255                                                   
    mpls-te enable                                                                
  #                                                                               
  interface Tunnel2                                                     
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol cr-static
   mpls te reserved-for-binding
   mpls te tunnel-id 200
   mpls te bidirectional                                                                
  #                                                       
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel1                          
   tunnel binding destination 3.3.3.3 te Tunnel2                          
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
  pw-template pw_ces                                                                      
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                    
   remote-ip 1.1.1.1
  #
  bidirectional static-cr-lsp egress Tunnel1
   forward in-label 40 lsrid 1.1.1.1 tunnel-id 100
   backward outgoing-interface GigabitEthernet0/1/1 nexthop 10.1.1.1 out-label 43
   hard-pipe enable                                                              
  #                                                                              
  interface GigabitEthernet0/1/1   
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
   mpls           
   mpls te                                                                                      
  #                                                                               
  interface LoopBack0                                                             
   ip address 2.2.2.2 255.255.255.255                                             
  #
  controller cpos0/2/1
   e1 1 channel-set 0 timeslot-list 1-31                                                                     
  # 
  interface serial0/2/1/1:0 
   link-protocol tdm
   mpls static-l2vc destination 1.1.1.1 pw-template pw_ces 10 transmit-vpn-label 100 receive-vpn-label 100 tunnel-policy policy1 control-word
   mpls l2vpn hard-pipe expand-ratio 20
  #
  interface Tunnel 1                                                     
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te reserved-for-binding
   mpls te tunnel-id 100
   mpls te signal-protocol cr-static
   mpls te passive-tunnel
   mpls te binding bidirectional static-cr-lsp egress Tunnel1
  #
  ospf 100                                                                        
   opaque-capability enable                                                       
   graceful-restart                                                               
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 10.1.1.0 0.0.0.255          
    mpls-te enable
  #                                                                     
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel1                        
  #
  controller cpos0/2/1
   sdh-alarm nni-ais lrdi enable
   sdh-alarm uni-tuais ces-underrun enable
  #
  slot 1
   idle-code-e1 ff card 2
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
  pw-template pw_ces
  #                                                                               
  mpls l2vpn 
  #
  bidirectional static-cr-lsp egress Tunnel2
   forward in-label 41 lsrid 1.1.1.1 tunnel-id 200
   backward outgoing-interface GigabitEthernet0/1/2 nexthop 10.1.2.1 out-label 42
   hard-pipe enable                                   
  #                                                                               
  interface GigabitEthernet0/1/2        
   undo shutdown  
   ip address 10.1.2.2 255.255.255.0
   mpls           
   mpls te        
  #                                                                               
  interface LoopBack0                                                             
   ip address 3.3.3.3 255.255.255.255
  #                                             
  controller cpos0/2/1
   e1 1 channel-set 0 timeslot-list 1-31                                                                     
  # 
  interface serial0/2/1/1:0 
   link-protocol tdm
   mpls static-l2vc destination 1.1.1.1 pw-template pw_ces 10 transmit-vpn-label 100 receive-vpn-label 100 tunnel-policy policy1 control-word
   mpls l2vpn hard-pipe expand-ratio 20
  #
  interface Tunnel2         
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te record-route
   mpls te reserved-for-binding
   mpls te tunnel-id 200
   mpls te signal-protocol cr-static
   mpls te passive-tunnel
   mpls te binding bidirectional static-cr-lsp egress Tunnel2
  #
  ospf 100        
   opaque-capability enable
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
    mpls-te enable
  #                              
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel2                          
  #
  controller cpos0/2/1
   sdh-alarm nni-ais lrdi enable
   sdh-alarm uni-tuais ces-underrun enable
  #
  slot 1
   idle-code-e1 ff card 2
  #                                                                              
  return
  ```