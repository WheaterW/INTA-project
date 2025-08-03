Example for Configuring EVC-based VPLS Accessing L3VPN
======================================================

Example for Configuring EVC-based VPLS Accessing L3VPN

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172363414__fig_dc_vrp_evc_cfg_004001), on the access network, the CSG provides a BD for user site access and connects to the ASG over a VPLS PW; on the bearer network, the ASG uses the VBDIF interface to terminate the VPLS PW and establishes an L3VPN with the RSG.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, sub-interface 1.1, and interface 2 stand for GE 0/1/0, GE 0/1/0.1, and GE 0/2/0, respectively.


**Figure 1** EVC-based L2VPN accessing L3VPN  
![](images/fig_dc_vrp_evc_cfg_004001.png)  


#### Configuration Roadmap

1. Configure IP addresses and IGPs on the CSG, ASG, and RSG.
2. Configure LDP LSPs on the CSG, ASG, and RSG.
3. Configure EVC VPLS on the CSG and ASG.
   1. Create an EVC Layer 2 sub-interface and a BD and add the sub-interface to the BD.
   2. Create a BD VSI, specify the signaling protocol as LDP, and bind the VSI to the corresponding BD.
4. Configure an L3VPN on the ASG and RSG.
   1. Configure VPN instances using the IPv4 address family.
   2. Establish an MP-IBGP peer relationship.
   3. Create a VBDIF interface on the ASG and bind the VBDIF interface to the L3VPN.

#### Data Preparation

To complete the configuration, you need the following data:

* BD IDs on the CSG and ASG
* VSI IDs on the CSG and ASG (must be the same)
* VSI names and interfaces bound to VSIs on the CSG and ASG
* MPLS LSR IDs on the CSG, ASG, and RSG
* VPN instance names and VPN targets on the ASG and RSG

#### Procedure

1. Assign an IP address to each node interface, including the loopback interface.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172363414__dc_vrp_evc_cfg_0040_example).
2. Configure an IGP on each node. In this example, OSPF is used.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172363414__dc_vrp_evc_cfg_0040_example).
3. Configure an MPLS LDP tunnel on each node.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172363414__dc_vrp_evc_cfg_0040_example).
4. Configure EVC VPLS on the CSG and ASG.
   1. Create an EVC Layer 2 sub-interface and a BD, and add the EVC Layer 2 sub-interface to the BD only on the CSG.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The status of a BD is determined by the status of all EVC Layer 2 sub-interfaces in the BD and the VSI. A BD goes Down only when all its EVC Layer 2 sub-interfaces and the VSI are both Down.
      
      # Configure the CSG.
      
      ```
      [~CSG] bridge-domain 1
      ```
      ```
      [*CSG-bd1] quit
      ```
      ```
      [*CSG] interface GigabitEthernet 0/1/0.1 mode l2
      ```
      ```
      [*CSG-GigabitEthernet0/1/0.1] encapsulation dot1q vid 1
      ```
      ```
      [*CSG-GigabitEthernet0/1/0.1] rewrite pop single
      ```
      ```
      [*CSG-GigabitEthernet0/1/0.1] bridge-domain 1
      ```
      ```
      [*CSG-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Configure the ASG.
      
      ```
      [~ASG] bridge-domain 1
      ```
      ```
      [*ASG-bd1] quit
      ```
      ```
      [*ASG] commit
      ```
   2. Enable MPLS L2VPN.
      
      
      
      # Configure the CSG.
      
      ```
      [~CSG] mpls l2vpn
      ```
      ```
      [*CSG-l2vpn] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Configure the ASG.
      
      ```
      [~ASG] mpls l2vpn
      ```
      ```
      [*ASG-l2vpn] quit
      ```
      ```
      [*ASG] commit
      ```
   3. Create a BD VSI, specify the signaling protocol as LDP, and bind the VSI to the corresponding BD.
      
      
      
      # Configure the CSG.
      
      ```
      [~CSG] vsi evc-vsi bd-mode
      ```
      ```
      [*CSG-vsi-evc-vsi] pwsignal ldp
      ```
      ```
      [*CSG-vsi-evc-vsi-ldp] vsi-id 10
      ```
      ```
      [*CSG-vsi-evc-vsi-ldp] peer 2.2.2.9
      ```
      ```
      [*CSG-vsi-evc-vsi-ldp] quit
      ```
      ```
      [*CSG-vsi-evc-vsi] quit
      ```
      ```
      [*CSG] bridge-domain 1
      ```
      ```
      [*CSG-bd1] l2 binding vsi evc-vsi pw-tag 1
      ```
      ```
      [*CSG-bd1] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Configure the ASG.
      
      ```
      [~ASG] vsi evc-vsi bd-mode
      ```
      ```
      [*ASG-vsi-evc-vsi] pwsignal ldp
      ```
      ```
      [*ASG-vsi-evc-vsi-ldp] vsi-id 10
      ```
      ```
      [*ASG-vsi-evc-vsi-ldp] peer 1.1.1.9
      ```
      ```
      [*ASG-vsi-evc-vsi-ldp] quit
      ```
      ```
      [*ASG-vsi-evc-vsi] quit
      ```
      ```
      [*ASG] bridge-domain 1
      ```
      ```
      [*ASG-bd1] l2 binding vsi evc-vsi pw-tag 1
      ```
      ```
      [*ASG-bd1] quit
      ```
      ```
      [*ASG] commit
      ```
5. Configure an L3VPN on the ASG and RSG.
   1. Configure VPN instances using the IPv4 address family.
      
      
      
      # Configure the ASG.
      
      ```
      [~ASG] ip vpn-instance vpna
      ```
      ```
      [*ASG-vpn-instance-vpna] ipv4-family
      ```
      ```
      [*ASG-vpn-instance-vpna-af-ipv4] route-distinguisher 100:100
      ```
      ```
      [*ASG-vpn-instance-vpna-af-ipv4] vpn-target 100:100 export-extcommunity
      ```
      ```
      [*ASG-vpn-instance-vpna-af-ipv4] vpn-target 100:100 import-extcommunity
      ```
      ```
      [*ASG-vpn-instance-vpna-af-ipv4] quit
      ```
      ```
      [*ASG-vpn-instance-vpna] quit
      ```
      ```
      [*ASG] commit
      ```
      
      # Configure the RSG.
      
      ```
      [~RSG] ip vpn-instance vpna
      ```
      ```
      [*RSG-vpn-instance-vpna] ipv4-family
      ```
      ```
      [*RSG-vpn-instance-vpna-af-ipv4] route-distinguisher 100:100
      ```
      ```
      [*RSG-vpn-instance-vpna-af-ipv4] vpn-target 100:100 export-extcommunity
      ```
      ```
      [*RSG-vpn-instance-vpna-af-ipv4] vpn-target 100:100 import-extcommunity
      ```
      ```
      [*RSG-vpn-instance-vpna-af-ipv4] quit
      ```
      ```
      [*RSG-vpn-instance-vpna] quit
      ```
      ```
      [*RSG] commit
      ```
   2. Establish an MP-IBGP peer relationship.
      
      
      
      # Configure the ASG.
      
      ```
      [~ASG] bgp 100
      ```
      ```
      [*ASG-bgp] peer 3.3.3.9 as-number 100
      ```
      ```
      [*ASG-bgp] peer 3.3.3.9 connect-interface LoopBack 1
      ```
      ```
      [*ASG-bgp] ipv4-family vpnv4
      ```
      ```
      [*ASG-bgp-af-vpnv4] peer 3.3.3.9 enable
      ```
      ```
      [*ASG-bgp-af-vpnv4] quit
      ```
      ```
      [*ASG-bgp] quit
      ```
      ```
      [*ASG] commit
      ```
      
      # Configure the RSG.
      
      ```
      [~RSG] bgp 100
      ```
      ```
      [*RSG-bgp] peer 2.2.2.9 as-number 100
      ```
      ```
      [*RSG-bgp] peer 2.2.2.9 connect-interface LoopBack 1
      ```
      ```
      [*RSG-bgp] ipv4-family vpnv4
      ```
      ```
      [*RSG-bgp-af-vpnv4] peer 2.2.2.9 enable
      ```
      ```
      [*RSG-bgp-af-vpnv4] quit
      ```
      ```
      [*RSG-bgp] quit
      ```
      ```
      [*RSG] commit
      ```
   3. Create a VBDIF interface on the ASG and bind the VBDIF interface to the L3VPN. On the RSG, bind GE 0/2/0 to the L3VPN.
      
      
      
      # Configure the ASG.
      
      ```
      [~ASG] interface Vbdif 1
      ```
      ```
      [*ASG-Vbdif1] ip binding vpn-instance vpna
      ```
      ```
      [*ASG-Vbdif1] ip address 10.1.1.2 24
      ```
      ```
      [*ASG-Vbdif1] quit
      ```
      ```
      [*ASG] commit
      ```
      
      # Configure the RSG.
      
      ```
      [~RSG] interface gigabitethernet 0/2/0
      ```
      ```
      [*RSG-GigabitEthernet0/2/0] ip binding vpn-instance vpna
      ```
      ```
      [*RSG-GigabitEthernet0/2/0] ip address 10.4.4.1 24
      ```
      ```
      [*RSG-GigabitEthernet0/2/0] quit
      ```
      ```
      [*RSG] commit
      ```
   4. Import indirect VPN routes.
      
      
      
      # Configure the ASG.
      
      ```
      [~ASG] bgp 100
      ```
      ```
      [*ASG-bgp] ipv4-family vpn-instance vpna
      ```
      ```
      [*ASG-bgp-vpna] import-route direct
      ```
      ```
      [*ASG-bgp-vpna] quit
      ```
      ```
      [*ASG-bgp] quit
      ```
      ```
      [*ASG] commit
      ```
      
      # Configure the RSG.
      
      ```
      [~RSG] bgp 100
      ```
      ```
      [*RSG-bgp] ipv4-family vpn-instance vpna
      ```
      ```
      [*RSG-bgp-vpna] import-route direct
      ```
      ```
      [*RSG-bgp-vpna] quit
      ```
      ```
      [*RSG-bgp] quit
      ```
      ```
      [*RSG] commit
      ```
6. Verify the configuration. 
   
   
   
   After completing the configuration, run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) command. The command output shows the BD to which an EVC Layer 2 sub-interface belongs and the BD status. The following example uses the command output on the CSG.
   
   ```
   [~CSG] display bridge-domain 1
   ```
   ```
   --------------------------------------------------------------------------------
   MAC_LRN: MAC learning;         STAT: Statistics;         SPLIT: Split-horizon;
   BC: Broadcast;                 MC: Unknown multicast;    UC: Unknown unicast;
   *down: Administratively down;  FWD: Forward;             DSD: Discard;
   U: Up;         D: Down;
   --------------------------------------------------------------------------------
   
   BDID         Ports                                                          
   --------------------------------------------------------------------------------
   1            GE0/1/0.1(U)                                                      
   
   BDID  State MAC-LRN STAT    BC  MC  UC  SPLIT   Description
   --------------------------------------------------------------------------------
   1     up    enable  disable FWD FWD FWD disable    
   ```
   
   Run the **display vsi name evc-vsi** command. The command output shows that the VSI named **evc-vsi** is **up**. The following example uses the command output on the CSG.
   
   ```
   [~CSG] display vsi name evc-vsi
   ```
   ```
   --------------------------------------------------------------------------
   Vsi                             Mem    PW    Mac       Encap     Mtu   Vsi
   Name                            Disc   Type  Learn     Type      Value State
   --------------------------------------------------------------------------
   evc-vsi                         --     ldp   qualify   vlan      1500  up  
   ```
   
   Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) command. The command output shows IPv4 VPN instance routing table information. The following example uses the command output on the ASG.
   
   ```
   [~ASG] display ip routing-table vpn-instance vpna
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
            Destinations : 5        Routes : 5         
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  Direct  0    0             D   10.1.1.2        Vbdif1
          10.1.1.2/32  Direct  0    0             D   127.0.0.1       Vbdif1
        10.1.1.255/32  Direct  0    0             D   127.0.0.1       Vbdif1
          10.4.4.0/24  IBGP    255  0             RD  3.3.3.9         GigabitEthernet0/2/0
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   
   ```

#### Configuration Files

* CSG configuration file
  
  ```
  #
  sysname CSG
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls l2vpn
  #
  vsi evc-vsi bd-mode
   pwsignal ldp
    vsi-id 10
    peer 2.2.2.9  
  #               
  bridge-domain 1 
   l2 binding vsi evc-vsi pw-tag 1
  #               
  mpls ldp        
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
  #               
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 1
   rewrite pop single
   bridge-domain 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.2.2.1 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #               
  ospf 1          
   area 0.0.0.0   
    network 1.1.1.9 0.0.0.0
    network 10.2.2.0 0.0.0.255
  #               
  return
  ```
* ASG configuration file
  
  ```
  #
  sysname ASG
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:100
    apply-label per-instance
    vpn-target 100:100 export-extcommunity
    vpn-target 100:100 import-extcommunity
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #               
  mpls l2vpn      
  #               
  vsi evc-vsi bd-mode
   pwsignal ldp   
    vsi-id 10     
    peer 1.1.1.9  
  #               
  bridge-domain 1 
   l2 binding vsi evc-vsi pw-tag 1
  #               
  mpls ldp        
  #               
  interface Vbdif 1
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.2.2.2 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.3.3.1 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
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
   ipv4-family vpn-instance vpna
    import-route direct
  #               
  ospf 1          
   area 0.0.0.0   
    network 2.2.2.9 0.0.0.0
    network 10.2.2.0 0.0.0.255
    network 10.3.3.0 0.0.0.255
  #               
  return
  ```
* RSG configuration file
  
  ```
  #
  sysname RSG
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:100
    apply-label per-instance
    vpn-target 100:100 export-extcommunity
    vpn-target 100:100 import-extcommunity
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #               
  mpls ldp        
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.3.3.2 255.255.255.0
   mpls           
   mpls ldp       
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.4.4.1 255.255.255.0
  #               
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.0
  #               
  bgp 100         
   peer 2.2.2.9 as-number 100
   peer 2.2.2.9 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.9 enable
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.9 enable
   #              
   ipv4-family vpn-instance vpna
    import-route direct
  #               
  ospf 1          
   area 0.0.0.0   
    network 3.3.3.9 0.0.0.0
    network 10.3.3.0 0.0.0.255
  #               
  return
  ```