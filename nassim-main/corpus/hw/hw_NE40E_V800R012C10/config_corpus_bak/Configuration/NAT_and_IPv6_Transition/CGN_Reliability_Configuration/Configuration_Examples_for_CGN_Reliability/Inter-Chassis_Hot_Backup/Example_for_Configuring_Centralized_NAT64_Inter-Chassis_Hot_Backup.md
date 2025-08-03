Example for Configuring Centralized NAT64 Inter-Chassis Hot Backup
==================================================================

This section provides an example for configuring HA dual-device inter-chassis hot backup for centralized NAT64.

#### Networking Requirements

In the centralized networking scenario shown in [Figure 1](#EN-US_TASK_0172362478__fig_01), a NAT service board is deployed in slot 1 on CGN1 and another NAT service board is deployed in slot 1 on CGN2. CGN1 and CGN2, between which a VRRP channel is established over GE interfaces, are deployed close to the CR on the MAN core as standalone devices. CPU0 of the NAT service board in slot 1 on CGN1 and CPU0 of the NAT service board in slot 1 on CGN2 implement NAT64 inter-chassis hot backup. VRRP enabled for the channel determines the master/backup status of the CGN devices, and the service board status is associated with VRRP.

**Figure 1** Networking of inter-chassis hot backup in a centralized NAT64 scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_ne_cgn-reliability_cfg_0039.png)

**Table 1** IP address plan
| Device Name | Interface Name | IP Address and Mask |
| --- | --- | --- |
| CGN1 | GE0/1/1 | 10.1.1.1/24 |
| GE0/1/2 | 2001:db8::1:110e/126 |
| CGN2 | GE0/1/1 | 10.1.1.2/24 |
| GE0/1/2 | 2001:db8::1:110f/126 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable NAT64 and configure NAT64 session resources.
2. Enable HA hot backup.
3. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure an inter-chassis backup channel.
4. Create and configure a VRRP group.
5. Associate HA with VRRP.
6. Bind the service-location group to the VRRP group.
7. Create a service-instance group and bind it to the service-location group.
8. Create a NAT64 instance and bind it to the service-instance group.
9. Configure a NAT64 traffic diversion policy and a NAT64 conversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* Index of the service-location group
* Slot ID and CPU ID of the active CPU on a service board of the master and backup devices (CPU 0 in slot 1 in this example)
* Interfaces of the inter-chassis backup channel and IP addresses of the peer devices
* Index, virtual IP address, member priorities, and preemption delay of a VRRP group
* Name of a service-instance group
* Name and index of a NAT64 instance
* Name, index, and IP address range of a NAT64 address pool
* NAT64 IPv6 prefix of 64:FF9B::/96
* ACL number and ACL rule
* Traffic classifier name, traffic behavior name, and traffic diversion policy name


#### Procedure

1. Enable NAT64 and configure NAT64 session resources.
   
   # Configure the master device CGN1.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CGN1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CGN1] vsm on-board-mode disable
   ```
   ```
   [*CGN1] commit
   ```
   ```
   [~CGN1] license
   ```
   ```
   [*CGN1-license] active nat64 vsuf slot 1
   ```
   ```
   [*CGN1-license] active nat session-table size 16 slot 1 
   ```
   ```
   [*CGN1-license] commit
   ```
   ```
   [~CGN1-license] quit
   ```
   
   # Configure the backup device CGN2.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CGN2
   ```
   ```
   [*HUAWEI] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of the NAT64 GTL license on CGN2 is the same as that on CGN1. For detailed configurations, see [CGN2 configuration file](#EN-US_TASK_0172362478__config_02).
2. Enable HA hot backup in the system view of master and backup devices.
   
   
   
   # Enable HA hot backup on CGN1.
   
   ```
   [~CGN1] service-ha hot-backup enable
   ```
   ```
   [*CGN1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of CGN2 is similar to that of CGN1. For detailed configurations, see [CGN2 configuration file](#EN-US_TASK_0172362478__config_02).
3. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure an inter-chassis backup channel between the master and backup devices.
   
   
   
   # On CGN1, create service-location group 1, configure CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1 and the peer IP address to 10.1.1.2.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [*CGN1-service-location-1] location slot 1 
   ```
   ```
   [*CGN1-service-location-1] remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.2
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   
   # On CGN2, create service-location group 1, configure CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to GE 0/1/1 and the peer IP address to 10.1.1.1.
   
   ```
   [~CGN2] service-location 1
   ```
   ```
   [*CGN2-service-location-1] location slot 1 
   ```
   ```
   [*CGN2-service-location-1] remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.1
   ```
   ```
   [*CGN2-service-location-1] commit
   ```
   ```
   [~CGN2-service-location-1] quit
   ```
4. Configure a VRRP group on each CGN device.
   
   
   
   # On CGN1, enter the view of GE 0/1/1, create VRRP group 1, and set the VRRP virtual IP address to 10.1.1.3. Configure the VRRP group as an mVRRP group, and set CGN1's priority in the VRRP group to 200, the VRRP preemption delay to 1500s, and the VRRP recovery delay to 15s.
   
   ```
   [~CGN1] interface GigabitEthernet0/1/1
   ```
   ```
   [~CGN1-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] vrrp vrid 1 priority 200
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] vrrp vrid 1 preempt-mode timer delay 1500
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] vrrp recover-delay 15
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/1/1] quit
   ```
   
   # On CGN2, enter the view of GE 0/1/1, create VRRP group 1, and set the VRRP virtual IP address to 10.1.1.3. Configure the VRRP group as an mVRRP group, set CGN2's priority in the VRRP group to 150, and set the VRRP recovery delay to 15s.
   
   ```
   [~CGN2] interface GigabitEthernet0/1/1
   ```
   ```
   [~CGN2-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] vrrp vrid 1 priority 150
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] vrrp recover-delay 15
   ```
   ```
   [*CGN2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CGN2-GigabitEthernet0/1/1] quit
   ```
5. Associate HA with VRRP on the master and backup devices.
   
   
   
   # On CGN1, enter the view of GE 0/1/1, and associate service-location group 1 with VRRP group 1.
   
   ```
   [~CGN1] interface GigabitEthernet 0/1/1
   ```
   ```
   [~CGN1-GigabitEthernet0/1/1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*CGN1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CGN1-GigabitEthernet0/1/1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This configuration is optional on the backup device. You can determine whether to perform this step based on network requirements.
   
   The configuration of CGN2 is the same as that of CGN1. For detailed configurations, see [CGN2 configuration file](#EN-US_TASK_0172362478__config_02).
6. Bind the service-location group to the VRRP group on each CGN device.
   
   
   
   # Bind service-location group 1 to VRRP group 1 on CGN1.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [~CGN1-service-location-1] vrrp vrid 1 interface GigabitEthernet 0/1/1
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of CGN2 is the same as that of CGN1. For detailed configurations, see [CGN2 configuration file](#EN-US_TASK_0172362478__config_02).
7. Create a service-instance group and bind it to the service-location group on each CGN device.
   
   
   
   # On CGN1, create service-instance group named **group1** and bind it to service-location group 1.
   
   ```
   [~CGN1] service-instance-group group1
   ```
   ```
   [~CGN1-service-instance-group-group1] service-location 1
   ```
   ```
   [*CGN1-service-instance-group-group1] commit
   ```
   ```
   [~CGN1-service-instance-group-group1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of CGN2 is the same as that of CGN1. For detailed configurations, see [CGN2 configuration file](#EN-US_TASK_0172362478__config_02).
8. Create a NAT64 instance on each CGN device and bind it to the service-instance group.
   
   
   
   # On CGN1, create a NAT64 instance named **nat64** and bind it to the service-instance group named **group1**. Configure a NAT64 IPv6 prefix of 64:FF9B::/96. This prefix must be the same as the prefix allocated by the DNS64 server.
   
   ```
   [~CGN1] nat64 instance nat64 id 1
   ```
   ```
   [*CGN1-nat64-instance-nat64] service-instance-group group1
   ```
   ```
   [*CGN1-nat64-instance-nat64] nat64 address-group nat64-group1 group-id 1
   ```
   ```
   [*CGN1-nat64-instance-nat64-nat64-address-group-nat64-group1] section 0 11.1.1.1 mask 24
   ```
   ```
   [*CGN1-nat64-instance-nat64-nat64-address-group-nat64-group1] quit
   ```
   ```
   [*CGN1-nat64-instance-nat64] nat64  prefix  64:FF9B:: prefix-length 96 1
   ```
   ```
   [*CGN1-nat64-instance-nat64] commit
   ```
   ```
   [~CGN1-nat64-instance-nat64] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of CGN2 is the same as that of CGN1. For detailed configurations, see [CGN2 configuration file](#EN-US_TASK_0172362478__config_02).
9. Configure a NAT64 traffic diversion policy and a NAT64 conversion policy. For configuration details, see "Example for Configuring Centralized NAT64" in *NAT and IPv6 Transition> NAT64 Configuration*.
   
   
   
   # Configure a NAT64 traffic diversion policy and a NAT64 conversion policy on CGN1.
   
   1. Configure a NAT64 traffic diversion policy.
      
      1. Configure an ACL-based traffic classification rule so that only hosts on internal network segment 2001:db8::1:1112/126 can access the IPv4 Internet.
         ```
         [~CGN1] acl ipv6 number 3001
         ```
         ```
         [*CGN1-acl6-adv-3001] rule 5 permit ipv6 source 2001:db8::1:1112/126 destination 64:FF9B::/96 
         ```
         ```
         [*CGN1-acl6-adv-3001] commit
         ```
         ```
         [~CGN1-acl6-adv-3001] quit
         ```
      2. Configure a traffic classifier.
         ```
         [~CGN1] traffic classifier c1
         ```
         ```
         [*CGN1-classifier-c1] if-match ipv6 acl 3001
         ```
         ```
         [*CGN1-classifier-c1] commit
         ```
         ```
         [~CGN1-classifier-c1] quit
         ```
      3. Configure a traffic behavior and bind it to the NAT64 instance.
         ```
         [~CGN1] traffic behavior b1 
         ```
         ```
         [*CGN1-behavior-b1] nat64 bind instance nat64
         ```
         ```
         [*CGN1-behavior-b1] commit
         ```
         ```
         [~CGN1-behavior-b1] quit
         ```
      4. Configure a traffic policy and associate the ACL-based traffic classification rule with the traffic behavior.
         ```
         [~CGN1] traffic policy p1
         ```
         ```
         [*CGN1-trafficpolicy-p1] classifier c1 behavior b1
         ```
         ```
         [*CGN1-trafficpolicy-p1] commit
         ```
         ```
         [~CGN1-trafficpolicy-p1] quit
         ```
      5. Configure an IPv6 address in the user-side interface view.
         ```
         [~CGN1] interface GigabitEthernet0/1/2
         ```
         ```
         [*CGN1-GigabitEthernet0/1/2] ipv6 enable
         ```
         ```
         [*CGN1-GigabitEthernet0/1/2] ipv6 address 2001:db8::1:110e 126
         ```
         ```
         [*CGN1-GigabitEthernet0/1/2] commit
         ```
         ```
         [~CGN1-GigabitEthernet0/1/2] quit
         ```
      6. Apply the NAT64 traffic diversion policy in the user-side interface view.
         ```
         [~CGN1] interface GigabitEthernet0/1/2
         ```
         ```
         [*CGN1-GigabitEthernet0/1/2] traffic-policy p1 inbound
         ```
         ```
         [*CGN1-GigabitEthernet0/1/2] commit
         ```
         ```
         [~CGN1-GigabitEthernet0/1/2] quit
         ```
   2. Configure a NAT64 conversion policy so that NAT64 is performed using addresses in the NAT64 address pool for the packets that are diverted by an interface board to a service board.
      
      ```
      [~CGN1] nat64 instance nat64 id 1
      ```
      ```
      [~CGN1-nat64-instance-nat64] nat64 outbound any address-group nat64-group1
      ```
      ```
      [*CGN1-nat64-instance-nat64] commit
      ```
      ```
      [~CGN1-nat64-instance-nat64] quit
      ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of CGN2 is the same as that of CGN1. For detailed configurations, see [CGN2 configuration file](#EN-US_TASK_0172362478__config_02).

#### Configuration Files

* CGN1 configuration file
  
  ```
  #
  sysname CGN1
  #
  vsm on-board-mode disable
  #
  license
   active nat64 vsuf slot 1
   active nat session-table size 16 slot 1
  #
  acl ipv6 number 3001
   rule 5 permit ipv6 source 2001:db8::1:1112/126 destination 64:FF9B::/96
  #
  traffic classifier c1 operator or
   if-match ipv6 acl 3001 precedence 1
  #
  traffic behavior b1
   nat64 bind instance nat64
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 1
  #
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1
   remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.2
  #
  service-instance-group group1
   service-location 1
  #
  nat64 instance nat64 id 1
   service-instance-group group1
   nat64 address-group nat64-group1 group-id 1 
    section 0 11.1.1.1 mask 24  
   #
   nat64 outbound any address-group nat64-group1
   nat64 prefix 64:FF9B:: prefix-length 96 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp recover-delay 15
  #
  interface GigabitEthernet 0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8::1:110e 126
   traffic-policy p1 inbound
  #
  return
  ```
* CGN2 configuration file
  
  ```
  #
  sysname CGN2
  #
  license
   active nat64 vsuf slot 1
   active nat session-table size 16 slot 1
  #
  acl ipv6 number 3001
   rule 5 permit ipv6 source 2001:db8::1:1112/126 destination 64:FF9B::/96
  #
  traffic classifier c1 operator or
   if-match ipv6 acl 3001 precedence 1
  #
  traffic behavior b1
   nat64 bind instance nat64
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 1
  #
  service-ha hot-backup enable
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface GigabitEthernet 0/1/1
   remote-backup interface GigabitEthernet 0/1/1 peer 10.1.1.1
  #
  service-instance-group group1
   service-location 1
  #
  nat64 instance nat64 id 1
   service-instance-group group1
   nat64 address-group nat64-group1 group-id 1 
    section 0 11.1.1.1 mask 24  
   #
   nat64 outbound any address-group nat64-group1
   nat64 prefix 64:FF9B:: prefix-length 96 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 150
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp recover-delay 15
  #
  interface GigabitEthernet 0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8::1:110f 126
   traffic-policy p1 inbound
  #
  return
  ```