Example for Configuring Dual-Device IGMP Hot Backup
===================================================

This section provides an example for configuring dual-device IGMP hot backup in a master/backup E-Trunk scenario. After dual-device IGMP hot backup is configured, multicast services are not interrupted during a master/backup E-Trunk switchover.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172366777__fig_dc_vrp_multicast_cfg_013201), an E-Trunk backup group is configured on DeviceA and DeviceB. DeviceA is the master device, and DeviceB is the backup device. In normal cases, the link between DeviceA and DeviceC is up, and the link between DeviceB and DeviceC is down. DeviceC sends IGMP messages to DeviceA through the link that is up. After receiving the messages, DeviceA backs them up to DeviceB through the RBS channel.

If Device A or the link between Device A and Device C fails, a master/backup E-Trunk switchover is performed and the link between Device B and Device C goes up. Device C sends packets to Device B through the up link, ensuring IGMP service continuity.

**Figure 1** Example for configuring dual-device IGMP hot backup in a master/backup E-Trunk scenario  
![](images/fig_dc_vrp_multicast_cfg_013201.png)

Interfaces 1 through 3 in this example represent GE0/1/1, GE0/1/2, and GE0/1/3, respectively.

To ensure that IGMP services are not interrupted during a master/backup switchover, configure dual-device IGMP hot backup on DeviceA and DeviceB. After the configuration is complete, DeviceB synchronizes IGMP entries from DeviceA in real time.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to loopback interfaces on the master and backup devices, and configure a routing protocol.
2. Configure an E-Trunk on Device A and Device B.
3. Establish a dual-device backup platform on Device A and Device B.
4. Create BFD sessions and bind them to E-Trunk on Device A and Device B.
5. Enable remote backup for IGMP services on Device A and Device B.

#### Data Preparation

To complete the configuration, you need the following data:

* Eth-Trunk ID on Device A, Device B, and Device C: 1. LACP system priority of Device A: 100.
* E-Trunk ID on DeviceA and DeviceB: 1.
* Device A's Loopback0 interface IP address is: 1.1.1.1/32; Device B's Loopback0 interface IP address: 3.3.3.3/32; TCP port number: 1025.
* Device A's IP address: 10.0.13.1/24; Device B's IP address: 10.0.13.3/24.
* RBS name: service1; RBP name: profile1; backup ID: 10.
* E-Trunk password in ciphertext.

#### Procedure

1. Assign an IP address to each interface and configure OSPF on DeviceA and DeviceB. For configuration details, see [Configuration Files](#EN-US_TASK_0172366777__section_dc_vrp_multicast_cfg_013203) in this section.
2. Add an Ethernet interface to Eth-Trunk 1, and add Eth-Trunk 1 to E-Trunk 1 on DeviceA and DeviceB. For configuration details, see [Configuration Files](#EN-US_TASK_0172366777__section_dc_vrp_multicast_cfg_013203) in this section.
3. Add the interfaces for connecting Device C to Device A and Device B to Eth-Trunk 1. For configuration details, see [Configuration Files](#EN-US_TASK_0172366777__section_dc_vrp_multicast_cfg_013203) in this section.
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
   [*DeviceA-rm-backup-srv-service1] peer 3.3.3.3 source 1.1.1.1 port 1025
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
   [*DeviceB-rm-backup-srv-service1] peer 1.1.1.1 source 3.3.3.3 port 1025
   ```
   ```
   [*DeviceB-rm-backup-srv-service1] commit
   ```
   ```
   [~DeviceB-rm-backup-srv-service1] quit
   ```
5. # Configure an RBP.
   
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
6. Configure a dual-device E-Trunk backup platform.
   
   
   
   # Configure a dual-device E-Trunk 1 backup platform on Device A.
   
   1. Configure E-Trunk 1 on Device A.
      ```
      [~DeviceA] e-trunk 1
      ```
      ```
      [*DeviceA-e-trunk-1] peer-address 3.3.3.3 source-address 1.1.1.1
      ```
      ```
      [*DeviceA-e-trunk-1] security-key cipher YsHsjx_202206
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
   3. # Bind the RBP to the Eth-Trunk interface on Device A.
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
   4. Enable IGMP Report/Leave packet forwarding function on Device A.
      ```
      [~DeviceA] multicast routing-enable
      ```
      ```
      [*DeviceA] interface Eth-Trunk 1
      ```
      ```
      [*DeviceA-Eth-Trunk1] pim sm
      ```
      ```
      [*DeviceA-Eth-Trunk1] igmp enable
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
   
   # Configure a dual-device E-Trunk 1 backup platform on Device B.
   
   1. Configure E-Trunk 1 on Device B.
      ```
      [~DeviceB] e-trunk 1
      ```
      ```
      [*DeviceB-e-trunk-1] peer-address 1.1.1.1 source-address 3.3.3.3
      ```
      ```
      [*DeviceB-e-trunk-1] security-key cipher YsHsjx_202206
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
   3. # Bind the RBP to the Eth-Trunk interface on Device B.
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
   4. Enable IGMP Report/Leave packet forwarding function on Device B.
      ```
      [~DeviceB] multicast routing-enable
      ```
      ```
      [*DeviceB] interface Eth-Trunk 1
      ```
      ```
      [*DeviceB-Eth-Trunk1] pim sm
      ```
      ```
      [*DeviceB-Eth-Trunk1] igmp enable
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
7. Enable remote backup for IGMP services.
   
   # Enable remote backup for IGMP services in the view of the RBP named profile1 on Device A.
   ```
   [~DeviceA] remote-backup-profile profile1
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] service-type igmp
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceA-rm-backup-prf-profile1] quit
   ```
   
   # Enable remote backup for IGMP services in the view of the RBP named profile1 on Device B.
   ```
   [~DeviceB] remote-backup-profile profile1
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] service-type igmp
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] commit
   ```
   ```
   [~DeviceB-rm-backup-prf-profile1] quit
   ```
8. Verify the configuration.
   
   After completing the configuration, run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on DeviceA. The command output shows that the RBP named **profile1** has been created and the master/backup protocol is **E-Trunk**.
   ```
   <DeviceA> display remote-backup-profile profile1
   ```
   ```
    -----------------------------------------------
    Profile-Index        : 0x1000
    Profile-Name         : profile1
    Service              : igmp
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
   
   Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) command on Device B. The command output shows that the RBP named **profile1** has been created and the master/backup protocol is **E-Trunk**.
   ```
   <DeviceB> display remote-backup-profile profile1
   ```
   ```
    -----------------------------------------------
    Profile-Index        : 0x1000
    Profile-Name         : profile1
    Service              : igmp
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
   
   Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) command on Device A. The command output shows that the RBS named **service1** has been created.
   ```
   <DeviceA> display remote-backup-service service1
   ```
   ```
   ----------------------------------------------------------
    Service-Index    : 1
    Service-Name     : service1
    TCP-State        : connected
    Peer-ip          : 3.3.3.3
    Source-ip        : 1.1.1.1
    TCP-Port         : 1025
    Track-BFD        : --
    SSL-Policy-Name  : --
    SSL-State        : --
    Last up time     : 2018-05-29 03:21:36
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
    TCP-State        : connected
    Peer-ip          : 1.1.1.1
    Source-ip        : 3.3.3.3
    TCP-Port         : 1025
    Track-BFD        : --
    SSL-Policy-Name  : --
    SSL-State        : --
    Last up time     : 2018-05-29 03:21:36
   ----------------------------------------------------------
   ```
   
   Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command on Device A. The command output shows the status of Eth-Trunk interface.
   ```
   <DeviceA> display eth-trunk
   ```
   ```
   Eth-Trunk1's state information is:
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 1                       WorkingMode: STATIC
   Preempt Delay: Disabled         Hash arithmetic: According to flow
   System Priority: 32768          System ID: 00e0-fc12-3455(Local)
   Least Active-linknumber: 1      Max Active-linknumber: 16
   Operate status: up              Number Of Up Ports In Trunk: 1
   Timeout Period: Slow
   PortKeyMode: Auto
   --------------------------------------------------------------------------------
   ActorPortName             Status   PortType PortPri    PortNo   PortKey    PortState   Weight
   GigabitEthernet0/1/2 (hr) Selected 1GE      32768       1       305        10111100     1
   Partner:
   --------------------------------------------------------------------------------
   ActorPortName         SysPri   SystemID        PortPri  PortNo   PortKey  PortState
   GigabitEthernet0/1/2  32768    00e0-fc12-3455  32768    1        305       10111100
   ```
   Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command on DeviceB. The command output shows the status of Eth-Trunk interface.
   ```
   <DeviceB> display eth-trunk
   ```
   ```
   Eth-Trunk1's state information is:
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 1 WorkingMode: STATIC
   Preempt Delay: Disabled Hash arithmetic: According to flow
   System Priority: 32768 System ID: 00e0-fc12-3456(Local)
   Least Active-linknumber: 1 Max Active-linknumber: 16
   Operate status: down Number Of Up Ports In Trunk: 0
   Timeout Period: Slow
   PortKeyMode: Auto
   --------------------------------------------------------------------------------
   ActorPortName Status PortType PortPri PortNo PortKey PortState Weight
   GigabitEthernet0/1/3(hr) Unselect 1GE 32768 32769 305 10110000 1
   Partner:
   --------------------------------------------------------------------------------
   ActorPortName          SysPri  SystemID        PortPri  PortNo PortKey  PortState
   GigabitEthernet0/1/3   32768   00e0-fc12-3456  32768    2      305      10100000
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  e-trunk 1
   peer-address 3.3.3.3 source-address 1.1.1.1
   security-key cipher %^%#VQE;E!Dl&Rr]if$F>}w9uk5C>y-4|MS$unQ!#Mb#%^%# 
  #
  lacp priority 100
  lacp e-trunk system-id 00e0-fc12-3455
  #
  remote-backup-service service1
   peer 3.3.3.3 source 1.1.1.1 port 1025
  #
  remote-backup-profile profile1
   service-type igmp
   backup-id 10 remote-backup-service service1
   peer-backup hot
   e-trunk 1 eth-trunk 1
  #
  interface Eth-Trunk1
   ip address 10.0.15.1 255.255.255.0
   pim sm
   igmp enable
   mode lacp-static
   e-trunk 1
   remote-backup-profile profile1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.13.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.0.12.1 255.255.255.0
   pim sm
  #
  interface Loopback0
   ip address 1.1.1.1 255.255.255.255
  #
  interface NULL0
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.0.12.0 0.0.0.255
    network 10.0.13.0 0.0.0.255
    network 10.0.15.0 0.0.0.255
  #
  pim
   static-rp 2.2.2.2
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  e-trunk 1
   peer-address 1.1.1.1 source-address 3.3.3.3
   security-key cipher %^%#VQE;E!Dl&Rr]if$F>}w9uk5C>y-4|MS$unQ!#Mb#%^%# 
  #
  lacp e-trunk system-id 00e0-fc12-3456
  #
  remote-backup-service service1
   peer 1.1.1.1 source 3.3.3.3 port 1025
  #
  remote-backup-profile profile1
   service-type igmp
   backup-id 10 remote-backup-service service1
   peer-backup hot
   e-trunk 1 eth-trunk 1
  #
  interface Eth-Trunk1
   ip address 10.0.35.3 255.255.255.0
   pim sm
   igmp enable
   mode lacp-static
   e-trunk 1
   remote-backup-profile profile1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.13.3 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.0.23.3 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   eth-trunk 1
  #
  interface Loopback0
   ip address 3.3.3.3 255.255.255.255
  #
  interface NULL0
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.0.13.0 0.0.0.255
    network 10.0.23.0 0.0.0.255
    network 10.0.35.0 0.0.0.255
  #
  pim
   static-rp 2.2.2.2
  #
  return
  ```
  
  Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 100
  #
  multicast routing-enable
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
   ip address 5.5.5.5 255.255.255.255
  #
  interface NULL0 
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
  #
  return
  ```
  
  Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #               
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.5.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.0.23.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.0.12.2 255.255.255.0
   pim sm
  #
  interface Loopback0
   ip address 2.2.2.2 255.255.255.255
  #
  interface NULL0
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.0.5.0 0.0.0.255
    network 10.0.12.0 0.0.0.255
    network 10.0.23.0 0.0.0.255
  #
  pim
   static-rp 2.2.2.2
  #
  return
  ```