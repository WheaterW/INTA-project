Example for Configuring Dual-Stack PPPoE User Access in a Dual-Device Hot Backup Scenario (ND Unshared+PD)
==========================================================================================================

In a dual-device hot backup scenario, dual-stack users connect to the master and backup BRASs using PPPoE. The BRASs assign IPv6 addresses to the users in ND unshared+PD mode to implement user access.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0210982515__fig_dc_ne_cfg_rui_003101), users access BRAS1 and BRAS2 through SW1. RADIUS authentication and accounting are configured on the BRASs. The BRASs use a local address pool to assign IPv4 addresses to users, use DHCPv6 IA\_PD to assign the IPv6 prefixes to be used on the network to users, and use DHCPv6 ND to assign IPv6 addresses to users.

**Figure 1** Configuring dual-stack PPPoE user access in a dual-device hot backup scenario (ND unshared+PD)![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/2/0 and GE0/2/1, respectively.

![](figure/en-us_image_0212730081.png)

| **Device** | **Interface** | **IP Address** |
| --- | --- | --- |
| BRAS1 | GE 0/2/1.1 | 10.1.1.1/24 |
| BRAS1 | GE 0/2/1.5 | Interface through which users go online |
| BRAS1 | GE 0/2/1.2 | 10.32.1.1/24 |
| BRAS1 | Loopback 1 | 10.1.2.1/32 |
| BRAS1 | Loopback 100 | 10.20.1.1/24 |
| BRAS2 | GE 0/2/1.1 | 10.1.1.2/24 |
| BRAS2 | GE 0/2/1.5 | Interface through which users go online |
| BRAS2 | GE 0/2/1.2 | 10.32.1.2/24 |
| BRAS2 | Loopback 1 | 10.1.2.2/32 |
| BRAS2 | Loopback 100 | 10.20.1.2/24 |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BFD sessions and VRRP on the access side of the master and backup BRASs.
2. Configure an RBS and an RBP.
3. Configure a routing protocol.
4. Configure AAA schemes and a RADIUS server group.
5. Configure address pools and bind the RBS to the address pools.
6. Configure a domain and bind the address pools to the domain.
7. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
8. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters (such as the VRRP ID and preemption delay)
* BFD parameters (such as the local and remote discriminators of a BFD session and the expected minimum interval at which BFD Control packets are sent and received)
* IP address of each interface on BRAS1 and BRAS2
* User access parameters
* User authentication mode (RADIUS authentication)

#### Procedure

1. Configure BFD sessions and VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
   
   
   
   The configurations on BRAS1 are as follows:
   
   # Configure a BFD session on the access side to allow BRAS1 to rapidly detect interface or link faults and trigger a master/backup VRRP switchover upon such a fault.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*BRAS1] commit
   [~BRAS1] bfd
   [*BRAS1-bfd] quit
   [*BRAS1] bfd bfd1 bind peer-ip 10.1.1.2
   [*BRAS1-bfd-session-bfd1] discriminator local 8
   [*BRAS1-bfd-session-bfd1] discriminator remote 6
   [*BRAS1-bfd-session-bfd1] commit
   [~BRAS1-bfd-session-bfd1] quit 
   ```
   
   # Configure a VRRP group on an interface (GE 0/2/1.1 is used as an example), and configure VRRP to track the BFD session and network-side interface status.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/2/1.1              
   [*BRAS1-GigabitEthernet0/2/1.1] vlan-type dot1q 200                           
   [*BRAS1-GigabitEthernet0/2/1.1] ip address 10.1.1.1 255.255.255.0            
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 virtual-ip 10.1.1.100            
   [*BRAS1-GigabitEthernet0/2/1.1] admin-vrrp vrid 1                             
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 priority 120 
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 preempt-mode timer delay 60 
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 track interface GigabitEthernet 0/2/0 reduced 50                           
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 track bfd-session session-name bfd1 peer                       
   [*BRAS1-GigabitEthernet0/2/1.1] commit
   [~BRAS1-GigabitEthernet0/2/1.1] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   # Configure a BFD session on the access side to allow BRAS2 to rapidly detect interface or link faults and trigger a master/backup VRRP switchover upon such a fault.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS2
   [*BRAS2] commit
   [~BRAS2] bfd
   [*BRAS2-bfd] quit
   [*BRAS2] bfd bfd2 bind peer-ip 10.1.1.1
   [*BRAS2-bfd-session-bfd2] discriminator local 6
   [*BRAS2-bfd-session-bfd2] discriminator remote 8
   [*BRAS2-bfd-session-bfd2] commit
   [~BRAS2-bfd-session-bfd2] quit 
   ```
   
   # Configure a VRRP group on an interface (GE 0/2/1.1 is used as an example), and configure VRRP to track the BFD session and network-side interface status.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/2/1.1              
   [*BRAS2-GigabitEthernet0/2/1.1] vlan-type dot1q 200                           
   [*BRAS2-GigabitEthernet0/2/1.1] ip address 10.1.1.2 255.255.255.0            
   [*BRAS2-GigabitEthernet0/2/1.1] vrrp vrid 1 virtual-ip 10.1.1.100            
   [*BRAS2-GigabitEthernet0/2/1.1] admin-vrrp vrid 1                             
   [*BRAS2-GigabitEthernet0/2/1.1] vrrp vrid 1 priority 100 
   [*BRAS2-GigabitEthernet0/2/1.1] vrrp vrid 1 preempt-mode timer delay 60 
   [*BRAS2-GigabitEthernet0/2/1.1] vrrp vrid 1 track interface GigabitEthernet 0/2/0 reduced 50                           
   [*BRAS2-GigabitEthernet0/2/1.1] vrrp vrid 1 track bfd-session session-name bfd2 peer                       
   [*BRAS2-GigabitEthernet0/2/1.1] commit
   [~BRAS2-GigabitEthernet0/2/1.1] quit
   ```
2. Configure an RBS and an RBP.
   
   
   
   The configurations on BRAS1 are as follows:
   
   # Configure an IP address for the protection tunnel.
   
   ```
   [~BRAS1] interface loopback1
   [*BRAS1-loopback1] ip address 10.1.2.1 32
   [*BRAS1-loopback1] commit
   [~BRAS1-loopback1] quit
   ```
   
   # Configure an RBS.
   
   ```
   [~BRAS1] remote-backup-service s1
   [*BRAS1-rm-backup-srv-s1] peer 10.1.2.2 source 10.1.2.1 port 6001
   [*BRAS1-rm-backup-srv-s1] track interface GigabitEthernet 0/2/0
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.1.2.2
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] quit
   ```
   
   # Configure an RBP.
   
   ```
   [~BRAS1] remote-backup-profile p1
   [*BRAS1-rm-backup-prf-p1] service-type bras
   [*BRAS1-rm-backup-prf-p1] backup-id 101 remote-backup-service s1
   [*BRAS1-rm-backup-prf-p1] peer-backup hot
   [*BRAS1-rm-backup-prf-p1] vrrp-id 1 interface Gigabitethernet 0/2/1.1
   [*BRAS1-rm-backup-prf-p1] nas logic-port Gigabitethernet 0/2/1
   [*BRAS1-rm-backup-prf-p1] nas logic-ip 10.10.1.1
   [*BRAS1-rm-backup-prf-p1] commit
   [~BRAS1-rm-backup-prf-p1] quit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS1] interface gigabitethernet 0/2/1.5
   [*BRAS1-GigabitEthernet0/2/1.5] remote-backup-profile p1
   [*BRAS1-GigabitEthernet0/2/1.5] commit
   [~BRAS1-GigabitEthernet0/2/1.5] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   # Configure an IP address for the protection tunnel.
   
   ```
   [~BRAS2] interface loopback1
   [*BRAS2-loopback1] ip address 10.1.2.2 32
   [*BRAS2-loopback1] commit
   [~BRAS2-loopback1] quit
   ```
   
   # Configure an RBS.
   
   ```
   [~BRAS2] remote-backup-service s1
   [*BRAS2-rm-backup-srv-s1] peer 10.1.2.1 source 10.1.2.2 port 6001
   [*BRAS2-rm-backup-srv-s1] track interface GigabitEthernet 0/2/0
   [*BRAS2-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.1.2.1
   [*BRAS2-rm-backup-srv-s1] commit
   [~BRAS2-rm-backup-srv-s1] quit
   ```
   
   # Configure an RBP.
   
   ```
   [~BRAS2] remote-backup-profile p1
   [*BRAS2-rm-backup-prf-p1] service-type bras
   [*BRAS2-rm-backup-prf-p1] backup-id 101 remote-backup-service s1
   [*BRAS2-rm-backup-prf-p1] peer-backup hot
   [*BRAS2-rm-backup-prf-p1] vrrp-id 1 interface Gigabitethernet 0/2/1.1
   [*BRAS2-rm-backup-prf-p1] nas logic-port Gigabitethernet 0/2/1
   [*BRAS2-rm-backup-prf-p1] nas logic-ip 10.10.1.1
   [*BRAS2-rm-backup-prf-p1] commit
   [~BRAS2-rm-backup-prf-p1] quit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS2] interface gigabitethernet 0/2/1.5
   [*BRAS2-GigabitEthernet0/2/1.5] remote-backup-profile p1
   [*BRAS2-GigabitEthernet0/2/1.5] commit
   [~BRAS2-GigabitEthernet0/2/1.5] quit
   ```
3. Configure a routing protocol.
   
   
   
   The configurations on BRAS1 are as follows:
   
   # Enable the function to automatically control a route's cost preference.
   
   ```
   [~BRAS1] peer-backup route-cost auto-advertising
   ```
   
   Configure MPLS.
   
   ```
   [*BRAS1] mpls lsr-id 10.1.1.1
   [*BRAS1] mpls
   [*BRAS1-mpls] commit
   [~BRAS1-mpls] mpls ldp
   [*BRAS1-mpls-ldp] commit
   [~BRAS1-mpls] quit
   ```
   
   # Configure OSPF to import UNRs.
   
   ```
   [~BRAS1] ospf 1
   [*BRAS1-ospf-1] default cost inherit-metric
   [*BRAS1-ospf-1] import-route unr
   [*BRAS1-ospf-1] area 0
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.1.1.1 0.0.0.0
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.1.2.1 0.0.0.255
   [*BRAS1-ospf-1-area-0.0.0.0] commit
   [~BRAS1-ospf-1-area-0.0.0.0] quit
   [~BRAS1-ospf-1] quit
   ```
   
   # Configure IS-IS to advertise network-side routes on the BRAS.
   
   ```
   [~BRAS1] isis 100
   [*BRAS1-isis-100] is-level level-2
   [*BRAS1-isis-100] cost-style wide
   [*BRAS1-isis-100] network-entity 10.1111.2222.3333.4444.00
   [*BRAS1-isis-100] ipv6 enable topology ipv6                
   [*BRAS1-isis-100] ipv6 preference 20
   [*BRAS1-isis-100] commit
   [~BRAS1-isis-100] quit
   ```
   
   # Configure BGP to advertise user-side routes on the BRAS.
   
   ```
   [~BRAS1] bgp 100
   [*BRAS1-bgp] group group1 internal
   [*BRAS1-bgp] peer group1 connect-interface LoopBack100
   [*BRAS1-bgp] group group2 external
   [*BRAS1-bgp] peer group2 connect-interface LoopBack100
   [*BRAS1-bgp] peer 2001:db8:7::2101 as-number 100 
   [*BRAS1-bgp] peer 2001:db8:7::2101 group group1 
   [*BRAS1-bgp] peer 2001:db8:7::2102 as-number 100 
   [*BRAS1-bgp] peer 2001:db8:7::2102 group group1 
   [*BRAS1-bgp] peer 2.2.2.2 as-number 101
   [*BRAS1-bgp] peer 2.2.2.2 group group2 
   [*BRAS1-bgp] peer 3.3.3.3 as-number 101 
   [*BRAS1-bgp] peer 3.3.3.3 group group2 
   [*BRAS1-bgp] ipv4-family unicast
   [*BRAS1-bgp-af-ipv4] import-route unr
   [*BRAS1-bgp-af-ipv4] quit 
   [*BRAS1-bgp] ipv6-family unicast
   [*BRAS1-bgp-af-ipv6] import-route unr
   [*BRAS1-bgp-af-ipv6] quit
   [*BRAS1-bgp] commit
   [~BRAS1-bgp] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   # Enable the function to automatically control a route's cost preference.
   
   ```
   [~BRAS2] peer-backup route-cost auto-advertising
   ```
   
   Configure MPLS.
   
   ```
   [*BRAS2] mpls lsr-id 10.1.1.2
   [*BRAS2] mpls
   [*BRAS2-mpls] commit
   [~BRAS2-mpls] mpls ldp
   [*BRAS2-mpls-ldp] commit
   [~BRAS2-mpls] quit
   ```
   
   # Configure OSPF to import UNRs.
   
   ```
   [~BRAS2] ospf 1
   [*BRAS2-ospf-1] default cost inherit-metric
   [*BRAS2-ospf-1] import-route unr
   [*BRAS2-ospf-1] area 0
   [*BRAS2-ospf-1-area-0.0.0.0] network 10.1.1.2 0.0.0.0
   [*BRAS2-ospf-1-area-0.0.0.0] network 10.1.2.2 0.0.0.255
   [*BRAS2-ospf-1-area-0.0.0.0] commit
   [~BRAS2-ospf-1-area-0.0.0.0] quit
   [~BRAS2-ospf-1] quit
   ```
   
   # Configure IS-IS to advertise network-side routes on the BRAS.
   
   ```
   [*BRAS2] isis 100
   [*BRAS2-isis-100] is-level level-2
   [*BRAS2-isis-100] cost-style wide
   [*BRAS2-isis-100] network-entity 10.1111.2222.3333.4444.00
   [*BRAS2-isis-100] ipv6 enable topology ipv6                
   [*BRAS2-isis-100] ipv6 preference 20
   ```
   
   # Configure BGP to advertise user-side routes on the BRAS.
   
   ```
   [~BRAS2] bgp 100
   [*BRAS2-bgp] group group1 internal
   [*BRAS2-bgp] peer group1 connect-interface LoopBack100
   [*BRAS2-bgp] group group2 external
   [*BRAS2-bgp] peer group2 connect-interface LoopBack100
   [*BRAS2-bgp] peer 2001:db8:7::2101 as-number 100 
   [*BRAS2-bgp] peer 2001:db8:7::2101 group group1 
   [*BRAS2-bgp] peer 2001:db8:7::2102 as-number 100 
   [*BRAS2-bgp] peer 2001:db8:7::2102 group group1 
   [*BRAS2-bgp] peer 2.2.2.2 as-number 101
   [*BRAS2-bgp] peer 2.2.2.2 group group2 
   [*BRAS2-bgp] peer 3.3.3.3 as-number 101 
   [*BRAS2-bgp] peer 3.3.3.3 group group2 
   [*BRAS2-bgp] ipv4-family unicast
   [*BRAS2-bgp-af-ipv4] import-route unr
   [*BRAS2-bgp-af-ipv4] quit 
   [*BRAS2-bgp] ipv6-family unicast
   [*BRAS2-bgp-af-ipv6] import-route unr
   [*BRAS2-bgp-af-ipv6] quit
   [*BRAS2-bgp] commit
   [~BRAS2-bgp] quit
   ```
4. Configure AAA schemes.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of BRAS2 is similar to the configuration of BRAS1. The configuration of BRAS1 is used in this example. For details about the configuration of BRAS2, see Configuration Files.
   
   # Configure an authentication scheme.
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] authentication-scheme auth1
   [*BRAS1-aaa-authen-auth1] authentication-mode radius
   [*BRAS1-aaa-authen-auth1] quit
   [*BRAS1-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~BRAS1-aaa] accounting-scheme acct1
   [*BRAS1-aaa-accounting-acct1] accounting-mode radius
   [*BRAS1-aaa-accounting-acct1] quit
   [*BRAS1-aaa] quit
   [*BRAS1] commit
   ```
5. Configure a RADIUS server group.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of BRAS2 is similar to the configuration of BRAS1. The configuration of BRAS1 is used in this example. For details about the configuration of BRAS2, see Configuration Files.
   
   ```
   [~BRAS1] radius-server group rd1
   [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1645
   [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1646
   [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
   [*BRAS1-radius-rd1] quit
   [*BRAS1] commit
   ```
6. Configure address pools and bind the RBS to the address pools.
   
   
   
   The configurations on BRAS1 are as follows:
   
   # Configure a user-side local IPv4 address pool.
   
   ```
   [~BRAS1] ip pool pool1 bas local
   [*BRAS1-ip-pool-pool1] gateway 10.179.180.1 255.255.255.0
   [*BRAS1-ip-pool-pool1] commit
   [~BRAS1-ip-pool-pool1] section 0 10.179.180.2 10.179.180.254
   [*BRAS1-ip-pool-pool1] commit
   [~BRAS1-ip-pool-pool1] quit
   ```
   
   # Configure a delegation prefix pool for IPv6 ND users.
   
   ```
   [~BRAS1] ipv6 prefix pre_nd delegation
   [*BRAS1-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48 delegating-prefix-length 64
   [*BRAS1-ipv6-prefix-pre_pd] commit
   [~BRAS1-ipv6-prefix-pre_nd] quit
   ```
   
   # Configure a delegation address pool for IPv6 ND users.
   
   ```
   [~BRAS1] ipv6 pool pool_nd bas delegation
   [*BRAS1-ipv6-pool-pool_nd] prefix pre_nd
   [*BRAS1-ipv6-pool-pool_nd] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_nd] commit
   [~BRAS1-ipv6-pool-pool_nd] quit
   ```
   
   # Configure a delegation prefix pool for IPv6 PD users.
   
   ```
   [~BRAS1] ipv6 prefix pre_pd delegation
   [*BRAS1-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
   [*BRAS1-ipv6-prefix-pre_pd] commit
   [~BRAS1-ipv6-prefix-pre_pd] quit
   ```
   
   # Configure a delegation address pool for IPv6 PD users.
   
   ```
   [~BRAS1] ipv6 pool pool_pd bas delegation
   [*BRAS1-ipv6-pool-pool_pd] prefix pre_pd
   [*BRAS1-ipv6-pool-pool_pd] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_pd] commit
   [~BRAS1-ipv6-pool-pool_pd] quit
   ```
   
   # Bind the RBS to the address pools.
   
   ```
   [~BRAS1] remote-backup-service s1
   [*BRAS1-rm-backup-srv-s1] ip-pool pool1
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_nd metric 10
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_pd metric 10
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   # Configure a user-side local IPv4 address pool.
   
   ```
   [~BRAS2] ip pool pool1 bas local rui-slave 
   [*BRAS2-ip-pool-pool1] gateway 10.179.180.1 255.255.255.0
   [*BRAS2-ip-pool-pool1] commit
   [~BRAS2-ip-pool-pool1] section 0 10.179.180.2 10.179.180.254
   [*BRAS2-ip-pool-pool1] commit
   [~BRAS2-ip-pool-pool1] quit
   ```
   
   # Configure an IPv6 ND unshared prefix pool.
   
   ```
   [~BRAS2] ipv6 prefix pre_nd delegation
   [*BRAS2-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48 delegating-prefix-length 64
   [*BRAS2-ipv6-prefix-pre_nd] commit
   [~BRAS2-ipv6-prefix-pre_nd] quit
   ```
   
   # Configure a delegation address pool for IPv6 ND users.
   
   ```
   [~BRAS2] ipv6 pool pool_nd bas delegation rui-slave
   [*BRAS2-ipv6-pool-pool_nd] prefix pre_nd
   [*BRAS2-ipv6-pool-pool_nd] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS2-ipv6-pool-pool_nd] commit
   [~BRAS2-ipv6-pool-pool_nd] quit
   ```
   
   # Configure a delegation prefix pool for IPv6 PD users.
   
   ```
   [~BRAS2] ipv6 prefix pre_pd delegation
   [*BRAS2-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
   [*BRAS2-ipv6-prefix-pre_pd] commit
   [~BRAS2-ipv6-prefix-pre_pd] quit
   ```
   
   # Configure a delegation address pool for IPv6 PD users.
   
   ```
   [~BRAS2] ipv6 pool pool_pd bas delegation rui-slave
   [*BRAS2-ipv6-pool-pool_pd] prefix pre_pd
   [*BRAS2-ipv6-pool-pool_pd] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS2-ipv6-pool-pool_pd] commit
   [~BRAS2-ipv6-pool-pool_pd] quit
   ```
   
   # Bind the RBS to the address pools.
   
   ```
   [~BRAS2] remote-backup-service s1
   [*BRAS2-rm-backup-srv-s1] ip-pool pool1
   [*BRAS2-rm-backup-srv-s1] ipv6-pool pool_nd metric 20
   [*BRAS2-rm-backup-srv-s1] ipv6-pool pool_pd metric 20
   [*BRAS2-rm-backup-srv-s1] commit
   [~BRAS2-rm-backup-srv-s1] quit
   ```
7. Configure a domain.
   
   
   
   The configurations on BRAS1 are as follows:
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain isp1
   [*BRAS1-aaa-domain-isp1] authentication-scheme auth1
   [*BRAS1-aaa-domain-isp1] accounting-scheme acct1
   [*BRAS1-aaa-domain-isp1] radius-server group rd1
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] prefix-assign-mode unshared  
   [~BRAS1-aaa-domain-isp1] ip-pool pool1
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_nd
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_pd
   [~BRAS1-aaa-domain-isp1] quit
   [~BRAS1-aaa] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   ```
   [~BRAS2] aaa
   [~BRAS2-aaa] domain isp1
   [*BRAS2-aaa-domain-isp1] authentication-scheme auth1
   [*BRAS2-aaa-domain-isp1] accounting-scheme acct1
   [*BRAS2-aaa-domain-isp1] radius-server group rd1
   [*BRAS2-aaa-domain-isp1] commit
   [~BRAS2-aaa-domain-isp1] prefix-assign-mode unshared  
   [~BRAS2-aaa-domain-isp1] ip-pool pool1
   [~BRAS2-aaa-domain-isp1] ipv6-pool pool_nd
   [~BRAS2-aaa-domain-isp1] ipv6-pool pool_pd
   [~BRAS2-aaa-domain-isp1] quit
   [~BRAS2-aaa] quit
   ```
8. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of BRAS2 is similar to the configuration of BRAS1. The configuration of BRAS1 is used in this example. For details about the configuration of BRAS2, see Configuration Files.
   
   ```
   [~BRAS1] dhcpv6 duid llt
   [*BRAS1] commit
   ```
9. Configure interfaces.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of BRAS2 is similar to the configuration of BRAS1. The configuration of BRAS1 is used in this example. For details about the configuration of BRAS2, see Configuration Files.
   
   # Configure a virtual template.
   
   ```
   [~BRAS1] interface Virtual-Template1
   [*BRAS1-Virtual-Template1] ppp authentication-mode chap
   [*BRAS1-Virtual-Template1] commit
   [~BRAS1-Virtual-Template1] quit
   ```
   
   # Specify the virtual template for a sub-interface and enable IPv6 on the sub-interface.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/2/1.5
   [*BRAS1-GigabitEthernet0/2/1.5] pppoe-server bind virtual-template 1
   [*BRAS1-GigabitEthernet0/2/1.5] ipv6 enable
   [*BRAS1-GigabitEthernet0/2/1.5] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/2/1.5] commit
   [~BRAS1-GigabitEthernet0/2/1.5] user-vlan 4003
   ```
   
   # Configure a BAS interface.
   
   ```
   [~BRAS1-GigabitEthernet0/2/1.5-vlan-4003-4003] bas
   [~BRAS1-GigabitEthernet0/2/1.5-bas] access-type layer2-subscriber default-domain authentication isp1
   [*BRAS1-GigabitEthernet0/2/1.5-bas] client-option82
   [*BRAS1-GigabitEthernet0/2/1.5-bas] authentication-method ppp web
   [*BRAS1-GigabitEthernet0/2/1.5-bas] authentication-method-ipv6 ppp web
   [*BRAS1-GigabitEthernet0/2/1.5-bas] commit
   [~BRAS1-GigabitEthernet0/2/1.5-bas] quit
   [~BRAS1-GigabitEthernet0/2/1.5] quit
   ```
   
   # Configure the network-side interface of the BRAS.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/2/1.2
   [~BRAS1-GigabitEthernet0/2/1.2] ipv6 enable 
   [*BRAS1-GigabitEthernet0/2/1.2] ipv6 address 2001:db8:8::7 128
   [*BRAS1-GigabitEthernet0/2/1.2] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/2/1.2] ip address 10.32.1.1 24
   [*BRAS1-GigabitEthernet0/2/1.2] isis enable 100 
   [*BRAS1-GigabitEthernet0/2/1.2] isis ipv6 enable 100
   [*BRAS1-GigabitEthernet0/2/1.2] isis ipv6 cost 50 level-2 
   [*BRAS1-GigabitEthernet0/2/1.2] commit
   [~BRAS1-GigabitEthernet0/2/1.2] quit
   ```
   
   # Configure loopback interface 100 as the source interface for sending BGP packets.
   
   ```
   [~BRAS1] interface LoopBack100
   [*BRAS1-LoopBack100] ipv6 enable
   [*BRAS1-LoopBack100] ipv6 address 2001:db8:7::7 127
   [*BRAS1-LoopBack100] ipv6 address auto link-local
   [*BRAS1-LoopBack100] ip address 10.20.1.1 24
   [*BRAS1-LoopBack100] isis enable 100 
   [*BRAS1-LoopBack100] isis ipv6 enable 100
   [*BRAS1-LoopBack100] quit
   [*BRAS1] commit
   ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1                                                         
  #                                                                               
  bfd
  #  
  bfd bfd1 bind peer-ip 10.1.1.2 
   discriminator local 8
   discriminator remote 6                                                  
  #                                                                               
  radius-server group rd1                                                         
   radius-server shared-key-cipher %^%#Q'!i-TMV5&@=QE}g/QK2ouBHee8WB|s|mB%^%
   radius-server authentication 192.168.7.249 1645                        
   radius-server accounting 192.168.7.249 1646 
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1  
    accounting-mode radius
  #
  remote-backup-service s1                      
   peer 10.1.2.2 source 10.1.2.1 port 6001       
   protect lsp-tunnel for-all-instance peer-ip 10.1.2.2   
   track interface GigabitEthernet0/2/0          
   ip-pool pool1
   ipv6-pool pool_nd metric 10
   ipv6-pool pool_pd metric 10
  #
  remote-backup-profile p1                       
   service-type bras         
   backup-id 101 remote-backup-service s1                 
   peer-backup hot                    
   vrrp-id 1 interface GigabitEthernet0/2/1.1
   nas logic-port gigabitethernet 0/2/1
   nas logic-ip 10.10.1.1
  #                                                                               
  ip pool pool1 bas local                                                         
   gateway 10.179.180.1 255.255.255.0                                                
   section 0 10.179.180.2 10.179.180.254                                                 
  #
  ipv6 prefix pre_nd delegation
   prefix 2001:db8:1::/48 delegating-prefix-length 64
  #
  ipv6 pool pool_nd bas delegation
   prefix pre_nd
   dns-server 2001:db8::2:2 2001:db8::2:3
  #
  ipv6 prefix pre_pd delegation
   prefix 2001:db8:2::/48 delegating-prefix-length 60
  #
  ipv6 pool pool_pd bas delegation
   prefix pre_pd
   dns-server 2001:db8::2:2 2001:db8::2:3
  # 
  aaa                                                                             
   domain isp1                                                                    
    authentication-scheme auth1                                                   
    accounting-scheme acct1                                                       
    radius-server group rd1
    prefix-assign-mode unshared  
    ip-pool pool1
    ipv6-pool pool_nd
    ipv6-pool pool_pd
  #
  dhcpv6 duid llt
  #                                                                               
  interface Virtual-Template1                                                     
   ppp authentication-mode chap                                                   
  #
  interface GigabitEthernet0/2/1
  #
  interface GigabitEthernet0/2/1.1
   vlan-type dot1q 200                             
   ip address 10.1.1.1 255.255.255.0            
   vrrp vrid 1 virtual-ip 10.1.1.100            
   admin-vrrp vrid 1                             
   vrrp vrid 1 priority 120                      
   vrrp vrid 1 preempt-mode timer delay 60       
   vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50                    
   vrrp vrid 1 track bfd-session session-name bfd1 peer
  #
  interface GigabitEthernet0/2/1.5
   remote-backup-profile p1                                                         
   pppoe-server bind Virtual-Template 1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 4003
   bas                                                                            
    access-type layer2-subscriber default-domain authentication isp1
    client-option82
    authentication-method ppp web
    authentication-method-ipv6 ppp web
  #
  interface GigabitEthernet0/2/1.2
   ipv6 enable
   ipv6 address 2001:db8:8::7 128
   ipv6 address auto link-local
   ip address 10.32.1.1 24
   isis enable 100
   isis ipv6 enable 100
   isis ipv6 cost 50 level-2 
  #                                                                               
  interface LoopBack1                                                           
   ip address 10.1.2.1 32
  #                                                                              
  interface LoopBack100                                                           
   ipv6 enable
   ipv6 address 2001:db8:7::7 127
   ipv6 address auto link-local
   ip address 10.20.1.1 24
   isis enable 100
   isis ipv6 enable 100
  #
  peer-backup route-cost auto-advertising
  #                                                                               
  mpls lsr-id 10.1.1.1
  #                                                                               
  mpls 
   mpls ldp
  #                                                                               
  ospf 1
   default cost inherit-metric
   import-route unr
   area 0
    network 10.1.1.1 0.0.0.0
    network 10.1.2.1 0.0.0.255
  #                                                                               
  isis 100
   is-level level-2
   cost-style wide
   network-entity 10.1111.2222.3333.4444.00
   ipv6 enable topology ipv6                
   ipv6 preference 20
  #                                                                               
  bgp 100
   group group1 internal
   peer group1 connect-interface LoopBack100
   group group2 external
   peer group2 connect-interface LoopBack100
   peer 2001:db8:7::2101 as-number 100
   peer 2001:db8:7::2101 group group1 
   peer 2001:db8:7::2102 as-number 100 
   peer 2001:db8:7::2102 group group1 
   peer 2.2.2.2 as-number 101
   peer 2.2.2.2 group group2 
   peer 3.3.3.3 as-number 101 
   peer 3.3.3.3 group group2                                                                              
   ipv4-family unicast
    import-route unr
   # 
   ipv6-family unicast
    import-route unr
  #
  return                            
  ```
* BRAS2 configuration file
  
  ```
  #
  sysname BRAS2                                                         
  #                                                                               
  bfd
  #  
  bfd bfd2 bind peer-ip 10.1.1.1
   discriminator local 6
   discriminator remote 8                                                  
  #                                                                               
  radius-server group rd1                                                         
   radius-server shared-key-cipher %^%#Q'!i-TMV5&@=QE}g/QK2ouBHee8WB|s|mB%^%
   radius-server authentication 192.168.7.249 1645                        
   radius-server accounting 192.168.7.249 1646 
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1  
    accounting-mode radius
  #
  remote-backup-service s1                      
   peer 10.1.2.1 source 10.1.2.2 port 6001       
   protect lsp-tunnel for-all-instance peer-ip 10.1.2.1  
   track interface GigabitEthernet0/2/0          
   ip-pool pool1
   ipv6-pool pool_nd metric 20
   ipv6-pool pool_pd metric 20
  #
  remote-backup-profile p1                       
   service-type bras         
   backup-id 101 remote-backup-service s1                 
   peer-backup hot                    
   vrrp-id 1 interface GigabitEthernet0/2/1.1
   nas logic-port gigabitethernet 0/2/1
   nas logic-ip 10.10.1.1
  #                                                                               
  ip pool pool1 bas local rui-slave                                                        
   gateway 10.179.180.1 255.255.255.0                                                
   section 0 10.179.180.2 10.179.180.254                                                 
  #
  ipv6 prefix pre_nd delegation
   prefix 2001:db8:1::/48 delegating-prefix-length 64
  #
  ipv6 pool pool_nd bas delegation rui-slave
   prefix pre_nd
   dns-server 2001:db8::2:2 2001:db8::2:3
  #
  ipv6 prefix pre_pd delegation
   prefix 2001:db8:2::/48 delegating-prefix-length 60
  #
  ipv6 pool pool_pd bas delegation rui-slave
   prefix pre_pd
   dns-server 2001:db8::2:2 2001:db8::2:3
  # 
  aaa                                                                             
   domain isp1                                                                    
    authentication-scheme auth1                                                   
    accounting-scheme acct1                                                       
    radius-server group rd1
    prefix-assign-mode unshared  
    ip-pool pool1
    ipv6-pool pool_nd
    ipv6-pool pool_pd
  #
  dhcpv6 duid llt
  #                                                                               
  interface Virtual-Template1                                                     
   ppp authentication-mode chap                                                   
  #
  interface GigabitEthernet0/2/1
  #
  interface GigabitEthernet0/2/1.1
   vlan-type dot1q 200                             
   ip address 10.1.1.2 255.255.255.0            
   vrrp vrid 1 virtual-ip 10.1.1.100            
   admin-vrrp vrid 1                                               
   vrrp vrid 1 preempt-mode timer delay 60       
   vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50                    
   vrrp vrid 1 track bfd-session session-name bfd2 peer
  #
  interface GigabitEthernet0/2/1.5
   remote-backup-profile p1                                                         
   pppoe-server bind Virtual-Template 1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 4003
   bas                                                                            
    access-type layer2-subscriber default-domain authentication isp1
    client-option82
    authentication-method ppp web
    authentication-method-ipv6 ppp web
  #
  interface GigabitEthernet0/2/1.2
   ipv6 enable
   ipv6 address 2001:db8:8::7 128
   ipv6 address auto link-local
   ip address 10.32.1.2 24
   isis enable 100
   isis ipv6 enable 100
   isis ipv6 cost 50 level-2 
  #                                                                               
  interface LoopBack1                                                           
   ip address 10.1.2.2 32
  #                                                                              
  interface LoopBack100                                                           
   ipv6 enable
   ipv6 address 2001:db8:7::7 127
   ipv6 address auto link-local
   ip address 10.20.1.2 24
   isis enable 100
   isis ipv6 enable 100
  #
  peer-backup route-cost auto-advertising
  #                                                                               
  mpls lsr-id 10.1.1.2
  #                                                                               
  mpls 
   mpls ldp
  #                                                                               
  ospf 1
   default cost inherit-metric
   import-route unr
   area 0
    network 10.1.1.2 0.0.0.0
    network 10.1.2.2 0.0.0.255
  #                                                                               
  isis 100
   is-level level-2
   cost-style wide
   network-entity 10.1111.2222.3333.4444.00
   ipv6 enable topology ipv6                
   ipv6 preference 20
  #                                                                               
  bgp 100
   group group1 internal
   peer group1 connect-interface LoopBack100
   group group2 external
   peer group2 connect-interface LoopBack100
   peer 2001:db8:7::2101 as-number 100
   peer 2001:db8:7::2101 group group1 
   peer 2001:db8:7::2102 as-number 100 
   peer 2001:db8:7::2102 group group1 
   peer 2.2.2.2 as-number 101
   peer 2.2.2.2 group group2 
   peer 3.3.3.3 as-number 101 
   peer 3.3.3.3 group group2                                                                              
   ipv4-family unicast
    import-route unr
   # 
   ipv6-family unicast
    import-route unr
  #
  return                           
  ```