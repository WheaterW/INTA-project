Example for Configuring IPoE Dual-Stack Access (Web+MAC Authentication)
=======================================================================

This section provides an example for configuring IPoE dual-stack user access through web+MAC authentication. When an IPoE dual-stack user connects to a BRAS and web+MAC authentication is used, the BRAS implements RADIUS authentication and accounting, assigns an IPv4 address from the local address pool to the user, and assigns an IPv6 address to the user through ND. This allows the user to access the Internet.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374034__fig_dc_ne_cfg_bras_000901), an IPv4/IPv6 dual-stack user accesses the network through web authentication. The BRAS performs RADIUS authentication and accounting for the user. When the user accesses the network for the first time, the user enters a MAC authentication domain, and the username and password need to be entered during web authentication. The RADIUS server automatically records the association between the terminal's MAC address and the entered username and password. After that, the user can automatically access the network without needing to repeatedly entering the username and password. This process is called MAC authentication. If the authentication fails, the user will be redirected to a web authentication domain. Users in a web authentication domain can access only limited network resources, such as the web server. (In this example, the web server and web authentication server are deployed on the same device.) If the user accesses unauthorized network resources, the user will be forcibly redirected to the specified web server. After the user re-enters the correct username and password and the authentication succeeds, the user becomes a post-authentication domain user and can access network resources normally. When the user logs in to the network next time, the BRAS performs MAC authentication based on the terminal's MAC address.

**Figure 1** Configuring IPoE dual-stack access (web+MAC authentication)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE 0/1/0.


  
![](images/fig_ipv4_ipv6_simultaneous_authentication_web_mac.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a MAC authentication domain named **mac-domain**, a web authentication domain named **web-domain**, and a post-authentication domain named **after-domain**.
2. Configure AAA schemes and a RADIUS server group named **group1**. In the RADIUS server group view, configure the BRAS to carry the Hw-Auth-Type attribute in authentication request packets(This attribute is optional and can be configured based on the configuration requirements of the RADIUS server.).
3. Configure address pools.
4. Enable MAC authentication in the MAC authentication domain **mac-domain**, and bind it to the RADIUS server group **group1** and the authentication scheme **portal-mac-auth**.
5. Configure a web authentication domain named **web-domain** in which users can access only limited network resources. Bind the none authentication scheme and none accounting scheme to the web authentication domain **web-domain**.
6. Configure ACL rules for the web authentication domain **web-domain**.
7. Configure a post-authentication domain named **after-domain** and bind it to the RADIUS accounting scheme and RADIUS authentication scheme.
8. In the AAA view, configure the MAC address carried in user access request packets as the pure username.
9. Configure a DUID for the device.
10. On a BAS interface, enable IPv6 and configure a MAC authentication domain, post-authentication domain, and authentication method.

#### Procedure

1. Create a MAC authentication domain named **mac-domain**, a web authentication domain named **web-domain**, and a post-authentication domain named **after-domain**.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain mac-domain
   ```
   ```
   [*Device-aaa-domain-mac-domain] quit
   ```
   ```
   [*Device-aaa] domain web-domain
   ```
   ```
   [*Device-aaa-domain-web-domain] quit
   ```
   ```
   [*Device-aaa] domain after-domain
   ```
   ```
   [*Device-aaa-domain-after-domain] quit
   ```
   ```
   [*Device-aaa] commit
   ```
   ```
   [~Device-aaa] quit 
   ```
2. Configure AAA schemes and a RADIUS server group.
   
   
   
   # Create a RADIUS server group named **group1**. In the RADIUS server group view, configure the BRAS to carry the Hw-Auth-Type attribute in authentication request packets.
   
   ```
   [~Device] radius-server group group1
   ```
   ```
   [*Device-radius-group1] radius-server authentication 10.1.2.10 1812
   ```
   ```
   [*Device-radius-group1] radius-server accounting 10.1.2.10 1813
   ```
   ```
   [*Device-radius-group1] radius-server shared-key-cipher Root_1234
   ```
   ```
   [*Device-radius-group1] commit 
   ```
   ```
   [~Device-radius-group1] radius-attribute include hw-auth-type
   ```
   ```
   [~Device-radius-group1] radius-server attribute translate
   ```
   ```
   [*Device-radius-group1] commit
   ```
   ```
   [~Device-radius-group1] quit
   ```
   
   # Create an authentication scheme named **portal-mac-auth**, and configure the BRAS to redirect the dual-stack user to the web authentication domain **web-domain** when web authentication fails.
   
   ```
   [~Device] aaa
   ```
   ```
   [*Device-aaa] authentication-scheme portal-mac-auth
   ```
   ```
   [*Device-aaa-authen-portal-mac-auth] commit 
   ```
   ```
   [~Device-aaa-authen-portal-mac-auth] authening authen-fail online authen-domain web-domain
   ```
   ```
   [~Device-aaa-authen-portal-mac-auth] quit
   ```
   
   # Configure an authentication scheme named **radius**, with RADIUS authentication specified.
   
   ```
   [~Device-aaa] authentication-scheme radius
   ```
   ```
   [*Device-aaa-authen-radius] authentication-mode radius local
   ```
   ```
   [*Device-aaa-authen-radius] commit
   ```
   ```
   [~Device-aaa-authen-radius] quit
   ```
   
   # Configure an authentication scheme named **none**, with none authentication specified.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In insecure network environments, you are advised to use a secure authentication mode. For details, see [Example for Configuring Layer 3 IPoE Access (Web Authentication)](dc_ne_ipox_cfg_0148.html).
   
   ```
   [~Device-aaa] authentication-scheme none
   ```
   ```
   [*Device-aaa-authen-none] authentication-mode none
   ```
   ```
   [*Device-aaa-authen-none] commit
   ```
   ```
   [~Device-aaa-authen-none] quit
   ```
   
   # Configure an accounting scheme named **radius**, with RADIUS accounting specified.
   
   ```
   [~Device-aaa] accounting-scheme radius
   ```
   ```
   [*Device-aaa-accounting-radius] accounting-mode radius
   ```
   ```
   [*Device-aaa-accounting-radius] accounting interim interval 10 hash
   ```
   ```
   [*Device-aaa-accounting-radius] commit
   ```
   ```
   [~Device-aaa-accounting-radius] quit
   ```
   
   # Configure an accounting scheme named **none**, with none accounting specified.
   
   ```
   [~Device-aaa] accounting-scheme none
   ```
   ```
   [*Device-aaa-accounting-none] accounting-mode none
   ```
   ```
   [*Device-aaa-accounting-none] commit
   ```
   ```
   [~Device-aaa-accounting-none] quit
   ```
   ```
   [~Device-aaa] quit
   ```
3. Configure address pools.
   
   # Configure an IPv4 address pool.
   ```
   [~Device] ip pool pool1 bas local
   ```
   ```
   [*Device-ip-pool-pool1] gateway 10.10.17.1 255.255.240.0
   ```
   ```
   [*Device-ip-pool-pool1] commit
   ```
   ```
   [~Device-ip-pool-pool1] section 0 10.10.17.2 10.10.19.254
   ```
   ```
   [~Device-ip-pool-pool1] dns-server 10.1.6.2
   ```
   ```
   [*Device-ip-pool-pool1] commit
   ```
   ```
   [~Device-ip-pool-pool1] quit
   ```
   
   # Configure an IPv6 prefix pool.
   ```
   [~Device] ipv6 prefix prefix1 delegation
   ```
   ```
   [*Device-ipv6-prefix-prefix1] prefix 2001:db8:2::/64
   ```
   ```
   [*Device-ipv6-prefix-prefix1] slaac-unshare-only
   ```
   ```
   [*Device-ipv6-prefix-prefix1] commit
   ```
   ```
   [~Device-ipv6-prefix-prefix1] quit
   ```
   
   # Configure an IPv6 address pool.
   ```
   [~Device] ipv6 pool pool1 bas delegation
   ```
   ```
   [*Device-ip-pool-pool1] prefix prefix1
   ```
   ```
   [*Device-ip-pool-pool1] dns-server 2001:db8:1::1
   ```
   ```
   [*Device-ip-pool-pool1] commit
   ```
   ```
   [~Device-ip-pool-pool1] quit
   ```
4. Enable MAC authentication in the MAC authentication domain **mac-domain**, and bind it to the RADIUS server group **group1** and the authentication scheme **portal-mac-auth**.
   
   
   ```
   [~Device] user-group mac-group
   ```
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain mac-domain
   ```
   ```
   [~Device-aaa-domain-mac-domain] radius-server group group1
   ```
   ```
   [*Device-aaa-domain-mac-domain] authentication-scheme portal-mac-auth
   ```
   ```
   [*Device-aaa-domain-mac-domain] accounting-scheme radius
   ```
   ```
   [*Device-aaa-domain-mac-domain] commit
   ```
   ```
   [~Device-aaa-domain-mac-domain] prefix-assign-mode unshared 
   ```
   ```
   [~Device-aaa-domain-mac-domain] ip-pool pool1
   ```
   ```
   [~Device-aaa-domain-mac-domain] ipv6-pool pool1
   ```
   ```
   [~Device-aaa-domain-mac-domain] mac-authentication enable
   ```
   ```
   [~Device-aaa-domain-mac-domain] user-group mac-group
   ```
   ```
   [~Device-aaa-domain-mac-domain] quit
   ```
   ```
   [~Device-aaa] quit
   ```
5. Configure a web authentication domain named **web-domain** in which users can access only limited network resources. Bind the none authentication scheme and none accounting scheme to this domain.
   
   
   ```
   [~Device] user-group web-group
   ```
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain web-domain
   ```
   ```
   [~Device-aaa-domain-web-domain] authentication-scheme none
   ```
   ```
   [*Device-aaa-domain-web-domain] accounting-scheme none
   ```
   ```
   [*Device-aaa-domain-web-domain] commit
   ```
   ```
   [~Device-aaa-domain-web-domain] prefix-assign-mode unshared
   ```
   ```
   [~Device-aaa-domain-web-domain] ip-pool pool1
   ```
   ```
   [~Device-aaa-domain-web-domain] ipv6-pool pool1
   ```
   ```
   [~Device-aaa-domain-web-domain] user-group web-group
   ```
   ```
   [~Device-aaa-domain-web-domain] web-server 10.1.1.10
   ```
   ```
   [~Device-aaa-domain-web-domain] web-server 2001:db8:1::2
   ```
   ```
   [~Device-aaa-domain-web-domain] web-server url http://www.isp1.com
   ```
   ```
   [~Device-aaa-domain-web-domain] web-server identical-url
   ```
   ```
   [~Device-aaa-domain-web-domain] quit
   ```
   ```
   [~Device-aaa] quit
   ```
   
   # Configure an IP address used by the device to receive portal packets from the web authentication server.
   
   ```
   [~Device] interface LoopBack 0
   ```
   ```
   [*Device-LoopBack0] ipv6 enable
   ```
   ```
   [*Device-LoopBack0] ip address 10.1.1.1 32
   ```
   ```
   [*Device-LoopBack0] ipv6 address 2001:db8:1::3 128
   ```
   ```
   [*Device-LoopBack0] ipv6 address auto link-local
   ```
   ```
   [*Device-LoopBack0] commit
   ```
   ```
   [~Device-LoopBack0] quit
   ```
   ```
   [~Device] web-auth-server source-ip 10.1.1.1
   ```
   ```
   [~Device] web-auth-server source-ipv6 2001:db8:1::3
   ```
   
   # Configure a web authentication server.
   
   ```
   [~Device] web-auth-server enable
   ```
   ```
   [~Device] web-auth-server source interface LoopBack 0
   ```
   ```
   [~Device] web-auth-server 10.1.1.10 key cipher Root_123
   ```
   ```
   [~Device] web-auth-server 2001:db8:1::2 key cipher Root_123
   ```
6. Configure ACL rules for the web authentication domain **web-domain**.
   
   
   
   # Configure IPv4 ACL rules.
   
   * Configure ACL 6000 to permit the traffic between user group **web-group** and web authentication server and between user group **web-group** and the DNS server.
     ```
     [~Device] acl number 6000
     ```
     ```
     [*Device-acl-ucl-6000] rule 5 permit ip source ip-address 10.1.1.10 0 destination user-group web-group
     ```
     ```
     [*Device-acl-ucl-6000] rule 10 permit ip source user-group web-group destination ip-address 10.1.1.10 0
     ```
     ```
     [*Device-acl-ucl-6000] rule 15 permit ip source ip-address 10.1.6.2 0 destination user-group web-group
     ```
     ```
     [*Device-acl-ucl-6000] rule 20 permit ip source user-group web-group destination ip-address 10.1.6.2 0
     ```
     ```
     [*Device-acl-ucl-6000] commit
     ```
     ```
     [~Device-acl-ucl-6000] quit
     ```
   * Configure an ACL numbered 6001 to allow HTTP redirect for the TCP packets originating from the user group **web-group** and carrying destination port **www** or 8080.
     ```
     [~Device] acl number 6001
     ```
     ```
     [*Device-acl-ucl-6001] rule 5 permit tcp source user-group web-group destination-port eq www
     ```
     ```
     [*Device-acl-ucl-6001] rule 10 permit tcp source user-group web-group destination-port eq 8080
     ```
     ```
     [*Device-acl-ucl-6001] commit
     ```
     ```
     [~Device-acl-ucl-6001] quit
     ```
   * Configure an ACL numbered 6002 to deny all the traffic originating from the user group **web-group**.
     ```
     [~Device] acl number 6002
     ```
     ```
     [*Device-acl-ucl-6002] rule 5 permit ip source ip-address any destination user-group web-group
     ```
     ```
     [*Device-acl-ucl-6002] rule 10 permit ip source user-group web-group destination ip-address any
     ```
     ```
     [*Device-acl-ucl-6002] commit
     ```
     ```
     [~Device-acl-ucl-6002] quit
     ```
   
   # Configure IPv6 ACL rules.
   
   * Configure ACL 6000 to permit the traffic between user group **web-group** and web authentication server and between user group **web-group** and the DNS server.
     ```
     [~Device] acl ipv6 number 6000
     ```
     ```
     [*Device-acl6-ucl-6000] rule 5 permit ipv6 source user-group web-group destination ipv6-address 2001:db8:1::1/128
     ```
     ```
     [*Device-acl6-ucl-6000] rule 10 permit ipv6 source ipv6-address 2001:db8:1::1/128 destination user-group web-group
     ```
     ```
     [*Device-acl6-ucl-6000] rule 15 permit ipv6 source ipv6-address 2001:db8:1::2/128 destination user-group web-group
     ```
     ```
     [*Device-acl6-ucl-6000] rule 20 permit ipv6 source user-group web-group destination ipv6-address 2001:db8:1::2/128
     ```
     ```
     [*Device-acl6-ucl-6000] commit
     ```
     ```
     [~Device-acl6-ucl-6000] quit
     ```
   * Configure an ACL numbered 6001 to allow HTTP redirect for the TCP packets originating from the user group **web-group** and carrying destination port **www** or 8080.
     ```
     [~Device] acl ipv6 number 6001
     ```
     ```
     [*Device-acl6-ucl-6001] rule 5 permit tcp source user-group web-group destination-port eq www
     ```
     ```
     [*Device-acl6-ucl-6001] rule 10 permit tcp source user-group web-group destination-port eq 8080
     ```
     ```
     [*Device-acl6-ucl-6001] commit
     ```
     ```
     [~Device-acl6-ucl-6001] quit
     ```
   * Configure an ACL numbered 6002 to deny all the traffic originating from the user group **web-group**.
     ```
     [~Device] acl ipv6 number 6002
     ```
     ```
     [*Device-acl6-ucl-6002] rule 5 permit ipv6 source ipv6-address any destination user-group web-group
     ```
     ```
     [*Device-acl6-ucl-6002] rule 10 permit ipv6 source user-group web-group destination ipv6-address any
     ```
     ```
     [*Device-acl6-ucl-6002] commit
     ```
     ```
     [~Device-acl6-ucl-6002] quit
     ```# Configure a traffic policy.
   ```
   [~Device] traffic classifier 6000
   ```
   ```
   [*Device-classifier-6000] if-match acl 6000
   ```
   ```
   [*Device-classifier-6000] if-match ipv6 acl 6000
   ```
   ```
   [*Device-classifier-6000] quit
   ```
   ```
   [*Device] traffic classifier 6001
   ```
   ```
   [*Device-classifier-6001] if-match acl 6001
   ```
   ```
   [*Device-classifier-6001] if-match ipv6 acl 6001
   ```
   ```
   [*Device-classifier-6001] quit
   ```
   ```
   [*Device] traffic classifier 6002
   ```
   ```
   [*Device-classifier-6002] if-match acl 6002
   ```
   ```
   [*Device-classifier-6002] if-match ipv6 acl 6002
   ```
   ```
   [*Device-classifier-6002] quit
   ```
   ```
   [*Device] traffic behavior permit
   ```
   ```
   [*Device-behavior-permit] permit
   ```
   ```
   [*Device-behavior-permit] quit
   ```
   ```
   [*Device] traffic behavior in-deny
   ```
   ```
   [*Device-behavior-in-deny] deny
   ```
   ```
   [*Device-behavior-in-deny] quit
   ```
   ```
   [*Device] traffic behavior redirect
   ```
   ```
   [*Device-behavior-redirect] http-redirect
   ```
   ```
   [*Device-behavior-redirect] quit
   ```
   ```
   [*Device] traffic policy before-auth-in
   ```
   ```
   [*Device-trafficpolicy-before-auth-in] share-mode
   ```
   ```
   [*Device-trafficpolicy-before-auth-in] classifier 6000 behavior permit
   ```
   ```
   [*Device-trafficpolicy-before-auth-in] classifier 6001 behavior redirect
   ```
   ```
   [*Device-trafficpolicy-before-auth-in] classifier 6002 behavior in-deny
   ```
   ```
   [*Device-trafficpolicy-before-auth-in] quit
   ```
   
   # Apply the traffic policy globally.
   
   ```
   [*Device] traffic-policy before-auth-in inbound
   [*Device] commit
   ```
7. Configure a post-authentication domain named **after-domain** and bind it to the RADIUS accounting scheme and RADIUS authentication scheme.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain after-domain
   ```
   ```
   [~Device-aaa-domain-after-domain] authentication-scheme radius
   ```
   ```
   [*Device-aaa-domain-after-domain] accounting-scheme radius
   ```
   ```
   [*Device-aaa-domain-after-domain] radius-server group group1
   ```
   ```
   [*Device-aaa-domain-after-domain] commit
   ```
   ```
   [~Device-aaa-domain-after-domain] quit
   ```
8. In the AAA view, configure the MAC address carried in user access request packets as the pure username.
   
   
   ```
   [~Device-aaa] default-user-name include mac-address -
   ```
   ```
   [*Device-aaa] commit
   ```
   ```
   [~Device-aaa] default-password cipher YsHsjx_202206 
   ```
   ```
   [*Device-aaa] commit
   ```
   ```
   [~Device-aaa] quit
   ```
9. Configure a DUID for the device.
   
   
   ```
   [~Device] dhcpv6 duid 12345678
   [*Device] commit
   ```
10. On a BAS interface, enable IPv6 and configure a MAC authentication domain, post-authentication domain, and authentication method.
    
    
    ```
    [~Device] interface gigabitethernet0/1/0
    ```
    ```
    [*Device-GigabitEthernet0/1/0] ipv6 enable
    ```
    ```
    [*Device-GigabitEthernet0/1/0] ipv6 address auto link-local
    ```
    ```
    [*Device-GigabitEthernet0/1/0] commit
    ```
    ```
    [~Device-GigabitEthernet0/1/0] bas
    ```
    ```
    [~Device-GigabitEthernet0/1/0-bas] access-type layer2-subscriber default-domain pre-authentication mac-domain authentication after-domain
    ```
    ```
    [*Device-GigabitEthernet0/1/0-bas] authentication-method web
    [*Device-GigabitEthernet0/1/0-bas] authentication-method-ipv6 web
    [*Device-GigabitEthernet0/1/0-bas] ip-trigger
    [*Device-GigabitEthernet0/1/0-bas] arp-trigger
    [*Device-GigabitEthernet0/1/0-bas] commit
    [~Device-GigabitEthernet0/1/0-bas] ipv6-trigger
    [~Device-GigabitEthernet0/1/0-bas] nd-trigger
    [~Device-GigabitEthernet0/1/0-bas] quit
    [~Device-GigabitEthernet0/1/0] quit
    ```
11. Verify the configuration.
    
    
    1. A user logs in to a PC and obtains an IP address.
    2. Run the [**display access-user domain web-domain**](cmdqueryname=display+access-user+domain+web-domain) command to check online user information.
    3. The user enters another website in the address bar and is automatically redirected to the address of the web server.
    4. The user enters the username and password, and accesses the Internet after the authentication succeeds.
    5. Run the [**display domain mac-domain**](cmdqueryname=display+domain+mac-domain) command to check configurations of the MAC authentication domain **mac-domain**. The command output shows that an IPv4 address pool and an IPv6 address pool are bound to the domain.

#### Configuration Files

```
#
sysname Device
#
radius-server group group1
 radius-server shared-key-cipher %^%#W)<2!w*fb2<lJf5$6S|($o\aAaq`_C!FAt*Yk-<!%^%#
 radius-server authentication 10.1.2.10 1812 weight 0
 radius-server accounting 10.1.2.10 1813 weight 0 
 radius-server attribute translate
 radius-attribute include HW-Auth-Type
#
ip pool pool1 bas local
 gateway 10.10.17.1 255.255.240.0
 section 0 10.10.17.2 10.10.19.254
 dns-server 10.1.6.2
#
ipv6 prefix prefix1 delegation
 prefix 2001:DB8:2::/64
 slaac-unshare-only
#
ipv6 pool pool1 bas delegation
 dns-server 2001:DB8:1::1
 prefix prefix1
#
user-group mac-group
user-group web-group
#
acl number 6000
 rule 5 permit ip source ip-address 10.1.1.10 0 destination user-group web-group
 rule 10 permit ip source user-group web-group destination ip-address 10.1.1.10 0
 rule 15 permit ip source ip-address 10.1.6.2 0 destination user-group web-group
 rule 20 permit ip source user-group web-group destination ip-address 10.1.6.2 0
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
 rule 10 permit ipv6 source ipv6-address 2001:DB8:1::1/128 destination user-group web-group
 rule 15 permit ipv6 source ipv6-address 2001:DB8:1::2/128 destination user-group web-group
 rule 20 permit ipv6 source user-group web-group destination ipv6-address 2001:DB8:1::2/128
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
 http-redirect
#
traffic policy before-auth-in
 share-mode
 classifier 6000 behavior permit precedence 1
 classifier 6001 behavior redirect precedence 2
 classifier 6002 behavior in-deny precedence 3
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
  accounting interim interval 10 hash
 #
 accounting-scheme none
  accounting-mode none
 #
 domain mac-domain
  authentication-scheme portal-mac-auth
  accounting-scheme radius
  radius-server group group1
  prefix-assign-mode unshared
  ip-pool pool1
  ipv6-pool pool1
  mac-authentication enable
  user-group mac-group
 #
 domain web-domain
  authentication-scheme none
  accounting-scheme none
  prefix-assign-mode unshared
  ip-pool pool1
  ipv6-pool pool1
  user-group web-group
  web-server 10.1.1.10 2001:DB8:1::2
  web-server url http://www.isp1.com
  web-server identical-url
 #
 domain after-domain
  authentication-scheme radius
  accounting-scheme radius
  radius-server group group1
#
interface GigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address auto link-local
 bas
 #
  access-type layer2-subscriber default-domain pre-authentication mac-domain authentication after-domain
  authentication-method web
  authentication-method-ipv6 web
  ip-trigger
  arp-trigger
  ipv6-trigger 
  nd-trigger
 #
#
interface LoopBack 0
 ipv6 enable
 ip address 10.1.1.1 32
 ipv6 address 2001:DB8:1::3 128
 ipv6 address auto link-local
#
web-auth-server enable
web-auth-server source interface LoopBack0
web-auth-server 2001:DB8:1::2 key cipher %^%#\39J9tmKl#+;)]1yEd@V#i(1Jeq"vO=9ka=-\qN<%^%#
web-auth-server 10.1.1.10 key cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%#
#
undo web-auth-server source-ip all
web-auth-server source-ip 10.1.1.1
#
undo web-auth-server source-ipv6 all
web-auth-server source-ipv6 2001:DB8:1::3
#
traffic-policy before-auth-in inbound
#
return
```