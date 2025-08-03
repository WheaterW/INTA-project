Example for Configuring IPoE Dual-Stack Access (Web Authentication)
===================================================================

This section provides an example for configuring IPoE dual-stack user access through web authentication. When an IPoE dual-stack user connects to a BRAS, the BRAS implements RADIUS authentication and accounting, assigns an IPv4 address from the local address pool to the user, and assigns an IPv6 address through ND to the user. This allows the user to access the Internet.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374031__fig_dc_ne_ipox_cfg_007201), the user belong to the domain **isp5** and uses the dual-stack access mode. The Device adopts RADIUS authentication and accounting, assigns an IPv4 address from a local address pool to the user, and assigns an IPv6 address to the user through ND. Web authentication is used. After passing web authentication, the user accesses the Internet through interface2 on the Device.

**Figure 1** Configuring IPoE dual-stack access (web authentication)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_ne_ipox_cfg_007201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure AAA schemes.
2. Configure an interface IP address for the device to receive portal packets from the web authentication server.
3. Configure a web authentication server. (In this example, the web server and web authentication server are deployed on the same device.)
4. Configure a RADIUS server group.
5. Configure a user password.
6. Configure ACLs to allow the user to access only the web server address before web authentication succeeds.
7. Configure a DUID for the device.
8. Configure a local IPv4 address pool.
9. Configure a local IPv6 prefix pool.
10. Configure a local IPv6 address pool and bind the prefix pool to the local IPv6 address pool.
11. Configure a pre-authentication domain and an authentication domain for web authentication.
12. Configure a BAS interface and an upstream interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP address and port numbers of the RADIUS authentication and accounting server
* Local prefix pool name
* IPv6 prefix to be assigned/prefix length
* Local address pool names
* Domain names

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
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
   [*Device-aaa-authen-auth5] commit
   ```
   ```
   [~Device-aaa-authen-auth5] quit
   ```
   ```
   [~Device-aaa] authentication-scheme none
   ```
   ```
   [~Device-aaa-authen-none] authentication-mode none
   ```
   ```
   [*Device-aaa-authen-none] commit
   ```
   ```
   [~Device-aaa-authen-none] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~Device-aaa] accounting-scheme acct5
   ```
   ```
   [*Device-aaa-accounting-acct5] accounting-mode radius
   ```
   ```
   [*Device-aaa-accounting-acct5] commit
   ```
   ```
   [~Device-aaa-accounting-acct5] quit
   ```
   ```
   [~Device-aaa] accounting-scheme none
   ```
   ```
   [*Device-aaa-accounting-none] accounting-mode none
   ```
   ```
   [*Device-aaa-accounting-none] commit
   ```
   ```
   [~Device-aaa-accounting-none] quit
   ```
   ```
   [~Device-aaa] quit
   ```
2. Configure an IP address used by the device to receive portal packets from the web authentication server.
   
   
   ```
   [~Device] interface LoopBack 0
   ```
   ```
   [*Device-LoopBack0] ipv6 enable
   ```
   ```
   [*Device-LoopBack0] ip address 10.6.55.1 32
   ```
   ```
   [*Device-LoopBack0] ipv6 address 2001:db8:1::3 128
   ```
   ```
   [*Device-LoopBack0] ipv6 address auto link-local
   ```
   ```
   [*Device-LoopBack0] commit
   ```
   ```
   [~Device-LoopBack0] quit
   ```
   ```
   [~Device] web-auth-server source-ip 10.6.55.1
   ```
   ```
   [~Device] web-auth-server source-ipv6 2001:db8:1::3
   ```
3. Configure a web authentication server.
   
   
   ```
   [~Device] web-auth-server enable
   ```
   ```
   [~Device] web-auth-server source interface LoopBack 0
   ```
   ```
   [~Device] web-auth-server 10.6.55.56 key cipher YsHsjx_202206
   ```
   ```
   [~Device] web-auth-server 2001:db8:1::2 key cipher YsHsjx_202206 
   ```
4. Configure a RADIUS server group.
   
   
   ```
   [~Device] radius-server group rd5
   ```
   ```
   [*Device-radius-rd5] radius-server authentication 10.6.55.55 1645
   ```
   ```
   [*Device-radius-rd5] radius-server accounting 10.6.55.55 1646
   ```
   ```
   [*Device-radius-rd5] commit
   ```
   ```
   [~Device-radius-rd5] radius-server type standard
   ```
   ```
   [~Device-radius-rd5] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*Device-radius-rd5] commit
   ```
   ```
   [~Device-radius-rd5] quit
   ```
5. Configure the IPoE user password.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] default-password cipher YsHsjx_202206
   ```
   ```
   [*Device-aaa] commit
   ```
   ```
   [~Device-aaa] quit
   ```
6. Configure ACLs to allow the user to access only the web server address before web authentication succeeds.
   
   
   
   # Configure a user group.
   
   ```
   [~Device] user-group huawei
   ```
   
   # Configure an ACL numbered 6000 to permit the traffic between the user group **huawei** and the web authentication server and between the user group **huawei** and the DNS server.
   
   ```
   [~Device] acl number 6000
   ```
   ```
   [*Device-acl-ucl-6000] rule permit ip source user-group huawei destination ip-address 10.6.55.56 0.0.0.255
   ```
   ```
   [*Device-acl-ucl-6000] rule permit ip source ip-address 10.6.55.56 0.0.0.255 destination user-group huawei
   ```
   ```
   [*Device-acl-ucl-6000] rule permit ip source user-group huawei destination ip-address 10.10.10.1 0.0.0.255
   ```
   ```
   [*Device-acl-ucl-6000] rule permit ip source ip-address 10.10.10.1 0.0.0.255 destination user-group huawei
   ```
   ```
   [*Device-acl-ucl-6000] commit
   ```
   ```
   [~Device-acl-ucl-6000] quit
   ```
   ```
   [~Device] acl ipv6 number 6000
   ```
   ```
   [*Device-acl6-ucl-6000] rule permit ipv6 source user-group huawei destination ipv6-address 2001:db8:1::2/128
   ```
   ```
   [*Device-acl6-ucl-6000] rule permit ipv6 source ipv6-address 2001:db8:1::2/128 destination user-group huawei
   ```
   ```
   [*Device-acl6-ucl-6000] rule permit ipv6 source user-group huawei destination ipv6-address 2001:db8:1::1/128
   ```
   ```
   [*Device-acl6-ucl-6000] rule permit ipv6 source ipv6-address 2001:db8:1::1/128 destination user-group huawei
   ```
   ```
   [*Device-acl6-ucl-6000] commit
   ```
   ```
   [~Device-acl6-ucl-6000] quit
   ```
   
   # Configure an ACL numbered 6001 and create ACL rules to match TCP packets from the user group **huawei** and with a destination port of www or 8080, so that HTTP redirect can be performed for the packets.
   
   ```
   [~Device] acl number 6001 
   ```
   ```
   [*Device-acl-ucl-6001] rule permit tcp source user-group huawei destination-port eq www
   ```
   ```
   [*Device-acl-ucl-6001] rule permit tcp source user-group huawei destination-port eq 8080
   ```
   ```
   [*Device-acl-ucl-6001] commit
   ```
   ```
   [~Device-acl-ucl-6001] quit
   ```
   ```
   [~Device] acl ipv6 number 6001
   ```
   ```
   [*Device-acl6-ucl-6001] rule permit tcp source user-group huawei destination-port eq www
   ```
   ```
   [*Device-acl6-ucl-6001] rule permit tcp source user-group huawei destination-port eq 8080
   ```
   ```
   [*Device-acl6-ucl-6001] commit
   ```
   ```
   [~Device-acl6-ucl-6001] quit
   ```
   
   # Configure an ACL numbered 6002 to deny all the traffic originating from the user group **huawei**.
   
   ```
   [~Device] acl 6002 match-order auto
   ```
   ```
   [*Device-acl-ucl-6002] rule permit ip source ip-address any destination user-group huawei
   ```
   ```
   [*Device-acl-ucl-6002] rule deny ip source user-group huawei destination ip-address any
   ```
   ```
   [*Device-acl-ucl-6002] commit
   ```
   ```
   [~Device-acl-ucl-6002] quit
   ```
   ```
   [~Device] acl ipv6 number 6002
   ```
   ```
   [*Device-acl6-ucl-6002] rule permit ipv6 source ipv6-address any destination user-group huawei
   ```
   ```
   [*Device-acl6-ucl-6002] rule deny ipv6 source user-group huawei destination ipv6-address any
   ```
   ```
   [*Device-acl6-ucl-6002] commit
   ```
   ```
   [~Device-acl6-ucl-6002] quit
   ```
   
   # Configure traffic classifiers.
   
   ```
   [~Device] traffic classifier c1
   ```
   ```
   [*Device-classifier-c1] if-match acl 6000
   ```
   ```
   [*Device-classifier-c1] if-match ipv6 acl 6000
   ```
   ```
   [*Device-classifier-c1] commit
   ```
   ```
   [~Device-classifier-c1] quit
   ```
   ```
   [~Device] traffic classifier c2
   ```
   ```
   [*Device-classifier-c2] if-match acl 6001
   ```
   ```
   [*Device-classifier-c2] if-match ipv6 acl 6001
   ```
   ```
   [*Device-classifier-c2] commit
   ```
   ```
   [~Device-classifier-c2] quit
   ```
   ```
   [~Device] traffic classifier c3
   ```
   ```
   [*Device-classifier-c3] if-match acl 6002
   ```
   ```
   [*Device-classifier-c3] if-match ipv6 acl 6002
   ```
   ```
   [*Device-classifier-c3] commit
   ```
   ```
   [~Device-classifier-c3] quit
   ```
   
   # Configure traffic behaviors.
   
   ```
   [~Device] traffic behavior b1
   ```
   ```
   [*Device-behavior-b1] permit
   ```
   ```
   [*Device-behavior-b1] commit
   ```
   ```
   [~Device-behavior-b1] quit
   ```
   ```
   [~Device] traffic behavior b2
   ```
   ```
   [*Device-behavior-b2] http-redirect
   ```
   ```
   [*Device-behavior-b2] commit
   ```
   ```
   [~Device-behavior-b2] quit
   ```
   ```
   [~Device] traffic behavior b3
   ```
   ```
   [*Device-behavior-b3] deny
   ```
   ```
   [*Device-behavior-b3] commit
   ```
   ```
   [~Device-behavior-b3] quit
   ```
   
   # Configure a traffic policy.
   
   ```
   [~Device] traffic policy policy
   ```
   ```
   [*Device-trafficpolicy-policy] classifier c1 behavior b1
   ```
   ```
   [*Device-trafficpolicy-policy] classifier c2 behavior b2
   ```
   ```
   [*Device-trafficpolicy-policy] classifier c3 behavior b3
   ```
   ```
   [*Device-trafficpolicy-policy] commit
   ```
   ```
   [~Device-trafficpolicy-policy] quit
   ```
   
   # Apply the traffic policy globally.
   
   ```
   [~Device] traffic-policy policy inbound
   ```
7. Configure a DUID for the device.
   
   
   ```
   [~Device] dhcpv6 duid 12345678
   ```
   ```
   [*Device] commit
   ```
8. Configure a user-side local IPv4 address pool.
   
   
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
   [~Device-ip-pool-pool2] dns-server 10.10.10.1
   ```
   ```
   [*Device-ip-pool-pool2] commit
   ```
   ```
   [~Device-ip-pool-pool2] quit
   ```
9. Configure a delegation prefix pool for IPv6 users.
   
   
   ```
   [~Device] ipv6 prefix pre1 delegation
   ```
   ```
   [*Device-ipv6-prefix-pre1] prefix 2001:db8:3::/48
   ```
   ```
   [*Device-ipv6-prefix-pre1] slaac-unshare-only
   ```
   ```
   [*Device-ipv6-prefix-pre1] commit
   ```
   ```
   [~Device-ipv6-prefix-pre1] quit
   ```
10. Configure a delegation address pool for IPv6 users.
    
    
    ```
    [~Device] ipv6 pool pool1 bas delegation
    ```
    ```
    [*Device-ipv6-pool-pool1] prefix pre1
    ```
    ```
    [*Device-ipv6-pool-pool1] commit
    ```
    ```
    [~Device-ipv6-pool-pool1] dns-server 2001:db8:1::1
    ```
    ```
    [*Device-ipv6-pool-pool1] commit
    ```
    ```
    [~Device-ipv6-pool-pool1] quit
    ```
11. Configure domains.
    
    
    
    # Configure a pre-authentication domain named **domain1**.
    
    ```
    [~Device] aaa
    ```
    ```
    [~Device-aaa] domain domain1
    ```
    ```
    [*Device-aaa-domain-domain1] authentication-scheme none
    ```
    ```
    [*Device-aaa-domain-domain1] accounting-scheme none
    ```
    ```
    [*Device-aaa-domain-domain1] commit
    ```
    ```
    [~Device-aaa-domain-domain1] prefix-assign-mode unshared
    ```
    ```
    [~Device-aaa-domain-domain1] user-group huawei
    ```
    ```
    [~Device-aaa-domain-domain1] ip-pool pool2 
    ```
    ```
    [~Device-aaa-domain-domain1] ipv6-pool pool1
    ```
    ```
    [~Device-aaa-domain-domain1] web-server 10.6.55.56 2001:db8:1::2
    ```
    ```
    [~Device-aaa-domain-domain1] web-server url http://www.isp1.com
    ```
    ```
    [~Device-aaa-domain-domain1] web-server identical-url
    ```
    ```
    [~Device-aaa-domain-domain1] quit
    ```
    
    # Configure an authentication domain named **isp5**.
    
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
    [~Device-aaa-domain-isp5] quit
    ```
    ```
    [~Device-aaa] quit
    ```
12. Configure a BAS interface and an upstream interface.
    
    
    
    # Configure a BAS interface.
    
    ```
    [~Device] interface gigabitethernet 0/1/2
    ```
    ```
    [~Device-GigabitEthernet0/1/2] bas
    ```
    ```
    [~Device-GigabitEthernet0/1/2-bas] access-type layer2-subscriber default-domain pre-authentication domain1 authentication isp5
    ```
    ```
    [*Device-GigabitEthernet0/1/2-bas] authentication-method web
    ```
    ```
    [*Device-GigabitEthernet0/1/2-bas] authentication-method-ipv6 web
    [*Device-GigabitEthernet0/1/2-bas] commit
    [~Device-GigabitEthernet0/1/2-bas] ip-trigger
    [*Device-GigabitEthernet0/1/2-bas] arp-trigger
    [*Device-GigabitEthernet0/1/2-bas] commit
    [~Device-GigabitEthernet0/1/2-bas] ipv6-trigger
    [~Device-GigabitEthernet0/1/2-bas] nd-trigger
    [~Device-GigabitEthernet0/1/2-bas] quit
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In dual-stack user access scenarios, if a user attempts to go offline from the second stack and the stack in the Logout NTF packets received by the portal server is inconsistent with the user stack in authentication packets, the portal server may fail to find this user due to a user stack mismatch. In this case, perform the following operations:
    
    * If the portal server can identify users based on MAC addresses, run the **web-server redirect-key user-mac-address** *user-mac-address* [ **simple** [ **type1** ] | **cipher** { **aes128** [ **cbc** | **gcm** ] | **des** }] or **web-server redirect-key ap-mac-address** *ap-mac-key* [ **simple** [ **type1** ] | **cipher** { **aes128** [ **cbc** | **gcm** ] | **des** }] command to configure the keyword of the customized Portal attribute. For security purposes, you are advised not to use the DES encryption mode. If you need to use such a mode, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
    * If the portal server cannot identify users by MAC address, run the **ipoe-service-type** { **ipv4** | **ipv6** } command to configure the base protocol stack of IPoE dual-stack users.
    
    # Enable IPv6 on an interface.
    
    ```
    [~Device-GigabitEthernet0/1/2] ipv6 enable
    ```
    ```
    [*Device-GigabitEthernet0/1/2] ipv6 address auto link-local
    ```
    ```
    [*Device-GigabitEthernet0/1/2] commit
    ```
    ```
    [~Device-GigabitEthernet0/1/2] quit
    ```
    ```
    [~Device] quit
    ```
13. Verify the configuration.
    
    
    
    # Check information about the address pool named **pool2**. The command output shows that the IP address of **pool2**'s gateway is **10.10.10.2**, the IP address of the DNS server is **10.10.10.1**, and addresses in **pool2** range from **10.10.10.3** to **10.10.10.100**.
    
    ```
    <Device> display ip pool name pool2
    ```
    ```
      Pool-Name      : pool2
      Pool-No        : 0    Pool-constant-index :- 
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
    
      DNS1           : 10.10.10.1
      Position       : Local           Status           : Unlocked
      RUI-Flag       : -                                                            
      Attribute      : Private 
      Gateway        : 10.10.10.2      Mask             : 255.255.255.0
      Vpn instance   : --              Unnumbered gateway: - 
      Profile-Name   : -               Server-Name      : -
      Total Idle     : 199             Have Dhcp IP     : 1
      Timeouts       : 0                                                            
      Timeout Count  : 0               Sub Option Count : 0                         
      Option Count   : 0               Force-reply Count: 0                         
      Auto-Blocked Times: 0            IP Allocation Failures: 0 
      Codes: CFLCT(conflicted)         Wait-Request-Time: -- 
      IP Loose Check : 0 
      ------------------------------------------------------------------------------------------------
      ID           start             end total  used  idle CFLCT disable reserved static-bind delayed
      ------------------------------------------------------------------------------------------------
       0      10.10.10.3    10.10.10.100    98     0    98     0       0        0       0       0 
      ------------------------------------------------------------------------------------------------
    ```
    
    # Check information about the prefix pool named **pre1**. The command output shows that the prefix pool is a local prefix pool and the prefix address is **2001:db8:3::/64**.
    
    ```
    <Device> display ipv6 prefix pre1
    ```
    ```
     ------------------------------------------------------------------------------
     Prefix Name        : pre1                
     Prefix Index       : 3
     Prefix constant index: -  Prefix Type        : DELEGATION          
     Prefix Address     : 2001:DB8:3::                                       
     Prefix Length      : 48                  
     Link-Address       : -
     Reserved Type      : NONE   
     Valid Lifetime     : 3 Days 0 Hours 0 Minutes
     Preferred Lifetime : 2 Days 0 Hours 0 Minutes
     IfLocked           : Unlocked            
     Vpn instance       : -         PD Prefix Len      : 64
     PD Prefix/C-DUID   : -
     slaac-unshare-only : TRUE                
     pd-unshare-only    : FALSE               
     Free Prefix Count  : 65536
     Used Prefix Count  : 0
     Bound Prefix Count (Free): 0
     Bound Prefix Count (Used): 0
     Flexibly-Allocted Prefix Count: 0
     Reserved Prefix Count: 0
     Excluded Prefix Count: 0
     Radius Used Total  : 0  
     Radius Used Online : 0  
     Auto-Blocked Times : 0 
     IP Allocation Failures : 0 
     ------------------------------------------------------------------------------
    ```
    
    # Check information about the address pool named **pool1**. The command output shows that **pool1** is a local address pool and is bound to the local prefix pool **pre1**.
    
    ```
    <Device> display ipv6 pool pool1
    ```
    ```
     ----------------------------------------------------------------------
     Pool name          : pool1                            
     Pool No            : 2     
     Pool constant index :-   
     Pool type          : BAS DELEGATION  
     RUI-Flag           : -  
     Preference         : 255   
     Renew time         : 50    
     Rebind time        : 80    
     Status             : UNLOCKED  
     Refresh interval   : infinite
     Used by domain     : 2     
     Dhcpv6 Unicast     : disable
     Dhcpv6 rapid-commit: disable
     Dns list           : -
     Dns server master  : 2001:DB8:1::1 
     Dns server slave   : -
     AFTR name          : -   
     Wait-Request-Time  : -- 
     Warning Threshold  : 10  
     Warning Exhaust Switch: TRUE 
     ----------------------------------------------------------------------
     Prefix-Name                      Prefix-Type 
     ----------------------------------------------------------------------
     pre1                             DELEGATION
     ----------------------------------------------------------------------
    ```
    
    # Check information about the domain named **domain1**. The command output shows that the domain is bound to the IPv6 address pool named **pool1** and the IPv4 address pool named **pool2**.
    
    ```
    <Device> display domain domain1
    ```
    ```
    ------------------------------------------------------------------------------
      Domain-name                     : domain1
      Domain-state                    : Active
      Authentication-scheme-name      : auth5
      Accounting-scheme-name          : acct5
      Authorization-scheme-name       :
      Primary-DNS-IP-address          : -
      Second-DNS-IP-address           : -
      Web-server-URL-parameter        : No
      Slave Web-IP-address            : -   Slave Web-URL                   : -   Slave Web-auth-server           : -    Slave Web-auth-state            : -    Portal-server-URL-parameter     : No
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
      IPUser-ReAuth-Time              : 300
      mscg-name-portal-key            : -
      Portal-user-first-url-key       : -
      Ancp auto qos adapt             : Disable
      RADIUS-server-template          : rd5
      Two-acct-template               : -
      HWTACACS-server-template        : -
      Bill Flow                       : Disable
      Tunnel-acct-2867                : Disable
    
      Flow Statistic:
      Flow-Statistic-Up               : Yes
      Flow-Statistic-Down             : Yes
      Source-IP-route                 : Disable
      IP-warning-threshold            : -
      IPv6-warning-threshold          : -    Multicast Forwarding            : Yes
      Multicast Virtual               : No
      Max-multilist num               : 4
      Multicast-profile               : -
      Multicast-profile ipv6          : -   IP-address-pool-name            : pool2
      IPv6-Pool-name                  : pool1
      Quota-out                       : Offline
      Service-type                    : -   User-basic-service-ip-type      : -/-/-   PPP-ipv6-address-protocol       : Ndra   IPv6-information-protocol       : Stateless dhcpv6   IPv6-PPP-assign-interfaceid     : Disable   Trigger-packet-wait-delay       : 60s   Peer-backup                     : Enable       ------------------------------------------------------------------------------
    
    ```

#### Configuration Files

* Router configuration file
  
  ```
  #
  sysname Device
  #
  radius-server group rd5
   radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^%#
   radius-server authentication 10.6.55.55 1645 weight 0
   radius-server accounting 10.6.55.55 1646 weight 0
  #
  ip pool pool2 bas local
   gateway 10.10.10.2 255.255.255.0
   section 0 10.10.10.3 10.10.10.100
   dns-server 10.10.10.1
  #
  ipv6 prefix pre1 delegation
   prefix 2001:DB8:3::/48
   slaac-unshare-only
  #
  ipv6 pool pool1 bas delegation
   dns-server 2001:DB8:1::1
   prefix pre1
  # 
  user-group huawei
  #
  acl number 6000
   rule 5 permit ip source user-group huawei destination ip-address 10.6.55.0 0.0.0.255
   rule 10 permit ip source ip-address 10.6.55.0 0.0.0.255 destination user-group huawei
   rule 15 permit ip source user-group huawei destination ip-address 10.10.10.0 0.0.0.255
   rule 20 permit ip source ip-address 10.10.10.0 0.0.0.255 destination user-group huawei
  #
  acl number 6001 
   rule 5 permit tcp source user-group huawei destination-port eq www 
   rule 10 permit tcp source user-group huawei destination-port eq 8080
  #
  acl number 6002 match-order auto
   rule 5 permit ip source ip-address any destination user-group huawei
   rule 10 deny ip source user-group huawei destination ip-address any
  #
  acl ipv6 number 6000
   rule 5 permit ipv6 source user-group huawei destination ipv6-address 2001:DB8:1::2/128
   rule 10 permit ipv6 source ipv6-address 2001:DB8:1::2/128 destination user-group huawei
   rule 15 permit ipv6 source user-group huawei destination ipv6-address 2001:DB8:1::1/128
   rule 20 permit ipv6 source ipv6-address 2001:DB8:1::1/128 destination user-group huawei
  #
  acl ipv6 number 6001 
   rule 5 permit tcp source user-group huawei destination-port eq www 
   rule 10 permit tcp source user-group huawei destination-port eq 8080
  #
  acl ipv6 number 6002 
   rule 5 permit ipv6 source ipv6-address any destination user-group huawei 
   rule 10 deny ipv6 source user-group huawei destination ipv6-address any
  #
  dhcpv6 duid 12345678
  #
  traffic classifier c1 operator or
   if-match acl 6000 precedence 8
   if-match ipv6 acl 6000 precedence 21
  #
  traffic classifier c2 operator or
   if-match acl 6001 precedence 9
   if-match ipv6 acl 6001 precedence 23
  #
  traffic classifier c3 operator or
   if-match acl 6002 precedence 24
   if-match ipv6 acl 6002 precedence 25
  #
  traffic behavior b1
  #
  traffic behavior b2
   http-redirect 
  #
  traffic behavior b3
   deny
  #
  traffic policy policy
   share-mode
   classifier c1 behavior b1 precedence 1
   classifier c2 behavior b2 precedence 2
   classifier c3 behavior b3 precedence 3
  #
  aaa
   default-password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
   #
   authentication-scheme none
    authentication-mode none
   #
   authentication-scheme auth5
   #
   authorization-scheme default
   #
   accounting-scheme none
    accounting-mode none
   #
   accounting-scheme acct5
   #
   domain domain1
    authentication-scheme none
    accounting-scheme none
    prefix-assign-mode unshared
    ip-pool pool2
    ipv6-pool pool1
    user-group huawei
    web-server 10.6.55.56 2001:DB8:1::2
    web-server url http://www.isp1.com
    web-server identical-url
   #
   domain isp5
    authentication-scheme auth5
    accounting-scheme acct5
    radius-server group rd5
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address auto link-local
   bas
   #
    access-type layer2-subscriber default-domain pre-authentication domain1 authentication isp5
    authentication-method web
    authentication-method-ipv6 web
    ip-trigger
    arp-trigger
    ipv6-trigger 
    nd-trigger
   #
  #
  interface LoopBack0
   ipv6 enable
   ip address 10.6.55.1 255.255.255.255
   ipv6 address 2001:DB8:1::3/128
   ipv6 address auto link-local
  #
  web-auth-server enable
  web-auth-server source interface LoopBack0
  web-auth-server 10.6.55.56 port 50100 key cipher %^%#NCpW"R\7zYnsG8-}qo7*Ceh4*af%5)|*O>N{kOyP%^%# 
  web-auth-server 2001:DB8:1::2 port 50100 key cipher %^%#\39J9tmKl#+;)]1yEd@V#i(1Jeq"vO=9ka=-\qN<%^%# 
  #
  undo web-auth-server source-ip all
  web-auth-server source-ip 10.6.55.1
  #
  undo web-auth-server source-ipv6 all
  web-auth-server source-ipv6 2001:DB8:1::3
  #
  traffic-policy policy inbound
  #
  return
  ```