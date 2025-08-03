Example for Configuring Basic PBB VPLS
======================================

This section provides an example for configuring basic PBB VPLS on a typical HVPLS network with UPEs, SPEs, and NPEs.

#### Networking Requirements

On the typical HVPLS network with UPEs, SPEs, and NPEs (as shown in [Figure 1](#EN-US_TASK_0172370800__fig_dc_vrp_pbb-vpls_cfg_001201)), basic PBB VPLS needs to be configured to replace QinQ with MAC-in-MAC. This helps reduce the number of MAC address entries that SPEs must learn, thereby improving network scalability.

**Figure 1** Configuring basic PBB VPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1, subinterface1.1, and interface2 represent GE0/1/0, GE0/1/0.1, and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_pbb-vpls_cfg_001201.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and an IGP for each involved interface to ensure IP connectivity.
2. Configure MPLS and MPLS LDP.
3. Enable MPLS L2VPN and configure PBB VPLS.

#### Data Preparation

* IP addresses and masks of interfaces on the backbone network
* I-VSI and B-VSI names, VSI IDs, B-SMAC addresses, B-DMAC addresses, and I-tags

#### Procedure

1. Configure IP addresses for CEs, UPEs, SPEs, and NPEs. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370800__dc_vrp_pbb-vpls_cfg_001201).
2. Configure an IGP (OSPF in this example) on UPEs, SPEs, and NPEs.
   
   
   
   # Configure UPE1.
   
   ```
   <UPE1> system-view
   ```
   ```
   [~UPE1] ospf 1
   ```
   ```
   [*UPE1-ospf-1] area 0
   ```
   ```
   [*UPE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*UPE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*UPE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*UPE1-ospf-1] quit
   ```
   ```
   [*UPE1] commit
   ```
   
   # Configure SPE1.
   
   ```
   <SPE1> system-view
   ```
   ```
   [~SPE1] ospf 1
   ```
   ```
   [*SPE1-ospf-1] area 0
   ```
   ```
   [*SPE1-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*SPE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*SPE1-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*SPE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*SPE1-ospf-1] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure NPE1.
   
   ```
   <NPE1> system-view
   ```
   ```
   [~NPE1] ospf 1
   ```
   ```
   [*NPE1-ospf-1] area 0
   ```
   ```
   [*NPE1-ospf-1-area-0.0.0.0] network 4.4.4.4 0.0.0.0
   ```
   ```
   [*NPE1-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*NPE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*NPE1-ospf-1] quit
   ```
   ```
   [*NPE1] commit
   ```
   
   # After the configuration is complete, check OSPF route information. The following example uses the command output on NPE1.
   
   ```
   [~NPE1] display ospf routing
   ```
   ```
             OSPF Process 1 with Router ID 4.4.4.4
                      Routing Tables
   
    Routing for Network
    Destination        Cost     Type       NextHop         AdvRouter       Area           
    1.1.1.1/32         2        Stub       10.2.1.1        10.1.1.1        0.0.0.0        
    2.2.2.2/32         1        Stub       10.2.1.1        10.1.1.2        0.0.0.0        
    4.4.4.4/32         0        Direct     4.4.4.4         4.4.4.4         0.0.0.0        
    10.1.1.0/24        2        Transit    10.2.1.1        10.1.1.1        0.0.0.0        
    10.2.1.0/24        1        Direct     10.2.1.2        4.4.4.4         0.0.0.0        
   
    Total Nets: 5
    Intra Area: 5  Inter Area: 0  ASE: 0  NSSA: 0
   ```
3. Configure MPLS and MPLS LDP and establish LSPs.
   
   
   
   # Configure UPE1.
   
   ```
   [~UPE1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*UPE1] mpls
   ```
   ```
   [*UPE1-mpls] quit
   ```
   ```
   [*UPE1] mpls ldp
   ```
   ```
   [*UPE1-mpls-ldp] quit
   ```
   ```
   [*UPE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*UPE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*UPE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*UPE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*UPE1] commit
   ```
   
   # Configure SPE1.
   
   ```
   [~SPE1] mpls lsr-id 2.2.2.2
   ```
   ```
   [*SPE1] mpls
   ```
   ```
   [*SPE1-mpls] quit
   ```
   ```
   [*SPE1] mpls ldp
   ```
   ```
   [*SPE1-mpls-ldp] quit
   ```
   ```
   [*SPE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*SPE1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*SPE1-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*SPE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*SPE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*SPE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*SPE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*SPE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   # Configure NPE1.
   
   ```
   [~NPE1] mpls lsr-id 4.4.4.4
   ```
   ```
   [*NPE1] mpls
   ```
   ```
   [*NPE1-mpls] quit
   ```
   ```
   [*NPE1] mpls ldp
   ```
   ```
   [*NPE1-mpls-ldp] quit
   ```
   ```
   [*NPE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*NPE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*NPE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*NPE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE1] commit
   ```
   
   # After the configuration is complete, check LDP LSP information. The following example uses the command output on NPE1.
   
   ```
   [~NPE1] display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   --------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------
    2.2.2.2:0          Operational DU   Active   0000:03:46   906/906
   --------------------------------------------------------------------------
   TOTAL: 1 Session(s) Found.
   ```
4. Configure PBB VPLS.
   1. Enable MPLS L2VPN.
      
      
      
      # Configure UPE1.
      
      ```
      [~UPE1] mpls l2vpn
      ```
      ```
      [*UPE1-l2vpn] quit
      ```
      ```
      [*UPE1] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] mpls l2vpn
      ```
      ```
      [*SPE1-l2vpn] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure NPE1.
      
      ```
      [~NPE1] mpls l2vpn
      ```
      ```
      [*NPE1-l2vpn] quit
      ```
      ```
      [*NPE1] commit
      ```
   2. Configure I-VSIs.
      
      
      
      # Configure UPE1.
      
      ```
      [~UPE1] vsi ivsi1 i-vsi p2p
      ```
      ```
      [*UPE1-vsi-ivsi1] pwsignal ldp
      ```
      ```
      [*UPE1-vsi-ivsi1-ldp] vsi-id 10
      ```
      ```
      [*UPE1-vsi-ivsi1-ldp] quit
      ```
      ```
      [*UPE1-vsi-ivsi1] pbb i-tag 100
      ```
      ```
      [*UPE1-vsi-ivsi1] pbb backbone-destination-mac 00e0-fc00-1234 static
      ```
      ```
      [*UPE1-vsi-ivsi1] quit
      ```
      ```
      [*UPE1] commit
      ```
      
      # Configure NPE1.
      
      ```
      [~NPE1] vsi ivsi1 i-vsi p2p
      ```
      ```
      [*NPE1-vsi-ivsi1] pwsignal ldp
      ```
      ```
      [*NPE1-vsi-ivsi1-ldp] vsi-id 10
      ```
      ```
      [*NPE1-vsi-ivsi1-ldp] quit
      ```
      ```
      [*NPE1-vsi-ivsi1] pbb i-tag 100
      ```
      ```
      [*NPE1-vsi-ivsi1] pbb backbone-destination-mac 00e0-fc12-3456 static
      ```
      ```
      [*NPE1-vsi-ivsi1] quit
      ```
      ```
      [*NPE1] commit
      ```
   3. Configure B-VSIs and specify peers for these B-VSIs.
      
      
      
      # Configure UPE1.
      
      ```
      [~UPE1] vsi bvsi1 b-vsi
      ```
      ```
      [*UPE1-vsi-bvsi1] pwsignal ldp
      ```
      ```
      [*UPE1-vsi-bvsi1-ldp] vsi-id 20
      ```
      ```
      [*UPE1-vsi-bvsi1-ldp] peer 2.2.2.2
      ```
      ```
      [*UPE1-vsi-bvsi1-ldp] quit
      ```
      ```
      [*UPE1-vsi-bvsi1] pbb backbone-source-mac 00e0-fc12-3456
      ```
      ```
      [*UPE1-vsi-bvsi1] quit
      ```
      ```
      [*UPE1] commit
      ```
      
      # Configure SPE1.
      
      ```
      [~SPE1] vsi bvsi1
      ```
      ```
      [*SPE1-vsi-bvsi1] pwsignal ldp
      ```
      ```
      [*SPE1-vsi-bvsi1-ldp] vsi-id 20
      ```
      ```
      [*SPE1-vsi-bvsi1-ldp] peer 1.1.1.1 upe
      ```
      ```
      [*SPE1-vsi-bvsi1-ldp] peer 4.4.4.4
      ```
      ```
      [*SPE1-vsi-bvsi1-ldp] quit
      ```
      ```
      [*SPE1-vsi-bvsi1] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure NPE1.
      
      ```
      [~NPE1] vsi bvsi1 b-vsi
      ```
      ```
      [*NPE1-vsi-bvsi1] pwsignal ldp
      ```
      ```
      [*NPE1-vsi-bvsi1-ldp] vsi-id 20
      ```
      ```
      [*NPE1-vsi-bvsi1-ldp] peer 2.2.2.2
      ```
      ```
      [*NPE1-vsi-bvsi1-ldp] quit
      ```
      ```
      [*NPE1-vsi-bvsi1] pbb backbone-source-mac 00e0-fc00-1234
      ```
      ```
      [*NPE1-vsi-bvsi1] quit
      ```
      ```
      [*NPE1] commit
      ```
   4. Bind each I-VSI to the corresponding B-VSI.
      
      # Configure UPE1.
      ```
      [~UPE1] vsi ivsi1
      ```
      ```
      [*UPE1-vsi-ivsi1] pbb binding b-vsi bvsi1
      ```
      ```
      [*UPE1-vsi-ivsi1] quit
      ```
      ```
      [*UPE1] commit
      ```
      
      # Configure NPE1.
      ```
      [~NPE1] vsi ivsi1
      ```
      ```
      [*NPE1-vsi-ivsi1] pbb binding b-vsi bvsi1
      ```
      ```
      [*NPE1-vsi-ivsi1] quit
      ```
      ```
      [*NPE1] commit
      ```
   5. Bind an AC interface to each I-VSI.
      
      
      
      # Configure UPE1.
      
      ```
      [~UPE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [~UPE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
      ```
      ```
      [*UPE1-GigabitEthernet0/1/0.1] l2 binding vsi ivsi1
      ```
      ```
      [*UPE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*UPE1] commit
      ```
      
      # Configure NPE1.
      
      ```
      [~NPE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [~NPE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
      ```
      ```
      [*NPE1-GigabitEthernet0/1/0.1] l2 binding vsi ivsi1
      ```
      ```
      [*NPE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*NPE1] commit
      ```
5. Verify the configuration.
   
   
   
   After the configuration is complete, CE1 and CE2 can ping each other. Ping CE2 from CE1. The command output shows that the ping operation is successful.
   
   ```
   [~UPE1] ping 10.3.1.2
   ```
   ```
   PING 10.3.1.2: 56  data bytes, press CTRL_C to break
       Reply from 10.3.1.2: bytes=56 Sequence=1 ttl=255 time=3 ms
       Reply from 10.3.1.2: bytes=56 Sequence=2 ttl=255 time=1 ms
       Reply from 10.3.1.2: bytes=56 Sequence=3 ttl=255 time=2 ms
       Reply from 10.3.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
       Reply from 10.3.1.2: bytes=56 Sequence=5 ttl=255 time=2 ms
   
     --- 10.3.1.2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/1/3 ms
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
   ip address 10.3.1.1 255.255.255.0                                              
  #                                                                               
  return                                                        
  ```
* UPE1 configuration file
  
  ```
  #                                                                               
  sysname UPE1                                                                    
  #                                                                               
  mpls lsr-id 1.1.1.1
  #                                                            
  mpls                                                                           
  #                                                                               
  mpls l2vpn                                                                     
  #                                                                               
  vsi bvsi1 b-vsi
   pwsignal ldp
    vsi-id 20                                                                     
    peer 2.2.2.2                                                                  
   pbb backbone-source-mac 00e0-fc12-3456                                         
  #                                                                               
  vsi ivsi1 i-vsi p2p
   pwsignal ldp
    vsi-id 10                                                                
   pbb i-tag 100                                                                  
   pbb backbone-destination-mac 00e0-fc00-1234 static                                    
   pbb binding b-vsi bvsi1                                                          
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 10                                                             
   l2 binding vsi ivsi1                                                            
  #                                                                               
  interface GigabitEthernet0/2/0                                                  
   undo shutdown                                                                  
   ip address 10.1.1.1 255.255.255.0                                             
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                               
  interface LoopBack0                                                             
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                                               
  ospf 1                                                                          
   area 0.0.0.0                                                                   
    network 10.1.1.0 0.0.0.255                                                   
    network 1.1.1.1 0.0.0.0                                                       
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
  #                                                                               
  mpls l2vpn                                                                     
  #                                                                               
  vsi bvsi1                                                                  
   pwsignal ldp                                                                   
    vsi-id 20                                                                     
    peer 1.1.1.1 upe                                                              
    peer 4.4.4.4                                                                  
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
   ip address 10.2.1.1 255.255.255.0                                             
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                               
  interface LoopBack0                                                             
   ip address 2.2.2.2 255.255.255.255                                             
  #                                                                               
  ospf 1                                                                          
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 10.1.1.0 0.0.0.255                                                   
    network 10.2.1.0 0.0.0.255                                                   
  #                                                                               
  return                                                                          
  ```
* NPE1 configuration file
  
  ```
  #                                                                               
  sysname NPE1                                                                   
  #                                                                               
  mpls lsr-id 4.4.4.4
  #                                                            
  mpls                                                                           
  #                                                                               
  mpls l2vpn                                                                     
  #                                                                               
  vsi bvsi1 b-vsi
   pwsignal ldp
    vsi-id 20                                                                     
    peer 2.2.2.2                                                                  
   pbb backbone-source-mac 00e0-fc00-1234                                         
  #                                                                               
  vsi ivsi1 i-vsi p2p
   pwsignal ldp
    vsi-id 10                                                                
   pbb i-tag 100                                                                  
   pbb backbone-destination-mac 00e0-fc12-3456 static                                    
   pbb binding b-vsi bvsi1                                                          
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 10                                                             
   l2 binding vsi ivsi1                                                            
  #                                                                               
  interface GigabitEthernet0/2/0                                                  
   undo shutdown                                                                  
   ip address 10.2.1.2 255.255.255.0                                             
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                               
  interface LoopBack0                                                             
   ip address 4.4.4.4 255.255.255.255                                             
  #                                                                               
  ospf 1                                                                          
   area 0.0.0.0                                                                   
    network 10.2.1.0 0.0.0.255                                                   
    network 4.4.4.4 0.0.0.0                                                       
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
   ip address 10.3.1.2 255.255.255.0                                              
  #                                                                               
  return                                                        
  ```