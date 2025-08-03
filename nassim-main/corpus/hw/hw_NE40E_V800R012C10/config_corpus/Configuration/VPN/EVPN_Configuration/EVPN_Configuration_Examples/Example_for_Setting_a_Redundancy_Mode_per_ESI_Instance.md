Example for Setting a Redundancy Mode per ESI Instance
======================================================

This section provides an example for setting a redundancy mode per ESI instance. In scenarios where multiple CEs are dual-homed to PEs, if you want a remote PE to send unicast traffic to different CEs in different modes (load balancing and non-load balancing), you can set a redundancy mode per ESI instance.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370606__fig62019292311), a user wants to deploy an EVPN to transmit services. In this case, you must configure an EVPN instance (BD EVPN instance in this example) on each PE and configure each PE to establish a BGP EVPN peer relationship with its neighboring PE. CE1 and CE2 are each dual-homed to PE1 and PE2. Statically set ESI values on PE1's and PE2's interfaces connecting to CE1 and CE2. If you want unicast traffic from CE3 to CE1 and from CE3 to CE2 to be transmitted in load-balancing and non-load-balancing modes, respectively, you can set a redundancy mode per ESI instance. Specifically, you can set the redundancy mode of the ESI1 instance to all-active and that of the ESI2 instance to single-active.

**Figure 1** Setting a redundancy mode per ESI instance![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, interface3, and interface4 in this example represent GigabitEthernet0/1/1, GigabitEthernet0/1/2, GigabitEthernet0/1/3, and GigabitEthernet0/1/4, respectively.


  
![](figure/en-us_image_0000001300989190.png)  


#### Configuration Precautions

During the configuration process, note the following:

* For the same EVPN instance, the export VPN target list of one site shares VPN targets with the import VPN target lists of the other sites. Conversely, the import VPN target list of one site shares VPN targets with the export VPN target lists of the other sites.
* Using each PE's local loopback interface address as its EVPN source address is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each PE interface, including the loopback interfaces.
2. Configure a routing protocol on each PE to ensure Layer 3 communication. OSPF is used in this example.
3. Configure MPLS LDP on each PE.
4. Create a BD EVPN instance and a BD on each PE, and bind the BD to the EVPN instance.
5. Configure E-Trunks on each PE and their interfaces connected to CEs, and configure ESIs for these interfaces. The E-Trunks use the default encryption mode **enhanced-hmac-sha256** for authentication.
6. Configure a source address on each PE.
7. Configure a BGP EVPN peer relationship between each PE and its neighboring PE.
8. Set a redundancy mode per ESI instance on each PE.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance names: evrf1 and evrf2
* RDs of evrf1 and evrf2: 10:1, 20:1, 10:2, 20:2, 10:3, and 20:3; RTs of evrf1 and evrf2: 11:1 and 22:2

#### Procedure

1. Assign an IP address to each PE interface, including the loopback interfaces.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370606__file1).
2. Configure a routing protocol on each PE to ensure Layer 3 communication. OSPF is used in this example.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370606__file1).
3. Configure MPLS LDP on each PE.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370606__file1).
4. Create a BD EVPN instance and a BD on each PE, and bind the BD to the EVPN instance.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 10:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 11:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] evpn vpn-instance evrf2 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf2] route-distinguisher 20:1
   ```
   ```
   [*PE1-evpn-instance-evrf2] vpn-target 22:2
   ```
   ```
   [*PE1-evpn-instance-evrf2] quit
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] bridge-domain 20
   ```
   ```
   [*PE1-bd20] evpn binding vpn-instance evrf2
   ```
   ```
   [*PE1-bd20] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370606__file1).
5. Configure PE interfaces connected to CEs and configure an ESI for each interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are not advised to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] lacp e-trunk system-id 00e0-fc00-0000
   ```
   ```
   [*PE1] e-trunk 1
   ```
   ```
   [*PE1-e-trunk-1] priority 10
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
   [*PE1] e-trunk 2
   ```
   ```
   [*PE1-e-trunk-2] priority 10
   ```
   ```
   [*PE1-e-trunk-2] peer-address 2.2.2.2 source-address 1.1.1.1
   ```
   ```
   [*PE1-e-trunk-2] security-key cipher YsHsjx_202207
   ```
   ```
   [*PE1-e-trunk-2] quit
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
   [*PE1-Eth-Trunk10] quit
   ```
   ```
   [*PE1] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE1-Eth-Trunk10.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE1-Eth-Trunk10.1] rewrite pop single
   ```
   ```
   [*PE1-Eth-Trunk10.1] bridge-domain 10
   ```
   ```
   [*PE1-Eth-Trunk10.1] quit
   ```
   ```
   [*PE1] interface eth-trunk 20
   ```
   ```
   [*PE1-Eth-Trunk20] mode lacp-static
   ```
   ```
   [*PE1-Eth-Trunk20] e-trunk 2
   ```
   ```
   [*PE1-Eth-Trunk20] esi 0001.0002.0003.0004.0005
   ```
   ```
   [*PE1-Eth-Trunk20] quit
   ```
   ```
   [*PE1] interface eth-trunk 20.1 mode l2
   ```
   ```
   [*PE1-Eth-Trunk20.1] encapsulation dot1q vid 20
   ```
   ```
   [*PE1-Eth-Trunk20.1] rewrite pop single
   ```
   ```
   [*PE1-Eth-Trunk20.1] bridge-domain 20
   ```
   ```
   [*PE1-Eth-Trunk20.1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] eth-trunk 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/4
   ```
   ```
   [*PE1-GigabitEthernet0/1/4] eth-trunk 20
   ```
   ```
   [*PE1-GigabitEthernet0/1/4] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] lacp e-trunk system-id 00e0-fc00-0000
   ```
   ```
   [*PE2] e-trunk 1
   ```
   ```
   [*PE2-e-trunk-1] priority 20
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
   [*PE2] e-trunk 2
   ```
   ```
   [*PE2-e-trunk-2] priority 20
   ```
   ```
   [*PE2-e-trunk-2] peer-address 1.1.1.1 source-address 2.2.2.2
   ```
   ```
   [*PE2-e-trunk-2] security-key cipher YsHsjx_202207
   ```
   ```
   [*PE2-e-trunk-2] quit
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
   [*PE2-Eth-Trunk10] quit
   ```
   ```
   [*PE2] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE2-Eth-Trunk10.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE2-Eth-Trunk10.1] rewrite pop single
   ```
   ```
   [*PE2-Eth-Trunk10.1] bridge-domain 10
   ```
   ```
   [*PE2-Eth-Trunk10.1] quit
   ```
   ```
   [*PE2] interface eth-trunk 20
   ```
   ```
   [*PE2-Eth-Trunk20] mode lacp-static
   ```
   ```
   [*PE2-Eth-Trunk20] e-trunk 2
   ```
   ```
   [*PE2-Eth-Trunk20] esi 0001.0002.0003.0004.0005
   ```
   ```
   [*PE2-Eth-Trunk20] quit
   ```
   ```
   [*PE2] interface eth-trunk 20.1 mode l2
   ```
   ```
   [*PE2-Eth-Trunk20.1] encapsulation dot1q vid 20
   ```
   ```
   [*PE2-Eth-Trunk20.1] rewrite pop single
   ```
   ```
   [*PE2-Eth-Trunk20.1] bridge-domain 20
   ```
   ```
   [*PE2-Eth-Trunk20.1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] eth-trunk 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/4
   ```
   ```
   [*PE2-GigabitEthernet0/1/4] eth-trunk 20
   ```
   ```
   [*PE2-GigabitEthernet0/1/4] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface gigabitethernet 0/3/0.1 mode l2
   ```
   ```
   [*PE3-GigabitEthernet0/1/1.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE3-GigabitEthernet0/1/1.1] rewrite pop single
   ```
   ```
   [*PE3-GigabitEthernet0/1/1.1] bridge-domain 10
   ```
   ```
   [*PE3-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/3/0.2 mode l2
   ```
   ```
   [*PE3-GigabitEthernet0/1/1.2] encapsulation dot1q vid 20
   ```
   ```
   [*PE3-GigabitEthernet0/1/1.2] rewrite pop single
   ```
   ```
   [*PE3-GigabitEthernet0/1/1.2] bridge-domain 20
   ```
   ```
   [*PE3-GigabitEthernet0/1/1.2] quit
   ```
   ```
   [*PE3] commit
   ```
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370606__file1).
6. Configure a source address on each PE.
   
   
   
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
   [~PE3] evpn source-address 3.3.3.3
   ```
   ```
   [*PE3] commit
   ```
7. Establish a BGP EVPN peer relationship between each PE and its neighboring PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.3 enable
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
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370606__file1).
8. Set a redundancy mode per ESI instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn
   ```
   ```
   [*PE1-evpn] esi 0001.0002.0003.0004.0005
   ```
   ```
   [*PE1-evpn-esi-0001.0002.0003.0004.0005] evpn redundancy-mode single-active
   ```
   ```
   [*PE1-evpn-esi-0001.0002.0003.0004.0005] quit
   ```
   ```
   [*PE1-evpn] esi 0000.1111.2222.1111.1111
   ```
   ```
   [*PE1-evpn-esi-0000.1111.2222.1111.1111] evpn redundancy-mode all-active
   ```
   ```
   [*PE1-evpn-esi-0000.1111.2222.1111.1111] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration of PE2 is similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370606__file1).
9. Configuring CEs to Access PEs
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] vlan 10
   [*CE1-vlan10] quit
   [*CE1] interface vlanif10
   [*CE1-Vlanif10] ip address 192.168.1.11 24
   [*CE1-Vlanif10] quit
   [*CE1] interface eth-trunk10
   [*CE1-Eth-Trunk10] portswitch
   [*CE1-Eth-Trunk10] port link-type trunk
   [*CE1-Eth-Trunk10] port trunk allow-pass vlan 10
   [*CE1-Eth-Trunk10] mode lacp-static
   [*CE1-Eth-Trunk10] quit
   [*CE1] interface gigabitethernet0/1/1
   [*CE1-GigabitEthernet0/1/1] eth-trunk 10
   [*CE1-GigabitEthernet0/1/1] quit
   [*CE1] interface gigabitethernet0/1/2
   [*CE1-GigabitEthernet0/1/2] eth-trunk 10
   [*CE1-GigabitEthernet0/1/2] quit
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] vlan 20
   [*CE2-vlan20] quit
   [*CE2] interface vlanif20
   [*CE2-Vlanif20] ip address 192.168.2.11 24
   [*CE2-Vlanif20] quit
   [*CE2] interface eth-trunk20
   [*CE2-Eth-Trunk20] portswitch
   [*CE2-Eth-Trunk20] port link-type trunk
   [*CE2-Eth-Trunk20] port trunk allow-pass vlan 20
   [*CE2-Eth-Trunk20] mode lacp-static
   [*CE2-Eth-Trunk20] lacp preempt enable
   [*CE2-Eth-Trunk20] max active-linknumber 1
   [*CE2-Eth-Trunk20] lacp preempt delay 180
   [*CE2-Eth-Trunk20] quit
   [*CE2] interface gigabitethernet0/1/1
   [*CE2-GigabitEthernet0/1/1] eth-trunk 20
   [*CE2-GigabitEthernet0/1/1] quit
   [*CE2] interface gigabitethernet0/1/2
   [*CE2-GigabitEthernet0/1/2] eth-trunk 20
   [*CE2-GigabitEthernet0/1/2] quit
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] vlan 10
   [*CE3-vlan10] quit
   [*CE3] vlan 20
   [*CE3-vlan20] quit
   [*CE3] interface vlanif10
   [*CE3-Vlanif10] ip address 192.168.1.12 24
   [*CE3-Vlanif10] quit
   [*CE3] interface vlanif20
   [*CE3-Vlanif20] ip address 192.168.2.12 24
   [*CE3-Vlanif20] quit
   [*CE3] interface gigabitethernet0/1/1
   [*CE3-GigabitEthernet0/1/1] portswitch
   [*CE3-GigabitEthernet0/1/1] port link-type trunk
   [*CE3-GigabitEthernet0/1/1] port trunk allow-pass vlan 10 20
   [*CE3-GigabitEthernet0/1/1] quit
   [*CE3] commit
   ```
10. Verify the configuration.
    
    
    
    Run the **display bgp evpn all esi** command on PE1. The command output shows ESI information of the two EVPN instances and the redundancy modes of the ESI instances.
    
    ```
    [~PE1] display bgp evpn all esi
    ```
    ```
    Number of ESI for EVPN address family: 2
    
     ESI                           IFName/Bridge-domain/PW    Redundancy-Mode    
     0000.1111.2222.1111.1111      Eth-Trunk10.1                   all-active
     0001.0002.0003.0004.0005      Eth-Trunk20.1                   single-active                 
    
    Number of ESI for evpn-instance evrf1: 1
    
     ESI                           IFName/Bridge-domain/PW    Redundancy-Mode    
     0000.1111.2222.1111.1111      Eth-Trunk10.1                   all-active          
    
    Number of ESI for evpn-instance evrf2: 1
    
     ESI                           IFName/Bridge-domain/PW    Redundancy-Mode    
     0001.0002.0003.0004.0005      Eth-Trunk20.1                   single-active 
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  lacp e-trunk system-id 00e0-fc00-0000
  #
  evpn
   #
   mac-duplication
   #
   esi 0000.1111.2222.1111.1111
    evpn redundancy-mode all-active
   #
   esi 0001.0002.0003.0004.0005
    evpn redundancy-mode single-active
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 20:1
   vpn-target 22:2 export-extcommunity
   vpn-target 22:2 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  mpls ldp
  #
  e-trunk 1
   priority 10
   peer-address 2.2.2.2 source-address 1.1.1.1
   security-key cipher %^%#VQE;E!Dl&Rr]if$F>}w9uk5C>y-4|MS$unQ!#Mb#%^%#
   authentication-mode enhanced-hmac-sha256
  #
  e-trunk 2
   priority 10
   peer-address 2.2.2.2 source-address 1.1.1.1
   security-key cipher %^%#F&zi0c6x_2+SrLT_nm4,vfS$SCd]G:r~A_T!C>A$%^%#
   authentication-mode enhanced-hmac-sha256
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.1111.2222.1111.1111
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk20
   mode lacp-static
   e-trunk 2
   esi 0001.0002.0003.0004.0005
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   eth-trunk 20
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
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
  #
  evpn
   #
   mac-duplication
   #
   esi 0000.1111.2222.1111.1111
    evpn redundancy-mode all-active
   #
   esi 0001.0002.0003.0004.0005
    evpn redundancy-mode single-active
  #               
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:2
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 20:2
   vpn-target 22:2 export-extcommunity
   vpn-target 22:2 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #               
  mpls ldp
  #
  e-trunk 1
   priority 20
   peer-address 1.1.1.1 source-address 2.2.2.2
   security-key cipher %^%#!8C!"bAoc~O}UW2)%$HP4%.G9179.;&Yr[GmV.PN%^%#
   authentication-mode enhanced-hmac-sha256
  #
  e-trunk 2
   priority 20
   peer-address 1.1.1.1 source-address 2.2.2.2
   security-key cipher %^%#GAG\Y-F%GY[GnwCkov7A<e(m/cl}m86`jd6z[79~%^%#
   authentication-mode enhanced-hmac-sha256
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.1111.2222.1111.1111
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #               
  interface Eth-Trunk20
   mode lacp-static
   e-trunk 2
   esi 0001.0002.0003.0004.0005
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 20
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   eth-trunk 10
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
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
   route-distinguisher 10:3
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 20:3
   vpn-target 22:2 export-extcommunity
   vpn-target 22:2 import-extcommunity
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls           
   mpls ldp
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/3/0.2 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  evpn source-address 3.3.3.3
  #
  return
  ```
* CE1 configuration file
  ```
  #
  sysname CE1
  #
  vlan batch 10
  #
  vlan 10
  #
  interface Vlanif10
   ip address 192.168.1.11 255.255.255.0
  #
  interface Eth-Trunk10
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10
   mode lacp-static
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 10
  #
  return
  ```
* CE2 configuration file
  ```
  #
  sysname CE2
  #
  vlan batch 20
  #
  vlan 20
  #
  interface Vlanif20
   ip address 192.168.2.11 255.255.255.0
  #
  interface Eth-Trunk20
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 20
   mode lacp-static
   lacp preempt enable
   max active-linknumber 1
   lacp preempt delay 180
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 20
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 20
  #
  return
  ```
* CE3 configuration file
  ```
  #
  sysname CE3
  #
  vlan batch 10 20
  #
  vlan 10
  #
  vlan 20
  #
  interface Vlanif10
   ip address 192.168.1.12 255.255.255.0
  #
  interface Vlanif20
   ip address 192.168.2.12 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 20
  #
  return
  ```