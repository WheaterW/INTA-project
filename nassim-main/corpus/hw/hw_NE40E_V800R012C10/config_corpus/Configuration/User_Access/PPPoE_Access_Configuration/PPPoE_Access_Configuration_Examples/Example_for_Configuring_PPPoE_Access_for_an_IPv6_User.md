Example for Configuring PPPoE Access for an IPv6 User
=====================================================

This section provides an example for configuring PPPoE access for an IPv6 user.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374123__fig_dc_ne_pppoe_cfg_001401), the requirements are as follows:

* The user belongs to the domain **isp5** and uses PPPoE to go online through GE 0/1/2.1 on the Router.
* RADIUS authentication and accounting are used.
* The IP address of the RADIUS server is 2001:db8::1:1. The authentication and accounting port numbers are 1645 and 1646, respectively. RADIUS+1.1 is used, with the key being **YsHsjx\_202206**.
* The DNS server address is 2001:db8::1:2.

**Figure 1** Networking for configuring PPPoE access for an IPv6 user![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2.1, respectively.


  
![](images/fig_dc_ne_pppoe_cfg_001401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VT.
2. Configure AAA schemes.
3. Configure a RADIUS server group.
4. Configure a local IPv6 prefix pool.
5. Configure a local IPv6 address pool and bind the prefix pool to the address pool.
6. Configure an AAA domain and bind the IPv6 address pool to it.
7. Configure interfaces.

#### Data Preparation

* Virtual template number
* Authentication and accounting schemes and their names
* RADIUS server group name and server addresses
* Start and end VLAN IDs of the sub-interface
* Local prefix pool name
* Assignable IPv6 prefixes and prefix lengths
* Local address pool name
* Domain name

#### Procedure

1. Configure a VT.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface virtual-template 5
   ```
   ```
   [*DeviceA-Virtual-Template5] ppp authentication-mode chap
   ```
   ```
   [*DeviceA-Virtual-Template5] quit
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
   [~DeviceA-aaa] authentication-scheme auth5
   ```
   ```
   [*DeviceA-aaa-authen-auth5] authentication-mode radius
   ```
   ```
   [*DeviceA-aaa-authen-auth5] quit
   ```
   ```
   [*HUAWEI-aaa] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   
   
   # Configure an accounting scheme.
   
   
   
   ```
   [~DeviceA-aaa] accounting-scheme acct5
   ```
   ```
   [*DeviceA-aaa-accounting-acct5] accounting-mode radius
   ```
   ```
   [*DeviceA-aaa-accounting-acct5] quit
   ```
   ```
   [*DeviceA-aaa] quit
   ```
   ```
   [*DeviceA] commit
   ```
3. Configure a RADIUS server group.
   
   
   ```
   [~DeviceA] radius-server group rd5
   ```
   ```
   [*DeviceA-radius-rd5] radius-server authentication 2001:db8::1:1 1645
   ```
   ```
   [*DeviceA-radius-rd5] radius-server accounting 2001:db8::1:1 1646
   ```
   ```
   [*DeviceA-radius-rd5] commit
   ```
   ```
   [~DeviceA-radius-rd5] radius-server type plus11
   ```
   ```
   [~DeviceA-radius-rd5] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-radius-rd5] commit
   ```
   ```
   [~DeviceA-radius-rd5] quit
   ```
4. Configure a local IPv6 prefix pool.
   
   
   ```
   [~DeviceA] ipv6 prefix pre1 local
   ```
   ```
   [*DeviceA-ipv6-prefix-pre1] prefix 2001:db8:2::/64
   ```
   ```
   [*DeviceA-ipv6-prefix-pre1] commit
   ```
   ```
   [~DeviceA-ipv6-prefix-pre1] quit
   ```
5. Configure a local IPv6 address pool and bind the prefix pool to the address pool.
   
   
   ```
   [~DeviceA] ipv6 pool pool1 bas local
   ```
   ```
   [*DeviceA-ipv6-pool-pool1] prefix pre1
   ```
   ```
   [*DeviceA-ipv6-pool-pool1] dns-server 2001:db8::1:2
   ```
   ```
   [*DeviceA-ipv6-pool-pool1] commit
   ```
   ```
   [~DeviceA-ipv6-pool-pool1] quit
   ```
6. Configure a domain named **isp5**.
   
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] domain isp5
   ```
   ```
   [*DeviceA-aaa-domain-isp5] authentication-scheme auth5
   ```
   ```
   [*DeviceA-aaa-domain-isp5] accounting-scheme acct5
   ```
   ```
   [*DeviceA-aaa-domain-isp5] radius-server group rd5
   ```
   ```
   [*DeviceA-aaa-domain-isp5] commit
   ```
   ```
   [~DeviceA-aaa-domain-isp5] ipv6-pool pool1
   ```
   ```
   [~DeviceA-aaa-domain-isp5] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
7. Configure interfaces.
   
   
   
   # Bind the virtual template to GE 0/1/2.1.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/2.1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] pppoe-server bind virtual-template 5
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] quit
   ```
   
   #Configure a BAS interface.
   
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] user-vlan 1 100
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1-vlan-1-100] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] bas
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain authentication isp5
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1-bas] authentication-method-ipv6 ppp
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
   
   # Enable IPv6 on the interface.
   
   ```
   [~DeviceA] interface gigabitEthernet0/1/2.1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2.1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1] ipv6 address auto link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2.1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure an uplink interface.
   
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
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8:3::/64 eui-64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] commit
   ```
8. Verify the configuration.
   
   
   
   # Check information about the prefix pool named **pre1**. The command output shows that the prefix pool is a local prefix pool and the prefix address is 2001:db8:2::/64.
   
   ```
   <DeviceA> display ipv6 prefix pre1
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
    Preferred Lifetime: 2 Days 0 Hours 0 Minutes
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
   <DeviceA> display ipv6 pool pool1
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
   
   # Check information about the domain named **isp5**. The command output shows that the IPv6 address pool named **pool1** is bound to the domain.
   
   ```
   <DeviceA> display domain isp5
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
sysname DeviceA
#
radius-server group rd5
 radius-server authentication 2001:db8::1:1 1645 weight 0
 radius-server accounting 2001:db8::1:1 1646 weight 0
 radius-server type plus11
 radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
#
interface Virtual-Template5
 ppp authentication-mode chap
#
ipv6 prefix pre1 local
prefix 2001:db8:2::/64
#
ipv6 pool pool1 bas local
prefix pre1
dns-server 2001:db8::1:2
#
aaa
 authentication-scheme default0
 authentication-scheme default1
 authentication-scheme auth5
 authentication-mode radius
#
accounting-scheme default0
accounting-scheme default1
accounting-scheme acct5
accounting-mode radius
#
domain isp5
 authentication-scheme auth5
 accounting-scheme acct5
 ipv6-pool pool1
 radius-server group rd5
 #
#
interface GigabitEthernet0/1/2.1
 pppoe-server bind Virtual-Template 5
 ipv6 enable
 ipv6 address auto link-local
 user-vlan 1 100
 bas
 access-type layer2-subscriber default-domain authentication isp5
 authentication-method-ipv6 ppp
#
interface GigabitEthernet0/1/1
 ipv6 enable
 ipv6 address 2001:db8:3::/64 eui-64
 ipv6 address auto link-local
#
return

```