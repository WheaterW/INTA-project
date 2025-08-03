Example for Configuring Layer 2 IPoE Access (Web+MAC Authentication)
====================================================================

This section provides an example for configuring Layer 2 IPoE access (web+MAC authentication). The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

Web+MAC authentication is the most common authentication mode for Layer 2 IPoE user access. This authentication mode requires a user to enter the username and password on a portal page when accessing the network for the first time. The RADIUS server associates the automatically recorded terminal MAC address with the username. Later, the user can access the network again without re-entering the username and password within a specified period after the first access.

The authentication process is as follows:

By default, the user enters the MAC authentication domain. If the user accesses the network for the first time, the MAC address fails to be found on the RADIUS server and the authentication fails. The user is forcibly switched to the web authentication domain and can access only the web authentication page. On this page, the user enters the username and password for authentication. After the authentication is successful, the user enters the post-authentication domain **after-auth** and can access network resources. If the user accesses the network not for the first time, the MAC address can be found on the RADIUS server and the authentication succeeds. The user then enters the post-authentication domain **after-auth** and can access network resources.

**Figure 1** Configuring Layer 2 IPoE access (web+MAC authentication)  
![](images/fig_dc_ne_cfg_bras_000901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a MAC authentication domain named **mac-auth**, a web authentication domain named **web-auth**, and a web post-authentication domain named **after-auth**.
2. Configure AAA schemes and adopt RADIUS authentication and RADIUS accounting.
3. Create a RADIUS server group named **d**. In the RADIUS server group view, configure the device to carry the HW-Auth-Type attribute in Access-Request packets to be sent to the RADIUS server.
4. Create an authentication scheme named **mac-auth**, and configure the device to redirect users to the web authentication domain **web-auth** when authentication fails.
5. Enable MAC authentication in the MAC authentication domain **mac-auth**, and bind the RADIUS server group **d** and authentication scheme **mac-auth** to the domain.
6. Configure forcible redirection to a specified web server in the web authentication domain **web-auth**, and bind a user group, an authentication scheme (none authentication), and an accounting scheme (none accounting) to the domain so that users in the user group can access only limited network resources.
7. Bind an authentication scheme (RADIUS authentication) and accounting scheme (RADIUS accounting) to the web post-authentication domain **after-auth**.
8. Configure the device to generate a pure username based on the MAC address carried in a user connection request packet in the AAA view.
9. Configure a MAC authentication domain and a post-authentication domain on the BAS interface.

#### Procedure

1. Create a MAC authentication domain named **mac-auth**, a web authentication domain named **web-auth**, and a post-authentication domain named **after-auth**.
   
   
   
   # Create a MAC authentication domain named **mac-auth**, a web authentication domain named **web-auth**, and a web post-authentication domain named **after-auth**.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain mac-auth
   ```
   ```
   [*HUAWEI-aaa-domain-mac-auth] commit
   ```
   ```
   [~HUAWEI-aaa-domain-mac-auth] quit
   ```
   ```
   [~HUAWEI-aaa] domain web-auth
   ```
   ```
   [*HUAWEI-aaa-domain-web-auth] commit
   ```
   ```
   [~HUAWEI-aaa-domain-web-auth] quit
   ```
   ```
   [~HUAWEI-aaa] domain after-auth
   ```
   ```
   [*HUAWEI-aaa-domain-after-auth] commit
   ```
   ```
   [~HUAWEI-aaa-domain-after-auth] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
2. Configure AAA schemes and a RADIUS server group.
   
   
   
   # Create a RADIUS server group named **d**, configure the device to carry the HW-Auth-Type attribute in Access-Request packets to be sent to the RADIUS server.
   
   ```
   [~HUAWEI] radius-server group d
   ```
   ```
   [*HUAWEI-radius-d] radius-server authentication 192.168.8.249 1812
   ```
   ```
   [*HUAWEI-radius-d] radius-server accounting 192.168.8.249 1813
   ```
   ```
   [*HUAWEI-radius-d] commit
   ```
   ```
   [~HUAWEI-radius-d] radius-server type standard
   ```
   ```
   [*HUAWEI-radius-d] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-radius-d] commit
   ```
   ```
   [~HUAWEI-radius-d] radius-attribute include hw-auth-type
   ```
   ```
   [*HUAWEI-radius-d] radius-server attribute translate
   ```
   ```
   [*HUAWEI-radius-d] commit
   ```
   ```
   [~HUAWEI-radius-d] quit
   ```
   
   # Create an authentication scheme named **mac-auth**, and configure the device to redirect users to the web authentication domain **web-auth** when authentication fails.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] authentication-scheme mac-auth
   ```
   ```
   [*HUAWEI-aaa-authen-mac-auth] authening authen-fail online authen-domain web-auth
   ```
   ```
   [*HUAWEI-aaa-authen-mac-auth] commit
   ```
   ```
   [~HUAWEI-aaa-authen-mac-auth] quit
   ```
   
   # Configure an authentication scheme named **auth2**, with RADIUS authentication specified.
   
   ```
   [~HUAWEI-aaa] authentication-scheme auth2
   ```
   ```
   [*HUAWEI-aaa-authen-auth2] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-auth2] commit
   ```
   ```
   [~HUAWEI-aaa-authen-auth2] quit
   ```
   
   # Configure an accounting scheme named **acct2**, with RADIUS accounting specified.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct2
   ```
   ```
   [*HUAWEI-aaa-accounting-acct2] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-acct2] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-acct2] quit
   ```
   
   # Configure an authentication scheme named **auth3**, with none authentication specified.
   
   ```
   [~HUAWEI-aaa] authentication-scheme auth3
   ```
   ```
   [*HUAWEI-aaa-authen-auth3] authentication-mode none
   ```
   ```
   [*HUAWEI-aaa-authen-auth3] commit
   ```
   ```
   [~HUAWEI-aaa-authen-auth3] quit
   ```
   
   # Configure an accounting scheme named **acct3**, with none accounting specified.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct3
   ```
   ```
   [*HUAWEI-aaa-accounting-acct3] accounting-mode none
   ```
   ```
   [*HUAWEI-aaa-accounting-acct3] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-acct3] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
3. Configure an address pool.
   
   
   ```
   [~HUAWEI] ip pool pool2 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool2] gateway 172.16.1.1 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool2] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool2] section 0 172.16.1.2 172.16.1.200
   ```
   ```
   [~HUAWEI-ip-pool-pool2] dns-server 192.168.8.252
   ```
   ```
   [*HUAWEI-ip-pool-pool2] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool2] quit
   ```
4. Enable MAC authentication in the MAC authentication domain **mac-auth**, and bind the RADIUS server group **d** and authentication scheme **mac-auth** to the domain.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain mac-auth
   ```
   ```
   [~HUAWEIdom-aaa-domain-mac-auth] radius-server group d
   ```
   ```
   [*HUAWEI-aaa-domain-mac-auth] authentication-scheme mac-auth
   ```
   ```
   [*HUAWEI-aaa-domain-mac-auth] accounting-scheme acct2
   ```
   ```
   [*HUAWEI-aaa-domain-mac-auth] commit
   ```
   ```
   [~HUAWEI-aaa-domain-mac-auth] ip-pool pool2
   ```
   ```
   [~HUAWEI-aaa-domain-mac-auth] mac-authentication enable
   ```
   ```
   [~HUAWEI-aaa-domain-mac-auth] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
5. Configure forcible redirection to a specified web server in the web authentication domain **web-auth**, and bind a user group, an authentication scheme (none authentication), and an accounting scheme (none accounting) to the domain so that users in the user group can access only the web authentication page.
   
   
   ```
   [~HUAWEI] user-group web-before
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain web-auth
   ```
   ```
   [*HUAWEI-aaa-domain-web-auth] authentication-scheme auth3
   ```
   ```
   [*HUAWEI-aaa-domain-web-auth] accounting-scheme acct3
   ```
   ```
   [*HUAWEI-aaa-domain-web-auth] commit
   ```
   ```
   [~HUAWEI-aaa-domain-web-auth] ip-pool pool2
   ```
   ```
   [~HUAWEI-aaa-domain-web-auth] user-group web-before
   ```
   ```
   [~HUAWEI-aaa-domain-web-auth] commit
   ```
   ```
   [~HUAWEI-aaa-domain-web-auth] web-server 192.168.8.251
   ```
   ```
   [~HUAWEI-aaa-domain-web-auth] web-server url http://192.168.8.251
   ```
   ```
   [~HUAWEI-aaa-domain-web-auth] web-server url-parameter
   ```
   ```
   [~HUAWEI-aaa-domain-web-auth] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   
   # Configure an IP address used by the device to receive portal packets from the web authentication server.
   
   ```
   [~HUAWEI] interface LoopBack 0
   ```
   ```
   [*HUAWEI-LoopBack0] ip address 10.6.55.1 32
   ```
   ```
   [*HUAWEI-LoopBack0] commit
   ```
   ```
   [*HUAWEI-LoopBack0] quit
   ```
   ```
   [~HUAWEI] web-auth-server source-ip 10.6.55.1
   ```
   
   # Configure a web authentication server.
   
   ```
   [~HUAWEI] web-auth-server enable
   ```
   ```
   [~HUAWEI] web-auth-server source interface LoopBack 0
   ```
   ```
   [~HUAWEI] web-auth-server 192.168.8.251 key cipher webvlan
   ```
   
   # Configure ACL rules.
   
   1. # Configure an ACL numbered 6004 to permit the traffic between the user group **web-before** and the web authentication server and between the user group **web-before** and the DNS server.
      ```
      [~HUAWEI] acl number 6004
      [*HUAWEI-acl-ucl-6004] rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
      [*HUAWEI-acl-ucl-6004] rule 10 permit ip source ip-address 192.168.8.251 0 destination user-group web-before
      [*HUAWEI-acl-ucl-6004] rule 15 permit ip source user-group web-before destination ip-address 192.168.8.252 0
      [*HUAWEI-acl-ucl-6004] rule 20 permit ip source ip-address 192.168.8.252 0 destination user-group web-before
      [*HUAWEI-acl-ucl-6004] commit
      [~HUAWEI-acl-ucl-6004] quit
      ```
   2. # Configure an ACL numbered 6005 and create ACL rules to match TCP packets from the user group **web-before** and with a destination port of www or 8080, so that HTTP redirect can be performed for the packets.
      ```
      [~HUAWEI] acl number 6005
      [*HUAWEI-acl-ucl-6005] rule 5 permit tcp source user-group web-before destination-port eq www
      [*HUAWEI-acl-ucl-6005] rule 10 permit tcp source user-group web-before destination-port eq 8080
      [*HUAWEI-acl-ucl-6005] commit
      [~HUAWEI-acl-ucl-6005] quit
      ```
   3. # Configure an ACL numbered 6008 to deny all the traffic originating from the user group **web-before**.
      ```
      [~HUAWEI] acl number 6008
      [*HUAWEI-acl-ucl-6008] rule 5 permit ip source ip-address any destination user-group web-before
      [*HUAWEI-acl-ucl-6008] rule 10 permit ip source user-group web-before destination ip-address any
      [*HUAWEI-acl-ucl-6008] commit
      [~HUAWEI-acl-ucl-6008] quit
      ```
   
   # Configure a traffic policy.
   
   a. Configure traffic classifiers.
   
   ```
   [~HUAWEI] traffic classifier web-be-permit
   ```
   ```
   [*HUAWEI-classifier-web-be-permit] if-match acl 6004
   ```
   ```
   [*HUAWEI-classifier-web-be-permit] commit
   ```
   ```
   [~HUAWEI-classifier-web-be-permit] quit
   ```
   ```
   [~HUAWEI] traffic classifier redirect
   ```
   ```
   [*HUAWEI-classifier-redirect] if-match acl 6005
   ```
   ```
   [*HUAWEI-classifier-redirect] commit
   ```
   ```
   [~HUAWEI-classifier-redirect] quit
   ```
   ```
   [~HUAWEI] traffic classifier web-be-deny
   ```
   ```
   [*HUAWEI-classifier-web-be-deny] if-match acl 6008
   ```
   ```
   [*HUAWEI-classifier-web-be-deny] commit
   ```
   ```
   [~HUAWEI-classifier-web-be-deny] quit
   ```
   
   b. Configure traffic behaviors.
   
   ```
   [~HUAWEI] traffic behavior perm1
   ```
   ```
   [*HUAWEI-behavior-perm1] permit
   ```
   ```
   [*HUAWEI-behavior-perm1] commit
   ```
   ```
   [~HUAWEI-behavior-perm1] quit
   ```
   ```
   [~HUAWEI] traffic behavior redirect
   ```
   ```
   [*HUAWEI-behavior-redirect] http-redirect
   ```
   ```
   [*HUAWEI-behavior-redirect] commit
   ```
   ```
   [~HUAWEI-behavior-redirect] quit
   ```
   ```
   [~HUAWEI] traffic behavior deny1
   ```
   ```
   [*HUAWEI-behavior-deny1] deny
   ```
   ```
   [*HUAWEI-behavior-deny1] commit
   ```
   ```
   [~HUAWEI-behavior-deny1] quit
   ```
   
   c. Configure a traffic policy.
   
   ```
   [~HUAWEI] traffic policy web
   ```
   ```
   [*HUAWEI-trafficpolicy-web] share-mode
   ```
   ```
   [*HUAWEI-trafficpolicy-web] classifier web-be-permit behavior perm1
   ```
   ```
   [*HUAWEI-trafficpolicy-web] classifier redirect behavior redirect
   ```
   ```
   [*HUAWEI-trafficpolicy-web] classifier web-be-deny behavior deny1
   ```
   ```
   [*HUAWEI-trafficpolicy-web] commit
   ```
   ```
   [~HUAWEI-trafficpolicy-web] quit
   ```
   
   # Apply the traffic policy globally.
   
   ```
   [~HUAWEI] traffic-policy web inbound
   ```
6. Configure an authentication domain named **after-auth**.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain after-auth
   ```
   ```
   [*HUAWEI-aaa-domain-after-auth] authentication-scheme auth2
   ```
   ```
   [*HUAWEI-aaa-domain-after-auth] accounting-scheme acct2
   ```
   ```
   [*HUAWEI-aaa-domain-after-auth] commit
   ```
   ```
   [~HUAWEI-aaa-domain-after-auth] radius-server group d
   ```
   ```
   [*HUAWEI-aaa-domain-after-auth] commit
   ```
   ```
   [~HUAWEI-aaa-domain-after-auth] quit
   ```
7. Configure the device to generate a pure username based on the MAC address carried in a user connection request packet in the AAA view.
   
   
   ```
   [~HUAWEI-aaa] default-user-name include mac-address -
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] default-password cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
8. Configure a MAC authentication domain, post-authentication domain, and authentication method on a BAS interface.
   
   
   ```
   [~HUAWEI] interface gigabitEthernet0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0-bas] access-type layer2-subscriber default-domain pre-authentication mac-auth authentication after-auth
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0-bas] authentication-method web
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0-bas] commit
   ```

#### Configuration Files

```
#
```
```
sysname HUAWEI
```
```
#
radius-server group d
 radius-server shared-key-cipher %^%#W)<2!w*fb2<lJf5$6S|($o\aAaq`_C!FAt*Yk-<!%^%#
 radius-server authentication 192.168.8.249 1812 weight 0
 radius-server accounting 192.168.8.249 1813 weight 0  
 radius-server attribute translate
 radius-attribute include HW-Auth-Type
#
ip pool pool2 bas local
 gateway 172.16.1.1 255.255.255.0
 section 0 172.16.1.2 172.16.1.200
 dns-server 192.168.8.252
#
user-group web-before
#
acl number 6004
 rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
 rule 10 permit ip source ip-address 192.168.8.251 0 destination user-group web-before
 rule 15 permit ip source user-group web-before destination ip-address 192.168.8.252 0
 rule 20 permit ip source ip-address 192.168.8.252 0 destination user-group web-before
#
acl number 6005
 rule 5 permit tcp source user-group web-before destination-port eq www
 rule 10 permit tcp source user-group web-before destination-port eq 8080
#
acl number 6008
 rule 5 permit ip source ip-address any destination user-group web-before
 rule 10 permit ip source user-group web-before destination ip-address any
#
traffic classifier redirect operator or
 if-match acl 6005 precedence 4
#
traffic classifier web-be-deny operator or
 if-match acl 6008 precedence 5
#
traffic classifier web-be-permit operator or
 if-match acl 6004 precedence 3
#
traffic behavior deny1
 deny
#
traffic behavior perm1
#
traffic behavior redirect
 http-redirect
#
traffic policy web
 share-mode
 classifier web-be-permit behavior perm1 precedence 1
 classifier redirect behavior redirect precedence 2  
 classifier web-be-deny behavior deny1 precedence 3
#
aaa
 default-user-name include mac-address -
 default-password cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
 #
 authentication-scheme auth2
 #
 authentication-scheme auth3
  authentication-mode none
 #
 authentication-scheme mac-auth
  authening authen-fail online authen-domain web-auth
 #
 accounting-scheme acct2
 #
 accounting-scheme acct3
  accounting-mode none
 #
 domain after-auth
  authentication-scheme auth2
  accounting-scheme acct2
  radius-server group d
 #
 domain mac-auth
  authentication-scheme mac-auth
  accounting-scheme acct2
  radius-server group d
  ip-pool pool2
  mac-authentication enable
 #
 domain web-auth
  authentication-scheme auth3
  accounting-scheme acct3
  ip-pool pool2
  user-group web-before
  web-server 192.168.8.251
  web-server url http://192.168.8.251
  web-server url-parameter
#
interface GigabitEthernet0/1/0
 bas
 #
  access-type layer2-subscriber default-domain pre-authentication mac-auth authentication after-auth
  authentication-method web
#
interface LoopBack0
 ip address 10.6.55.1 255.255.2555.255
#
web-auth-server enable
web-auth-server source interface LoopBack 0
web-auth-server 192.168.8.251 key cipher %^%#aQL6,Ua<|@sxPQK/1f'4/GBJ6,6)q>$Z^7*,!2yR%^%#
#
undo web-auth-server source-ip all
web-auth-server source-ip 10.6.55.1
#
undo web-auth-server source-ipv6 all
#
traffic-policy web inbound
#
return
```