Example for Configuring PPPoE Access for IPv4 Users
===================================================

This section provides an example for configuring PPPoEoVLAN access for IPv4 users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374120__fig_dc_ne_pppoe_cfg_001301), the requirements are as follows:

* The users belong to the domain **isp1** and use PPPoEoVLAN to go online through GE 0/1/2.1 on the Router. The LAN switch marks the priorities of user packets from VLAN1 and VLAN2.
* RADIUS authentication and accounting are used.
* The IP address of the RADIUS server is 192.168.7.249. The authentication and accounting port numbers are 1645 and 1646, respectively. RADIUS+1.1 is used, with the key being **YsHsjx\_202206**.
* The IP address of the DNS server is 192.168.7.252.
* The network-side interface is GE 0/1/1.

**Figure 1** Networking for configuring PPPoEoVLAN access for IPv4 users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2.1, respectively.


  
![](images/fig_dc_ne_pppoe_cfg_001301.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VT.
2. Configure AAA schemes.
3. Configure a RADIUS server group.
4. Configure an IPv4 address pool.
5. Configure a domain.
6. Bind the virtual template to a sub-interface.
7. Configure a BAS interface.
8. Configure OSPF.
9. Configure a loopback interface.

#### Data Preparation

* Virtual template number
* Authentication and accounting schemes and their names
* RADIUS server group name and server addresses
* DNS server address
* User domain name
* BAS interface parameters

#### Procedure

1. Configure a VT.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface virtual-template 1
   ```
   ```
   [*HUAWEI-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*HUAWEI-Virtual-Template1] quit
   ```
   ```
   [*HUAWEI] commit
   ```
2. Configure an authentication scheme.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] quit
   ```
   ```
   [*HUAWEI-aaa] quit
   ```
   ```
   [*HUAWEI] commit
   ```
3. Configure an accounting scheme.
   
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] quit
   ```
   ```
   [*HUAWEI-aaa] quit
   ```
   ```
   [*HUAWEI] commit
   ```
4. Configure a RADIUS server group.
   
   
   ```
   [~HUAWEI] radius-server group rd1
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server authentication 192.168.7.249 1645
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server accounting 192.168.7.249 1646
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] radius-server type plus11
   ```
   ```
   [~HUAWEI-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] quit
   ```
5. Configure an IPv4 address pool.
   
   
   ```
   [~HUAWEI] ip pool pool1 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool1] gateway 10.82.0.1 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] section 0 10.82.0.2 10.82.0.200
   ```
   ```
   [~HUAWEI-ip-pool-pool1] dns-server 192.168.7.252
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] quit
   ```
6. Configure a domain named **isp1**.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
7. Configure user VLANs on the sub-interface and bind the virtual template to it.
   
   
   
   # Configure user VLANs and bind the virtual template.
   
   ```
   [~HUAWEI] interface gigabitethernet 0/1/2.1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] user-vlan 1 2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1-vlan-1-2] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] pppoe-server bind virtual-template 1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1] quit
   ```
   ```
   [*HUAWEI] commit
   ```
8. Configure a BAS interface.
   
   
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] bas
   [~HUAWEI-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain authentication isp1
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] commit
   [~HUAWEI-GigabitEthernet0/1/2.1-bas] quit
   [~HUAWEI-GigabitEthernet0/1/2.1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, users go online with the domain name **isp1** carried in the usernames. Therefore, the BAS interface does not need to have any authentication domain configured. If users go online with no domain name carried in the usernames, you must specify an authentication domain on the BAS interface.
9. Configure OSPF.
   
   
   ```
   [~HUAWEI] ospf 1
   ```
   ```
   [*HUAWEI-ospf-1] import-route unr
   ```
   ```
   [*HUAWEI-ospf-1] area 0.0.0.0
   ```
   ```
   [*HUAWEI-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*HUAWEI-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~HUAWEI-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~HUAWEI-ospf-1] quit
   ```
10. Configure a loopback interface.
    
    
    ```
    [~HUAWEI] interface loopback1
    ```
    ```
    [*HUAWEI-LoopBack1] ip address 10.1.2.2 255.255.255.255
    ```
    ```
    [*HUAWEI-LoopBack1] ospf enable 1 area 0.0.0.0
    ```
    ```
    [*HUAWEI-LoopBack1] commit
    ```
    ```
    [~HUAWEI-LoopBack1] quit
    ```
    ```
    [~HUAWEI] quit
    ```
11. Verify the configuration.
    
    
    
    # Check information about the address pool named **pool1**. The command output shows that the gateway address is 10.82.0.1, the addresses in the pool range from 10.82.0.2 to 10.82.0.200, and the DNS server address is 192.168.7.252.
    
    ```
    <HUAWEI> display ip pool name pool1
    ```
    ```
      Pool-Name      : pool1
      Pool-No        : 19 
      Pool-constant-index :- 
      Lease          : 3 Days 0 Hours 0 Minutes
      Frameip-Lease-Manage: disable
      NetBios Type   : N-Node
      Auto recycle   : 30
      Option 3       : Enable
      DNS-Suffix     : -
      Dom-Search-List0 : -
      Dom-Search-List1 : -
      Dom-Search-List2 : -
      Dom-Search-List3 : -
      Option-Code 125 : enterprise-code : 2011  string: -
      Position       : Local           Status           : Unlocked
      RUI-Flag        : -
      Attribute       : Private
      Gateway        : 10.82.0.1       Mask             : 255.255.255.0
      Vpn instance   : --              Unnumbered gateway: -
      Profile-Name   : -               Server-Name      : -
      Total Idle     : 198             Have Dhcp IP     : 1
      Timeouts       : 0
      Timeout Count  :0               Sub Option Count:0
      Option Count   :0               Force-reply Count:0
      Auto-Blocked Times: 0            IP Allocation Failures: 0
      Codes: CFLCT(conflicted)       Wait-Request-Time: --
      IP Loose Check : 0
    ```
    ```
      --------------------------------------------------------------------------------------
      ID           start             end         total  used  idle    CFLCT disable reserved static-bind delayed
      -----------------------------------------------------------------------------------------------------------    
       0           10.82.0.2       10.82.0.200    199     0    199     0       0           0           0       0
      ----------------------------------------------------------------------------------------------------------- 
    ```
    
    # Check information about the domain named **isp1**. The command output shows that the address pool named **pool1** is bound to the domain.
    
    ```
    <HUAWEI> display domain isp1
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
      IP-address-pool-name            : pool1
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

```
#
sysname HUAWEI
#
radius-server group rd1
radius-server authentication 192.168.7.249 1645 weight 0
radius-server accounting 192.168.7.249 1646 weight 0
radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
radius-server type plus11
#
interface Virtual-Template1
 ppp authentication-mode chap
#
interface GigabitEthernet0/1/2
#
interface GigabitEthernet0/1/2.1
 pppoe-server bind virtual-template 1
 user-vlan 1 2
 bas
 access-type layer2-subscriber default-domain authentication isp1 
#
interface GigabitEthernet0/1/1
 ip address 192.168.7.1 255.255.255.0
#
ospf 1
 import-route unr
 area 0.0.0.0
 network 10.1.2.0 0.0.0.255
#
interface LoopBack1
 ip address 10.1.2.2 255.255.255.255
 ospf enable 1 area 0.0.0.0
#
ip pool pool1 bas local
 gateway 10.82.0.1 255.255.255.0
 section 0 10.82.0.2 10.82.0.200
 dns-server 192.168.7.252
#
aaa
 authentication-scheme auth1
 accounting-scheme acct1
 domain default0
 domain default1
 domain default_admin
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ip-pool pool1
#
return
```