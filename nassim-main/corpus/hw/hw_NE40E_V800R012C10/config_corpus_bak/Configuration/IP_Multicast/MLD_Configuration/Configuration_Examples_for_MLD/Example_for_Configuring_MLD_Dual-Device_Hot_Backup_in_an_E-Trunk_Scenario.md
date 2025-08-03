Example for Configuring MLD Dual-Device Hot Backup in an E-Trunk Scenario
=========================================================================

This section provides an example for configuring MLD dual-device hot backup in an E-Trunk scenario to ensure that multicast services are not interrupted after a master/backup device switchover.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001198468591__fig_dc_vrp_multicast_cfg_013201), an E-Trunk is configured on DeviceA and DeviceB, with DeviceA as the master device, and DeviceB as the backup device. In normal situations, the link between DeviceA and DeviceC is up, and the link between DeviceB and DeviceC is down. DeviceC sends MLD messages to DeviceA through the link that is up. After receiving the messages, DeviceA backs up them to DeviceB through an RBS channel.

If DeviceA or the link between DeviceA and DeviceC fails, a master/backup switchover is performed within the E-Trunk. Then the link between DeviceB and DeviceC goes up, and DeviceC sends messages to DeviceB through this link. In addition, MLD dual-device hot backup can be deployed on DeviceA and DeviceB so that DeviceB can synchronize MLD entries from DeviceA in real time. After a master/backup switchover is performed, MLD services are not affected.

**Figure 1** Networking for configuring MLD dual-device hot backup in an E-Trunk scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](figure/en-us_image_0000001220765507.png)

![](figure/en-us_image_0000001200308613.png)

**Table 1** IPv6 addresses of interfaces
| Device | Interface | IPv6 Address |
| --- | --- | --- |
| DeviceA | GigabitEthernet0/1/1 | 2001:DB8:10::1/64 |
| GigabitEthernet0/1/2 | Eth-trunk 1 |
| GigabitEthernet0/1/3 | 2001:DB8:20::1/64 |
| LoopBack0 | 2001:DB8:11::11/64 |
| DeviceB | GigabitEthernet0/1/0 | 2001:DB8:10::2/64 |
| GigabitEthernet0/1/2 | 2001:DB8:30::1/64 |
| GigabitEthernet0/1/3 | Eth-trunk 1 |
| LoopBack0 | 2001:DB8:33::33/64 |
| DeviceC | GigabitEthernet0/1/0 | 2001:DB8:40::1/64 |
| GigabitEthernet0/1/2 | - |
| GigabitEthernet0/1/3 | - |
| DeviceD | GigabitEthernet0/1/0 | 2001:DB8:40::1/64 |
| GigabitEthernet0/1/2 | 2001:DB8:30::2/64 |
| GigabitEthernet0/1/3 | 2001:DB8:20::2/64 |
| LoopBack0 | 2001:DB8:22::22/64 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on the master and backup devices, configure IP addresses for the two ends of the RBS channel, and configure a routing protocol to ensure network-layer route reachability.
2. Configure an E-Trunk on DeviceA and DeviceB.
3. Establish a dual-device backup platform on DeviceA and DeviceB, and configure a password in ciphertext for the E-Trunk.
4. Enable remote backup for MLD services on DeviceA and DeviceB.

#### Procedure

1. Configure IP addresses for interfaces on DeviceA and DeviceB and configure IS-IS for interworking. For details, see [Configuration Files](#EN-US_TASK_0000001198468591__section_dc_vrp_multicast_cfg_013203).
2. Add Ethernet interfaces on DeviceA and DeviceB to Eth-Trunk 1, and add Eth-Trunk 1 to E-Trunk 1. For details, see [Configuration Files](#EN-US_TASK_0000001198468591__section_dc_vrp_multicast_cfg_013203).
3. Add the interfaces connecting DeviceC to DeviceA and DeviceB to Eth-Trunk 1. For details, see [Configuration Files](#EN-US_TASK_0000001198468591__section_dc_vrp_multicast_cfg_013203).
4. Configure an RBS.
   
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
   [*DeviceA-rm-backup-srv-service1] peer-ipv6 2001:DB8:33::33 source-ipv6 2001:DB8:11::11 port 1025
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
   [*DeviceB-rm-backup-srv-service1] peer-ipv6 2001:DB8:11::11 source-ipv6 2001:DB8:33::33 port 1025
   ```
   ```
   [*DeviceB-rm-backup-srv-service1] commit
   ```
   ```
   [~DeviceB-rm-backup-srv-service1] quit
   ```
5. Configure an RBP.
   
   # Configure an RBP on DeviceA.
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
   
   # Configure an RBP on DeviceB.
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
6. Configure a dual-device E-Trunk backup platform.
   
   
   
   # Configure a dual-device E-Trunk 1 backup platform on DeviceA.
   
   1. # Configure E-Trunk 1 on DeviceA.
      ```
      [~DeviceA] e-trunk 1
      ```
      ```
      [*DeviceA-e-trunk-1] priority 20
      ```
      ```
      [*DeviceA-e-trunk-1] security-key cipher YsHsjx_202206
      ```
      ```
      [*DeviceA-e-trunk-1] peer-ipv6 2001:DB8:33::33 source-ipv6 2001:DB8:11::11
      ```
      ```
      [*DeviceA-e-trunk-1] commit
      ```
      ```
      [~DeviceA-e-trunk-1] quit
      ```
      ```
      [~DeviceA] lacp e-trunk system-id 00e0-fc12-3455
      ```
      ```
      [*DeviceA] commit
      ```
   2. # Configure the E-Trunk master/backup protocol and bind E-Trunk 1's member interface Eth-Trunk 1 to the RBP named **profile1** on DeviceA.
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
   3. # Bind the RBP to the Eth-Trunk interface on DeviceA.
      ```
      [~DeviceA] interface Eth-Trunk 1
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
   4. # Enable MLD on DeviceA.
      ```
      [~DeviceA] multicast ipv6 routing-enable
      ```
      ```
      [*DeviceA] interface Eth-Trunk 1
      ```
      ```
      [*DeviceA-Eth-Trunk1] pim ipv6 sm
      ```
      ```
      [*DeviceA-Eth-Trunk1] mld enable
      ```
      ```
      [*DeviceA-Eth-Trunk1] mode lacp-static
      ```
      ```
      [*DeviceA-Eth-Trunk1] commit
      ```
      ```
      [~DeviceA-Eth-Trunk1] quit
      ```
   
   # Configure a dual-device E-Trunk 1 backup platform on DeviceB.
   
   1. # Configure E-Trunk 1 on DeviceB.
      ```
      [~DeviceB] e-trunk 1
      ```
      ```
      [*DeviceB-e-trunk-1] priority 10
      ```
      ```
      [*DeviceB-e-trunk-1] security-key cipher YsHsjx_202206
      ```
      ```
      [*DeviceB-e-trunk-1] peer-ipv6 2001:DB8:11::11 source-ipv6 2001:DB8:33::33
      ```
      ```
      [*DeviceB-e-trunk-1] commit
      ```
      ```
      [~DeviceB-e-trunk-1] quit
      ```
      ```
      [~DeviceB] lacp e-trunk system-id 00e0-fc12-3456
      ```
      ```
      [*DeviceB] commit
      ```
   2. # Configure the E-Trunk master/backup protocol and bind E-Trunk 1's member interface Eth-Trunk 1 to the RBP named **profile1** on DeviceB.
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
   3. # Bind the RBP to the Eth-Trunk interface on DeviceB.
      ```
      [~DeviceB] interface Eth-Trunk 1
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
   4. # Enable MLD on DeviceB.
      ```
      [~DeviceB] multicast ipv6 routing-enable
      ```
      ```
      [*DeviceB] interface Eth-Trunk 1
      ```
      ```
      [*DeviceB-Eth-Trunk1] pim ipv6 sm
      ```
      ```
      [*DeviceB-Eth-Trunk1] mld enable
      ```
      ```
      [*DeviceB-Eth-Trunk1] mode lacp-static
      ```
      ```
      [*DeviceB-Eth-Trunk1] commit
      ```
      ```
      [~DeviceB-Eth-Trunk1] quit
      ```
7. Enable remote backup for MLD services.
   
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
8. Verify the configuration.
   
   After completing the configuration, run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on DeviceA. The command output shows that the RBP named **profile1** has been created and that the master/backup protocol is E-Trunk.
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
    track protocol       : E-TRUNK
        E-Trunk  ID      : 1
        Eth-trunk ID     : 1
    Interface            :
                           Eth-Trunk1
    Forwarding Configured: Slave Forwarding
    Backup mode          : hot
    Slot-Number          : --
    Card-Number          : --
    Port-Number          : --
   ```
   
   Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on DeviceB. The command output shows that the RBP named **profile1** has been created and that the master/backup protocol is E-Trunk.
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
    track protocol       : E-TRUNK
        E-Trunk  ID      : 1
        Eth-trunk ID     : 1
    Interface            :
                           Eth-Trunk1
    Forwarding Configured: Slave Forwarding
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
    Peer-ip          : 2001:DB8:33::33
    Source-ip        : 2001:DB8:11::11
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
    Peer-ip          : 2001:DB8:11::11
    Source-ip        : 2001:DB8:33::33
    TCP-Port         : 1025
    Track-BFD        : --
    SSL-Policy-Name  : --
    SSL-State        : --
    Last up time     : 2021-05-29 03:21:36
   ----------------------------------------------------------
   ```
   
   Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command on DeviceA to check the status of the Eth-Trunk interface.
   ```
   <DeviceA> display eth-trunk
   ```
   ```
   Eth-Trunk1's state information is:
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 1                                  WorkingMode: STATIC
   Preempt Delay: Disabled                    Hash arithmetic: According to flow
   System Priority: 32768                     System ID: 00e0-fc12-3455(Local)
   Least Active-linknumber: 1                 Max Active-linknumber: 16
   Operate status: up                         Number Of Up Ports In Trunk: 1
   Timeout Period: Slow
   PortKeyMode: Auto
   --------------------------------------------------------------------------------
   ActorPortName             Status    PortType   PortPri   PortNo  PortKey   PortState  Weight
   GigabitEthernet0/1/2 (hr) Selected  1GE        32768     1       305       10111100   1
   Partner:
   --------------------------------------------------------------------------------
   ActorPortName        SysPri      SystemID        PortPri   PortNo   PortKey    PortState
   GigabitEthernet0/1/2 32768       00e0-fc12-3460  32768     1        305        10111100
   ```
   Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command on DeviceB to check the status of the Eth-Trunk interface.
   ```
   <DeviceB> display eth-trunk
   ```
   ```
   Eth-Trunk1's state information is:
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 1                      WorkingMode: STATIC
   Preempt Delay: Disabled        Hash arithmetic: According to flow
   System Priority: 32768         System ID: 00e0-fc12-3456(Local)
   Least Active-linknumber: 1     Max Active-linknumber: 16
   Operate status: down           Number Of Up Ports In Trunk: 0
   Timeout Period: Slow
   PortKeyMode: Auto
   --------------------------------------------------------------------------------
   ActorPortName            Status   PortType   PortPri  PortNo  PortKey  PortState  Weight
   GigabitEthernet0/1/3(hr) Unselect 1GE        32768    32769   305      10110000   1
   Partner:
   --------------------------------------------------------------------------------
   ActorPortName         SysPri   SystemID       PortPri  PortNo PortKey  PortState
   GigabitEthernet0/1/3  32768    00e0-fc12-3461 32768    2      305      10100000
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  e-trunk 1
   priority 20
   peer-ipv6 2001:DB8:33::33 source-ipv6 2001:DB8:11::11
   security-key cipher %^%#VQE;E!Dl&Rr]if$F>}w9uk5C>y-4|MS$unQ!#Mb#%^%# 
  #
  lacp priority 100
  lacp e-trunk system-id 00e0-fc12-3455
  #
  remote-backup-service service1
   peer-ipv6 2001:DB8:33::33 source-ipv6 2001:DB8:11::11 port 1025
  #
  remote-backup-profile profile1
   service-type mld
   backup-id 10 remote-backup-service service1
   peer-backup hot
   e-trunk 1 eth-trunk 1
  #
  isis 1
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   #
  #
  interface Eth-Trunk1
   ipv6 enable
   ipv6 address 2001:DB8:15::1/64
   pim ipv6 sm
   mld enable
   mode lacp-static
   e-trunk 1
   isis ipv6 enable 1
   remote-backup-profile profile1
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
   eth-trunk 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface Loopback0
   ipv6 enable
   ipv6 address 2001:DB8:11::11/64
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
  e-trunk 1
   priority 10
   peer-ipv6 2001:DB8:11::11 source-ipv6 2001:DB8:33::33
   security-key cipher %^%#VQE;E!Dl&Rr]if$F>}w9uk5C>y-4|MS$unQ!#Mb#%^%# 
  #
  lacp e-trunk system-id 00e0-fc12-3456
  #
  remote-backup-service service1
   peer-ipv6 2001:DB8:11::11 source-ipv6 2001:DB8:33::33 port 1025
  #
  remote-backup-profile profile1
   service-type mld
   backup-id 10 remote-backup-service service1
   peer-backup hot
   e-trunk 1 eth-trunk 1
  #
  isis 1
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   #
  #
  interface Eth-Trunk1
   ipv6 enable
   ipv6 address 2001:DB8:35::3/64
   pim ipv6 sm
   mld enable
   mode lacp-static
   e-trunk 1
   isis ipv6 enable 1
   remote-backup-profile profile1
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
   eth-trunk 1
  #
  interface Loopback0
   ipv6 enable
   ipv6 address 2001:DB8:33::33/64
   isis ipv6 enable 1
  #
  interface NULL0
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
  interface Eth-Trunk1
   portswitch
   port link-type access
   port default vlan 100
   mode lacp-static
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 100
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   eth-trunk 1
  #
  interface Loopback0
   ipv6 enable
   ipv6 address 2001:DB8:55::55/64
   isis ipv6 enable 1
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
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   #
  #
  interface GigabitEthernet0/1/0
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
   isis ipv6 enable 1
  #
  interface NULL0
  #
  pim-ipv6
   static-rp 2001:DB8:22::22
  #
  return
  ```