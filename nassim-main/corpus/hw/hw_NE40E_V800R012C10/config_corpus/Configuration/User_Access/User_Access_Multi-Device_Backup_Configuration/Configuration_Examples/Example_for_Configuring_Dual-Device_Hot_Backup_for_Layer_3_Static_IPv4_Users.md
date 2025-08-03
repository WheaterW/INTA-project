Example for Configuring Dual-Device Hot Backup for Layer 3 Static IPv4 Users
============================================================================

This section provides an example for configuring dual-device hot backup for Layer 3 static IPv4 users.

#### Usage Scenario

High reliability is a basic requirement for carrier-class devices.

The NE40E is an edge service aggregation router that carries multiple services. It plays a vital role on a network. It is uplinked to the core layer to implement the Layer 3 routing function and downlinked to the aggregation layer to terminate Layer 2 user packets for user access. Additionally, it carries Triple Play services â HSI, VoIP, and IPTV â which require high reliability. The NE40E provides service-level high-reliability technologies. Non-stop data flow forwarding does not mean that user services are not interrupted. If a network node or link fails, user traffic is switched to a backup device. If user information is not synchronized to the backup device, user services are still interrupted. To prevent this problem, dual-device hot backup is introduced.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172374419__fig_dc_ne_cfg_rui_005701), users access PE1 and PE2 through a CE. An Eth-Trunk interface is configured on each PE, and the two PEs are directly connected. A VRRP group is configured on PE1 and PE2 to track the status of Eth-Trunk member interfaces. Access links are bundled on the CE, and LACP is deployed to determine the primary and backup links between the PEs. Services can be immediately switched to the backup device if the master device fails after users go online. DeviceA functions as a DHCP relay agent and obtains an IP address from the DHCP server. A static route destined for the Internet is configured on DeviceA (layer 3 device), with the next hop being the IP address of the Layer 3 BAS interface. The primary/backup status of the static routes destined for PE1 and PE2 is controlled by priority.

**Figure 1** Network diagram of configuring dual-device hot backup for Layer 3 static IPv4 users![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 7 represent GE0/1/0, GE0/1/1, GE0/1/5, GE0/2/0, GE0/2/3, GE0/1/6, and GE0/1/7, respectively.


  
![](images/fig_dc_ne_cfg_rui_005701.png)

| **Device** | **Interface** | **IP Address** |
| --- | --- | --- |
| PE1 | GE 0/1/0 | Member interface of Eth-Trunk 10, which is the BAS main interface  (Note: It is recommended that Layer 2 and Layer 3 users not share the same main interface.) |
| PE1 | GE0/1/1 | 10.1.1.1/24 (network-side interface) |
| PE1 | GE0/1/5 | 10.193.2.2/24 (address of the interface running VRRP) |
| PE1 | Loopback1 | 172.16.18.1/32 (address of PE1's interface with an RBS deployed) |
| PE2 | GE0/1/0 | Member interface of Eth-Trunk 10, which is the BAS main interface  (Note: It is recommended that Layer 2 and Layer 3 users not share the same main interface.) |
| PE2 | GE0/1/1 | 10.1.1.2/24 (network-side interface) |
| PE2 | GE0/1/5 | 10.193.2.1/24 (address of the interface running VRRP) |
| PE2 | Loopback2 | 172.16.18.2/32 (address of PE2's interface with an RBS deployed) |
| CE | GE0/2/0 | Associate PE1 with VRRP |
| CE | GE0/2/3 | Associate PE2 with VRRP |
| CE | GE0/1/6 | Layer 2 transparent transmission |
| DeviceA | GE0/1/6 | 10.10.3.1/24 |
| DeviceA | GE0/1/7 | 10.10.8.1/24 |





#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic user access functions and ensure that the two devices for backup have the same configuration. For details, see *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - User Access*.
2. Configure Eth-Trunk interfaces to work in static LACP mode. For details, see *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - LAN Access and MAN Access*.
3. Configure an mVRRP group.
4. Configure VRRP to track the interface status on the PEs.
5. Associate the Eth-Trunk interfaces working in static LACP mode on the PEs with the mVRRP group.

#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters (VRRP ID)
* IP address of each interface on PE1 and PE2
* Backup ID, which works together with an RBS to identify an RBP to which users belong
* IP address (192.168.1.2) of the DHCP server connected to DeviceA
* IP address (192.168.8.251) of the web server and IP address (192.168.8.55) of the RADIUS server to which PE1 and PE2 connect
* User access parameters

#### Procedure

1. User access configuration
   
   
   
   For details, see *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - User Access - AAA and User Management Configuration*. For configuration details, see the configuration files.
2. Configure Eth-Trunk interfaces to work in static LACP mode and add member interfaces GE 0/2/0 and GE 0/2/3 to the Eth-Trunk interfaces.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] vlan batch 1 10
   ```
   ```
   [*CE1] interface Eth-Trunk 20
   ```
   ```
   [*CE1-Eth-Trunk20] mode lacp-static
   ```
   ```
   [*CE1-Eth-Trunk20] lacp timeout fast
   ```
   ```
   [*CE1-Eth-Trunk20] trunkport gigabitethernet 0/2/0
   ```
   ```
   [*CE1-Eth-Trunk20] trunkport gigabitethernet 0/2/3
   ```
   ```
   [*CE1-Eth-Trunk20] Port trunk allow-pass vlan 1 10
   ```
   ```
   [*CE1-Eth-Trunk20] commit
   ```
   ```
   [~CE1-Eth-Trunk20] quit
   ```
   ```
   [~CE1] interface gigabitethernet 0/1/6
   [~CE1-Gigabitethernet0/1/6] Portswich
   [*CE1-Gigabitethernet0/1/6] Port trunk allow-pass vlan 1 10
   [*CE1-Gigabitethernet0/1/6] commit
   [~CE1-Gigabitethernet0/1/6] quit
   ```
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] interface Eth-Trunk 10
   ```
   ```
   [*PE1-Eth-Trunk10] mac-address 00e0-fc12-3456
   ```
   ```
   [*PE1-Eth-Trunk10] mode lacp-static
   ```
   ```
   [*PE1-Eth-Trunk10] lacp timeout fast
   ```
   ```
   [*PE1-Eth-Trunk10] trunkport gigabitethernet 0/1/0
   ```
   ```
   [*PE1-Eth-Trunk10] commit
   ```
   ```
   [~PE1-Eth-Trunk10] quit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface Eth-Trunk 10
   ```
   ```
   [*PE2-Eth-Trunk10] mac-address 00e0-fc12-3456
   ```
   ```
   [*PE2-Eth-Trunk10] mode lacp-static
   ```
   ```
   [*PE2-Eth-Trunk10] lacp timeout fast
   ```
   ```
   [*PE2-Eth-Trunk10] trunkport gigabitethernet 0/1/0
   ```
   ```
   [*PE2-Eth-Trunk10] commit
   ```
   ```
   [~PE2-Eth-Trunk10] quit
   ```
3. Configure an IP address for the interface on DeviceA.
   
   
   
   # Configure an address for the interface that connects DeviceA to users and configure the DHCP relay function.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface gigabitethernet 0/1/7
   [*DeviceA-GigabitEthernet0/1/7] ip address 10.10.8.1 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/7] ip relay address 192.168.1.2
   [*DeviceA-GigabitEthernet0/1/7] dhcp select relay
   [*DeviceA-GigabitEthernet0/1/7] commit
   [~DeviceA-GigabitEthernet0/1/7] quit
   ```
   
   # Configure an IP address for the interface that connects DeviceA to the CE. The IP address must be on the same network segment as the IP address of the BAS interface.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/6.1
   [*DeviceA-GigabitEthernet0/1/6.1] ip address 10.10.10.3 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/6.1] vlan-type dot1q 1
   [*DeviceA-GigabitEthernet0/1/6.1] commit
   [~DeviceA-GigabitEthernet0/1/6.1] quit
   ```
4. On DeviceA, configure a static route with the next-hop address being the IP address of a Layer 3 BAS interface.
   
   
   ```
   [~DeviceA] ip route-static 10.1.1.1 24 10.10.10.1 preference 30
   [*DeviceA] ip route-static 10.1.1.2 24 10.10.10.2 preference 40
   [*DeviceA] commit
   ```
5. Configure an mVRRP group.
   
   
   
   # Configure an IP address for the specified GE interface, and set the priority of PE1 in the VRRP group to 120 (as the master device).
   
   ```
   [~PE1] interface Gigabitethernet 0/1/5
   ```
   ```
   [*PE1-Gigabitethernet0/1/5] undo shutdown
   ```
   ```
   [*PE1-Gigabitethernet0/1/5] ip address 10.193.2.2 255.255.255.0
   ```
   ```
   [*PE1-Gigabitethernet0/1/5] vrrp vrid 120 virtual-ip 10.193.2.100
   ```
   ```
   [*PE1-Gigabitethernet0/1/5] vrrp vrid 120 priority 120
   ```
   ```
   [*PE1-Gigabitethernet0/1/5] admin-vrrp vrid 120 ignore-if-down
   ```
   ```
   [*PE1-Gigabitethernet0/1/5] commit
   ```
   
   # Configure an IP address for the specified GE interface, and set the priority of PE2 in the VRRP group to the default value (as the backup device).
   
   ```
   [~PE2] interface Gigabitethernet 0/1/5
   ```
   ```
   [*PE2-Gigabitethernet0/1/5] undo shutdown
   ```
   ```
   [*PE2-Gigabitethernet0/1/5] ip address 10.193.2.1 255.255.255.0
   ```
   ```
   [*PE2-Gigabitethernet0/1/5] vrrp vrid 120 virtual-ip 10.193.2.100
   ```
   ```
   [*PE2-Gigabitethernet0/1/5] admin-vrrp vrid 120 ignore-if-down
   ```
   ```
   [*PE2-Gigabitethernet0/1/5] commit
   ```
6. Configure the VRRP group to track the interface status.
   
   
   
   # Configure VRRP on PE1 to track the interface status.
   
   ```
   [~PE1-Gigabitethernet0/1/5] vrrp vrid 120 track interface Gigabitethernet 0/1/0 reduced 40
   ```
   ```
   [*PE1-Gigabitethernet0/1/5] vrrp vrid 120 track interface Gigabitethernet 0/1/1 reduced 40
   ```
   ```
   [*PE1-Gigabitethernet0/1/5] commit
   ```
   ```
   [~PE1-Gigabitethernet0/1/5] quit
   ```
   
   # Configure VRRP on PE2 to track the interface status.
   
   ```
   [~PE2-Gigabitethernet0/1/5] vrrp vrid 120 track interface Gigabitethernet 0/1/1 reduced 40
   ```
   ```
   [*PE2-Gigabitethernet0/1/5] vrrp vrid 120 track interface Gigabitethernet 0/1/0 reduced 40
   ```
   ```
   [*PE2-Gigabitethernet0/1/5] commit
   ```
   ```
   [~PE2-Gigabitethernet0/1/5] quit
   ```
7. Associate the Eth-Trunk interfaces working in static LACP mode with the mVRRP group.
   
   
   
   # Associate PE1's Eth-Trunk interface working in static LACP mode with the mVRRP group.
   
   ```
   [~PE1] interface Eth-Trunk 10
   ```
   ```
   [*PE1-Eth-Trunk 10] lacp track vrrp vrid 120 interface Gigabitethernet 0/1/5
   ```
   ```
   [*PE1-Eth-Trunk 10] commit
   ```
   ```
   [~PE1-Eth-Trunk 10] quit
   ```
   
   # Associate PE2's Eth-Trunk interface working in static LACP mode with the mVRRP group.
   
   ```
   [~PE2] interface Eth-Trunk 12
   ```
   ```
   [*PE2-Eth-Trunk 12] lacp track vrrp vrid 120 interface Gigabitethernet 0/1/5
   ```
   ```
   [*PE2-Eth-Trunk 12] commit
   ```
   ```
   [~PE2-Eth-Trunk 12] quit
   ```
8. Configure an RBS, address pool, and RBP. (PE1 is used as an example.)
   
   
   
   # Configure an RBS named s1.
   
   ```
   [~PE1] remote-backup-service s1
   ```
   ```
   [*PE1-rm-backup-srv-s1] peer 172.16.18.1 source 172.16.18.2 port 12012
   ```
   ```
   [*PE1-rm-backup-srv-s1] track interface GigabitEthernet 0/1/1
   ```
   ```
   [*PE1-rm-backup-srv-s1] commit
   ```
   ```
   [~PE1-rm-backup-srv-s1] quit
   ```
   
   # Configure an RBP named p1.
   
   ```
   [~PE1] remote-backup-profile p1
   ```
   ```
   [*PE1-rm-backup-prf-p1] service-type bras
   ```
   ```
   [*PE1-rm-backup-prf-p1] backup-id 1 remote-backup-service s1
   ```
   ```
   [*PE1-rm-backup-prf-p1] peer-backup hot
   ```
   ```
   [*PE1-rm-backup-prf-p1] vrrp-id 120 interface gigabitethernet 0/1/5
   ```
   ```
   [*PE1-rm-backup-prf-p1] commit
   ```
   ```
   [~PE1-rm-backup-prf-p1] quit
   ```
9. Configure user-side interfaces.
   
   
   
   # Configure PE1.
   
   # Configure Layer 3 static users to be triggered to go online through IP packets.
   
   ```
   [~PE1] layer3-subscriber 10.0.0.2 10.0.0.254 domain-name pre
   ```
   ```
   [*PE1] interface Eth-Trunk 10.1
   ```
   ```
   [*PE1-Eth-Trunk 10.1] vlan-type dot1q 10
   ```
   ```
   [*PE1-Eth-Trunk 10.1] ip address 10.10.10.1 255.255.255.0
   ```
   ```
   [*PE1-Eth-Trunk 10.1] remote-backup-profile p1
   ```
   ```
   [*PE1-Eth-Trunk 10.1] bas
   ```
   ```
   [*PE1-Eth-Trunk 10.1-bas] access-type layer3-subscriber default-domain pre-authentication pre authentication huawei
   ```
   ```
   [*PE1-Eth-Trunk 10.1-bas] commit
   ```
   
   
   
   # Configure PE2.
   
   # Configure Layer 3 static users to be triggered to go online through IP packets.
   
   ```
   [~PE2] layer3-subscriber 10.0.0.2 10.0.0.254 domain-name pre
   ```
   ```
   [*PE2] interface Eth-Trunk 10.1
   ```
   ```
   [*PE2-Eth-Trunk 10.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-Eth-Trunk 10.1] ip address 10.10.10.2 255.255.255.0
   ```
   ```
   [*PE2-Eth-Trunk 10.1] remote-backup-profile p1
   ```
   ```
   [*PE2-Eth-Trunk 10.1] bas
   ```
   ```
   [*PE2-Eth-Trunk 10.1-bas] access-type layer3-subscriber default-domain pre-authentication pre authentication huawei
   ```
   ```
   [*PE2-Eth-Trunk 12.1-bas] commit
   ```
10. Verify the configuration.
    
    
    
    After completing the configurations, run the following command. The command output shows that the status of PE1 is **Master** and that of PE2 is **Slave**.
    
    ```
    <PE1> display remote-backup-profile p1
    ```
    ```
    -----------------------------------------------
     Profile-Index        : 0x1000
     Profile-Name         : p1
     Service              : bras 
     Remote-backup-service: s1
     Backup-ID            : 1
     track protocol       : VRRP
     VRRP-ID              : 120
     VRRP-Interface       : GigabitEthernet0/1/5
     Access-Control       : --
     State                : Slave
     Peer State           : Master
     Interface            :
                            Eth-Trunk10.1
     Backup mode          : hot
     Slot-Number          : --
     Card-Number          : --
     Port-Number          : --
     Traffic threshold    : 50(MB)
     Traffic interval     : 10(minutes)
     IP-Pool              :
                            ln
     Forwarding Configured: Slave Forwarding 
    ```
    ```
    <PE1> display remote-backup-service S1
    ```
    ```
    ----------------------------------------------------------
     Service-Index    : 1
     Service-Name     : s1
     TCP-State        : Connected
     Peer-ip          : 172.16.18.2
     Source-ip        : 172.16.18.1
     TCP-Port         : 12012
     Track-BFD        : -
     SSL-Policy-Name  : --
     SSL-State        : --
     Last up time     : 2016-08-02 15:34:36
     Track-interface0 : GigabitEthernet0/1/1
                        Weight : 10
     Uplink state     : 2 (1:DOWN 2:UP)
     Domain-map-list  : --
     Send Q pkt count : 0
    ----------------------------------------------------------
    
     ip pool:  
     ipv6 pool:  
     Failure ratio    : 100%
     Failure duration : 0 min
     pool route status: 2
     switch mark      : 2
    ```

#### Configuration Files

* CE configuration file
  ```
  #
  sysname CE1
  #
  vlan batch 1 10
  #
  interface Eth-Trunk 20
   mode lacp-static
   lacp timeout fast
   trunkport gigabitethernet 0/2/0
   trunkport gigabitethernet 0/2/3
   Port trunk allow-pass vlan 1 10
  #
  interface gigabitethernet 0/1/6
   portswich
   port trunk allow-pass vlan 1 10
  #
  return
  ```
* DeviceA configuration file
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/6
   undo shutdown
  #
  interface GigabitEthernet0/1/6.1
   vlan-type dot1q 1
   ip address 10.10.10.3 255.255.255.0
  #
  interface GigabitEthernet0/1/7
   undo shutdown
   ip address 10.10.8.1 255.255.255.0
   dhcp select relay
   ip relay address 192.168.1.2
  #
  ip route-static 10.1.1.1 24 10.10.10.1 preference 30
  ip route-static 10.1.1.2 24 10.10.10.2 preference 40
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  radius-server group rd1
   radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
   radius-server authentication 192.168.8.55 1645 weight 0
   radius-server accounting 192.168.8.55 1646 weight 0
   radius-server source interface LoopBack 0      
  #
  user-group web-before
  #
  acl number 6000
   rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0 
   rule 10 permit ip source ip-address 192.168.8.251 0 destination user-group web-before
  #
  acl number 6001
   rule 5 permit tcp source user-group web-before destination-port eq www
   rule 10 permit tcp source user-group web-before destination-port eq 8080
  #
  acl number 6002
   rule 5 permit ip source ip-address any destination user-group web-before
   rule 10 permit ip source user-group web-before destination ip-address any
  #
  traffic classifier redirect operator or
   if-match acl 6001 precedence 18
  #
  traffic classifier web_deny operator or
   if-match acl 6002 precedence 20
  #
  traffic classifier web_permit operator or
   if-match acl 6000 precedence 1 
  #
  traffic behavior redirect
   http-redirect
  #
  traffic behavior web_deny
   deny
  #
  traffic behavior web_permit
  #
  traffic policy web
   share-mode
   classifier redirect behavior redirect precedence 2
   classifier web_permit behavior web_permit precedence 4
   classifier web_deny behavior web_deny precedence 5
  #
  aaa
   authentication-scheme none
    authentication-mode none
   #
   authentication-scheme auth2  
   #
   accounting-scheme none
    accounting-mode none
   #
   accounting-scheme acct2 
   #
   domain huawei 
    authentication-scheme auth2
    accounting-scheme acct2
    radius-server group rd1 
   # 
   domain pre
    authentication-scheme none
    accounting-scheme none
    user-group web-before
    web-server 192.168.8.251
    web-server url http://www.isp1.com
    web-server identical-url
  #
  remote-backup-service s1
   peer 172.16.18.1 source 172.16.18.2 port 12012
   track interface GigabitEthernet0/1/1 
  #
  remote-backup-profile p1
   service-type bras
   backup-id 1 remote-backup-service s1
   peer-backup hot
   vrrp-id 120 interface GigabitEthernet0/1/5
  #
  layer3-subscriber 10.0.0.2 10.0.0.254 domain-name pre
  #
  interface Loopback1
  undo shutdown
  ip address 172.16.18.1 255.255.255.0
  #
  interface Eth-Trunk10
   mac-address 00e0-fc12-3456
   mode lacp-static
   lacp timeout fast
   lacp track vrrp vrid 120 interface GigabitEthernet0/1/5
  #
  interface Eth-Trunk 10.1
   vlan-type dot1q 10
   ip address 10.10.10.1 255.255.255.0
   remote-backup-profile p1
   bas
   #
    access-type layer3-subscriber default-domain pre-authentication pre authentication huawei
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
   dcn
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/5
   undo shutdown
   ip address 10.193.2.2 255.255.255.0
   vrrp vrid 120 virtual-ip 10.193.2.100
   admin-vrrp vrid 120 ignore-if-down
   vrrp vrid 120 priority 120
   vrrp vrid 120 track interface GigabitEthernet0/1/0 reduced 40
   vrrp vrid 120 track interface GigabitEthernet0/1/1 reduced 40
   dcn
  #
  web-auth-server enable
  web-auth-server source interface LoopBack 0
  web-auth-server 192.168.8.251 port 50100 key cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
  #
  undo web-auth-server source-ip all
  web-auth-server source-ip 192.168.8.251
  #
  traffic-policy web inbound
  #
  ospf 1 
   default cost inherit-metric
   import-route direct
   import-route unr
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  radius-server group rd1
   radius-server shared-key-cipher %^%#0Iy%9Gu1),kLlP/jw;X-AOiZD%{YoCH<RC(P*>^5%^%#
   radius-server authentication 192.168.8.55 1645 weight 0
   radius-server accounting 192.168.8.55 1646 weight 0
   radius-server source interface LoopBack 0 
  #
  user-group web-before
  #
  acl number 6000
   rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0 
   rule 10 permit ip source ip-address 192.168.8.251 0 destination user-group web-before
  #
  acl number 6001
   rule 5 permit tcp source user-group web-before destination-port eq www
   rule 10 permit tcp source user-group web-before destination-port eq 8080
  #
  acl number 6002
   rule 5 permit ip source ip-address any destination user-group web-before
   rule 10 permit ip source user-group web-before destination ip-address any
  #
  traffic classifier redirect operator or
   if-match acl 6001 precedence 18
  #
  traffic classifier web_deny operator or
   if-match acl 6002 precedence 20
  #
  traffic classifier web_permit operator or
   if-match acl 6000 precedence 1 
  #
  traffic behavior redirect
   http-redirect
  #
  traffic behavior web_deny
   deny
  #
  traffic behavior web_permit
  #
  traffic policy web
   share-mode
   classifier redirect behavior redirect precedence 2
   classifier web_permit behavior web_permit precedence 4
   classifier web_deny behavior web_deny precedence 5
  #
  aaa
   authentication-scheme none
    authentication-mode none
   #
   authentication-scheme auth2  
   #
   accounting-scheme none
    accounting-mode none
   #
   accounting-scheme acct2 
   #
   domain huawei 
    authentication-scheme auth2
    accounting-scheme acct2
    radius-server group rd1
   #  
   domain pre
    authentication-scheme none
    accounting-scheme none
    user-group web-before
    web-server 192.168.8.251
    web-server url http://www.isp1.com
    web-server identical-url  
  #
  remote-backup-service s2
   peer 172.16.18.2 source 172.16.18.1 port 12012
   track interface GigabitEthernet0/1/1 
  #
  remote-backup-profile p1
   service-type bras
   backup-id 1 remote-backup-service s2
   peer-backup hot
   vrrp-id 120 interface GigabitEthernet0/1/5
  #
  layer3-subscriber 10.0.0.2 10.0.0.254 domain-name pre
  #
  interface Loopback1
   undo shutdown
   ip address 172.16.18.2 255.255.255.0
  #
  interface Eth-Trunk10
   mac-address 00e0-fc12-3456
   mode lacp-static
   lacp timeout fast
   lacp track vrrp vrid 120 interface GigabitEthernet0/1/5
  #
  interface Eth-Trunk 10.1
   vlan-type dot1q 10
   ip address 10.10.10.2 255.255.255.0
   remote-backup-profile p1
   bas
   #
    access-type layer3-subscriber default-domain pre-authentication pre authentication huawei
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
   dcn
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/5
   undo shutdown
   ip address 10.193.2.1 255.255.255.0
   vrrp vrid 120 virtual-ip 10.193.2.100
   admin-vrrp vrid 120 ignore-if-down
   vrrp vrid 120 track interface GigabitEthernet0/1/0 reduced 40
   vrrp vrid 120 track interface GigabitEthernet0/1/1 reduced 40
   dcn
  #
  web-auth-server enable
  web-auth-server source interface LoopBack 0
  web-auth-server 192.168.8.251 port 50100 key cipher %^%#aQL6,Ua<|@sxPQK/1f'4/GBJ6,6)q>$Z^7*,!2yR%^%#
  #
  undo web-auth-server source-ip all
  web-auth-server source-ip 192.168.8.251
  #
  traffic-policy web inbound
  #
  ospf 1
   default cost inherit-metric
   import-route direct
   import-route unr
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  return
  ```