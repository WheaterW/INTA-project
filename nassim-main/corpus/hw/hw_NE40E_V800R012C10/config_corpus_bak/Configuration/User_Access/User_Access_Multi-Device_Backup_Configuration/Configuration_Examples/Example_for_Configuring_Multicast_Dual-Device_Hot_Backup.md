Example for Configuring Multicast Dual-Device Hot Backup
========================================================

This section provides an example for configuring multicast dual-device hot backup.

#### Usage Scenario

As IP technologies develop rapidly, various value-added services are widely used on the Internet. Carrier-grade services, such as emerging IPTV, NGN, 4G, VIP customers' private line, and VPN interconnection, place higher requirements for IP network reliability. IP network reliability for carrier-grade services covers device, link, and network reliability. On a transport network, the availability of network devices must reach 99.999%. In other words, the downtime for maintenance during the continuous running of a device in a year is less than 5 minutes. High reliability is a basic requirement for carrier-grade devices.

The NE40E is an edge router used to carry multiple services. It plays a vital role on a network. It is uplinked to the core layer to implement the Layer 3 routing function and downlinked to the aggregation layer to terminate Layer 2 user packets for user access. Additionally, it carries multiple services including Triple Play services (HSI, VoIP, and IPTV), requiring high reliability. The NE40E provides service-level high-reliability technologies. Non-stop data flow forwarding does not mean that user services are not interrupted. Instead, when user traffic is switched to a backup device after a network node or link fails, user services are still interrupted if user information is not synchronized to the backup device. High reliability has been considered when the NE40E is designed to function as a network edge service aggregation and control device. This ensures that users' HSI, IPTV, and VoIP services are not interrupted if a network node or link fault occurs. Dual-device hot backup is designed based on this reliability scenario.

#### Requirements on Hardware

A board that supports user access is installed on the device.

#### Requirements on Interconnected Devices

* Upstream device: There are no special requirements. The upstream device is generally a core-layer CR that can exchange routes normally and supports MPLS and MPLS L3VPN. It is recommended that the upstream device be able to provide MPLS L2VPN capabilities. In multi-device hot backup scenarios, MPLS tunnels are best suited to function as protection tunnels. This is because an MPLS protection tunnel can be established from the IP core network if a direct link cannot be deployed between NE40Es.
* Downstream device: An aggregation switch is used as the downstream device to learn MAC addresses from Layer 2 VLAN packets.
#### Solution Limitations

* The VRRP recovery delay must be twice or three times the interval at which multicast query packets are sent to ensure that entries on the master and backup devices are the same. The default interval at which multicast query packets are sent is 60s.
* The NE40E functions as the multicast replication point and uses the copy by session mode.
#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374404__fig_dc_ne_cfg_01043201), users access Device A and Device B through a LAN switch. The two devices run VRRP to determine the master/backup status. Basic user access functions are configured on Device A and Device B, allowing the users to go online through the master device. If the master device or the link on the network or user side of the master device fails, service traffic needs to be quickly switched to the backup device.

**Figure 1** Example for configuring multicast dual-device hot backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/2, respectively.


  
![](images/fig_dc_ne_cfg_rui_000003.png)  

| Device | Interface | IP Address |
| --- | --- | --- |
| Device A | Eth-Trunk3.4001 | 192.168.254.2/29 |
| Device A | Loopback0 | 172.20.1.1/32 |
| Device A | Loopback10 | 172.20.1.3/32 |
| Device A | GE 0/1/0 | 172.20.0.33/30 |
| Device A | GE 0/2/2 | 172.20.0.57/30 |
| Device B | Eth-Trunk3.4001 | 192.168.254.3/29 |
| Device B | Loopback0 | 172.20.1.1/32 |
| Device B | Loopback10 | 172.20.1.2/32 |
| Device B | GE 0/1/0 | 172.20.0.37/30 |
| Device B | GE 0/2/2 | 172.20.0.61/30 |





#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interfaces and assign IP addresses to them.
2. Establish a multi-device backup platform.
3. Configure IP address pool binding.
4. Bind an RBP to an interface through which the user goes online.
5. Configure routes to ensure IP connectivity between devices. For details, see "IP Routing" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide*.

#### Data Preparation

To complete the configuration, you need the following data:

* VRRP ID
* Interface IP addresses of Routers that back up each other
* Backup ID, which works together with an RBS to identify an RBP to which users belong

#### Procedure

1. Configure interfaces for connecting Device A to the LAN switch, and assign IP addresses to them.
   
   
   
   The configuration on Device A is used as an example. The configuration of Device B is similar to that ofDevice A.
   
   ```
   [~DeviceA] interface GigabitEthernet0/1/3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] description ToJiaohuanji 
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
   [~DeviceA] interface Eth-Trunk3
   ```
   ```
   [*DeviceA-Eth-Trunk3] description ToJiaohuanji 
   ```
   ```
   [*DeviceA-Eth-Trunk3] commit 
   ```
   ```
   [~DeviceA-Eth-Trunk3] quit 
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
2. Configure the loopback address of Device A.
   
   
   
   The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   ```
   [~DeviceA] interface loopback10
   ```
   ```
   [*DeviceA-loopback10] ip address 172.20.1.3 255.255.255.255
   ```
   ```
   [*DeviceA-loopback10] commit 
   ```
   ```
   [~DeviceA-loopback10] quit 
   ```
   ```
   [~DeviceA] interface loopback0
   ```
   ```
   [*DeviceA-loopback0] ip address 172.20.1.1 255.255.255.255
   ```
   ```
   [*DeviceA-loopback0] commit 
   ```
   ```
   [~DeviceA-loopback0] quit 
   ```
3. Establish a multi-device backup platform. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, only the RUI-related configuration is described. For other configurations, see the corresponding configuration guide.
   
   # Configure a BFD session named **bfd** on the access side to rapidly detect interface or link faults and trigger a master/backup VRRP switchover. 192.168.254.3 is the IP address of Eth-Trunk 3.4001 on Device B.
   
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
   [*DeviceA-bfd-session-bfd] discriminator local 2 
   ```
   ```
   [*DeviceA-bfd-session-bfd] discriminator remote 3 
   ```
   ```
   [*DeviceA-bfd-session-bfd] commit 
   ```
   ```
   [~DeviceA-bfd-session-bfd] quit 
   ```
   
   # Configure a VRRP group on Eth-Trunk 3.4001, and configure the VRRP group to track the BFD session and network-side interface.
   
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
   [*DeviceA-Eth-Trunk3.4001] vrrp recover-delay 20
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
   [*DeviceA-rm-backup-rbs_qhmd] track interface GigabitEthernet0/1/0
   ```
   ```
   [*DeviceA-rm-backup-rbs_qhmd] track interface GigabitEthernet0/2/2
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
   [*DeviceA-rm-backup-prf-rbp3] service-type multicast 
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
   [~DeviceA-rm-backup-prf-rbp3] quit 
   ```
4. Configure IP address pool binding. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   
   
   # Configure an address pool.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] ip pool dmtjs_xi bas local
   ```
   ```
   [*DeviceA-ip-pool-dmtjs_xi] gateway 192.168.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-ip-pool-dmtjs_xi] section 0 192.168.1.2 192.168.1.254 
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
   
   # Bind the address pool.
   
   ```
   [~DeviceA] remote-backup-service rbs_qhmd
   ```
   ```
   [*DeviceA-rm-backup-service rbs_qhmd] ip-pool dmtjs_xi
   ```
   ```
   [*DeviceA-rm-backup-service rbs_qhmd] commit 
   ```
   ```
   [~DeviceA-backup-service rbs_qhmd] quit
   ```
5. Configure a RADIUS server group.
   
   
   ```
   [~DeviceA-aaa] radius-server group rd
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
   [*DeviceA-aaa]  authentication-scheme wu
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
   [*DeviceA-aaa]  domain dmtjs_xi
   ```
   ```
   [*DeviceA-aaa-dmtjs_xi] authentication-scheme wu
   ```
   ```
   [*DeviceA-aaa-dmtjs_xi] accounting-scheme wu
   ```
   ```
   [*DeviceA-aaa-dmtjs_xi] ip-pool dmtjs_xi
   ```
   ```
   [*DeviceA-aaa-dmtjs_xi] radius-server group rd
   ```
   ```
   [*DeviceA-aaa-dmtjs_xi] commit
   ```
   ```
   [~DeviceA-aaa-dmtjs_xi] quit
   ```
7. Bind the RBP to Eth-Trunk 3.501 from which users go online. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   
   ```
   [~DeviceA] interface Eth-Trunk3.501
   ```
   ```
   [*DeviceA-Eth-Trunk3.501] user-vlan 501
   ```
   ```
   [*DeviceA-Eth-Trunk3.501-vlan-501-501] remote-backup-profile rbp3 
   ```
   ```
   [*DeviceA-Eth-Trunk3.501-vlan-501-501] bas
   ```
   ```
   [*DeviceA-Eth-Trunk3.501-bas] access-type layer2-subscriber default-domain authentication dmtjs_xi
   ```
   ```
   [*DeviceA-Eth-Trunk3.501-bas] multicast copy by-session
   ```
   ```
   [*DeviceA-Eth-Trunk3.501-bas] authentication-method bind
   ```
   ```
   [*DeviceA-Eth-Trunk3.501-bas] commit 
   ```
   ```
   [~DeviceA-Eth-Trunk3.501-bas] quit 
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
9. Configure multicast.
   
   
   
   # Enable multicast globally. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   ```
   [~DeviceA] multicast routing-enable
   ```
   ```
   [*DeviceA] commit 
   ```
   
   # Enable PIM on the network-side interface. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   ```
   [~DeviceA] interface GigabitEthernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 172.20.0.33 255.255.255.252
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit 
   ```
   ```
   [~DeviceA] interface GigabitEthernet0/2/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/2] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/2] ip address 172.20.0.61 255.255.255.252
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/2] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/2] commit 
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/2] quit 
   ```
   
   # Enable IGMP and PIM on the access-side interface. The configuration on Device A is used as an example. The configuration of Device B is similar to that of Device A.
   
   ```
   [~DeviceA] interface Eth-Trunk3.501
   ```
   ```
   [*DeviceA-Eth-Trunk3.501] pim sm
   ```
   ```
   [*DeviceA-Eth-Trunk3.501] igmp enable
   ```
   ```
   [*DeviceA-Eth-Trunk3.501] commit 
   ```
   ```
   [~DeviceA-Eth-Trunk3.501] quit 
   ```
   
   # Configure an RP.
   
   ```
   [~DeviceA] pim
   ```
   ```
   [*DeviceA-pim] static-rp 192.168.2.2
   ```
   ```
   [*DeviceA-pim] commit 
   ```
10. Verify the configuration.
    
    
    
    View the master/backup status of VRRP. On Device A, **Master** is displayed and the BFD session is in the **UP** state. **Backup** should be displayed on Device B.
    
    ```
    <DeviceA> display vrrp
    ```
    ```
      Eth-Trunk3.4001 | Virtual Router 3
        State : Master
        Virtual IP : 192.168.254.1
        Master IP : 192.168.254.2 
        Local IP : 192.168.254.3 
        PriorityRun : 120
        PriorityConfig : 120
        MasterPriority : 120
        Preempt : YES   Delay Time : 1200s
        Hold Multiplier : 4
        TimerRun : 1 s
        TimerConfig : 1 s
        Auth Type : NONE
        Virtual Mac :  00e0-fc12-3456
        Check TTL : YES
        Config type : admin-vrrp
        Track IF :   Eth-Trunk3.4001   Priority reduced : 30
        IF State : UP
        Config track link-bfd down-number : 0
        Track BFD : 1  Type: peer
        BFD-session state : UP
        Create time : 2016-05-05 09:05:17
        Last change time : 2016-05-05 09:14:38    
    ```
    ```
    <DeviceB> display vrrp
    ```
    ```
        Eth-Trunk3.4001 | Virtual Router 3
        State : Backup
        Virtual IP : 192.168.254.1
        Master IP : 192.168.254.3
        Local IP : 192.168.254.2
        PriorityRun : 100
        PriorityConfig : 100
        MasterPriority : 120
        Preempt : YES   Delay Time : 1200s
        Hold Multiplier : 4
        TimerRun : 1 s
        TimerConfig : 1 s
        Auth Type : NONE
        Virtual Mac :  00e0-fc12-3456
        Check TTL : YES
        Config type : admin-vrrp
        Track IF : Eth-Trunk3.4001  Priority reduced : 30
        IF State : UP
        Config track link-bfd down-number : 0
        Track BFD : 2  Type: peer
        BFD-session state : UP
        Create time : 2016-05-05 09:11:48
        Last change time : 2016-05-05 09:11:54    
    ```
    
    When multicast hot backup is successfully configured, you can view that the backup service type is **bras multicast**, IGMP packet replication is enabled, Device A is in the **Master** state, and Device B is in the **Slave** state.
    
    ```
    <DeviceA> display remote-backup-profile rbp3
    ```
    ```
     -----------------------------------------------
     Profile-Index        : 0x801
     Profile-Name         : rbp3
     Service              : bras multicast
     Remote-backup-service: rbs_qhmd
     Backup-ID            : 3
     track protocol       : VRRP
     VRRP-ID              : 3
     VRRP-Interface       : Eth-Trunk3.4001
     Interface            :
                           Eth-Trunk3.501
     State                : Master
     Peer State           : slave
     Backup mode          : hot
     Slot-Number          : 2
     Card-Number          : 1
     Port-Number          : 0
     Traffic threshold    : 50(MB)
     Traffic interval     : 10(minutes)
     dhcp-stb igmp-copy enable 
    ```
    ```
    <DeviceB> display remote-backup-profile rbp3
    ```
    ```
     -----------------------------------------------
     Profile-Index        : 0x800
     Profile-Name         : rbp3
     Service              : bras multicast
     Remote-backup-service: rbs_qhmd
     Backup-ID            : 3
     track protocol       : VRRP
     VRRP-ID              : 1
     VRRP-Interface       : Eth-Trunk3.4001
     Interface            :
                            Eth-Trunk3.501
     State                : Slave
     Peer State           : master
     Backup mode          : hot
     Slot-Number          : 2
     Card-Number          : 0
     Port-Number          : 0
     Traffic threshold    : 50(MB)
     Traffic interval     : 10(minutes)
     dhcp-stb igmp-copy enable  
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
  vlan batch 2 to 9 11 to 504 506 to 3999 4001 to 4094
  ```
  ```
  #
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
  static-rp 192.168.2.2
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
    authentication-scheme wu
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
  description ToJiaohuanji
  ```
  ```
  undo shutdown
  #
  ```
  ```
  interface Eth-Trunk3
   description ToJiaohuanji
  #
  ```
  ```
  interface Eth-Trunk3.4001
  ```
  ```
   encapsulation 4001 dot1q-termination
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
   vrrp recover-delay 20
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
   pim sm
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
   pim sm
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
   ip-pool dmtjs_xi
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
   service-type multicast 
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
  #
  ```
  ```
  interface Eth-Trunk3.501
  ```
  ```
   user-vlan 501 
  ```
  ```
   remote-backup-profile rbp3 
  ```
  ```
   pim sm 
  ```
  ```
   igmp enable
  ```
  ```
   bas 
  ```
  ```
  access-type layer2-subscriber default-domain authentication dmtjs_xi
  ```
  ```
   multicast copy  by-session
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
  vlan batch 2 to 9 11 to 504 506 to 3999 4001 to 4094
  ```
  ```
  #
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
  static-rp 192.168.2.2
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
  ip pool pool1 bas local rui-slave
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
  radius-server group rd 
   radius-server authentication 10.7.66.66 1812 weight 0 
   radius-server accounting 10.7.66.66 1813 weight 0 
   radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^% 
   radius-server retransmit 2 
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
   authentication-scheme wu
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
  description ToJiaohuanji
  ```
  ```
  undo shutdown
  #
  ```
  ```
  interface Eth-Trunk3
   description ToJiaohuanji
  #
  ```
  ```
  interface Eth-Trunk3.4001
  ```
  ```
   encapsulation 4001 dot1q-termination
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
   ip address 172.20.1.1 255.255.255.255
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
   pim sm 
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
   ip address 172.20.0.65 255.255.255.252
  ```
  ```
   pim sm 
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
   ip-pool pool1
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
   service-type multicast 
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
  #
  ```
  ```
  interface Eth-Trunk3.501
  ```
  ```
   user-vlan 501 
  ```
  ```
   remote-backup-profile rbp3 
  ```
  ```
   pim sm
  ```
  ```
  igmp enable
  ```
  ```
   bas 
  ```
  ```
  access-type layer2-subscriber default-domain authentication dmtjs_xi
  ```
  ```
   multicast copy  by-session
  ```
  ```
   authentication-method bind 
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