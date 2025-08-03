Example for Configuring RUI in Shared Address Pool Mode
=======================================================

This section provides an example for configuring RUI in shared address pool mode. A networking diagram is provided to help you understand the configuration procedure. This example covers networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Usage Scenario

As IP technologies develop rapidly, various value-added services are widely used on the Internet. Carrier-grade services, such as emerging IPTV, NGN, 4G, VIP customers' private line, and VPN interconnection, place higher requirements for IP network reliability. IP network reliability for carrier-grade services covers device, link, and network reliability. On a transport network, the availability of network devices must reach 99.999%. In other words, the downtime for maintenance during the continuous running of a device in a year is less than 5 minutes. High reliability is a basic requirement for carrier-grade devices.

The NE40E is an edge router used to carry multiple services. It plays a vital role on a network. It is uplinked to the core layer to implement the Layer 3 routing function and downlinked to the aggregation layer to terminate Layer 2 user packets for user access. Additionally, it carries multiple services including Triple Play services (HSI, VoIP, and IPTV), requiring high reliability. The NE40E provides service-level high-reliability technologies. Non-stop data flow forwarding does not mean that user services are not interrupted. Instead, when user traffic is switched to a backup device after a network node or link fails, user services are still interrupted if user information is not synchronized to the backup device. High reliability has been considered when the NE40E is designed to function as a network edge service aggregation and control device. This ensures that users' HSI, IPTV, and VoIP services are not interrupted if a network node or link fault occurs. Dual-device hot backup is designed based on this reliability scenario.

#### Hardware and Software Requirements

A board that supports user access is installed on the device.

#### Requirements on Interconnected Devices

* Upstream device: There are no special requirements. The upstream device is generally a core-layer CR that can exchange routes normally and supports MPLS and MPLS L3VPN. It is recommended that the upstream device be able to provide MPLS L2VPN capabilities. In multi-device hot backup scenarios, MPLS tunnels are best suited to function as protection tunnels. This is because an MPLS protection tunnel can be established from the IP core network if a direct link cannot be deployed between NE40Es.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the upstream device is a firewall, disable the IP spoofing attack defense function on the firewall.
* Downstream device: An aggregation switch is used as the downstream device to learn MAC addresses from Layer 2 VLAN packets.

#### Solution Limitations

* In shared address pool mode, an address pool (an IP network segment) is planned based on services. Each service (for example, Internet access or VoIP service) corresponds to a domain's configuration. If terminals that go online through different access links have the same service (for example, Internet access service), the terminals share address pool resources in a domain. This mode is called multi-link address pool sharing.
* In actual deployment, planning address pools based on links is difficult. The reason is that the number of public addresses is limited, and dividing address pools causes address resources to be wasted. Therefore, address pools are divided based on authentication domains. This allows an address pool on an MSCG to be shared among multiple links or backup groups. In this case, forwarding control cannot be performed by advertising or withdrawing address pool routes. To implement forwarding control, using a shared address pool and tunnel protection is recommended.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374398__fig_dc_ne_cfg_01043201), users access Device A and Device B through a LAN switch. The two devices run VRRP to determine the master/backup status. Basic user access functions are configured on Device A and Device B, allowing the users to go online through the master device. If the master device or the link on the network or user side of the master device fails, service traffic needs to be quickly switched to the backup device.

**Figure 1** Configuring RUI in shared address pool mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/2, and GE0/1/2, respectively.


  
![](images/fig_dc_ne_cfg_rui_000002.png)  

| **Device** | **Interface** | **IP Address** |
| --- | --- | --- |
| Device A | Eth-Trunk3.4001 | 192.168.254.2/29 |
| Device A | Loopback0 | 172.20.1.1/32 |
| Device A | Loopback10 | 172.20.1.3/32 |
| Device A | Eth-Trunk2 | 172.20.0.41/30 |
| Device A | GE0/1/0 | 172.20.0.33/30 |
| Device A | GE0/2/2 | 172.20.0.57/30 |
| Device B | Eth-Trunk3.4001 | 192.168.254.3/29 |
| Device B | Loopback0 | 172.20.1.4/32 |
| Device B | Loopback10 | 172.20.1.2/32 |
| Device B | Eth-Trunk2 | 172.20.0.42/30 |
| Device B | GE0/1/0 | 172.20.0.37/30 |
| Device B | GE0/2/2 | 172.20.0.61/30 |





#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interfaces and assign IP addresses to them.
2. Establish a multi-device backup platform.
3. Configure IP address pool binding.
4. Bind an RBP to an interface through which the user goes online.
5. Configure routes to ensure IP connectivity between devices. For details, see "IP Routing" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide*.

#### Data Preparation

To complete the configuration, you need the following data:

* VRRP ID
* Interface IP addresses of Routers that back up each other
* Backup ID, which works together with an RBS to identify an RBP to which users belong

#### Procedure

1. Configure interfaces for connecting Device A to the LAN switch, and assign IP addresses to them.
   
   
   
   The configuration on Device A is used as an example. The configuration of Device B is similar to the configuration of Device A.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface Eth-Trunk3
   ```
   ```
   [*DeviceA-Eth-Trunk3] description ToSwitch
   ```
   ```
   [*DeviceA-Eth-Trunk3] commit 
   ```
   ```
   [~DeviceA-Eth-Trunk3] quit 
   ```
   ```
   [~DeviceA] interface GigabitEthernet0/1/3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] description ToSwitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] undo shutdown 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] eth-trunk 3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] commit 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/3] quit 
   ```
   ```
   [~DeviceA] interface Eth-Trunk3.4001
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] control-vid 4001 dot1q-termination
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] dot1q termination vid 4001
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] ip address 192.168.254.2 255.255.255.248
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] commit 
   ```
   ```
   [~DeviceA-Eth-Trunk3.4001] quit 
   ```
2. Configure IP addresses for loopback and interconnection interfaces on Device A and Device B.
   
   
   
   Configure IP addresses for loopback interfaces. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   ```
   [~DeviceA]interface loopback10
   ```
   ```
   [*DeviceA-Loopback10] ip address 172.20.1.3 255.255.255.255
   ```
   ```
   [*DeviceA-Loopback10] commit 
   ```
   ```
   [~DeviceA-Loopback10] quit 
   ```
   ```
   [~DeviceA] interface loopback0
   ```
   ```
   [*DeviceA-Loopback0] ip address 172.20.1.1 255.255.255.255
   ```
   ```
   [*DeviceA-Loopback0] commit 
   ```
   ```
   [~DeviceA-Loopback0] quit 
   ```
   
   Configure IP addresses for interconnection interfaces. The configuration on Device A is used as an example. The configuration of Device B is similar to the configuration of Device A.
   
   ```
   [~DeviceA]interface Eth-Trunk2
   ```
   ```
   [*DeviceA-Eth-Trunk2] description ToBackupDevice 
   ```
   ```
   [*DeviceA-Eth-Trunk2]ip address 172.20.0.41 255.255.255.252
   ```
   ```
   [*DeviceA-Eth-Trunk2] commit 
   ```
   ```
   [~DeviceA-Eth-Trunk2] quit 
   ```
   ```
   [~DeviceA]interface GigabitEthernet0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] description ToBackupDevice
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] undo shutdown 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] eth-trunk 2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit 
   ```
3. Establish a multi-device backup platform. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, only the RUI-related configuration is described. For other configurations, see the corresponding configuration guide.
   
   # Configure a BFD session on the access side to rapidly detect interface or link faults and trigger a master/backup VRRP switchover. 192.168.254.3 is the IP address of Eth-Trunk 3.4001 on Device B.
   
   ```
   [~DeviceA] bfd 
   ```
   ```
   [*DeviceA-bfd] quit 
   ```
   ```
   [*DeviceA] bfd eth-trunk3-peer bind peer-ip 192.168.254.3 source-ip 192.168.254.2
   ```
   ```
   [*DeviceA-bfd-session-eth-trunk3-peer] discriminator local 2 
   ```
   ```
   [*DeviceA-bfd-session-eth-trunk3-peer] discriminator remote 3 
   ```
   ```
   [*DeviceA-bfd-session-eth-trunk3-peer] commit 
   ```
   ```
   [~DeviceA-bfd-session-eth-trunk3-peer] quit 
   ```
   
   # Configure a VRRP group on Eth-Trunk 3.4001, and configure the VRRP group to track the BFD session and network-side interface.
   
   ```
   [~DeviceA] vrrp recover-delay 15
   ```
   ```
   [*DeviceA] commit 
   ```
   ```
   [~DeviceA] interface Eth-Trunk3.4001
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] vrrp vrid 3 virtual-ip 192.168.254.1
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] admin-vrrp vrid 3
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] vrrp vrid 3 priority 120
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] vrrp vrid 3 preempt-mode timer delay 1200
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] vrrp vrid 3 track interface GigabitEthernet0/1/0 reduced 30
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] vrrp vrid 3 track bfd-session 2 peer
   ```
   ```
   [*DeviceA-Eth-Trunk3.4001] commit 
   ```
   ```
   [~DeviceA-Eth-Trunk3.4001] quit 
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Different priorities must be configured for devices in a VRRP group. The device with a higher priority is the master device.
   
   # Configure an RBS.
   
   ```
   [~DeviceA] remote-backup-service rbs_qhmd 
   ```
   ```
   [*DeviceA-rm-backup-rbs_qhmd] peer 172.20.1.2 source 172.20.1.3 port 2046
   ```
   ```
   [*DeviceA-rm-backup-rbs_qhmd] commit
   ```
   ```
   [~DeviceA-rm-backup-rbs_qhmd] track interface GigabitEthernet0/1/0
   ```
   ```
   [*DeviceA-rm-backup-rbs_qhmd] track interface GigabitEthernet0/2/2
   ```
   ```
   [*DeviceA-rm-backup-rbs_qhmd] protect redirect ip-nexthop 172.20.0.42 interface Eth-Trunk2
   ```
   ```
   [*DeviceA-rm-backup-rbs_qhmd] commit
   ```
   ```
   [~DeviceA-rm-backup-rbs_qhmd] quit 
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Ensure that the master and backup devices can ping each other.
   
   # Configure an RBP.
   
   ```
   [~DeviceA] remote-backup-profile rbp3 
   ```
   ```
   [*DeviceA-rm-backup-prf-rbp3] service-type bras 
   ```
   ```
   [*DeviceA-rm-backup-prf-rbp3] backup-id 3 remote-backup-service rbs_qhmd
   ```
   ```
   [*DeviceA-rm-backup-prf-rbp3] peer-backup hot 
   ```
   ```
   [*DeviceA-rm-backup-prf-rbp3] vrrp-id 3 interface Eth-Trunk3.4001
   ```
   ```
   [*DeviceA-rm-backup-prf-rbp3] commit
   ```
   ```
   [~DeviceA-rm-backup-prf-rbp3] nas logic-port Gigabitethernet 0/1/3
   ```
   ```
   [*DeviceA-rm-backup-prf-rbp3] commit
   ```
   ```
   [~DeviceA-rm-backup-prf-rbp3] nas logic-sysname MasterDevice
   ```
   ```
   [~DeviceA-rm-backup-prf-rbp3] nas logic-ip 172.20.1.1
   ```
   ```
   [~DeviceA-rm-backup-prf-rbp3] quit 
   ```
4. Configure IP address pool binding. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure an address pool on the backup device, run the **[**ip pool**](cmdqueryname=ip+pool)** **ip-pool-name** ****bas**** { ****local**** | ****remote**** } ****rui-slave**** command. In load balancing scenarios, if this command is not run, the master and backup devices may be assigned the same IP address, causing an address assignment conflict.
   
   # Configure an address pool.
   
   ```
   [~DeviceA] ip pool dmtjs_xi bas local
   ```
   ```
   [~DeviceA-ip-pool-dmtjs_xi] gateway 192.168.1.1 255.255.255.0
   ```
   ```
   [~DeviceA-ip-pool-dmtjs_xi] section 0 192.168.1.2 192.168.1.254 
   ```
   ```
   [*DeviceA-ip-pool-dmtjs_xi] dns-server 192.168.1.1
   ```
   ```
   [*DeviceA-ip-pool-dmtjs_xi] commit
   ```
   ```
   [~DeviceA-ip-pool-dmtjs_xi] quit
   ```
   
   # Bind the address pool to the RBS.
   
   ```
   [~DeviceA] remote-backup-service rbs_qhmd
   ```
   ```
   [*DeviceA-rm-backup-service rbs_qhmd] commit 
   ```
   ```
   [~DeviceA-rm-backup-service rbs_qhmd] ip-pool dmtjs_xi metric 10
   ```
   ```
   [*DeviceA-rm-backup-service rbs_qhmd] commit
   ```
   ```
   [~DeviceA-backup-service rbs_qhmd] quit
   ```
5. Configure a RADIUS server group.
   
   
   ```
   [~DeviceA] radius-server group rd
   ```
   ```
   [*DeviceA-radius-rd] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*DeviceA-radius-rd] radius-server accounting 10.7.66.66 1813
   ```
   ```
   [*DeviceA-radius-rd] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-radius-rd] radius-server retransmit 2
   ```
   ```
   [*DeviceA-radius-rd] commit
   ```
   ```
   [~DeviceA-radius-rd] quit
   ```
6. Configure authentication and accounting policies for user access. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] authentication-scheme wu
   ```
   ```
   [*DeviceA-aaa-authen-wu] authentication-mode radius
   ```
   ```
   [*DeviceA-aaa-authen-wu] commit
   ```
   ```
   [~DeviceA-aaa-authen-wu] quit
   ```
   ```
   [*DeviceA-aaa]  accounting-scheme wu
   ```
   ```
   [*DeviceA-aaa-accounting-wu] accounting-mode none
   ```
   ```
   [*DeviceA-aaa-accounting-wu] commit
   ```
   ```
   [~DeviceA-aaa-accounting-wu] quit
   ```
   ```
   [~DeviceA-aaa]  domain dmtjs_xi
   ```
   ```
   [*DeviceA-aaa-domain-dmtjs_xi] authentication-scheme wu
   ```
   ```
   [*DeviceA-aaa-domain-dmtjs_xi] accounting-scheme wu
   ```
   ```
   [*DeviceA-aaa-domain-dmtjs_xi] radius-server group rd
   ```
   ```
   [*DeviceA-aaa-domain-dmtjs_xi] ip-pool dmtjs_xi
   ```
   ```
   [*DeviceA-aaa-domain-dmtjs_xi] commit
   ```
   ```
   [~DeviceA-aaa-domain-dmtjs_xi] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
7. Bind the RBP to Eth-Trunk3.5001 through which users go online. The configuration of Device B is similar to that of Device A.
   
   
   ```
   [~DeviceA] interface Eth-Trunk3.5001
   ```
   ```
   [*DeviceA-Eth-Trunk3.5001] commit
   ```
   ```
   [~DeviceA-Eth-Trunk3.5001] user-vlan 1
   ```
   ```
   [~DeviceA-Eth-Trunk3.5001-vlan-1-1] quit
   ```
   ```
   [~DeviceA-Eth-Trunk3.5001] remote-backup-profile rbp3 
   ```
   ```
   [*DeviceA-Eth-Trunk3.5001] bas
   ```
   ```
   [*DeviceA-Eth-Trunk3.5001-bas]access-type layer2-subscriber default-domain authentication dmtjs_xi
   ```
   ```
   [*DeviceA-Eth-Trunk3.5001-bas] authentication-method bind
   ```
   ```
   [*DeviceA-Eth-Trunk3.5001-bas] commit 
   ```
   ```
   [~DeviceA-Eth-Trunk3.5001-bas] quit 
   ```
8. Configure advertisement of address pool routes. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] import-route unr
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.20.1.1 0.0.0.0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.20.1.3 0.0.0.0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.20.0.36 0.0.0.3
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.20.0.40 0.0.0.3
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 172.20.0.60 0.0.0.3
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit 
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.0] quit 
   ```
9. Verify the configuration.
   
   
   
   After successfully configuring the RBP, run the **display remote-backup-profile** command. The command output shows that the RBS type is **bras**, the RBP named **rbp3** is bound to **Eth-Trunk3.5001** through which users go online, and Device A is in the **Master** state.
   
   ```
   <DeviceA> display remote-backup-profile rbp3
   -----------------------------------------------
    Profile-Index        : 0x802
    Profile-Name         : rbp3
    Service            : bras
    Remote-backup-service: rbs_qhmd
    Backup-ID            : 10
    track protocol       : VRRP
    VRRP-ID              : 3
    VRRP-Interface       : Eth-Trunk3.4001
    Interface          : Eth-Trunk3.5001
    State              : Master
    Peer-state         : Slave
    Backup mode          : hot
    Slot-Number          : 1
    Card-Number          : 0
    Port-Number          : 0
    Nas logic-port       : Gigabitethernet 0/1/3
    Nas logic-ip         : 172.20.1.1
    Nas logic-sysname    : MasterDevice
    Traffic interval     : 10(minutes)
   ```
   
   After the RBS is configured successfully, the TCP connection status becomes **Connected**.
   
   ```
   <DeviceA> display remote-backup-service rbs_qhmd 
   ----------------------------------------------------------
    Service-Index    : 0
    Service-Name     : rbs_qhmd
    TCP-State      : Connected
    Peer-ip          : 172.20.1.2 
    Source-ip        : 172.20.1.3 
    TCP-Port         : 2046
    Track-BFD        : --
    Track-interface0 : 0/1/0
                     Weight : 10
    Track-interface1 : 0/2/2
                     Weight : 10
    SSL-Policy-Name  : --
    SSL-State        : --
   Uplink state     : 2 (1:DOWN 2:UP)
    Domain-map-list  : --
   ----------------------------------------------------------
   
    ip pool:  
            dmtjs_xi metric 10
    ipv6 pool:  
    Failure ratio    : 100%
    Failure duration : 0 min
   --------------------------------------------------------
   ```
   
   After users go online, run the **display backup-user** command to check information about backup users.
   
   ```
   <DeviceA> display backup-user
   ```
   ```
     Remote-backup-service: rbs_qhmd
     Total Users Numer: 3
   ------------------------------------------------------------------------
    100     101     102    
   ------------------------------------------------------------------------
   
   ```
   
   Run the **display access-user interface** command to view online user information on a specified interface.
   
   ```
   <DeviceA> display access-user interface Eth-Trunk3.5001
   ```
   ```
   ------------------------------------------------------------------------------
     UserID  Username                Interface      IP address       MAC                     IPv6 address
     ------------------------------------------------------------------------------
     --------------------------------------------------------------------------
     100     user1@dmtjs_xi          Eth-Trunk3.5001   192.168.1.10    00e0-fc12-0101          -
     101     user2@dmtjs_xi          Eth-Trunk3.5001   192.168.1.9     00e0-fc12-0102          -
     102     user3@dmtjs_xi          Eth-Trunk3.5001   192.168.1.8     00e0-fc12-0103          -
     --------------------------------------------------------------------------
     Total users                        :3
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
  router id 172.20.1.3
  ```
  ```
  #
  ```
  ```
  vrrp recover-delay 15
  ```
  ```
  #
  ```
  ```
  vlan batch 2 to 9 11 to 504 506 to 3999 4001 to 4094
  ```
  ```
  #
  ```
  ```
  bfd
  ```
  ```
  #
  ```
  ```
  ip pool dmtjs_xi bas local 
  ```
  ```
  gateway 192.168.1.1 255.255.255.0
  ```
  ```
  section 0 192.168.1.2 192.168.1.254 
  ```
  ```
  dns-server 192.168.1.1
  ```
  ```
  #
  ```
  ```
  radius-server group rd                                                                                         
  ```
  ```
   radius-server authentication 10.7.66.66 1812 weight 0                                             
  ```
  ```
   radius-server accounting 10.7.66.66 1813 weight 0                                                            
  ```
  ```
   radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
  ```
  ```
   radius-server retransmit 2   
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
   authentication-scheme wu
  ```
  ```
    authentication-mode radius
  ```
  ```
   accounting-scheme wu 
  ```
  ```
    accounting-mode none
  ```
  ```
   domain dmtjs_xi 
  ```
  ```
    authentication-scheme wu 
  ```
  ```
    accounting-scheme wu
  ```
  ```
    radius-server group rd
  ```
  ```
    ip-pool dmtjs_xi 
  ```
  ```
  #
  ```
  ```
  bfd eth-trunk3-peer bind peer-ip 192.168.254.3 source-ip 192.168.254.2
  ```
  ```
   discriminator local 2 
  ```
  ```
   discriminator remote 3 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
  description ToSwitch
  ```
  ```
  undo shutdown
  #
  ```
  ```
  interface Eth-Trunk3
   description ToSwitch
  #
  ```
  ```
  interface Eth-Trunk3.4001
  ```
  ```
   control-vid 4001 dot1q-termination
  ```
  ```
   dot1q termination vid 4001
  ```
  ```
   ip address 192.168.254.2 255.255.255.248
  ```
  ```
   vrrp vrid 3 virtual-ip 192.168.254.1
  ```
  ```
   admin-vrrp vrid 3 
  ```
  ```
   vrrp vrid 3 priority 120 
  ```
  ```
   vrrp vrid 3 preempt-mode timer delay 1200
  ```
  ```
   vrrp vrid 3 track bfd-session 2 peer
  ```
  ```
   vrrp vrid 3 track interface GigabitEthernet0/1/0 reduced 30
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 172.20.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  interface LoopBack10
  ```
  ```
   ip address 172.20.1.3 255.255.255.255
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.20.0.33 255.255.255.252
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.20.0.57 255.255.255.252
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   description ToBackupDevice
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 2
  ```
  ```
  #
  ```
  ```
  interface Eth-Trunk2
  ```
  ```
   description ToBackupDevice
  ```
  ```
   ip address 172.20.0.41 255.255.255.252
  ```
  ```
  #
  ```
  ```
  remote-backup-service rbs_qhmd
  ```
  ```
   peer 172.20.1.2 source 172.20.1.3 port 2046
  ```
  ```
   track interface gigabitethernet 0/1/0 
  ```
  ```
   track interface gigabitethernet 0/2/2 
  ```
  ```
   protect redirect ip-nexthop 172.20.0.42 interface Eth-Trunk2
  ```
  ```
   ip-pool dmtjs_xi metric 10
  ```
  ```
  #
  ```
  ```
  remote-backup-profile rbp3 
  ```
  ```
   service-type bras
  ```
  ```
   backup-id 3 remote-backup-service rbs_qhmd
  ```
  ```
   peer-backup hot 
  ```
  ```
   vrrp-id 3 interface Eth-Trunk3.4001
  ```
  ```
   nas logic-port gigabitethernet0/1/3 
  ```
  ```
   nas logic-sysname MasterDevice 
  ```
  ```
   nas logic-ip 172.20.1.1 
  ```
  ```
  #
  ```
  ```
  interface Eth-Trunk3.5001
  ```
  ```
   user-vlan 1 
  ```
  ```
   remote-backup-profile rbp3 
  ```
  ```
   bas 
  ```
  ```
    access-type layer2-subscriber default-domain authentication dmtjs_xi
  ```
  ```
    authentication-method bind 
  ```
  ```
   #
  ```
  ```
  #
  ospf 1
   import-route unr
   area 0.0.0.0
    network 172.20.0.36 0.0.0.3
    network 172.20.0.60 0.0.0.3
    network 172.20.0.40 0.0.0.3
    network 172.20.1.1 0.0.0.0
    network 172.20.1.3 0.0.0.0
  ```
  ```
  #
  ```
  ```
   return 
  ```
* Device B configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
  router id 172.20.1.2
  ```
  ```
  #
  ```
  ```
  vrrp recover-delay 15
  ```
  ```
  #
  ```
  ```
  vlan batch 2 to 9 11 to 504 506 to 3999 4001 to 4094
  ```
  ```
  #
  ```
  ```
  bfd
  ```
  ```
  #
  ```
  ```
  ip pool dmtjs_xi bas local rui-slave
  ```
  ```
  gateway 192.168.1.1 255.255.255.0
  ```
  ```
  section 0 192.168.1.2 192.168.1.254 
  ```
  ```
  dns-server 192.168.1.1
  ```
  ```
  #
  ```
  ```
  radius-server group rd                                                                                         
   radius-server authentication 10.7.66.66 1812 weight 0                                             
   radius-server accounting 10.7.66.66 1813 weight 0                                                            
   radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
   radius-server retransmit 2   
  #
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
   authentication-scheme wu
  ```
  ```
    authentication-mode radius
  ```
  ```
   accounting-scheme wu 
  ```
  ```
    accounting-mode none
  ```
  ```
   domain dmtjs_xi 
  ```
  ```
    authentication-scheme wu 
  ```
  ```
    accounting-scheme wu
  ```
  ```
    ip-pool dmtjs_xi 
  ```
  ```
    radius-server group rd
  ```
  ```
  #
  ```
  ```
  bfd eth-trunk3-peer bind peer-ip 192.168.254.2 source-ip 192.168.254.3
  ```
  ```
   discriminator local 3 
  ```
  ```
   discriminator remote 2 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   description ToSwitch
  ```
  ```
   undo shutdown
  #
  ```
  ```
  interface Eth-Trunk3
   description ToSwitch
  #
  ```
  ```
   interface Eth-Trunk3.4001
  ```
  ```
   control-vid 4001 dot1q-termination
  ```
  ```
   dot1q termination vid 4001
  ```
  ```
   ip address 192.168.254.3 255.255.255.248
  ```
  ```
   vrrp vrid 3 virtual-ip 192.168.254.1
  ```
  ```
   admin-vrrp vrid 3 
  ```
  ```
   vrrp vrid 3 track bfd-session 3 peer
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 172.20.1.4 255.255.255.255
  ```
  ```
  #
  ```
  ```
  interface LoopBack10
  ```
  ```
   ip address 172.20.1.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.20.0.37 255.255.255.252
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.20.0.61 255.255.255.252
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   description ToMasterDevice
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 2
  ```
  ```
  #
  ```
  ```
  interface Eth-Trunk2
  ```
  ```
   description ToMasterDevice
  ```
  ```
   ip address 172.20.0.42 255.255.255.252
  ```
  ```
  #
  ```
  ```
  remote-backup-service rbs_qhmd
  ```
  ```
   peer 172.20.1.3 source 172.20.1.2 port 2046
  ```
  ```
   track interface gigabitethernet 0/1/0
  ```
  ```
   track interface gigabitethernet 0/2/2
  ```
  ```
   protect redirect ip-nexthop 172.20.0.41 interface Eth-Trunk2
  ```
  ```
   ip-pool dmtjs_xi metric 20
  ```
  ```
  #
  ```
  ```
  remote-backup-profile rbp3 
  ```
  ```
   service-type bras
  ```
  ```
   backup-id 3 remote-backup-service rbs_qhmd
  ```
  ```
   peer-backup hot 
  ```
  ```
   vrrp-id 3 interface Eth-Trunk3.4001
  ```
  ```
   nas logic-port gigabitethernet0/1/3 
  ```
  ```
   nas logic-sysname MasterDevice 
  ```
  ```
   nas logic-ip 172.20.1.1 
  ```
  ```
  #
  ```
  ```
  interface Eth-Trunk3.5001
  ```
  ```
   user-vlan 1 
  ```
  ```
   remote-backup-profile rbp3 
  ```
  ```
   bas 
  ```
  ```
    access-type layer2-subscriber default-domain authentication dmtjs_xi
  ```
  ```
    authentication-method bind 
  ```
  ```
   #
  ```
  ```
  #
  ospf 1
   import-route unr
   area 0.0.0.0
    network 172.20.0.36 0.0.0.3
    network 172.20.0.60 0.0.0.3
    network 172.20.0.40 0.0.0.3
    network 172.20.1.2 0.0.0.0
    network 172.20.1.3 0.0.0.0
  ```
  ```
  #
  ```
  ```
   return 
  ```