Example for Configuring IPoEv6 Access (Web Authentication)
==========================================================

This section provides an example for configuring IPoEv6 access through web authentication. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374028__fig_dc_ne_ipoxv6_cfg_006701), the networking requirements are as follows:

* The user belongs to the domain **isp2** and accesses the Internet through GE 0/1/2.1 on DeviceA in IPoEv6 mode.
* The user adopts web authentication, and the IP address of the web authentication server is 2001:db8:1::5.

**Figure 1** Configuring IPoEv6 access through web authentication![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/2.1, GE 0/1/1, and GE 0/1/3, respectively.


  
![](images/fig_dc_ne_ipoxv6_cfg_006701.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a local IPv6 address pool.
2. Configure AAA schemes and adopt RADIUS authentication and RADIUS accounting.
3. Configure a user password.
4. Configure web pre-authentication and authentication domains.
5. Configure a web authentication server and an interface connecting DeviceA to the web authentication server.
6. Configure UCL rules and a traffic policy.
7. Configure a BAS interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address pool name
* Domain names
* IP address of the web authentication server
* UCL rules
* Traffic policies
* BAS interface parameters

#### Procedure

1. Configure a local IPv6 address pool.
   
   
   
   # Configure DeviceA.
   
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
   [~DeviceA] ipv6 prefix prefix1 local
   ```
   ```
   [*DeviceA-ipv6-prefix-prefix1] prefix 2001:db8::/64
   ```
   ```
   [*DeviceA-ipv6-prefix-prefix1] commit
   ```
   ```
   [~DeviceA-ipv6-prefix-prefix1] quit
   ```
   ```
   [~DeviceA] ipv6 pool pool_local bas local
   ```
   ```
   [*DeviceA-ipv6-pool-pool_local] prefix prefix1
   ```
   ```
   [*DeviceA-ipv6-pool-pool_local] commit
   ```
   ```
   [~DeviceA-ipv6-pool-pool_local] quit
   ```
   ```
   [~DeviceA] dhcpv6 duid llt
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] authentication-scheme none
   ```
   ```
   [*DeviceA-aaa-authen-none] authentication-mode radius
   ```
   ```
   [*DeviceA-aaa-authen-none] commit
   ```
   ```
   [~DeviceA-aaa-authen-none] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~DeviceA-aaa] accounting-scheme none
   ```
   ```
   [*DeviceA-aaa-accounting-none] accounting-mode radius
   ```
   ```
   [*DeviceA-aaa-accounting-none] commit
   ```
   ```
   [~DeviceA-aaa-accounting-none] quit
   ```
3. Configure the IPoE user password.
   
   
   ```
   [~DeviceA-aaa] default-password cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-aaa] commit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
4. Configure domains.
   
   
   
   # Configure a web pre-authentication domain named **huawei**.
   
   ```
   [~DeviceA] user-group web-before
   ```
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] domain huawei
   ```
   ```
   [*DeviceA-aaa-domain-huawei] commit
   ```
   ```
   [~DeviceA-aaa-domain-huawei] user-group web-before
   ```
   ```
   [~DeviceA-aaa-domain-huawei] web-server url http://[2001:db8:1::]/portal/default.portal
   ```
   ```
   [~DeviceA-aaa-domain-huawei] web-server identical-url
   ```
   ```
   [~DeviceA-aaa-domain-huawei] ipv6-pool pool_local
   ```
   ```
   [~DeviceA-aaa-domain-huawei] authentication-scheme none
   ```
   ```
   [*DeviceA-aaa-domain-huawei] accounting-scheme none
   ```
   ```
   [*DeviceA-aaa-domain-huawei] commit
   ```
   ```
   [~DeviceA-aaa-domain-huawei] quit
   ```
   
   # Configure a web authentication domain named **isp2**.
   
   ```
   [~DeviceA-aaa] domain isp2
   ```
   ```
   [*DeviceA-aaa-domain-isp2] authentication-scheme none
   ```
   ```
   [*DeviceA-aaa-domain-isp2] accounting-scheme none
   ```
   ```
   [*DeviceA-aaa-domain-isp2] commit
   ```
   ```
   [~DeviceA-aaa-domain-isp2] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
5. Configure a loopback interface.
   
   
   ```
   [~DeviceA] interface LoopBack 0
   [*DeviceA-LoopBack0] ipv6 enable
   [*DeviceA-LoopBack0] ipv6 address 2001:db8:1::3 128 
   [*DeviceA-LoopBack0] commit
   [~DeviceA-LoopBack0] quit
   ```
6. Configure a web authentication server and an interface connecting DeviceA to the web authentication server.
   
   
   ```
   [~DeviceA] web-auth-server enable
   ```
   ```
   [~DeviceA] web-auth-server source interface LoopBack0
   ```
   ```
   [~DeviceA] web-auth-server 2001:db8:1::5 port 50100 key cipher YsHsjx_202206
   ```
   ```
   [~DeviceA] web-auth-server source-ipv6 2001:db8:1::3
   ```
7. Configure UCLs.
   
   
   
   # Configure UCL rules.
   
   ```
   [~DeviceA] acl ipv6 6200
   ```
   ```
   [*DeviceA-acl6-ucl-6200] rule 5 permit tcp source user-group any destination ipv6-address 2001:db8:1::/64
   ```
   ```
   [*DeviceA-acl6-ucl-6200] commit
   ```
   ```
   [~DeviceA-acl6-ucl-6200] quit
   ```
   ```
   [~DeviceA] acl ipv6 6300
   ```
   ```
   [*DeviceA-acl6-ucl-6300] rule 5 permit tcp source user-group web-before destination-port eq www
   ```
   ```
   [*DeviceA-acl6-ucl-6300] commit
   ```
   ```
   [~DeviceA-acl6-ucl-6300] quit
   ```
   
   # Configure a traffic policy.
   
   ```
   [~DeviceA] traffic classifier web_permit
   ```
   ```
   [*DeviceA-classifier-web_permit] if-match ipv6 acl 6200
   ```
   ```
   [*DeviceA-classifier-web_permit] commit
   ```
   ```
   [~DeviceA-classifier-web_permit] quit
   ```
   ```
   [~DeviceA] traffic behavior web_permit
   ```
   ```
   [*DeviceA-behavior-web_permit] permit
   ```
   ```
   [*DeviceA-behavior-web_permit] commit
   ```
   ```
   [~DeviceA-behavior-web_permit] quit
   ```
   ```
   [~DeviceA] traffic classifier web_http-redirect
   ```
   ```
   [*DeviceA-classifier-web_http-redirect] if-match ipv6 acl 6300
   ```
   ```
   [*DeviceA-classifier-web_http-redirect] commit
   ```
   ```
   [~DeviceA-classifier-web_http-redirect] quit
   ```
   ```
   [~DeviceA] traffic behavior web_http-redirect
   ```
   ```
   [*DeviceA-behavior-web_http-redirect] http-redirect
   ```
   ```
   [*DeviceA-behavior-web_http-redirect] commit
   ```
   ```
   [~DeviceA-behavior-web_http-redirect] quit
   ```
   ```
   [~DeviceA] traffic policy web
   ```
   ```
   [*DeviceA-trafficpolicy-web] classifier web_permit behavior web_permit
   ```
   ```
   [*DeviceA-trafficpolicy-web] classifier web_http-redirect behavior web_http-redirect
   ```
   ```
   [*DeviceA-trafficpolicy-web] commit
   ```
   ```
   [~DeviceA-trafficpolicy-web] quit
   ```
   
   # Apply the user-side traffic policy globally.
   
   ```
   [~DeviceA] traffic-policy web inbound
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure a BAS interface.
   
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/2.1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] user-vlan 1 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1-vlan-1-1] quit 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1] ipv6 address auto link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1] ipv6 nd autoconfig managed-address-flag
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] bas
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain pre-authentication huawei authentication isp2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1-bas] authentication-method-ipv6 web
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1-bas] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1-bas] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] quit
   ```
   
   # Configure an upstream interface.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address auto link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8:1::1/64 eui-64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
9. Verify the configuration.
   
   
   
   # Check information about the prefix pool named **prefix1**. The command output shows that the prefix pool is a local prefix pool and the prefix address is **2001:db8::/64**.
   
   ```
   [~DeviceA] display ipv6 prefix prefix1                                        
    ------------------------------------------------------------------------------                                                                   
    Prefix Name        : prefix1                                                      
    Prefix Index       : 1                                                         
    Prefix constant index: -                                                       
    Prefix Type        : LOCAL                                                     
    Prefix Address     : 2001:DB8::                                               
    Prefix Length      : 64                                                        
    Reserved Type      : NONE                                                      
    Valid Lifetime     : 3 Days 0 Hours 0 Minutes                                  
    Preferred Lifetime : 2 Days 0 Hours 0 Minutes                                  
    IfLocked           : Unlocked                                                  
    Vpn instance       : -                                                         
    Free Prefix Count  : 262143                                                    
    Used Prefix Count  : 0                                                         
    Reserved Prefix Count: 0                                                       
    Conflict Prefix Count: 0                                                       
    Excluded Prefix Count: 0                                                       
    Radius Used Total  : 0                                                         
    Radius Used Online : 0                                                         
    Auto-Blocked Times : 0                                                         
    IP Allocation Failures : 0                                                     
    -------------------------------------------------------------------------------
   ```
   
   # Check information about the address pool named **pool\_local**. The command output shows that the address pool is a user-side local address pool and is bound to the local prefix pool **prefix1**.
   
   ```
   [~DeviceA] display ipv6 pool pool_local                                    
    ----------------------------------------------------------------------         
    Pool name          : pool_local                                                
    Pool No            : 1                                                         
    Pool constant index: -                                                         
    Pool type          : BAS LOCAL                                                 
    RUI-Flag           : -                                                         
    Preference         : 255                                                       
    Renew time         : 50                                                        
    Rebind time        : 80                                                        
    Status             : UNLOCKED                                                  
    Refresh interval   : infinite                                                  
    Used by domain     : 1                                                         
    Dhcpv6 Unicast     : disable                                                   
    Dhcpv6 rapid-commit: disable                                                   
    Dns list           : -                                                         
    Dns server master  : -                                                         
    Dns server slave   : -                                                         
    AFTR name          : -                                                         
    Wait-Request-Time  : --                                                        
    Warning Threshold  : 80                                                        
    Warning Exhaust Switch: FALSE                                                  
    ----------------------------------------------------------------------         
    Prefix-Name                      Prefix-Type                                   
    ----------------------------------------------------------------------         
    prefix1                          LOCAL                                         
    ----------------------------------------------------------------------         
   ```
   
   # Check information about the domain named **isp2**.
   
   ```
   [~DeviceA] display domain isp2                                             
     ------------------------------------------------------------------------------
     Domain-name                     : isp2                                        
     Domain-state                    : Active                                      
     Authentication-scheme-name      : none                                        
     Accounting-scheme-name          : none                                        
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
     User-access-limit               : 283648                                      
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
     RADIUS-server-template          : -                                         
     Two-acct-template               : -                                           
     RADIUS-server-pre-template      : -                                           
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
     Quota-out                       : Offline                                     
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
     Nas logic-sysname               : -                                           
     Accounting exclude-type vlan    : -/-                                         
     Framed-ip urpf                  : Enable                                      
     RA link-prefix                  : Disable                                     
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
  dhcpv6 duid 0001000125a7625df063f9761497 
  #
  ipv6 prefix prefix1 local
   prefix 2001:DB8::/64 
  #
  ipv6 pool pool_local bas local
   prefix prefix1
  #
  user-group web-before
  #
  acl ipv6 number 6200
   rule 5 permit tcp source user-group any destination ipv6-address 2001:DB8:1::/64
  #
  acl ipv6 number 6300
   rule 5 permit tcp source user-group web-before destination-port eq www
  #
  traffic classifier web_http-redirect operator or
   if-match ipv6 acl 6300 precedence 19
  #
  traffic classifier web_permit operator or
   if-match ipv6 acl 6200 precedence 18
  #
  traffic behavior web_http-redirect 
   http-redirect
  #
  traffic behavior web_permit
  #
  traffic policy web 
   share-mode
   classifier web_permit behavior web_permit precedence 4
   classifier web_http-redirect behavior web_http-redirect precedence 6
  #
  aaa  
   default-password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
   #
   domain huawei
    authentication-scheme none
    accounting-scheme none
    ipv6-pool pool_local
    user-group web-before
    web-server url http://[2001:db8:1::]/portal/default.portal
    web-server identical-url
   #
   domain isp2
    authentication-scheme none
    accounting-scheme none
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64 eui-64
   ipv6 address auto link-local
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 1
   ipv6 nd autoconfig managed-address-flag
   bas
   #
    access-type layer2-subscriber default-domain pre-authentication huawei authentication isp2
    authentication-method-ipv6 web
   #
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:1::3 128
  #
  web-auth-server enable
  web-auth-server source interface LoopBack 0
  web-auth-server 192.168.8.251 port 50100 key cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
  #
  undo web-auth-server source-ip all
  #
  undo web-auth-server source-ipv6 all
  web-auth-server source-ipv6 2001:DB8:1::3
  #
  traffic-policy web inbound
  #
  return
  ```