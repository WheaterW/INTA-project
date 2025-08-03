Example for Configuring HTTP Redirect for Layer 2 IPoE Users Access with Dual Portal Servers and Dual RADIUS Servers Deployed
=============================================================================================================================

This section provides an example for configuring HTTP redirect for Layer 2 IPoE user access with dual portal servers and dual RADIUS servers deployed.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0202550852__fig1733344912107), the Layer 2 IPoE user belongs to the **isp1** domain, and web authentication based on HTTP redirect is used. RADIUS authentication and accounting are implemented to allow the user to access the network in Layer 2 IPoE mode through GE 0/1/2 of DeviceA. Configure the two portal&web servers to work in master/backup mode to implement redundant backup. Configure the two RADIUS servers to work in master/backup and load-sharing modes. This allows both RADIUS servers to authenticate users and improves the user access performance. After the configurations are complete, ensure that the user can access the network after the user enters the correct username and password on the web authentication page and passes the authentication.

**Figure 1** Configuring redirection of Layer 2 IPoE access users from HTTP pages to the web authentication page on a network with dual portal servers and dual RADIUS servers deployed![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example represent GE 0/1/2.1 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0214972052.png)

#### Configuration Roadmap

1. Configure a user group.
2. Configure an address pool.
3. Configure authentication and accounting schemes.
4. Configure a RADIUS server group.
5. Configure web pre-authentication and authentication domains.
6. Configure a loopback interface.
7. Configure the master and backup web authentication servers.
8. Configure ACL rules and a traffic policy.
9. Configure a BAS interface and an upstream interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP addresses and port numbers of the RADIUS authentication and accounting servers
* IP address pool name, gateway address, and DNS server address
* Domain names
* IP addresses of the master and backup portal and web servers In this example, the master web server and master portal server are deployed on the same device, and their backup servers are also deployed on the same device.

* BAS interface parameters

#### Procedure

1. Configure a user group.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] user-group huawei
   ```
2. Configure a local address pool on DeviceA.
   ```
   [~DeviceA] ip pool huawei bas local
   [*DeviceA-ip-pool-huawei] gateway 10.10.10.1 24
   [*DeviceA-ip-pool-huawei] commit
   [~DeviceA-ip-pool-huawei] section 0 10.10.10.2 10.10.10.200
   [~DeviceA-ip-pool-huawei] quit
   ```
3. Configure AAA schemes.
   
   # Configure an authentication scheme.
   
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
   
   # Configure an accounting scheme.
   
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
4. Configure a RADIUS server group and bind the two RADIUS servers to the group to implement redundancy backup and load balancing.
   ```
   [~DeviceA] radius-server group rd2
   [*DeviceA-radius-rd2] radius-server authentication 192.168.2.2 1812
   [*DeviceA-radius-rd2] radius-server authentication 192.168.2.3 1812
   [*DeviceA-radius-rd2] radius-server accounting 192.168.2.2 1813
   [*DeviceA-radius-rd2] radius-server accounting 192.168.2.3 1813
   [*DeviceA-radius-rd2] radius-server shared-key Huawei
   [*DeviceA-radius-rd2] radius-server algorithm loading-share
   [*DeviceA-radius-rd2] commit
   [~DeviceA-radius-rd2] quit
   ```
5. Configure domains and HTTP redirect.
   
   # Configure a web pre-authentication domain named **web\_before**. Bind the two web servers to the domain to implement redundancy backup.
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] domain web_before
   [*DeviceA-aaa-domain-web_before] authentication-scheme none
   [*DeviceA-aaa-domain-web_before] accounting-scheme none
   [*DeviceA-aaa-domain-web_before] commit
   [~DeviceA-aaa-domain-web_before] user-group huawei
   [~DeviceA-aaa-domain-web_before] dns primary-ip 192.168.2.254
   [*DeviceA-aaa-domain-web_before] commit
   [~DeviceA-aaa-domain-web_before] web-server 192.168.2.4
   [~DeviceA-aaa-domain-web_before] web-server 192.168.2.5 slave
   [~DeviceA-aaa-domain-web_before] web-server url http://192.168.2.4/portal.html 
   [~DeviceA-aaa-domain-web_before] web-server url http://192.168.2.5/portal.html slave
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
6. Configure a loopback interface.
   ```
   [~DeviceA] interface Loopback 0
   [*DeviceA-LoopBack0] ip address 192.168.2.1 32
   [*DeviceA-LoopBack0] commit
   [~DeviceA-LoopBack0] quit
   ```
7. Configure a web authentication server. That is, configure the portal authentication server.
   ```
   [~DeviceA] web-auth-server enable
   [~DeviceA] web-auth-server source interface LoopBack0
   [~DeviceA] web-auth-server source-ip 192.168.2.1
   [~DeviceA] web-auth-server 192.168.2.4 key cipher Huawei
   [~DeviceA] web-auth-server 192.168.2.5 key cipher Huawei
   ```
8. Configure a traffic policy.
   1. Configure ACLs.
      
      # Configure an ACL numbered 6000 to permit the traffic originating from the user group **huawei** to the web server and DNS server.
      
      ```
      [~DeviceA] acl 6000
      [*DeviceA-acl-ucl-6000] rule 5 permit ip source user-group huawei destination ip-address 192.168.2.4 0
      [*DeviceA-acl-ucl-6000] rule 10 permit ip source user-group huawei destination ip-address 192.168.2.5 0
      [*DeviceA-acl-ucl-6000] rule 15 permit ip source user-group huawei destination ip-address 192.168.2.254 0
      [*DeviceA-acl-ucl-6000] commit
      [~DeviceA-acl-ucl-6000] quit
      ```
      
      # Configure an ACL numbered 6001 to allow HTTP redirect for the TCP packets originating from the user group **huawei** and whose destination port information is www.
      
      ```
      [~DeviceA] acl 6001
      [*DeviceA-acl-ucl-6001] rule 5 permit tcp destination-port eq www source user-group huawei
      [*DeviceA-acl-ucl-6001] commit
      [~DeviceA-acl-ucl-6001] quit
      ```
      
      # Configure an ACL numbered 6002 to deny the traffic originating from the user group **huawei**.
      
      ```
      [~DeviceA] acl 6002
      [*DeviceA-acl-ucl-6002] rule 5 permit ip source user-group huawei
      [*DeviceA-acl-ucl-6002] commit
      [~DeviceA-acl-ucl-6002] quit
      ```
   2. Configure traffic classifiers.
      
      # Configure a traffic classifier named **c1** and apply ACL 6000 to the classifier.
      
      ```
      [~DeviceA] traffic classifier c1
      [*DeviceA-classifier-c1] if-match acl 6000
      [*DeviceA-classifier-c1] commit
      [~DeviceA-classifier-c1] quit
      ```
      
      # Configure a traffic classifier named **c2** and apply ACL 6001 to the classifier.
      
      ```
      [~DeviceA] traffic classifier c2
      [*DeviceA-classifier-c2] if-match acl 6001
      [*DeviceA-classifier-c2] commit
      [~DeviceA-classifier-c2] quit
      ```
      # Configure a traffic classifier named **c3** and apply ACL 6002 to the classifier.
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
      [*DeviceA-behavior-b2] http-redirect
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
      ```
9. Configure interfaces.
   
   # Configure a BAS interface.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/2.1
   [*DeviceA-GigabitEthernet0/1/2.1] user-vlan 1
   [*DeviceA-GigabitEthernet0/1/2.1-vlan-1-1] commit
   [~DeviceA-GigabitEthernet0/1/2.1-vlan-1-1] quit
   [~DeviceA-GigabitEthernet0/1/2.1] bas 
   [~DeviceA-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain pre-authentication web_before authentication isp1
   [*DeviceA-GigabitEthernet0/1/2.1-bas] authentication-method web
   [*DeviceA-GigabitEthernet0/1/2.1-bas] commit
   [~DeviceA-GigabitEthernet0/1/2.1-bas] quit
   [~DeviceA-GigabitEthernet0/1/2.1] quit
   ```
   
   # Configure an upstream interface connecting the BRAS to the Internet.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/1
   [~DeviceA-GigabitEthernet0/1/1] ip address 192.168.3.1 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/1] commit
   [~DeviceA-GigabitEthernet0/1/1] quit
   [~DeviceA] quit
   ```
10. Verify the configuration.
    
    After completing the configurations, have the user go online. Then, run the **display access-user domain** command to check information about the user in the domain. The command output shows that the user has gone online successfully.
    
    ```
    <DeviceA> display access-user domain web_before
      ------------------------------------------------------------------------------
      UserID  Username             Interface         IP address       MAC
              Vlan                 IPv6 address      Access type
      ------------------------------------------------------------------------------
      20      user1@web_before     GE0/1/2.1         10.10.10.200     00e0-fc12-3456
              1/-                  -                 IPOE 
      ------------------------------------------------------------------------------
    ```
    
    Normally, after the user opens a browser on the PC and enters an HTTP address in the address bar, a web authentication page is displayed. The user then enters the username and password. If the user is authenticated, it can enter the post-authentication domain.
    
    ```
    <DeviceA> display access-user domain isp1
      ------------------------------------------------------------------------------
      UserID  Username             Interface         IP address       MAC
              Vlan                 IPv6 address      Access type
      ------------------------------------------------------------------------------
      20      user1@isp1           GE0/1/2.1         10.10.10.200     00e0-fc12-3456
              1/-                  -                 IPOE 
      ------------------------------------------------------------------------------
    ```

#### Configuration Files

```
#
sysname DeviceA
#
radius-server group rd2
 radius-server shared-key-cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%# 
 radius-server authentication 192.168.2.2 1812 weight 0
 radius-server authentication 192.168.2.3 1812 weight 0
 radius-server accounting 192.168.2.2 1813 weight 0
 radius-server accounting 192.168.2.3 1813 weight 0
 radius-server algorithm loading-share      
#
ip pool huawei bas local
 gateway 10.10.10.1 255.255.255.0
 section 0 10.10.10.2 10.10.10.200 
#
user-group huawei
#
acl number 6000
 rule 5 permit ip source user-group huawei destination ip-address 192.168.2.4 0
 rule 10 permit ip source user-group huawei destination ip-address 192.168.2.5 0
 rule 15 permit ip source user-group huawei destination ip-address 192.168.2.254 0
#
acl number 6001
 rule 5 permit tcp source user-group huawei destination-port eq www 
#
acl number 6002
 rule 5 permit ip source user-group huawei 
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
 http-redirect
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
  dns primary-ip 192.168.2.254
  user-group huawei
  web-server 192.168.2.4
  web-server 192.168.2.5 slave
  web-server url http://192.168.2.4/portal.html  
  web-server url http://192.168.2.5/portal.html slave
#
interface GigabitEthernet0/1/1
 ip address 192.168.3.1 255.255.255.0
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
 ip address 192.168.2.1 255.255.255.255
#
web-auth-server enable
web-auth-server source interface LoopBack0 
web-auth-server 192.168.2.4 port 50100 key cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
web-auth-server 192.168.2.5 port 50100 key cipher %^%#Nc67(,q}Y3l).<Ny>huLjy&GBFKkF6''OlL^yW|H%^%#
#
undo web-auth-server source-ip all
web-auth-server source-ip 192.168.2.1
#
undo web-auth-server source-ipv6 all
#
traffic-policy p1 inbound
#
return
```