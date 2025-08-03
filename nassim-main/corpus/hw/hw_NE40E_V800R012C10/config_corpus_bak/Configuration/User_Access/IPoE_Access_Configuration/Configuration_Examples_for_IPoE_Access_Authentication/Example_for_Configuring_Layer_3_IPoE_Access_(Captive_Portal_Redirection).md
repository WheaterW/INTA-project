Example for Configuring Layer 3 IPoE Access (Captive Portal Redirection)
========================================================================

This section provides an example for configuring Layer 3 IPoE access with captive portal redirection. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374009__fig_dc_ne_ipox_cfg_014801), the networking requirements are as follows:

* A user belongs to the domain **isp2** and connects to GE 0/1/2.1 on DeviceB through DeviceA, a DHCP relay agent. The user then accesses the Internet in Layer 3 IPoE access mode.
* The user adopts web authentication, with the authentication scheme and accounting scheme set to RADIUS authentication and RADIUS accounting, respectively.
* The IP address of the RADIUS server is 192.168.8.249, and the authentication and accounting port numbers are 1812 and 1813, respectively. The standard RADIUS protocol is adopted, and the key is **it-is-my-secret1**.
* The IP address of the DNS server is 192.168.8.252.
* A device has all the web server, web authentication server, and portal server functionalities, with the portal server address 192.168.8.251.
* To improve the success rate for captive portal redirection, configure flow-based captive portal redirection to allow users accessing a specified web page at 4.4.4.4 to be redirected to the portal redirection page.

**Figure 1** Configuring Layer 3 IPoE access (captive portal redirection)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 5 in this example represent GE 0/1/1, GE 0/1/2, GE 0/1/1.1, GE 0/1/2.1, and GE 0/1/3, respectively.


  
![](images/fig_dc_ne_ipox_cfg_014801.png)

#### Configuration Roadmap

The configuration roadmap is as follows (all functions, except DHCP relay, are configured on DeviceB):

1. Configure DHCP relay on DeviceA.
2. Configure authentication and accounting schemes.
3. Configure a RADIUS server group.
4. Configure a user password.
5. Configure an IP address pool.
6. Configure web pre-authentication and authentication domains.
7. Configure a web authentication server.
8. Configure a portal server.
9. Configure a portal service policy.
10. Configure UCL rules and a traffic policy.
11. Configure a BAS interface and an upstream interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP address and port numbers of the RADIUS authentication and accounting server
* Address pool name, gateway address, and DNS server address
* Domain names
* Portal service policy name
* Portal server address
* UCL rules
* Traffic policy name
* BAS interface parameters

#### Procedure

1. Assign IP addresses to interfaces on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface GigabitEthernet0/1/2
   [~DeviceA-GigabitEthernet0/1/2] ip address 11.11.11.1 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/2] commit
   [~DeviceA-GigabitEthernet0/1/2] quit
   [*DeviceA] interface GigabitEthernet0/1/1.1
   [*DeviceA-GigabitEthernet0/1/1.1] ip address 192.168.1.2 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/1.1] vlan-type dot1q 1
   [*DeviceA-GigabitEthernet0/1/1.1] commit
   [~DeviceA-GigabitEthernet0/1/1.1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface GigabitEthernet0/1/2.1
   [*DeviceB-GigabitEthernet0/1/2.1] ip address 192.168.1.1 255.255.255.0
   [*DeviceB-GigabitEthernet0/1/2.1] vlan-type dot1q 1
   [*DeviceB-GigabitEthernet0/1/2.1] commit
   [~DeviceB-GigabitEthernet0/1/2.1] quit
   ```
2. Configure DHCP relay on DeviceA.
   
   
   ```
   [~DeviceA] interface GigabitEthernet0/1/2
   [*DeviceA-GigabitEthernet0/1/2] dhcp select relay
   [*DeviceA-GigabitEthernet0/1/2] ip relay address 192.168.1.1
   [*DeviceA-GigabitEthernet0/1/2] commit
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
3. Configure a network-side IP address pool on DeviceB. The gateway address of the IP address pool must be on the same network segment as the IP address of the inbound interface on DeviceA, the DHCP relay agent.
   
   
   ```
   [~DeviceB] ip pool huawei bas local
   [*DeviceB-ip-pool-huawei] gateway 11.11.11.1 24
   [*DeviceB-ip-pool-huawei] commit
   [~DeviceB-ip-pool-huawei] section 0 11.11.11.2 11.11.11.255
   [~DeviceB-ip-pool-huawei] dns-server 192.168.8.252
   [*DeviceB-ip-pool-huawei] commit
   [~DeviceB-ip-pool-huawei] quit
   ```
4. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   [~DeviceB] aaa
   ```
   ```
   [~DeviceB-aaa] authentication-scheme auth2
   ```
   ```
   [*DeviceB-aaa-authen-auth2] authentication-mode radius
   ```
   ```
   [*DeviceB-aaa-authen-auth2] commit
   ```
   ```
   [~DeviceB-aaa-authen-auth2] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~DeviceB-aaa] accounting-scheme acct2
   ```
   ```
   [*DeviceB-aaa-accounting-acct2] accounting-mode radius
   ```
   ```
   [*DeviceB-aaa-accounting-acct2] commit
   ```
   ```
   [~DeviceB-aaa-accounting-acct2] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
5. Configure a RADIUS server group.
   
   
   ```
   [~DeviceB] radius-server group rd2
   ```
   ```
   [*DeviceB-radius-rd2] radius-server authentication 192.168.8.249 1812
   ```
   ```
   [*DeviceB-radius-rd2] radius-server accounting 192.168.8.249 1813
   ```
   ```
   [*DeviceB-radius-rd2] commit
   ```
   ```
   [~DeviceB-radius-rd2] radius-server type standard
   ```
   ```
   [~DeviceB-radius-rd2] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*DeviceB-radius-rd2] commit
   ```
   ```
   [~DeviceB-radius-rd2] quit
   ```
6. Configure domains.
   
   
   
   # Configure a domain named **default0** as the pre-authentication domain for web authentication.
   
   ```
   [~DeviceB] user-group huawei
   ```
   ```
   [~DeviceB] aaa
   ```
   ```
   [~DeviceB-aaa] domain default0
   ```
   ```
   [~DeviceB-aaa-domain-default0] user-group huawei
   ```
   ```
   [*DeviceB-aaa-domain-default0] web-server 192.168.8.251
   ```
   ```
   [*DeviceB-aaa-domain-default0] web-server url http://192.168.8.251
   ```
   ```
   [*DeviceB-aaa-domain-default0] commit
   ```
   ```
   [~DeviceB-aaa-domain-default0] ip-pool huawei
   ```
   ```
   [~DeviceB-aaa-domain-default0] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
   
   # Configure a portal service policy.
   
   ```
   [~DeviceB] service-group portal-group
   ```
   ```
   [*DeviceB] service-policy name portal-policy portal
   ```
   ```
   [*DeviceB-service-policy-portal-policy] service-group portal-group
   ```
   ```
   [*DeviceB-service-policy-portal-policy] commit
   ```
   ```
   [~DeviceB-service-policy-portal-policy] quit
   ```
   
   # Configure an authentication domain named **isp2**, and bind the portal service policy to the domain.
   
   ```
   [~DeviceB] aaa
   ```
   ```
   [~DeviceB-aaa] domain isp2
   ```
   ```
   [*DeviceB-aaa-domain-isp2] authentication-scheme auth2
   ```
   ```
   [*DeviceB-aaa-domain-isp2] accounting-scheme acct2
   ```
   ```
   [*DeviceB-aaa-domain-isp2] radius-server group rd2
   ```
   ```
   [*DeviceB-aaa-domain-isp2] commit
   ```
   ```
   [~DeviceB-aaa-domain-isp2] portal-server 192.168.8.251
   ```
   ```
   [~DeviceB-aaa-domain-isp2] portal-server url http://192.168.8.251/portal/admin/
   ```
   ```
   [~DeviceB-aaa-domain-isp2] service-policy portal-policy
   ```
   ```
   [~DeviceB-aaa-domain-isp2] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
7. Configure an IP address used by DeviceB to receive portal packets from the web authentication server.
   
   
   ```
   [~DeviceB] interface Loopback 0
   ```
   ```
   [*DeviceB-LoopBack0] ip address 10.6.55.1 32
   ```
   ```
   [*DeviceB-LoopBack0] quit
   ```
   ```
   [*DeviceB-LoopBack0] commit
   ```
   ```
   [~DeviceB] web-auth-server source-ip 10.6.55.1
   ```
8. Configure a web authentication server.
   
   
   ```
   [~DeviceB] web-auth-server enable
   ```
   ```
   [~DeviceB] web-auth-server source interface LoopBack 0
   ```
   ```
   [~DeviceB] web-auth-server 192.168.8.251
   ```
9. Configure UCLs.
   
   
   
   # Configure UCL rules that allow pre-authentication domain users to be redirected to the web authentication page. Rules in UCL 6000 define the IP addresses of web pages that pre-authentication users are allowed to access.
   
   ```
   [~DeviceB] acl 6000
   [*DeviceB-acl-ucl-6000] rule 10 permit ip source user-group huawei destination ip-address 127.0.0.1 0
   [*DeviceB-acl-ucl-6000] rule 15 permit ip source ip-address 127.0.0.1 0  destination user-group huawei
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The preceding UCL rules involving 127.0.0.1 serve as an example for permitting users in the pre-authentication domain to access specified websites. After the UCL rules are configured, user packets sent to the CPU of DeviceB can pass through and users in the pre-authentication domain can access 127.0.0.1.
   
   ```
   [*DeviceB-acl-ucl-6000] rule 20 permit ip source user-group huawei destination ip-address 192.168.8.252 0
   [*DeviceB-acl-ucl-6000] rule 25 permit ip source ip-address 192.168.8.252 0  destination user-group huawei
   [*DeviceB-acl-ucl-6000] rule 30 permit ip source user-group huawei destination ip-address 192.168.8.249 0
   [*DeviceB-acl-ucl-6000] rule 35 permit ip source ip-address 192.168.8.249 0  destination user-group huawei
   [*DeviceB-acl-ucl-6000] rule 40 permit ip source user-group huawei destination ip-address 192.168.8.251 0
   [*DeviceB-acl-ucl-6000] rule 45 permit ip source ip-address 192.168.8.251 0  destination user-group huawei
   [*DeviceB-acl-ucl-6000] commit
   [~DeviceB-acl-ucl-6000] quit
   [~DeviceB] acl 6001
   [*DeviceB-acl-ucl-6001] rule 10 permit tcp source user-group huawei destination-port eq www
   [*DeviceB-acl-ucl-6001] rule 15 permit tcp source user-group huawei destination-port eq 8080
   [*DeviceB-acl-ucl-6001] rule 20 permit ip source user-group huawei
   [*DeviceB-acl-ucl-6001] commit
   [~DeviceB-acl-ucl-6001] quit
   ```
   
   # Configure UCL rules that allow authentication users to be redirected to the portal server when these users access a specified web page at 4.4.4.4.
   
   ```
   [~DeviceB] acl 7000
   ```
   ```
   [*DeviceB-acl-ucl-7000] rule 5 permit tcp source service-group portal-group destination ip-address 4.4.4.4 0 destination-port eq www
   ```
   ```
   [*DeviceB-acl-ucl-7000] rule 10 permit tcp source service-group portal-group destination ip-address 4.4.4.4 0 destination-port eq 8080
   ```
   ```
   [*DeviceB-acl-ucl-7000] commit
   ```
   ```
   [~DeviceB-acl-ucl-7000] quit
   ```
   
   # Configure a traffic policy.
   
   ```
   [~DeviceB] traffic classifier web_permit
   [*DeviceB-classifier-web_permit] if-match acl 6000
   [*DeviceB-classifier-web_permit] commit
   [~DeviceB-classifier-web_permit] quit
   [~DeviceB] traffic behavior web_permit
   [*DeviceB-behavior-web_permit] permit
   [*DeviceB-behavior-web_permit] commit
   [~DeviceB-behavior-web_permit] quit
   [~DeviceB] traffic classifier web_deny
   [*DeviceB-classifier-web_deny] if-match acl 6001
   [*DeviceB-classifier-web_deny] commit
   [~DeviceB-classifier-web_deny] quit
   [~DeviceB] traffic behavior web_deny
   [*DeviceB-behavior-web_deny] http-redirect
   [*DeviceB-behavior-web_deny] commit
   [~DeviceB-behavior-web_deny] quit
   [~DeviceB] traffic classifier portal
   [*DeviceB-classifier-portal] if-match acl 7000
   [*DeviceB-classifier-portal] commit
   [~DeviceB-classifier-portal] quit
   [~DeviceB] traffic behavior portal
   [*DeviceB-behavior-portal] redirect-cpu portal
   [*DeviceB-behavior-portal] commit
   [~DeviceB-behavior-portal] quit
   [~DeviceB] traffic policy l3-ipoe
   [*DeviceB-trafficpolicy-l3-ipoe] classifier portal behavior portal
   [*DeviceB-trafficpolicy-l3-ipoe] classifier web_permit behavior web_permit
   [*DeviceB-trafficpolicy-l3-ipoe] classifier web_deny behavior web_deny
   [*DeviceB-trafficpolicy-l3-ipoe] commit
   [~DeviceB-trafficpolicy-l3-ipoe] quit
   ```
   
   # Apply the user-side traffic policy globally.
   
   ```
   [~DeviceB] traffic-policy l3-ipoe inbound
   [~DeviceB] traffic-policy l3-ipoe outbound
   ```
10. Configure interfaces.
    
    
    
    # Configure a BAS interface.
    
    ```
    [~DeviceB] interface GigabitEthernet 0/1/2.1
    [~DeviceB-GigabitEthernet0/1/2.1] bas
    [~DeviceB-GigabitEthernet0/1/2.1-bas] access-type layer3-subscriber default-domain pre-authentication default0 authentication isp2
    [*DeviceB-GigabitEthernet0/1/2.1-bas] commit
    [~DeviceB-GigabitEthernet0/1/2.1-bas] quit
    [~DeviceB-GigabitEthernet0/1/2.1] quit
    ```
    
    # Configure an upstream interface.
    
    ```
    [~DeviceB] interface GigabitEthernet 0/1/1
    ```
    ```
    [*DeviceB-GigabitEthernet0/1/1] ip address 192.168.2.1 255.255.255.0
    ```
    ```
    [*DeviceB-GigabitEthernet0/1/1] commit
    ```
    ```
    [~DeviceB-GigabitEthernet0/1/1] quit
    ```

#### Configuration Files

* DeviceA configuration file
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 1
   ip address 192.168.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 11.11.11.1 255.255.255.0
   dhcp select relay
   ip relay address 192.168.1.1
  #
  return
  ```
* DeviceB configuration file
  ```
  #
  sysname DeviceB
  #
  radius-server group rd2
   radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#  
   radius-server authentication 192.168.8.249 1812 weight 0
   radius-server accounting 192.168.8.249 1813 weight 0     
  #
  ip pool huawei bas local
   gateway 11.11.11.1 255.255.255.0
   section 0 11.11.11.2 11.11.11.255 
   dns-server 192.168.8.252
  #
  user-group huawei
  #
  acl number 6000
   rule 10 permit ip source user-group huawei destination ip-address 127.0.0.1 0 
   rule 15 permit ip source ip-address 127.0.0.1 0  destination user-group huawei
   rule 20 permit ip source user-group huawei destination ip-address 192.168.8.252 0
   rule 25 permit ip source ip-address 192.168.8.252 0  destination user-group huawei
   rule 30 permit ip source user-group huawei destination ip-address 192.168.8.249 0
   rule 35 permit ip source ip-address 192.168.8.249 0  destination user-group huawei
   rule 40 permit ip source user-group huawei destination ip-address 192.168.8.251 0
   rule 45 permit ip source ip-address 192.168.8.251 0  destination user-group huawei
  #
  acl number 6001
   rule 10 permit tcp source user-group huawei destination-port eq www
   rule 15 permit tcp source user-group huawei destination-port eq 8080
   rule 20 permit ip source user-group huawei
  #
  acl number 7000                                                               
   rule 5 permit tcp source service-group portal-group destination ip-address 4.4.4.4 0 destination-port eq www
   rule 10 permit tcp source service-group portal-group destination ip-address 4.4.4.4 0 destination-port eq 8080
  #
  traffic classifier portal operator or
   if-match acl 7000 precedence 3
  #
  traffic classifier web_deny operator or
   if-match acl 6001 precedence 2
  #
  traffic classifier web_permit operator or
   if-match acl 6000 precedence 1
  #
  traffic behavior portal
   redirect-cpu portal
  #
  traffic behavior web_deny
   http-redirect
  #
  traffic behavior web_permit
  #
  traffic policy l3-ipoe
   share-mode
   classifier portal behavior portal precedence 1
   classifier web_permit behavior web_permit precedence 2
   classifier web_deny behavior web_deny precedence 3
  #
  aaa
   #  
   authentication-scheme auth2
   #
    accounting-scheme acct2 
   #  
   domain default0
    ip-pool huawei
    user-group huawei
    web-server 192.168.8.251
    web-server url http://192.168.8.251
   #
   domain isp2
    authentication-scheme auth2
    accounting-scheme acct2
    radius-server group rd2
    portal-server 192.168.8.251
    portal-server url http://192.168.8.251/portal/admin/
    service-policy portal-policy
  #
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1
   vlan-type dot1q 1
   ip address 192.168.1.1 255.255.255.0
   bas
   #
    access-type layer3-subscriber default-domain pre-authentication default0 authentication isp2
  #
  interface LoopBack0
   ip address 10.6.55.1 255.255.255.255
  #
  web-auth-server enable
  web-auth-server source interface LoopBack 0
  web-auth-server 192.168.8.251
  #
   undo web-auth-server source-ip all
   web-auth-server source-ip 10.6.55.1
  #
   undo web-auth-server source-ipv6 all
  #
   traffic-policy l3-ipoe inbound
   traffic-policy l3-ipoe outbound
  #
  return
  ```