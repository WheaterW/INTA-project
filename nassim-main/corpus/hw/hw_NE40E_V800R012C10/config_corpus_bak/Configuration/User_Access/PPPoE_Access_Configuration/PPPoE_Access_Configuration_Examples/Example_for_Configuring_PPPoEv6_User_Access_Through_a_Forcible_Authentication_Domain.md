Example for Configuring PPPoEv6 User Access Through a Forcible Authentication Domain
====================================================================================

This section provides an example for configuring PPPoEv6 user access through a forcible authentication domain. After the configuration is complete, all users in domain 1 are forcibly assigned to domain 2 (with IPv6 addresses configured) for network access.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0204850935__fig611834582516), a user belongs to domain 1 and accesses the Internet through a GE interface on DeviceA in PPPoE mode. DeviceA is configured with RADIUS authentication and accounting. When the user requests to go online, the user is authenticated and charged according to the policies bound to the forcible authentication domain, regardless of whether the domain name is contained in the authentication request packet or what the contained domain name is. In this example, the user is forcibly authenticated and charged in domain 2 where an IPv6 address pool is configured. In addition, DHCPv6 IA\_PD is used to allocate an IPv6 prefixes to the user, and DHCPv6 IA\_ND is used to allocate an IPv6 address to the user. The user goes online through Eth-Trunk 2.10 on DeviceA.

**Figure 1** Configuring PPPoE user access through a forcible authentication domain![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/2.1 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0205123037.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a virtual template.
2. Configure AAA schemes.
3. Configure a RADIUS server group.
4. Configure a local IPv6 prefix pool and a local IPv6 address pool, and bind the prefix pool to the address pool.
5. Configure an AAA domain and bind the local IPv6 address pool to the AAA domain.
6. Configure the BRAS to generate DUIDs in DUID-LLT mode.
7. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Virtual template number
* RADIUS authentication and accounting schemes and their names
* RADIUS server group name and RADIUS server addresses
* Local prefix pool names
* Assignable IPv6 prefixes and prefix lengths
* Local address pool names
* Domain names

#### Configuration Procedure

1. Configure a virtual template.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] interface virtual-template 1
   [*HUAWEI-Virtual-Template1] ppp authentication-mode chap
   [*HUAWEI-Virtual-Template1] commit
   [~HUAWEI-Virtual-Template1] quit
   ```
2. Configure AAA schemes.
   
   # Configure an authentication scheme.
   
   ```
   [~HUAWEI] aaa
   [~HUAWEI-aaa] authentication-scheme auth1
   [*HUAWEI-aaa-authen-auth1] authentication-mode radius
   [*HUAWEI-aaa-authen-auth1] commit
   [~HUAWEI-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct1
   [*HUAWEI-aaa-accounting-acct1] accounting-mode radius
   [*HUAWEI-aaa-accounting-acct1] commit
   [~HUAWEI-aaa-accounting-acct1] quit
   [~HUAWEI-aaa] quit
   ```
3. Configure a RADIUS server group.
   ```
   [~HUAWEI] radius-server group rd1
   [*HUAWEI-radius-rd1] radius-server authentication 2001:db8:5::1 1645
   [*HUAWEI-radius-rd1] radius-server accounting 2001:db8:5::1 1646
   [*HUAWEI-radius-rd1] commit
   [~HUAWEI-radius-rd1] radius-server type standard
   [~HUAWEI-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
   [*HUAWEI-radius-rd1] commit
   [~HUAWEI-radius-rd1] quit
   ```
4. Configure IPv6 address pools.
   1. Configure a delegation prefix pool for ND users.
      ```
      [~HUAWEI] ipv6 prefix pre_nd delegation
      [*HUAWEI-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48 delegating-prefix-length 64
      [*HUAWEI-ipv6-prefix-pre_nd] slaac-unshare-only
      [~HUAWEI-ipv6-prefix-pre_nd] commit
      [~HUAWEI-ipv6-prefix-pre_nd] quit
      ```
   2. Configure a delegation address pool for ND users.
      
      ```
      [~HUAWEI] ipv6 pool ipv6_nd bas delegation
      [*HUAWEI-ipv6-pool-ipv6_nd] prefix pre_nd
      [*HUAWEI-ipv6-pool-ipv6_nd] dns-server 2001:db8::2:2
      [*HUAWEI-ipv6-pool-ipv6_nd] commit
      [~HUAWEI-ipv6-pool-ipv6_nd] quit
      ```
   3. Configure a delegation prefix pool for PD users.
      ```
      [~HUAWEI] ipv6 prefix pre_pd delegation
      [*HUAWEI-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
      [*HUAWEI-ipv6-prefix-pre_pd] commit
      [~HUAWEI-ipv6-prefix-pre_pd] pd-unshare-only
      [~HUAWEI-ipv6-prefix-pre_pd] quit
      ```
   4. Configure a delegation address pool for PD users.
      ```
      [~HUAWEI] ipv6 pool ipv6_pd bas delegation
      [*HUAWEI-ipv6-pool-ipv6_pd] prefix pre_pd
      [*HUAWEI-ipv6-pool-ipv6_pd] dns-server 2001:db8::2:2
      [*HUAWEI-ipv6-pool-ipv6_pd] commit
      [~HUAWEI-ipv6-pool-ipv6_pd] quit
      ```
5. Configure domains.
   
   # Configure a domain named **domain1**.
   
   ```
   [~HUAWEI] aaa
   [~HUAWEI-aaa] domain domain1
   [*HUAWEI-aaa-domain-domain1] authentication-scheme acct1
   [*HUAWEI-aaa-domain-domain1] accounting-scheme acct1
   [*HUAWEI-aaa-domain-domain1] radius-server group rd1
   [*HUAWEI-aaa-domain-domain1] commit
   [~HUAWEI-aaa-domain-domain1] quit
   ```
   
   # Configure a domain named **domain2**.
   
   ```
   [~HUAWEI-aaa] domain domain2
   [*HUAWEI-aaa-domain-domain2] authentication-scheme acct1
   [*HUAWEI-aaa-domain-domain2] accounting-scheme acct1
   [*HUAWEI-aaa-domain-domain2] radius-server group rd1 
   [*HUAWEI-aaa-domain-domain2] prefix-assign-mode unshared
   [*HUAWEI-aaa-domain-domain2] ipv6-pool ipv6_nd
   [*HUAWEI-aaa-domain-domain2] ipv6-pool ipv6_pd
   [*HUAWEI-aaa-domain-domain2] commit
   [~HUAWEI-aaa-domain-domain2] quit
   [~HUAWEI-aaa] quit
   ```
6. Configure the BRAS to generate DUIDs in DUID-LLT mode.
   ```
   [~HUAWEI] dhcpv6 duid llt
   [*HUAWEI] commit
   ```
7. Configure interfaces.
   1. Configure a sub-interface and bind the virtual template to the sub-interface.
      ```
      [~HUAWEI] interface Eth-Trunk 2.10
      [*HUAWEI-Eth-Trunk2.10] pppoe-server bind virtual-template 1
      ```
   2. Enable IPv6 on the sub-interface.
      ```
      [*HUAWEI-Eth-Trunk2.10] ipv6 enable
      [*HUAWEI-Eth-Trunk2.10] ipv6 address auto link-local
      [*HUAWEI-Eth-Trunk2.10] commit
      ```
   3. Configure a BAS interface to encapsulate the BAS interface information into the access-line-id field of the authentication request packet sent by a client. Then, configure a forcible authentication domain on the BAS interface.
      ```
      [~HUAWEI-Eth-Trunk2.10] bas
      [~HUAWEI-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain authentication domain1
      [*HUAWEI-Eth-Trunk2.10-bas] client-option82 basinfo-insert cn-telecom
      [*HUAWEI-Eth-Trunk2.10-bas] default-domain authentication ppp-user force domain2
      [*HUAWEI-Eth-Trunk2.10-bas] commit
      [~HUAWEI-Eth-Trunk2.10-bas] quit
      [~HUAWEI-Eth-Trunk2.10] quit
      ```
   4. Configure an upstream interface.
      ```
      [~HUAWEI] interface gigabitEthernet 0/1/1
      [~HUAWEI-GigabitEthernet0/1/1] ipv6 enable
      [*HUAWEI-GigabitEthernet0/1/1] ipv6 address auto link-local
      [*HUAWEI-GigabitEthernet0/1/1] ipv6 address 2001:db8:1::1/64 eui-64
      [*HUAWEI-GigabitEthernet0/1/1] commit
      ```
8. Verify the configuration.
   
   # After completing the configurations, run the **display ipv6 prefix pre\_nd** command to view information about the prefix pool named **pre\_nd**. The command output shows that the prefix pool is a local prefix pool and the prefix address is 2001:db8:1::/48.
   
   ```
   <HUAWEI> display ipv6 prefix pre_nd  
   -------------------------------------------------------------  
   Prefix Name        : pre_nd  
   Prefix Index       : 4 
   Prefix constant index: -  
   Prefix Type        : LOCAL  
   Prefix Address     : 2001:db8:1::  
   Prefix Length      : 48 
   Reserved Type      : NONE    
   Valid Lifetime     : 3 Days 0 Hours 0 Minutes  
   Preferred Lifetime : 2 Days 0 Hours 0 Minutes  
   IfLocked           : Unlocked 
   Vpn instance       : -        
   Conflict address   : - 
   Free Prefix Count  : 262144  
   Used Prefix Count  : 0  
   Reserved Prefix Count: 0     
   ------------------------------------------------------------- 
   ```
   
   # Run the **display ipv6 pool pool1** command to view information about the address pool named **pool1**. The command output shows that **pool1** is a local address pool on the user side and the local prefix pool named **pre1** is bound to this address pool.
   
   ```
   <HUAWEI> display ipv6 pool pool1  
   ----------------------------------------------------------------------  
   Pool name          : pool1  
   Pool No            : 4    
   Pool-constant-index:-   
   Pool type          : BAS LOCAL  
   Preference         : 0  
   Renew time         : 50  
   Rebind time        : 80  
   Status             : UNLOCKED  
   Refresh interval   : 0 Days 0 Hours 0 Minutes  
   Used by domain     : 1  
   Dhcpv6 Unicast     : disable  
   Dhcpv6 rapid-commit: disable  
   Dns list           : -  
   Dns server master  : 2001:db8::2:2  
   Dns server slave   : - 
   AFTR name          : -   
   ----------------------------------------------------------------------  
   Prefix-Name                      Prefix-Type  
   ----------------------------------------------------------------------  
   pre1                               LOCAL 
   ---------------------------------------------------------------------- 
   ```
   
   # View information about the domain named **domain2**.
   
   ```
   <HUAWEI> display domain domain2 
   ------------------------------------------------------------------------------   
   Domain-name                     : domain2   
   Domain-state                    : Active   
   Authentication-scheme-name      : auth1   
   Accounting-scheme-name          : acct1  
   Authorization-scheme-name       :   
   Primary-DNS-IP-address          : -   
   Second-DNS-IP-address           : -   
   Web-server-URL-parameter        : No   
   Slave Web-IP-address            : -   
   Slave Web-URL                   : -   
   Slave Web-auth-server           : -    
   Slave Web-auth-state            : -    
   Portal-server-URL-parameter     : No   
   Primary-NBNS-IP-address         : -   
   Second-NBNS-IP-address          : -   
   User-group-name                 : -   
   Idle-data-attribute (time,flow) : 0, 60   
   Install-BOD-Count               : 0   
   Report-VSM-User-Count           : 0   
   Value-added-service             : default   
   User-access-limit               : 279552   
   Online-number                   : 0   
   Web-IP-address                  : -   
   Web-URL                         : -   
   Portal-server-IP                : -   
   Portal-URL                      : -   
   Portal-force-times              : 2   
   PPPoE-user-URL                  : Disable     
   RADIUS-server-template          : rd1   
   Two-acct-template               : -   
   HWTACACS-server-template        : -   
   Bill Flow                       : Disable   
   Tunnel-acct-2867                : Disabled    
   Flow Statistic:   
   Flow-Statistic-Up               : Yes   
   Flow-Statistic-Down             : Yes   
   Source-IP-route                 : Disable   
   IP-warning-threshold            : -   
   IPv6-warning-threshold          : -    
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
   Trigger-packet-wait-delay       : 60s   
   Peer-backup                     : enable      
   ------------------------------------------------------------------------------ 
   ```

#### Configuration Files

```
#
sysname HUAWEI 
#                                                                               
radius-server group rd1
radius-server authentication 2001:db8:5::1 1645 weight 0 
radius-server accounting 2001:db8:5::1 1646 weight 0  
radius-server type standard
radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%  
# 
interface Virtual-Template1 
 ppp authentication-mode chap 
# 
ipv6 prefix pre_nd delegation 
 prefix 2001:db8:1::/48 delegating-prefix-length 64
 slaac-unshare-only 
# 
ipv6 pool ipv6_nd bas delegation 
 prefix pre_nd 
 dns-server 2001:db8::2:2
# 
ipv6 prefix pre_pd delegation 
 prefix 2001:db8:2::/48 delegating-prefix-length 60
 pd-unshare-only 
# 
ipv6 pool ipv6_pd bas delegation 
 prefix pre_nd 
 dns-server 2001:db8::2:2
#
aaa  
 authentication-scheme auth1  
 authentication-mode radius 
 accounting-scheme acct1 
 accounting-mode radius 
# 
domain domain1  
 authentication-scheme auth1  
 accounting-scheme acct1    
 radius-server group rd1 
# 
domain domain2  
 authentication-scheme auth1  
 accounting-scheme acct1    
 radius-server group rd1
 prefix-assign-mode unshared
 ipv6-pool ipv6_nd 
 ipv6-pool ipv6_pd 
#
 dhcpv6 duid llt
# 
interface Eth-Trunk 2.10  
 pppoe-server bind Virtual-Template 1  
 ipv6 enable  
 ipv6 address auto link-local  
 bas  
 access-type layer2-subscriber default-domainauthentication domain1
 client-option82 basinfo-insert cn-telecom
 default-domain authentication ppp-user force domain2
# 
interface gigabitEthernet0/1/1  
 ipv6 enable   
 ipv6 address auto link-local
 ipv6 address 2001:db8:1::1 eui-64  
# 
return 

```