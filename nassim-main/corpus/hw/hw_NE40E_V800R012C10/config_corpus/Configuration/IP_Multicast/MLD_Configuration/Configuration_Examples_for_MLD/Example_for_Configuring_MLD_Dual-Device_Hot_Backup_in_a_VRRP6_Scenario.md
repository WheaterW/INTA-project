Example for Configuring MLD Dual-Device Hot Backup in a VRRP6 Scenario
======================================================================

This section provides an example for configuring MLD dual-device hot backup in a VRRP6 scenario to ensure that multicast services are not interrupted after a master/backup switchover.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001198628483__fig_dc_vrp_multicast_cfg_013201), a VRRP6 group is configured on DeviceA and DeviceB, with DeviceA as the master device and DeviceB as the backup device. In normal situations, the link between DeviceA and DeviceC is up, and the link between DeviceB and DeviceC is down. DeviceC sends MLD messages to DeviceA through the link that is up. After receiving the messages, DeviceA backs up them to DeviceB through an RBS channel.

If DeviceA or the link between DeviceA and DeviceC fails, the link between DeviceB and DeviceC goes up, and DeviceC sends messages to DeviceB through this link. In addition, MLD dual-device hot backup can be deployed on DeviceA and DeviceB so that DeviceB can synchronize MLD entries from DeviceA in real time. After a master/backup switchover is performed, MLD services are not affected.

**Figure 1** Networking for configuring MLD dual-device hot backup in a VRRP6 scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](figure/en-us_image_0000001220604033.png)

**Table 1** IPv6 addresses of interfaces
| Device | Interface | IPv6 Address |
| --- | --- | --- |
| DeviceA | GigabitEthernet0/1/1 | 2001:DB8:10::1/64 |
| GigabitEthernet0/1/2 | 2001:DB8:50::1/64 |
| GigabitEthernet0/1/3 | 2001:DB8:20::1/64 |
| DeviceB | GigabitEthernet0/1/1 | 2001:DB8:10::2/64 |
| GigabitEthernet0/1/2 | 2001:DB8:30::1/64 |
| GigabitEthernet0/1/3 | 2001:DB8:50::2/64 |
| DeviceC | GigabitEthernet0/1/1 | 2001:DB8:40::1/64 |
| GigabitEthernet0/1/2 | - |
| GigabitEthernet0/1/3 | - |
| DeviceD | GigabitEthernet0/1/1 | 2001:DB8:70::1/64 |
| GigabitEthernet0/1/2 | 2001:DB8:30::2/64 |
| GigabitEthernet0/1/3 | 2001:DB8:20::2/64 |
| LoopBack0 | 2001:DB8:22::22/64 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on the master and backup devices, configure IP addresses for the two ends of the RBS channel, and configure a routing protocol to ensure network-layer route reachability.
2. Configure a VRRP6 group on DeviceA and DeviceB.
3. Configure a VRRP6 dual-device backup platform on DeviceA and DeviceB.
4. Enable remote backup for MLD services on DeviceA and DeviceB.

#### Procedure

1. Configure IP addresses for interfaces on DeviceA and DeviceB and configure IS-IS for interworking. For configuration details, see [Configuration Files](#EN-US_TASK_0000001198628483__section_dc_vrp_multicast_cfg_013203) in this section.
2. Configure a VRRP6 group. For configuration details, see [Configuration Files](#EN-US_TASK_0000001198628483__section_dc_vrp_multicast_cfg_013203) in this section.
3. Configure an RBS.
   
   # Configure an RBS on DeviceA.
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
   [*DeviceA-rm-backup-srv-service1] peer-ipv6 2001:DB8:10::2 source-ipv6 2001:DB8:10::1 port 1025
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] commit
   ```
   ```
   [~DeviceA-rm-backup-srv-service1] quit
   ```
   
   # Configure an RBS on DeviceB.
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
   [*DeviceB-rm-backup-srv-service1] peer-ipv6 2001:DB8:10::1 source-ipv6 2001:DB8:10::2 port 1025
   ```
   ```
   [*DeviceB-rm-backup-srv-service1] commit
   ```
   ```
   [~DeviceB-rm-backup-srv-service1] quit
   ```
4. Configure an RBP.
   
   # Configure an RBP on DeviceA.
   ```
   [~DeviceA] remote-backup-profile profile1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] backup-id 10 remote-backup-service service1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] peer-backup hot
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceA-rm-backup-prf-profile1] quit
   ```
   
   # Configure an RBP on DeviceB.
   ```
   [~DeviceB] remote-backup-profile profile1
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] backup-id 10 remote-backup-service service1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] peer-backup hot
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceB-rm-backup-prf-profile1] quit
   ```
5. Configure a VRRP6 dual-device backup platform.
   
   # Configure a dual-device backup platform on DeviceA. The configuration of DeviceB is similar to that of DeviceA. For configuration details, see [Configuration Files](#EN-US_TASK_0000001198628483__section_dc_vrp_multicast_cfg_013203) in this section.
   ```
   [~DeviceA] remote-backup-profile profile1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] vrrp6-id 1 interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceA-rm-backup-prf-profile1] quit
   ```
   
   # Enable MLD and bind the multicast service interface to the VRRP6 group on DeviceA. The configuration of DeviceB is similar to that of DeviceA. For configuration details, see [Configuration Files](#EN-US_TASK_0000001198628483__section_dc_vrp_multicast_cfg_013203) in this section.
   ```
   [~DeviceA] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] mld enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] multicast ipv6 track vrrp6 vrid 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] pim ipv6 ignore dr-state
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] pim ipv6 ignore assert-state
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] remote-backup-profile profile1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [~DeviceA] commit
   ```
6. Enable remote backup for MLD services.
   
   # Enable remote backup for MLD services in the RBP view on DeviceA.
   ```
   [~DeviceA] remote-backup-profile profile1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] service-type mld
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceA-rm-backup-prf-profile1] quit
   ```
   
   # Enable remote backup for MLD services in the RBP view on DeviceB.
   ```
   [~DeviceB] remote-backup-profile profile1
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] service-type mld
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceB-rm-backup-prf-profile1] quit
   ```
7. Verify the configuration.
   
   After completing the configuration, run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on DeviceA. The command output shows that the RBP named **profile1** has been created and that the master/backup protocol is VRRP.
   ```
   <DeviceA> display remote-backup-profile profile1
   ```
   ```
    -----------------------------------------------
    Profile-Index        : 0x1000
    Profile-Name         : profile1
    Service              : MLD
    Remote-backup-service: service1
    Backup-ID            : 10
    track protocol       : VRRP
    VRRP-ID              : 1
    VRRP-Interface       : GigabitEthernet0/1/2
    State                :
    Peer State           :
    Interface            : 
                        GigabitEthernet0/1/2
    Backup mode          : hot
    Slot-Number          : --
    Card-Number          : --
    Port-Number          : --
   ```
   
   Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on DeviceB. The command output shows that the RBP named **profile1** has been created and that the master/backup protocol is VRRP.
   ```
   <DeviceB> display remote-backup-profile profile1
   ```
   ```
    -----------------------------------------------
    Profile-Index        : 0x1000
    Profile-Name         : profile1
    Service              : MLD
    Remote-backup-service: service1
    Backup-ID            : 10
    track protocol       : VRRP
    VRRP-ID              : 1
    VRRP-Interface       : GigabitEthernet0/1/2
    State                :
    Peer State           :
    Interface            : 
                           GigabitEthernet0/1/3
    Backup mode          : hot
    Slot-Number          : --
    Card-Number          : --
    Port-Number          : --
   ```
   
   Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) command on DeviceA. The command output shows that the RBS **service1** has been created.
   ```
   <DeviceA> display remote-backup-service service1
   ```
   ```
   ----------------------------------------------------------
    Service-Index    : 1
    Service-Name     : service1
    TCP-State        : connected
    Peer-ip          : 2001:DB8:10::2
    Source-ip        : 2001:DB8:10::1
    TCP-Port         : 1025
    Track-BFD        : --
    SSL-Policy-Name  : --
    SSL-State        : --
    Last up time     : 2021-05-29 03:21:36
   ----------------------------------------------------------
   ```
   
   Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) command on DeviceB. The command output shows that the RBS **service1** has been created.
   ```
   <DeviceB> display remote-backup-service service1
   ```
   ```
   ----------------------------------------------------------
    Service-Index    : 1
    Service-Name     : service1
    TCP-State        : connected
    Peer-ip          : 2001:DB8:10::1
    Source-ip        : 2001:DB8:10::2
    TCP-Port         : 1025
    Track-BFD        : --
    SSL-Policy-Name  : --
    SSL-State        : --
    Last up time     : 2021-05-29 03:21:36
   ----------------------------------------------------------
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  remote-backup-service service1
   peer-ipv6 2001:DB8:10::2 source-ipv6 2001:DB8:10::1 port 1025
  #
  remote-backup-profile profile1
   service-type mld
   backup-id 10 remote-backup-service service1
   peer-backup hot
   vrrp6-id 1 interface GigabitEthernet0/1/2
  #
  isis 1
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   #
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:50::1/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::50
   vrrp6 vrid 1 priority 200
   vrrp6 vrid 1 preempt-mode timer delay 10
   pim ipv6 sm
   pim ipv6 ignore dr-state
   mld enable
   multicast ipv6 track vrrp6 vrid 1
   isis ipv6 enable 1
   remote-backup-profile profile1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface NULL0
  #
  pim-ipv6
   static-rp 2001:DB8:22::22
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast ipv6 routing-enable
  #
  remote-backup-service service1
   peer-ipv6 2001:DB8:10::1 source-ipv6 2001:DB8:10::2 port 1025
  #
  remote-backup-profile profile1
   service-type mld
   backup-id 10 remote-backup-service service1
   peer-backup hot
   vrrp6-id 1 interface GigabitEthernet0/1/3
  #
  isis 1
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   #
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:30::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:50::2/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::50
   vrrp6 vrid 1 priority 120
   vrrp6 vrid 1 preempt-mode timer delay 10
   pim ipv6 sm
   pim ipv6 ignore assert-state
   mld enable
   multicast ipv6 track vrrp6 vrid 1
   isis ipv6 enable 1
   remote-backup-profile profile1
  #
  pim-ipv6
   static-rp 2001:DB8:22::22
  #
  return
  ```
  
  DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 100
  #
  multicast ipv6 routing-enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 100
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type access
   port default vlan 100
  #
  interface GigabitEthernet0/1/3
   portswitch
   undo shutdown
   port link-type access
   port default vlan 100
  #
  interface NULL0 
  #
  return
  ```
  
  DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast ipv6 routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0004.00
   #
   ipv6 enable topology ipv6
   #
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:40::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:30::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface Loopback0
   ipv6 enable
   ipv6 address 2001:DB8:22::22/64
  #
  interface NULL0
  #
  pim-ipv6
   static-rp 2001:DB8:22::22
  #
  return
  ```