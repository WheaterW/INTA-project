Example for Configuring HTTPS Redirect for Web Authentication of Layer 2 IPoE Users
===================================================================================

This section provides an example for configuring HTTPS redirect for web authentication of Layer 2 IPoE users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0242541453__fig1070175815327), the user belongs to the domain **isp1**, and the device is configured with HTTPS redirect as well as RADIUS authentication and accounting schemes. When accessing the Internet, the user needs to enter the username and password on the web page. After the user passes the authentication, the user can access the Internet through interface1 on DeviceA in Layer 2 IPoE mode.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and interface2 in this example represent GE 0/1/2.1 and GE 0/1/1, respectively.


**Figure 1** Configuring HTTPS redirect for web authentication of Layer 2 IPoE users  
![](figure/en-us_image_0242581954.png)

#### Configuration Roadmap

The configuration roadmap is as follows: (All the configurations are performed on DeviceA.)

1. Configure a user group.
2. Configure a cipher suite and HTTPS self-signed certificate.
3. Configure an address pool.
4. Configure authentication and accounting schemes.
5. Configure a RADIUS server group.
6. Configure a web pre-authentication domain and web authentication domain. Then, configure HTTPS redirect.
7. Configure a web authentication server.
8. Configure ACL rules and a traffic policy.
9. Configure BAS and upstream interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, RADIUS authentication server's IP address and port number, and RADIUS accounting server's IP address and port number
* Address pool name, gateway address, and DNS server address
* Domain names
* IP addresses of the web server (web page server) and web authentication server (In this example, the two servers are deployed on the same device that supports HTTPS.)
* ACL rules
* Traffic policy
* BAS interface parameters

#### Procedure

1. Configure a user group.
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceA 
   [*HUAWEI] commit 
   [~DeviceA] user-group huawei
   ```
2. Configure a cipher suite and HTTPS self-signed certificate.
   ```
   [~DeviceA] access https-redirect 
   [*DeviceA-access-https-redirect] self-signed rsa modulus 2048
   [*DeviceA-access-https-redirect] cipher-suite support c02f 1301 1302 c02b
   [*DeviceA-access-https-redirect] commit
   [~DeviceA-access-https-redirect] quit
   ```
3. Configure an address pool.
   ```
   [~DeviceA] ip pool huawei bas local 
   [*DeviceA-ip-pool-huawei] gateway 10.10.10.1 24
   [*DeviceA-ip-pool-huawei] commit
   [~DeviceA-ip-pool-huawei] section 0 10.10.10.2 10.10.10.200
   [~DeviceA-ip-pool-huawei] dns-server 1.1.1.1
   [*DeviceA-ip-pool-huawei] commit
   [~DeviceA-ip-pool-huawei] quit
   ```
4. Configure authentication and accounting schemes.
   
   # Configure authentication schemes.
   
   ```
   [~DeviceA] aaa 
   [~DeviceA-aaa] authentication-scheme auth2 
   [*DeviceA-aaa-authen-auth2] authentication-mode radius 
   [*DeviceA-aaa-authen-auth2] commit 
   [~DeviceA-aaa-authen-auth2] quit 
   [~DeviceA-aaa] authentication-scheme none  
   [*DeviceA-aaa-authen-none] authentication-mode none 
   [*DeviceA-aaa-authen-none] commit
   [~DeviceA-aaa-authen-none] quit
   ```
   
   # Configure accounting schemes.
   
   ```
   [~DeviceA-aaa] accounting-scheme acct2 
   [*DeviceA-aaa-accounting-acct2] accounting-mode radius 
   [*DeviceA-aaa-accounting-acct2] commit
   [~DeviceA-aaa-accounting-acct2] quit
   [~DeviceA-aaa] accounting-scheme none
   [*DeviceA-aaa-accounting-none] accounting-mode none
   [*DeviceA-aaa-accounting-none] commit
   [~DeviceA-aaa-accounting-none] quit
   ```
   
   # Configure the IPoE user password.
   
   ```
   [~DeviceA-aaa] default-password cipher YsHsjx_202206
   [*DeviceA-aaa] commit
   [~DeviceA-aaa] quit
   ```
5. Configure a RADIUS server group.
   ```
   [~DeviceA] radius-server group rd2 
   [*DeviceA-radius-rd2] radius-server authentication 192.168.8.249 1812 
   [*DeviceA-radius-rd2] radius-server accounting 192.168.8.249 1813 
   [*DeviceA-radius-rd2] radius-server shared-key Huawei 
   [*DeviceA-radius-rd2] commit 
   [~DeviceA-radius-rd2] quit
   ```
6. Configure a web pre-authentication domain and web authentication domain. Then, configure HTTPS redirect.
   
   # Configure a web pre-authentication domain named **web\_before**. Then, configure HTTPS redirect.
   
   ```
   [~DeviceA] aaa 
   [~DeviceA-aaa] domain web_before 
   [*DeviceA-aaa-domain-web_before] commit
   [~DeviceA-aaa-domain-web_before] web-server mode post
   [~DeviceA-aaa-domain-web_before] authentication-scheme none
   [*DeviceA-aaa-domain-web_before] accounting-scheme none 
   [*DeviceA-aaa-domain-web_before] commit
   [~DeviceA-aaa-domain-web_before] user-group huawei
   [*DeviceA-aaa-domain-web_before] commit
   [~DeviceA-aaa-domain-web_before] web-server 192.168.8.251 
   [~DeviceA-aaa-domain-web_before] web-server url https://192.168.8.251
   [~DeviceA-aaa-domain-web_before] ip-pool huawei 
   [~DeviceA-aaa-domain-web_before] quit
   ```
   
   # Configure a web authentication domain named **isp1**.
   
   ```
   [~DeviceA-aaa] domain isp1
   [*DeviceA-aaa-domain-isp1] authentication-scheme auth2 
   [*DeviceA-aaa-domain-isp1] accounting-scheme acct2 
   [*DeviceA-aaa-domain-isp1] radius-server group rd2 
   [*DeviceA-aaa-domain-isp1] commit 
   [~DeviceA-aaa-domain-isp1] quit 
   [~DeviceA-aaa] quit
   ```
7. Configure a web authentication server.
   ```
   [~DeviceA] web-auth-server enable
   [~DeviceA] interface loopback 0
   [*DeviceA-LoopBack0] ip address 192.168.8.1 255.255.255.0
   [*DeviceA-LoopBack0] commit
   [~DeviceA-LoopBack0] quit
   [~DeviceA] web-auth-server source interface loopBack0
   [~DeviceA] web-auth-server source-ip 192.168.8.1
   [~DeviceA] web-auth-server 192.168.8.251 key cipher Huawei
   ```
8. Configure a traffic policy.
   1. Configure ACLs.
      
      # Configure an ACL numbered 6000 to permit the traffic originating from the user group **huawei** to the web server and DNS server.
      
      ```
      [~DeviceA] acl 6000 
      [*DeviceA-acl-ucl-6000] rule 5 permit tcp source user-group huawei destination ip-address 192.168.8.251 0  
      [*DeviceA-acl-ucl-6000] rule 10 permit ip source ip-address 192.168.8.251 0 destination user-group huawei
      [*DeviceA-acl-ucl-6000] rule 15 permit ip source user-group huawei destination ip-address 1.1.1.1 0
      [*DeviceA-acl-ucl-6000] commit 
      [~DeviceA-acl-ucl-6000] quit
      ```
      
      # Configure an ACL numbered 6001 to allow HTTPS redirect for the TCP packets originating from the user group **huawei** with the destination port number being 443.
      
      ```
      [~DeviceA] acl 6001 
      [*DeviceA-acl-ucl-6001] rule 5 permit tcp source user-group huawei destination-port eq 443
      [*DeviceA-acl-ucl-6001] commit 
      [~DeviceA-acl-ucl-6001] quit
      ```
      
      # Configure an ACL numbered 6002 to deny the traffic originating from the user group **huawei**.
      
      ```
      [~DeviceA] acl 6002 
      [*DeviceA-acl-ucl-6002] rule 5 permit ip source user-group huawei destination ip-address any
      [*DeviceA-acl-ucl-6002] rule 10 permit ip source user-group huawei destination user-group huawei
      [*DeviceA-acl-ucl-6002] commit 
      [~DeviceA-acl-ucl-6002] quit
      ```
   2. Configure traffic classifiers.
      
      # Configure a traffic classifier named **c1**, and apply ACL 6000 to it.
      
      ```
      [~DeviceA] traffic classifier c1 
      [*DeviceA-classifier-c1] if-match acl 6000 
      [*DeviceA-classifier-c1] commit 
      [~DeviceA-classifier-c1] quit
      ```
      
      # Configure a traffic classifier named **c2** and apply ACL 6001 to it.
      
      ```
      [~DeviceA] traffic classifier c2 
      [*DeviceA-classifier-c2] if-match acl 6001 
      [*DeviceA-classifier-c2] commit 
      [~DeviceA-classifier-c2] quit
      ```
      
      # Configure a traffic classifier named **c3** and apply ACL 6002 to it.
      
      ```
      [~DeviceA] traffic classifier c3 
      [*DeviceA-classifier-c3] if-match acl 6002 
      [*DeviceA-classifier-c3] commit 
      [~DeviceA-classifier-c3] quit
      ```
   3. Configure traffic behaviors.
      
      # Configure a traffic behavior named **b1**.
      
      ```
      [~DeviceA] traffic behavior b1 
      [*DeviceA-behavior-b1] permit 
      [*DeviceA-behavior-b1] commit 
      [~DeviceA-behavior-b1] quit
      ```
      
      # Configure a traffic behavior named **b2**.
      
      ```
      [~DeviceA] traffic behavior b2
      [*DeviceA-behavior-b2] https-redirect 
      [*DeviceA-behavior-b2] commit 
      [~DeviceA-behavior-b2] quit
      ```
      
      # Configure a traffic behavior named **b3**.
      
      ```
      [~DeviceA] traffic behavior b3
      [*DeviceA-behavior-b3] deny 
      [*DeviceA-behavior-b3] commit 
      [~DeviceA-behavior-b3] quit
      ```
   4. Configure a traffic policy.
      
      # Configure a traffic policy named **p1**.
      
      ```
      [~DeviceA] traffic policy p1 
      [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1 
      [*DeviceA-trafficpolicy-p1] classifier c2 behavior b2 
      [*DeviceA-trafficpolicy-p1] classifier c3 behavior b3
      [*DeviceA-trafficpolicy-p1] commit 
      [~DeviceA-trafficpolicy-p1] quit
      ```
   5. Apply the traffic policy.
      ```
      [~DeviceA] traffic-policy p1 inbound
      Warning: After this operation is performed,the global ucl traffic policy becomes effective. Continue? [Y/N]:Y
      [*DeviceA] commit
      ```
9. Configure interfaces.# Configure a BAS interface.
   ```
   [~DeviceA] interface GigabitEthernet0/1/2.1
   [*DeviceA-GigabitEthernet0/1/2.1] commit 
   [~DeviceA-GigabitEthernet0/1/2.1] user-vlan 1 
   [~DeviceA-GigabitEthernet0/1/2.1-vlan-1-1] quit
   [~DeviceA-GigabitEthernet0/1/2.1] bas  
   [~DeviceA-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain pre-authentication web_before authentication isp1 
   [*DeviceA-GigabitEthernet0/1/2.1-bas] authentication-method web
   [*DeviceA-GigabitEthernet0/1/2.1-bas] commit 
   [~DeviceA-GigabitEthernet0/1/2.1-bas] quit 
   [~DeviceA-GigabitEthernet0/1/2.1] quit
   ```
   
   # Configure an upstream interface connecting the device to the Internet.
   ```
   [~DeviceA] interface GigabitEthernet0/1/1 
   [*DeviceA-GigabitEthernet0/1/1] ip address 192.168.2.1 255.255.255.0 
   [*DeviceA-GigabitEthernet0/1/1] commit
   [~DeviceA-GigabitEthernet0/1/1] quit
   [~DeviceA] quit
   ```
10. Verify the configuration.
    
    After completing the configurations, have the user go online. Then, run the **display access-user domain** command to check information about the user in the domain. The command output shows that the user has gone online successfully.
    
    ```
    <DeviceA> display access-user domain web_before
    --------------------------------------------------------------------------------
       UserID  Username                Interface      IP address       MAC 
               Vlan          IPv6 address             Access type 
    -------------------------------------------------------------------------------- 
       20      user1@web_before        GE0/1/2.1      10.10.10.200    00e0-fc12-3456 
               1/-           -                        IPOE  
    -------------------------------------------------------------------------------- 
    ```
    After the user opens a browser on the PC and enters an HTTPS website address in the address bar, a web authentication page is displayed. The user then enters the username and password. After being authenticated, the user can enter the authentication domain. You can run the **display access-user domain** command to check whether the user is online in the domain.
    ```
    <DeviceA> display access-user domain isp1
    --------------------------------------------------------------------------------- 
       UserID  Username                Interface      IP address       MAC 
               Vlan          IPv6 address             Access type 
    --------------------------------------------------------------------------------- 
       20      user1@isp1         GE0/1/2.1           10.10.10.200    00e0-fc12-3456 
               1/-           -                        IPOE  
    --------------------------------------------------------------------------------- 
    ```


#### Configuration Files

```
# 
sysname DeviceA  
# 
radius-server group rd2 
 radius-server shared-key-cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%# 
 radius-server authentication 192.168.8.249 1812 weight 0 
 radius-server accounting 192.168.8.249 1813 weight 0       
# 
ip pool huawei bas local 
 gateway 10.10.10.1 255.255.255.0 
 section 0 10.10.10.2 10.10.10.200
 dns-server 1.1.1.1  
#
access https-redirect
 self-signed rsa modulus 2048
 cipher-suite support c02f 1301 1302 c02b
# 
user-group huawei
# 
acl number 6000 
 rule 5 permit tcp source user-group huawei destination ip-address 192.168.8.251 0
 rule 10 permit ip source ip-address 192.168.8.251 0 destination user-group huawei
 rule 15 permit ip source user-group huawei destination ip-address 1.1.1.1 0
# 
acl number 6001 
 rule 5 permit tcp source user-group huawei destination-port eq 443
# 
acl number 6002 
 rule 5 permit ip source user-group huawei destination ip-address any
 rule 10 permit ip source user-group huawei destination user-group huawei
#
traffic classifier c1 operator or
 if-match acl 6000 precedence 8
# 
traffic classifier c2 operator or
 if-match acl 6001 precedence 9
# 
traffic classifier c3 operator or
 if-match acl 6002 precedence 10
#
traffic behavior b1 
# 
traffic behavior b2 
 https-redirect
#
traffic behavior b3 
 deny
#  
traffic policy p1 
 classifier c1 behavior b1 precedence 2
 classifier c2 behavior b2 precedence 3
 classifier c3 behavior b3 precedence 4 
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
 domain isp1 
  authentication-scheme auth2 
  accounting-scheme acct2 
  radius-server group rd2 
 #   
 domain web_before
  authentication-scheme none
  accounting-scheme none 
  ip-pool huawei
  user-group huawei 
  web-server 192.168.8.251
  web-server url https://192.168.8.251 
  web-server mode post 
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 192.168.2.1 255.255.255.0 
# 
interface GigabitEthernet0/1/2 
 undo shutdown 
# 
interface GigabitEthernet0/1/2.1 
 user-vlan 1  
 bas 
 # 
  access-type layer2-subscriber default-domain pre-authentication web_before authentication isp1 
  authentication-method web 
 #
#
interface LoopBack0                                                           
 ip address 192.168.8.1 255.255.255.0
# 
web-auth-server enable 
web-auth-server source interface LoopBack0  
web-auth-server 192.168.8.251 port 50100 key cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%# 
# 
traffic-policy p1 inbound 
# 
undo web-auth-server source-ip all 
web-auth-server source-ip 192.168.8.1 
# 
undo web-auth-server source-ipv6 all 
# 
return 
```