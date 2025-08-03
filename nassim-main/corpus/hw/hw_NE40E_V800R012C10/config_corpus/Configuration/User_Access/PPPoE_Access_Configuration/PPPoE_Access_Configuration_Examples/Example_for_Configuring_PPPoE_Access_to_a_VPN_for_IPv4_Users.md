Example for Configuring PPPoE Access to a VPN for IPv4 Users
============================================================

This section provides an example for configuring PPPoE access to a VPN for IPv4 users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0281506197__fig_dc_ne_pppox_cfg_018801), the requirements are as follows:

* The user belongs to domain **isp1** and accesses the VPN through GE 0/1/1.1 on DeviceA in PPPoE mode.
* RADIUS authentication and accounting are used.
* The RADIUS server address is 192.168.7.249. The authentication port number is 1645, and the accounting port number is 1646. RADIUS+1.1 is used, with the key being **it-is-my-secret1**.
* The DNS server address is 192.168.7.252.

**Figure 1** Network diagram of configuring PPPoE access to a VPN for IPv4 users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and interface2 in this example represent GE 0/1/1.1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0281508108.png)

#### Configuration Roadmap

1. Configure a virtual template.
2. Configure AAA schemes.
3. Configure a VPN instance.
4. Configure a RADIUS server group.
5. Configure an IPv4 address pool.
6. Configure a domain and bind the VPN instance to the domain.
7. Configure a user-VLAN sub-interface and bind the virtual template to the sub-interface.
8. Configure a BAS interface.

#### Data Preparation

* Virtual template number
* Authentication and accounting schemes and their names
* RADIUS server group name and RADIUS server address
* DNS server address
* User access domain name
* BAS interface parameters

#### Procedure

1. Configure a virtual template.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [~DeviceA] interface virtual-template 1
   ```
   ```
   [*DeviceA-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*DeviceA-Virtual-Template1] commit
   ```
   ```
   [~DeviceA-Virtual-Template1] quit
   ```
2. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] authentication-scheme acct1
   ```
   ```
   [*DeviceA-aaa-authen-acct1] authentication-mode radius
   ```
   ```
   [*DeviceA-aaa-authen-acct1] commit
   ```
   ```
   [~DeviceA-aaa-authen-acct1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~DeviceA-aaa] accounting-scheme acct1
   ```
   ```
   [*DeviceA-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*DeviceA-aaa-accounting-acct1] commit
   ```
   ```
   [~DeviceA-aaa-accounting-acct1] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
3. Configure a VPN instance.
   
   
   ```
   [~DeviceA] ip vpn-instance isp1
   ```
   ```
   [*DeviceA-vpn-instance-isp1] ipv4-family
   ```
   ```
   [*DeviceA-vpn-instance-isp1-af-ipv4] route-distinguisher 100:2
   ```
   ```
   [*DeviceA-vpn-instance-isp1-af-ipv4] vpn-target 100:100 export-extcommunity
   ```
   ```
   [*DeviceA-vpn-instance-isp1-af-ipv4] vpn-target 100:100 import-extcommunity
   ```
   ```
   [*DeviceA-vpn-instance-isp1-af-ipv4] commit
   ```
   ```
   [~DeviceA-vpn-instance-isp1-af-ipv4] quit
   ```
   ```
   [~DeviceA-vpn-instance-isp1] quit
   ```
4. Configure a RADIUS server group.
   
   
   ```
   [~DeviceA] radius-server group rd1
   ```
   ```
   [*DeviceA-radius-rd1] radius-server authentication 192.168.7.249 1645
   ```
   ```
   [*DeviceA-radius-rd1] radius-server accounting 192.168.7.249 1646
   ```
   ```
   [*DeviceA-radius-rd1] commit
   ```
   ```
   [~DeviceA-radius-rd1] radius-server type plus11
   ```
   ```
   [~DeviceA-radius-rd1] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*DeviceA-radius-rd1] commit
   ```
   ```
   [~DeviceA-radius-rd1] quit
   ```
5. Configure an IPv4 address pool.
   
   
   ```
   [~DeviceA] ip pool pool1 bas local
   ```
   ```
   [*DeviceA-ip-pool-pool1] gateway 10.82.0.1 255.255.255.0
   ```
   ```
   [*DeviceA-ip-pool-pool1] commit
   ```
   ```
   [~DeviceA-ip-pool-pool1] section 0 10.82.0.2 10.82.0.200
   ```
   ```
   [~DeviceA-ip-pool-pool1] dns-server 192.168.7.252
   ```
   ```
   [*DeviceA-ip-pool-pool1] commit
   ```
   ```
   [~DeviceA-ip-pool-pool1] vpn-instance isp1
   ```
   ```
   [*DeviceA-ip-pool-pool1] commit
   ```
   ```
   [~DeviceA-ip-pool-pool1] quit
   ```
6. Configure a domain and bind the VPN instance to the domain.
   
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] domain isp1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] authentication-scheme acct1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] commit
   ```
   ```
   [~DeviceA-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [~DeviceA-aaa-domain-isp1] vpn-instance isp1
   ```
   ```
   [~DeviceA-aaa-domain-isp1] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
7. Configure a user-VLAN sub-interface and bind the virtual template to the sub-interface.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1.1] user-vlan 1 2
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1.1-vlan-1-2] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1.1] pppoe-server bind virtual-template 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1.1] commit
   ```
8. Configure a BAS interface.
   
   
   ```
   [~DeviceA-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1.1-bas] authentication-method ppp
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1.1-bas] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1.1-bas] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1.1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, the user goes online using a username carrying the domain name **isp1**. Therefore, you do not need to bind the BAS interface to an authentication domain. If a user goes online with a username that does not carry a domain name, you must specify an authentication domain on the BAS interface.
9. Verify the configuration. 
   
   
   
   # Check information about the address pool named **pool1**. The command output shows that the gateway address is 10.82.0.1, the addresses in the pool range from 10.82.0.2 to 10.82.0.200, and the DNS server address is 192.168.7.252.
   
   ```
   [~DeviceA] display ip pool name pool1
   2020-01-23 17:38:40.529
     ------------------------------------------------------------------------------
     Pool-Name      : pool1
     Pool-No        : 270
     Pool-constant-index: 270
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
    
     DNS1         :192.168.7.252
     Position       : Local           Status           : Unlocked
     RUI-Flag       : -
     Attribute      : Private
     Gateway        : 10.82.0.1       Mask             : 255.255.255.0
     Vpn instance   : isp1            Unnumbered gateway: -
     Profile-Name   : -               Server-Name     : -
     Total Idle     : 199             Have Dhcp IP     : 1
     Timeouts       : 0
     Timeout Count  : 0               Sub Option Count : 0
     Option Count   : 0               Force-reply Count: 0
     Auto-Blocked Times: 0            IP Allocation Failures: 0
     Codes: CFLCT(conflicted)         Wait-Request-Time: --
     IP Loose Check : 0               Blocked Times : 0
     -------------------------------------------------------------------------------------------------------
     ID           start             end   total    used    idle   CFLCT disable reserved static-bind delayed
     ------------------------------------------------------------------------------------------------------
     0       10.82.0.2     10.82.0.200     199       0     199       0       0        0           0       0
     -------------------------------------------------------------------------------------------------------
   ```
   
   # Check the configuration of the domain named **isp1**. The command output shows that the address pool named **pool1** is bound to the domain **isp1**.
   
   ```
   [~DeviceA] display domain isp1
   2020-01-23 17:40:01.532
   ------------------------------------------------------------------------------
     Domain-name                     : isp1
     Domain-state                    : Active
     Authentication-scheme-name      : none
     Accounting-scheme-name          : none
     Authorization-scheme-name       : -
     Vpn-instance-name               : isp1
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
     User-access-limit               : 1045504
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
     IP-address-pool-name            : pool1
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
     Session-group function          : Disable
     DAA Direction                   : both
     Session Volumequota apply direction: both
     Soap-server group               : -
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

```
#
 sysname DeviceA
#
interface Virtual-Template1
 ppp authentication-mode chap
#
interface GigabitEthernet0/1/1
#
interface GigabitEthernet0/1/1.1
 pppoe-server bind virtual-template 1
 user-vlan 1 2
 bas
 access-type layer2-subscriber
#
ip vpn-instance isp1
 ipv4-family
  route-distinguisher 100:2
  vpn-target 100:100 export-extcommunity
  vpn-target 100:100 import-extcommunity
# 
interface GigabitEthernet0/1/2
 ip address 10.1.1.1 255.255.255.0
#
radius-server group rd1
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server shared-key-cipher %^%#clY:%[]x='-RMNJus[s/VJ:3YBq3<..|.{'xgbp+%^%
 radius-server type plus11
 radius-server traffic-unit kbyte
#
ip pool pool1 bas local
 vpn-instance isp1
 gateway 10.82.0.1 255.255.255.0
 section 0 10.82.0.2 10.82.0.200
 dns-server 192.168.7.252
#
aaa
 #
 authentication-scheme acct1
  authentication-mode radius
 #
 accounting-scheme acct1
  accounting-mode radius
#
 domain default0
 domain default1
 domain default_admin
#
 domain isp1
  authentication-scheme acct1
  accounting-scheme acct1
  radius-server group rd1
  ip-pool pool1
  vpn-instance isp1
#
return
```