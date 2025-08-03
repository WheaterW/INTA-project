Example for Configuring IPoE Dual-Stack User Access (ND Unshared+PD) in a Dual-Device Hot Backup Scenario with a Remote Address Pool Deployed
=============================================================================================================================================

In a dual-device hot backup scenario, dual-stack users connect to the master and backup BRASs using IPoE. The BRASs assign IPv6 addresses to the users in ND unshared+PD mode to implement user access.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001121618340__fig_dc_ne_cfg_rui_003101), users access BRAS1 and BRAS2 through SW1 (LAN switch). VRRP runs on BRAS1 and BRAS2 to implement master/backup switchover protection.

RADIUS authentication and accounting are configured on the BRASs. The BRASs use a remote address pool to assign IPv4 addresses to users, use DHCPv6 IA\_PD to assign the IPv6 prefixes to be used on the network to users, and use DHCPv6 ND to assign IPv6 addresses to users.

**Figure 1** Configuring IPoE dual-stack user access (ND unshared+PD) in a dual-device hot backup scenario with a remote address pool deployed![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001168538003.png)

**Table 1** Interfaces and IP addresses
| **Device** | **Interface Name** | **Interface Number** | **IP Address** |
| --- | --- | --- | --- |
| BRAS1 | interface1 | GE0/1/0.1 | 192.168.1.1 |
| interface1 | GE0/1/0.2 | BAS interface |
| interface2 | GE0/2/0 | 10.0.0.1, 2001:db8:1::1 |
| interface3 | GE0/3/0 | 10.1.1.1 |
| - | LoopBack0 | 10.2.2.2, 2001:db8:2::2 |
| - | LoopBack1 | 10.3.3.3 |
| BRAS2 | interface1 | GE0/1/0.1 | 192.168.1.2 |
| interface1 | GE0/1/0.2 | BAS interface |
| interface2 | GE0/2/0 | 10.0.0.2, 2001:db8:2::1 |
| interface3 | GE0/3/0 | 10.1.1.2 |
| - | LoopBack0 | 10.4.4.4 |
| - | LoopBack1 | 10.5.5.5 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure BFD sessions and VRRP on the access side of the master and backup BRASs.
3. Configure an RBS and an RBP.
4. Configure a routing protocol.
5. Configure address pools.
6. Configure AAA schemes.
7. Configure a RADIUS server group.
8. Configure a domain.
9. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
10. Configure a BAS interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration on BRAS2 is similar to that on BRAS1. The configuration procedure on BRAS1 is used as an example. For details about the configuration on BRAS2, see Configuration Files.



#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters (such as the VRRP group ID and preemption delay)
* BFD parameters (such as the local and remote discriminators of a BFD session and the expected minimum intervals at which BFD Control packets are sent and received)
* IP address of each interface on BRAS1 and BRAS2
* User access parameters
* User authentication mode (RADIUS authentication)

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   # Configure IP addresses for network-side interfaces.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*HUAWEI] commit
   [~BRAS1] interface GigabitEthernet0/2/0
   [~BRAS1-GigabitEthernet0/2/0] ip address 10.0.0.1 24
   [*BRAS1-GigabitEthernet0/2/0] ipv6 enable
   [*BRAS1-GigabitEthernet0/2/0] ipv6 address 2001:db8:1::1 120
   [*BRAS1-GigabitEthernet0/2/0] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/2/0] commit
   [~BRAS1-GigabitEthernet0/2/0] quit
   [~BRAS1] interface LoopBack0
   [*BRAS1-LoopBack0] ipv6 enable
   [*BRAS1-LoopBack0] ipv6 address 2001:db8:2::2 128
   [*BRAS1-LoopBack0] ipv6 address auto link-local
   [*BRAS1-LoopBack0] ip address 10.2.2.2 32
   [*BRAS1-LoopBack0] commit
   [~BRAS1-LoopBack0] quit
   ```
   
   # Configure an IP address for the protection tunnel interface.
   
   ```
   [~BRAS1] interface LoopBack1
   [*BRAS1-LoopBack1] ip address 10.3.3.3 32
   [*BRAS1-LoopBack1] commit
   [~BRAS1-LoopBack1] quit
   ```
2. Configure BFD sessions and VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
   
   
   
   # Configure a BFD session on the access side to allow the device to rapidly detect interface or link faults and trigger a master/backup VRRP switchover upon such a fault.
   
   ```
   [~BRAS1] bfd
   [*BRAS1-bfd] quit
   [*BRAS1] bfd bfd1 bind peer-ip 192.168.1.2
   [*BRAS1-bfd-session-bfd1] discriminator local 8
   [*BRAS1-bfd-session-bfd1] discriminator remote 6
   [*BRAS1-bfd-session-bfd1] commit
   [~BRAS1-bfd-session-bfd1] quit
   ```
   
   
   
   # Configure a VRRP group on an interface (GE 0/1/0.1 is used as an example), and configure VRRP to track the BFD session and network-side interface status.
   
   ```
   [~BRAS1] interface GigabitEthernet0/1/0.1
   [*BRAS1-GigabitEthernet0/1/0.1] quit
   [*BRAS1-GigabitEthernet0/1/0.1] vlan-type dot1q 400
   [*BRAS1-GigabitEthernet0/1/0.1] ip address 192.168.1.1 255.255.255.0
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 virtual-ip 192.168.1.100
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 priority 120
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 preempt-mode timer delay 60
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 track interface GigabitEthernet 0/2/0 reduced 50
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 track bfd-session session-name bfd1 link
   [*BRAS1-GigabitEthernet0/1/0.1] commit
   [~BRAS1-GigabitEthernet0/1/0.1] quit
   [~BRAS1] vrrp recover-delay 60
   [*BRAS1] commit
   ```
3. Configure an RBS and an RBP.
   
   
   
   # Configure an interface monitoring group.
   
   ```
   [~BRAS1] monitor-group group1
   [*BRAS1-monitor-group-group1] monitor enable
   [*BRAS1-monitor-group-group1] binding interface GigabitEthernet 0/2/0
   [*BRAS1-monitor-group-group1] binding interface GigabitEthernet 0/3/0
   [*BRAS1-monitor-group-group1] trigger-up-delay 100
   [*BRAS1-monitor-group-group1] commit
   [~BRAS1-monitor-group-group1] quit
   ```
   
   
   
   # Configure an RBS.
   
   ```
   [~BRAS1] remote-backup-service s1
   [*BRAS1-rm-backup-srv-s1] peer 10.5.5.5 source 10.3.3.3 port 11000
   [*BRAS1-rm-backup-srv-s1] track monitor-group group1 switchover failure-ratio 50
   [*BRAS1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.5.5.5
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] quit
   ```
   
   
   
   # Configure an RBP.
   
   ```
   [~BRAS1] remote-backup-profile p1
   [*BRAS1-rm-backup-prf-p1] service-type bras
   [*BRAS1-rm-backup-prf-p1] peer-backup hot
   [*BRAS1-rm-backup-prf-p1] backup-id 1 remote-backup-service s1
   [*BRAS1-rm-backup-prf-p1] vrrp-id 1 interface GigabitEthernet 0/1/0.1
   [*BRAS1-rm-backup-prf-p1] commit
   [~BRAS1-rm-backup-prf-p1] quit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/0.2
   [*BRAS1-GigabitEthernet0/1/0.2] remote-backup-profile p1
   [*BRAS1-GigabitEthernet0/1/0.2] commit
   [~BRAS1-GigabitEthernet0/1/0.2] quit
   ```
4. Configure a routing protocol.
   
   
   
   # Enable the function to automatically control a route's cost preference.
   
   ```
   [~BRAS1] peer-backup route-cost auto-advertising
   [*BRAS1] commit
   ```
   
   
   
   # Configure MPLS.
   
   ```
   [~BRAS1] mpls
   [*BRAS1-mpls] mpls ldp
   [*BRAS1-mpls-ldp] commit
   [~BRAS1-mpls-ldp] quit
   [~BRAS1] mpls lsr-id 10.3.3.3
   [*BRAS1] interface GigabitEthernet0/2/0
   [*BRAS1-GigabitEthernet0/2/0] mpls
   [*BRAS1-GigabitEthernet0/2/0] mpls ldp
   [*BRAS1-GigabitEthernet0/2/0] commit
   [~BRAS1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure OSPF to import UNRs.
   
   
   
   ```
   [~BRAS1] ospf 1
   [*BRAS1-ospf-1] default cost inherit-metric
   [*BRAS1-ospf-1] import-route unr
   [*BRAS1-ospf-1] area 0.0.0.0
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.0.0.1 0.0.0.255
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.3.3.3 0.0.0.0
   [*BRAS1-ospf-1-area-0.0.0.0] commit
   [~BRAS1-ospf-1-area-0.0.0.0] quit
   [~BRAS1-ospf-1] quit
   ```
5. Configure address pools.
   
   
   
   # Configure the DHCP server.
   
   ```
   [~BRAS1] dhcp check-server-pkt loose include option 3
   [~BRAS1] dhcp-server group ipvt-v4
   [*BRAS1-dhcp-server-group-ipvt-v4] dhcp-server 111.1.1.1
   [*BRAS1-dhcp-server-group-ipvt-v4] dhcp-server source interface LoopBack0
   [*BRAS1-dhcp-server-group-ipvt-v4] undo release-agent
   [*BRAS1-dhcp-server-group-ipvt-v4] commit
   [~BRAS1-dhcp-server-group-ipvt-v4] quit
   ```
   
   # Configure an IPv4 address pool.
   
   ```
   [~BRAS1] ip pool test bas remote
   [*BRAS1-ip-pool-test] gateway 172.16.1.1 255.255.0.0
   [*BRAS1-ip-pool-test] dhcp-server group ipvt-v4
   [*BRAS1-ip-pool-test] commit
   [~BRAS1-ip-pool-test] quit
   ```
   
   # Configure the DHCPv6 server.
   
   ```
   [~BRAS1] dhcpv6-server group iptv-v6
   [*BRAS1-dhcpv6-server-group-iptv-v6] dhcpv6-server destination 2001:db8:5::5
   [*BRAS1-dhcpv6-server-group-iptv-v6] commit
   [~BRAS1-dhcpv6-server-group-iptv-v6] dhcpv6-server source interface LoopBack0
   [*BRAS1-dhcpv6-server-group-iptv-v6] commit
   [~BRAS1-dhcpv6-server-group-iptv-v6] quit
   ```
   
   # Configure IPv6 address pools.
   
   ```
   [~BRAS1] ipv6 prefix nd remote
   [*BRAS1-ipv6-prefix-nd] link-address 2001:db8:10::10/128
   [*BRAS1-ipv6-prefix-nd] commit
   [~BRAS1-ipv6-prefix-nd] quit 
   [~BRAS1] ipv6 prefix pd remote
   [*BRAS1-ipv6-prefix-pd] link-address 2001:db8:11::11/128
   [*BRAS1-ipv6-prefix-pd] commit
   [~BRAS1-ipv6-prefix-pd] quit
   [~BRAS1] ipv6 pool nd bas remote
   [*BRAS1-ipv6-pool-nd] prefix nd
   [*BRAS1-ipv6-pool-nd] dhcpv6-server group iptv-v6
   [*BRAS1-ipv6-pool-nd] commit
   [~BRAS1-ipv6-pool-nd] quit
   [~BRAS1] ipv6 pool pd bas remote
   [*BRAS1-ipv6-pool-pd] prefix pd
   [*BRAS1-ipv6-pool-nd] dhcpv6-server group iptv-v6
   [*BRAS1-ipv6-pool-nd] commit
   [~BRAS1-ipv6-pool-pd] quit
   ```
   
   # Bind the RBS to the address pools.
   
   ```
   [~BRAS1] remote-backup-service s1
   [~BRAS1-rm-backup-srv-s1] ip-pool test 
   [*BRAS1-rm-backup-srv-s1] ipv6-pool nd 
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pd 
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] quit
   ```
6. Configure AAA schemes.
   1. Configure an authentication scheme.
      
      
      ```
      [~BRAS1] aaa
      [~BRAS1-aaa] authentication-scheme auth1
      [*BRAS1-aaa-authen-auth1] authentication-mode radius
      [*BRAS1-aaa-authen-auth1] commit
      [~BRAS1-aaa-authen-auth1] quit
      ```
   2. Configure an accounting scheme.
      
      
      ```
      [~BRAS1-aaa] accounting-scheme acct1
      [*BRAS1-aaa-accounting-acct1] accounting-mode radius
      [*BRAS1-aaa-accounting-radius] commit
      [~BRAS1-aaa-accounting-radius] quit
      ```
7. Configure a RADIUS server group.
   
   
   ```
   [~BRAS1-aaa] radius-server group rd1
   [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1645
   [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1646
   [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   [*BRAS1-radius-rd1] radius-server source interface LoopBack0
   [*BRAS1-radius-rd1] radius-server calling-station-id include mac 
   [*BRAS1-radius-rd1] commit
   [~BRAS1-radius-rd1] quit
   ```
8. Configure a domain.
   
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain test
   [*BRAS1-aaa-domain-test] authentication-scheme auth1
   [*BRAS1-aaa-domain-test] accounting-scheme acct1
   [*BRAS1-aaa-domain-test] radius-server group rd1
   [*BRAS1-aaa-domain-test] prefix-assign-mode unshared
   [*BRAS1-aaa-domain-test] commit
   [~BRAS1-aaa-domain-test] ip-pool test
   [*BRAS1-aaa-domain-test] ipv6-pool nd
   [*BRAS1-aaa-domain-test] ipv6-pool pd
   [*BRAS1-aaa-domain-test] commit
   [~BRAS1-aaa-domain-test] quit
   [~BRAS1-aaa] quit
   ```
9. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
   
   
   ```
   [~BRAS1] dhcpv6 duid llt
   [*BRAS1] commit
   ```
10. Configure a BAS interface, bind the BAS interface to the VT, and enable IPv6 on the BAS interface.
    
    
    ```
    [~BRAS1] interface GigabitEthernet 0/1/0.2
    [~BRAS1-GigabitEthernet0/1/0.2] ipv6 enable
    [*BRAS1-GigabitEthernet0/1/0.2] ipv6 address auto link-local
    [*BRAS1-GigabitEthernet0/1/0.2] commit
    [~BRAS1-GigabitEthernet0/1/0.2] user-vlan 5                                           
    [~BRAS1-GigabitEthernet0/1/0.2-user-vlan 5] quit
    [~BRAS1-GigabitEthernet0/1/0.2] bas
    [~BRAS1-GigabitEthernet0/1/0.2-bas] access-type layer2-subscriber default-domain authentication test
    [~BRAS1-GigabitEthernet0/1/0.2-bas] client-option82
    [~BRAS1-GigabitEthernet0/1/0.2-bas] authentication-method bind
    [*BRAS1-GigabitEthernet0/1/0.2-bas] authentication-method-ipv6 bind
    [*BRAS1-GigabitEthernet0/1/0.2-bas] commit
    [~BRAS1-GigabitEthernet0/1/0.2-bas] quit
    ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1
  #
  vrrp recover-delay 60
  #
  radius-server group rd1
   radius-server shared-key-cipher %^%#b-SAV,j)4#)Ez2TokT,%2z'sNM~0@4h~G.KsQhz)%^%#
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server source interface LoopBack0
   radius-server calling-station-id include mac 
  #
  bfd
  #
  mpls lsr-id 10.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  ip pool test bas remote
   gateway 172.16.1.1 255.255.0.0
   dhcp-server group ipvt-v4
  #
  dhcp-server group ipvt-v4
   dhcp-server 111.1.1.1
   dhcp-server source interface LoopBack0
   undo release-agent
  #
  dhcpv6-server group iptv-v6
   dhcpv6-server destination 2001:db8:5::5
   dhcpv6-server source interface LoopBack0
  #
  ipv6 prefix nd remote
   link-address 2001:db8:10::10/128
  #
  ipv6 prefix pd remote
   link-address 2001:db8:11::11/128
  #
  ipv6 pool nd bas remote
   prefix nd
   dhcpv6-server group iptv-v6
  #
  ipv6 pool pd bas remote
   prefix pd
   dhcpv6-server group iptv-v6
  #
  dhcp check-server-pkt loose include option 3
  #
  monitor-group group1
   monitor enable
   binding interface GigabitEthernet0/2/0 down-weight 10
   binding interface GigabitEthernet0/3/0 down-weight 10
   trigger-up-delay 100
  #
  remote-backup-service s1
   peer 10.5.5.5 source 10.3.3.3 port 11000
   track monitor-group group1 switchover failure-ratio 50
   protect lsp-tunnel for-all-instance peer-ip 10.5.5.5
   ip-pool test metric 10
   ipv6-pool nd metric 10
   ipv6-pool pd metric 10
  #
  remote-backup-profile p1
   service-type bras
   backup-id 1 remote-backup-service s1
   peer-backup hot
   vrrp-id 1 interface GigabitEthernet0/1/0.1
  #
  dhcpv6 duid 00010001280ef7a400e0fc904b50
  #
  aaa
   #
   authentication-scheme auth1
   #
   accounting-scheme acct1
   #
   domain test
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    prefix-assign-mode unshared
    ip-pool test
    ipv6-pool nd
    ipv6-pool pd
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ip address 10.0.0.1 255.255.255.0
   ipv6 address 2001:db8:1::1/120
   ipv6 address auto link-local
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 400
   ip address 192.168.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 192.168.1.100
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt-mode timer delay 60
   vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50
   vrrp vrid 1 track bfd-session session-name bfd1 link
  #
  interface GigabitEthernet0/1/0.2
   ipv6 enable
   ipv6 address auto link-local
   statistic enable
   user-vlan 5
   remote-backup-profile p1
   bas
   #
    access-type layer2-subscriber default-domain authentication test
    client-option82
    authentication-method bind
    authentication-method-ipv6 bind
   #
  #
  interface LoopBack0
   ipv6 enable
   ip address 10.2.2.2 255.255.255.255
   ipv6 address 2001:db8:2::2/128
   ipv6 address auto link-local
  #
  interface LoopBack1
   ip address 10.3.3.3 255.255.255.255
  #
  bfd bfd1 bind peer-ip 192.168.1.2
   discriminator local 8
   discriminator remote 6
  #
  ospf 1
   default cost inherit-metric
   import-route unr
   area 0.0.0.0
   network 10.0.0.1 0.0.0.255
   network 10.3.3.3 0.0.0.0
  #
  peer-backup route-cost auto-advertising 
  #
  return
  ```
* BRAS2 configuration file
  
  ```
  #
  sysname BRAS2
  #
  vrrp recover-delay 60
  #
  radius-server group rd1
   radius-server shared-key-cipher %^%#b-SAV,j)4#)Ez2TokT,%2z'sNM~0@4h~G.KsQhz)%^%#
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server source interface LoopBack0
   radius-server calling-station-id include mac 
  #
  bfd
  #
  mpls lsr-id 10.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  ip pool test bas remote rui-slave
   gateway 172.16.1.1 255.255.0.0
   dhcp-server group ipvt-v4
  #
  dhcp-server group ipvt-v4
   dhcp-server 111.1.1.1
   dhcp-server source interface LoopBack0
   undo release-agent
  #
  dhcpv6-server group iptv-v6
   dhcpv6-server destination 2001:db8:5::5
   dhcpv6-server source interface LoopBack0
  #
  ipv6 prefix nd remote
   link-address 2001:db8:10::10/128
  #
  ipv6 prefix pd remote
   link-address 2001:db8:11::11/128
  #
  ipv6 pool nd bas remote rui-slave
   prefix nd
   dhcpv6-server group iptv-v6
  #
  ipv6 pool pd bas remote rui-slave
   prefix pd
   dhcpv6-server group iptv-v6
  #
  dhcp check-server-pkt loose include option 3
  #
  monitor-group group1
   monitor enable
   binding interface GigabitEthernet0/2/0 down-weight 10
   binding interface GigabitEthernet0/3/0 down-weight 10
   trigger-up-delay 100
  #
  remote-backup-service s1
   peer 10.3.3.3 source 10.5.5.5 port 11000
   track monitor-group group1 switchover failure-ratio 50
   protect lsp-tunnel for-all-instance peer-ip 10.3.3.3
   ip-pool test metric 20
   ipv6-pool nd metric 20
   ipv6-pool pd metric 20
  #
  remote-backup-profile p1
   service-type bras
   backup-id 1 remote-backup-service s1
   peer-backup hot
   vrrp-id 1 interface GigabitEthernet0/1/0.1
  #
  dhcpv6 duid 00010001280ef7a400e0fc904b50
  #
  aaa
   #
   authentication-scheme auth1
   #
   accounting-scheme acct1
   #
   domain test
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    prefix-assign-mode unshared
    ip-pool test
    ipv6-pool nd
    ipv6-pool pd
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ip address 10.0.0.2 255.255.255.0
   ipv6 address 2001:db8:3::3/120
   ipv6 address auto link-local
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 400
   ip address 192.168.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 192.168.1.100
   vrrp vrid 1 priority 100
   vrrp vrid 1 preempt-mode timer delay 60
   vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50
   vrrp vrid 1 track bfd-session session-name bfd1 link
  #
  interface GigabitEthernet0/1/0.2
   ipv6 enable
   ipv6 address auto link-local
   statistic enable
   user-vlan 5
   remote-backup-profile p1
   bas
   #
    access-type layer2-subscriber default-domain authentication test
    client-option82
    authentication-method bind
    authentication-method-ipv6 bind
   #
  #
  interface LoopBack0
   ipv6 enable
   ip address 10.4.4.4 255.255.255.255
   ipv6 address 2001:db8:4::4/128
   ipv6 address auto link-local
  #
  interface LoopBack1
   ip address 10.5.5.5 255.255.255.255
  #
  bfd bfd1 bind peer-ip 192.168.1.1
   discriminator local 6
   discriminator remote 8
  #
  ospf 1
   default cost inherit-metric
   import-route unr
   area 0.0.0.0
   network 10.9.9.9 0.0.0.255
   network 10.5.5.5 0.0.0.0
  #
  peer-backup route-cost auto-advertising 
  #
  return
  ```