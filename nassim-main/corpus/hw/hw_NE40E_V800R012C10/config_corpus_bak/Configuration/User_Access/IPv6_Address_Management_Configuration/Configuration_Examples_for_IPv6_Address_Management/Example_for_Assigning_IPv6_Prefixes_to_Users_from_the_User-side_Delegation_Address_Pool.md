Example for Assigning IPv6 Prefixes to Users from the User-side Delegation Address Pool
=======================================================================================

This section provides an example for assigning IPv6 prefixes to users from the user-side delegation address pool. A networking diagram is provided to help you understand the configuration procedure. The example covers the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

The CPE obtains IPv6 addresses and prefixes from the NE40E in NDRA+IA\_PD mode, and the IPv6 addresses of the LAN users connected to the CPE are generated based on the prefixes and interface IDs.

On the network shown in [Figure 1](#EN-US_TASK_0172373935__fig_dc_ne_ipv6_address_cfg_011201):

* The NE40E functions as a delegating router to assign IPv6 prefixes to a requesting router.
* The requesting router resides in the domain named **isp1** and is connected to the delegating router through GE 0/1/1. PPP authentication is used for PPPoE users.
* RADIUS authentication and accounting are used.
* The IP address of the RADIUS server is 10.6.55.55, the authentication port number is 1550, the accounting port number is 1551, the standard RADIUS protocol is used, and the key is **YsHsjx\_202206**.
* The DNS server address is 2001:db8:1::1.

**Figure 1** Network diagram of assigning IPv6 prefixes from the user-side delegation address pool![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/1/1, respectively.


  
![](images/fig_dc_ne_ipv6_address_cfg_011201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VT.
2. Configure AAA schemes.
3. Configure a RADIUS server group.
4. Configure a prefix pool, an address pool, and the binding between the prefix pool and address pool. Specify the DNS server address in the address pool.
5. Configure a domain named **isp1**.
6. Configure a DUID for the DHCPv6 server.
7. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and RADIUS authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP addresses and port numbers of the RADIUS authentication and accounting servers
* Names, address prefixes, and assignable prefix lengths of the local IPv6 prefix pool and IPv6 delegation prefix pool
* Names of the user-side local IPv6 address pool and user-side IPv6 delegation address pool
* Domain name
* Parameters of the BAS interface

#### Procedure

1. Configure DeviceB.
   
   
   
   # Configure a VT.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] interface Virtual-Template 1
   ```
   ```
   [*Device-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*Device-Virtual-Template1] commit
   ```
   ```
   [~Device-Virtual-Template1] quit
   ```
2. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] authentication-scheme auth1
   ```
   ```
   [*Device-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*Device-aaa-authen-auth1] commit
   ```
   ```
   [~Device-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~Device-aaa] accounting-scheme acct1
   ```
   ```
   [*Device-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*Device-aaa-accounting-acct1] commit
   ```
   ```
   [~Device-aaa-accounting-acct1] quit
   ```
   ```
   [~Device-aaa] quit
   ```
3. Configure a RADIUS server group.
   
   
   ```
   [~Device] radius-server group rd1
   ```
   ```
   [*Device-radius-rd1] radius-server authentication 10.6.55.55 1550
   ```
   ```
   [*Device-radius-rd1] radius-server accounting 10.6.55.55 1551
   ```
   ```
   [*Device-radius-rd1] commit
   ```
   ```
   [~Device-radius-rd1] radius-server type standard
   ```
   ```
   [~Device-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [~Device-radius-rd1] quit
   ```
4. Configure a local prefix pool.
   
   
   ```
   [~Device] ipv6 prefix pre1 local
   ```
   ```
   [*Device-ipv6-prefix-pre1] prefix 2001:db8::/64
   ```
   ```
   [*Device-ipv6-prefix-pre1] commit
   ```
   ```
   [~Device-ipv6-prefix-pre1] quit
   ```
5. Configure a user-side local address pool.
   
   
   ```
   [~Device] ipv6 pool pool1 bas local
   ```
   ```
   [*Device-ipv6-pool-pool1] prefix pre1
   ```
   ```
   [*Device-ipv6-pool-pool1] dns-server 2001:db8:1::1
   ```
   ```
   [*Device-ipv6-pool-pool1] commit
   ```
   ```
   [~Device-ipv6-pool-pool1] quit
   ```
6. Configure a delegation prefix pool.
   
   
   ```
   [~Device] ipv6 prefix pre2 delegation
   ```
   ```
   [*Device-ipv6-prefix-pre2] prefix 2001:db8::/62 delegating-prefix-length 63
   ```
   ```
   [*Device-ipv6-prefix-pre2] commit
   ```
   ```
   [~Device-ipv6-prefix-pre2] quit
   ```
7. Configure a user-side delegation address pool.
   
   
   ```
   [~Device] ipv6 pool pool2 bas delegation
   ```
   ```
   [*Device-ipv6-pool-pool2] prefix pre2
   ```
   ```
   [*Device-ipv6-pool-pool2] dns-server 2001:db8:1::1
   ```
   ```
   [*Device-ipv6-pool-pool2] commit
   ```
   ```
   [~Device-ipv6-pool-pool2] quit
   ```
8. Configure a domain named **isp1**.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain isp1
   ```
   ```
   [*Device-aaa-domain-isp1] authentication-scheme auth1
   ```
   ```
   [*Device-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [*Device-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*Device-aaa-domain-isp1] commit
   ```
   ```
   [~Device-aaa-domain-isp1] ipv6-pool pool1
   ```
   ```
   [~Device-aaa-domain-isp1] ipv6-pool pool2
   ```
   ```
   [~Device-aaa-domain-isp1] quit
   ```
   ```
   [~Device-aaa] quit
   ```
9. Configure a DUID for the DHCPv6 server.
   
   
   ```
   [~Device] dhcpv6 duid llt
   ```
   ```
   [*Device] commit
   ```
10. Configure interfaces.
    
    
    
    # Configure a BAS interface.
    
    ```
    [~Device] interface GigabitEthernet 0/1/1.1
    ```
    ```
    [*Device-GigabitEthernet0/1/1.1] commit
    ```
    ```
    [~Device-GigabitEthernet0/1/1.1] user-vlan 1 20
    ```
    ```
    [~Device-GigabitEthernet0/1/1.1-vlan-1-20] quit
    ```
    ```
    [~Device-GigabitEthernet0/1/1.1] bas
    ```
    ```
    [~Device-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication isp1
    ```
    ```
    [*Device-GigabitEthernet0/1/1.1-bas] authentication-method-ipv6 ppp
    ```
    ```
    [*Device-GigabitEthernet0/1/1.1-bas] commit
    ```
    ```
    [~Device-GigabitEthernet0/1/1.1-bas] quit
    ```
    
    # Bind the VT to the interface.
    
    ```
    [~Device-GigabitEthernet0/1/1.1] pppoe-server bind virtual-template 1
    ```
    ```
    [*Device-GigabitEthernet0/1/1.1] commit
    ```
    
    # Enable IPv6 on the interface.
    
    ```
    [~Device-GigabitEthernet0/1/1.1] ipv6 enable
    ```
    ```
    [*Device-GigabitEthernet0/1/1.1] ipv6 address auto link-local
    ```
    ```
    [*Device-GigabitEthernet0/1/1.1] commit
    ```
    ```
    [~Device-GigabitEthernet0/1/1] quit
    ```
    
    # Configure an upstream interface.
    
    ```
    [~Device] interface GigabitEthernet 0/1/2
    ```
    ```
    [~Device-GigabitEthernet0/1/2] ipv6 enable
    ```
    ```
    [*Device-GigabitEthernet0/1/2] ipv6 address auto link-local
    ```
    ```
    [*Device-GigabitEthernet0/1/2] ipv6 address 2001:db8::2 64 eui-64
    ```
    ```
    [*Device-GigabitEthernet0/1/2] commit
    ```
    ```
    [~Device-GigabitEthernet0/1/2] quit
    ```
11. Verify the configuration. 
    
    
    
    # Check information about the prefix pool named **pre1**. The command output shows that the prefix pool is a local prefix pool and the prefix address is 2001:db8::/64.
    
    ```
    [~Device] display ipv6 prefix pre1
    ```
    ```
     -------------------------------------------------------------
     Prefix Name        : pre1
     Prefix Index       : 4
     Prefix constant index: -
     Prefix Type        : LOCAL
     Prefix Address     : 2001:db8::
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
    
    # Check information about the prefix pool named **pre2**. The command output shows that the prefix pool is a delegation prefix pool and the prefix address is 2001:db8::/62.
    
    ```
    [~Device] display ipv6 prefix pre2
    ```
    ```
     -------------------------------------------------------------
     Prefix Name        : pre2
     Prefix Index       : 5
     Prefix constant index: -
     Prefix Type        : DELEGATION
     Prefix Address     : 2001:db8::
     Prefix Length      : 62
     Valid Lifetime     : 3 Days 0 Hours 0 Minutes
     Preferred Lifetime : 2 Days 0 Hours 0 Minutes
     IfLocked           : Unlocked
     Vpn instance       : -      
     PD Prefix Len      : 64
     PD Prefix/C-DUID   : -
     slaac-unshare-only : FALSE
     Conflict address   : -
     Free Prefix Count  : 4
     Used Prefix Count  : 0
     Binded Prefix Count (Free): 0
     Binded Prefix Count (Used): 0
     Reserved Prefix Count: 0     
     -------------------------------------------------------------
    
    ```
    
    # Check information about the address pool named **pool1**. The command output shows that the address pool is a user-side local address pool and has been bound to the local prefix pool **pre1**.
    
    ```
    [~Device] display ipv6 pool pool1
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
     Status              : UNLOCKED
     Refresh interval   : 0 Days 0 Hours 0 Minutes
     Used by domain     : 1
     Dhcpv6 Unicast     : disable
     Dhcpv6 rapid-commit: disable
     Dns list             : -
     Dns server master  : 2001:db8::2:2
     Dns server slave   : -
     AFTR name          : - 
     ----------------------------------------------------------------------
     Prefix-Name                      Prefix-Type
     ----------------------------------------------------------------------
     pre1                               LOCAL
    ----------------------------------------------------------------------
    
    ```
    
    # Check information about the address pool named **pool2**. The command output shows that the address pool is a user-side delegation address pool and has been bound to the local prefix pool named **pre2**.
    
    ```
    [~Device] display ipv6 pool pool2
    ```
    ```
    ----------------------------------------------------------------------
     Pool name          : pool2
     Pool No            : 5 
      Pool-constant-index :- 
     Pool type          : BAS DELEGATION
     Preference         : 255
     Renew time         : 50
     Rebind time        : 80
     Status              : UNLOCKED
     Refresh interval   : 0 Days 0 Hours 0 Minutes
     Used by domain     : 0
     Dhcpv6 Unicast     : disable
     Dhcpv6 rapid-commit: disable
     Dns list            : -
     Dns server master  : -
     Dns server slave   : -
     AFTR name          : - 
     ----------------------------------------------------------------------
     Prefix-Name                      Prefix-Type
     ----------------------------------------------------------------------
     pre2                               DELEGATION
    ----------------------------------------------------------------------
    
    ```
    
    Check configurations of the domain **isp1**. The command output shows that the domain is bound to IPv6 address pools **pool1** and **pool2**.
    
    ```
    [~Device] display domain isp1
    ```
    ```
    ------------------------------------------------------------------------------
      Domain-name                     : isp1
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
      IPUser-ReAuth-Time(second)      : 300
      mscg-name-portal-key            : -
      Portal-user-first-url-key       : -
      Ancp auto qos adapt             : Disable
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
      Multicast-profile ipv6          : -
      Max-multilist num               : 4
      Multicast-profile               : -
      IPv6-Pool-name                  : pool1
      IPv6-Pool-name                  : pool2
      Quota-out                     : Offline
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

* Device configuration file
  
  ```
  # 
  sysname Device                                                         
  #
  dhcpv6 duid 006735f300188253a56a
  #
  radius-server group rd1
   radius-server authentication 10.6.55.55 1550 weight 0
   radius-server accounting 10.6.55.55 1551 weight 0
   radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
  #
  interface Virtual-Template1
   ppp authentication-mode chap
  #
  ipv6 prefix pre1 local
   prefix 2001:DB8::/64
  #
  ipv6 prefix pre2 delegation
   prefix 2001:DB8::/62 delegating-prefix-length 63
  #
  ipv6 pool pool1 bas local
  prefix pre1
  #
  ipv6 pool pool2 bas delegation
   prefix pre2
  dns-server 2001:db8:1::1
  #
  aaa
  authentication-scheme auth1
   authentication-mode radius
  accounting-scheme acct1
   accounting-mode radius
  #
  domain isp1
   authentication-scheme auth1
   accounting-scheme acct1
   radius-server group rd1
   ipv6-pool pool1
   ipv6-pool pool2
  #
  interface GigabitEthernet0/1/1.1
   ipv6 enable
   ipv6 address auto link-local
   user-vlan 1 20
   pppoe-server bind Virtual-Template 1 
   bas
   #
    access-type layer2-subscriber default-domain authentication isp1
   #
  #
  interface GigabitEthernet0/1/2
   ipv6 enable
   ipv6 address 2001:DB8::2 64 eui-64
   ipv6 address auto link-local
  #
  return
  ```