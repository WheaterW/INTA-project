Example for Configuring PPPoE Access for an IPv4/IPv6 Dual-Stack User
=====================================================================

This section provides an example for configuring PPPoE access for an IPv4/IPv6 dual-stack user.

#### Networking Requirements

On the network in [Figure 1](#EN-US_TASK_0172374126__fig_dc_ne_pppoe_cfg_001501), to allow the IPv4/IPv6 dual-stack user to go online, configure PPPoE access. The requirements are as follows:

* The user belongs to the domain **isp5** and uses PPPoE to go online through GE 0/1/2 on the Router.
* RADIUS authentication and accounting are used.
* The IP address of the RADIUS server is 10.6.55.55. The authentication and accounting port numbers are 1645 and 1646, respectively. The standard RADIUS protocol is used, with the key being **YsHsjx\_202206**.
* The addresses of the two DNS servers are 2001:db8::1:2 and 10.10.10.1, respectively.

**Figure 1** Networking for configuring PPPoE access for an IPv4/IPv6 dual-stack user![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_ne_pppoe_cfg_001501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a virtual template.
2. Configure AAA schemes.
3. Configure a RADIUS server group.
4. Configure a local IPv4 address pool.
5. Configure a local IPv6 prefix pool.
6. Configure a local IPv6 address pool and bind the prefix pool to the address pool.
7. Configure an AAA domain and bind the IPv4 and IPv6 address pools to the domain.
8. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Virtual template number
* Name of the authentication scheme and RADIUS authentication mode
* Name of the accounting scheme and RADIUS accounting mode
* RADIUS server group name and IP addresses and port numbers of the RADIUS authentication and accounting servers
* Local prefix pool name
* Assignable IPv6 prefixes and prefix lengths
* Local address pool name
* Domain name

#### Procedure

1. Configure a virtual template.
   
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] interface virtual-template 5
   ```
   ```
   [*Device-Virtual-Template5] ppp authentication-mode chap
   ```
   ```
   [*Device-Virtual-Template5] quit
   ```
   ```
   [*Device] commit
   ```
2. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] authentication-scheme auth5
   ```
   ```
   [*Device-aaa-authen-auth5] authentication-mode radius
   ```
   ```
   [*Device-aaa-authen-auth5] quit
   ```
   ```
   [*Device-aaa] quit
   ```
   ```
   [*Device] commit
   ```
   
   
   
   # Configure an accounting scheme.
   
   
   
   ```
   [~Device-aaa] accounting-scheme acct5
   ```
   ```
   [*Device-aaa-accounting-acct5] accounting-mode radius
   ```
   ```
   [*Device-aaa-accounting-acct5] quit
   ```
   ```
   [*Device-aaa] quit
   ```
   ```
   [*Device] commit
   ```
3. Configure a RADIUS server group.
   
   
   ```
   [~Device] radius-server group rd5
   ```
   ```
   [*Device-radius-rd1] radius-server authentication 10.6.55.55 1645
   ```
   ```
   [*Device-radius-rd1] radius-server accounting 10.6.55.55 1646
   ```
   ```
   [~Device-radius-rd1] commit
   ```
   ```
   [~Device-radius-rd1] radius-server type standard
   ```
   ```
   [~Device-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*Device-radius-rd1] commit
   ```
   ```
   [*Device-radius-rd1] quit
   ```
4. Configure a local IPv4 address pool.
   
   
   ```
   [~Device] ip pool pool2 bas local
   ```
   ```
   [*Device-ip-pool-pool2] gateway 10.10.10.2 255.255.255.0
   ```
   ```
   [*Device-ip-pool-pool2] commit
   ```
   ```
   [~Device-ip-pool-pool2] section 0 10.10.10.3 10.10.10.100
   ```
   ```
   [*Device-ip-pool-pool2] dns-server 10.10.10.1
   ```
   ```
   [*Device-ip-pool-pool2] commit
   ```
   ```
   [~Device-ip-pool-pool2] quit
   ```
5. Configure a local IPv6 prefix pool.
   
   
   ```
   [~Device] ipv6 prefix pre1 local
   ```
   ```
   [*Device-ipv6-prefix-pre1] prefix 2001:db8:2::/64
   ```
   ```
   [*Device-ipv6-prefix-pre1] commit
   ```
   ```
   [~Device-ipv6-prefix-pre1] quit
   ```
6. Configure a local IPv6 address pool and bind the prefix pool to the address pool.
   
   
   ```
   [~Device] ipv6 pool pool1 bas local
   ```
   ```
   [*Device-ipv6-pool-pool1] prefix pre1
   ```
   ```
   [*Device-ipv6-pool-pool1] dns-server 2001:db8::1:2
   ```
   ```
   [*Device-ipv6-pool-pool1] commit
   ```
   ```
   [~Device-ipv6-pool-pool1] quit
   ```
7. Configure a domain named **isp5**.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain isp5
   ```
   ```
   [*Device-aaa-domain-isp5] authentication-scheme auth5
   ```
   ```
   [*Device-aaa-domain-isp5] accounting-scheme acct5
   ```
   ```
   [*Device-aaa-domain-isp5] radius-server group rd5
   ```
   ```
   [*Device-aaa-domain-isp5] commit
   ```
   ```
   [~Device-aaa-domain-isp5] ipv6-pool pool1
   ```
   ```
   [~Device-aaa-domain-isp5] ip-pool pool2
   ```
   ```
   [~Device-aaa-domain-isp5] quit
   ```
   ```
   [~Device-aaa] quit
   ```
8. Configure interfaces.
   
   
   
   # Bind the virtual template to the interface.
   
   ```
   [~Device] interface gigabitethernet 0/1/2
   ```
   ```
   [*Device-GigabitEthernet0/1/2] pppoe-server bind virtual-template 5
   ```
   ```
   [*Device] commit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~Device-GigabitEthernet0/1/2] bas
   ```
   ```
   [~Device-GigabitEthernet0/1/2-bas] access-type layer2-subscriber default-domain authentication isp5
   ```
   ```
   [*Device-GigabitEthernet0/1/2-bas] commit
   ```
   ```
   [~Device-GigabitEthernet0/1/2-bas] quit
   ```
   
   # Enable IPv6 on the interface.
   
   ```
   [~Device-GigabitEthernet0/1/2] ipv6 enable
   ```
   ```
   [*Device-GigabitEthernet0/1/2] ipv6 address auto link-local
   ```
   ```
   [*Device-GigabitEthernet0/1/2] quit
   ```
   ```
   [*Device] commit
   ```
   
   # Configure upstream interfaces.
   
   ```
   [~Device] interface GigabitEthernet 0/1/1
   ```
   ```
   [~Device-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*Device-GigabitEthernet0/1/1] ipv6 address auto link-local
   ```
   ```
   [*Device-GigabitEthernet0/1/1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*Device-GigabitEthernet0/1/1] ipv6 address 2001:db8:3::/64 eui-64
   ```
   ```
   [*Device-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Device] commit
   ```
9. Verify the configuration.
   
   
   
   # Check information about the address pool named **pool2**. The command output shows that the gateway address is 10.10.10.2, the addresses in the pool range from 10.10.10.3 to 10.10.10.100, and the DNS server address is 10.10.10.1.
   
   ```
   <Device> display ip pool name pool2
   ```
   ```
     Pool-Name      : pool2
     Pool-No        : 0  
     Pool-constant-index :- 
     Lease          : 3 Days 0 Hours 0 Minutes
     NetBios Type   : N-Node
     DNS-Suffix     : -
   
     DNS1           :10.10.10.1
     Position       : Local           Status           : Unlocked
     Gateway        : 10.10.10.2      Mask             : 255.255.255.0
     Vpn instance   : --
     Profile-Name   : -               Server-Name      : -
     Codes: CFLCT(conflicted)
     ---------------------------------------------------------------------------
     ID           start             end total  used  idle CFLCT disable reserved
     ---------------------------------------------------------------------------
      0      10.10.10.3    10.10.10.100    98     0    98     0       0        0
     --------------------------------------------------------------------------- 
   ```
   
   # Check information about the prefix pool named **pre1**. The command output shows that the prefix pool is a local prefix pool and the prefix address is 2001:db8:2::/64.
   
   ```
   <Device> display ipv6 prefix pre1
   ```
   ```
    -------------------------------------------------------------
    Prefix Name        : pre1
    Prefix Index       : 4
    Prefix constant index: -
    Prefix Type        : LOCAL
    Prefix Address     : 2001:db8:2::
    Prefix Length      : 64
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
   
   # Check information about the address pool named **pool1**. The command output shows that the address pool is a user-side local address pool and the local prefix pool named **pre1** is bound to it.
   
   ```
   <Device> display ipv6 pool pool1
   ```
   ```
    ----------------------------------------------------------------------
    Pool name          : pool1
    Pool No            : 4  
    Pool-constant-index :- 
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
    Dns server master  : 2001:db8::1:2
    Dns server slave   : -
    AFTR name          : - 
    ----------------------------------------------------------------------
    Prefix-Name                      Prefix-Type
    ----------------------------------------------------------------------
    pre1                               LOCAL
   ----------------------------------------------------------------------
   
   ```
   
   # Check the configuration of the domain named **isp5**. The command output shows that the IPv6 address pool named **pool1** and the IPv4 address pool named **pool2** are bound to the domain.
   
   ```
   <Device> display domain isp5
   ```
   ```
   ------------------------------------------------------------------------------
     Domain-name                     : isp5
     Domain-state                    : Active
     Authentication-scheme-name      : auth5
     Accounting-scheme-name          : acct5
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
     IPUser-ReAuth-Time(second)      : 300
     mscg-name-portal-key            : -
     Portal-user-first-url-key       : -
     Ancp auto qos adapt             : Disable
     Service-type                    : STB
     RADIUS-server-template          : rd5
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
     IP-address-pool-name            : pool2
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
sysname Device
#
radius-server group rd5
 radius-server authentication 10.6.55.55 1645 weight 0
 radius-server accounting 10.6.55.55 1646 weight 0
 radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
#
interface Virtual-Template5
 ppp authentication-mode chap
#
ip pool pool2 bas local
 gateway 10.10.10.2 255.255.255.0
 section 0 10.10.10.3 10.10.10.100
 dns-server 10.10.10.1
#
ipv6 prefix pre1 local
 prefix 2001:DB8:2::/64
#
ipv6 pool pool1 bas local
 prefix pre1
 dns-server 2001:db8::1:2
#
aaa
 #
 authentication-scheme default0
 #
 authentication-scheme default1
 #
 authentication-scheme auth5
  authentication-mode radius
 #
 accounting-scheme default0
 #
 accounting-scheme default1
 #
 accounting-scheme acct5
  accounting-mode radius
#
domain isp5
 authentication-scheme auth5
 accounting-scheme acct5
 ip-pool pool2
 ipv6-pool pool1
 radius-server group rd5
#
interface GigabitEthernet0/1/2
 pppoe-server bind Virtual-Template 5
 ipv6 enable
 ipv6 address auto link-local
 bas
 access-type layer2-subscriber default-domain authentication isp5
#
interface GigabitEthernet0/1/1
 ipv6 enable
 ip address 10.1.1.1 255.255.255.0
 ipv6 address 2001:db8:3::/64 eui-64
 ipv6 address auto link-local
#
return
```