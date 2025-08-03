Example for Configuring IPoEv6 Access in ND Mode
================================================

This section provides an example for configuring IPoEv6 access in ND mode.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374025__fig_dc_ne_ipox_cfg_009801), the networking requirements are as follows:

* A user belongs to the domain **isp6** and accesses the network through GE 0/1/2 on the NE40E in ND mode. Binding authentication is adopted.
* RADIUS authentication and RADIUS accounting are used.
* The IP address of the RADIUS server is 10.6.55.55. The authentication port number is 1645, and the accounting port number is 1646. The standard RADIUS protocol is adopted. The shared key is **it-is-my-secret1**.
* The IP address of the DNS server is 2001:db8:1::2.

**Figure 1** Networking for configuring IPoEv6 access in ND mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_ne_ipox_cfg_009801.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure AAA schemes.
2. Configure a RADIUS server group.
3. Configure an IPv6 delegation prefix pool.
4. Configure an IPv6 delegation address pool and bind the address pool to the prefix pool.
5. Configure an AAA domain and bind the domain to the address pool.
6. Configure a user password.
7. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication template name and authentication method
* Accounting template name and accounting mode
* RADIUS server group name, and IP addresses and port numbers of the RADIUS authentication server and accounting server
* Local prefix pool name
* Prefix length and assignable IPv6 prefixes
* Local address pool name
* Domain name

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] authentication-scheme auth6
   ```
   ```
   [*HUAWEI-aaa-authen-auth6] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-auth6] commit
   ```
   ```
   [~HUAWEI-aaa-authen-auth6] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct6
   ```
   ```
   [*HUAWEI-aaa-accounting-acct6] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-acct6] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-acct6] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
2. Configure a RADIUS server group.
   
   
   ```
   [~HUAWEI] radius-server group rd6
   ```
   ```
   [*HUAWEI-radius-rd6] radius-server authentication 10.6.55.55 1645
   ```
   ```
   [*HUAWEI-radius-rd6] radius-server accounting 10.6.55.55 1646
   ```
   ```
   [*HUAWEI-radius-rd6] commit
   ```
   ```
   [~HUAWEI-radius-rd6] radius-server type standard
   ```
   ```
   [*HUAWEI-radius-rd6] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*HUAWEI-radius-rd6] commit
   ```
   ```
   [~HUAWEI-radius-rd6] quit
   ```
3. Configure a delegation prefix pool.
   
   
   ```
   [~HUAWEI] ipv6 prefix pre1 delegation
   ```
   ```
   [*HUAWEI-ipv6-prefix-pre1] prefix 2001:db8:2::/64
   ```
   ```
   [~*HUAWEI-ipv6-prefix-pre1] slaac-unshare-only
   ```
   ```
   [*HUAWEI-ipv6-prefix-pre1] commit
   ```
   ```
   [~HUAWEI-ipv6-prefix-pre1] quit
   ```
4. Configure a user-side delegation address pool.
   
   
   ```
   [~HUAWEI] ipv6 pool pool1 bas delegation
   ```
   ```
   [*HUAWEI-ipv6-pool-pool1] prefix pre1
   ```
   ```
   [*HUAWEI-ipv6-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ipv6-pool-pool1] dns-server 2001:db8:1::2
   ```
   ```
   [~HUAWEI-ipv6-pool-pool1] quit
   ```
5. Configure a domain named **isp6**.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp6
   ```
   ```
   [*HUAWEI-aaa-domain-isp6] authentication-scheme auth6
   ```
   ```
   [*HUAWEI-aaa-domain-isp6] accounting-scheme acct6
   ```
   ```
   [*HUAWEI-aaa-domain-isp6] radius-server group rd6
   ```
   ```
   [*HUAWEI-aaa-domain-isp6] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp6] ipv6-pool pool1
   ```
   ```
   [~HUAWEI-aaa-domain-isp6] prefix-assign-mode unshared
   ```
   ```
   [~HUAWEI-aaa-domain-isp6] quit
   ```
6. Configure a user password
   
   
   ```
   [~HUAWEI-aaa] [default-password cipher test@123](cmdqueryname=default-password+cipher+test%40123)
   ```
   ```
   [*HUAWEI-aaa] [commit](cmdqueryname=commit)
   ```
7. Configure interfaces.
   
   
   
   # Configure a BAS interface.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/2
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2-bas] access-type layer2-subscriber default-domain authentication isp6
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2-bas] authentication-method-ipv6 bind
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2-bas] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2-bas] quit
   ```
   
   # Enable IPv6 on GE 0/1/2.
   
   ```
   [~HUAWEI-GigabitEthernet0/1/2] ipv6 enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] ipv6 address auto link-local
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2] quit
   ```
   
   # Configure an upstream interface.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] ipv6 address auto link-local
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] ipv6 address 2001:db8:3::/64 eui-64
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] quit
   ```
   ```
   [~HUAWEI] quit
   ```
8. Verify the configuration.
   
   
   
   # After the configuration is complete, you can run the **display ipv6 prefix** command to view information about the prefix pool named **pre1**. The command output shows that the prefix pool is a delegation prefix pool and the prefix address is 2001:DB8:2::/64.
   
   ```
   <HUAWEI> display ipv6 prefix pre1
   ```
   ```
    -------------------------------------------------------------
    Prefix Name        : pre1
    Prefix Index       : 4
    Prefix constant index: -
    Prefix Type        : DELEGATION
    Prefix Address     : 2001:DB8:2::
    Prefix Length      : 64
    Reserved Type      : NONE  
    Valid Lifetime     : 3 Days 0 Hours 0 Minutes
    Preferred Lifetime: 2 Days 0 Hours 0 Minutes
    IfLocked            : Unlocked
    Vpn instance       : -       
    Conflict address   : -
    Free Prefix Count  : 262144
    Used Prefix Count  : 0
    Reserved Prefix Count: 0   
    -------------------------------------------------------------
   
   ```
   
   # Run the **display ipv6 pool** command to view information about the address pool named **pool1**. The command output shows that the address pool is a user-side local address pool and the address pool is bound to the prefix pool named **pre1**.
   
   ```
   <HUAWEI> display ipv6 pool pool1
   ```
   ```
    ----------------------------------------------------------------------
    Pool name          : pool1
    Pool No            : 4 
    Pool constant index :- 
    Pool type          : BAS DELEGATION
    Preference         : 0
    Renew time         : 50
    Rebind time        : 80
    Status              : UNLOCKED
    Refresh interval   : 0 Days 0 Hours 0 Minutes
    Used by domain     : 1
    Dhcpv6 Unicast     : disable
    Dhcpv6 rapid-commit: disable
    Dns list             : -
    Dns server master  : 2001:DB8:1::2
    Dns server slave   : -
    AFTR name          : -   
    ----------------------------------------------------------------------
    Prefix-Name                      Prefix-Type
    ----------------------------------------------------------------------
    pre1                             DELEGATION
   ----------------------------------------------------------------------
   
   ```
   
   # Run the **display domain** command to view information about the domain named **isp6**. The command output shows that the domain is bound to the IPv6 address pool named **pool1**.
   
   ```
   <HUAWEI> display domain isp6
   ```
   ```
     ------------------------------------------------------------------------------
     Domain-name                     : isp6                                          
     Domain-state                    : Active                                      
     Authentication-scheme-name      : auth6                                    
     Accounting-scheme-name          : acct6                                    
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
     User-access-limit               : 152576                                      
     Online-number                   : 0                                           
     Web-IP-address                  : -                                           
     Web-URL                         : -                                           
     Web-auth-server                 : -                                           
     Web-auth-state                  : -                                           
     Web-server-mode                 : get                                         
     Slave Web-IP-address            : -                                           
     Slave Web-URL                   : -                                           
     Slave Web-auth-server           : -                                           
     Slave Web-auth-state            : -                                           
     Portal-server-IP                : -                                           
     Portal-URL                      : -                                           
     Portal-force-times              : 2                                           
     Service-policy(Portal)          : -                                           
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
                                       -                                           
                                       -                                           
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
     IPv6-Pool-name                  : pool1                                         
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
     DAA Direction                   : both                                        
     ------------------------------------------------------------------------------
   ```

#### Configuration Files

* Device configuration file
  
  ```
  #
  sysname HUAWEI
  #
  radius-server group rd6
   radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
   radius-server authentication 10.6.55.55 1645 weight 0
   radius-server accounting 10.6.55.55 1646 weight 0
  #
  ipv6 prefix pre1 delegation
   prefix 2001:DB8:2::/64
   slaac-unshare-only
  #
  ipv6 pool pool1 bas delegation
   dns-server 2001:DB8:1::2
   prefix pre1
  #
  aaa
   #
   default-password cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
   #
   authentication-scheme default1
   #
   authentication-scheme auth6
   #
   accounting-scheme default1
   #
   accounting-scheme acct6
   #
   domain isp6
    authentication-scheme auth6
    accounting-scheme acct6
    radius-server group rd6
    prefix-assign-mode unshared
    ipv6-pool pool1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::/64 eui-64
   ipv6 address auto link-local
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address auto link-local
   bas
   #
    access-type layer2-subscriber default-domain authentication isp6
    authentication-method-ipv6 bind
   #
  #
  return
  ```