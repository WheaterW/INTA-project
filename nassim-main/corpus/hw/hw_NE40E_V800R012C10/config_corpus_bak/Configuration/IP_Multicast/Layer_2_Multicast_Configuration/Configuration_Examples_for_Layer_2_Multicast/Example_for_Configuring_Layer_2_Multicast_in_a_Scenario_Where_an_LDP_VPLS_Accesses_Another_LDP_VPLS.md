Example for Configuring Layer 2 Multicast in a Scenario Where an LDP VPLS Accesses Another LDP VPLS
===================================================================================================

This section provides an example for configuring Layer 2 multicast in a scenario where an LDP VPLS accesses another LDP VPLS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176572068__fig_dc_vrp_l2mc_cfg_003401), UPEs and the NPE use LDP as the signaling protocol to establish VPLSs. Two virtual interfaces, VE0/2/0 and VE0/2/1, are created on the NPE. VE0/2/0 functions as an L2VE interface and is used for VPLS termination, whereas VE0/2/1 functions as an L3VE interface and is used for VPLS access.

**Figure 1** Configuring Layer 2 multicast in a scenario where an LDP VPLS accesses another LDP VPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 4 represent GE0/1/0, GE0/2/0, VE0/2/0, and VE0/2/1, respectively.


  
![](figure/en-us_image_0000001176735394.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an LDP VPLS, which involves the following operations:
   
   * Configure a routing protocol (OSPF in this example) on the UPEs and the NPE to implement communication at Layer 3.
   * Configure basic MPLS functions and MPLS LDP to establish MPLS LSPs.
   * Enable MPLS L2VPN, and enable L2VPN globally.
2. Create an L2VE interface and an L3VE interface on the NPE, and bind them to the same VE-Group.
3. Bind the L2VE interface to a VSI.
4. Configure the L3VE interface as a sub-interface for dot1q VLAN tag termination to access the L2VPN.
5. Enable Layer 2 multicast on the UPEs and the NPE.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface names, IP addresses, and OSPFv2 process ID
* VE-Group number
* LSR ID of each node
* VSI names and VSI IDs

#### Procedure

1. Assign an IP address to each interface and configure OSPF.
   
   
   
   Assign an IP address to each interface on UPE1, the NPE, and UPE2 according to [Figure 1](#EN-US_TASK_0000001176572068__fig_dc_vrp_l2mc_cfg_003401). Ensure that the 32-bit loopback addresses of UPE1, the NPE, and UPE2 are advertised during OSPF configuration. For configuration details, see Configuration Files in this section.
2. Configure basic MPLS functions and LDP on UPE1, the NPE, and UPE2.
   
   
   
   # Configure UPE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE1
   ```
   ```
   [*HUAWEI] commit
   ```
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
   [*UPE1] interface GigabitEthernet 0/1/0
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
   
   # Configure the NPE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname NPE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~NPE] mpls lsr-id 2.2.2.2
   ```
   ```
   [*NPE] mpls
   ```
   ```
   [*NPE-mpls] quit
   ```
   ```
   [*NPE] mpls ldp
   ```
   ```
   [*NPE-mpls-ldp] quit
   ```
   ```
   [*NPE] interface GigabitEthernet 0/1/0
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*NPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE] commit
   ```
   
   # Configure UPE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~UPE2] mpls lsr-id 3.3.3.3
   ```
   ```
   [*UPE2] mpls
   ```
   ```
   [*UPE2-mpls] quit
   ```
   ```
   [*UPE2] mpls ldp
   ```
   ```
   [*UPE2-mpls-ldp] quit
   ```
   ```
   [*UPE2] interface GigabitEthernet 0/1/0
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*UPE2] commit
   ```
3. Enable MPLS L2VPN and configure a VSI.
   
   
   
   # Configure UPE1.
   
   ```
   [~UPE1] mpls l2vpn
   ```
   ```
   [*UPE1-l2vpn] quit
   ```
   ```
   [*UPE1] vsi vsi1
   ```
   ```
   [*UPE1-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*UPE1-vsi-vsi1-ldp] vsi-id 100
   ```
   ```
   [*UPE1-vsi-vsi1-ldp] peer 2.2.2.2
   ```
   ```
   [*UPE1-vsi-vsi1-ldp] quit
   ```
   ```
   [*UPE1-vsi-vsi1] quit
   ```
   ```
   [*UPE1] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] mpls l2vpn
   ```
   ```
   [*NPE-l2vpn] quit
   ```
   ```
   [*NPE] vsi vsi1
   ```
   ```
   [*NPE-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*NPE-vsi-vsi1-ldp] vsi-id 100
   ```
   ```
   [*NPE-vsi-vsi1-ldp] peer 1.1.1.1
   ```
   ```
   [*NPE-vsi-vsi1-ldp] quit
   ```
   ```
   [*NPE-vsi-vsi1] quit
   ```
   ```
   [*NPE] vsi vsi2
   ```
   ```
   [*NPE-vsi-vsi2] pwsignal ldp
   ```
   ```
   [*NPE-vsi-vsi2-ldp] vsi-id 200
   ```
   ```
   [*NPE-vsi-vsi2-ldp] peer 3.3.3.3
   ```
   ```
   [*NPE-vsi-vsi2-ldp] quit
   ```
   ```
   [*NPE-vsi-vsi2] quit
   ```
   ```
   [*NPE] commit
   ```
   
   # Configure UPE2.
   
   ```
   [~UPE2] mpls l2vpn
   ```
   ```
   [*UPE2-l2vpn] quit
   ```
   ```
   [*UPE2] vsi vsi2
   ```
   ```
   [*UPE2-vsi-vsi2] pwsignal ldp
   ```
   ```
   [*UPE2-vsi-vsi2-ldp] vsi-id 200
   ```
   ```
   [*UPE2-vsi-vsi2-ldp] peer 2.2.2.2
   ```
   ```
   [*UPE2-vsi-vsi2-ldp] quit
   ```
   ```
   [*UPE2-vsi-vsi2] quit
   ```
   ```
   [*UPE2] commit
   ```
4. Configure GigabitEthernet0/2/0.1 sub-interfaces on UPE1 and UPE2 and bind each of the sub-interfaces to a VSI.
   
   
   
   # Configure UPE1.
   
   ```
   [~UPE1] interface GigabitEthernet 0/2/0.1
   ```
   ```
   [*UPE1-GigabitEthernet0/2/0.1] vlan-type dot1q 200
   ```
   ```
   [*UPE1-GigabitEthernet0/2/0.1] l2 binding vsi vsi1
   ```
   ```
   [*UPE1-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*UPE1] commit
   ```
   
   # Configure UPE2.
   
   ```
   [~UPE2] interface GigabitEthernet 0/2/0.1
   ```
   ```
   [*UPE2-GigabitEthernet0/2/0.1] vlan-type dot1q 200
   ```
   ```
   [*UPE2-GigabitEthernet0/2/0.1] l2 binding vsi vsi2
   ```
   ```
   [*UPE2-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*UPE2] commit
   ```
5. Create two VE interfaces on the NPE, and bind them to the same VE-Group.
   
   
   
   # Create VE0/2/0 for MPLS L2VPN termination.
   
   ```
   [~NPE] interface Virtual-Ethernet 0/2/0
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0] ve-group 1 l2-terminate
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0] quit
   ```
   ```
   [~NPE] interface Virtual-Ethernet 0/2/0.1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0.1] vlan-type dot1q 200
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0.1] l2 binding vsi vsi2
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/0.1] quit
   ```
   ```
   [*NPE] commit
   ```
   
   # Create VE0/2/1 for MPLS L2VPN access.
   
   ```
   [~NPE] interface Virtual-Ethernet 0/2/1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1] ve-group 1 l3-access
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1] quit
   ```
   ```
   [~NPE] interface Virtual-Ethernet 0/2/1.1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1.1] vlan-type dot1q 200
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1.1] l2 binding vsi vsi1
   ```
   ```
   [*NPE-Virtual-Ethernet0/2/1.1] quit
   ```
   ```
   [*NPE] commit
   ```
6. Enable Layer 2 multicast.
   
   
   
   # Configure UPE1.
   
   ```
   [~UPE1] igmp-snooping enable
   ```
   ```
   [*UPE1] vsi vsi1
   ```
   ```
   [*UPE1-vsi-vsi1] igmp-snooping enable
   ```
   ```
   [*UPE1-vsi-vsi1] quit
   ```
   ```
   [*UPE1] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] igmp-snooping enable
   ```
   ```
   [*NPE] vsi vsi1
   ```
   ```
   [*NPE-vsi-vsi1] igmp-snooping enable
   ```
   ```
   [*NPE-vsi-vsi1] quit
   ```
   ```
   [*NPE] vsi vsi2
   ```
   ```
   [*NPE-vsi-vsi2] igmp-snooping enable
   ```
   ```
   [*NPE-vsi-vsi2] quit
   ```
   ```
   [*NPE] commit
   ```
   
   # Configure UPE2.
   
   ```
   [~UPE2] igmp-snooping enable
   ```
   ```
   [*UPE2] vsi vsi2
   ```
   ```
   [*UPE2-vsi-vsi2] igmp-snooping enable
   ```
   ```
   [*UPE2-vsi-vsi2] igmp-snooping proxy
   ```
   ```
   [*UPE2-vsi-vsi2] quit
   ```
   ```
   [*UPE2] commit
   ```
7. Verify the configuration.
   
   # Run the [**display igmp-snooping port-info**](cmdqueryname=display+igmp-snooping+port-info) command on the NPE to check information about multicast ports.
   ```
   [~NPE] display igmp-snooping port-info 
    -----------------------------------------------------------------------------------
     Flag: S:Static     D:Dynamic     M:Ssm-mapping
           A:Active     P:Protocol    F:Fast-channel
                        (Source, Group)  Port                                      Flag
    -----------------------------------------------------------------------------------
    VSI vsi1, 1 Entry(s)
                         (*, 225.1.0.1)                                            PA-
                                         PW(1.1.1.1/100)                           -D-
                                                           1 port(s) include
    VSI vsi2, 1 Entry(s)
                         (*, 225.1.0.1)                                            PA-
                                         VE0/2/0.1                                 -D-
                                                           1 port(s) include
   ```
   
   # Run the [**display igmp-snooping router-port**](cmdqueryname=display+igmp-snooping+router-port) command on the NPE to check information about router ports.
   ```
   [~NPE] display igmp-snooping router-port 
    -------------------------------------------------------------------------------
    Port Name                                 UpTime        Expires       Flags
    -------------------------------------------------------------------------------
    VSI vsi1, 1 router-port(s)
    VE0/2/1.1                                 00:53:26      00:02:21      DYNAMIC
   
    VSI vsi2, 1 router-port(s)
    PW(3.3.3.3/200)                           00:49:38      00:02:21      DYNAMIC
   ```

#### Configuration Files

* UPE1 configuration file
  
  ```
  #
  sysname UPE1
  #
  igmp-snooping enable
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1
   pwsignal ldp
    vsi-id 100
    peer 2.2.2.2
   igmp-snooping enable
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 200
   l2 binding vsi vsi1
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* NPE configuration file
  
  ```
  #
  sysname NPE
  #
  igmp-snooping enable
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1
   pwsignal ldp
    vsi-id 100
    peer 1.1.1.1
   igmp-snooping enable
  #
  vsi vsi2
   pwsignal ldp
    vsi-id 200
    peer 3.3.3.3
   igmp-snooping enable
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface Virtual-Ethernet0/2/0
   ve-group 1 l2-terminate
  #
  interface Virtual-Ethernet0/2/0.1
   vlan-type dot1q 200
   l2 binding vsi vsi2
  #
  interface Virtual-Ethernet0/2/1
   ve-group 1 l3-access
  #
  interface Virtual-Ethernet0/2/1.1
   vlan-type dot1q 200
   l2 binding vsi vsi1
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* UPE2 configuration file
  ```
  #
  sysname UPE2
  #
  igmp-snooping enable
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi2
   pwsignal ldp
    vsi-id 200
    peer 2.2.2.2
   igmp-snooping enable
   igmp-snooping proxy
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0 
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 200
   l2 binding vsi vsi2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  return
  ```