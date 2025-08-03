Example for Configuring Inter-VLAN Proxy ND on an L2VPN+L3VPN IP RAN
====================================================================

This section provides an example for configuring inter-VLAN proxy ND on an L2VPN+L3VPN IP RAN.

#### Networking Requirements

If hosts are on the same network segment and physical network but belong to different VLANs, inter-VLAN proxy ND must be enabled on the associated VLAN interfaces to enable Layer 3 interworking between the hosts.

On the L2VPN+L3VPN IP RAN shown in [Figure 1](#EN-US_TASK_0172365204__fig_dc_vrp_nd_feature_002903), the CSGs are connected to the ASG through L2VE sub-interfaces, and the ASG terminates L2VPN packets and is connected to the BGP/MPLS IPv6 VPN through an L3VE sub-interface. CSG1 and CSG2 belong to VLAN 1000 and VLAN 1100, respectively. HostA and HostB connected to the CSGs are on the same network segment but in different VLANs. Therefore, HostA and HostB cannot ping each other. To address this problem, enable inter-VLAN proxy ND on the L3VE sub-interface of the ASG.**Figure 1** Networking of inter-VLAN proxy ND on an L2VPN+L3VPN IP RAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_nd_feature_003716.png)

| Device Name | Interface Name | Interface Address |
| --- | --- | --- |
| CSG1 | GE0/1/1 | 192.168.2.2/24 |
| GE0/1/2 | - |
| Loopback0 | 3.3.3.3/32 |
| CSG2 | GE0/1/1 | - |
| GE0/1/2 | 192.168.1.2/24 |
| Loopback0 | 2.2.2.2/32 |
| ASG | GE0/1/1 | 192.168.2.1/24 |
| GE0/1/2 | 192.168.1.1/24 |
| Loopback0 | 1.1.1.1/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to interfaces.
2. On the ASG, create an L2VE interface for VPWS termination and an L3VE interface for L3VPN access and bind the two VE interfaces to a VE-group.
3. Configure VPWS in LDP mode. Details are as follows:
   1. Configure a routing protocol to ensure that devices can communicate.
   2. Configure basic MPLS functions and LDP.
   3. Enable MPLS L2VPN and create VCs.
4. Configure a dot1q VLAN tag termination sub-interface on the ASG and enable inter-VLAN proxy ND.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface addresses
* IS-IS process ID
* LSR ID

#### Procedure

1. Assign IP addresses to interfaces.
   
   
   
   Assign IP addresses to all physical interfaces and loopback interfaces according to [Figure 1](#EN-US_TASK_0172365204__fig_dc_vrp_nd_feature_002903). For configuration details, see [Configuration Files](#EN-US_TASK_0172365204__file1) in this section.
2. Create VE 0/2/0 and VE 0/2/1 on the ASG and bind the VE interfaces to the same VE-group.
   
   
   
   # Create VE 0/2/0 for MPLS L2VPN termination.
   
   ```
   [~ASG] interface virtual-ethernet0/2/0
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/0] ve-group 1 l2-terminate
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/0] quit
   ```
   
   # Create VE 0/2/1 for MPLS L3VPN access.
   
   ```
   [*ASG] interface virtual-ethernet0/2/1
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1] ve-group 1 l3-access
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1] quit
   ```
   ```
   [*ASG] commit
   ```
   
   # After completing the configurations, run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) command on the ASG to view the binding relationship between the VE interfaces and VE-group.
   
   ```
   [~ASG] display virtual-ethernet ve-group
   ```
   ```
    Ve-groupID    TerminateVE                   AccessVE
    1             Virtual-Ethernet0/2/0         Virtual-Ethernet0/2/1
   Total 1, 1 printed
   ```
3. Configure an IGP to allow device communication. IS-IS is used in this example.
   
   
   
   During IS-IS configuration, ensure that the routes destined for the 32-bit loopback addresses of the ASG and CSGs are advertised.
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172365204__file1) in this section.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised not to use weak security algorithms in the IS-IS feature. If you need to use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function first.
4. Configure basic MPLS functions and LDP.
   
   
   
   # Configure CSG1.
   
   ```
   [~CSG1] mpls lsr-id 3.3.3.3
   ```
   ```
   [*CSG1] mpls
   ```
   ```
   [*CSG1-mpls] quit
   ```
   ```
   [*CSG1] mpls ldp
   ```
   ```
   [*CSG1-mpls-ldp] quit
   ```
   ```
   [*CSG1] interface gigabitethernet 0/1/1
   ```
   ```
   [*CSG1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CSG1-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*CSG1-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*CSG1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CSG1] commit
   ```
   
   # Configure CSG2.
   
   ```
   [~CSG2] mpls lsr-id 2.2.2.2
   ```
   ```
   [*CSG2] mpls
   ```
   ```
   [*CSG2-mpls] quit
   ```
   ```
   [*CSG2] mpls ldp
   ```
   ```
   [*CSG2-mpls-ldp] quit
   ```
   ```
   [*CSG2] interface gigabitethernet 0/1/2
   ```
   ```
   [*CSG2-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CSG2-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*CSG2-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*CSG2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CSG2] commit
   ```
   
   # Configure the ASG.
   
   ```
   [~ASG] mpls lsr-id 1.1.1.1
   ```
   ```
   [*ASG] mpls
   ```
   ```
   [*ASG-mpls] quit
   ```
   ```
   [*ASG] mpls ldp
   ```
   ```
   [*ASG-mpls-ldp] quit
   ```
   ```
   [*ASG] interface gigabitethernet 0/1/1
   ```
   ```
   [*ASG-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*ASG-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*ASG-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*ASG-GigabitEthernet0/1/1] quit
   ```
   ```
   [*ASG] interface gigabitethernet 0/1/2
   ```
   ```
   [*ASG-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*ASG-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*ASG-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*ASG-GigabitEthernet0/1/2] quit
   ```
   ```
   [*ASG] commit
   ```
5. Enable MPLS L2VPN and create VCs.
   
   
   
   # Configure CSG1.
   
   ```
   [~CSG1] mpls l2vpn
   ```
   ```
   [*CSG1-l2vpn] quit
   ```
   ```
   [*CSG1] interface gigabitethernet 0/1/2.1
   ```
   ```
   [*CSG1-GigabitEthernet0/1/2.1] undo shutdown
   ```
   ```
   [*CSG1-GigabitEthernet0/1/2.1] vlan-type dot1q 1000
   ```
   ```
   [*CSG1-GigabitEthernet0/1/2.1] mpls l2vc 1.1.1.1 1
   ```
   ```
   [*CSG1-GigabitEthernet0/1/2.1] quit
   ```
   ```
   [*CSG1] commit
   ```
   
   # Configure CSG2.
   
   ```
   [~CSG2] mpls l2vpn
   ```
   ```
   [*CSG2-l2vpn] quit
   ```
   ```
   [*CSG2] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*CSG2-GigabitEthernet0/1/1.1] undo shutdown
   ```
   ```
   [*CSG2-GigabitEthernet0/1/1.1] vlan-type dot1q 1100
   ```
   ```
   [*CSG2-GigabitEthernet0/1/1.1] mpls l2vc 1.1.1.1 1
   ```
   ```
   [*CSG2-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*CSG2] commit
   ```
   
   # Configure the ASG.
   
   ```
   [~ASG] mpls l2vpn
   ```
   ```
   [*ASG-l2vpn] quit
   ```
   ```
   [*ASG] interface virtual-ethernet0/2/0.1
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/0.1] vlan-type dot1q 1000
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/0.1] mpls l2vc 3.3.3.3 1
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/0.1] quit
   ```
   ```
   [*ASG] interface virtual-ethernet0/2/0.2
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/0.2] vlan-type dot1q 1100
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/0.2] mpls l2vc 2.2.2.2 1
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/0.2] quit
   ```
   ```
   [*ASG] commit
   ```
6. Configure a dot1q VLAN tag termination sub-interface on the ASG and enable inter-VLAN proxy ND.
   
   
   ```
   [~ASG] interface virtual-ethernet0/2/1.1
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1.1] ipv6 enable
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1.1] ipv6 address 2001:db8:300:400::3 64
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1.1] encapsulation dot1q-termination
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1.1] dot1q termination vid 1000 to 1100
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1.1] ipv6 nd ns multicast-enable
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1.1] ipv6 nd proxy inter-access-vlan enable
   ```
   ```
   [*ASG-Virtual-Ethernet0/2/1.1] quit
   ```
   ```
   [*ASG] commit
   ```
7. Configure the IPv6 addresses of hosts.
   
   
   
   # Configure the IPv6 address of HostA as 2001:db8:300:400::1/64.
   
   # Configure the IPv6 address of HostB as 2001:db8:300:400::2/64.
8. Verifying the configuration.
   
   
   
   After the configurations are complete, HostA and HostB can ping each other.

#### Configuration Files

* CSG1 configuration file
  
  ```
  #
  sysname CSG1
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0000.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1
   vlan-type dot1q 1000
   mpls l2vc 1.1.1.1 1
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  return
  
  ```
* CSG2 configuration file
  
  ```
  #
  sysname CSG2
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0001.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 1100
   mpls l2vc 1.1.1.1 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  return
  
  ```
* ASG configuration file
  
  ```
  #
  sysname ASG
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0002.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  interface Virtual-Ethernet0/2/0
   ve-group 1 l2-terminate
  #
  interface Virtual-Ethernet0/2/0.1
   vlan-type dot1q 1000
   mpls l2vc 3.3.3.3 1
  #
  interface Virtual-Ethernet0/2/0.2
   vlan-type dot1q 1100
   mpls l2vc 2.2.2.2 1
  #
  interface Virtual-Ethernet0/2/1 
   ve-group 1 l3-access
  #
  interface Virtual-Ethernet0/2/1.1
   ipv6 enable
   ipv6 address 2001:db8:300:400::3/64
   encapsulation dot1q-termination
   dot1q termination vid 1000 to 1100
   ipv6 nd ns multicast-enable
   ipv6 nd proxy inter-access-vlan enable
  #
  return
  
  ```