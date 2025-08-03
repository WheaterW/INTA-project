Example for Configuring PPPoE Dual-Stack User Access (ND+PD) in Scenarios Where the RADIUS Quota Is Exhausted
=============================================================================================================

This section provides an example for configuring PPPPoE dual-stack user access in ND+PD mode in scenarios where the RADIUS quota is exhausted. When a PPPoE dual-stack user connects to a BRAS, the BRAS implements RADIUS authentication and accounting. The BRAS also assigns an IPv4 address to the user from the local address pool, an IPv6 prefix to the CPE through DHCPv6 IA\_PD, and an IPv6 address to the CPE through DHCPv6 ND. This allows the user to access the network. After the quota delivered by the RADIUS server is exhausted, the PPPoE dual-stack user is switched to a redirect domain in which user access is controlled. If the PPPoE dual-stack user is visiting an unauthorized address, it will be forcibly redirected to a payment page.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0245960423__fig_dc_ne_ipox_cfg_007201), a PPPoE user belongs to the **huawei** domain and uses the dual-stack access mode. DeviceA implements RADIUS authentication and accounting, as well as assigns an IPv4 address to the user from the local address pool and an IPv6 address to the user through DHCPv6 ND. The user can then access the network through interface 2 on DeviceA. After the PPPoE dual-stack user goes online, the RADIUS server delivers a quota. After the quota is exhausted, the user is switched to a redirect domain in which user access is controlled. If the PPPoE dual-stack user is visiting an unauthorized address, it will be forcibly redirected to a payment page.

**Figure 1** Configuring PPPoE dual-stack user access (ND+PD) in scenarios where the RADIUS quota is exhausted![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](figure/en-us_image_0245963967.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a RADIUS server group.
2. Configure AAA schemes.
3. Configure ACL rules and a traffic policy.
4. Configure a local IPv4 address pool.
5. Configure IPv6 address pools.
6. Configure domains.
7. Configure a virtual template.
8. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, RADIUS authentication server's IP addresses and port number, and RADIUS accounting server's IP address and port number
* Local prefix pool names
* IPv6 prefix to be assigned/prefix length
* Local address pool names
* Domain names

#### Procedure

1. Configure a RADIUS server group.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] radius-server group radius
   ```
   ```
   [*DeviceA-radius-radius] radius-server authentication 10.6.55.55 1645
   ```
   ```
   [*DeviceA-radius-radius] radius-server accounting 10.6.55.55 1646
   ```
   ```
   [*DeviceA-radius-radius] commit
   ```
   ```
   [~DeviceA-radius-radius] radius-server type standard
   ```
   ```
   [*DeviceA-radius-radius] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*DeviceA-radius-radius] commit
   ```
   ```
   [~DeviceA-radius-radius] quit
   ```
2. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme. In the authentication scheme view, configure a redirect domain and enable the function to redirect users to this domain when users' RADIUS quota is exhausted.
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] domain redirect
   ```
   ```
   [*DeviceA-aaa-domain-redirect] quit
   ```
   ```
   [*DeviceA-aaa] authentication-scheme radius
   ```
   ```
   [*DeviceA-aaa-authen-radius] commit
   ```
   ```
   [~DeviceA-aaa-authen-radius] authening authen-redirect online authen-domain redirect
   ```
   ```
   [~DeviceA-aaa-authen-radius] authening quota-out-redirect-enable
   ```
   ```
   [~DeviceA-aaa-authen-radius] quit
   ```
   ```
   [~DeviceA-aaa] authentication-scheme none
   ```
   ```
   [*DeviceA-aaa-authen-none] authentication-mode none
   ```
   ```
   [*DeviceA-aaa-authen-none] commit
   ```
   ```
   [~DeviceA-aaa-authen-none] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~DeviceA-aaa] accounting-scheme radius
   ```
   ```
   [*DeviceA-aaa-accounting-radius] accounting-mode radius
   ```
   ```
   [*DeviceA-aaa-accounting-radius] commit
   ```
   ```
   [~DeviceA-aaa-accounting-radius] quit
   ```
   ```
   [~DeviceA-aaa] accounting-scheme none
   ```
   ```
   [*DeviceA-aaa-accounting-none] accounting-mode none
   ```
   ```
   [*DeviceA-aaa-accounting-none] commit
   ```
   ```
   [~DeviceA-aaa-accounting-none] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
3. Configure ACL rules and a traffic policy.
   
   
   
   # Configure a user group.
   
   ```
   [~DeviceA] user-group web-before
   ```
   
   # Configure an ACL numbered 6000 to permit the traffic between the user group **web-before** and the web authentication server and between the user group **web-before** and the DNS server.
   
   ```
   [~DeviceA] acl number 6000
   ```
   ```
   [*DeviceA-acl-ucl-6000] rule permit ip source user-group web-before destination ip-address 10.6.55.56 0.0.0.255
   ```
   ```
   [*DeviceA-acl-ucl-6000] rule permit ip source ip-address 10.6.55.56 0.0.0.255 destination user-group web-before
   ```
   ```
   [*DeviceA-acl-ucl-6000] rule permit ip source user-group web-before destination ip-address 10.10.10.1 0.0.0.255
   ```
   ```
   [*DeviceA-acl-ucl-6000] rule permit ip source ip-address 10.10.10.1 0.0.0.255 destination user-group web-before
   ```
   ```
   [*DeviceA-acl-ucl-6000] commit
   ```
   ```
   [~DeviceA-acl-ucl-6000] quit
   ```
   ```
   [~DeviceA] acl ipv6 number 6000
   ```
   ```
   [*DeviceA-acl6-ucl-6000] rule permit ipv6 source user-group web-before destination ipv6-address 2001:db8:1::2/128
   ```
   ```
   [*DeviceA-acl6-ucl-6000] rule permit ipv6 source ipv6-address 2001:db8:1::2/128 destination user-group web-before
   ```
   ```
   [*DeviceA-acl6-ucl-6000] rule permit ipv6 source user-group web-before destination ipv6-address 2001:db8:1::1/128
   ```
   ```
   [*DeviceA-acl6-ucl-6000] rule permit ipv6 source ipv6-address 2001:db8:1::1/128 destination user-group web-before
   ```
   ```
   [*DeviceA-acl6-ucl-6000] commit
   ```
   ```
   [~DeviceA-acl6-ucl-6000] quit
   ```
   
   # Configure an ACL numbered 6001 to allow HTTPS redirection for the TCP packets originating from the user group **web-before** and whose destination port information is www or 8080.
   
   ```
   [~DeviceA] acl number 6001 
   ```
   ```
   [*DeviceA-acl-ucl-6001] rule permit tcp source user-group web-before destination-port eq www
   ```
   ```
   [*DeviceA-acl-ucl-6001] rule permit tcp source user-group web-before destination-port eq 8080
   ```
   ```
   [*DeviceA-acl-ucl-6001] commit
   ```
   ```
   [~DeviceA-acl-ucl-6001] quit
   ```
   ```
   [~DeviceA] acl ipv6 number 6001
   ```
   ```
   [*DeviceA-acl6-ucl-6001] rule permit tcp source user-group web-before destination-port eq www
   ```
   ```
   [*DeviceA-acl6-ucl-6001] rule permit tcp source user-group web-before destination-port eq 8080
   ```
   ```
   [*DeviceA-acl6-ucl-6001] commit
   ```
   ```
   [~DeviceA-acl6-ucl-6001] quit
   ```
   
   # Configure an ACL numbered 6002 to deny all the traffic originating from the user group **web-before**.
   
   ```
   [~DeviceA] acl 6002 match-order auto
   ```
   ```
   [*DeviceA-acl-ucl-6002] rule permit ip source ip-address any destination user-group web-before
   ```
   ```
   [*DeviceA-acl-ucl-6002] rule deny ip source user-group web-before destination ip-address any
   ```
   ```
   [*DeviceA-acl-ucl-6002] commit
   ```
   ```
   [~DeviceA-acl-ucl-6002] quit
   ```
   ```
   [~DeviceA] acl ipv6 number 6002
   ```
   ```
   [*DeviceA-acl6-ucl-6002] rule permit ipv6 source ipv6-address any destination user-group web-before
   ```
   ```
   [*DeviceA-acl6-ucl-6002] rule deny ipv6 source user-group web-before destination ipv6-address any
   ```
   ```
   [*DeviceA-acl6-ucl-6002] commit
   ```
   ```
   [~DeviceA-acl6-ucl-6002] quit
   ```
   
   # Configure traffic classifiers.
   
   ```
   [~DeviceA] traffic classifier c1
   ```
   ```
   [*DeviceA-classifier-c1] if-match acl 6000
   ```
   ```
   [*DeviceA-classifier-c1] if-match ipv6 acl 6000
   ```
   ```
   [*DeviceA-classifier-c1] commit
   ```
   ```
   [~DeviceA-classifier-c1] quit
   ```
   ```
   [~DeviceA] traffic classifier c2
   ```
   ```
   [*DeviceA-classifier-c2] if-match acl 6001
   ```
   ```
   [*DeviceA-classifier-c2] if-match ipv6 acl 6001
   ```
   ```
   [*DeviceA-classifier-c2] commit
   ```
   ```
   [~DeviceA-classifier-c2] quit
   ```
   ```
   [~DeviceA] traffic classifier c3
   ```
   ```
   [*DeviceA-classifier-c3] if-match acl 6002
   ```
   ```
   [*DeviceA-classifier-c3] if-match ipv6 acl 6002
   ```
   ```
   [*DeviceA-classifier-c3] commit
   ```
   ```
   [~DeviceA-classifier-c3] quit
   ```
   
   # Configure traffic behaviors.
   
   ```
   [~DeviceA] traffic behavior b1
   ```
   ```
   [*DeviceA-behavior-b1] permit
   ```
   ```
   [*DeviceA-behavior-b1] commit
   ```
   ```
   [~DeviceA-behavior-b1] quit
   ```
   ```
   [~DeviceA] traffic behavior b2
   ```
   ```
   [*DeviceA-behavior-b2] http-redirect
   ```
   ```
   [*DeviceA-behavior-b2] commit
   ```
   ```
   [~DeviceA-behavior-b2] quit
   ```
   ```
   [~DeviceA] traffic behavior b3
   ```
   ```
   [*DeviceA-behavior-b3] deny
   ```
   ```
   [*DeviceA-behavior-b3] commit
   ```
   ```
   [*DeviceA-behavior-b3] quit
   ```
   
   # Configure a traffic policy.
   
   ```
   [~DeviceA] traffic policy p1
   ```
   ```
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   ```
   ```
   [*DeviceA-trafficpolicy-p1] classifier c2 behavior b2
   ```
   ```
   [*DeviceA-trafficpolicy-p1] classifier c3 behavior b3
   ```
   ```
   [*DeviceA-trafficpolicy-p1] commit
   ```
   ```
   [~DeviceA-trafficpolicy-p1] quit
   ```
   
   # Apply the traffic policy globally.
   
   ```
   [~DeviceA] traffic-policy p1 inbound
   ```
   ```
   [*DeviceA] commit
   ```
4. Configure a user-side local IPv4 address pool.
   
   
   ```
   [~DeviceA] ip pool pool2 bas local
   ```
   ```
   [*DeviceA-ip-pool-pool2] gateway 10.10.10.2 255.255.255.0
   ```
   ```
   [*DeviceA-ip-pool-pool2] commit
   ```
   ```
   [~DeviceA-ip-pool-pool2] section 0 10.10.10.3 10.10.10.100
   ```
   ```
   [~DeviceA-ip-pool-pool2] dns-server 10.10.10.1
   ```
   ```
   [*DeviceA-ip-pool-pool2] commit
   ```
   ```
   [~DeviceA-ip-pool-pool2] quit
   ```
5. Configure IPv6 address pools.
   
   
   1. Configure a delegation prefix pool for ND users.
      
      ```
      [~DeviceA] ipv6 prefix pre_nd delegation
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_nd] prefix 2001:db8:3::/48
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_nd] slaac-unshare-only
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_nd] commit
      ```
      ```
      [~DeviceA-ipv6-prefix-pre_nd] quit
      ```
   2. Configure a delegation address pool for ND users.
      ```
      [~DeviceA] ipv6 pool pool_nd bas delegation
      ```
      ```
      [*DeviceA-ipv6-pool-pool_nd] prefix pre_nd
      ```
      ```
      [*DeviceA-ipv6-pool-pool_nd] dns-server 2001:db8:1::1 
      ```
      ```
      [*DeviceA-ipv6-pool-pool_nd] commit
      ```
      ```
      [~DeviceA-ipv6-pool-pool_nd] quit
      ```
   3. Configure a delegation prefix pool for PD users.
      ```
      [~DeviceA] ipv6 prefix pre_pd delegation
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_pd] commit
      ```
      ```
      [~DeviceA-ipv6-prefix-pre_pd] pd-unshare-only
      ```
      ```
      [~DeviceA-ipv6-prefix-pre_pd] quit
      ```
   4. Configure a delegation address pool for PD users.
      ```
      [~DeviceA] ipv6 pool pool_pd bas delegation
      ```
      ```
      [*DeviceA-ipv6-pool-pool_pd] prefix pre_pd
      ```
      ```
      [*DeviceA-ipv6-pool-pool_pd] dns-server 2001:db8:1::1 
      ```
      ```
      [*DeviceA-ipv6-pool-pool_pd] commit
      ```
      ```
      [~DeviceA-ipv6-pool-pool_pd] quit
      ```
6. Configure domains.
   
   
   
   # Configure a redirect domain and specify the fields that are allowed to take effect in the redirect domain when the RADIUS quota is exhausted.
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] domain redirect
   ```
   ```
   [~DeviceA-aaa-domain-redirect] redirect-domain effect-attribute user-group
   ```
   ```
   [*DeviceA-aaa-domain-redirect] authentication-scheme none
   ```
   ```
   [*DeviceA-aaa-domain-redirect] accounting-scheme none
   ```
   ```
   [*DeviceA-aaa-domain-redirect] commit
   ```
   ```
   [~DeviceA-aaa-domain-redirect] prefix-assign-mode unshared
   ```
   ```
   [~DeviceA-aaa-domain-redirect] user-group web-before
   ```
   ```
   [~DeviceA-aaa-domain-redirect] web-server 10.6.55.56 2001:db8:1::2
   ```
   ```
   [~DeviceA-aaa-domain-redirect] web-server url isp1.com
   ```
   ```
   [~DeviceA-aaa-domain-redirect] web-server identical-url
   ```
   ```
   [~DeviceA-aaa-domain-redirect] quit
   ```
   
   # Configure a user access domain named **huawei**, and configure the BRAS to forcibly redirect online users when their RADIUS quota is exhausted.
   
   ```
   [~DeviceA-aaa] domain huawei
   ```
   ```
   [*DeviceA-aaa-domain-huawei] authentication-scheme radius
   ```
   ```
   [*DeviceA-aaa-domain-huawei] accounting-scheme radius
   ```
   ```
   [*DeviceA-aaa-domain-huawei] radius-server group radius
   ```
   ```
   [*DeviceA-aaa-domain-huawei] commit
   ```
   ```
   [~DeviceA-aaa-domain-huawei] prefix-assign-mode unshared 
   ```
   ```
   [~DeviceA-aaa-domain-huawei] ip-pool pool2 
   ```
   ```
   [~DeviceA-aaa-domain-huawei] ipv6-pool pool_pd
   ```
   ```
   [~DeviceA-aaa-domain-huawei] ipv6-pool pool_nd
   ```
   ```
   [~DeviceA-aaa-domain-huawei] quota-out redirect url http://www.portal.com
   ```
   ```
   [*DeviceA-aaa-domain-huawei] commit
   ```
   ```
   [~DeviceA-aaa-domain-huawei] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
7. Configure a virtual template.
   
   
   ```
   [~DeviceA] interface virtual-template 1
   ```
   ```
   [*DeviceA-Virtual-Template5] ppp authentication-mode chap
   ```
   ```
   [*DeviceA-Virtual-Template5] commit
   ```
   ```
   [~DeviceA-Virtual-Template5] quit
   ```
8. Configure interfaces.
   
   
   
   # Configure a BAS interface.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/2
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] pppoe-server bind Virtual-Template 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] bas
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2-bas] access-type layer2-subscriber default-domain authentication huawei
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2-bas] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2-bas] quit
   ```
   
   # Enable IPv6 on the BAS interface.
   
   ```
   [~DeviceA-GigabitEthernet0/1/2] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ipv6 address auto link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
   
   # Configure an upstream interface.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address auto link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8:5::1/64 eui-64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ip address 10.2.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceA] quit
   ```
9. Verify the configuration.
   
   
   
   # Check information about the address pool named **pool2**. The command output shows that the gateway address is 10.10.10.2, the addresses in the pool range from 10.10.10.3 to 10.10.10.100, and the DNS server address is 10.10.10.1.
   
   ```
   <DeviceA> display ip pool name pool2
   ```
   ```
     Pool-Name      : pool2                                                        
     Pool-No        : 0                                                            
     Pool-constant-index: -                                                        
     Lease          : 3 Days 0 Hours 0 Minutes                                     
     Frameip-Lease-Manage:  disable                                                
     NetBios Type   : N-Node                                                       
     Auto recycle   : 30                                                           
     Option 3       : Enable                                                       
     DNS-Suffix     : -                                                            
     Dom-Search-List0: -                                                           
     Dom-Search-List1: -                                                           
     Dom-Search-List2: -                                                           
     Dom-Search-List3: -                                                           
     Option-Code 125 : enterprise-code : 2011, string: -                           
   
     DNS1         :10.10.10.1                                                      
     Position       : Local           Status           : Unlocked                  
     RUI-Flag       : -                                                            
     Attribute      : Private                                                      
     Gateway        : 10.10.10.2      Mask             : 255.255.255.0             
     Vpn instance   : --              Unnumbered gateway: -                        
     Profile-Name   : -               Server-Name     : -                          
     Total Idle     : 98              Have Dhcp IP     : 1                         
     Timeouts       : 0                                                            
     Timeout Count  : 0               Sub Option Count : 0                         
     Option Count   : 0               Force-reply Count: 0                         
     Auto-Blocked Times: 0            IP Allocation Failures: 0                    
     Codes: CFLCT(conflicted)         Wait-Request-Time: --                        
     IP Loose Check : 0                                                            
     ------------------------------------------------------------------------------------------------------                                                       
     ID           start             end   total    used    idle   CFLCT disable reserved static-bind delayed                                                       
     -------------------------------------------------------------------------------------------------------                                                       
      0      10.10.10.3    10.10.10.100      98       0      98       0       0    0           0       0                                                       
     -------------------------------------------------------------------------------------------------------                                                       
   ```
   
   # Check information about the prefix pool **pre\_nd**. The command output shows that **pre\_nd** is a local prefix pool and the prefix address is **2001:db8:3::**.
   
   ```
   <DeviceA> display ipv6 prefix pre_nd
   ```
   ```
    ------------------------------------------------------------------------------
    Prefix Name        : pre_nd                
    Prefix Index       : 3
    Prefix constant index: -
    Prefix Type        : DELEGATION          
    Prefix Address     : 2001:DB8:3::                                       
    Prefix Length      : 48 
    Link-Address       : -                  
    Reserved Type      : NONE  
    Valid Lifetime     : 3 Days 0 Hours 0 Minutes
    Preferred Lifetime : 2 Days 0 Hours 0 Minutes
    IfLocked           : Unlocked            
    Vpn instance       : -       
    PD Prefix Len      : 64
    PD Prefix/C-DUID   : -
    slaac-unshare-only : TRUE                
    pd-unshare-only    : FALSE 
    dhcpv6-unshare-only: FALSE               
    Free Prefix Count  : 65536
    Used Prefix Count  : 0
    Bound Prefix Count (Free): 0
    Bound Prefix Count (Used): 0
    Flexibly-Allocted Prefix Count: 0
    Reserved Prefix Count: 0
    Conflict Prefix Count: 0
    Excluded Prefix Count: 0
    Radius Used Total  : 0                                                         
    Radius Used Online : 0                                                         
    Auto-Blocked Times : 0                                                         
    IP Allocation Failures : 0
    ------------------------------------------------------------------------------
   ```
   
   # Check information about the address pool named **pool\_nd**. The command output shows that **pool\_nd** is a user-side local one and is bound to the local prefix pool **pre\_nd**.
   
   ```
   <DeviceA> display ipv6 pool pool_nd
   ```
   ```
    ----------------------------------------------------------------------
    Pool name          : pool_nd                            
    Pool No            : 2     
    Pool-constant-index :- 
    Pool type          : BAS DELEGATION      
    Preference         : 255   
    Renew time         : 50    
    Rebind time        : 80    
    Status             : UNLOCKED  
    Refresh interval   : infinite
    Used by domain     : 1     
    Dhcpv6 Unicast     : disable
    Dhcpv6 rapid-commit: disable
    Dns list           : -
    Dns server master  : 2001:DB8:1::1
    Dns server slave   : -
    AFTR name          : -
    Wait-Request-Time  : --                                                        
    Warning Threshold  : 80                                                        
    Warning Exhaust Switch: FALSE  
    ----------------------------------------------------------------------
    Prefix-Name                      Prefix-Type 
    ----------------------------------------------------------------------
    pre_nd                           DELEGATION
    ----------------------------------------------------------------------
   
   ```
   
   # Check the configuration of the user access domain **huawei**. The command output shows that the IPv6 address pool **pool\_nd** and IPv4 address pool **pool2** are bound to the user access domain **huawei**.
   
   ```
   <DeviceA> display domain huawei
   ```
   ```
   ------------------------------------------------------------------------------
     Domain-name                     : huawei                                      
     Domain-state                    : Active                                      
     Authentication-scheme-name      : radius                                      
     Accounting-scheme-name          : radius                                      
     Authorization-scheme-name       : -                                           
     Primary-DNS-IP-address          : -                                           
     Second-DNS-IP-address           : -                                           
     Primary-DNS-IPV6-address        : -                                           
     Second-DNS-IPV6-address         : -                                           
     Web-server-URL-parameter        : No                                          
     Portal-server-URL-parameter     : No                                          
     Primary-NBNS-IP-address         : -                                           
     Second-NBNS-IP-address          : -                                           
     Time-range                      : Disable                                     
     Idle-cut direction              : Both                                        
     Idle-data-attribute (time,flow) : 0, 60                                       
     User detect interval            : 0s                                          
     User detect retransmit times    : 0                                           
     Install-BOD-Count               : 0                                           
     Report-VSM-User-Count           : 0                                           
     Value-added-service             : default                                     
     User-access-limit               : 118272                                      
     Online-number                   : 0                                           
     Web-IP-address                  : -                                           
     Web-IPv6-address                : -                                           
     Dns-redirect-IP-address         : -                                           
     Web-URL                         : -                                           
     Web-auth-server                 : -                                           
     Web-auth-state                  : -                                           
     Web-server-mode                 : get                                         
     Slave Web-IP-address            : -                                           
     Slave Web-IPv6-address          : -                                           
     Slave Web-URL                   : -                                           
     Slave Web-auth-server           : -                                           
     Slave Web-auth-state            : -                                           
     Web-server identical-url        : Disable                                     
     Portal-server-IP                : -                                           
     Portal-URL                      : -                                           
     Portal-force-times              : 2                                           
     Portal-server identical-url     : Disable                                     
     Service-policy(Portal)          : -                                           
     Ds-lite IPv4 portal             : Disable                                     
     PPPoE-user-URL                  : Disable                                     
     AdminUser-priority              : 16                                          
     IPUser-ReAuth-Time              : 300s                                        
     mscg-name-portal-key            : -                                           
     Portal-user-first-url-key       : -                                           
     User-session-limit              : 4294967295                                  
     Ancp auto qos adapt             : Disable                                     
     L2TP-group-name                 : -                                           
     User-lease-time-no-response     : 0s                                          
     RADIUS-server-template          : radius                                      
     Two-acct-template               : -                                           
     RADIUS-server-pre-template      : -                                           
                                       -                                           
                                       -                                           
     RADIUS-server-llid-first-template: -                                          
     HWTACACS-server-template        : -                                           
     Bill Flow                       : Disable                                     
     Tunnel-acct-2867                : Disable                                     
     Qos-profile-name inbound        : -                                           
     Qos-profile-name outbound       : -                                           
   
     Flow Statistic:                                                               
     Flow-Statistic-Up               : Yes                                         
     Flow-Statistic-Down             : Yes                                         
     Source-IP-route                 : Disable                                     
     IP-warning-threshold            : -                                           
     IP-warning-threshold(Low)       : -                                           
     IPv6-warning-threshold          : -                                           
     IPv6-warning-threshold(Low)     : -                                           
     Multicast Forwarding            : Yes                                         
     Multicast Virtual               : No                                          
     Max-multilist num               : 4                                           
     Multicast-profile               : -                                           
     Multicast-profile ipv6          : -                                           
     Multicast-policy                : -                                           
     Multicast-bandwidth             : -                                           
     Multicast-bandwidth-level-1     : -                                           
     IP-address-pool-name            : pool2                                       
     IPv6-Pool-name                  : pool_pd                                     
     IPv6-Pool-name                  : pool_nd                                     
     Quota-out                       : redirect to URL:http://www.portal.com       
     Service-type                    : -                                           
     User-basic-service-ip-type      : -/-/-                                       
     PPP-ipv6-address-protocol       : Ndra                                        
     IPv6-information-protocol       : Stateless dhcpv6                            
     IPv6-PPP-assign-interfaceid     : Disable                                     
     IPv6-PPP-NDRA-halt              : Disable                                     
     IPv6-PPP-NDRA-unicast           : Disable                                     
     Trigger-packet-wait-delay       : 60s                                         
     Peer-backup                     : Enable                                      
     Reallocate-ip-address           : Disable                                     
     Cui  enable                     : Disable                                     
     Igmp enable                     : Enable                                      
     CPE IP address                  : -                                           
     Pim snooping enable             : Enable                                      
     L2tp-user radius-force          : Disable                                     
     Accounting dual-stack           : Separate                                    
     Prefix-assign-mode              : Unshared                                    
     Radius server domain-annex      : -                                           
     Dhcp-option64-service           : Disable                                     
     Parse-separator                 : -                                           
     Parse-segment-value             : -                                           
     Dhcp-receive-server-packet      : -                                           
     Http-hostcar                    : Disable                                     
     Public-address assign-first     : Disable                                     
     Public-address nat              : Enable                                      
     Dhcp-user auto-save             : Disable                                     
     IP-pool usage-status threshold  : 255 , 255                                   
     Select-Pool-Rule                : gateway + local priority                    
     AFTR name                       : -                                           
     Traffic-rate-mode               : Separate                                    
     Traffic-statistic-mode          : Separate                                    
     Rate-limit-mode-inbound         : Car                                         
     Rate-limit-mode-outbound        : Car                                         
     Service-change-mode             : Stop-start                                  
     DAA Direction                   : both                                        
     Session Volumequota apply direction: both                                     
     Soap-server group               : -                                           
     Nas logic-sysname               : -                                           
     Accounting exclude-type vlan    : -/-                                         
     Framed-ip urpf                  : Enable                                      
     RA link-prefix                  : Disable                                     
     Dslam connect speed             : Disable                                     
     Local backup                    : Enable                                      
     DAA start accounting merge      : disable                                     
     DAA stop accounting merge       : disable                                     
     DAA interim accounting merge    : disable                                     
     DAA merged interim accounting interval(minute) : --                           
     DAA merged interim accounting hash  : disable                                 
     EDSG stop accounting merge      : disable                                     
     EDSG interim accounting merge   : disable                                     
     EDSG merged interim accounting interval(minute): --                           
     EDSG merged interim accounting hash : disable                                 
     Stop dropped flow direction     : -                                           
     Interval dropped flow direction : -                                           
     Edsg family-schedule inbound    : Disable                                     
     Edsg family-schedule outbound   : Disable                                     
     Layer2 IPoE ip-pool select-mode : Local                                       
     Layer2 PPPoE ip-pool select-mode: Local                                       
     access-trigger loose time(minute)   : 0                                       
     access-trigger loose infinite-lease : Disable                                 
     IPv6 address assignment mode    : -                                           
     LNS Tcp-Ack Priority-Car        : Disable                                     
     EDSG Tcp-Ack Priority-Car       : Disable                                     
     Include LNS-IPv6                : Disable                                     
     Map priority                    : MAP-E                                       
     Coa-zero-lease Dual-cut         : Disable                                     
     COA lease zero policy           : -                                           
     Authentication fail online domain : -  
     ------------------------------------------------------------------------------
   
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  # 
  user-group web-before
  #
  radius-server group radius
   radius-server authentication 10.6.55.55 1645 weight 0
   radius-server accounting 10.6.55.55 1646 weight 0
   radius-server type standard
   radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%
  #
  acl number 6000
   rule 5 permit ip source user-group web-before destination ip-address 10.6.55.56 0.0.0.255
   rule 10 permit ip source ip-address 10.6.55.56 0.0.0.255 destination user-group web-before
   rule 15 permit ip source user-group web-before destination ip-address 10.10.10.1 0.0.0.255
   rule 20 permit ip source ip-address 10.10.10.1 0.0.0.255 destination user-group web-before
  #
  acl ipv6 number 6000
   rule 5 permit ipv6 source user-group web-before destination ipv6-address 2001:db8:1::2/128
   rule 10 permit ipv6 source ipv6-address 2001:db8:1::2/128 destination user-group web-before
   rule 15 permit ipv6 source user-group web-before destination ipv6-address 2001:db8:1::1/128
   rule 20 permit ipv6 source ipv6-address 2001:db8:1::1/128 destination user-group web-before
  #
  acl number 6001 
   rule 5 permit tcp destination-port eq www source user-group web-before
   rule 10 permit tcp source user-group web-before destination-port eq 8080
  #
  acl ipv6 number 6001 
   rule 5 permit tcp destination-port eq www source user-group web-before
   rule 10 permit tcp source user-group web-before destination-port eq 8080
  #
  acl number 6002 match-order auto
   rule 5 permit ip source ip-address any destination user-group web-before
   rule 10 deny ip source user-group web-before destination ip-address any
  #
  acl ipv6 number 6002 
   rule 5 permit ipv6 source ipv6-address any destination user-group web-before 
   rule 10 deny ipv6 source user-group web-before destination ipv6-address any
  #
  traffic classifier c1 operator or
   if-match acl 6000
   if-match ipv6 acl 6000
  #
  traffic classifier c2 operator or
   if-match acl 6001
   if-match ipv6 acl 6001
  #
  traffic classifier c3 operator or
   if-match acl 6002
   if-match ipv6 acl 6002
  #
  traffic behavior b1
   permit
  #
  traffic behavior b2
   http-redirect
  #
  traffic behavior b3
   deny
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1
   classifier c2 behavior b2
   classifier c3 behavior b3
  #
  ip pool pool2 bas local
   gateway 10.10.10.2 255.255.255.0
   section 0 10.10.10.3 10.10.10.100
   dns-server 10.10.10.1
  #
  ipv6 prefix pre_nd delegation
   prefix 2001:db8:3::/48
   slaac-unshare-only
  #
  ipv6 pool pool_nd bas delegation
   dns-server 2001:db8:1::1
   prefix pre_nd
  #
  ipv6 prefix pre_pd delegation
   prefix 2001:db8:2::/48 delegating-prefix-length 60
   pd-unshare-only
  #
  ipv6 pool pool_pd bas delegation
   prefix pre_pd
   dns-server 2001:db8:1::1
  #
  aaa
   authentication-scheme none
   authentication-mode none
   authentication-scheme radius
   authening authen-redirect online authen-domain redirect
   authening quota-out-redirect-enable
   #
   authorization-scheme default
   #
   accounting-scheme none
   accounting-mode none
   accounting-scheme radius
   accounting-mode radius
   #
   domain redirect
    redirect-domain effect-attribute user-group
    authentication-scheme none
    accounting-scheme none
    prefix-assign-mode unshared
    user-group web-before
    web-server 10.6.55.56 2001:db8:1::2
    web-server url isp1.com
    web-server identical-url
   #
   domain huawei
    authentication-scheme radius
    accounting-scheme radius
    radius-server group radius
    prefix-assign-mode unshared
    ip-pool pool2
    ipv6-pool pool_pd
    ipv6-pool pool_nd
    quota-out redirect url http://www.portal.com
  #
  interface virtual-template 1
   ppp authentication-mode chap
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address auto link-local
   pppoe-server bind Virtual-Template 1
   bas
   #
    access-type layer2-subscriber default-domain authentication huawei
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ip address 10.2.1.1 24
   ipv6 address 2001:db8:5::1/64 eui-64
   ipv6 address auto link-local
  #
   traffic-policy p1 inbound
  #
   return
  ```