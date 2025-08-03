Example for Configuring Layer 3 DHCPv6 to Support IANA+IAPD Access (Web Authentication) from a Local Address Pool
=================================================================================================================

This section provides an example for configuring Layer 3 DHCPv6 to support IANA+IAPD access. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374054__fig_dc_ne_ipox_cfg_014801), the networking requirements are as follows:

* A user belongs to the domain **isp2** and connects to GE 0/1/2.1 on DeviceB through DeviceA, a DHCPv6 relay agent, in DHCPv6 (IANA+IAPD) mode.
* Web authentication, RADIUS authentication, and RADIUS accounting are used.
* The IP address of the RADIUS server is 192.168.8.249, and the authentication and accounting port numbers are 1812 and 1813, respectively. The standard RADIUS protocol is used, and the key is **it-is-my-secret1**.
* The address of the DNS server is 2001:db8:3::1/64.
* The address of the web server is 2001:db8:3::2/64, and the shared key is **webvlan**.

**Figure 1** Configuring Layer 3 DHCPv6 to support IANA+IAPD access (web authentication)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE 0/1/1, GE 0/1/2, GE 0/1/1.1, and GE 0/1/2.1, respectively.


  
![](figure/en-us_image_0172374056.png)

#### Configuration Roadmap

All functions are configured on DeviceB except the DHCPv6 relay function. The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on DeviceA and DeviceB.
2. Configure DHCPv6 relay on DeviceA.
3. Configure network-side address pools on DeviceB. The gateway address of the address pools must be on the same network segment as the IP address of the inbound interface on DeviceA, the DHCP relay agent.
4. Configure AAA schemes.
5. Configure an interface IP address for DeviceB to receive portal packets from the web authentication server.
6. Configure a web authentication server.
7. Configure a RADIUS server group.
8. Configure an ACL to allow the user to access only the web server address before web authentication succeeds.
9. Configure a DUID for the device.
10. Configure a domain.
11. Configure a BAS interface and an uplink interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* Configure a username.
* RADIUS server group name, and IP address and port numbers of the RADIUS authentication and accounting server
* Address pool names
* Domain names
* BAS interface parameters

#### Procedure

1. Configure IP addresses for interfaces on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface GigabitEthernet0/1/2
   [~DeviceA-GigabitEthernet0/1/2] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/22] ipv6 address 2001:db8:2::1/64
   [*DeviceA-GigabitEthernet0/1/2] ipv6 address auto link-local
   [*DeviceA-GigabitEthernet0/1/2] commit
   [~DeviceA-GigabitEthernet0/1/22] quit
   [~DeviceA] interface GigabitEthernet1/0/1.1
   [*DeviceA-GigabitEthernet1/0/1.1] ipv6 enable
   [*DeviceA-GigabitEthernet1/0/1.1] ipv6 address 2001:db8:1::2/64
   [*DeviceA-GigabitEthernet1/0/1.1] vlan-type dot1q 1
   [*DeviceA-GigabitEthernet1/0/1.1] ipv6 address auto link-local
   [*DeviceA-GigabitEthernet1/0/1.1] commit
   [~DeviceA-GigabitEthernet1/0/1.1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface GigabitEthernet1/0/2.1
   [*DeviceB-GigabitEthernet1/0/2.1] ipv6 enable
   [*DeviceB-GigabitEthernet1/0/2.1] ipv6 address 2001:db8:1::1/64
   [*DeviceB-GigabitEthernet1/0/2.1] vlan-type dot1q 1
   [*DeviceB-GigabitEthernet1/0/2.1] commit
   [~DeviceB-GigabitEthernet1/0/2.1] quit
   ```
2. Configure DHCPv6 relay on DeviceA.
   
   
   ```
   [~DeviceA] interface GigabitEthernet1/0/2
   [~DeviceA-GigabitEthernet1/0/2] dhcp select relay
   [*DeviceA-GigabitEthernet1/0/2] dhcpv6 relay destination 2001:db8:1::1
   [*DeviceA-GigabitEthernet1/0/2] ipv6 address auto link-local
   [*DeviceA-GigabitEthernet1/0/2] commit
   [~DeviceA-GigabitEthernet1/0/2] quit
   ```
3. Configure network-side address pools on DeviceB. The gateway address of the address pools must be on the same network segment as the IP address of the inbound interface on DeviceA, the DHCP relay agent.
   
   
   
   # Configure an IAPD prefix pool.
   
   ```
   [~DeviceB] ipv6 prefix prefixpd delegation
   [*DeviceB-ipv6-prefix-prefixpd] prefix 2001:db8:5::/48
   [*DeviceB-ipv6-prefix-prefixpd] commit
   [~DeviceB-ipv6-prefix-prefixpd] quit
   ```
   
   # Configure an IAPD address pool.
   
   ```
   [~DeviceB] ipv6 pool poolpd bas delegation
   [*DeviceB-ipv6-pool-poolpd] prefix prefixpd
   [*DeviceB-ipv6-pool-poolpd] dns-server 2001:db8:3::1
   [*DeviceB-ipv6-pool-poolpd] commit
   [~DeviceB-ipv6-pool-poolpd] quit
   ```
   
   # Configure an IANA prefix pool.
   
   ```
   [~DeviceB] ipv6 prefix na local
   [*DeviceB-ipv6-prefix-na] prefix 2001:db8:2::/64
   [*DeviceB-ipv6-prefix-na] commit
   [~DeviceB-ipv6-prefix-na] quit
   ```
   
   # Configure an IANA relay address pool.
   
   ```
   [~DeviceB] ipv6 pool na bas relay
   [*DeviceB-ipv6-prefix-na] prefix na
   [*DeviceB-ipv6-prefix-na] dns-server 2001:db8:3::1
   [*DeviceB-ipv6-prefix-na] commit
   [~DeviceB-ipv6-prefix-na] quit
   ```
4. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   [~DeviceB] aaa
   [~DeviceB-aaa] authentication-scheme auth2
   [*DeviceB-aaa-authen-auth2] authentication-mode radius
   [*DeviceB-aaa-authen-auth2] commit
   [~DeviceB-aaa-authen-auth2] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~DeviceB-aaa] accounting-scheme acct2
   [*DeviceB-aaa-accounting-acct2] accounting-mode radius
   [*DeviceB-aaa-accounting-acct2] commit
   [~DeviceB-aaa-accounting-acct2] quit
   ```
5. Configure the IPoE user password.
   
   
   ```
   [~DeviceB-aaa] default-password cipher YsHsjx_202206
   [*DeviceB-aaa] commit
   [~DeviceB-aaa] quit
   ```
6. Configure an interface IP address for DeviceB to receive portal packets from the web authentication server.
   
   
   ```
   [~DeviceB] interface LoopBack 0
   [*DeviceB-LoopBack0] ipv6 enable
   [*DeviceB-LoopBack0] ipv6 address 2001:db8:3::3 128
   [*DeviceB-LoopBack0] ipv6 address auto link-local
   [*DeviceB-LoopBack0] commit
   [~DeviceB-LoopBack0] quit
   [~DeviceB] web-auth-server source-ipv6 2001:db8:3::3
   ```
7. Configure a web authentication server.
   
   
   ```
   [~DeviceB] web-auth-server enable
   [~DeviceB] web-auth-server source interface LoopBack 0
   [~DeviceB] web-auth-server 2001:db8:3::3 key cipher Root_123 
   ```
8. Configure a RADIUS server group.
   
   
   ```
   [~DeviceB] radius-server group rd2
   [*DeviceB-radius-rd2] radius-server authentication 192.168.8.249 1812
   [*DeviceB-radius-rd2] radius-server accounting 192.168.8.249 1813
   [*DeviceB-radius-rd2] commit
   [~DeviceB-radius-rd2] radius-server type standard
   [~DeviceB-radius-rd2] radius-server shared-key-cipher it-is-my-secret1
   [*DeviceB-radius-rd2] commit
   [~DeviceB-radius-rd2] quit
   ```
9. Configure an ACL to allow the user to access only the web server address before web authentication succeeds.
   
   
   
   # Configure a user group.
   
   ```
   [~DeviceB] user-group huawei
   ```
   
   # Configure an ACL numbered 6000 to permit the traffic between the user group **huawei** and the web authentication server and between the user group **huawei** and the DNS server.
   
   ```
   [~DeviceB] acl ipv6 number 6000
   [*Device-acl6-ucl-6000] rule permit ipv6 source user-group huawei destination ipv6-address 2001:db8:3::2/128
   [*DeviceB-acl6-ucl-6000] rule permit ipv6 source ipv6-address 2001:db8:3::2/128 destination user-group huawei
   [*DeviceB-acl6-ucl-6000] rule permit ipv6 source user-group huawei destination ipv6-address 2001:db8:3::1/128
   [*DeviceB-acl6-ucl-6000] rule permit ipv6 source ipv6-address 2001:db8:3::1/128 destination user-group huawei
   [*DeviceB-acl6-ucl-6000] commit
   [~DeviceB-acl6-ucl-6000] quit
   ```
   
   # Configure an ACL numbered 6001 to allow redirection for the TCP packets originating from user group **huawei** and carrying destination port **www** or 8080.
   
   ```
   [~DeviceB] acl ipv6 number 6001
   [*DeviceB-acl6-ucl-6001] rule permit tcp source user-group huawei destination-port eq www
   [*DeviceB-acl6-ucl-6001] rule permit tcp source user-group huawei destination-port eq 8080
   [*DeviceB-acl6-ucl-6001] commit
   [~DeviceB-acl6-ucl-6001] quit
   ```
   
   # Configure an ACL numbered 6002 to deny all traffic originating from the user group **huawei**.
   
   ```
   [~DeviceB] acl ipv6 number 6002
   [*DeviceB-acl6-ucl-6002] rule permit ipv6 source ipv6-address any destination user-group huawei
   [*DeviceB-acl6-ucl-6002] rule deny ipv6 source user-group huawei destination ipv6-address any
   [*DeviceB-acl6-ucl-6002] commit
   [~DeviceB-acl6-ucl-6002] quit
   ```
   
   # Configure traffic classifiers.
   
   ```
   [~DeviceB] traffic classifier c1
   [*DeviceB-classifier-c1] if-match ipv6 acl 6000
   [*DeviceB-classifier-c1] commit
   [~DeviceB-classifier-c1] quit
   [~DeviceB] traffic classifier c2
   [*DeviceB-classifier-c2] if-match ipv6 acl 6001
   [*DeviceB-classifier-c2] commit
   [~DeviceB-classifier-c2] quit
   [~DeviceB] traffic classifier c3
   [*DeviceB-classifier-c3] if-match ipv6 acl 6002
   [*DeviceB-classifier-c3] commit
   [~DeviceB-classifier-c3] quit
   ```
   
   # Configure traffic behaviors.
   
   ```
   [~DeviceB] traffic behavior b1
   [*DeviceB-behavior-b1] permit
   [*DeviceB-behavior-b1] commit
   [~DeviceB-behavior-b1] quit
   [~DeviceB] traffic behavior b2
   [*DeviceB-behavior-b2] http-redirect
   [*DeviceB-behavior-b2] commit
   [~DeviceB-behavior-b2] quit
   [~DeviceB] traffic behavior b3
   [*DeviceB-behavior-b3] deny
   [*DeviceB-behavior-b3] commit
   ```
   
   # Configure a traffic policy.
   
   ```
   [~DeviceB] traffic policy policy
   [*DeviceB-trafficpolicy-policy] classifier c1 behavior b1
   [*DeviceB-trafficpolicy-policy] classifier c2 behavior b2
   [*DeviceB-trafficpolicy-policy] classifier c3 behavior b3
   [*DeviceB-trafficpolicy-policy] commit
   [~DeviceB-trafficpolicy-policy] quit
   ```
   
   # Apply the traffic policy globally.
   
   ```
   [~DeviceB] traffic-policy policy inbound
   ```
10. Configure a DUID for the device.
    
    
    ```
    [~DeviceB] dhcpv6 duid 12345678
    [*DeviceB] commit
    ```
11. Configure domains.
    
    
    
    # Configure a pre-authentication domain named **domain1** for web authentication.
    
    ```
    [~DeviceB] aaa
    [~DeviceB-aaa] domain domain1
    [*DeviceB-aaa-domain-domain1] authentication-scheme none
    [*DeviceB-aaa-domain-domain1] accounting-scheme none
    [*DeviceB-aaa-domain-domain1] commit
    [~DeviceB-aaa-domain-domain1] prefix-assign-mode unshared
    [~DeviceB-aaa-domain-domain1] user-group huawei
    [~DeviceB-aaa-domain-domain1] ipv6-pool poolpd
    [~DeviceB-aaa-domain-domain1] web-server 2001:db8:3::2
    [~DeviceB-aaa-domain-domain1] web-server url http://www.isp1.com
    [~DeviceB-aaa-domain-domain1] web-server identical-url
    [~DeviceB-aaa-domain-domain1] quit
    ```
    
    
    
    # Configure a web authentication domain named **isp2**.
    
    ```
    [~DeviceB] aaa
    [~DeviceB-aaa] domain isp2
    [*DeviceB-aaa-domain-isp2] authentication-scheme auth2
    [*DeviceB-aaa-domain-isp2] accounting-scheme acct2
    [*DeviceB-aaa-domain-isp2] radius-server group rd2
    [*DeviceB-aaa-domain-isp2] commit
    [~DeviceB-aaa-domain-isp2] quit
    [~DeviceB-aaa] quit
    ```
12. Configure interfaces.
    
    
    
    # Configure a BAS interface.
    
    ```
    [~DeviceB] interface GigabitEthernet 1/0/2.1
    [~DeviceB-GigabitEthernet1/0/2.1] ipv6 address auto link-local
    [*DeviceB-GigabitEthernet1/0/2.1] ipv6 nd autoconfig managed-address-flag
    [*DeviceB-GigabitEthernet1/0/2.1] commit   
    [~DeviceB-GigabitEthernet1/0/2.1] bas
    [~DeviceB-GigabitEthernet1/0/2.1-bas] access-type layer3-subscriber default-domain pre-authentication isp2 authentication isp2
    [*DeviceB-GigabitEthernet1/0/2.1-bas] commit
    [~DeviceB-GigabitEthernet1/0/2.1-bas] quit
    [~DeviceB-GigabitEthernet1/0/2.1] quit
    ```
    
    # Configure an uplink interface.
    
    ```
    [~DeviceB] interface GigabitEthernet 1/0/1
    [~DeviceB-GigabitEthernet1/0/1] ipv6 enable
    [*DeviceB-GigabitEthernet1/0/1] ipv6 address 2001:db8:4::1/64
    [*DeviceB-GigabitEthernet1/0/1] ipv6 address auto link-local
    [*DeviceB-GigabitEthernet1/0/1] commit
    [~DeviceB-GigabitEthernet1/0/1] quit
    ```

#### Configuration Files

* DeviceA configuration file
  ```
  # 
  sysname DeviceA
  #
  interface GigabitEthernet1/0/1.1
   vlan-type dot1q 1
   ipv6 enable    
   ipv6 address 2001:DB8:1::2/64
   ipv6 address auto link-local
  #
  interface GigabitEthernet1/0/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   dhcp select relay
   ipv6 address auto link-local
   dhcpv6 relay destination 2001:DB8:1::1
  #
  return
  ```
* DeviceB configuration file
  ```
  #
  sysname DeviceB
  #
  radius-server group rd2
   radius-server shared-key-cipher %^%#clY:%[]x='-RMNJus[s/VJ:3YBq3<..|.{'xgbp+%^%#   
   radius-server authentication 192.168.8.249 1812 weight 0
   radius-server accounting 192.168.8.249 1813 weight 0
  #
  ipv6 prefix prefixpd delegation
   
   prefix 2001:DB8:5::/48
  #
  ipv6 prefix na local
   prefix 2001:DB8:2::/64
  #
  ipv6 pool na bas relay
   dns-server 2001:DB8:3::1
   prefix na
  #
  ipv6 pool poolpd bas delegation  
   dns-server 2001:DB8:3::1
  prefix prefixpd
  # 
  user-group huawei
  #
  acl ipv6 number 6000
   rule 5 permit ipv6 source user-group huawei destination ipv6-address 2001:DB8:3::2/128
   rule 10 permit ipv6 source ipv6-address 2001:DB8:3::2/128 destination user-group huawei
   rule 15 permit ipv6 source user-group huawei destination ipv6-address 2001:DB8:3::1/128
   rule 20 permit ipv6 source ipv6-address 2001:DB8:3::1/128 destination user-group huawei
  #
  acl ipv6 number 6001 
   rule 5 permit tcp source user-group huawei destination-port eq www 
   rule 10 permit tcp source user-group huawei destination-port eq 8080
  #
  acl ipv6 number 6002 
   rule 5 permit ipv6 source ipv6-address any destination user-group huawei 
   rule 10 deny ipv6 source user-group huawei destination ipv6-address any
  #
  dhcpv6 duid 12345678
  #
  traffic classifier c1 operator or
   if-match ipv6 acl 6000 precedence 21
  #
  traffic classifier c2 operator or
   if-match ipv6 acl 6001 precedence 23
  #
  traffic classifier c3 operator or
   if-match ipv6 acl 6002 precedence 25
  #
  traffic behavior b1
  #
  traffic behavior b2
   http-redirect 
  #
  traffic behavior b3
   deny
  #
  traffic policy policy
   share-mode
   classifier c1 behavior b1 precedence 1
   classifier c2 behavior b2 precedence 2
   classifier c3 behavior b3 precedence 3
  #
  aaa
   default-password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
   #
   authentication-scheme default0
   #
   authentication-scheme default1
   #
   authentication-scheme default
    authentication-mode local radius
   #
   authentication-scheme auth2
   #
   authorization-scheme default
   #
   accounting-scheme default0
   #
   accounting-scheme default1
   #
   accounting-scheme acct2
   #
   domain default0
   #
   domain default1
   #
   domain default_admin
   #
   domain domain1
    authentication-scheme none
    accounting-scheme none
    prefix-assign-mode unshared 
    user-group huawei
    ipv6-pool poolpd
    web-server 2001:db8:3::2
    web-server url http://www.isp1.com
    web-server identical-url
   #
   domain isp2
    authentication-scheme auth2
    accounting-scheme acct2
    radius-server group rd2
  #
  interface GigabitEthernet1/0/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   ipv6 address auto link-local
   dcn
  #
  interface GigabitEthernet1/0/2
   undo shutdown
  #
  interface GigabitEthernet1/0/2.1
   vlan-type dot1q 1
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   ipv6 nd autoconfig managed-address-flag
   bas
   #
    access-type layer3-subscriber default-domain pre-authentication isp2 authentication isp2
   #
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:3::3/128
   ipv6 address auto link-local
  #
  traffic-policy policy inbound
  #
  web-auth-server enable
  web-auth-server source interface LoopBack0
  web-auth-server 2001:DB8:3::2 port 50100 key cipher %^%#\39J9tmKl#+;)]1yEd@V#i(1Jeq"vO=9ka=-\qN<%^%# 
  #
  undo web-auth-server source-ip all
  #
  undo web-auth-server source-ipv6 all
  web-auth-server source-ipv6 2001:DB8:3::3
  #
  return
  ```