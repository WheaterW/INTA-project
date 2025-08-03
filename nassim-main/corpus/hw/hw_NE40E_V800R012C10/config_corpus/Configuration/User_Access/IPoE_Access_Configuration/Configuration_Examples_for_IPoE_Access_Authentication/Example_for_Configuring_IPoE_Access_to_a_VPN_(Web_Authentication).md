Example for Configuring IPoE Access to a VPN (Web Authentication)
=================================================================

This section provides an example for configuring IPoE access to a VPN by using web authentication. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374010__fig_dc_ne_ipox_cfg_008401), the networking requirements are as follows:

* A user belongs to the domain **isp2** and accesses the network through GE 0/1/2 on the Router in IPoE mode.
* The user adopts web authentication, with the authentication scheme and accounting scheme set to RADIUS authentication and RADIUS accounting, respectively.
* The IP address of the RADIUS server is 192.168.8.249, and the authentication and accounting port numbers are 1812 and 1813, respectively. The standard RADIUS protocol is adopted, and the key is **it-is-my-secret1**.
* The user is a VPN user and belongs to the VPN instance named **vpn1**.
* The IP address of the DNS server is 192.168.8.252.
* The IP address of the web server is 192.168.8.251, and the key is **webvlan**.
* The network-side interface is GE 0/1/1.

**Figure 1** Configuring IPoE access to a VPN (web authentication)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_ne_ipox_cfg_008401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VPN instance.
2. Configure authentication and accounting schemes.
3. Configure a RADIUS server group.
4. Configure a user password.
5. Configure an address pool.
6. Configure web pre-authentication and authentication domains.
7. Configure a web authentication server.
8. Configure ACL rules and a traffic policy.
9. Configure a BAS interface and an upstream interface.

#### Data Preparation

To complete the configuration, you need the following data:

* VPN instance name, RD, and VPN target
* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP address and port numbers of the RADIUS authentication and accounting server
* Address pool name, gateway address, and DNS server address
* Domain names
* Web authentication server address
* ACL rules
* Traffic policy name
* BAS interface parameters

#### Procedure

1. Configure a VPN instance.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] ip vpn-instance vpn1
   ```
   ```
   [*HUAWEI-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*HUAWEI-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 both
   ```
   ```
   [*HUAWEI-vpn-instance-vpn1-af-ipv4] commit
   ```
   ```
   [~HUAWEI-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [~HUAWEI-vpn-instance-vpn1] quit
   ```
2. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
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
   
   # Configure an accounting scheme.
   
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
3. Configure a RADIUS server group.
   
   
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
   [~HUAWEI-radius-rd2] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*HUAWEI-radius-rd2] commit
   ```
   ```
   [~HUAWEI-radius-rd2] quit
   ```
4. Configure the IPoE user password.
   
   
   ```
   [~HUAWEI] aaa
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
5. Configure an address pool.
   
   
   ```
   [~HUAWEI] ip pool pool2 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool2] gateway 10.82.1.1 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool2] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool2] section 0 10.82.1.2 10.82.1.200
   ```
   ```
   [~HUAWEI-ip-pool-pool2] dns-server 192.168.8.252
   ```
   ```
   [*HUAWEI-ip-pool-pool2] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool2] vpn-instance vpn1
   ```
   ```
   [~HUAWEI-ip-pool-pool2] quit
   ```
6. Configure domains.
   
   
   
   # Configure a domain named **default0** as the pre-authentication domain for web authentication.
   
   ```
   [~HUAWEI] user-group web-before
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain default0
   ```
   ```
   [~HUAWEI-aaa-domain-default0] ip-pool pool2
   ```
   ```
   [~HUAWEI-aaa-domain-default0] user-group web-before
   ```
   ```
   [~HUAWEI-aaa-domain-default0] web-server 192.168.8.251
   ```
   ```
   [~HUAWEI-aaa-domain-default0] web-server url http://192.168.8.251
   ```
   ```
   [~HUAWEI-aaa-domain-default0] vpn-instance vpn1
   ```
   ```
   [~HUAWEI-aaa-domain-default0] http-hostcar enable
   ```
   ```
   [~HUAWEI-aaa-domain-default0] quit
   ```
   
   # Configure the domain **isp2** as the authentication domain for web authentication.
   
   ```
   [~HUAWEI-aaa] domain isp2
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] authentication-scheme auth2
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] accounting-scheme acct2
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] radius-server group rd2
   ```
   ```
   [*HUAWEI-aaa-domain-isp2] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp2] vpn-instance vpn1
   ```
   ```
   [~HUAWEI-aaa-domain-isp2] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**reallocate-ip-address**](cmdqueryname=reallocate-ip-address) command is run to enable IP address reallocation for the web authentication domain isp2, the domain must be bound to an address pool. The function is optional. In normal circumstances, a private network address is allocated in the pre-authentication domain before authentication, and a public network address is allocated in the authentication domain after authentication. This addresses public network address shortage and increases usage of public network addresses.
   
   However, the IP address reallocation function requires the web server to comply with the Huawei proprietary protocol for address reallocation, and the client must download the plug-in through the web server.
7. Configure an IP address used by Device to receive portal packets from the web authentication server.
   
   
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
   [~HUAWEI-LoopBack0] quit
   ```
   ```
   [~HUAWEI] web-auth-server source-ip 10.6.55.1
   ```
8. Configure a web authentication server.
   
   
   ```
   [~HUAWEI] web-auth-server enable
   ```
   ```
   [~HUAWEI] web-auth-server source interface LoopBack 0
   ```
   ```
   [~HUAWEI] web-auth-server 192.168.8.251 vpn-instance vpn1 key cipher webvlan
   ```
9. Configure ACLs.
   
   
   
   # Configure ACL rules.
   
   ```
   [~HUAWEI] acl number 6000
   ```
   ```
   [*HUAWEI-acl-ucl-6000] rule 20 permit tcp source user-group web-before destination-port eq www
   ```
   ```
   [*HUAWEI-acl-ucl-6000] commit
   ```
   ```
   [~HUAWEI-acl-ucl-6000] quit
   ```
   ```
   [~HUAWEI] acl number 6001
   ```
   ```
   [*HUAWEI-acl-ucl-6001] rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
   ```
   ```
   [*HUAWEI-acl-ucl-6001] rule 10 permit ip source user-group web-before destination ip-address 192.168.8.252 0
   ```
   ```
   [*HUAWEI-acl-ucl-6001] commit
   ```
   ```
   [~HUAWEI-acl-ucl-6001] quit
   ```
   ```
   [~HUAWEI] acl number 6002
   ```
   ```
   [*HUAWEI-acl-ucl-6002] rule 30 permit ip source user-group web-before destination ip-address any 
   ```
   ```
   [*HUAWEI-acl-ucl-6002] rule 35 permit ip source ip-address any destination user-group web-before 
   ```
   ```
   [*HUAWEI-acl-ucl-6002] commit
   ```
   ```
   [~HUAWEI-acl-ucl-6002] quit
   ```
   
   # Configure a traffic policy.
   
   ```
   [~HUAWEI] traffic classifier c1
   ```
   ```
   [*HUAWEI-classifier-c1] if-match acl 6000
   ```
   ```
   [*HUAWEI-classifier-c1] commit
   ```
   ```
   [~HUAWEI-classifier-c1] quit
   ```
   ```
   [~HUAWEI] traffic classifier c2
   ```
   ```
   [*HUAWEI-classifier-c2] if-match acl 6001
   ```
   ```
   [*HUAWEI-classifier-c2] commit
   ```
   ```
   [~HUAWEI-classifier-c2] quit
   ```
   ```
   [~HUAWEI] traffic classifier c3
   ```
   ```
   [*HUAWEI-classifier-c3] if-match acl 6002
   ```
   ```
   [*HUAWEI-classifier-c3] commit
   ```
   ```
   [~HUAWEI-classifier-c3] quit
   ```
   ```
   [~HUAWEI] traffic behavior deny1
   ```
   ```
   [*HUAWEI-behavior-deny1] http-redirect plus
   ```
   ```
   [*HUAWEI-behavior-deny1] commit
   ```
   ```
   [~HUAWEI-behavior-deny1] quit
   ```
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
   [~HUAWEI] traffic behavior deny2
   ```
   ```
   [*HUAWEI-behavior-deny2] deny
   ```
   ```
   [*HUAWEI-behavior-deny2] commit
   ```
   ```
   [~HUAWEI-behavior-deny2] quit
   ```
   ```
   [~HUAWEI] traffic policy action1
   ```
   ```
   [*HUAWEI-trafficpolicy-action1] share-mode
   ```
   ```
   [*HUAWEI-trafficpolicy-action1] classifier c2 behavior perm1
   ```
   ```
   [*HUAWEI-trafficpolicy-action1] classifier c1 behavior deny1
   ```
   ```
   [*HUAWEI-trafficpolicy-action1] classifier c3 behavior deny2
   ```
   ```
   [*HUAWEI-trafficpolicy-action1] commit
   ```
   ```
   [~HUAWEI-trafficpolicy-action1] quit
   ```
   
   # Apply the traffic policy globally.
   
   ```
   [~HUAWEI] traffic-policy action1 inbound
   ```
   ```
   [~HUAWEI] traffic-policy action1 outbound
   ```
10. Configure interfaces.
    
    
    
    # Configure a BAS interface.
    
    ```
    [~HUAWEI] interface gigabitethernet0/1/2
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2] bas
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2-bas] access-type layer2-subscriber
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2-bas] authentication-method web
    [*HUAWEI-GigabitEthernet0/1/2-bas] default-domain authentication isp2
    [*HUAWEI-GigabitEthernet0/1/2-bas] commit
    [~HUAWEI-GigabitEthernet0/1/2-bas] quit
    [~HUAWEI-GigabitEthernet0/1/2] quit
    ```
    
    # Configure an upstream interface.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The upstream interface is connected to an MPLS network, and the configuration is not provided here. For details, see the chapter BGP/MPLS IP VPN of the *NE40E Configuration Guide - VPN*.
    
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1] ip address 192.168.2.1 255.255.255.0
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1] commit
    ```

#### Configuration Files

```
#
sysname HUAWEI
#
ip vpn-instance vpn1
 ipv4-family
 route-distinguisher 100:1
 apply-label per-instance
 vpn-target 100:1 export-extcommunity
 vpn-target 100:1 import-extcommunity
#
radius-server group rd2
 radius-server type standard
 radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
 radius-server authentication 192.168.8.249 1812 weight 0
 radius-server accounting 192.168.8.249 1813 weight 0
#
ip pool pool2 bas local
 vpn-instance vpn1
 gateway 10.82.1.1 255.255.255.0
 section 0 10.82.1.2 10.82.1.200
 dns-server 192.168.8.252
#
user-group web-before
#
acl number 6000
 rule 20 permit tcp source user-group web-before destination-port eq www
#
acl number 6001
 rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
 rule 10 permit ip source user-group web-before destination ip-address 192.168.8.252 0
#
acl number 6002
 rule 30 permit ip source user-group web-before destination ip-address any 
 rule 35 permit ip source ip-address any destination user-group web-before
#
traffic classifier c1 operator or 
 if-match acl 6000 precedence 1
#
traffic classifier c2 operator or
 if-match acl 6001 precedence 2
#
traffic classifier c3 operator or
 if-match acl 6002 precedence 3
#
traffic behavior deny1
 http-redirect plus
#
traffic behavior deny2
 deny
#
traffic behavior perm1
#
traffic policy action1
 share mode
 classifier c2 behavior perm1 precedence 1
 classifier c1 behavior deny1 precedence 2
 classifier c3 behavior deny2 precedence 3
#
aaa
 default-password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
 #
 authentication-scheme auth2
 #
 accounting-scheme acct2
 #
 domain default0
  ip-pool pool2
  vpn-instance vpn1
  user-group web-before
  web-server 192.168.8.251
  web-server url http://192.168.8.251
  http-hostcar enable 
 #
 domain isp2
  authentication-scheme auth2
  accounting-scheme acct2
  radius-server group rd2
  vpn-instance vpn1
# 
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 192.168.2.1 255.255.255.0
# 
interface GigabitEthernet0/1/2
 undo shutdown
 bas
 #
 access-type layer2-subscriber default-domain authentication isp2 
 authentication-method web 
#
interface LoopBack0
 ip address 10.6.55.1 255.255.255.255
web-auth-server enable
web-auth-server source interface LoopBack 0
web-auth-server 192.168.8.251 vpn-instance vpn1 port 50100 key cipher %^%#aQL6,Ua<|@sxPQK/1f'4/GBJ6,6)q>$Z^7*,!2yR%^%#
#
 undo web-auth-server source-ip all 
 web-auth-server source-ip 10.6.55.1
#
 undo web-auth-server source-ipv6 all
#
 traffic-policy action1 inbound
 traffic-policy action1 outbound
#
return
```