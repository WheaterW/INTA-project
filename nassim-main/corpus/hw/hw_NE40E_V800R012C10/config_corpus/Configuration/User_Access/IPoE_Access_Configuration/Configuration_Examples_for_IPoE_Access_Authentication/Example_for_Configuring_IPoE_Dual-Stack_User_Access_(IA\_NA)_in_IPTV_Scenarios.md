Example for Configuring IPoE Dual-Stack User Access (IA\_NA) in IPTV Scenarios
==============================================================================

This section provides an example for configuring IPoE dual-stack user access in IA\_NA mode in IPTV scenarios. When a user (an STB) connects to a BRAS in IPoE access mode in an IPTV scenario, the BRAS implements RADIUS authentication and accounting, as well as assigns an IPv4 address to the user from the local address pool and an IPv6 address to the user through DHCPv6 (IA\_NA). This allows the user to access the network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0265005357__fig_dc_ne_ipox_cfg_007201), a user (an STB) initiates a connection in an IPTV scenario. DeviceA implements RADIUS authentication and accounting, assigns an IPv4 address to the user from the local address pool, and assigns an IPv6 address to the user through the DHCPv6 IA\_NA option carrying an IA Address option. DeviceA uses the binding authentication mode. Specifically, the Option field is filled in the password during user authentication, and a character string in the format of *MAC address@IPTV domain name* is generated as the username. The username and password are then sent to the RADIUS server for authentication. After being authenticated, the user accesses the network through GE 0/1/2 on DeviceA.

**Figure 1** Configuring IPoE dual-stack user access (IA\_NA) in IPTV scenarios![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and interface2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0265005358.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure AAA schemes and adopt RADIUS authentication and RADIUS accounting.
2. Configure a loopback interface as the source interface for accessing servers.
3. Configure a RADIUS server group.
4. Configure a local IPv4 address pool.
5. Configure a local IPv6 prefix pool.
6. Configure a local IPv6 address pool, and bind the local IPv6 prefix pool to this address pool.
7. Configure the device to generate user passwords based on Option 60.
8. Configure a domain.
9. Configure a DUID for the device.
10. Configure a BAS interface and an upstream interface.
11. Configure basic multicast functions.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, RADIUS authentication server's IP address and port number, and RADIUS accounting server's IP address and port number
* Local prefix pool name
* IPv6 prefix to be assigned/prefix length
* Local address pool names
* Domain name

#### Procedure

1. Configure AAA schemes.
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] aaa
   [~DeviceA-aaa] authentication-scheme auth1
   [*DeviceA-aaa-authen-auth1] authentication-mode radius
   [*DeviceA-aaa-authen-auth1] commit
   [~DeviceA-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~DeviceA-aaa] accounting-scheme acct1
   [*DeviceA-aaa-accounting-acct1] accounting-mode radius
   [*DeviceA-aaa-accounting-acct1] commit
   [~DeviceA-aaa-accounting-acct1] quit
   [~DeviceA-aaa] quit
   ```
2. Configure a loopback interface as the source interface for accessing servers.
   ```
   [~DeviceA] interface loopBack 0
   [*DeviceA-LoopBack0] ipv6 enable
   [*DeviceA-LoopBack0] ip address 10.0.0.1 255.255.255.255
   [*DeviceA-LoopBack0] ipv6 address 2001:db8:1::3 128
   [*DeviceA-LoopBack0] ipv6 address auto link-local 
   [*DeviceA-LoopBack0] commit 
   [~DeviceA-LoopBack0] quit
   ```
3. Configure a RADIUS server group.
   ```
   [~DeviceA] radius-server group rd1
   [*DeviceA-radius-rd1] radius-server authentication 10.6.55.55 1645
   [*DeviceA-radius-rd1] radius-server accounting 10.6.55.55 1646
   [*DeviceA-radius-rd1] radius-server source interface LoopBack 0
   [*DeviceA-radius-rd1] commit
   [~DeviceA-radius-rd1] radius-server shared-key-cipher it-is-my-secret1
   [*DeviceA-radius-rd1] commit
   [~DeviceA-radius-rd1] quit
   ```
4. Configure a local IPv4 address pool.
   ```
   [~DeviceA] ip pool pool2 bas local
   [*DeviceA-ip-pool-pool2] gateway 10.10.10.2 255.255.255.0
   [*DeviceA-ip-pool-pool2] commit
   [~DeviceA-ip-pool-pool2] section 0 10.10.10.3 10.10.10.100
   [~DeviceA-ip-pool-pool2] dns-server 10.0.0.10 10.0.0.11
   [*DeviceA-ip-pool-pool2] commit
   [~DeviceA-ip-pool-pool2] quit
   ```
5. Configure a local IPv6 prefix pool.
   ```
   [~DeviceA] ipv6 prefix pre1 local
   [~DeviceA-ipv6-prefix-pre1] prefix 2001:db8:3::/48
   [~DeviceA-ipv6-prefix-pre1] quit
   ```
6. Configure a local IPv6 address pool, and bind the local IPv6 prefix pool to this address pool.
   ```
   [~DeviceA] ipv6 pool pool1 bas local
   [~DeviceA-ipv6-pool-pool1] prefix pre1
   [*DeviceA-ipv6-pool-pool1] commit
   [~DeviceA-ipv6-pool-pool1] dns-server 2001:db8:1::1 2001:db8:1::2
   [~DeviceA-ipv6-pool-pool1] quit
   ```
7. Configure the device to generate user passwords based on Option 60.
   ```
   [~DeviceA] aaa
   [*DeviceA-aaa] default-password template iptv option60
   [*DeviceA-aaa] commit
   [~DeviceA-aaa] quit
   ```
8. Configure a domain.
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] domain huawei
   [*DeviceA-aaa-domain-huawei] authentication-scheme auth1
   [*DeviceA-aaa-domain-huawei] accounting-scheme acct1
   [*DeviceA-aaa-domain-huawei] radius-server group rd1
   [*DeviceA-aaa-domain-huawei] commit
   [~DeviceA-aaa-domain-huawei] ip-pool pool2 
   [~DeviceA-aaa-domain-huawei] ipv6-pool pool1
   [~DeviceA-aaa-domain-huawei] quit
   [~DeviceA-aaa] quit
   ```
9. Configure a DUID for the device.
   ```
   [~DeviceA] dhcpv6 duid llt
   [*DeviceA] commit
   ```
10. Configure a BAS interface and an upstream interface.
    
    # Enable IPv6 and configure stateful address autoconfiguration on a sub-interface.
    
    ```
    [~DeviceA] interface gigabitethernet 0/1/1.1
    [*DeviceA-GigabitEthernet0/1/1.1] commit
    [~DeviceA-GigabitEthernet0/1/1.1] ipv6 enable
    [*DeviceA-GigabitEthernet0/1/1.1] ipv6 address auto link-local
    [*DeviceA-GigabitEthernet0/1/1.1] ipv6 nd autoconfig managed-address-flag 
    [*DeviceA-GigabitEthernet0/1/1.1] commit
    ```
    
    # Configure a BAS interface for IPoE user access.
    
    ```
    [~DeviceA-GigabitEthernet0/1/1.1] user-vlan 3000 3799 qinq 2700 2955
    [~DeviceA-GigabitEthernet0/1/1.1-vlan-3000-3799-QinQ-2700-2955] quit
    [~DeviceA-GigabitEthernet0/1/1.1] bas
    [~DeviceA-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication huawei
    [*DeviceA-GigabitEthernet0/1/1.1-bas] authentication-method bind 
    [*DeviceA-GigabitEthernet0/1/1.1-bas] authentication-method-ipv6 bind
    [*DeviceA-GigabitEthernet0/1/1.1-bas] client-option82
    [*DeviceA-GigabitEthernet0/1/1.1-bas] client-option60
    [*DeviceA-GigabitEthernet0/1/1.1-bas] client-option18
    [*DeviceA-GigabitEthernet0/1/1.1-bas] client-option37
    [*DeviceA-GigabitEthernet0/1/1.1-bas] ip-trigger
    [*DeviceA-GigabitEthernet0/1/1.1-bas] arp-trigger
    [*DeviceA-GigabitEthernet0/1/1.1-bas] commit
    [~DeviceA-GigabitEthernet0/1/1.1-bas] ipv6-trigger
    [~DeviceA-GigabitEthernet0/1/1.1-bas] nd-trigger
    [~DeviceA-GigabitEthernet0/1/1.1-bas] default-password-template iptv
    ```
    
    # Enable multicast replication by interface+VLAN on the BAS interface.
    
    ```
    [~DeviceA-GigabitEthernet0/1/1.1-bas] multicast copy by-vlan
    [*DeviceA-GigabitEthernet0/1/1.1-bas] commit
    [~DeviceA-GigabitEthernet0/1/1.1-bas] quit
    [~DeviceA-GigabitEthernet0/1/1.1] quit
    ```
    
    # Configure an upstream interface.
    
    ```
    [~DeviceA] interface gigabitethernet 0/1/2
    [~DeviceA-GigabitEthernet0/1/2] ipv6 enable
    [*DeviceA-GigabitEthernet0/1/2] ip address 10.10.10.10
    [*DeviceA-GigabitEthernet0/1/2] ipv6 address 2001:db8:5::/64 eui-64
    [*DeviceA-GigabitEthernet0/1/2] ipv6 address auto link-local
    [*DeviceA-GigabitEthernet0/1/2] commit
    [~DeviceA-GigabitEthernet0/1/2] quit
    ```
11. Configure basic multicast functions.
    ```
    [~DeviceA] multicast routing-enable
    [*DeviceA] multicast ipv6 routing-enable
    [*DeviceA] interface gigabitethernet 0/1/1.1
    [*DeviceA-GigabitEthernet0/1/1.1] pim sm
    [*DeviceA-GigabitEthernet0/1/1.1] pim ipv6 sm
    [*DeviceA-GigabitEthernet0/1/1.1] igmp enable
    [*DeviceA-GigabitEthernet0/1/1.1] mld enable
    [*DeviceA-GigabitEthernet0/1/1.1] commit
    [~DeviceA-GigabitEthernet0/1/1.1] quit
    [~DeviceA] interface gigabitethernet 0/1/2
    [~DeviceA-GigabitEthernet0/1/2] pim sm
    [*DeviceA-GigabitEthernet0/1/2] pim ipv6 sm
    [*DeviceA-GigabitEthernet0/1/2] commit
    [~DeviceA-GigabitEthernet0/1/2] quit
    [~DeviceA] quit
    ```
12. Verify the configuration.
    
    # Check information about the address pool named **pool2**. The command output shows that the gateway address is **10.10.10.2** and the IP addresses in the address pool range from **10.10.10.3** to **10.10.10.100**.
    
    ```
    <DeviceA> display ip pool name pool2
     ----------------------------------------------------------------------
      Pool-Name      : pool2                                                        
      Pool-No        : 2                                                            
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
    
      Position       : Local           Status           : Unlocked                  
      RUI-Flag       : -                                                            
      Attribute      : Private                                                      
      Gateway        : 10.10.10.2     Mask             : 255.255.255.0             
      Vpn instance   : --              Unnumbered gateway: -                        
      Profile-Name   : -               Server-Name     : -                          
      Total Idle     : 98              Have Dhcp IP     : 1                         
      Timeouts       : 0                                                            
      Timeout Count  : 0               Sub Option Count : 0                         
      Option Count   : 0               Force-reply Count: 0                         
      Auto-Blocked Times: 0            IP Allocation Failures: 0                    
      Codes: CFLCT(conflicted)         Wait-Request-Time: --                        
      IP Loose Check : 0                                                            
      -------------------------------------------------------------------------------------------------------                                                       
      ID           start            end   total    used    idle   CFLCT disable reserved static-bind delayed                                                       
      -------------------------------------------------------------------------------------------------------                                                       
       0      10.10.10.3    10.10.10.100      98       0      98       0       0     0           0       0                                                       
      -------------------------------------------------------------------------------------------------------              
    
    ```
    
    # Check information about the prefix pool named **pre1**. The command output shows that **pre1** is a local prefix pool and its prefix address is **2001:db8:3::**.
    
    ```
    <DeviceA> display ipv6 prefix pre1
     ------------------------------------------------------------------------------
     Prefix Name        : pre1                                                      
     Prefix Index       : 0                                                         
     Prefix constant index: -                                                       
     Prefix Type        : LOCAL                                                     
     Prefix Address     : 2001:DB8:3::                                              
     Prefix Length      : 48                                                        
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
     ------------------------------------------------------------------------------
    ```
    
    # Check information about the address pool named **pool1**. The command output shows that **pool1** is a local address pool and is bound to the local prefix pool **pre1**.
    
    ```
    <DeviceA> display ipv6 pool pool1
     ----------------------------------------------------------------------
     Pool name          : pool1                                                     
     Pool No            : 0                                                         
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
     pre1                             LOCAL                                         
     ---------------------------------------------------------------------- 
    ```
    
    # Check the configurations of the domain named **huawei**. The command output shows that the domain **huawei** is bound to the IPv6 address pool **pool1** and IPv4 address pool **pool2**.
    
    ```
    <DeviceA> display domain huawei
     ------------------------------------------------------------------------------
      Domain-name                     : huawei                                      
      Domain-state                    : Active                                      
      Authentication-scheme-name      : auth1                                       
      Accounting-scheme-name          : acct1                                       
      Authorization-scheme-name       : -                                           
      Primary-DNS-IP-address          : 10.0.0.10                                   
      Second-DNS-IP-address           : 10.0.0.11                                 
      Primary-DNS-IPV6-address        : 2001:DB8:1::1                               
      Second-DNS-IPV6-address         : 2001:DB8:1::2                               
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
      User-access-limit               : 1078272                                     
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
      RADIUS-server-template          : rd1                                         
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
    
    # Run the **display multicast group-ip** command to check the users who have ordered a specific multicast program.
    
    ```
    <DeviceA> display multicast group-ip FF18::1 out-interface gigabitEthernet 0/1/1.1   
    User ID    User IP             User type    Interface    
    65         2001:db8:3::9      Local        GigabitEthernet0/1/1.1    
    Local user number :1   
    Remote user number:0   
    Total user number :1
    ```

#### Configuration Files

```
#
sysname DeviceA
#
multicast routing-enable
#
multicast ipv6 routing-enable
#
radius-server group rd1
 radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
 radius-server authentication 10.6.55.55 1645 weight 0
 radius-server accounting 10.6.55.55 1646 weight 0
 radius-server source interface LoopBack0
#
ip pool pool2 bas local
 gateway 10.10.10.2 255.255.255.0
 section 0 10.10.10.3 10.10.10.100
 dns-server 10.0.0.10 10.0.0.11
#
ipv6 prefix pre1 local
 prefix 2001:DB8:3::/48
#
ipv6 pool pool1 bas local
 dns-server 2001:DB8:1::1 2001:DB8:1::2
 prefix pre1
#
dhcpv6 duid 0001000125a7625df063f9761497
#
aaa
 default-password template iptv option60
 # 
 authentication-scheme auth1
 #
 authorization-scheme default
 #
 accounting-scheme acct1
 #
 domain huawei 
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1 
  ip-pool pool2
  ipv6-pool pool1
#
interface GigabitEthernet0/1/1
 undo shutdown
#
interface GigabitEthernet0/1/1.1
 ipv6 enable
 ipv6 address auto link-local 
 user-vlan 3000 3799 qinq 2700 2955
 pim sm
 pim ipv6 sm
 igmp enable
 mld enable
 ipv6 nd autoconfig managed-address-flag 
 bas
 #
  access-type layer2-subscriber default-domain authentication huawei
  client-option82
  client-option60
  client-option37
  client-option18
  authentication-method bind                                                    
  authentication-method-ipv6 bind
  ip-trigger
  arp-trigger
  ipv6-trigger 
  nd-trigger
  default-password-template iptv
  multicast copy by-vlan 
#
interface GigabitEthernet0/1/2
 undo shutdown
 ipv6 enable
 ip address 10.10.10.10 255.255.255.0 
 ipv6 address 2001:DB8:5::/64 eui-64
 ipv6 address auto link-local
 pim sm
 pim ipv6 sm
#                                                                               
interface LoopBack 0                                                             
 ipv6 enable                                                                    
 ip address 10.0.0.1 255.255.255.255                                            
 ipv6 address 2001:DB8:1::3/128                                                 
 ipv6 address auto link-local   
#
return
```