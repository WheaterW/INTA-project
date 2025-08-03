Example for Configuring IPoE Dual-Stack User Access (Web+MAC Authentication) in a Dual-Device Hot Backup Scenario
=================================================================================================================

This section provides an example for configuring IPoE dual-stack access through web+MAC authentication in a dual-device hot backup scenario. When IPoE dual-stack users connect to BRASs and web+MAC authentication is used, the BRASs implement RADIUS authentication and accounting, assign IPv4 addresses from the local address pool, and assign IPv6 addresses through DHCPv6 ND. This allows the users to access the network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001206474186__fig_dc_ne_cfg_bras_000901), IPv4/IPv6 dual-stack users access the network through web authentication. The BRASs use RADIUS authentication and accounting. When each user accesses the network for the first time, the user enters a MAC authentication domain, and the username and password required during web authentication. The RADIUS server automatically records the association between the terminal's MAC address and the entered username and password. After that, the user can automatically access the network with no need for repeatedly entering the username and password. This process is called MAC authentication. If the authentication fails, the user will be redirected to a web authentication domain. Users in a web authentication domain can access only limited network resources, such as the web server. In this example, the web server and web authentication server are deployed on the same device. If the user accesses unauthorized network resources, the user will be forcibly redirected to the specified web server. After the user re-enters the correct username and password and the authentication succeeds, the user becomes a post-authentication domain user and can access network resources normally. When the user logs in to the network next time, the BRASs perform MAC authentication based on the terminal's MAC address. To improve network reliability, dual-device hot backup also needs to be deployed. If a fault occurs, a master/backup device switchover needs to be triggered to prevent user services from being interrupted and users from being aware of the fault.

**Figure 1** Configuring IPoE dual-stack user access (web+MAC authentication) in a dual-device hot backup scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent Eth-Trunk2 and GE0/1/0, respectively.


![](figure/en-us_image_0000001206816318.png)

**Table 1** Interfaces and IP addresses
| **Device** | **Interface Name** | **Interface Number** | **IP Address** |
| --- | --- | --- | --- |
| BRAS1 | interface1 | Eth-trunk2 | - |
| interface1 | Eth-trunk2.1 | 192.168.4.129/29 |
| interface2 | GE0/1/0 | 10.2.1.1/24, 2001:db8:8::7/128 |
| - | Loopback1 | 10.2.2.2/24, 2001:db8::2:2/64 |
| - | Loopback2 | 10.3.3.3/24 |
| BRAS2 | interface1 | Eth-trunk2 | - |
| interface1 | Eth-trunk2.1 | 192.168.4.130/29 |
| interface2 | GE0/1/0 | 10.4.1.1/24, 2001:db8:9::7/128 |
| - | Loopback1 | 10.4.4.4/24, 2001:db8::3:3/64 |
| - | Loopback2 | 10.13.13.13/24 |





#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure a routing protocol.
3. Create a MAC authentication domain named **mac-domain**, a web authentication domain named **web-domain**, and a post-authentication domain named **after-domain**.
4. Configure AAA schemes and a RADIUS server group.
5. Configure address pools.
6. Enable MAC authentication in the MAC authentication domain **mac-domain** and bind the RADIUS server group and authentication scheme to the domain.
7. Configure a web authentication domain named **web-domain** in which users can access only limited network resources. Bind the non-authentication scheme and non-accounting scheme to this domain.
8. Configure ACL rules for web authentication domain **web-domain**.
9. Bind post-authentication domain **after-domain** to the RADIUS accounting scheme and RADIUS authentication scheme.
10. In the AAA view, configure the MAC address carried in user access request packets as the pure username.
11. Configure DUIDs for the devices.
12. On a BAS interface, enable IPv6 and configure a MAC authentication domain, post-authentication domain, and authentication method.
13. Configure a BFD session and VRRP on the access side of the master and backup BRASs.
14. Configure an RBS and an RBP.

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   # Configure IP addresses for network-side interfaces.
   
   
   
   ```
   [~BRAS1] interface gigabitEthernet 0/1/0
   [*BRAS1-GigabitEthernet0/1/0] ipv6 enable 
   [*BRAS1-GigabitEthernet0/1/0] ipv6 address 2001:db8:8::7 128
   [*BRAS1-GigabitEthernet0/1/0] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/1/0] ip address 10.2.1.1 24
   [*BRAS1-GigabitEthernet0/1/0] quit
   [*BRAS1-GigabitEthernet0/1/0] commit
   [*BRAS1] interface Loopback1
   [*BRAS1-Loopback1] ipv6 enable
   [*BRAS1-Loopback1] ipv6 address 2001:db8::2:2 64
   [*BRAS1-Loopback1] ipv6 address auto link-local
   [*BRAS1-Loopback1] ip address 10.2.2.2 24
   [*BRAS1-Loopback1] quit
   [*BRAS1] commit
   ```
   
   # Configure an IP address for the protection tunnel.
   
   ```
   [~BRAS1] interface loopback2
   [*BRAS1-Loopback2] ip address 10.3.3.3 24
   [*BRAS1-Loopback2] quit
   [*BRAS1] commit
   ```
2. Configure a routing protocol.
   
   
   
   # Enable the function to automatically control a route's cost preference.
   
   ```
   [~BRAS1] peer-backup route-cost auto-advertising
   [*BRAS1] commit
   ```
   
   # Configure MPLS.
   
   ```
   [~BRAS1] mpls
   [~BRAS1-mpls] mpls ldp
   [~BRAS1-mpls] quit
   [~BRAS1] mpls lsr-id 10.3.3.3
   [*BRAS1] interface GigabitEthernet0/1/0
   [*BRAS1-GigabitEthernet0/1/0] mpls
   [*BRAS1-GigabitEthernet0/1/0] mpls ldp
   [*BRAS1-GigabitEthernet0/1/0] quit
   [*BRAS1] commit
   ```
   
   # Configure OSPF to import UNRs.
   
   ```
   [~BRAS1] ospf 1
   [*BRAS1-ospf-1] default cost inherit-metric
   [*BRAS1-ospf-1] import-route unr
   [*BRAS1-ospf-1] area 0
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.3.3.3 0.0.0.0
   [*BRAS1-ospf-1-area-0.0.0.0] quit
   [*BRAS1-ospf-1] quit
   [*BRAS1] commit
   ```
3. Create a MAC authentication domain named **mac-domain**, a web authentication domain named **web-domain**, and a post-authentication domain named **after-domain**.
   
   
   ```
   [~BRAS] system-view
   [~BRAS] web-auth-server source 10.32.1.1
   [*BRAS] sysname BRAS1
   [*BRAS] commit
   [~BRAS1] aaa
   [~BRAS1-aaa] domain mac-domain
   [*BRAS1-aaa-domain-mac-domain] quit
   [*BRAS1-aaa] domain web-domain
   [*BRAS1-aaa-domain-web-domain] quit
   [*BRAS1-aaa] domain after-domain
   [*BRAS1-aaa-domain-after-domain] quit
   [*BRAS1-aaa] commit
   [~BRAS1-aaa] quit 
   ```
4. Configure AAA schemes and a RADIUS server group.
   
   
   
   # Create UDP sockets with the local port numbers 1645, 1646, and 3799 and with any local IP address.
   
   ```
   [~BRAS1] radius local-ip all
   [*BRAS1] commit
   ```
   
   # Create a RADIUS server group.
   
   ```
   [~BRAS1] radius-server group rd1
   [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
   [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
   [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   [*BRAS1-radius-rd1] radius-server source interface loopback1
   [*BRAS1-radius-rd1] commit 
   [~BRAS1-radius-rd1] quit
   ```
   
   # Create an authentication scheme named **portal-mac-auth**, and configure the BRASs to redirect the dual-stack user to web authentication domain **web-domain** if web authentication fails.
   
   ```
   [~BRAS1] aaa
   [*BRAS1-aaa] authentication-scheme portal-mac-auth
   [*BRAS1-aaa-authen-portal-mac-auth] commit 
   [~BRAS1-aaa-authen-portal-mac-auth] authening authen-fail online authen-domain web-domain
   [~BRAS1-aaa-authen-portal-mac-auth] quit
   ```
   
   # Configure an authentication scheme named **radius**, with RADIUS authentication specified.
   
   ```
   [~BRAS1-aaa] authentication-scheme radius
   [*BRAS1-aaa-authen-radius] authentication-mode radius
   [*BRAS1-aaa-authen-radius] commit
   [~BRAS1-aaa-authen-radius] quit
   ```
   
   # Configure an authentication scheme named **none**, with non-authentication specified. In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, and protocol. For examples in secure environments, see [Example for Configuring RADIUS for User Authentication and Accounting](dc_ne_aaa_cfg_0401.html).
   
   ```
   [~BRAS1-aaa] authentication-scheme none
   [*BRAS1-aaa-authen-none] authentication-mode none
   [*BRAS1-aaa-authen-none] commit
   [~BRAS1-aaa-authen-none] quit
   ```
   
   # Configure an accounting scheme named **radius**, with RADIUS accounting specified.
   
   ```
   [~BRAS1-aaa] accounting-scheme radius
   [*BRAS1-aaa-accounting-radius] accounting-mode radius
   [*BRAS1-aaa-accounting-radius] commit
   [~BRAS1-aaa-accounting-radius] quit
   ```
   
   # Configure an accounting scheme named **none**, with non-accounting specified.
   
   ```
   [~BRAS1-aaa] accounting-scheme none
   [*BRAS1-aaa-accounting-none] accounting-mode none
   [*BRAS1-aaa-accounting-none] commit
   [~BRAS1-aaa-accounting-none] quit
   [~BRAS1-aaa] quit
   ```
5. Configure address pools.
   
   # Configure an IPv4 address pool.
   ```
   [~BRAS1] ip pool pool_v4 bas local
   [*BRAS1-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0
   [*BRAS1-ip-pool-pool_v4] commit
   [~BRAS1-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.200 
   [~BRAS1-ip-pool-pool_v4] dns-server 10.1.6.2
   [*BRAS1-ip-pool-pool_v4] quit
   [*BRAS1] commit
   ```
   
   # Configure IPv6 address pools.
   ```
   [~BRAS1] ipv6 prefix pre_nd_1 local
   [*BRAS1-ipv6-prefix-pre_nd_1] prefix 2001:db8:1::/48
   [*BRAS1-ipv6-prefix-pre_nd_1] slaac-unshare-only
   [*BRAS1-ipv6-prefix-pre_nd_1] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 pool pool_nd_1 bas local
   [*BRAS1-ipv6-pool-pool_nd_1] prefix pre_nd_1
   [*BRAS1-ipv6-pool-pool_nd_1] dns-server 2001:db8:11::1
   [*BRAS1-ipv6-pool-pool_nd_1] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 prefix pre_nd_2 local
   [*BRAS1-ipv6-prefix-pre_nd_2] prefix 2001:db8:2::/48
   [*BRAS1-ipv6-prefix-pre_nd_2] slaac-unshare-only
   [*BRAS1-ipv6-prefix-pre_nd_2] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 pool pool_nd_2 bas local rui-slave
   [*BRAS1-ipv6-pool-pool_nd_2] prefix pre_nd_2
   [*BRAS1-ipv6-pool-pool_nd_2] dns-server 2001:db8:12::1
   [*BRAS1-ipv6-pool-pool_nd_2] quit
   [*BRAS1] commit
   ```
6. Enable MAC authentication in MAC authentication domain **mac-domain**, and bind it to RADIUS server group **rd1** and authentication scheme **portal-mac-auth**.
   
   
   ```
   [~BRAS1-aaa] domain mac-domain
   [~BRAS1-aaa-domain-mac-domain] radius-server group rd1
   [*BRAS1-aaa-domain-mac-domain] authentication-scheme portal-mac-auth
   [*BRAS1-aaa-domain-mac-domain] accounting-scheme radius
   [*BRAS1-aaa-domain-mac-domain] commit
   [~BRAS1-aaa-domain-mac-domain] prefix-assign-mode unshared 
   [~BRAS1-aaa-domain-mac-domain] ip-pool pool_v4
   [~BRAS1-aaa-domain-mac-domain] ipv6-pool pool_nd_1
   [~BRAS1-aaa-domain-mac-domain] mac-authentication enable
   [~BRAS1-aaa-domain-mac-domain] quit
   [~BRAS1-aaa] quit
   ```
7. Configure a web authentication domain named **web-domain** in which users can access only limited network resources. Bind the non-authentication scheme and non-accounting scheme to this domain.
   
   
   ```
   [~BRAS1] user-group web-group
   [~BRAS1] aaa
   [~BRAS1-aaa] domain web-domain
   [~BRAS1-aaa-domain-web-domain] authentication-scheme none
   [*BRAS1-aaa-domain-web-domain] accounting-scheme none
   [*BRAS1-aaa-domain-web-domain] commit
   [~BRAS1-aaa-domain-web-domain] prefix-assign-mode unshared
   [~BRAS1-aaa-domain-web-domain] ip-pool pool_v4
   [~BRAS1-aaa-domain-web-domain] ipv6-pool pool_nd1
   [~BRAS1-aaa-domain-web-domain] user-group web-group
   [~BRAS1-aaa-domain-web-domain] web-server 10.1.1.10
   [~BRAS1-aaa-domain-web-domain] web-server url http://www.isp1.com
   [~BRAS1-aaa-domain-web-domain] web-server identical-url
   [~BRAS1-aaa-domain-web-domain] quit
   [~BRAS1-aaa] quit
   ```
   
   # Configure the addresses carried in the Portal packets received by the BRASs from the web authentication server.
   
   ```
   [~BRAS1] interface LoopBack 0
   [*BRAS1-LoopBack0] ipv6 enable
   [*BRAS1-LoopBack0] ip address 10.1.1.1 32
   [*BRAS1-LoopBack0] ipv6 address 2001:db8:1::3 128
   [*BRAS1-LoopBack0] ipv6 address auto link-local
   [*BRAS1-LoopBack0] commit
   [~BRAS1-LoopBack0] quit
   ```
   
   # Configure the web authentication server.
   
   ```
   [~BRAS1] web-auth-server source-ip 10.1.1.1
   [~BRAS1] web-auth-server enable
   [~BRAS1] web-auth-server source interface LoopBack 0
   [~BRAS1] web-auth-server 10.1.1.10 key cipher YsHsjx_202206
   [~BRAS1] web-auth-server version v2 v1
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   V1.0 does not provide the authenticator, and therefore no encryption is needed. The V2.0 authenticator uses MD5 encryption that has low security, potentially bringing security risks. For security purposes, you are advised not to use V2.0 or V1.0. If they are required, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
8. Configure ACL rules for web authentication domain **web-domain**.
   
   
   
   # Configure IPv4 ACL rules.
   
   * Configure ACL 6000 to permit the traffic between user group **web-group** and web authentication server and between user group **web-group** and the DNS server.
     ```
     [~BRAS1] acl number 6000
     [*BRAS1-acl-ucl-6000] rule 10 permit ip source user-group web-group destination ip-address 10.1.6.2 0
     [*BRAS1-acl-ucl-6000] rule 20 permit ip source user-group web-group destination ip-address 10.1.1.10 0
     [*BRAS1-acl-ucl-6000] commit
     [~BRAS1-acl-ucl-6000] quit
     ```
   * Configure ACL 6001 to allow HTTP redirection for the TCP packets originating from user group **web-group** and carrying destination port www or 8080.
     ```
     [~BRAS1] acl number 6001
     [*BRAS1-acl-ucl-6001] rule 5 permit tcp source user-group web-group destination-port eq www
     [*BRAS1-acl-ucl-6001] rule 10 permit tcp source user-group web-group destination-port eq 8080
     [*BRAS1-acl-ucl-6001] commit
     [~BRAS1-acl-ucl-6001] quit
     ```
   * Configure ACL 6002 to deny all the traffic originating from user group **web-group**.
     ```
     [~BRAS1] acl number 6002
     [*BRAS1-acl-ucl-6002] rule 5 permit ip source ip-address any destination user-group web-group
     [*BRAS1-acl-ucl-6002] rule 10 permit ip source user-group web-group destination ip-address any
     [*BRAS1-acl-ucl-6002] commit
     [~BRAS1-acl-ucl-6002] quit
     ```
   
   # Configure IPv6 ACL rules.
   
   * Configure ACL 6000 to permit the traffic between user group **web-group** and web authentication server and between user group **web-group** and the DNS server.
     ```
     [~BRAS1] acl ipv6 number 6000
     [*BRAS1-acl6-ucl-6000] rule 5 permit ipv6 source user-group web-group destination ipv6-address 2001:db8:1::1/128
     [*BRAS1-acl6-ucl-6000] commit
     [~BRAS1-acl6-ucl-6000] quit
     ```
   * Configure ACL 6001 to allow HTTP redirection for the TCP packets originating from user group **web-group** and carrying destination port www or 8080.
     ```
     [~BRAS1] acl ipv6 number 6001
     [*BRAS1-acl6-ucl-6001] rule 5 permit tcp source user-group web-group destination-port eq www
     [*BRAS1-acl6-ucl-6001] rule 10 permit tcp source user-group web-group destination-port eq 8080
     [*BRAS1-acl6-ucl-6001] commit
     [~BRAS1-acl6-ucl-6001] quit
     ```
   * Configure ACL 6002 to deny all the traffic originating from user group **web-group**.
     ```
     [~BRAS1] acl ipv6 number 6002
     [*BRAS1-acl6-ucl-6002] rule 5 permit ipv6 source ipv6-address any destination user-group web-group
     [*BRAS1-acl6-ucl-6002] rule 10 permit ipv6 source user-group web-group destination ipv6-address any
     [*BRAS1-acl6-ucl-6002] commit
     [~BRAS1-acl6-ucl-6002] quit
     ```# Configure a traffic policy.
   ```
   [~BRAS1] traffic classifier 6000
   [*BRAS1-classifier-6000] if-match acl 6000
   [*BRAS1-classifier-6000] if-match ipv6 acl 6000
   [*BRAS1-classifier-6000] quit
   [*BRAS1] traffic classifier 6001
   [*BRAS1-classifier-6001] if-match acl 6001
   [*BRAS1-classifier-6001] if-match ipv6 acl 6001
   [*BRAS1-classifier-6001] quit
   [*BRAS1] traffic classifier 6002
   [*BRAS1-classifier-6002] if-match acl 6002
   [*BRAS1-classifier-6002] if-match ipv6 acl 6002
   [*BRAS1-classifier-6002] quit
   [*BRAS1] traffic behavior permit
   [*BRAS1-behavior-permit] permit
   [*BRAS1-behavior-permit] quit
   [*BRAS1] traffic behavior in-deny
   [*BRAS1-behavior-in-deny] deny
   [*BRAS1-behavior-in-deny] quit
   [*BRAS1] traffic behavior redirect
   [*BRAS1-behavior-redirect] http-redirect plus
   [*BRAS1-behavior-redirect] quit
   [*BRAS1] traffic policy before-auth-in
   [*BRAS1-trafficpolicy-before-auth-in] share-mode
   [*BRAS1-trafficpolicy-before-auth-in] classifier 6000 behavior permit
   [*BRAS1-trafficpolicy-before-auth-in] classifier 6001 behavior redirect
   [*BRAS1-trafficpolicy-before-auth-in] classifier 6002 behavior in-deny
   [*BRAS1-trafficpolicy-before-auth-in] quit
   ```
   
   # Apply the traffic policy in the system view.
   
   ```
   [*BRAS1] traffic-policy before-auth-in inbound
   [*BRAS1] commit
   ```
9. Configure a post-authentication domain named **after-domain** and bind it to the RADIUS accounting template and RADIUS authentication template.
   
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain after-domain
   [~BRAS1-aaa-domain-after-domain] authentication-scheme radius
   [*BRAS1-aaa-domain-after-domain] accounting-scheme radius
   [*BRAS1-aaa-domain-after-domain] commit
   [~BRAS1-aaa-domain-after-domain] prefix-assign-mode unshared
   [~BRAS1-aaa-domain-after-domain] ip-pool pool_v4
   [~BRAS1-aaa-domain-after-domain] ipv6-pool pool_nd1
   [~BRAS1-aaa-domain-after-domain] radius-server group rd1
   [~BRAS1-aaa-domain-after-domain] quit
   ```
10. In the AAA view, configure the MAC address carried in user access request packets as the pure username.
    
    
    ```
    [~BRAS1-aaa] default-user-name include mac-address -
    [*BRAS1-aaa] commit
    [~BRAS1-aaa] default-password cipher YsHsjx_202206
    [*BRAS1-aaa] commit
    [~BRAS1-aaa] quit
    ```
11. Configure a DUID for the device.
    
    
    ```
    [~BRAS1] dhcpv6 duid 12345678
    [*BRAS1] commit
    ```
12. Configure a BAS interface.
    
    
    
    # Configure the Eth-Trunk interface to work in static LACP mode and set a timeout period for the interface to receive LACPDUs.
    
    ```
    [~BRAS1] interface Eth-Trunk2
    [*BRAS1-Eth-Trunk2] mode lacp-static
    [*BRAS1-Eth-Trunk2] lacp timeout fast
    [*BRAS1-Eth-Trunk2] commit
    ```
    
    # Configure a BAS interface.
    
    ```
    [~BRAS1-Eth-Trunk2] interface Eth-Trunk2.10
    [*BRAS1-Eth-Trunk2.10] ipv6 enable
    [*BRAS1-Eth-Trunk2.10] ipv6 address auto link-local
    [*BRAS1-Eth-Trunk2.10] commit
    [~BRAS1-Eth-Trunk2.10] user-vlan 2001
    [~BRAS1-Eth-Trunk2.10-user-vlan-2001] quit
    [~BRAS1-Eth-Trunk2.10] bas
    [~BRAS1-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain pre-authentication mac-domain authentication after-domain
    [*BRAS1-Eth-Trunk2.10-bas] authentication-method web
    [*BRAS1-Eth-Trunk2.10-bas] authentication-method-ipv6 web
    [*BRAS1-Eth-Trunk2.10-bas] commit
    [~BRAS1-Eth-Trunk2.10-bas] quit
    [~BRAS1-Eth-Trunk2.10] quit
    ```
13. Configure a BFD session and VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
    
    
    
    # Configure a BFD session on the access side to allow the device to rapidly detect interface or link faults and trigger a master/backup VRRP switchover upon such a fault.
    
    ```
    [~BRAS1] bfd
    [*BRAS1-bfd] quit
    [*BRAS1] bfd bfd1 bind peer-ip 192.168.4.130
    [*BRAS1-bfd-session-bfd1] discriminator local 1
    [*BRAS1-bfd-session-bfd1] discriminator remote 1
    [*BRAS1-bfd-session-bfd1] quit 
    [*BRAS1] commit
    ```
    
    # Configure a VRRP group on an interface/sub-interface (sub-interface Eth-Trunk2.1 is used in this example), and configure VRRP to track the BFD session and network-side interface. Set the VRRP preemption delay to 1800s.
    
    ```
    [~BRAS1] interface Eth-Trunk2.1              
    [*BRAS1-Eth-Trunk2.1] vlan-type dot1q 96                           
    [*BRAS1-Eth-Trunk2.1] ip address 192.168.4.129 255.255.255.248            
    [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 virtual-ip 192.168.4.131   
    [*BRAS1-Eth-Trunk2.1] admin-vrrp vrid 5           
    [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 priority 120 
    [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 preempt-mode timer delay 1800 
    [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 track interface GigabitEthernet 0/1/0 reduced 50 
    [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 track bfd-session session-name bfd1 link
    [*BRAS1-Eth-Trunk2.1] commit
    [~BRAS1-Eth-Trunk2.1] quit
    [~BRAS1] vrrp recover-delay 300
    [*BRAS1] commit
    ```
14. Configure an RBS and an RBP.
    
    
    
    # Configure an RBS, and configure the device to use the NAS IP address as the source IP address in packets replied to the RADIUS server.
    
    ```
    [~BRAS1] peer-backup route-cost auto-advertising
    [~BRAS1] remote-backup-service s1
    [*BRAS1-rm-backup-srv-s1] peer 10.13.13.13 source 10.3.3.3 port 6001
    [*BRAS1-rm-backup-srv-s1] track interface GigabitEthernet 0/1/0
    [*BRAS1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
    [*BRAS1-rm-backup-srv-s1] ip-pool pool_v4 metric 10
    [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_nd_1 metric 10
    [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_nd_2 metric 20
    [*BRAS1-rm-backup-srv-s1] radius-authorization source same-as nas-logic-ip
    [*BRAS1-rm-backup-srv-s1] quit
    [*BRAS1] commit
    ```
    
    # Configure an RBP, and configure a logical IP address, logical interface, and logical hostname, so that the active and standby devices use the same NAS-IP-Address, NAS-Port, NAS-Port-ID, and Option 82 information in the packets sent to the RADIUS and DHCP servers.
    
    ```
    [~BRAS1] remote-backup-profile p1
    [*BRAS1-rm-backup-prf-p1] service-type bras
    [*BRAS1-rm-backup-prf-p1] peer-backup hot
    [*BRAS1-rm-backup-prf-p1] backup-id 5 remote-backup-service s1
    [*BRAS1-rm-backup-prf-p1] vrrp-id 5 interface Eth-Trunk2.1
    [*BRAS1-rm-backup-prf-p1] nas logic-port Eth-Trunk2 
    [*BRAS1-rm-backup-prf-p1] nas logic-ip 10.10.1.1
    [*BRAS1-rm-backup-prf-p1] nas logic-sysname huawei
    [*BRAS1-rm-backup-prf-p1] quit
    [*BRAS1] commit
    ```
    
    # Bind the RBP to the interface through which users go online.
    
    ```
    [~BRAS1] interface Eth-Trunk2.10
    [*BRAS1-Eth-Trunk2.10] remote-backup-profile p1
    [*BRAS1-Eth-Trunk2.10] quit
    [*BRAS1] commit
    ```

#### Configuration Files

* BRAS1 configuration file

```
#
sysname BRAS1
#
radius-server group rd1                                                       
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% 
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server source interface LoopBack1
# 
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.1.6.2
#
ipv6 prefix pre_nd_1 local                                                   
 prefix 2001:DB8:1::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd_1 bas local                                                
 dns-server 2001:DB8:11::1                                         
 prefix pre_nd_1                                                                  
#
ipv6 prefix pre_nd_2 local                                                   
 prefix 2001:DB8:2::/48 
 slaac-unshare-only
#                                                                               
ipv6 pool pool_nd_2 bas local rui-slave                                                
 dns-server 2001:DB8:12::1                                         
 prefix pre_nd_2                                                                  
#
user-group web-group
#
acl number 6000
 rule 5 permit ip source user-group web-group destination ip-address 10.1.6.2 0
 rule 10 permit ip source user-group web-group destination ip-address 10.1.1.10 0
#
acl number 6001
 rule 5 permit tcp source user-group web-group destination-port eq www
 rule 10 permit tcp source user-group web-group destination-port eq 8080
#
acl number 6002
 rule 5 permit ip source ip-address any destination user-group web-group
 rule 10 permit ip source user-group web-group destination ip-address any
#
acl ipv6 number 6000
 rule 5 permit ipv6 source user-group web-group destination ipv6-address 2001:DB8:1::1/128
#
acl ipv6 number 6001
 rule 5 permit tcp source user-group web-group destination-port eq www
 rule 10 permit tcp source user-group web-group destination-port eq 8080
#
acl ipv6 number 6002
 rule 5 permit ipv6 source ipv6-address any destination user-group web-group
 rule 10 permit ipv6 source user-group web-group destination ipv6-address any
#
dhcpv6 duid 12345678
#
traffic classifier 6000 operator or
 if-match acl 6000 precedence 1
 if-match ipv6 acl 6000 precedence 2
#
traffic classifier 6001 operator or
 if-match acl 6001 precedence 3
 if-match ipv6 acl 6001 precedence 4
#
traffic classifier 6002 operator or
 if-match acl 6002 precedence 5
 if-match ipv6 acl 6002 precedence 6
#
traffic behavior in-deny
 deny
#
traffic behavior permit
#
traffic behavior redirect
 http-redirect plus
#
traffic policy before-auth-in
 share-mode
 classifier 6000 behavior permit precedence 1
 classifier 6001 behavior redirect precedence 2
 classifier 6002 behavior in-deny precedence 3
#
radius local-ip all
#
bfd
#
bfd bfd1 bind peer-ip 192.168.4.130
 discriminator local 1 
 discriminator remote 1
#
mpls lsr-id 10.3.3.3
#
mpls
#
mpls ldp
#
aaa
 default-password cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
 default-user-name include mac-address -
 #
 authentication-scheme none
  authentication-mode none
 #
 authentication-scheme radius
  authentication-mode radius local
 #
 authentication-scheme portal-mac-auth
  authening authen-fail online authen-domain web-domain
 #
 accounting-scheme radius
 #
 accounting-scheme none
  accounting-mode none
 #
 domain mac-domain
  authentication-scheme portal-mac-auth
  accounting-scheme radius
  radius-server group rd1
  prefix-assign-mode unshared
  ip-pool pool_v4
  ipv6-pool pool_nd1
  ipv6-pool pool_nd2
  mac-authentication enable
  #
 domain web-domain
  authentication-scheme none
  accounting-scheme none
  prefix-assign-mode unshared
  ip-pool pool_v4
  ipv6-pool pool_nd1
  user-group web-group
  web-server 10.1.1.10
  web-server url http://www.isp1.com
  web-server identical-url
 #
 domain after-domain
  authentication-scheme radius
  accounting-scheme radius
  radius-server group group1
  prefix-assign-mode unshared
  ip-pool pool_v4
  ipv6-pool pool_nd1
  user-group web-group
#                                                                               
interface Eth-Trunk2                                                      
 pppoe-server bind Virtual-Template 5                                           
 mode lacp-static                                                               
 lacp timeout fast                                                              
#
interface  Eth-Trunk2.1
 vlan-type dot1q 96
 ip address 192.168.4.129 255.255.255.248
 vrrp vrid 5 virtual-ip 192.168.4.131
 admin-vrrp vrid 5
 vrrp vrid 5 priority 120
 vrrp vrid 5 preempt-mode timer delay 1800
 vrrp vrid 5 track interface GigabitEthernet0/1/0 reduced 50
 vrrp vrid 5 track bfd-session session-name bfd1 link
#
peer-backup route-cost auto-advertising
#
remote-backup-service s1
 peer 10.13.13.13 source 10.3.3.3 port 6001
 track interface GigabitEthernet0/1/0
 protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
 ip-pool pool_v4 metric 10
 ipv6-pool pool_nd_1 metric 10
 ipv6-pool pool_nd_2 metric 20
 radius-authorization source same-as nas-logic-ip
#
remote-backup-profile p1
 service-type bras
 backup-id 5 remote-backup-service s1
 peer-backup hot
 vrrp-id 5 interface Eth-Trunk2.1
 nas logic-port Eth-Trunk2 
 nas logic-ip 10.10.1.1
 nas logic-sysname huawei
#
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                   
 statistic enable                                                               
 user-vlan 2001
 remote-backup-profile p1                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain pre-authentication mac-domain authentication after-domain            
  authentication-method web
  authentication-method-ipv6 web  
 #                                                                              
#                                                                               
interface GigabitEthernet0/1/0                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.2.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:8::7/64                                                 
 ipv6 address auto link-local
 mpls
 mpls ldp
#
interface LoopBack0
 ipv6 enable
 ip address 10.1.1.1 32
 ipv6 address 2001:DB8:1::3 128
 ipv6 address auto link-local
#
interface LoopBack1
 ipv6 enable
 ip address 10.2.2.2 255.255.255.0
 ipv6 address 2001:DB8::2:2/64
 ipv6 address auto link-local
#
interface LoopBack2
 ip address 10.3.3.3 255.255.255.0
#
web-auth-server enable
web-auth-server 10.1.1.10 port 50100 key cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%#
web-auth-server source interface LoopBack0
web-auth-server version v2 v1
#
undo web-auth-server source-ip all
web-auth-server source-ip 10.1.1.1
#
traffic-policy before-auth-in inbound
#
ospf 1
 default cost inherit-metric
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.2.1.0 0.0.0.255
  network 10.3.3.3 0.0.0.0
#
vrrp recover-delay 300
#
return
```

* BRAS2 configuration file

```
#
sysname BRAS2
#
radius-server group rd1                                                       
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% 
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server source interface LoopBack1
# 
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.1.6.2
#
ipv6 prefix pre_nd_1 local                                                   
 prefix 2001:DB8:1::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd_1 bas local                                                
 dns-server 2001:DB8:11::1                                         
 prefix pre_nd_1                                                                  
#
ipv6 prefix pre_nd_2 local                                                   
 prefix 2001:DB8:2::/48 
 slaac-unshare-only
#                                                                               
ipv6 pool pool_nd_2 bas local rui-slave                                                
 dns-server 2001:DB8:12::1                                         
 prefix pre_nd_2                                                                  
#
user-group web-group
#
acl number 6000
 rule 5 permit ip source user-group web-group destination ip-address 10.1.6.2 0
 rule 10 permit ip source user-group web-group destination ip-address 10.1.1.10 0
#
acl number 6001
 rule 5 permit tcp source user-group web-group destination-port eq www
 rule 10 permit tcp source user-group web-group destination-port eq 8080
#
acl number 6002
 rule 5 permit ip source ip-address any destination user-group web-group
 rule 10 permit ip source user-group web-group destination ip-address any
#
acl ipv6 number 6000
 rule 5 permit ipv6 source user-group web-group destination ipv6-address 2001:DB8:1::2/128
 #
acl ipv6 number 6001
 rule 5 permit tcp source user-group web-group destination-port eq www
 rule 10 permit tcp source user-group web-group destination-port eq 8080
#
acl ipv6 number 6002
 rule 5 permit ipv6 source ipv6-address any destination user-group web-group
 rule 10 permit ipv6 source user-group web-group destination ipv6-address any
#
dhcpv6 duid 12345678
#
traffic classifier 6000 operator or
 if-match acl 6000 precedence 1
 if-match ipv6 acl 6000 precedence 2
#
traffic classifier 6001 operator or
 if-match acl 6001 precedence 3
 if-match ipv6 acl 6001 precedence 4
#
traffic classifier 6002 operator or
 if-match acl 6002 precedence 5
 if-match ipv6 acl 6002 precedence 6
#
traffic behavior in-deny
 deny
#
traffic behavior permit
#
traffic behavior redirect
 http-redirect plus
#
traffic policy before-auth-in
 share-mode
 classifier 6000 behavior permit precedence 1
 classifier 6001 behavior redirect precedence 2
 classifier 6002 behavior in-deny precedence 3
#
radius local-ip all
#
bfd
#
bfd bfd1 bind peer-ip 192.168.4.129
 discriminator local 1 
 discriminator remote 1
#
mpls lsr-id 10.13.13.13
#
mpls
#
mpls ldp
#
aaa
 default-password cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
 default-user-name include mac-address -
 #
 authentication-scheme none
  authentication-mode none
 #
 authentication-scheme radius
  authentication-mode radius local
 #
 authentication-scheme portal-mac-auth
  authening authen-fail online authen-domain web-domain
 #
 accounting-scheme radius
 #
 accounting-scheme none
  accounting-mode none
 #
 domain mac-domain
  authentication-scheme portal-mac-auth
  accounting-scheme radius
  radius-server group rd1
  prefix-assign-mode unshared
  ip-pool pool_v4
  ipv6-pool pool_nd2
  mac-authentication enable
  #
 domain web-domain
  authentication-scheme none
  accounting-scheme none
  prefix-assign-mode unshared
  ip-pool pool_v4
  ipv6-pool pool_nd2
  user-group web-group
  web-server 10.1.1.10 2001:DB8:1::2
  web-server url http://www.isp1.com
  web-server identical-url
 #
 domain after-domain
  authentication-scheme radius
  accounting-scheme radius
  radius-server group group1
  prefix-assign-mode unshared
  ip-pool pool_v4
  ipv6-pool pool_nd2
  user-group web-group
#                                                                               
interface Eth-Trunk2                                                      
 pppoe-server bind Virtual-Template 5                                           
 mode lacp-static                                                               
 lacp timeout fast                                                              
#
interface Eth-Trunk2.1
 vlan-type dot1q 96
 ip address 192.168.4.130 255.255.255.248
 vrrp vrid 5 virtual-ip 192.168.4.131
 admin-vrrp vrid 5
 vrrp vrid 5 priority 100
 vrrp vrid 5 track bfd-session session-name bfd1 peer
#
peer-backup route-cost auto-advertising
#
remote-backup-service s1
 peer 10.3.3.3 source 10.13.13.13 port 6001
 track interface GigabitEthernet0/1/0
 protect lsp-tunnel for-all-instance peer-ip 10.3.3.3
 ip-pool pool_v4 metric 20
 ipv6-pool pool_nd_1 metric 20
 ipv6-pool pool_nd_2 metric 10
 radius-authorization source same-as nas-logic-ip
#
remote-backup-profile p1
 service-type bras
 backup-id 5 remote-backup-service s1
 peer-backup hot
 vrrp-id 5 interface Eth-Trunk2.1
 nas logic-port Eth-Trunk2 
 nas logic-ip 10.10.1.1
 nas logic-sysname huawei
#
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                   
 statistic enable                                                               
 user-vlan 2001
 remote-backup-profile p1                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain pre-authentication mac-domain authentication after-domain            
  authentication-method web
  authentication-method-ipv6 web  
 #                                                                              
#                                                                               
interface GigabitEthernet0/1/0                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.4.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:9::7/128                                                 
 ipv6 address auto link-local
 mpls
 mpls ldp
#
interface LoopBack0
 ipv6 enable
 ip address 10.11.1.1 32
 ipv6 address 2001:DB8:1::3 128
 ipv6 address auto link-local
#
interface LoopBack1
 ipv6 enable
 ip address 10.4.4.4 255.255.255.0
 ipv6 address 2001:DB8::3:3/64
 ipv6 address auto link-local
#
interface LoopBack2
 ip address 10.13.13.13 255.255.255.0
#
web-auth-server enable
web-auth-server 10.1.1.10 port 50100 key cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%#
web-auth-server source interface LoopBack0
web-auth-server version v2 v1
#
undo web-auth-server source-ip all
web-auth-server source-ip 10.11.1.1
#
traffic-policy before-auth-in inbound
#
ospf 1
 default cost inherit-metric
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.4.1.0 0.0.0.255
  network 10.13.13.13 0.0.0.0
#
vrrp recover-delay 300
#
return
```