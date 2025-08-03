Example for Configuring Dual-Device IGMP Snooping Hot Backup for a VSI
======================================================================

This section provides an example for configuring dual-device IGMP snooping hot backup for a VSI in a master/backup E-Trunk scenario. After dual-device IGMP snooping hot backup is configured, multicast services are not interrupted during a master/backup E-Trunk switchover.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172362262__fig125654388184), configure an E-Trunk on Device A and Device B. Device A is the master device, and Device B is the backup device. In normal situations, the link between Device A and Device C is up, and the link between Device B and Device C is down. Device C sends packets to Device A through the link in the up state to establish IGMP snooping entries. After receiving the packets, Device A backs up the packets to Device B through the RBS channel. If Device A or the link between Device A and Device C fails, a master/backup E-Trunk switchover is performed and the link between Device B and Device C goes up. Device C sends packets to Device B through the link, ensuring IGMP snooping service continuity.

**Figure 1** Configuring dual-device IGMP snooping hot backup in a master/backup E-Trunk scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example are GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001867209549.png)

To ensure that IGMP snooping services are not interrupted during a master/backup E-Trunk switchover, configure dual-device IGMP snooping hot backup on Device A and Device B to ensure Device A to back up IGMP Snooping entries to Device B in real time. After the configuration is complete, Device B synchronizes IGMP snooping entries from Device A in real time.

#### 



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for loopback interfaces on the master and backup devices, configure IP addresses for the two ends of the RBS channel, and configure a routing protocol to ensure network-layer route reachability.
2. Configure an E-Trunk on Device A and Device B.
3. Establish a dual-device backup platform on Device A and Device B.
4. Create BFD sessions and bind them to E-Trunk on Device A and Device B.
5. Enable remote backup for IGMP snooping services on Device A and Device B.
6. Establish VPLS Layer 2 multicast services between Device A and Device D, and between Device B and Device D.

#### Data Preparation

To complete the configuration, you need the following data:

* Eth-Trunk 1 with Ethernet member interfaces on Device A, Device B, and Device C
* Eth-Trunk 1 in E-Trunk 1 on Device A and Device B
* TCP connection parameters for the remote backup service: Device A's loopback1 interface IP address (1.1.1.1/32), Device B's loopback1 interface IP address (2.2.2.2/32), and TCP port number (1025)
* Device A's IP address: 10.0.0.1/24; Device B's IP address: 10.0.0.2/24
* RBS name: service1; RBP name: profile1; backup ID: 10
* VPLS network established between Device A and Device D, and between Device B and Device D; IP address of Loopback1 on Device D: 3.3.3.3/32

#### Procedure

1. Assign an IP address to each interface on Device A, Device B, and Device D. Then, configure OSPF to ensure that the devices can communicate with each other. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172362262__section_dc_vrp_rbs_cfg_001108).
2. Add Ethernet interfaces on Device A and Device B to Eth-Trunk 1, and add Eth-Trunk 1 to E-Trunk 1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172362262__section_dc_vrp_rbs_cfg_001108).
3. Add the interfaces for connecting Device C to Device A and Device B to Eth-Trunk 1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172362262__section_dc_vrp_rbs_cfg_001108).
4. Configure an RBS.
   
   # Configure an RBS on Device A.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*DeviceA] remote-backup-service service1
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] peer 2.2.2.2 source 1.1.1.1 port 1025
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] commit
   ```
   ```
   [~DeviceA-rm-backup-srv-service1] quit
   ```
   
   # Configure an RBS on Device B.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*DeviceB] remote-backup-service service1
   ```
   ```
   [*DeviceB-rm-backup-srv-service1] peer 1.1.1.1 source 2.2.2.2 port 1025
   ```
   ```
   [*DeviceB-rm-backup-srv-service1] commit
   ```
   ```
   [~DeviceB-rm-backup-srv-service1] quit
   ```
5. Configure an RBP.
   
   # Configure an RBP on Device A.
   ```
   [~DeviceA] remote-backup-profile profile1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] backup-id 10 remote-backup-service service1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceA-rm-backup-prf-profile1] quit
   ```
   
   # Configure an RBP on Device B.
   ```
   [~DeviceB] remote-backup-profile profile1
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] backup-id 10 remote-backup-service service1
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceB-rm-backup-prf-profile1] quit
   ```
6. Configure basic MPLS functions and LDP, enable MPLS L2VPN, and configure a VSI.
   
   
   
   # Configure a VSI on Device A and enable IGMP snooping for the VSI.
   
   ```
   [~DeviceA] mpls lsr-id 1.1.1.1
   ```
   ```
   [*DeviceA] mpls
   ```
   ```
   [*DeviceA-mpls] quit
   ```
   ```
   [*DeviceA] mpls ldp
   ```
   ```
   [*DeviceA-mpls-ldp] quit
   ```
   ```
   [*DeviceA] mpls l2vpn
   ```
   ```
   [*DeviceA-l2vpn] quit
   ```
   ```
   [*DeviceA] vsi v123
   ```
   ```
   [*DeviceA-vsi-v123] pwsignal ldp
   ```
   ```
   [*DeviceA-vsi-v123-ldp] vsi-id 123
   ```
   ```
   [*DeviceA-vsi-v123-ldp] peer 3.3.3.3
   ```
   ```
   [*DeviceA-vsi-v123-ldp] quit
   ```
   ```
   [*DeviceA-vsi-v123] ignore-ac-state
   ```
   ```
   [*DeviceA-vsi-v123] igmp-snooping enable
   ```
   ```
   [*DeviceA-vsi-v123] igmp-snooping proxy
   ```
   ```
   [*DeviceA-vsi-v123] commit
   ```
   ```
   [~DeviceA-vsi-v123] quit
   ```
   ```
   [~DeviceA] interface GigabitEthernet0/3/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] ip address 10.2.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] mpls ldp
   ```
   
   # Configure a VSI on Device B and enable IGMP snooping for the VSI.
   
   ```
   [~DeviceB] mpls lsr-id 2.2.2.2
   ```
   ```
   [*DeviceB] mpls
   ```
   ```
   [*DeviceB-mpls] quit
   ```
   ```
   [*DeviceB] mpls ldp
   ```
   ```
   [*DeviceB-mpls-ldp] quit
   ```
   ```
   [*DeviceB] mpls l2vpn
   ```
   ```
   [*DeviceB-l2vpn] quit
   ```
   ```
   [*DeviceB] vsi v123
   ```
   ```
   [*DeviceB-vsi-v123] pwsignal ldp
   ```
   ```
   [*DeviceB-vsi-v123-ldp] vsi-id 123
   ```
   ```
   [*DeviceB-vsi-v123-ldp] peer 3.3.3.3
   ```
   ```
   [*DeviceA-vsi-v123-ldp] quit
   ```
   ```
   [*DeviceB-vsi-v123] ignore-ac-state
   ```
   ```
   [*DeviceB-vsi-v123] igmp-snooping enable
   ```
   ```
   [*DeviceB-vsi-v123] igmp-snooping proxy
   ```
   ```
   [*DeviceB-vsi-v123] commit
   ```
   ```
   [~DeviceB-vsi-v123] quit
   ```
   ```
   [~DeviceB] interface GigabitEthernet0/3/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] ip address 10.3.1.1 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] commit
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] quit
   ```
7. Configure a VLAN.
   
   
   
   # Configure a VLAN on Device A.
   
   ```
   [~DeviceA] vlan 1
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a VLAN on Device B.
   
   
   
   ```
   [~DeviceB] vlan 1
   ```
   ```
   [*DeviceB] commit
   ```
8. Configure a dual-device E-Trunk backup platform.
   
   
   
   # Configure a dual-device E-Trunk 1 backup platform on Device A.
   
   1. # Configure E-Trunk 1 on Device A.
      ```
      [~DeviceA] e-trunk 1
      ```
      ```
      [*DeviceA-e-trunk-1] priority 20
      ```
      ```
      [*DeviceA-e-trunk-1] peer-address 2.2.2.2 source-address 1.1.1.1
      ```
      ```
      [*DeviceA-e-trunk-1] commit
      ```
      ```
      [~DeviceA-e-trunk-1] quit
      ```
   2. # Bind E-Trunk 1's member interface Eth-Trunk 1 to the RBP named **profile1** on Device A.
      ```
      [~DeviceA] remote-backup-profile profile1
      ```
      ```
      [*DeviceA-rm-backup-prf-profile1] e-trunk 1 eth-trunk 1
      ```
      ```
      [*DeviceA-rm-backup-prf-profile1] commit
      ```
      ```
      [~DeviceA-rm-backup-prf-profile1] quit
      ```
   3. # Bind an interface to the VSI and enable IGMP Report/Leave message forwarding on Device A.
      ```
      [~DeviceA] igmp-snooping enable
      ```
      ```
      [*DeviceA] interface Eth-Trunk 1
      ```
      ```
      [*DeviceA-Eth-Trunk1] mode lacp-static
      ```
      ```
      [*DeviceA-Eth-Trunk1] e-trunk 1
      ```
      ```
      [*DeviceA-Eth-Trunk1] quit
      ```
      ```
      [*DeviceA] interface Eth-Trunk 1.1
      ```
      ```
      [*DeviceA-Eth-Trunk1.1] vlan-type dot1q 1
      ```
      ```
      [*DeviceA-Eth-Trunk1.1] l2 binding vsi v123
      ```
      ```
      [*DeviceA-Eth-Trunk1.1] igmp-snooping backup-report forward
      ```
      ```
      [*DeviceA-Eth-Trunk1.1] commit
      ```
      ```
      [~DeviceA-Eth-Trunk1.1] quit
      ```
   
   # Configure a dual-device E-Trunk 1 backup platform on Device B.
   
   1. # Configure E-Trunk 1 on Device B.
      ```
      [~DeviceB] e-trunk 1
      ```
      ```
      [*DeviceB-e-trunk-1] priority 30
      ```
      ```
      [*DeviceB-e-trunk-1] peer-address 1.1.1.1 source-address 2.2.2.2
      ```
      ```
      [*DeviceB-e-trunk-1] commit
      ```
      ```
      [~DeviceB-e-trunk-1] quit
      ```
   2. # Configure the E-Trunk master/backup protocol and bind E-Trunk 1's member interface Eth-Trunk 1 to the RBP named **profile1** on Device B.
      ```
      [~DeviceB] remote-backup-profile profile1
      ```
      ```
      [*DeviceB-rm-backup-prf-profile1] e-trunk 1 eth-trunk 1
      ```
      ```
      [*DeviceB-rm-backup-prf-profile1] commit
      ```
      ```
      [~DeviceB-rm-backup-prf-profile1] quit
      ```
   3. # Bind an interface to the VSI and enable IGMP Report/Leave message forwarding on Device B.
      ```
      [~DeviceB] igmp-snooping enable
      ```
      ```
      [*DeviceB] interface Eth-Trunk 1
      ```
      ```
      [*DeviceB-Eth-Trunk1] mode lacp-static
      ```
      ```
      [*DeviceB-Eth-Trunk1] e-trunk 1
      ```
      ```
      [*DeviceB-Eth-Trunk1] quit
      ```
      ```
      [*DeviceB] interface Eth-Trunk 1.1
      ```
      ```
      [*DeviceB-Eth-Trunk1.1] vlan-type dot1q 1
      ```
      ```
      [*DeviceB-Eth-Trunk1.1] l2 binding vsi v123
      ```
      ```
      [*DeviceB-Eth-Trunk1.1] igmp-snooping backup-report forward
      ```
      ```
      [*DeviceB-Eth-Trunk1.1] commit
      ```
      ```
      [~DeviceB-Eth-Trunk1.1] quit
      ```
9. (Optional) Create BFD sessions and bind them to the E-Trunk.
   
   # Create BFD sessions and bind the peer IP tracking session to E-Trunk on Device A.
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd bfd1 bind peer-ip 2.2.2.2 track-interface interface Eth-Trunk 1
   ```
   ```
   [*DeviceA-bfd-session-bfd1] discriminator local 10
   ```
   ```
   [*DeviceA-bfd-session-bfd1] discriminator remote 30
   ```
   ```
   [*DeviceA-bfd-session-bfd1] quit
   ```
   ```
   [*DeviceA] bfd bfd2 bind peer-ip 2.2.2.2
   ```
   ```
   [*DeviceA-bfd-session-bfd2] discriminator local 60
   ```
   ```
   [*DeviceA-bfd-session-bfd2] discriminator remote 80
   ```
   ```
   [*DeviceA-bfd-session-bfd2] quit
   ```
   ```
   [*DeviceA] e-trunk 1
   ```
   ```
   [*DeviceA-e-trunk-1] e-trunk track bfd-session session-name bfd2
   ```
   ```
   [*DeviceA-e-trunk-1] security-key simple etrunkkey
   ```
   ```
   [*DeviceA-e-trunk-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Create BFD sessions and bind the peer IP tracking session to E-Trunk on Device B.
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd bfd1 bind peer-ip 1.1.1.1
   ```
   ```
   [*DeviceB-bfd-session-bfd1] discriminator local 30
   ```
   ```
   [*DeviceB-bfd-session-bfd1] discriminator remote 10
   ```
   ```
   [*DeviceB-bfd-session-bfd1] quit
   ```
   ```
   [*DeviceB] bfd bfd2 bind peer-ip 1.1.1.1 track-interface interface Eth-Trunk 1
   ```
   ```
   [*DeviceB-bfd-session-bfd2]  discriminator local 80
   ```
   ```
   [*DeviceB-bfd-session-bfd2]  discriminator remote 60
   ```
   ```
   [*DeviceB-bfd-session-bfd2] quit
   ```
   ```
   [*DeviceB] e-trunk 1
   ```
   ```
   [*DeviceB-e-trunk-1] e-trunk track bfd-session session-name bfd1
   ```
   ```
   [*DeviceB-e-trunk-1] security-key simple etrunkkey
   ```
   ```
   [*DeviceB-e-trunk-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
10. Enable remote backup for IGMP snooping services.
    
    # Enable remote backup for IGMP snooping services in the view of the RBP named **profile1** on Device A.
    ```
    [~DeviceA] remote-backup-profile profile1
    ```
    ```
    [*DeviceA-rm-backup-prf-profile1] service-type igmp-snooping
    ```
    ```
    [*DeviceA-rm-backup-prf-profile1] commit
    ```
    ```
    [~DeviceA-rm-backup-prf-profile1] quit
    ```
    # Bind the RBP to Device A's Eth-Trunk interface.
    ```
    [~DeviceA] interface Eth-Trunk 1.1
    ```
    ```
    [*DeviceA-Eth-Trunk1] remote-backup-profile profile1
    ```
    ```
    [*DeviceA-Eth-Trunk1] commit
    ```
    ```
    [~DeviceA-Eth-Trunk1] quit
    ```
    
    # Enable remote backup for IGMP snooping services in the view of the RBP named **profile1** on Device B.
    ```
    [~DeviceB] remote-backup-profile profile1
    ```
    ```
    [*DeviceB-rm-backup-prf-profile1] service-type igmp-snooping
    ```
    ```
    [*DeviceB-rm-backup-prf-profile1] commit
    ```
    ```
    [~DeviceB-rm-backup-prf-profile1] quit
    ```
    # Bind the RBP to Device B's Eth-Trunk interface.
    ```
    [~DeviceB] interface Eth-Trunk 1.1
    ```
    ```
    [*DeviceB-Eth-Trunk1] remote-backup-profile profile1
    ```
    ```
    [*DeviceB-Eth-Trunk1] commit
    ```
    ```
    [~DeviceB-Eth-Trunk1] quit
    ```
11. Verify the configuration.
    
    After completing the configuration, run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on Device A. The command output shows that the RBP named **profile1** has been created and the master/backup protocol is E-Trunk.
    ```
    <DeviceA> display remote-backup-profile profile1
    ```
    ```
     -----------------------------------------------
     Profile-Index        : 0x1001
     Profile-Name         : profile1
     Service              : igmp-snooping
     Remote-backup-service: service1
     Backup-ID            : 10
     track protocol       : E-TRUNK
         E-Trunk  ID      : 1
         Eth-trunk ID     : 1
     Interface            :
                            Eth-Trunk1
     Backup mode          : hot
     Slot-Number          : --
     Card-Number          : --
     Port-Number          : --
    ----------------------------------------------------------
    ```
    
    Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on Device B. The command output shows that the RBP named **profile1** has been created and the master/backup protocol is E-Trunk.
    ```
    <DeviceB> display remote-backup-profile profile1
    ```
    ```
     -----------------------------------------------
     Profile-Index        : 0x1001
     Profile-Name         : profile1
     Service              : igmp-snooping 
     Remote-backup-service: service1
     Backup-ID            : 10
     track protocol       : E-TRUNK
         E-Trunk  ID      : 1
         Eth-trunk ID     : 1
     Interface            :
                            Eth-Trunk1
     Backup mode          : hot
     Slot-Number          : --
     Card-Number          : --
     Port-Number          : --
    ----------------------------------------------------------
    ```
    
    Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) command on Device A. The command output shows that the RBS named **service1** has been created.
    ```
    <DeviceA> display remote-backup-service service1
    ```
    ```
    ----------------------------------------------------------
     Service-Index    : 1
     Service-Name     : service1
     TCP-State        : Connected
     Peer-ip          : 2.2.2.2
     Source-ip        : 1.1.1.1
     TCP-Port         : 1025
     Track-BFD        : --
     Last up time     : 2017-03-12 06:43:17
    ----------------------------------------------------------
    ```
    
    Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) command on Device B. The command output shows that the RBS named **service1** has been created.
    ```
    <DeviceB> display remote-backup-service service1
    ```
    ```
    ----------------------------------------------------------
     Service-Index    : 1
     Service-Name     : service1
     TCP-State        : Connected
     Peer-ip          : 1.1.1.1
     Source-ip        : 2.2.2.2
     TCP-Port         : 1025
     Track-BFD        : --
     Last up time     : 2017-03-12 06:43:54
     ----------------------------------------------------------
    ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  lacp e-trunk system-id 00e0-fc12-7890
  # 
  vlan 1 
  #
  igmp-snooping enable
  #
  bfd
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi v123
   pwsignal ldp
    vsi-id 123
    peer 3.3.3.3
   ignore-ac-state
   igmp-snooping enable
   igmp-snooping proxy
  #
  mpls ldp
  #
   ipv4-family
  #
  e-trunk 1
   priority 20
   peer-address 2.2.2.2 source-address 1.1.1.1
   security-key simple etrunkkey
   e-trunk track bfd-session session-name bfd2
   authentication-mode enhanced-hmac-sha256
  #
  remote-backup-service service1
   peer 2.2.2.2 source 1.1.1.1 port 1025
  #
  remote-backup-profile profile1
   service-type igmp-snooping  
   backup-id 10 remote-backup-service service1
   peer-backup hot
   e-trunk 1 eth-trunk 1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.0.0.1 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface Eth-Trunk1
   mode lacp-static
   e-trunk 1
  #
  interface Eth-Trunk1.1   
   vlan-type dot1q 1
   l2 binding vsi v123
   igmp-snooping backup-report forward
   remote-backup-profile profile1
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bfd bfd1 bind peer-ip 2.2.2.2 track-interface interface Eth-Trunk 1
   discriminator local 10
   discriminator remote 30
  #
  bfd bfd2 bind peer-ip 2.2.2.2
   discriminator local 60
   discriminator remote 80
  #
  ospf 1
   area 0.0.0.0 
    network 1.1.1.1 0.0.0.0
    network 10.0.0.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  lacp e-trunk system-id 00e0-fc12-7890
  #
  vlan 1 
  #
  igmp-snooping enable
  #
  bfd
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi v123
   pwsignal ldp
    vsi-id 123
    peer 3.3.3.3
   ignore-ac-state
   igmp-snooping enable
   igmp-snooping proxy
  #
  mpls ldp
  #
   ipv4-family
  #
  e-trunk 1
   priority 30
   peer-address 1.1.1.1 source-address 2.2.2.2
   security-key simple etrunkkey
   e-trunk track bfd-session session-name bfd1
   authentication-mode enhanced-hmac-sha256
  #
  remote-backup-service service1
   peer 1.1.1.1 source 2.2.2.2 port 1025
  #
  remote-backup-profile profile1
   service-type igmp-snooping  
   backup-id 10 remote-backup-service service1
   peer-backup hot
   e-trunk 1 eth-trunk 1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.0.0.2 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface Eth-Trunk1
   mode lacp-static
   e-trunk 1
  #
  interface Eth-Trunk1.1 
   vlan-type dot1q 1
   l2 binding vsi v123
   igmp-snooping backup-report forward
   remote-backup-profile profile1
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bfd bfd1 bind peer-ip 1.1.1.1
   discriminator local 30
   discriminator remote 10
  #
  bfd bfd2 bind peer-ip 1.1.1.1 track-interface interface Eth-Trunk 1
   discriminator local 80
   discriminator remote 60
  #
  ospf 1
   area 0.0.0.0 
    network 2.2.2.2 0.0.0.0
    network 10.0.0.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  return
  ```
  
  Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  vlan 1
  #
  interface Eth-Trunk1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 1
   mode lacp-static
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/3/0 
   portswitch
   undo shutdown
   port link-type access
   port default vlan 1 
  #
  return
  ```
  
  Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  vlan batch 1
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  vsi v123
   pwsignal ldp
    vsi-id 123
    peer 1.1.1.1 upe
    peer 2.2.2.2 upe
   igmp-snooping enable
   igmp-snooping proxy
  #
  mpls ldp
  #
   ipv4-family
  #
  igmp-snooping enable
  #
  vlan 1
   igmp-snooping enable
  # 
  interface GigabitEthernet0/1/0 
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp 
  # 
  interface GigabitEthernet0/2/0 
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp 
  # 
  interface GigabitEthernet0/3/0.1 
   vlan-type dot1q 1
   l2 binding vsi v123 
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  return
  ```