Example for Configuring an IP-SDH Hybrid Network to Bear the CTS Service
========================================================================

Example for Configuring an IP-SDH Hybrid Network to Bear the CTS Service

#### Networking Requirements

The Cordless Telephony System (CTS) is a dispatch phone service for railway networks. On the network shown in [Figure 1](#EN-US_TASK_0172364258__fig_01), both IP and SDH devices are deployed, a dispatch phone is single-homed to a UPE, the UPE is dual-homed to SPEs, and the SPEs are connected to the SDH devices on the transmission backbone network. To bear the CTS service in this scenario, implement the communication between the IP and SDH devices, configure primary and secondary PWs between the UPE and SPEs, and configure dual feed and selective receiving on the UPE. In addition, configure BFD sessions on the IP network to monitor link status and enable SNCP on the SDH network (the SNCP configuration is not provided in this section) to improve service reliability.

**Figure 1** Configuring an IP-SDH hybrid network to bear the CTS service![](../../../../public_sys-resources/note_3.0-en-us.png) 

On the example network, the device models of SPE1 and SPE2 are NE40Es.

Interface 0, interface 1, interface 2, and interface 3 stand for serial 0/2/1:0, GE 0/1/1, GE 0/1/2, and serial 0/2/1/1:0, respectively.


  
![](images/fig_dc_ne_tdm_cfg_002201.png "Click to enlarge")  

| Device | Interface | IP Address |
| --- | --- | --- |
| UPE | GE 0/1/1  GE 0/1/2  Loopback0 | 10.1.1.1/24  10.1.2.1/24  1.1.1.1/32 |
| SPE1 | GE 0/1/1  Loopback0 | 10.1.1.2/24  2.2.2.2/32 |
| SPE2 | GE 0/1/2  Loopback0 | 10.1.2.2/24  3.3.3.3/32 |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each interface on the UPE, SPE1, and SPE2, allowing the devices to communicate at the network layer. This example uses OSPF as the routing protocol.
2. Configure basic MPLS functions and public tunnels to bear PWs.
3. Configure remote MPLS LDP sessions and PWs between the UPE and SPEs.
4. Configure BFD sessions to monitor the PWs.
5. Configure fast alarm detection.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses for interfaces on the UPE, SPE1, and SPE2
* LSR IDs for the UPE, SPE1, and SPE2
* L2VC IDs for each PW (must be the same on the two ends of the PW)
* BFD parameters

#### Procedure

1. Configure an IP address and a routing protocol for each interface on the UPE, SPE1, and SPE2, allowing the devices to communicate at the network layer. For configuration details, see "[Configuration Files](#EN-US_TASK_0172364258__section_05)" in this section.
2. Configure basic MPLS functions and public network tunnels.
   1. Configure basic MPLS functions and enable MPLS LDP and MPLS TE.
      
      
      
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
      [*UPE] mpls ldp
      ```
      ```
      [*UPE-mpls-ldp] quit
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
      
      The configurations of SPE1 and SPE2 are similar to the configuration of the UPE. For configuration details, see "[Configuration Files](#EN-US_TASK_0172364258__section_05)" in this section.
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
      [*UPE-Tunnel1] destination 2.2.2.2
      ```
      ```
      [*UPE-Tunnel1] mpls te tunnel-id 100
      ```
      ```
      [*UPE-Tunnel1] mpls te reserved-for-binding
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
      [*UPE-Tunnel2] destination 3.3.3.3
      ```
      ```
      [*UPE-Tunnel2] mpls te tunnel-id 200
      ```
      ```
      [*UPE-Tunnel2] mpls te reserved-for-binding
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
      [*UPE-Serial0/2/1:0] mpls l2vc 2.2.2.2 1 tunnel-policy policy1 control-word
      ```
      ```
      [*UPE-Serial0/2/1:0] mpls l2vc 3.3.3.3 2 secondary tunnel-policy policy1 control-word secondary
      ```
      ```
      [*UPE-Serial0/2/1:0] mpls l2vpn stream-dual-receiving
      ```
      ```
      [*UPE-Serial0/2/1:0] quit
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
      [*SPE1-Serial0/2/1/1:0] mpls l2vc 1.1.1.1 1 tunnel-policy policy1 control-word
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
      [*SPE2-Serial0/2/1/1:0] mpls l2vc 1.1.1.1 1 tunnel-policy policy1 control-word
      ```
      ```
      [*SPE2-Serial0/2/1/1:0] quit
      ```
      ```
      [*SPE2] commit
      ```
4. Configure BFD sessions to monitor the PWs.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] bfd
   ```
   ```
   [*UPE-bfd] quit
   ```
   ```
   [*UPE] bfd master bind pw interface Serial 0/2/1:0 remote-peer 2.2.2.2 pw-ttl auto-calculate
   ```
   ```
   [*UPE-bfd-lsp-session-master] discriminator local 2
   ```
   ```
   [*UPE-bfd-lsp-session-master] discriminator remote 2
   ```
   ```
   [*UPE-bfd-lsp-session-master] quit
   ```
   ```
   [*UPE] bfd slave bind pw interface Serial 0/2/1:0 remote-peer 3.3.3.3 pw-ttl auto-calculate secondary
   ```
   ```
   [*UPE-bfd-lsp-session-slave] discriminator local 2
   ```
   ```
   [*UPE-bfd-lsp-session-slave] discriminator remote 2
   ```
   ```
   [*UPE-bfd-lsp-session-slave] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure SPE1.
   
   ```
   [~SPE1] bfd
   ```
   ```
   [*SPE1-bfd] quit
   ```
   ```
   [*SPE1] bfd pw1 bind pw interface serial 0/2/1/1:0
   ```
   ```
   [*SPE1-bfd-lsp-session-pw1] discriminator local 2
   ```
   ```
   [*SPE1-bfd-lsp-session-pw1] discriminator remote 2
   ```
   ```
   [*SPE1-bfd-lsp-session-pw1] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure SPE2.
   
   ```
   [~SPE2] bfd
   ```
   ```
   [*SPE2-bfd] quit
   ```
   ```
   [*SPE2] bfd pw2 bind pw interface serial 0/2/1/1:0
   ```
   ```
   [*SPE2-bfd-lsp-session-pw2] discriminator local 2
   ```
   ```
   [*SPE2-bfd-lsp-session-pw2] discriminator remote 2
   ```
   ```
   [*SPE2-bfd-lsp-session-pw2] quit
   ```
   ```
   [*SPE2] commit
   ```
5. Configure fast alarm detection on SPE1 and SPE2.
   
   
   
   # Configure SPE1.
   
   ```
   [~SPE1] interface serial 0/2/1/1:0
   ```
   ```
   [~SPE1-Serial0/2/1/1:0] fast-alarm-detect enable
   ```
   ```
   [*SPE1-Serial0/2/1/1:0] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure SPE2.
   
   ```
   [~SPE2] interface serial 0/2/1/1:0
   ```
   ```
   [~SPE2-Serial0/2/1/1:0] fast-alarm-detect enable
   ```
   ```
   [*SPE2-Serial0/2/1/1:0] quit
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
  bfd                                                                             
  #
  mpls lsr-id 1.1.1.1
  #                                                                               
  mpls
    mpls te
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls ldp
  #                                                                               
  mpls ldp remote-peer 2.2.2.2                                                    
   remote-ip 2.2.2.2                                                              
  #                                                                               
  mpls ldp remote-peer 3.3.3.3                                                    
   remote-ip 3.3.3.3                                                              
  #
  controller e1 0/2/1
   channel-set 0 timeslot-list 1-31                                                                          
  # 
  interface serial 0/2/1:0 
   link-protocol tdm                           
   mpls l2vc 2.2.2.2 1 tunnel-policy policy1 control-word
   mpls l2vc 3.3.3.3 2 secondary tunnel-policy policy1 control-word secondary
   mpls l2vpn stream-dual-receiving
   mpls l2vpn stream-dual-send                                              
  #                                                                               
  interface GigabitEthernet 0/1/1                                            
   undo shutdown                                                                  
   ip address 10.1.1.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
  #                                                                               
  interface GigabitEthernet 0/1/2 
   undo shutdown                                                                  
   ip address 10.1.2.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
  # 
  interface LoopBack0                                                             
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                                               
  interface Tunnel 1                                                    
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te reserved-for-binding
   mpls te bit-error-detection
   mpls te tunnel-id 100 
  #                                                                               
  ospf 100                                                                        
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 1.1.1.1 0.0.0.0                                                       
    network 10.1.1.0 0.0.0.255                                                   
    network 10.1.2.0 0.0.0.255                                                   
    mpls-te enable                                                                
  #                                                                               
  interface Tunnel 2                                                     
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te reserved-for-binding
   mpls te bit-error-detection
   mpls te tunnel-id 200                                                                
  #                                                       
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel 1                          
   tunnel binding destination 3.3.3.3 te Tunnel 2         
  #                                                                               
  bfd master bind pw interface serial 0/2/1:0 remote-peer 2.2.2.2 pw-ttl auto-calculate
   discriminator local 2
   discriminator remote 2
  #
  bfd slave bind pw interface serial 0/2/1:0 remote-peer 3.3.3.3 pw-ttl auto-calculate secondary
   discriminator local 2
   discriminator remote 2
  # 
  return
  ```
* SPE1 configuration file
  
  ```
  #                                                                               
  sysname SPE1                                                                    
  #                                                                               
  bfd                                                                             
  #                                                                               
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls ldp
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                    
   remote-ip 1.1.1.1                                                              
  #                                                                               
  interface GigabitEthernet 0/1/1   
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
   mpls           
   mpls te                                                                                      
  #                                                                               
  interface LoopBack0                                                             
   ip address 2.2.2.2 255.255.255.255                                                       
  #
  controller cpos 0/2/1
   e1 1 channel-set 0 timeslot-list 1-31                                                                     
  # 
  interface serial 0/2/1/1:0 
   link-protocol tdm
   mpls l2vc 1.1.1.1 1 tunnel-policy policy1 control-word
   mpls l2vpn pw bit-error-detection
   fast-alarm-detect enable
  #
  interface Tunnel 1 
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te reserved-for-binding
   mpls te bit-error-detection
   mpls te tunnel-id 100
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
   tunnel binding destination 1.1.1.1 te Tunnel 1               
  #                                                                               
  bfd pw1 bind pw interface serial 0/2/1/1:0
   discriminator local 2
   discriminator remote 2                                                                        
  #                                                                               
  return
  ```
* SPE2 configuration file
  
  ```
  #                                                                               
  sysname SPE2                                                                    
  #                                                                               
  bfd                                                                             
  #                                                                               
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
  #                                                                               
  mpls l2vpn                                                                      
  #                                                                               
  mpls ldp
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                    
   remote-ip 1.1.1.1                                                                        
  #                                                                               
  interface GigabitEthernet 0/1/2        
   undo shutdown  
   ip address 10.1.2.2 255.255.255.0
   mpls           
   mpls te        
  #                                                                               
  interface LoopBack0                                                             
   ip address 3.3.3.3 255.255.255.255                                             
  #                                                                               
  controller cpos 0/2/1
   e1 1 channel-set 0 timeslot-list 1-31                                                                     
  # 
  interface serial 0/2/1/1:0 
   link-protocol tdm
   mpls l2vc 1.1.1.1 1 tunnel-policy policy1 control-word
   mpls l2vpn pw bit-error-detection
   fast-alarm-detect enable
  #
  interface Tunnel 2         
   ip address unnumbered interface LoopBack0
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te record-route
   mpls te reserved-for-binding
   mpls te bit-error-detection
   mpls te tunnel-id 200
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
   tunnel binding destination 1.1.1.1 te Tunnel 2                          
  #                                                                               
  bfd pw2 bind pw interface serial 0/2/1/1:0
   discriminator local 2
   discriminator remote 2
  #                                                                              
  return
  ```