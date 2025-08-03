Example for Configuring DNS Redirect for Web Authentication of Layer 2 IPoE Users
=================================================================================

This section provides an example for configuring DNS redirect for web authentication of Layer 2 IPoE users. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374069__fig_dc_ne_cfg_01444801), web authentication is performed for the user in the domain **isp1**. DNS redirect, RADIUS authentication scheme, and RADIUS accounting scheme are configured. The user accesses the Internet in Layer 2 IPoE access mode through GE 0/1/2 of DeviceA.

**Figure 1** Configuring DNS redirect for web authentication of Layer 2 IPoE users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and interface2 in this example represent GE 0/1/2.1 and GE 0/1/1, respectively.


  
![](images/fig_dc_ne_cfg_014455.png)

#### Configuration Roadmap

The configuration roadmap is as follows: (All the configurations are performed on DeviceA.)

1. Configure a user group.
2. Configure an address pool.
3. Configure authentication and accounting schemes.
4. Configure a RADIUS server group.
5. Configure web pre-authentication and authentication domains.
6. Configure a web authentication server.
7. Configure ACL rules and a traffic policy.
8. Configure whitelists.
9. Configure a BAS interface and an upstream interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, RADIUS authentication server's IP address and port number, and RADIUS accounting server's IP address and port number
* Address pool name, gateway address, and DNS server address
* Domain names
* Address of the web server and web authentication server (in this example, the two servers are deployed on the same device that supports DNS)
* ACL rules
* Traffic policies
* Whitelist configuration
* BAS interface parameters

#### Procedure

1. Configure a user group.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] user-group huawei
   ```
2. Configure a local address pool on the Device.
   
   
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
   [*DeviceA-aaa] authentication-scheme auth2
   [*DeviceA-aaa-authen-auth2] authentication-mode radius
   [*DeviceA-aaa-authen-auth2] commit
   [~DeviceA-aaa-authen-auth2] quit
   [~DeviceA-aaa] authentication-scheme none
   [*DeviceA-aaa-authen-none] authentication-mode none
   [*DeviceA-aaa-authen-none] commit
   [~DeviceA-aaa-authen-none] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In insecure network environments, you are advised to use a secure authentication mode. For details, see [Example for Configuring Layer 3 IPoE Access (Web Authentication)](dc_ne_ipox_cfg_0148.html).
   
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
4. Configure a RADIUS server group.
   
   
   ```
   [~DeviceA] radius-server group rd2
   [*DeviceA-radius-rd2] radius-server authentication 192.168.8.249 1812
   [*DeviceA-radius-rd2] radius-server accounting 192.168.8.249 1813
   [*DeviceA-radius-rd2] radius-server shared-key Huawei
   [*DeviceA-radius-rd2] commit
   [~DeviceA-radius-rd2] quit
   ```
5. Configure domains and DNS redirect.
   
   
   
   # Configure a web pre-authentication domain named **web\_before**. Then, configure DNS redirect.
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] domain web_before
   [*DeviceA-aaa-domain-web_before] authentication-scheme none
   [*DeviceA-aaa-domain-web_before] accounting-scheme none
   [*DeviceA-aaa-domain-web_before] commit
   [~DeviceA-aaa-domain-web_before] user-group huawei
   [~DeviceA-aaa-domain-web_before] dns primary-ip 1.1.1.1
   [*DeviceA-aaa-domain-web_before] dns-redirect web-server 192.168.8.251
   [*DeviceA-aaa-domain-web_before] commit
   [~DeviceA-aaa-domain-web_before] ip-pool huawei
   [~DeviceA-aaa-domain-web_before] quit
   ```
   
   # Configure a web authentication domain named **isp1**.
   
   ```
   [~DeviceA-aaa] domain isp1
   [*DeviceA-aaa-domain-isp1] authentication-scheme auth2
   [*DeviceA-aaa-domain-isp1] accounting-scheme acct2
   [*DeviceA-aaa-domain-isp1] commit
   [~DeviceA-aaa-domain-isp1] radius-server group rd2
   [*DeviceA-aaa-domain-isp1] commit
   [~DeviceA-aaa-domain-isp1] quit
   [~DeviceA-aaa] quit
   ```
6. Configure a loopback interface.
   
   
   ```
   [~DeviceA] interface LoopBack 0
   [*DeviceA-LoopBack0] ip address 192.168.8.1 32 
   [*DeviceA-LoopBack0] commit
   [~DeviceA-LoopBack0] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The loopback interface must be routable to the DNS server.
7. Configure a web authentication server.
   
   
   ```
   [~DeviceA] web-auth-server enable
   ```
   ```
   [~DeviceA] web-auth-server source interface LoopBack0
   ```
   ```
   [~DeviceA] web-auth-server source-ip 192.168.8.1
   ```
   ```
   [~DeviceA] web-auth-server 192.168.8.251 key cipher Huawei
   ```
8. Configure traffic policies.
   1. Configure ACLs.
      
      
      
      # Configure an ACL numbered 6000.
      
      ```
      [~DeviceA] acl 6000
      [*DeviceA-acl-ucl-6000] rule 5 permit ip source user-group huawei destination ip-address 1.1.1.1 0
      [*DeviceA-acl-ucl-6000] rule 15 permit ip source user-group huawei destination ip-address 192.168.8.251 0
      [*DeviceA-acl-ucl-6000] commit
      [~DeviceA-acl-ucl-6000] quit
      ```
      
      # Configure an ACL numbered 6001.
      
      ```
      [~DeviceA] acl 6001
      [*DeviceA-acl-ucl-6001] rule 5 permit ip source user-group huawei
      [*DeviceA-acl-ucl-6001] commit
      [~DeviceA-acl-ucl-6001] quit
      ```
      
      # Configure an ACL numbered 6002.
      
      ```
      [~DeviceA] acl 6002
      [*DeviceA-acl-ucl-6002] rule 5 permit udp source-port eq dns destination user-group huawei
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
      [*DeviceA-behavior-b2] deny
      [*DeviceA-behavior-b2] commit
      [~DeviceA-behavior-b2] quit
      ```
      
      # Configure a traffic behavior named **b3**.
      
      ```
      [~DeviceA] traffic behavior b3
      [*DeviceA-behavior-b3] dns-redirect 
      [*DeviceA-behavior-b3] commit
      [~DeviceA-behavior-b3] quit
      ```
   4. Configure traffic policies.
      
      
      
      # Configure a traffic policy named **p1**.
      
      ```
      [~DeviceA] traffic policy p1
      [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
      [*DeviceA-trafficpolicy-p1] classifier c2 behavior b2
      [*DeviceA-trafficpolicy-p1] commit
      [~DeviceA-trafficpolicy-p1] quit
      ```
      
      # Configure a traffic policy named **p2**.
      
      ```
      [~DeviceA] traffic policy p2
      [*DeviceA-trafficpolicy-p2] classifier c3 behavior b3
      [*DeviceA-trafficpolicy-p2] commit
      [~DeviceA-trafficpolicy-p2] quit
      ```
   5. Apply the traffic policies.
      
      
      ```
      [~DeviceA] traffic-policy p1 inbound
      [~DeviceA] traffic-policy p2 outbound
      ```
9. Configure whitelists.
   
   
   ```
   [~DeviceA] dns-url permit www.huawei.com
   [~DeviceA] dns-url permit 192.168.2.1
   ```
10. Configure interfaces.
    
    
    
    # Configure a BAS interface.
    
    ```
    [~DeviceA] interface GigabitEthernet 0/1/2.1
    [*DeviceA-GigabitEthernet0/1/2.1] commit
    [~DeviceA-GigabitEthernet0/1/2.1] user-vlan 1
    [~DeviceA-GigabitEthernet0/1/2.1-vlan-1-1] quit
    [~DeviceA-GigabitEthernet0/1/2.1] bas 
    [~DeviceA-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain pre-authentication web_before authentication isp1
    [*DeviceA-GigabitEthernet0/1/2.1-bas] commit
    [~DeviceA-GigabitEthernet0/1/2.1-bas] authentication-method web
    [~DeviceA-GigabitEthernet0/1/2.1-bas] quit
    [~DeviceA-GigabitEthernet0/1/2.1] quit
    ```
    
    # Configure an upstream interface connecting the device to the Internet.
    
    ```
    [~DeviceA] interface GigabitEthernet 0/1/1
    [*DeviceA-GigabitEthernet0/1/1] ip address 192.168.2.1 255.255.255.0
    [*DeviceA-GigabitEthernet0/1/1] commit
    [~DeviceA-GigabitEthernet0/1/1] quit
    [~DeviceA] quit
    ```
11. Verify the configuration.
    
    
    
    After completing the configurations, have the user go online. Then, run the **display access-user domain** command to check information about the user in the domain. The command output shows that the user has gone online successfully.
    
    ```
    <DeviceA> display access-user domain web_before
    ```
    ```
    ------------------------------------------------------------------------------
      UserID  Username                Interface      IP address       MAC
              Vlan          IPv6 address             Access type
      ------------------------------------------------------------------------------
      20      user1@web_before        GE0/1/2.1      10.10.10.200    00e0-fc12-3456
              1/-           -                        IPOE 
       ------------------------------------------------------------------------------
      
    ```
    
    Normally, after the user opens a browser on the PC and enters an HTTP or HTTPS address in the address bar, a web authentication page is displayed. The user then enters the username and password. After being authenticated, the user can enter the authentication domain.
    
    ```
    <DeviceA> display access-user domain isp1
    ```
    ```
    ------------------------------------------------------------------------------
      UserID  Username                Interface      IP address       MAC
              Vlan          IPv6 address             Access type
      ------------------------------------------------------------------------------
      20      user1@isp1         GE0/1/2.1      10.10.10.200     00e0-fc12-3456
              1/-           -                        IPOE 
       ------------------------------------------------------------------------------
      
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
#
user-group huawei
#
acl number 6000
 rule 5 permit ip source user-group huawei destination ip-address 1.1.1.1 0
 rule 15 permit ip source user-group huawei destination ip-address 192.168.8.251 0
#
acl number 6001
 rule 5 permit ip source user-group huawei 
#
acl number 6002
 rule 5 permit udp source-port eq dns destination user-group huawei 
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
 deny
#
traffic behavior b3
 dns-redirect
#
traffic policy p1
 classifier c1 behavior b1 precedence 1
 classifier c2 behavior b2 precedence 2
#
traffic policy p2
 classifier c3 behavior b3 precedence 1
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
 accounting-scheme none
  accounting-mode none
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
  dns primary-ip 1.1.1.1 
  user-group huawei
  dns-redirect web-server 192.168.8.251
#
interface GigabitEthernet0/1/1
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
 ip address 192.168.8.1 255.255.255.255
#
web-auth-server enable
web-auth-server source interface LoopBack0 
web-auth-server 192.168.8.251 port 50100 key cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
#
undo web-auth-server source-ip all
web-auth-server source-ip 192.168.8.1
#
undo web-auth-server source-ipv6 all
#
dns-url permit 192.168.2.1
dns-url permit www.huawei.com
#
traffic-policy p1 inbound
traffic-policy p2 outbound
#
return
```