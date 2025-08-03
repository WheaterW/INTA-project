Example for Configuring a Local CCC to Access an L3VPN
======================================================

A local CCC can access an L3VPN through a VE group.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370368__fig_dc_vrp_l2-l3_cfg_501401), the local CCC configured on PE1 accesses the L3VPN between PE1 and PE2.

**Figure 1** Configuring a local CCC to access an L3VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_l2-l3_cfg_501401.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface.
2. Configure public network routes between PE1 and PE2 and advertise IP addresses of loopback interfaces.
3. Enable MPLS and MPLS LDP on PE1 and PE2, and enable MPLS L2VPN on PE1.
4. Configure a local CCC on PE1.
5. Configure an L3VPN on PE1 and PE2.

#### Data Preparation

To complete the configuration, you need the following data:

* VE-Group ID
* IP addresses of the interfaces

#### Procedure

1. Assign an IP address to each interface. Configuration details are not mentioned here. For details, please check Configuration Files.
2. Configure public network routes between PE1 and PE2 and advertise IP addresses of loopback interfaces. IS-IS is adopted here, and configuration details are not mentioned. For details, please check Configuration Files.
3. Enable MPLS and MPLS LDP on PE1 and PE2. Enable MPLS L2VPN on PE1. For detailed configurations, see Configuration Files.
4. Configure a local CCC on PE1.
   1. Configure an L2VE interface and an L3VE interface on PE1, and add these interfaces to a VE group.
      
      
      ```
      [~PE1] interface virtual-ethernet0/1/0
      [*PE1-Virtual-Ethernet0/1/0] ve-group 1 l2-terminate
      [*PE1-Virtual-Ethernet0/1/0] quit
      [*PE1] interface virtual-ethernet0/1/1
      [*PE1-Virtual-Ethernet0/1/1] ve-group 1 l3-access
      [*PE1-Virtual-Ethernet0/1/1] quit
      [*PE1] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This example uses VE interfaces to implement L2VPN accessing L3VPN. Because VE interfaces are bound to only one board, services are interrupted when the board fails. To improve service reliability, create two global VE interfaces on NPEs: Global-VE1 (L2VE interface used to terminate L2VPN services) and Global-VE2 (L3VE interface used to access an L3VPN network). Other configurations do not need to be changed.
   2. Configure a local CCC on PE1, with the inbound interface as the PE1 interface connecting to CE1 and the outbound interface as the L2VE interface.
      
      
      ```
      [~PE1] interface virtual-ethernet0/1/0.1
      [*PE1-Virtual-Ethernet0/1/0.1] vlan-type dot1q 100
      [*PE1-Virtual-Ethernet0/1/0.1] quit
      [*PE1] ccc ccc-ve interface gigabitethernet 0/1/0 out-interface virtual-ethernet0/1/0.1
      [*PE1] commit
      ```
   3. Verify the configuration. Run the **display vll ccc** command to check whether the local CCC is in the up state.
      
      
      ```
      [~PE1] display vll ccc
      total  ccc vc : 1
      local  ccc vc : 1,  1 up
      remote ccc vc : 0,  0 up
      
      name: ccc-ve, type: local, state: up,
      intf1: GigabitEthernet0/1/0 (up),access-port: false
      
      intf2: Virtual-Ethernet0/1/0.1 (up),access-port: false
      
      VC last up time : 2013/01/23 15:13:10
      VC total up time:  4 days, 4 hours, 58 minutes, 1 seconds
      ```
5. Configure an L3VPN on PE1 and PE2.
   1. Configure a VPN instance and bind the corresponding interface to the VPN instance.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] ip vpn-instance VPN1
      [*PE1-vpn-instance-VPN1] ipv4-family
      [*PE1-vpn-instance-VPN1-af-ipv4] route-distinguisher 200:1
      [*PE1-vpn-instance-VPN1-af-ipv4] vpn-target 111:1 both
      [*PE1-vpn-instance-VPN1-af-ipv4] quit
      [*PE1-vpn-instance-VPN1] quit
      [*PE1] interface virtual-ethernet0/1/1.1
      [*PE1-Virtual-Ethernet0/1/1.1] vlan-type dot1q 100
      [*PE1-Virtual-Ethernet0/1/1.1] ip binding vpn-instance VPN1
      [*PE1-Virtual-Ethernet0/1/1.1] ip address 10.1.1.2 24
      [*PE1-Virtual-Ethernet0/1/1.1] quit
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] ip vpn-instance VPN1
      [*PE2-vpn-instance-VPN1] ipv4-family
      [*PE2-vpn-instance-VPN1-af-ipv4] route-distinguisher 200:1
      [*PE2-vpn-instance-VPN1-af-ipv4] vpn-target 111:1 both
      [*PE2-vpn-instance-VPN1-af-ipv4] quit
      [*PE2-vpn-instance-VPN1] quit
      [*PE2] interface gigabitethernet0/1/1
      [*PE2-GigabitEthernet0/1/1] ip binding vpn-instance VPN1
      [*PE2-GigabitEthernet0/1/1] ip address 10.10.2.2 24
      [*PE2-GigabitEthernet0/1/1] undo shutdown
      [*PE2-GigabitEthernet0/1/1] quit
      [*PE2] commit
      ```
   2. Set up EBGP peer relationships between PEs and CEs and import VPN routes.
      
      
      
      # Configure CE1.
      
      ```
      [~CE1] bgp 65010
      [*CE1-bgp] peer 10.1.1.2 as-number 100
      [*CE1-bgp] import-route direct
      [*CE1-bgp] commit
      ```
      
      # Configure CE2.
      
      ```
      [~CE2] bgp 65020
      [*CE2-bgp] peer 10.10.2.2 as-number 100
      [*CE2-bgp] import-route direct
      [*CE2-bgp] commit
      ```
      
      # Configure PE1.
      
      ```
      [~PE1] bgp 100
      [*PE1-bgp] ipv4-family vpn-instance VPN1
      [*PE1-bgp-VPN1] peer 10.1.1.1 as-number 65010
      [*PE1-bgp-VPN1] import-route direct
      [*PE1-bgp-VPN1] quit
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] bgp 100
      [*PE2-bgp] ipv4-family vpn-instance VPN1
      [*PE2-bgp-VPN1] peer 10.10.2.1 as-number 65020
      [*PE2-bgp-VPN1] import-route direct
      [*PE2-bgp-VPN1] quit
      [*PE2] commit
      ```
   3. Set up the MP-IBGP peer relationship between PE1 and PE2.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] bgp 100
      [*PE1-bgp] peer 2.2.2.2 as-number 100
      [*PE1-bgp] peer 2.2.2.2 connect-interface loopback 0
      [*PE1-bgp] ipv4-family vpnv4
      [*PE1-bgp-af-vpnv4] peer 2.2.2.2 enable
      [*PE1-bgp-af-vpnv4] quit
      [*PE1-bgp] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] bgp 100
      [*PE2-bgp] peer 4.4.4.4 as-number 100
      [*PE2-bgp] peer 4.4.4.4 connect-interface loopback 0
      [*PE2-bgp] ipv4-family vpnv4
      [*PE2-bgp-af-vpnv4] peer 4.4.4.4 enable
      [*PE2-bgp-af-vpnv4] quit
      [*PE2-bgp] commit
      ```
6. Verify the configuration. CE1 and CE2 can ping each other successfully. The following example uses the command output on CE1.
   
   
   ```
   <CE1> ping 10.10.2.1
     PING 10.10.2.1: 56  data bytes, press CTRL_C to break
       Reply from 10.10.2.1: bytes=56 Sequence=1 ttl=255 time=180 ms
       Reply from 10.10.2.1: bytes=56 Sequence=2 ttl=255 time=60 ms
       Reply from 10.10.2.1: bytes=56 Sequence=3 ttl=255 time=10 ms
       Reply from 10.10.2.1: bytes=56 Sequence=4 ttl=255 time=70 ms
       Reply from 10.10.2.1: bytes=56 Sequence=5 ttl=255 time=60 ms
     --- 10.10.2.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 10/76/180 ms
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #                                                                               
   sysname CE1                                                              
  #                                                                                                                     
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.1.1.1 255.255.255.0                                              
  #                                                      
  bgp 65010                                                                       
   peer 10.1.1.2 as-number 100                                                    
   #                                                                              
   ipv4-family unicast    
    undo synchronization                                                        
    import-route direct                                                           
    peer 10.1.1.2 enable                                                          
   #                                                                              
  return                  
  ```
* PE1 configuration file
  
  ```
  #                                                                               
   sysname PE1                                                              
  #                                                                               
  ip vpn-instance VPN1
   ipv4-family
   route-distinguisher 200:1
   apply-label per-instance
   vpn-target 111:1 export-extcommunity                                           
   vpn-target 111:1 import-extcommunity                                           
  #                                                                               
   mpls lsr-id 4.4.4.4                                                            
   mpls                                                                           
  #                                                                               
   mpls l2vpn                                                                     
  #                                                                               
  mpls ldp                                                                        
  isis 1                                                                          
   network-entity 10.0000.0000.0004.00                                            
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 10.10.1.1 255.255.255.0                                             
   isis enable 1                                                                  
   mpls                                                                           
   mpls ldp                                                                       
  #                                      
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
  #                                             
  interface Virtual-Ethernet0/1/0                                                 
   ve-group 1 l2-terminate                                                        
  #                                                                               
  interface Virtual-Ethernet0/1/0.1                                               
   vlan-type dot1q 100                                                            
  #                                                                               
  interface Virtual-Ethernet0/1/1                                                 
   ve-group 1 l3-access                                                           
  #                                                                               
  interface Virtual-Ethernet0/1/1.1                                               
   vlan-type dot1q 100                                                            
   ip binding vpn-instance VPN1                                                   
   ip address 10.1.1.2 255.255.255.0                                              
  #                                                               
   ccc ccc-ve interface GigabitEthernet0/1/0 out-interface Virtual-Ethernet0/1/0.1
  #                                                                               
  interface LoopBack0                                                             
   ip address 4.4.4.4 255.255.255.255                                             
   isis enable 1                                                                  
  #                                                   
  bgp 100                                                                         
   peer 2.2.2.2 as-number 100                                                     
   peer 2.2.2.2 connect-interface LoopBack0                                       
   #                                                                              
   ipv4-family unicast      
    undo synchronization                                                         
    peer 2.2.2.2 enable                                                           
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2.2.2.2 enable                                                           
   #                                                                              
   ipv4-family vpn-instance VPN1                                                  
    import-route direct                                                           
    peer 10.1.1.1 as-number 65010                                                 
  #                                         
  return                                                
  ```
* PE2 configuration file
  
  ```
  #                                                                               
  sysname PE2                                                              
  #                                            
  ip vpn-instance VPN1
   ipv4-family
   route-distinguisher 200:1
   apply-label per-instance                                                     
   vpn-target 111:1 export-extcommunity                                           
   vpn-target 111:1 import-extcommunity                                           
  #                                                                               
   mpls lsr-id 2.2.2.2                                                            
   mpls                                                                           
  #                                                                               
  mpls ldp                                                                        
  #                                              
  isis 1                                                                          
   network-entity 10.0000.0000.0003.00                                            
  #                                    
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip binding vpn-instance VPN1                                                   
   ip address 10.10.2.2 255.255.255.0                                             
  #                                   
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ip address 10.10.1.2 255.255.255.0                                             
   isis enable 1                                                                  
   mpls                                                                           
   mpls ldp                                                                       
  #                                  
  interface LoopBack0                                                             
   ip address 2.2.2.2 255.255.255.255                                             
   isis enable 1                                                                  
  #                                                        
  bgp 100                                                                         
   peer 4.4.4.4 as-number 100                                                     
   peer 4.4.4.4 connect-interface LoopBack0                                       
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization 
    peer 4.4.4.4 enable                                                           
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 4.4.4.4 enable                                                           
   #                                                                              
   ipv4-family vpn-instance VPN1                                                  
    import-route direct                                                           
    peer 10.10.2.1 as-number 65020                                                
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
   ip address 10.10.2.1 255.255.255.0                                             
  #                                       
  bgp 65020                                                                       
   peer 10.10.2.2 as-number 100                                                   
   #                                                                              
   ipv4-family unicast                                                              
    undo synchronization                                                         
    import-route direct                                                           
    peer 10.10.2.2 enable                                                         
  #                                                   
  return                            
  ```