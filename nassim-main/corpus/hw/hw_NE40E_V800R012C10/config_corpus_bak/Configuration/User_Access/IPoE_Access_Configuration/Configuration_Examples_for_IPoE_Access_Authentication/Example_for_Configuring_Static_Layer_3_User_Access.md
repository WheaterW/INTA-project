Example for Configuring Static Layer 3 User Access
==================================================

This section provides an example for configuring IPoE access for static Layer 3 users. An IPoE user obtains an IP address from the DHCP server over a DHCP relay agent and accesses the Layer 3 BAS interface of the BRAS through static routing. The BRAS provides the RADIUS authentication and accounting functions. After the user is authenticated, it accesses the network from the BRAS as a static Layer 3 user.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0258838470__fig_dc_ne_ipox_cfg_014801), an IPoE user obtains an IP address from the DHCP server through DeviceA, which functions as a DHCP relay agent. On DeviceA, a static route is configured, with the next-hop address being the IP address of the Layer 3 BAS interface and the destination address being the Internet server address. DeviceB functions as a BRAS that provides the RADIUS authentication and accounting functions, and web authentication is used. After being authenticated, the IPoE user accesses the network as a static Layer 3 user through GE 0/1/1.1 on DeviceB.

**Figure 1** Configuring static Layer 3 user access![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE 0/1/1, GE 0/1/2.1, GE 0/1/3, and GE 0/1/1.1, respectively.


  
![](figure/en-us_image_0258838471.png)

| Device | Interface | IPv4 Address | IPv6 Address |
| --- | --- | --- | --- |
| DeviceA | GE 0/1/1 | 10.10.10.1/24 | 2001:db8:1::1/120 |
| GE 0/1/2.1 | 10.0.0.1/24 | 2001:db8:2::1/120 |
| GE 0/1/3 | 192.168.1.1/24 | 2001:db8:3::1/120 |
| DeviceB | GE 0/1/1.1 | 10.0.0.2/24 | 2001:db8:2::2/120 |
| Loopback0 | 192.168.8.1/32 | 2001:db8:4::1/128 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on DeviceA and DeviceB.
2. On DeviceA, configure a static route with the next-hop address being the IP address of a Layer 3 BAS interface.
3. Configure DeviceA to generate DUIDs.
4. Configure DeviceB to generate DUIDs.
5. Configure AAA schemes and a RADIUS server group.
6. Configure a user password.
7. Configure domains
8. Configure a web authentication server.
9. Configure a traffic policy.
10. On DeviceB, configure a BAS interface for static user access.
11. Configure static Layer 3 users.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme names and authentication modes
* Accounting scheme names and accounting modes
* RADIUS server group name, RADIUS authentication server's IP address and port number, and RADIUS accounting server's IP address and port number
* Domain names
* IP address of the web authentication server
* ACL rules
* Traffic policy name
* BAS interface parameters

#### Procedure

1. Configure IP addresses for interfaces on DeviceA and DeviceB.
   
   
   
   # Assign an IPv4 address and an IPv6 address to the interface connecting DeviceA to the user and configure the DHCP relay function on the interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface gigabitethernet 0/1/1
   [~DeviceA-GigabitEthernet0/1/1] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/1] ip address 10.10.10.1 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/1] ip relay address 192.168.1.2
   [*DeviceA-GigabitEthernet0/1/1] dhcp select relay
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8:1::1/120
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address auto link-local
   [*DeviceA-GigabitEthernet0/1/1] dhcpv6 relay destination 2001:db8:3::2
   [*DeviceA-GigabitEthernet0/1/1] commit
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Assign an IPv4 address and an IPv6 address to the interface connecting DeviceA to DeviceB.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/2.1
   [*DeviceA-GigabitEthernet0/1/2.1] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/2.1] ip address 10.0.0.1 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/2.1] ipv6 address 2001:db8:2::1/120 
   [*DeviceA-GigabitEthernet0/1/2.1] vlan-type dot1q 1
   [*DeviceA-GigabitEthernet0/1/2.1] ipv6 address auto link-local 
   [*DeviceA-GigabitEthernet0/1/2.1] commit
   [~DeviceA-GigabitEthernet0/1/2.1] quit
   ```
   
   # Assign an IP address to the interface connecting DeviceA to the DHCPv6 server, and enable DHCPv6 on the interface.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/3 
   [~DeviceA-GigabitEthernet0/1/3] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/3] ip address 192.168.1.1 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/3] ipv6 address 2001:db8:3::1/120
   [*DeviceA-GigabitEthernet0/1/3] ipv6 address auto link-local
   [*DeviceA-GigabitEthernet0/1/3] commit
   [~DeviceA-GigabitEthernet0/1/3] quit
   ```
   
   # Assign an IPv4 address and an IPv6 address to GE 0/1/1.1 on DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface gigabitethernet 0/1/1.1
   [*DeviceB-GigabitEthernet0/1/1.1] commit
   [~DeviceB-GigabitEthernet0/1/1.1] ipv6 enable
   [*DeviceB-GigabitEthernet0/1/1.1] ip address 10.0.0.2 255.255.255.0 
   [*DeviceB-GigabitEthernet0/1/1.1] ipv6 address 2001:db8:2::2/120 
   [*DeviceB-GigabitEthernet0/1/1.1] commit
   ```
2. On DeviceA, configure a static route with the next-hop address being the IP address of a Layer 3 BAS interface.
   
   
   ```
   [~DeviceA] ip route-static 10.1.1.1 32 10.0.0.2
   [~DeviceA] ipv6 route-static 2001:db8:: 128 2001:db8:2::2
   ```
3. Configure DeviceA to generate DUIDs.
   
   
   ```
   [~DeviceA] dhcpv6 duid llt
   [*DeviceA] commit
   ```
4. Configure DeviceB to generate DUIDs.
   
   
   ```
   [~DeviceB] dhcpv6 duid llt
   [*DeviceB] commit
   ```
5. Configure AAA schemes and a RADIUS server group.
   
   
   
   # Configure authentication schemes.
   
   ```
   [~DeviceB] aaa
   [~DeviceB-aaa] authentication-scheme auth2
   [*DeviceB-aaa-authen-auth2] authentication-mode radius
   [*DeviceB-aaa-authen-auth2] quit
   [*DeviceB-aaa] authentication-scheme none
   [*DeviceB-aaa-authen-none] authentication-mode none
   [*DeviceB-aaa-authen-none] quit
   [*DeviceB-aaa] commit
   ```
   
   # Configure accounting schemes.
   
   ```
   [~DeviceB-aaa] accounting-scheme acct2
   [*DeviceB-aaa-accounting-acct2] accounting-mode radius
   [*DeviceB-aaa-accounting-acct2] quit
   [*DeviceB-aaa] accounting-scheme none
   [*DeviceB-aaa-accounting-none] accounting-mode none
   [*DeviceB-aaa-accounting-none] quit
   [*DeviceB-aaa] commit
   [~DeviceB-aaa] quit
   ```
   
   # Configure a loopback interface.
   
   ```
   [~DeviceB] interface loopBack 0
   [*DeviceB-LoopBack0] ipv6 enable
   [*DeviceB-LoopBack0] ip address 192.168.8.1 255.255.255.255
   [*DeviceB-LoopBack0] ipv6 address 2001:db8:4::1 128
   [*DeviceB-LoopBack0] ipv6 address auto link-local 
   [*DeviceB-LoopBack0] commit 
   [~DeviceB-LoopBack0] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~DeviceB] radius-server group rd1
   [*DeviceB-radius-rd1] radius-server authentication 192.168.8.55 1645
   [*DeviceB-radius-rd1] radius-server accounting 192.168.8.55 1646
   [*DeviceB-radius-rd1] radius-server source interface LoopBack 0
   [*DeviceB-radius-rd1] commit 
   [~DeviceB-radius-rd1] radius-server shared-key-cipher it-is-my-secret1
   [*DeviceB-radius-rd1] commit
   [~DeviceB-radius-rd1] quit
   ```
6. Configure the IPoE user password.
   
   
   ```
   [~DeviceB] aaa
   ```
   ```
   [~DeviceB-aaa] default-password cipher YsHsjx_202206
   ```
   ```
   [*DeviceB-aaa] commit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
7. Configure domains.
   
   
   
   # Configure a web pre-authentication domain named **pre**, and bind the authentication scheme with the none authentication mode specified and the accounting scheme with the none accounting mode specified to this domain.
   
   ```
   [~DeviceB] user-group web-before
   [~DeviceB] aaa
   [~DeviceB-aaa] domain pre
   [*DeviceB-aaa-domain-pre] commit
   [~DeviceB-aaa-domain-pre] user-group web-before
   [~DeviceB-aaa-domain-pre] authentication-scheme none
   [*DeviceB-aaa-domain-pre] accounting-scheme none
   [*DeviceB-aaa-domain-pre] commit
   [~DeviceB-aaa-domain-pre] web-server 192.168.8.251 2001:db8:3::2 
   [~DeviceB-aaa-domain-pre] web-server url http://www.isp1.com
   [~DeviceB-aaa-domain-pre] web-server identical-url 
   [~DeviceB-aaa-domain-pre] quit
   ```
   
   # Configure a web authentication domain named **huawei**.
   
   ```
   [~DeviceB-aaa] domain huawei
   [*DeviceB-aaa-domain-huawei] authentication-scheme auth2
   [*DeviceB-aaa-domain-huawei] accounting-scheme acct2
   [*DeviceB-aaa-domain-huawei] radius-server group rd1
   [*DeviceB-aaa-domain-huawei] commit
   [~DeviceB-aaa-domain-huawei] quit
   [~DeviceB-aaa] quit
   ```
8. Configure a web authentication server.
   
   
   ```
   [~DeviceB] web-auth-server enable
   [~DeviceB] web-auth-server source interface LoopBack 0
   [~DeviceB] web-auth-server 192.168.8.251 key cipher webvlan
   [~DeviceB] web-auth-server 2001:db8:4::2 key cipher webvlan
   [~DeviceB] web-auth-server source-ip 192.168.8.251
   [~DeviceB] web-auth-server source-ipv6 2001:db8:4::2
   ```
9. Configure a traffic policy.
   
   
   
   # Configure an ACL numbered 6000 to permit the traffic between the user group **web-before** and the web authentication server.
   
   ```
   [~DeviceB] acl 6000
   [*DeviceB-acl-ucl-6000] rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
   [*DeviceB-acl-ucl-6000] rule 10 permit ip source ip-address 192.168.8.251 0 destination user-group web-before
   [*DeviceB-acl-ucl-6000] commit
   [~DeviceB-acl-ucl-6000] quit
   [~DeviceB] acl ipv6 number 6000
   [*DeviceB-acl6-ucl-6000] rule 5 permit ipv6 source user-group web-before destination ipv6-address 2001:db8:4::2/128
   [*DeviceB-acl6-ucl-6000] rule 10 permit ipv6 source ipv6-address 2001:db8:4::2/128 destination user-group web-before
   [*DeviceB-acl6-ucl-6000] commit
   [~DeviceB-acl6-ucl-6000] quit
   ```
   
   # Configure an ACL numbered 6001 to allow HTTP redirect for the TCP packets originating from the user group **web-before** and whose destination port information is www or 8080.
   
   ```
   [~DeviceB] acl 6001
   [*DeviceB-acl-ucl-6001] rule 5 permit tcp source user-group web-before destination-port eq www
   [*DeviceB-acl-ucl-6001] rule 10 permit tcp source user-group web-before destination-port eq 8080
   [*DeviceB-acl-ucl-6001] commit
   [~DeviceB-acl-ucl-6001] quit
   [~DeviceB] acl ipv6 number 6001
   [*DeviceB-acl6-ucl-6001] rule 5 permit tcp source user-group web-before destination-port eq www
   [*DeviceB-acl6-ucl-6001] rule 10 permit tcp source user-group web-before destination-port eq 8080
   [*DeviceB-acl6-ucl-6001] commit
   [~DeviceB-acl6-ucl-6001] quit
   ```
   
   # Configure an ACL numbered 6002 to deny all the traffic originating from the user group **huawei**.
   
   ```
   [~DeviceB] acl 6002
   [*DeviceB-acl-ucl-6002] rule 5 permit ip source ip-address any destination user-group web-before
   [*DeviceB-acl-ucl-6002] rule 10 permit ip source user-group web-before destination ip-address any 
   [*DeviceB-acl-ucl-6002] commit
   [~DeviceB-acl-ucl-6002] quit
   [~DeviceB] acl ipv6 number 6002
   [*DeviceB-acl6-ucl-6002] rule 5 permit ipv6 source ipv6-address any destination user-group web-before
   [*DeviceB-acl6-ucl-6002] rule 10 permit ipv6 source user-group web-before destination ipv6-address any
   [*DeviceB-acl6-ucl-6002] commit
   [~DeviceB-acl6-ucl-6002] quit
   ```
   
   # Configure traffic classifiers.
   
   ```
   [~DeviceB] traffic classifier web_permit
   [*DeviceB-classifier-web_permit] if-match acl 6000
   [*DeviceB-classifier-web_permit] if-match ipv6 acl 6000
   [*DeviceB-classifier-web_permit] commit
   [~DeviceB-classifier-web_permit] quit
   [~DeviceB] traffic classifier redirect 
   [*DeviceB-classifier-redirect] if-match acl 6001
   [*DeviceB-classifier-redirect] if-match ipv6 acl 6001
   [*DeviceB-classifier-redirect] commit
   [~DeviceB-classifier-redirect] quit
   [~DeviceB] traffic classifier web_deny
   [*DeviceB-classifier-web_deny] if-match acl 6002
   [*DeviceB-classifier-web_deny] if-match ipv6 acl 6002
   [*DeviceB-classifier-web_deny] commit
   [~DeviceB-classifier-web_deny] quit
   ```
   
   # Configure traffic behaviors.
   
   ```
   [~DeviceB] traffic behavior web_permit
   [*DeviceB-behavior-web_permit] permit
   [*DeviceB-behavior-web_permit] commit
   [~DeviceB-behavior-web_permit] quit
   [~DeviceB] traffic behavior redirect
   [*DeviceB-behavior-redirect] http-redirect
   [*DeviceB-behavior-redirect] commit
   [~DeviceB-behavior-redirect] quit
   [~DeviceB] traffic behavior web_deny
   [*DeviceB-behavior-web_deny] deny
   [*DeviceB-behavior-web_deny] commit
   [~DeviceB-behavior-web_deny] quit
   ```
   
   # Configure a traffic policy.
   
   ```
   [~DeviceB] traffic policy web 
   [*DeviceB-trafficpolicy-web] share-mode
   [*DeviceB-trafficpolicy-web] classifier web_permit behavior web_permit
   [*DeviceB-trafficpolicy-web] classifier redirect behavior redirect
   [*DeviceB-trafficpolicy-web] classifier web_deny behavior web_deny
   [*DeviceB-trafficpolicy-web] commit
   [~DeviceB-trafficpolicy-web] quit
   ```
   
   # Apply the user-side traffic policy globally.
   
   ```
   [~DeviceB] traffic-policy web inbound
   [*DeviceB] commit
   ```
10. Configure a BAS interface for static user access.
    
    
    ```
    [~DeviceB] interface gigabitethernet 0/1/1.1
    [~DeviceB-GigabitEthernet0/1/1.1] vlan-type dot1q 1
    [*DeviceB-GigabitEthernet0/1/1.1] ipv6 address auto link-local
    [*DeviceB-GigabitEthernet0/1/1.1] commit
    [~DeviceB-GigabitEthernet0/1/1.1] bas
    [~DeviceB-GigabitEthernet0/1/1.1-bas] access-type layer3-subscriber default-domain pre-authentication pre authentication huawei
    [*DeviceB-GigabitEthernet0/1/1.1-bas] commit
    [~DeviceB-GigabitEthernet0/1/1.1-bas] quit
    [~DeviceB-GigabitEthernet0/1/1.1] quit
    ```
11. Configure static Layer 3 users.
    
    
    ```
    [~DeviceB] layer3-subscriber 10.10.10.2 10.10.10.3 2001:db8:1::2 2001:db8:1::3 domain-name pre
    [*DeviceB] commit
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    For Layer 3 users who do not obtain IP addresses through DeviceB, you must run the [**layer3-subscriber**](cmdqueryname=layer3-subscriber) *start-ip-address* [ *end-ip-address* ] [ **vpn-instance** *instance-name* ] **domain-name** *domain-name* command in the system view to specify the IP address range to which the static Layer 3 users belong and the name of the associated authentication domain.
12. Verify the configuration.
    
    
    
    # After completing the configurations, run the [**display access-user domain**](cmdqueryname=display+access-user+domain) command to check information about the user in the domain. The command output shows that the user has gone online successfully.
    
    
    
    ```
    [~DeviceB] display access-user domain pre
    ------------------------------------------------------------------------------
      UserID  Username                Interface      IP address       MAC
              Vlan          IPv6 address             Access type
    ------------------------------------------------------------------------------
      20      user1@pre        GE0/1/1.1      10.10.10.200    00e0-fc12-3456
              1/-           -                        IPOE 
    ------------------------------------------------------------------------------
    ```
    
    # After the user opens a browser on the PC and enters a website address in the address bar, a web authentication page is displayed. The user then enters the username and password. If the user is authenticated, it can enter the post-authentication domain. You can run the **display access-user domain** command to check whether the user is online in the domain.
    
    ```
    <DeviceA> display access-user domain huawei
    ------------------------------------------------------------------------------
      UserID  Username                Interface      IP address       MAC
              Vlan          IPv6 address             Access type
    ------------------------------------------------------------------------------
      20      user1@huawei     GE0/1/1.1      10.10.10.200     00e0-fc12-3456
              1/-           -                        IPOE 
    ------------------------------------------------------------------------------
    ```

#### Configuration Files

* DeviceA configuration file
  ```
  #
  sysname DeviceA
  #
  dhcpv6 duid 0001000125a7625df063f9761497
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ip address 10.10.10.1 255.255.255.0
   ipv6 address 2001:DB8:1::1/120
   ipv6 address auto link-local
   dhcp select relay
   ip relay address 192.168.1.2
   dhcpv6 relay destination 2001:DB8:3::2
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1
   vlan-type dot1q 1
   ipv6 enable
   ip address 10.0.0.1 255.255.255.0
   ipv6 address 2001:DB8:2::1/120 
   ipv6 address auto link-local 
  #
  interface GigabitEthernet0/1/3 
   undo shutdown
   ipv6 enable
   ip address 192.168.1.1 255.255.255.0
   ipv6 address 2001:DB8:3::1/120
   ipv6 address auto link-local
  #
  ip route-static 10.1.1.1 255.255.255.255 10.0.0.2
  ipv6 route-static 2001:DB8:: 128 2001:DB8:2::2
  #
  return
  ```
* DeviceB configuration file
  ```
  #
  sysname DeviceB
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
  acl ipv6 number 6000
   rule 5 permit ipv6 source user-group web-before destination ipv6-address 2001:DB8:4::2/128
   rule 10 permit ipv6 source ipv6-address 2001:DB8:4::2/128 destination user-group web-before
  #
  acl ipv6 number 6001
   rule 5 permit tcp source user-group web-before destination-port eq www
   rule 10 permit tcp source user-group web-before destination-port eq 8080
  #
  acl ipv6 number 6002
   rule 5 permit ipv6 source ipv6-address any destination user-group web-before
   rule 10 permit ipv6 source user-group web-before destination ipv6-address any
  #
  dhcpv6 duid 0001000125a7625df063f9761498
  #
  traffic classifier redirect operator or
   if-match acl 6001 precedence 18
   if-match ipv6 acl 6001 precedence 19
  #
  traffic classifier web_deny operator or
   if-match acl 6002 precedence 20
   if-match ipv6 acl 6002 precedence 21
  #
  traffic classifier web_permit operator or
   if-match acl 6000 precedence 1 
   if-match ipv6 acl 6000 precedence 17
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
   default-password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
   #
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
    web-server 192.168.8.251 2001:DB8:3::2
    web-server url http://www.isp1.com
    web-server identical-url
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 1
   ipv6 enable
   ip address 10.0.0.2 255.255.255.0
   ipv6 address 2001:DB8:2::2/120
   ipv6 address auto link-local
   bas
   #
    access-type layer3-subscriber default-domain pre-authentication pre authentication huawei
  #
  interface LoopBack0
   ipv6 enable
   ip address 192.168.8.1 255.255.255.255
   ipv6 address 2001:DB8:4::1 128
   ipv6 address auto link-local 
  #
  web-auth-server enable
  web-auth-server source interface LoopBack 0
  web-auth-server 192.168.8.251 port 50100 key cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
  web-auth-server 2001:DB8:4::2 port 50100 key cipher %^%#clY:%[]x='-RMNJus[s/VJ:3YBq3<..|.{'xgbp+%^%#
  #
  undo web-auth-server source-ip all
  web-auth-server source-ip 192.168.8.251
  #
  undo web-auth-server source-ipv6 all
  web-auth-server source-ipv6 2001:DB8:4::2
  #
  traffic-policy web inbound
  #
  layer3-subscriber 10.10.10.2 10.10.10.3 2001:DB8:1::2 2001:DB8:1::3 domain-name pre
  #
  return
  ```