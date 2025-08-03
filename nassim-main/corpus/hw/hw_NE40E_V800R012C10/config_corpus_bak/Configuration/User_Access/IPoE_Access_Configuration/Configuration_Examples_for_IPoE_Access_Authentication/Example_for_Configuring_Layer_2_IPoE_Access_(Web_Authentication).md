Example for Configuring Layer 2 IPoE Access (Web Authentication)
================================================================

This section provides an example for configuring Layer 2 IPoE access (web authentication). The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

In web authentication mode, users must enter usernames and passwords on a portal page for authentication and can access the network after passing the authentication.

**Figure 1** Configuring Layer 2 IPoE access (web authentication)  
![](images/fig_dc_ne_cfg_bras_000901.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a pre-authentication domain named **pre-web** and an authentication domain named **after-auth**.
2. Configure AAA schemes.
3. Create a RADIUS server group.
4. Configure a user password.
5. Configure forcible redirection to a specified web server in the pre-authentication domain **pre-web**, and bind a user group, an authentication scheme (none authentication), and an accounting scheme (none accounting) to the domain so that users in the user group can access only limited resources.
6. Bind an authentication scheme (RADIUS authentication) and accounting scheme (RADIUS accounting) to the authentication domain **after-auth**.
7. Configure a pre-authentication domain and authentication domain on a BAS interface.

#### Procedure

1. Create a pre-authentication domain named **pre-web** and an authentication domain named **after-auth**.
   
   
   
   # Create a pre-authentication domain named **pre-web** and an authentication domain named **after-auth**.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain pre-web
   ```
   ```
   [*HUAWEI-aaa-domain-pre-web] commit
   ```
   ```
   [~HUAWEI-aaa-domain-pre-web] quit
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
   
   
   
   # Configure a RADIUS server group named **rd2**.
   
   ```
   [~HUAWEI] radius-server group rd2
   ```
   ```
   [*HUAWEI-radius-rd2] radius-server authentication 192.168.8.249 1812
   ```
   ```
   [*HUAWEI-radius-rd2] radius-server accounting 192.168.8.249 1813
   ```
   ```
   [*HUAWEI-radius-rd2] commit
   ```
   ```
   [~HUAWEI-radius-rd2] radius-server type standard
   ```
   ```
   [~HUAWEI-radius-rd2] radius-server shared-key-cipher Root@1234
   ```
   ```
   [*HUAWEI-radius-rd2] commit
   ```
   ```
   [~HUAWEI-radius-rd2] quit
   ```
   
   # Configure an authentication scheme named **auth2**, with RADIUS authentication specified.
   
   ```
   [~HUAWEI] aaa
   ```
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
   ```
   [~HUAWEI-aaa] quit
   ```
   
   # Configure an authentication scheme named **auth3**, with none authentication specified.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, or protocol. For security examples, see [Example for Configuring Layer 3 IPoE Access (Web Authentication)](dc_ne_ipox_cfg_0148.html).
   
   ```
   [~HUAWEI] aaa
   ```
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
3. Configure the IPoE user password.
   
   
   ```
   [~HUAWEI-aaa] default-password cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
4. Configure an address pool.
   
   
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
5. Configure forcible redirection to a specified web server in the pre-authentication domain **pre-web**, and bind a user group, an authentication scheme (none authentication), and an accounting scheme (none accounting) to the domain so that users in the user group can access only the web authentication page.
   1. Enable HTTP redirect in the pre-authentication domain and bind the authentication scheme (none authentication) and accounting scheme (none accounting) to the domain.
      
      
      ```
      [~HUAWEI] user-group web-before
      ```
      ```
      [~HUAWEI] aaa
      ```
      ```
      [~HUAWEI-aaa] domain pre-web
      ```
      ```
      [*HUAWEI-aaa-domain-pre-web] authentication-scheme auth3
      ```
      ```
      [*HUAWEI-aaa-domain-pre-web] accounting-scheme acct3
      ```
      ```
      [*HUAWEI-aaa-domain-pre-web] commit
      ```
      ```
      [~HUAWEI-aaa-domain-pre-web] ip-pool pool2
      ```
      ```
      [~HUAWEI-aaa-domain-pre-web] user-group web-before
      ```
      ```
      [~HUAWEI-aaa-domain-pre-web] web-server 192.168.8.251
      ```
      ```
      [~HUAWEI-aaa-domain-pre-web] web-server url http://192.168.8.251
      ```
      ```
      [~HUAWEI-aaa-domain-pre-web] web-server url-parameter
      ```
      ```
      [~HUAWEI-aaa-domain-pre-web] quit
      ```
      ```
      [~HUAWEI-aaa] quit
      ```
   2. Configure an IP address used by the device to receive portal packets from the web authentication server.
      
      
      ```
      [~HUAWEI] interface Loopback 0
      ```
      ```
      [*HUAWEI-LoopBack0] ip address 10.6.55.1 32
      ```
      ```
      [*HUAWEI-LoopBack0] commit
      ```
      ```
      [~HUAWEI-LoopBack0] quit
      ```
      ```
      [~HUAWEI] web-auth-server source-ip 10.6.55.1
      ```
   3. Configure a web authentication server.
      
      
      ```
      [~HUAWEI] web-auth-server enable
      ```
      ```
      [~HUAWEI] web-auth-server source interface LoopBack 0
      ```
      ```
      [~HUAWEI] web-auth-server 192.168.8.251 key cipher webvlan
      ```
   4. Configure ACL rules.
      
      
      
      # Configure an ACL numbered 6004 to permit the traffic between the user group **web-before** and the web authentication server and between the user group **web-before** and the DNS server.
      
      ```
      [~HUAWEI] acl number 6004
      ```
      ```
      [*HUAWEI-acl-ucl-6004] rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
      [*HUAWEI-acl-ucl-6004] rule 10 permit ip source ip-address 192.168.8.251 0 destination user-group web-before
      [*HUAWEI-acl-ucl-6004] rule 15 permit ip source user-group web-before destination ip-address 192.168.8.252 0
      [*HUAWEI-acl-ucl-6004] rule 20 permit ip source ip-address 192.168.8.252 0 destination user-group web-before
      [*HUAWEI-acl-ucl-6004] commit
      [~HUAWEI-acl-ucl-6004] quit
      ```
      
      # Configure an ACL numbered 6005 and create ACL rules to match TCP packets from the user group **web-before** and with a destination port of www or 8080, so that HTTP redirect can be performed for the packets.
      
      ```
      [~HUAWEI] acl number 6005
      ```
      ```
      [*HUAWEI-acl-ucl-6005] rule 5 permit tcp source user-group web-before destination-port eq www
      [*HUAWEI-acl-ucl-6005] rule 10 permit tcp source user-group web-before destination-port eq 8080
      [*HUAWEI-acl-ucl-6005] commit
      [~HUAWEI-acl-ucl-6005] quit
      ```
      
      # Configure an ACL numbered 6008 to deny all the traffic originating from the user group **web-before**.
      
      ```
      [~HUAWEI] acl number 6008
      ```
      ```
      [*HUAWEI-acl-ucl-6008] rule 3 permit ip source ip-address any destination user-group web-before
      [*HUAWEI-acl-ucl-6008] rule 5 permit ip source user-group web-before destination ip-address any
      [*HUAWEI-acl-ucl-6008] commit
      [~HUAWEI-acl-ucl-6008] quit
      ```
   5. Configure a traffic policy.
      
      
      
      # Configure traffic classifiers.
      
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
      
      # Configure traffic behaviors.
      
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
      
      # Configure a traffic policy.
      
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
   [~HUAWEI-aaa-domain-after-auth] radius-server group rd2
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
7. Configure a pre-authentication domain, an authentication domain, and an authentication method on a BAS interface.
   
   
   ```
   [~HUAWEI] interface gigabitEthernet0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0-bas] access-type layer2-subscriber default-domain pre-authentication pre-web authentication after-auth
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
sysname HUAWEI
#
radius-server group rd2
 radius-server shared-key-cipher %^%#W)<2!w*fb2<lJf5$6S|($o\aAaq`_C!FAt*Yk-<!%^%#
 radius-server authentication 192.168.8.249 1812 weight 0
 radius-server accounting 192.168.8.249 1813 weight 0 
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
 rule 3 permit ip source ip-address any destination user-group web-before
 rule 5 permit ip source user-group web-before destination ip-address any
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
 default-password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
 authentication-scheme auth2
 #
 authentication-scheme auth3
  authentication-mode none
 #
 accounting-scheme acct2
 #
 accounting-scheme acct3
  accounting-mode none
 #
 domain pre-web
 authentication-scheme auth3
 accounting-scheme acct3
 ip-pool pool2
 user-group web-before
 web-server 192.168.8.251
 web-server url http://192.168.8.251
 web-server url-parameter
 #
 domain after-auth
 authentication-scheme auth2
 accounting-scheme acct2
 radius-server group rd2
#
interface GigabitEthernet0/1/0
 bas
 #
  access-type layer2-subscriber default-domain pre-authentication pre-web authentication after-auth
  authentication-method web
#
interface LoopBack0
 ip address 10.6.55.1 255.255.255.255
#
traffic-policy web inbound
#
web-auth-server enable
web-auth-server source interface LoopBack0
web-auth-server 192.168.8.251 key cipher %^%#aQL6,Ua<|@sxPQK/1f'4/GBJ6,6)q>$Z^7*,!2yR%^%#
#
undo web-auth-server source-ip all
web-auth-server source-ip 10.6.55.1
#
undo web-auth-server source-ipv6 all
#
return
```