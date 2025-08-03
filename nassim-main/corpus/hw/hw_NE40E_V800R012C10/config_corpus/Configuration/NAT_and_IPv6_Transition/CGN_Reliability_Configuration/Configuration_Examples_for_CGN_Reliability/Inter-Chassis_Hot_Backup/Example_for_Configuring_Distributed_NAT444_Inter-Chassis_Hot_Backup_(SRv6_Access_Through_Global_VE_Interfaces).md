Example for Configuring Distributed NAT444 Inter-Chassis Hot Backup (SRv6 Access Through Global VE Interfaces)
==============================================================================================================

This section provides an example for configuring distributed NAT inter-chassis hot backup in scenarios where global VE interfaces are used for SRv6 access.

#### Networking Requirements

In distributed deployment networking shown in [Figure 1](#EN-US_TASK_0000001118405358__fig144014448151), NAT service boards are installed in slot 1 on BRAS1 and slot 1 on BRAS2, respectively. A VRRP channel is established between the two BRASs through global VE interfaces. The master/backup status of the BRASs is determined by the VRRP protocol.

**Figure 1** Distributed inter-chassis backup networking in a scenario where global VE interfaces are used for SRv6 access![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001119361330.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding on devices and configure interface addresses.
2. Configure IS-IS on devices.
3. Configure VPN instances and BGP on the BRASs.
4. Configure SRv6.
5. Configure session resources for service boards and enable HA hot backup.
6. Configure EVPN instances.
7. Configure global VE interfaces and VRRP groups.
8. Create service-location groups.
9. Associate HA with VRRP.
10. Create RBSs and service-instance groups.
11. Configure NAT instances.
12. Configure user information and RADIUS authentication on the BRASs and bind the user groups to the NAT instances.
13. Configure NAT traffic diversion policies and NAT conversion policies.
14. Configure user-side VRRP.
15. Configure RBPs.
16. Bind the NAT instances to the service-instance groups.

#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | Index of the service-location group |
| 2 | Slot ID and CPU ID of the active CPU on a service board of BRAS1 (CPU 0 in slot 1 in this example) |
| 3 | Slot ID and CPU ID of the standby CPU on a service board of BRAS2 (CPU 0 in slot 1 in this example) |
| 4 | Interface IP addresses on the devices at both ends |
| 5 | Names of global-VE interfaces on the devices at both ends |
| 4 | Interfaces and IP addresses of the VRRP channel between the devices at both ends |
| 6 | Indexes, virtual IP addresses, member priorities, and preemption delay of the VRRP groups |
| 10 | Names of the service-instance groups |
| 11 | Names and indexes of the NAT instances |
| 12 | IP address pools, IP addresses of the address pool gateways, and IP address segments of the devices at both ends |
| 13 | Names of the user group and user domain, and AAA schemes on the devices at both ends |
| 14 | Remote backup identifiers for RUI backup on the devices at both ends |
| 15 | User-side interfaces and IP addresses on the devices at both ends |
| 17 | Indexes, virtual IP addresses, priorities, and preemption delay of the user-side VRRP groups on the devices at both ends |




#### Procedure

1. Enable IPv6 and configure IP addresses for interfaces.
   
   
   
   # Configure BRAS1. The configurations of the P and BRAS2 are similar to the configuration of BRAS1. For details, see [BRAS2 configuration file](#EN-US_TASK_0000001118405358__config_02) and [P configuration file](#EN-US_TASK_0000001118405358__li1321121461610).
   
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS1] interface gigabitethernet 0/1/1
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] ipv6 address 2001:DB8:10::1 96
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*BRAS1] interface LoopBack 1
   ```
   ```
   [*BRAS1-LoopBack1] ipv6 enable
   ```
   ```
   [*BRAS1-LoopBack1] ipv6 address 2001:DB8:1::1 64
   ```
   ```
   [*BRAS1-LoopBack1] ip address 10.1.2.1 255.255.255.255
   ```
   ```
   [*BRAS1-LoopBack1] quit
   ```
   ```
   [~BRAS1] interface gigabitethernet 0/1/2
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/2] ip address 10.1.1.1 24
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*BRAS1] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure BRAS1. The configurations of the P and BRAS2 are similar to the configuration of BRAS1. For details, see [BRAS2 configuration file](#EN-US_TASK_0000001118405358__config_02) and [P configuration file](#EN-US_TASK_0000001118405358__li1321121461610).
   
   ```
   [~BRAS1] isis 1
   ```
   ```
   [*BRAS1-isis-1] is-level level-2
   ```
   ```
   [*BRAS1-isis-1] cost-style wide
   ```
   ```
   [*BRAS1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*BRAS1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*BRAS1-isis-1] quit
   ```
   ```
   [*BRAS1-isis-1] interface gigabitethernet 0/1/1
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] isis ipv6 enable 1
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/1] quit
   ```
   ```
   [~BRAS1] interface LoopBack 1
   ```
   ```
   [*BRAS1-Loopback1] isis ipv6 enable 1
   ```
   ```
   [*BRAS1-Loopback1] isis enable 1
   ```
   ```
   [*BRAS1-Loopback1] quit
   ```
   ```
   [*BRAS1] commit
   ```
3. Configure VPN instances and BGP.
   
   
   
   # Configure BRAS1. The configuration of BRAS2 is similar to the configuration of BRAS1. For details, see [BRAS2 configuration file](#EN-US_TASK_0000001118405358__config_02).
   
   ```
   [~BRAS1] ip vpn-instance VPN1
   ```
   ```
   [*BRAS1-vpn-instance-VPN1] vpn-id 100:100
   ```
   ```
   [*BRAS1-vpn-instance-VPN1] ipv4-family
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv4] route-distinguisher 65060:12006 
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv4] apply-label per-route 
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv4] vpn-target 65060:1 export-extcommunity evpn 
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv4] vpn-target 65060:1 export-extcommunity
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv4] vpn-target 65060:1 import-extcommunity evpn 
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv4] vpn-target 65060:1 import-extcommunity
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv4] quit
   ```
   ```
   [*BRAS1-vpn-instance-VPN1] ipv6-family
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv6] route-distinguisher 65060:12006 
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv6] apply-label per-route 
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv6] vpn-target 65060:1 export-extcommunity evpn 
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv6] vpn-target 65060:1 import-extcommunity evpn 
   ```
   ```
   [*BRAS1-vpn-instance-VPN1-af-ipv6] quit
   ```
   ```
   [*BRAS1-vpn-instance-VPN1] quit
   ```
   ```
   [*BRAS1] commit
   ```
   ```
   [~BRAS1] bgp 100
   ```
   ```
   [*BRAS1-bgp] peer 2001:DB8:3::1 as-number 100
   ```
   ```
   [*BRAS1-bgp] peer 2001:DB8:3::1 connect-interface loopBack1
   ```
   ```
   [*BRAS1-bgp] peer 10.2.2.2 as-number 100
   ```
   ```
   [*BRAS1-bgp] peer 10.2.2.2 connect-interface LoopBack1 
   ```
   ```
   [*BRAS1-bgp] ipv4-family unicast 
   ```
   ```
   [*BRAS1-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*BRAS1-bgp-af-ipv4] import-route direct 
   ```
   ```
   [*BRAS1-bgp-af-ipv4] import-route unr
   ```
   ```
   [*BRAS1-bgp-af-ipv4] peer 2001:DB8:3::1 enable
   ```
   ```
   [*BRAS1-bgp-af-ipv4] peer 10.2.2.2 enable
   ```
   ```
   [*BRAS1-bgp-af-ipv4] commit
   ```
   ```
   [~BRAS1-bgp-af-ipv4] quit
   ```
   ```
   [*BRAS1-bgp] ipv6-family unicast 
   ```
   ```
   [*BRAS1-bgp-af-ipv6] undo synchronization
   ```
   ```
   [*BRAS1-bgp-af-ipv6] import-route direct 
   ```
   ```
   [*BRAS1-bgp-af-ipv6] import-route unr
   ```
   ```
   [*BRAS1-bgp-af-ipv6] peer 2001:DB8:3::1 enable
   ```
   ```
   [*BRAS1-bgp-af-ipv6] quit
   ```
   ```
   [*BRAS1-bgp] quit
   ```
   ```
   [*BRAS1] commit
   ```
4. Configure SRv6.
   
   
   
   # Configure BRAS1. The configurations of the P and BRAS2 are similar to the configuration of BRAS1. For details, see [BRAS2 configuration file](#EN-US_TASK_0000001118405358__config_02) and [P configuration file](#EN-US_TASK_0000001118405358__li1321121461610).
   
   
   
   ```
   [~BRAS1] segment-routing ipv6
   ```
   ```
   [*BRAS1-segment-routing-ipv6] encapsulation source-address 2001:DB8:4::1
   ```
   ```
   [*BRAS1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:40:: 64 static 6 args 3
   ```
   ```
   [*BRAS1-segment-routing-ipv6] locator as2 ipv6-prefix 2001:DB8:41:: 64
   ```
   ```
   [*BRAS1-segment-routing-ipv6-locator] quit 
   ```
   ```
   [*BRAS1-segment-routing-ipv6] quit
   ```
   ```
   [*BRAS1] bgp 100
   ```
   ```
   [*BRAS1-bgp] l2vpn-family evpn 
   ```
   ```
   [*BRAS1-bgp-af-evpn] policy vpn-target
   ```
   ```
   [*BRAS1-bgp-af-evpn] peer 2001:DB8:3::1 enable 
   ```
   ```
   [*BRAS1-bgp-af-evpn] peer 2001:DB8:3::1 advertise encap-type srv6
   ```
   ```
   [*BRAS1-bgp-af-evpn] quit
   ```
   ```
   [*BRAS1-bgp] ipv6-family vpn-instance VPN1
   ```
   ```
   [*BRAS1-bgp-6-VPN1] maximum load-balancing 16 
   ```
   ```
   [*BRAS1-bgp-6-VPN1] advertise l2vpn evpn
   ```
   ```
   [*BRAS1-bgp-6-VPN1] segment-routing ipv6 locator as1 evpn 
   ```
   ```
   [*BRAS1-bgp-6-VPN1] segment-routing ipv6 best-effort evpn
   ```
   ```
   [*BRAS1-bgp-6-VPN1] quit
   ```
   ```
   [*BRAS1-bgp] ipv4-family vpn-instance VPN1
   ```
   ```
   [*BRAS1-bgp-VPN1] maximum load-balancing 16
   ```
   ```
   [*BRAS1-bgp-VPN1] advertise l2vpn evpn
   ```
   ```
   [*BRAS1-bgp-VPN1] segment-routing ipv6 locator as1 evpn
   ```
   ```
   [*BRAS1-bgp-VPN1] segment-routing ipv6 best-effort evpn
   ```
   ```
   [*BRAS1-bgp-VPN1] quit
   ```
   ```
   [*BRAS1-bgp] commit 
   ```
   ```
   [~BRAS1-bgp] quit
   ```
   ```
   [~BRAS1] isis 1 
   ```
   ```
   [*BRAS1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   ```
   ```
   [*BRAS1-isis-1] segment-routing ipv6 locator as2 
   ```
   ```
   [*BRAS1-isis-1] commit
   ```
   ```
   [~BRAS1-isis-1] quit
   ```
5. Configure session resources for the service boards and enable HA hot backup on the devices.
   
   
   
   # Configure BRAS1.
   
   ```
   [~BRAS1] vsm on-board-mode disable
   ```
   ```
   [*BRAS1] commit
   ```
   ```
   [~BRAS1] license
   ```
   ```
   [~BRAS1-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*BRAS1-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS1-license] commit
   ```
   ```
   [~BRAS1-license] quit
   ```
   ```
   [~BRAS1] service-ha hot-backup enable
   ```
   ```
   [*BRAS1] commit
   ```
   
   # Configure BRAS2.
   
   ```
   [~BRAS2] vsm on-board-mode disable
   ```
   ```
   [*BRAS2] commit
   ```
   ```
   [~BRAS2] license
   ```
   ```
   [~BRAS2-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*BRAS2-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS2-license] commit
   ```
   ```
   [~BRAS2-license] quit
   ```
   ```
   [~BRAS2] service-ha hot-backup enable
   ```
   ```
   [*BRAS2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The method for configuring bandwidth resources varies according to the board type. As such, determine whether to run the **active nat bandwidth-enhance** command and the corresponding parameters based on the board type.
6. Create EVPN instances.
   
   
   
   # Configure BRAS1.
   
   ```
   [~BRAS1] evpn vpn-instance cgnrui bd-mode
   ```
   ```
   [*BRAS1-evpn-instance-cgnrui] route-distinguisher 1:10
   ```
   ```
   [*BRAS1-evpn-instance-cgnrui] segment-routing ipv6 best-effort
   ```
   ```
   [*BRAS1-evpn-instance-cgnrui] segment-routing ipv6 locator as1
   ```
   ```
   [*BRAS1-evpn-instance-cgnrui] vpn-target 9:10 export-extcommunity
   ```
   ```
   [*BRAS1-evpn-instance-cgnrui] vpn-target 9:10 import-extcommunity
   ```
   ```
   [*BRAS1-evpn-instance-cgnrui] commit
   ```
   ```
   [~BRAS1-evpn-instance-cgnrui] quit
   ```
   ```
   [~BRAS1] bridge-domain 10
   ```
   ```
   [*BRAS1-bd10] evpn binding vpn-instance cgnrui
   ```
   ```
   [*BRAS1-bd10] commit
   ```
   ```
   [~BRAS1-bd10] quit
   ```
   
   # Configure BRAS2.
   
   
   
   ```
   [~BRAS2] evpn vpn-instance cgnrui bd-mode
   ```
   ```
   [*BRAS2-evpn-instance-cgnrui] route-distinguisher 1:9
   ```
   ```
   [*BRAS2-evpn-instance-cgnrui] segment-routing ipv6 best-effort
   ```
   ```
   [*BRAS2-evpn-instance-cgnrui] segment-routing ipv6 locator as1
   ```
   ```
   [*BRAS2-evpn-instance-cgnrui] vpn-target 9:10 export-extcommunity
   ```
   ```
   [*BRAS2-evpn-instance-cgnrui] vpn-target 9:10 import-extcommunity
   ```
   ```
   [*BRAS2-evpn-instance-cgnrui] commit
   ```
   ```
   [~BRAS2-evpn-instance-cgnrui] quit
   ```
   ```
   [~BRAS2] bridge-domain 10
   ```
   ```
   [*BRAS2-bd10] evpn binding vpn-instance cgnrui
   ```
   ```
   [*BRAS2-bd10] commit
   ```
   ```
   [~BRAS2-bd10] quit
   ```
7. Configure global VE interfaces and VRRP groups.
   
   # Configure BRAS1.
   ```
   [~BRAS1] interface Global-VE0
   ```
   ```
   [~BRAS1-Global-VE0] ve-group 2 l3-access
   ```
   ```
   [*BRAS1-Global-VE0] commit
   ```
   ```
   [~BRAS1-Global-VE0] quit
   ```
   ```
   [~BRAS1] interface Global-VE1
   ```
   ```
   [~BRAS1-Global-VE1] ve-group 2 l2-terminate
   ```
   ```
   [*BRAS1-Global-VE1] commit
   ```
   ```
   [~BRAS1-Global-VE1] quit
   ```
   ```
   [~BRAS1] interface Global-VE0.1
   ```
   ```
   [~BRAS1-Global-VE0.1] vlan-type dot1q 11
   ```
   ```
   [*BRAS1-Global-VE0.1] ip binding vpn-instance VPN1
   ```
   ```
   [*BRAS1-Global-VE0.1] ip address 10.10.1.1 255.255.255.0
   ```
   ```
   [*BRAS1-Global-VE0.1] vrrp vrid 1 virtual-ip 10.10.1.3
   ```
   ```
   [*BRAS1-Global-VE0.1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*BRAS1-Global-VE0.1] vrrp vrid 1 priority 200
   ```
   ```
   [*BRAS1-Global-VE0.1] vrrp vrid 1 preempt-mode timer delay 1500
   ```
   ```
   [*BRAS1-Global-VE0.1] vrrp recover-delay 20
   ```
   ```
   [*BRAS1-Global-VE0.1] commit
   ```
   ```
   [~BRAS1-Global-VE0.1] quit
   ```
   ```
   [~BRAS1] interface Global-VE1.1 mode l2
   ```
   ```
   [~BRAS1-Global-VE1.1] encapsulation dot1q vid 11 
   ```
   ```
   [*BRAS1-Global-VE1.1] bridge-domain 10
   ```
   ```
   [*BRAS1-Global-VE1.1] commit
   ```
   ```
   [~BRAS1] quit
   ```
   
   # Configure BRAS2.
   
   ```
   [~BRAS2] interface Global-VE0
   ```
   ```
   [~BRAS2-Global-VE0] ve-group 2 l3-access
   ```
   ```
   [*BRAS2-Global-VE0] commit
   ```
   ```
   [~BRAS2-Global-VE0] quit
   ```
   ```
   [~BRAS2] interface Global-VE1
   ```
   ```
   [~BRAS2-Global-VE1] ve-group 2 l2-terminate
   ```
   ```
   [*BRAS2-Global-VE1] commit
   ```
   ```
   [~BRAS2-Global-VE1] quit
   ```
   ```
   [~BRAS2] interface Global-VE0.1
   ```
   ```
   [~BRAS2-Global-VE0.1] vlan-type dot1q 11
   ```
   ```
   [*BRAS2-Global-VE0.1] ip binding vpn-instance VPN1
   ```
   ```
   [*BRAS2-Global-VE0.1] ip address 10.10.1.2 255.255.255.0
   ```
   ```
   [*BRAS2-Global-VE0.1] vrrp vrid 1 virtual-ip 10.10.1.3
   ```
   ```
   [*BRAS2-Global-VE0.1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*BRAS2-Global-VE0.1] vrrp vrid 1 priority 150
   ```
   ```
   [*BRAS2-Global-VE0.1] commit
   ```
   ```
   [~BRAS2-Global-VE0.1] quit
   ```
   ```
   [~BRAS2] interface Global-VE1.1 mode l2
   ```
   ```
   [~BRAS2-Global-VE1.1] encapsulation dot1q vid 11 
   ```
   ```
   [*BRAS2-Global-VE1.1] bridge-domain 10
   ```
   ```
   [*BRAS2-Global-VE1.1] commit
   ```
   ```
   [~BRAS2] quit
   ```
8. Create a service-location group on BRAS1 and BRAS2, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
   
   
   
   # Configure BRAS1.
   
   ```
   [~BRAS1] service-location 1
   ```
   ```
   [*BRAS1-service-location-1] location slot 1 
   ```
   ```
   [*BRAS1-service-location-1] remote-backup interface Global-VE0.1 peer 10.10.1.2
   ```
   ```
   [*BRAS1-service-location-1] vrrp vrid 1 interface Global-VE0.1
   ```
   ```
   [*BRAS1-service-location-1] commit
   ```
   ```
   [~BRAS1-service-location-1] quit
   ```
   
   # Configure BRAS2.
   
   ```
   [~BRAS2] service-location 1
   ```
   ```
   [*BRAS2-service-location-1] location slot 1 
   ```
   ```
   [*BRAS2-service-location-1] remote-backup interface Global-VE0.1 peer 10.10.1.1
   ```
   ```
   [*BRAS2-service-location-1] vrrp vrid 1 interface Global-VE0.1
   ```
   ```
   [*BRAS2-service-location-1] commit
   ```
   ```
   [~BRAS2-service-location-1] quit
   ```
9. Associate HA with VRRP.
   
   
   
   # Configure BRAS1.
   
   ```
   [~BRAS1] interface Global-VE0.1
   ```
   ```
   [~BRAS1-Global-VE0.1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*BRAS1-Global-VE0.1] commit
   ```
   ```
   [~BRAS1-Global-VE0.1] quit
   ```
   
   # Configure BRAS2.
   
   ```
   [~BRAS2] interface Global-VE0.1
   ```
   ```
   [~BRAS2-Global-VE0.1] vrrp vrid 1 track service-location 1 reduced 60
   ```
   ```
   [*BRAS2-Global-VE0.1] commit
   ```
   ```
   [~BRAS2-Global-VE0.1] quit
   ```
10. Configure RBSs, create service-instance groups, and bind the service-instance groups to the service-location groups.
    
    # Configure BRAS1.
    ```
    [~BRAS1] remote-backup-service rui
    ```
    ```
    [*BRAS1-rm-backup-srv-rui] peer 10.1.2.2 source 10.1.2.1 port 6001
    ```
    ```
    [*BRAS1-rm-backup-srv-rui] protect lsp-tunnel for-all-instance peer-ip 10.1.2.2
    ```
    ```
    [*BRAS1-rm-backup-srv-rui] commit
    ```
    ```
    [~BRAS1-rm-backup-srv-rui] quit
    ```
    ```
    [~BRAS1] service-instance-group group1
    ```
    ```
    [*BRAS1-service-instance-group-group1] service-location 1
    ```
    ```
    [*BRAS1-service-instance-group-group1] remote-backup-service rui
    ```
    ```
    [*BRAS1-service-instance-group-group1] commit
    ```
    ```
    [~BRAS1-service-instance-group-group1] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] remote-backup-service rui
    ```
    ```
    [*BRAS2-rm-backup-srv-rui] peer 10.1.2.1 source 10.1.2.2 port 6001
    ```
    ```
    [*BRAS2-rm-backup-srv-rui] protect lsp-tunnel for-all-instance peer-ip 10.1.2.1
    ```
    ```
    [*BRAS2-rm-backup-srv-rui] commit
    ```
    ```
    [~BRAS2-rm-backup-srv-rui] quit
    ```
    ```
    [~BRAS2] service-instance-group group1
    ```
    ```
    [*BRAS2-service-instance-group-group1] service-location 1
    ```
    ```
    [*BRAS2-service-instance-group-group1] remote-backup-service rui
    ```
    ```
    [*BRAS2-service-instance-group-group1] commit
    ```
    ```
    [~BRAS2-service-instance-group-group1] quit
    ```
11. Create NAT instances.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] nat instance nat id 1
    ```
    ```
    [*BRAS1-nat-instance-nat] commit
    ```
    ```
    [~BRAS1-nat-instance-nat] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] nat instance nat id 1
    ```
    ```
    [*BRAS2-nat-instance-nat] commit
    ```
    ```
    [~BRAS2-nat-instance-nat] quit
    ```
12. Configure user information (user group named **natbras**, IP address pool named **natbras**, user domain named **natbras**, and AAA) on BRAS1 and BRAS2 and bind the user groups to the NAT instance named **nat**.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] user-group natbras
    ```
    ```
    [~BRAS1] commit
    ```
    ```
    [~BRAS1] ip pool natbras bas local
    ```
    ```
    [*BRAS1-ip-pool-natbras] gateway 192.168.0.1 255.255.0.0
    ```
    ```
    [*BRAS1-ip-pool-natbras] commit
    ```
    ```
    [~BRAS1-ip-pool-natbras] section 0 192.168.0.2 192.168.0.254
    ```
    ```
    [~BRAS1-ip-pool-natbras] quit
    ```
    ```
    [~BRAS1] remote-backup-service rui
    ```
    ```
    [*BRAS1-rm-backup-srv-rui] ip-pool natbras
    ```
    ```
    [*BRAS1-rm-backup-srv-rui] commit
    ```
    ```
    [~BRAS1-rm-backup-srv-rui] quit
    ```
    ```
    [~BRAS1] radius-server group rd1
    ```
    ```
    [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
    ```
    ```
    [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
    ```
    ```
    [*BRAS1-radius-rd1] radius-server shared-key YsHsjx_202206
    ```
    ```
    [*BRAS1-radius-rd1] commit
    ```
    ```
    [~BRAS1-radius-rd1] radius-server type plus11
    ```
    ```
    [~BRAS1-radius-rd1] radius-server traffic-unit kbyte
    ```
    ```
    [~BRAS1-radius-rd1] quit
    ```
    ```
    [~BRAS1] aaa
    ```
    ```
    [~BRAS1-aaa] authentication-scheme auth1
    ```
    ```
    [*BRAS1-aaa-authen-auth1] authentication-mode radius
    ```
    ```
    [*BRAS1-aaa-authen-auth1] commit
    ```
    ```
    [~BRAS1-aaa-authen-auth1] quit
    ```
    ```
    [~BRAS1-aaa] accounting-scheme acct1
    ```
    ```
    [*BRAS1-aaa-accounting-acct1] accounting-mode radius
    ```
    ```
    [~BRAS1-aaa-accounting-acct1] commit
    ```
    ```
    [~BRAS1-aaa-accounting-acct1] quit
    ```
    ```
    [~BRAS1-aaa] domain natbras
    ```
    ```
    [*BRAS1-aaa-domain-natbras] authentication-scheme auth1
    ```
    ```
    [*BRAS1-aaa-domain-natbras] accounting-scheme acct1
    ```
    ```
    [*BRAS1-aaa-domain-natbras] radius-server group rd1
    ```
    ```
    [*BRAS1-aaa-domain-natbras] commit
    ```
    ```
    [~BRAS1-aaa-domain-natbras] ip-pool natbras
    ```
    ```
    [~BRAS1-aaa-domain-natbras] user-group natbras bind nat instance nat
    ```
    ```
    [~BRAS1-aaa-domain-natbras] quit
    ```
    ```
    [~BRAS1-aaa] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] user-group natbras
    ```
    ```
    [~BRAS2] commit
    ```
    ```
    [~BRAS2] ip pool natbras bas local
    ```
    ```
    [*BRAS2-ip-pool-natbras] gateway 192.168.0.1 255.255.0.0
    ```
    ```
    [*BRAS2-ip-pool-natbras] commit
    ```
    ```
    [~BRAS2-ip-pool-natbras] section 0 192.168.0.2 192.168.0.254
    ```
    ```
    [~BRAS2-ip-pool-natbras] quit
    ```
    ```
    [~BRAS2] remote-backup-service rui
    ```
    ```
    [*BRAS2-rm-backup-srv-rui] ip-pool natbras
    ```
    ```
    [*BRAS2-rm-backup-srv-rui] commit
    ```
    ```
    [~BRAS2-rm-backup-srv-rui] quit
    ```
    ```
    [~BRAS2] radius-server group rd1
    ```
    ```
    [*BRAS2-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
    ```
    ```
    [*BRAS2-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
    ```
    ```
    [*BRAS2-radius-rd1] radius-server shared-key YsHsjx_202206
    ```
    ```
    [*BRAS2-radius-rd1] commit
    ```
    ```
    [~BRAS2-radius-rd1] radius-server type plus11
    ```
    ```
    [~BRAS2-radius-rd1] radius-server traffic-unit kbyte
    ```
    ```
    [~BRAS2-radius-rd1] quit
    ```
    ```
    [~BRAS2] aaa
    ```
    ```
    [~BRAS2-aaa] authentication-scheme auth1
    ```
    ```
    [*BRAS2-aaa-authen-auth1] authentication-mode radius
    ```
    ```
    [*BRAS2-aaa-authen-auth1] commit
    ```
    ```
    [~BRAS2-aaa-authen-auth1] quit
    ```
    ```
    [~BRAS2-aaa] accounting-scheme acct1
    ```
    ```
    [*BRAS2-aaa-accounting-acct1] accounting-mode radius
    ```
    ```
    [~BRAS2-aaa-accounting-acct1] commit
    ```
    ```
    [~BRAS2-aaa-accounting-acct1] quit
    ```
    ```
    [~BRAS2-aaa] domain natbras
    ```
    ```
    [*BRAS2-aaa-domain-natbras] authentication-scheme auth1
    ```
    ```
    [*BRAS2-aaa-domain-natbras] accounting-scheme acct1
    ```
    ```
    [*BRAS2-aaa-domain-natbras] radius-server group rd1
    ```
    ```
    [*BRAS2-aaa-domain-natbras] commit
    ```
    ```
    [~BRAS2-aaa-domain-natbras] ip-pool natbras
    ```
    ```
    [~BRAS2-aaa-domain-natbras] user-group natbras bind nat instance nat
    ```
    ```
    [~BRAS2-aaa-domain-natbras] quit
    ```
    ```
    [~BRAS2-aaa] quit
    ```
13. Configure traffic classification rules, NAT behaviors, and NAT traffic diversion policies, and apply the NAT traffic diversion policies on the master and backup devices.
    
    
    
    # Configure a NAT conversion policy on BRAS1.
    
    1. Configure an ACL numbered 6001 and an ACL rule numbered 1.
       
       ```
       [~BRAS1] acl 6001
       ```
       ```
       [*BRAS1-acl-ucl-6001] rule 1 permit ip source user-group natbras
       ```
       ```
       [*BRAS1-acl-ucl-6001] commit
       ```
       ```
       [~BRAS1-acl-ucl-6001] quit
       ```
    2. Configure ACL 3001 that is used for IP address assignment during user login.
       
       ```
       [~BRAS1] acl 3001
       ```
       ```
       [*BRAS1-acl4-advance-3001] rule 10 permit ip source 192.168.0.0 0.0.255.255
       ```
       ```
       [*BRAS1-acl4-advance-3001] commit
       ```
       ```
       [~BRAS1-acl4-advance-3001] quit
       ```
    3. Configure a traffic classifier.
       
       ```
       [~BRAS1] traffic classifier c1
       ```
       ```
       [*BRAS1-classifier-c1] if-match acl 6001
       ```
       ```
       [*BRAS1-classifier-c1] commit
       ```
       ```
       [~BRAS1-classifier-c1] quit
       ```
    4. Configure a traffic behavior.
       
       ```
       [~BRAS1] traffic behavior b1 
       ```
       ```
       [*BRAS1-behavior-b1] nat bind instance nat
       ```
       ```
       [*BRAS1-behavior-b1] commit
       ```
       ```
       [~BRAS1-behavior-b1] quit
       ```
    5. Define a traffic policy to associate the traffic classifier with the traffic behavior.
       
       ```
       [~BRAS1] traffic policy p1
       ```
       ```
       [*BRAS1-trafficpolicy-p1] classifier c1 behavior b1
       ```
       ```
       [*BRAS1-trafficpolicy-p1] commit
       ```
       ```
       [~BRAS1-trafficpolicy-p1] quit
       ```
    6. Apply the NAT traffic diversion policy in the system view.
       
       ```
       [~BRAS1] traffic-policy p1 inbound
       ```
       ```
       [*BRAS1] commit
       ```
    7. Configure a NAT conversion policy.
       
       ```
       [~BRAS1] nat instance nat
       ```
       ```
       [~BRAS1-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
       ```
       ```
       [*BRAS1-nat-instance-nat] nat outbound 3001 address-group address-group1
       ```
       ```
       [*BRAS1-nat-instance-nat] commit
       ```
       ```
       [~BRAS1-nat-instance-nat] quit
       ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of BRAS2 is similar to the configuration of BRAS1. For configuration details, see [BRAS2 configuration file](#EN-US_TASK_0000001118405358__config_02).
14. On each of the master and backup devices, configure a user-side VRRP group (between BRAS1/BRAS2 and SWITCH) and enable it to track the service-location group. If the service-location group is not tracked, a CGN board failure cannot trigger a master/backup BRAS switchover. As a result, new distributed NAT users cannot go online.
    
    
    
    # On BRAS1, configure a user-side VRRP group (between BRAS1 and SWITCH).
    
    ```
    [~BRAS1] interface GigabitEthernet 0/1/2
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2] ip address 10.1.1.1 255.255.255.0
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2] vrrp vrid 2 virtual-ip 10.1.1.3
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2] admin-vrrp vrid 2
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2] vrrp vrid 2 priority 180
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2] vrrp vrid 2 preempt-mode timer delay 1500
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2] vrrp recover-delay 20
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2] vrrp vrid 2 track service-location 1 reduced 50
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2] quit
    ```
    
    # On BRAS2, configure a user-side VRRP group (between BRAS2 and SWITCH).
    
    ```
    [~BRAS2] interface GigabitEthernet 0/1/2
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2] ip address 10.1.1.2 255.255.255.0
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2] vrrp vrid 2 virtual-ip 10.1.1.3
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2] admin-vrrp vrid 2
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2] vrrp vrid 2 priority 120
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2] vrrp vrid 2 track service-location 1
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.] quit
    ```
15. Configure an RBP for backing up BRAS information on each of the devices.
    
    
    
    # Configure an RBP named **natbras** on BRAS1.
    
    ```
    [~BRAS1] remote-backup-profile natbras
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] service-type bras
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] backup-id 10 remote-backup-service natbras
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] peer-backup hot
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] vrrp-id 2 interface GigabitEthernet0/1/2
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] commit
    ```
    ```
    [~BRAS1-rm-backup-prf-natbras] quit
    ```
    
    
    
    # Configure an RBP named **natbras** on BRAS2.
    
    ```
    [~BRAS2] remote-backup-profile natbras
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] service-type bras
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] backup-id 10 remote-backup-service natbras
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] peer-backup hot
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] vrrp-id 2 interface GigabitEthernet0/1/2
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] commit
    ```
    ```
    [~BRAS2-rm-backup-prf-natbras] quit
    ```
16. Bind service-instance groups to NAT instances.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] nat instance nat id 1
    ```
    ```
    [~BRAS1-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*BRAS1-nat-instance-nat] commit
    ```
    ```
    [~BRAS1-nat-instance-nat] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] nat instance nat id 1
    ```
    ```
    [~BRAS2-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*BRAS2-nat-instance-nat] commit
    ```
    ```
    [~BRAS2-nat-instance-nat] quit
    ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1
  #
  vsm on-board-mode disable
  #
  service-ha hot-backup enable
  #
  evpn vpn-instance cgnrui bd-mode
   route-distinguisher 1:10
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator as1
   vpn-target 9:10 export-extcommunity
   vpn-target 9:10 import-extcommunity
  #
  ip vpn-instance VPN1
   vpn-id 100:100
   ipv4-family
    route-distinguisher 65060:12006
    apply-label per-route
    vpn-target 65060:1 export-extcommunity evpn
    vpn-target 65060:1 export-extcommunity
    vpn-target 65060:1 import-extcommunity evpn
    vpn-target 65060:1 import-extcommunity
   ipv6-family
    route-distinguisher 65060:12006
    apply-label per-route
    vpn-target 65060:1 export-extcommunity evpn
    vpn-target 65060:1 import-extcommunity evpn
  #
  service-location 1
   location slot 1 
   remote-backup interface Global-VE0.1 peer 10.10.1.2
   vrrp vrid 1 interface Global-VE0.1
  #
  service-instance-group group1
   service-location 1
   remote-backup-service rui
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105 
   nat outbound 3001 address-group address-group1
  #
  bridge-domain 10
   evpn binding vpn-instance cgnrui
  #
  ip pool natbras bas local
   gateway 192.168.0.1 255.255.0.0
   section 0 192.168.0.2 192.168.0.254
  #
  user-group natbras
  #
  remote-backup-service rui
   peer 10.1.2.2 source 10.1.2.1 port 6001
   protect lsp-tunnel for-all-instance peer-ip 10.1.2.2
   ip-pool natbras
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 2 interface GigabitEthernet0/1/2
  #
  acl number 3001
   rule 10 permit ip source 192.168.0.0 0.0.255.255
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1 precedence 1
  #
  traffic-policy p1 inbound
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
   radius-server type plus11
   radius-server traffic-unit kbyte
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1
    accounting-mode radius
   domain natbras
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool natbras
    user-group natbras bind nat instance nat
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:4::1
   locator as1 ipv6-prefix 2001:DB8:40:: 64 static 6 args 3
   locator as2 ipv6-prefix 2001:DB8:41:: 64
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   segment-routing ipv6 locator as2
   #
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/96
   isis enable 1
   isis ipv6 enable 1
   dcn
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 2 virtual-ip 10.1.1.3
   admin-vrrp vrid 2
   vrrp vrid 2 priority 180
   vrrp vrid 2 preempt-mode timer delay 1500
   vrrp recover-delay 20
   vrrp vrid 2 track service-location 1 reduced 50
   dcn
  #
  interface LoopBack1
   ipv6 enable
   ip address 10.1.2.1 255.255.255.255
   ipv6 address 2001:DB8:1::1/64
   isis enable 1
   isis ipv6 enable 1
  #
  interface Global-VE0
   ve-group 2 l3-access
  #
  interface Global-VE0.1
   vlan-type dot1q 11
   ip binding vpn-instance VPN1
   ip address 10.10.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.10.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp recover-delay 20
   vrrp vrid 1 track service-location 1 reduced 60
  #
  interface Global-VE1
   ve-group 2 l2-terminate
  #
  interface Global-VE1.1 mode l2
   encapsulation dot1q vid 11
   bridge-domain 10
  #
  bgp 100
   router-id 10.10.1.1
   peer 10.2.2.2 as-number 100
   peer 10.2.2.2 connect-interface LoopBack1
   peer 2001:DB8:3::1 as-number 100
   peer 2001:DB8:3::1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    import-route unr
    unicast-route recursive-lookup tunnel-v6 tunnel-selector srv6
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer
    peer 10.2.2.2 enable
    peer 2001:DB8:3::1 enable
   #
   ipv6-family unicast
    undo synchronization
    import-route direct
    import-route unr
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer
    peer 2001:DB8:3::1 enable
   #
   ipv4-family vpn-instance VPN1
    maximum load-balancing 16
    advertise l2vpn evpn
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 best-effort evpn
   #
   ipv6-family vpn-instance VPN1
    maximum load-balancing 16
    advertise l2vpn evpn
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 best-effort evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::1 enable
    peer 2001:DB8:3::1 advertise encap-type srv6
  #
  return
  ```
* BRAS2 configuration file
  
  ```
  #
  sysname BRAS2
  #
  vsm on-board-mode disable
  #
  service-ha hot-backup enable
  #
  evpn vpn-instance cgnrui bd-mode
   route-distinguisher 1:9
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator as1
   vpn-target 9:10 export-extcommunity
   vpn-target 9:10 import-extcommunity
  #
  ip vpn-instance VPN1
   vpn-id 100:100
   ipv4-family
    route-distinguisher 65060:12006
    apply-label per-route
    vpn-target 65060:1 export-extcommunity evpn
    vpn-target 65060:1 export-extcommunity
    vpn-target 65060:1 import-extcommunity evpn
    vpn-target 65060:1 import-extcommunity
   ipv6-family
    route-distinguisher 65060:12006
    apply-label per-route
    vpn-target 65060:1 export-extcommunity evpn
    vpn-target 65060:1 import-extcommunity evpn
  #
  service-location 1
   location slot 1 
   remote-backup interface Global-VE0.1 peer 10.10.1.1
   vrrp vrid 1 interface Global-VE0.1
  #
  service-instance-group group1
   service-location 1
   remote-backup-service rui
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105 
   nat outbound 3001 address-group address-group1
  #
  bridge-domain 10
   evpn binding vpn-instance cgnrui
  #
  ip pool natbras bas local
   gateway 192.168.0.1 255.255.0.0
   section 0 192.168.0.2 192.168.0.254
  #
  user-group natbras
  #
  remote-backup-service rui
   peer 10.1.2.1 source 10.1.2.2 port 6001
   protect lsp-tunnel for-all-instance peer-ip 10.1.2.1
   ip-pool natbras
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 2 interface GigabitEthernet0/1/2
  #
  acl number 3001
   rule 10 permit ip source 192.168.0.0 0.0.255.255
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1 precedence 1
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
   radius-server type plus11
   radius-server traffic-unit kbyte
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1
    accounting-mode radius
   domain natbras
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool natbras
    user-group natbras bind nat instance nat
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::1
   locator as1 ipv6-prefix 2001:DB8:30:: 64 static 6 args 3
   locator as2 ipv6-prefix 2001:DB8:31:: 64
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   segment-routing ipv6 locator as2
   #
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::2/96
   isis enable 1
   isis ipv6 enable 1
   dcn
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 2 virtual-ip 10.1.1.3
   admin-vrrp vrid 2
   vrrp vrid 2 priority 120
   vrrp vrid 2 track service-location 1
   dcn
  #
  interface LoopBack1
   ipv6 enable
   ip address 10.1.2.2 255.255.255.255
   ipv6 address 2001:DB8:3::1/64
   isis enable 1
   isis ipv6 enable 1
  #
  interface Global-VE0
   ve-group 2 l3-access
  #
  interface Global-VE0.1
   vlan-type dot1q 11
   ip binding vpn-instance VPN1
   ip address 10.10.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.10.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 150
   vrrp vrid 1 track service-location 1 reduced 60
  #
  interface Global-VE1
   ve-group 2 l2-terminate
  #
  interface Global-VE1.1 mode l2
   encapsulation dot1q vid 11
   bridge-domain 10
  #
  bgp 100
   router-id 10.10.10.10
   peer 10.2.2.3 as-number 100
   peer 10.2.2.3 connect-interface LoopBack1
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    import-route unr
    unicast-route recursive-lookup tunnel-v6 tunnel-selector srv6
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer
    peer 10.2.2.3 enable
    peer 2001:DB8:1::1 enable
   #
   ipv6-family unicast
    undo synchronization
    import-route direct
    import-route unr
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer
    peer 2001:DB8:1::1 enable
   #
   ipv4-family vpn-instance VPN1
    maximum load-balancing 16
    advertise l2vpn evpn
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 best-effort evpn
   #
   ipv6-family vpn-instance VPN1
    maximum load-balancing 16
    advertise l2vpn evpn
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 best-effort evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
  #
  return
  ```
* P configuration file
  ```
  #
  sysname P
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator as1 ipv6-prefix 2001:DB8:20:: 64 static 6 args 3
   locator as2 ipv6-prefix 2001:DB8:21:: 64 static 6
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::2/96
   isis enable 1
   isis ipv6 enable 1
   dcn
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/96
   isis enable 1
   isis ipv6 enable 1
   dcn
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   isis ipv6 enable 1
  #
  return
  ```