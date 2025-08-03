Example for Configuring VE Access for PPPoE Dual-Stack Users in an EVPN Active-Active RUI Scenario
==================================================================================================

This section provides an example for configuring VE access for PPPoE dual-stack users in an EVPN active-active RUI scenario where RADIUS authentication and accounting are performed on a BRAS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0195430308__fig163420251515), the CE is connected to PE1 and PE2 through Eth-Trunk interface. The Eth-Trunk interfaces configured on PE1 and PE2 are added to an E-Trunk to implement the EVPN active-active mode. PE1 and PE2 function as BRASs. A PPPoE dual-stack user goes online through an L3VE sub-interface on a BRAS.

**Figure 1** Example for configuring VE access for PPPoE dual-stack users in an EVPN active-active RUI scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0224617343.png)

| Device | Interface | IPv4 Address | IPv6 Address |
| --- | --- | --- | --- |
| PE1 | Loopback 1 | 1.1.1.1/32 | 2001:db8:1::1/128 |
| PE1 | GE 0/1/1 | 192.168.1.1/24 | 2001:db8:2::1/64 |
| PE2 | Loopback 1 | 2.2.2.2/32 | 2001:db8:3::1/128 |
| PE2 | GE 0/1/1 | 192.168.1.2 /24 | 2001:db8:4::1/64 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each device interface, including loopback interfaces.
2. Configure an Eth-Trunk channel between the CE and each PE.
3. Configure basic MPLS functions and MPLS LDP, and set up MPLS LSPs.
4. Configure an IGP to implement interworking between PEs. In this example, OSPF is used as an IGP.
5. Configure an EVPN instance in BD mode, and bind the BD to the EVPN instance.
6. Configure an EVPN source address.
7. Configure VRRP and BFD on the access side of each PE to control the master/backup status and fault association, and add Eth-Trunk interfaces to an E-Trunk.
8. Configure fast traffic switching.
9. Configure a BGP peer for each PE, and establish an EVPN IBGP peer relationship between PEs.
10. Configure AAA schemes and a RADIUS server group.
11. Configure an IPv4 address pool and an IPv6 address pool, and bind the address pools to a domain.
12. Configure a remote backup service (RBS) and a remote backup policy (RBP).
13. Create two VE interfaces and bind them to the same VE-group.
14. Bind an L2VE sub-interface and an Eth-Trunk sub-interface to the same BD.
15. Configure BRAS access on an L3VE sub-interface.
16. Configure a DUID for the DHCPv6 server.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses
* EVPN instance name
* RADIUS authentication and accounting schemes and their names
* RADIUS server group name and RADIUS server addresses
* Names of an IPv4 address pool and an IPv6 address pool
* Domain to which users belong

#### Procedure

1. Assign an IP address to each device interface, including loopback interfaces. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
2. Configure an Eth-Trunk channel between the CE and each PE.
   
   # Configure the CE.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname CE
   [*HUAWEI] commit
   [~CE] interface gigabitethernet 0/1/0 
   [~CE-GigabitEthernet0/1/0] portswitch
   [*CE-GigabitEthernet0/1/0] port trunk allow-pass vlan 100
   [*CE-GigabitEthernet0/1/0] commit
   [~CE-GigabitEthernet0/1/0] quit
   [~CE] interface Eth-Trunk100
   [*CE-Eth-Trunk100] portswitch
   [*CE-Eth-Trunk100] port trunk allow-pass vlan 100
   [*CE-Eth-Trunk100] mode lacp-static
   [*CE-Eth-Trunk100] commit
   [~CE-Eth-Trunk100] quit
   [~CE]interface GigabitEthernet 0/1/1
   [~CE-GigabitEthernet0/1/1] eth-trunk 100
   [*CE-GigabitEthernet0/1/1] commit
   [~CE-GigabitEthernet0/1/1] quit
   [~CE]interface GigabitEthernet 0/1/2
   [~CE-GigabitEthernet0/1/2] eth-trunk 100
   [*CE-GigabitEthernet0/1/2] commit
   [~CE-GigabitEthernet0/1/2] quit
   ```
   
   # Configure PE1.
   
   The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface Eth-Trunk 100
   [*PE1-Eth-Trunk100] mode lacp-static
   [*PE1-Eth-Trunk100] commit
   [~PE1-Eth-Trunk100] quit
   [~PE1]interface GigabitEthernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] eth-trunk 100
   [*PE1-GigabitEthernet0/1/0] commit
   [~PE1-GigabitEthernet0/1/0] quit
   ```
3. Configure basic MPLS functions and MPLS LDP, and set up MPLS LSPs. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
   ```
   [~PE1] mpls lsr-id 1.1.1.1
   [*PE1] mpls
   [*PE1-mpls] commit
   [~PE1-mpls] quit
   [~PE1] mpls ldp
   [*PE1-mpls-ldp] quit
   [~PE1] interface GigabitEthernet 0/1/1
   [~PE1-GigabitEthernet0/1/1] mpls
   [*PE1-GigabitEthernet0/1/1] mpls ldp
   [*PE1-GigabitEthernet0/1/1] commit
   [~PE1-GigabitEthernet0/1/1] quit
   ```
4. Configure an IGP to implement interworking between PEs. In this example, OSPF is used as an IGP. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
   ```
   [~PE1] ospf 1
   [*PE1-ospf-1] default cost inherit-metric
   [*PE1-ospf-1] import-route direct
   [*PE1-ospf-1] import-route unr
   [*PE1-ospf-1] area 0
   [*PE1-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*PE1-ospf-1-area-0.0.0.0] commit
   [~PE1-ospf-1-area-0.0.0.0] quit
   [~PE1-ospf-1] quit
   ```
5. Configure an EVPN instance in BD mode, and bind the BD to the EVPN instance. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
   ```
   [~PE1] evpn vpn-instance evrf bd-mode
   [*PE1-evpn-instance-evrf] route-distinguisher 1:1
   [*PE1-evpn-instance-evrf] vpn-target 1:1 export-extcommunity
   [*PE1-evpn-instance-evrf] vpn-target 1:1 import-extcommunity
   [*PE1-evpn-instance-evrf] commit
   [~PE1-evpn-instance-evrf] quit
   [~PE1] bridge-domain 100
   [*PE1-bd100] evpn binding vpn-instance evrf
   [*PE1-bd100] commit
   [~PE1-bd100] quit
   ```
6. Configure an EVPN source address.
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 2.2.2.2
   [*PE2] commit
   ```
7. Configure VRRP and BFD on the access side of each PE to control the master/backup status and fault association, and add Eth-Trunk interfaces to an E-Trunk. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
   
   # Configure BFD sessions.
   
   ```
   [~PE1] e-trunk 1
   [*PE1-e-trunk-1] commit
   [~PE1-e-trunk-1] priority 10
   [*PE1-e-trunk-1] peer-address 2.2.2.2 source-address 1.1.1.1
   [*PE1-e-trunk-1] timer hello 9
   [*PE1-e-trunk-1] commit
   [~PE1-e-trunk-1] quit
   [~PE1] bfd
   [~PE1-bfd] quit
   [~PE1] bfd evpn_bfd1 bind peer-ip 2.2.2.2 source-ip 1.1.1.1 track-interface interface Eth-Trunk100
   [*PE1-bfd-session-evpn_bfd1] commit
   [~PE1-bfd-session-evpn_bfd1] discriminator local 5
   [*PE1-bfd-session-evpn_bfd1] discriminator remote 6
   [*PE1-bfd-session-evpn_bfd1] commit
   [~PE1-bfd-session-evpn_bfd1] quit
   [~PE1] bfd evpn_bfd2 bind peer-ip 2.2.2.2 source-ip 1.1.1.1
   [*PE1-bfd-session-evpn_bfd] commit
   [~PE1-bfd-session-evpn_bfd] discriminator local 7
   [*PE1-bfd-session-evpn_bfd] discriminator remote 8
   [*PE1-bfd-session-evpn_bfd] commit
   [~PE1-bfd-session-evpn_bfd] quit
   [~PE1] interface Eth-Trunk 100
   [~PE1-Eth-Trunk100] e-trunk 1
   [*PE1-Eth-Trunk100] e-trunk mode force-master
   [*PE1-Eth-Trunk100] es track bfd evpn_bfd2
   [*PE1-Eth-Trunk100] esi 0001.0002.0003.0004.0005
   [*PE1-Eth-Trunk100] timer es-recovery 120 
   [*PE1-Eth-Trunk100] commit
   [~PE1-Eth-Trunk100] quit
   ```
   # Configure a VRRP group on an interface. (GE 0/1/1.1 is used as an example.)
   ```
   [~PE1] interface GigabitEthernet0/1/1.1
   [*PE1-GigabitEthernet0/1/1.1] commit
   [~PE1-GigabitEthernet0/1/1.1] vlan-type dot1q 2011
   [*PE1-GigabitEthernet0/1/1.1] ip address 192.168.3.1 255.255.255.0
   [*PE1-GigabitEthernet0/1/1.1] vrrp vrid 100 virtual-ip 192.168.3.100
   [*PE1-GigabitEthernet0/1/1.1] admin-vrrp vrid 100
   [*PE1-GigabitEthernet0/1/1.1] vrrp vrid 100 priority 120
   [*PE1-GigabitEthernet0/1/1.1] vrrp vrid 100 preempt-mode timer delay 1800
   [*PE1-GigabitEthernet0/1/1.1] vrrp vrid 100 track bfd-session session-name evpn_bfd1
   [*PE1-GigabitEthernet0/1/1.1] vrrp recover-delay 20
   [*PE1-GigabitEthernet0/1/1.1] commit
   [~PE1-GigabitEthernet0/1/1.1] quit
   ```
8. Configure fast traffic switching. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
   ```
   [~PE1] evpn
   [*PE1-evpn] commit
   [~PE1-evpn] df-election type vlan 
   [*PE1-evpn] vlan-extend private enable
   [*PE1-evpn] vlan-extend redirect enable
   [*PE1-evpn] local-remote frr enable
   [*PE1-evpn] commit
   [~PE1-evpn] mac-duplication
   [~PE1-evpn-mac-dup] quit
   [~PE1-evpn] quit
   ```
9. Configure a BGP peer for each PE, and establish an EVPN IBGP peer relationship between PEs. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
   ```
   [~PE1] interface Loopback1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] ipv6 enable 
   [*PE1-LoopBack1] ip address 1.1.1.1 255.255.255.255
   [*PE1-LoopBack1] ipv6 address 2001:db8:1::1/128
   [*PE1-LoopBack1] ipv6 address auto link-local
   [*PE1-LoopBack1] commit
   [~PE1-evpn] quit
   ```
   ```
   [~PE1] bgp 100
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   [*PE1-bgp] peer 2.2.2.2 connect-interface LoopBack1
   [*PE1-bgp] commit
   [~PE1-bgp] ipv4-family unicast
   [*PE1-bgp-af-ipv4] undo synchronization
   [*PE1-bgp-af-ipv4] import-route direct
   [*PE1-bgp-af-ipv4] import-route unr
   [*PE1-bgp-af-ipv4] peer 2.2.2.2 enable
   [*PE1-bgp-af-ipv4] commit
   [~PE1-bgp-af-ipv4] quit
   [~PE1-bgp] ipv6-family unicast
   [*PE1-bgp-af-ipv6] undo synchronization
   [*PE1-bgp-af-ipv6] import-route direct
   [*PE1-bgp-af-ipv6] import-route unr
   [*PE1-bgp-af-ipv6] peer 2.2.2.2 enable
   [*PE1-bgp-af-ipv6] commit
   [~PE1-bgp-af-ipv6] quit
   [~PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] undo policy vpn-target
   [*PE1-bgp-af-evpn] timer df-delay 0
   [*PE1-bgp-af-evpn] peer 2.2.2.2 enable
   [*PE1-bgp-af-evpn] commit
   [~PE1-bgp-af-evpn] quit
   [~PE1-bgp] quit
   ```
10. Configure AAA schemes and a RADIUS server group. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
    
    # Configure AAA schemes.
    
    ```
    [~PE1] aaa
    [~PE1-aaa] authentication-scheme auth1
    [*PE1-aaa-authen-auth1] authentication-mode radius
    [*PE1-aaa-authen-auth1] quit
    [*PE1-aaa] commit
    [~PE1-aaa] accounting-scheme acct1
    [*PE1-aaa-accounting-acct1] accounting-mode radius
    [*PE1-aaa-accounting-acct1] quit
    [*PE1-aaa] quit
    [*PE1] commit
    ```
    
    # Configure a RADIUS server group.
    
    ```
    [~PE1] radius-server group rd1
    [*PE1-radius-rd1] radius-server authentication 192.168.7.249 1645
    [*PE1-radius-rd1] radius-server accounting 192.168.7.249 1646
    [*PE1-radius-rd1] commit
    [~PE1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
    [*PE1-radius-rd1] commit
    [~PE1-radius-rd1] quit
    ```
11. Configure an IPv4 address pool and an IPv6 address pool, and bind the address pools to a domain. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
    
    # Configure address pools.
    
    ```
    [~PE1] ip pool pool_v4 bas local
    [*PE1-ip-pool-pool_v4] gateway 10.1.1.1 255.255.255.0
    [*PE1-ip-pool-pool_v4] commit
    [~PE1-ip-pool-pool_v4] section 0 10.1.1.2 10.1.1.255
    [~PE1-ip-pool-pool_v4] quit
    [~PE1] ipv6 prefix pre_local local
    [*PE1-ipv6-prefix-pre_local] prefix 2001:db8:5::1/64
    [*PE1-ipv6-prefix-pre_local] commit
    [~PE1-ipv6-prefix-pre_local] quit
    [~PE1] ipv6 pool ipv6_local bas local
    [*PE1-ipv6-pool-ipv6_local] prefix pre_local
    [*PE1-ipv6-pool-ipv6_local] commit
    [~PE1-ipv6-pool-ipv6_local] quit
    [~PE1] ipv6 prefix pre_pd delegation
    [*PE1-ipv6-prefix-pre_pd] prefix 2001:db8::/32
    [*PE1-ipv6-prefix-pre_pd] commit
    [~PE1-ipv6-prefix-pre_pd] pd-unshare-only
    [~PE1-ipv6-prefix-pre_pd] quit
    [~PE1] ipv6 pool pool_pd bas delegation
    [*PE1-ipv6-pool-pool_pd] prefix pre_pd
    [*PE1-ipv6-pool-pool_pd] commit
    [~PE1-ipv6-pool-pool_pd] quit
    ```
    
    # Bind the address pools to a domain.
    
    ```
    [~PE1] aaa
    [~PE1-aaa] domain isp1
    [*PE1-aaa-domain-isp1] authentication-scheme auth1
    [*PE1-aaa-domain-isp1] accounting-scheme acct1
    [*PE1-aaa-domain-isp1] radius-server group rd1
    [*PE1-aaa-domain-isp1] commit
    [~PE1-aaa-domain-isp1] ipv6 nd autoconfig managed-address-flag  
    [~PE1-aaa-domain-isp1] ip-pool pool_v4
    [~PE1-aaa-domain-isp1] ipv6-pool ipv6_local
    [~PE1-aaa-domain-isp1] ipv6-pool pool_pd
    [~PE1-aaa-domain-isp1] quit
    [~PE1-aaa] quit
    ```
12. Configure an RBS and an RBP. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
    
    # Configure an RBS.
    
    ```
    [~PE1] remote-backup-service rbs1
    [*PE1-rm-backup-srv-rbs1] peer 2.2.2.2 source 1.1.1.1 port 50000
    [*PE1-rm-backup-srv-rbs1] commit
    [~PE1-rm-backup-srv-rbs1] track interface GigabitEthernet 0/1/2
    [~PE1-rm-backup-srv-rbs1] protect lsp-tunnel for-all-instance peer-ip 2.2.2.2
    [~PE1-rm-backup-srv-rbs1] ip-pool pool_v4 metric 10
    [~PE1-rm-backup-srv-rbs1] ipv6-pool ipv6_local metric 10
    [~PE1-rm-backup-srv-rbs1] ipv6-pool pool_pd metric 10
    [~PE1-rm-backup-srv-rbs1] quit
    ```
    
    # Configure an RBP.
    
    ```
    [~PE1] remote-backup-profile rbp1
    [*PE1-rm-backup-prf-rbp1] service-type bras
    [*PE1-rm-backup-prf-rbp1] backup-id 1 remote-backup-service rbs1
    [*PE1-rm-backup-prf-rbp1] peer-backup hot
    [*PE1-rm-backup-prf-rbp1] vrrp-id 100 interface GigabitEthernet 0/1/1.1
    [*PE1-rm-backup-prf-rbp1] commit
    [~PE1-rm-backup-prf-rbp1] rui-slave inbound without-forwarding
    [~PE1-rm-backup-prf-rbp1] nas logic-port eth-Trunk 200/0/0
    [*PE1-rm-backup-prf-rbp1] nas logic-sysname huawei
    [*PE1-rm-backup-prf-rbp1] nas logic-ip 172.16.1.1
    [*PE1-rm-backup-prf-rbp1] acct-session-id nas-logic-sysname huawei
    [*PE1-rm-backup-prf-rbp1] commit
    [~PE1-rm-backup-prf-rbp1] quit
    ```
13. Create two VE interfaces and bind them to the same VE-group. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
    ```
    [~PE1] interface virtual-ethernet 0/1/0
    [*PE1-Virtual-Ethernet0/1/0] ve-group 2 l2-terminate
    [*PE1-Virtual-Ethernet0/1/0] quit
    [*PE1] commit
    [~PE1] interface virtual-ethernet 0/1/1
    [*PE1-Virtual-Ethernet0/1/1] ve-group 2 l3-access
    [*PE1-Virtual-Ethernet0/1/1] quit
    [*PE1] commit
    ```
14. Bind an L2VE sub-interface and an Eth-Trunk sub-interface to the same BD. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
    ```
    [~PE1] interface Virtual-Ethernet 0/1/0.1 mode l2
    [*PE1-Virtual-Ethernet0/1/0.1] commit
    [~PE1-Virtual-Ethernet0/1/0.1] encapsulation dot1q vid 100
    [*PE1-Virtual-Ethernet0/1/0.1] bridge-domain 100
    [*PE1-Virtual-Ethernet0/1/0.1] commit
    [~PE1-Virtual-Ethernet0/1/0.1] quit
    [~PE1] interface Eth-Trunk 100.1 mode l2
    [*PE1-Eth-Trunk100.1] commit
    [~PE1-Eth-Trunk100.1] encapsulation dot1q vid 100
    [*PE1-Eth-Trunk100.1] bridge-domain 100
    [*PE1-Eth-Trunk100.1] split-horizon
    [*PE1-Eth-Trunk100.1] commit
    [~PE1-Eth-Trunk100.1] quit
    ```
15. Configure BRAS access on an L3VE sub-interface. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
    ```
    [~PE1] interface virtual-template 1
    [*PE1-interface virtual-template1] ppp authentication-mode chap
    [*PE1-interface virtual-template1] commit
    [~PE1-interface virtual-template1] quit
    [~PE1] interface Virtual-Ethernet 0/1/1.1
    [*PE1-Virtual-Ethernet0/1/1.1] commit
    [~PE1-Virtual-Ethernet0/1/1.1] pppoe-server bind virtual-template 1
    [*PE1-Virtual-Ethernet0/1/1.1] ipv6 enable
    [*PE1-Virtual-Ethernet0/1/1.1] ipv6 address auto link-local
    [*PE1-Virtual-Ethernet0/1/1.1] ipv6 nd autoconfig managed-address-flag
    [*PE1-Virtual-Ethernet0/1/1.1] remote-backup-profile rbp1
    [*PE1-Virtual-Ethernet0/1/1.1] commit
    [~PE1-Virtual-Ethernet0/1/1.1] user-vlan 100
    [~PE1-Virtual-Ethernet0/1/1.1-vlan-100-100] quit
    [~PE1-Virtual-Ethernet0/1/1.1] bas
    [~PE1-Virtual-Ethernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication isp1
    [*PE1-Virtual-Ethernet0/1/1.1-bas] commit
    [~PE1-Virtual-Ethernet0/1/1.1-bas] quit
    [~PE1-Virtual-Ethernet0/1/1.1] quit
    ```
16. Configure a DUID for the DHCPv6 server. The configuration on PE1 is used as an example. Repeat this step for PE2. For configuration details, see [Configuration Files](#EN-US_CONCEPT_0195430308__section1188091525216) in this section.
    ```
    [~PE1] dhcpv6 duid llt
    [*PE1] commit
    ```
17. Verify the configuration.
    
    # After completing the configurations, run the **display remote-backup-profile** command. The command output shows that the backup service type is **bras**, the backup policy **profile1** is bound to the user access interface Virtual-Ethernet 0/1/1.1, and the status of PE1 is **Master**.
    
    ```
    <PE1> display remote-backup-profile rbp1
    ----------------------------------------------------------
     Profile-Index        : 0x802
     Profile-Name         : rbp1
     Service              : bras
     Remote-backup-service: rbs1 
     Backup-ID            : 1
     track protocol       : VRRP
     VRRP-ID              : 100
     VRRP-Interface       : GigabitEthernet0/1/1.1
     Access-Control       : --
     State                : Master
     Peer State           : Slave
     Interface            :
                            Virtual-Ethernet0/1/1.1
     Backup mode          : hot
     Slot-Number          : 1
     Card-Number          : 0
     Port-Number          : 1
     Nas logic-port       : eth-Trunk 200/0/0 
     Nas logic-ip         : 172.16.1.1
     Nas logic-sysname    : huawei 
     Traffic threshold       : 50(MB)
     Traffic interval       : 10(minutes)
     Forwarding Configured: Slave Forwarding 
    ```
    
    # Run the **display remote-backup-service** command to check the RBS configuration on PE1. The command output shows that the TCP connection state (**TCP-State**) of the RBS is **Connected**.
    
    ```
    <PE1> display remote-backup-service rbs1 
    ----------------------------------------------------------
     Service-Index    : 0
     Service-Name     : rbs1
     TCP-State        : Connected
     Peer-ip          : 2.2.2.2 
     Source-ip        : 1.1.1.1 
     TCP-Port         : 2046
     Track-BFD        : --
     Track-interface0 : GigabitEthernet0/1/2
                      Weight : 10
     Track-interface1 : -- 
                      Weight : -- 
     SSL-Policy-Name  : --
     SSL-State        : --
    Uplink state     : 2 (1:DOWN 2:UP)
     Domain-map-list  : --
    ----------------------------------------------------------
    
     ip pool:  
             pool_v4 metric 20
     ipv6 pool: 
             ipv6_local metric 20
             pool_pd metric 20
     Failure ratio    : 100%
     Failure duration : 0 min
    --------------------------------------------------------
    ```

#### Configuration Files

# CE configuration file

```
#
sysname CE                                                       
#
interface Eth-Trunk100
 portswitch
 port trunk allow-pass vlan 100
 mode lacp-static
#
interface GigabitEthernet0/1/0
 portswitch
 undo shutdown
 port trunk allow-pass vlan 100
#
interface GigabitEthernet0/1/1
 undo shutdown
 eth-trunk 100
#
interface GigabitEthernet0/1/2
 undo shutdown
 eth-trunk 100
#
```

# PE1 configuration file

```
#
sysname PE1                                                         
#
dhcpv6 duid 0001000125a7625df063f9761497
#
ipv6 prefix pre_local local
 prefix 2001:db8:5::1/64
#
ipv6 pool ipv6_local bas local
 prefix pre_local
#
ipv6 prefix pre_pd delegation
 prefix 2001:db8::/32
 pd-unshare-only
#
ipv6 pool pool_pd bas delegation
 prefix pre_pd
#                                                                               
radius-server group rd1                                                         
 radius-server shared-key-cipher %^%#Iw/n)xU8oC.hNn6T==./WdM*2:1|w/iSW#T0*o55%^%#
 radius-server authentication 192.168.7.249 1645 weight 0                       
 radius-server accounting 192.168.7.249 1646 weight 0
#
evpn
 df-election type vlan
 vlan-extend private enable
 vlan-extend redirect enable
 local-remote frr enable
 #
 mac-duplication
#
evpn vpn-instance evrf bd-mode
 route-distinguisher 1:1
 vpn-target 1:1 export-extcommunity
 vpn-target 1:1 import-extcommunity
# 
mpls lsr-id 1.1.1.1
#
mpls
#               
mpls ldp
#
bridge-domain 100
 evpn binding vpn-instance evrf
#                                                                           
ip pool pool_v4 bas local                                                         
 gateway 10.1.1.1 255.255.255.0                                                
 section 0 10.1.1.2 10.1.1.255                                                 
#
e-trunk 1
 priority 10
 peer-address 2.2.2.2 source-address 1.1.1.1
 timer hello 9
# 
interface Virtual-Template1  
  ppp authentication-mode chap 
#
remote-backup-service rbs1
 peer 2.2.2.2 source 1.1.1.1 port 50000
 track interface GigabitEthernet0/1/2
 protect lsp-tunnel for-all-instance peer-ip 2.2.2.2
 ip-pool pool_v4 metric 10
 ipv6-pool ipv6_local metric 10
 ipv6-pool pool_pd metric 10
#
remote-backup-profile rbp1
 service-type bras
 backup-id 1 remote-backup-service rbs1
 rui-slave inbound without-forwarding
 peer-backup hot
 vrrp-id 100 interface GigabitEthernet0/1/1.1
 nas logic-port Eth-Trunk 200/0/0
 nas logic-sysname huawei
 nas logic-ip 172.16.1.1
 acct-session-id nas-logic-sysname huawei
#
aaa
 authentication-scheme auth1
  authentication-mode radius
#
 accounting-scheme acct1  
  accounting-mode radius
#                                                                            
 domain isp1                                                                    
  authentication-scheme auth1                                                   
  accounting-scheme acct1                                                       
  radius-server group rd1
  ipv6 nd autoconfig managed-address-flag  
  ip-pool pool_v4
  ipv6-pool ipv6_local
  ipv6-pool pool_pd
#
interface Eth-Trunk100
 mode lacp-static
 e-trunk 1
 e-trunk mode force-master
 es track bfd evpn_bfd2
 esi 0001.0002.0003.0004.0005
 timer es-recovery 120
#
interface Eth-Trunk100.1 mode l2
 encapsulation dot1q vid 100
 bridge-domain 100
 split-horizon
#
interface GigabitEthernet0/1/0
 undo shutdown
 eth-trunk 100
#
interface GigabitEthernet0/1/1
 undo shutdown
 ipv6 enable
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:db8:2::1/64
 ipv6 address auto link-local
 mpls
 mpls ldp
#
interface GigabitEthernet0/1/1.1
 vlan-type dot1q 2011
 ip address 192.168.3.1 255.255.255.0
 vrrp vrid 100 virtual-ip 192.168.3.100
 admin-vrrp vrid 100
 vrrp vrid 100 priority 120
 vrrp vrid 100 preempt-mode timer delay 1800
 vrrp vrid 100 track bfd-session session-name evpn_bfd1
 vrrp recover-delay 20
#                                                                              
interface LoopBack1 
 ipv6 enable
 ip address 1.1.1.1 255.255.255.255
 ipv6 address 2001:db8:1::1/128
 ipv6 address auto link-local
#
interface Virtual-Ethernet0/1/0
 ve-group 2 l2-terminate
#
interface Virtual-Ethernet0/1/0.1 mode l2
 encapsulation dot1q vid 100
 bridge-domain 100
#
interface Virtual-Ethernet0/1/1
 ve-group 2 l3-access
#
interface Virtual-Ethernet0/1/1.1
 ipv6 enable
 ipv6 address auto link-local
 statistic enable
 user-vlan 100
 pppoe-server bind Virtual-Template 1
 ipv6 nd autoconfig managed-address-flag
 remote-backup-profile rbp1
 bas
 #
  access-type layer2-subscriber default-domain authentication isp1
#
bfd evpn_bfd1 bind peer-ip 2.2.2.2 source-ip 1.1.1.1 track-interface interface Eth-Trunk100
 discriminator local 5
 discriminator remote 6
#
bfd evpn_bfd2 bind peer-ip 2.2.2.2 source-ip 1.1.1.1
 discriminator local 7
 discriminator remote 8
#
bgp 100
 peer 2.2.2.2 as-number 100
 peer 2.2.2.2 connect-interface LoopBack1
 #
 ipv4-family unicast
  undo synchronization
  import-route direct
  import-route unr
  peer 2.2.2.2 enable
 #
 ipv6-family unicast
  undo synchronization
  import-route direct
  import-route unr
  peer 2.2.2.2 enable
 #
 l2vpn-family evpn
  undo policy vpn-target
  timer df-delay 0
  peer 2.2.2.2 enable
#
ospf 1
 default cost inherit-metric
 import-route direct
 import-route unr
 area 0.0.0.0
  network 192.168.1.0 0.0.0.255
#
evpn source-address 1.1.1.1
#
return
```

# PE2 configuration file

```
#
sysname PE2                                                         
#
dhcpv6 duid llt                                                                             
# 
interface Virtual-Template1  
  ppp authentication-mode chap 
#
ipv6 prefix pre_local_slave local
 prefix 2001:db8:5::1/64
#
ipv6 pool ipv6_local_slave bas local rui-slave
 prefix pre_local_slave
#
ipv6 prefix pre_pd_slave delegation
 prefix 2001:db8::/32
 pd-unshare-only
#
ipv6 pool pool_pd_slave bas delegation rui-slave
 prefix pre_pd_slave
#                                                                               
radius-server group rd1                                                         
 radius-server shared-key-cipher %^%#Q'!i-TMV5&@=QE}g/QK2ouBHee8WB|s|mB%^%
 radius-server authentication 192.168.7.249 1645 weight 0                       
 radius-server accounting 192.168.7.249 1646 weight 0
#
evpn
 df-election type vlan
 vlan-extend private enable
 vlan-extend redirect enable
 local-remote frr enable
 #
 mac-duplication
#
evpn vpn-instance evrf bd-mode
 route-distinguisher 1:1
 vpn-target 1:1 export-extcommunity
 vpn-target 1:1 import-extcommunity
# 
mpls lsr-id 2.2.2.2
#
mpls
#
bridge-domain 100
 evpn binding vpn-instance evrf
#               
mpls ldp
#                                                                           
ip pool pool_v4_slave bas local rui-slave                                                         
 gateway 10.1.1.1 255.255.255.0                                                
 section 0 10.1.1.2 10.1.1.255                                                 
#
e-trunk 1
 priority 12
 peer-address 1.1.1.1 source-address 2.2.2.2
 timer hello 9
#
remote-backup-service rbs1
 peer 1.1.1.1 source 2.2.2.2 port 50000
 track interface GigabitEthernet0/1/2
 protect lsp-tunnel for-all-instance peer-ip 1.1.1.1
 ip-pool pool_v4_slave metric 20
 ipv6-pool ipv6_local_slave metric 20
 ipv6-pool pool_pd_slave metric 20
#
remote-backup-profile rbp1
 service-type bras
 backup-id 1 remote-backup-service rbs1
 rui-slave inbound without-forwarding
 peer-backup hot
 vrrp-id 100 interface GigabitEthernet0/1/1.1
 nas logic-port Eth-Trunk 200/0/0
 nas logic-sysname huawei
 nas logic-ip 172.16.1.1
 acct-session-id nas-logic-sysname huawei
#
aaa
 authentication-scheme auth1
  authentication-mode radius
#
 accounting-scheme acct1  
  accounting-mode radius
#                                                                            
 domain isp1                                                                    
  authentication-scheme auth1                                                   
  accounting-scheme acct1                                                       
  radius-server group rd1
  ipv6 nd autoconfig managed-address-flag  
  ip-pool pool_v4_slave
  ipv6-pool ipv6_local_slave
  ipv6-pool pool_pd_slave
#
interface Eth-Trunk100
 mode lacp-static
 e-trunk 1
 e-trunk mode force-master
 es track bfd evpn_bfd1
 esi 0001.0002.0003.0004.0005
 timer es-recovery 120
#
interface Eth-Trunk100.1 mode l2
 encapsulation dot1q vid 100
 bridge-domain 100
 split-horizon
#
interface GigabitEthernet0/1/0
 undo shutdown
 eth-trunk 100
#
interface GigabitEthernet0/1/1.1
 vlan-type dot1q 2011
 ip address 192.168.3.2 255.255.255.0
 vrrp vrid 100 virtual-ip 192.168.3.100
 admin-vrrp vrid 100
 vrrp vrid 100 track bfd-session session-name evpn_bfd2
#
interface GigabitEthernet0/1/1
 undo shutdown
 ipv6 enable
 ip address 192.168.1.2 255.255.255.0
 ipv6 address 2001:db8:4::1/64
 ipv6 address auto link-local
 mpls
 mpls ldp
#                                                                              
interface LoopBack1 
 ipv6 enable                                                                                                                                       
 ip address 2.2.2.2 255.255.255.255
 ipv6 address 2001:db8:3::1/128
 ipv6 address auto link-local
#
interface Virtual-Ethernet0/1/0
 ve-group 2 l2-terminate
#
interface Virtual-Ethernet0/1/0.1 mode l2
 encapsulation dot1q vid 100
 bridge-domain 100
#
interface Virtual-Ethernet0/1/1
 ve-group 2 l3-access
#
interface Virtual-Ethernet0/1/1.1
 pppoe-server bind Virtual-Template 1
 ipv6 enable
 ipv6 address auto link-local
 statistic enable
 user-vlan 100
 ipv6 nd autoconfig managed-address-flag
 remote-backup-profile rbp1
 bas
 #
  access-type layer2-subscriber default-domain authentication isp1
#
bfd evpn_bfd1 bind peer-ip 1.1.1.1 source-ip 2.2.2.2
 discriminator local 6
 discriminator remote 5
#
bfd evpn_bfd2 bind peer-ip 1.1.1.1 source-ip 2.2.2.2 track-interface interface Eth-Trunk100
 discriminator local 8
 discriminator remote 7
#
bgp 100
 peer 1.1.1.1 as-number 100
 peer 1.1.1.1 connect-interface LoopBack1
 #
 ipv4-family unicast
  undo synchronization
  import-route direct
  import-route unr
  peer 1.1.1.1 enable
 #
 ipv6-family unicast
  undo synchronization
  import-route direct
  import-route unr
  peer 1.1.1.1 enable
 #
 l2vpn-family evpn
  undo policy vpn-target
  timer df-delay 0
  peer 1.1.1.1 enable
#
ospf 1
 default cost inherit-metric
 import-route direct
 import-route unr
 area 0.0.0.0
  network 192.168.1.0 0.0.0.255
#
evpn source-address 2.2.2.2
#
return
```