Example for Configuring User Address Assignment Through a Local Address Pool
============================================================================

This section provides an example for configuring a local address pool to assign IPv4 addresses to users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373812__fig_dc_ne_ipv4_address_cfg_006601), it is required that a local address pool be configured to assign addresses to access users and the following requirements be met:

* A local address pool is used to assign addresses to users in the domain **isp1**.
* The IP addresses in the address pool range from 10.10.10.3 to 10.10.10.100, and the gateway address is 10.10.10.2.
* The DNS server address is 10.20.20.1.
* The IP address of GE0/3/0 connecting the device to the DNS server is 10.20.20.2.

**Figure 1** User address assignment through a local address pool![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0.1, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001238682231.png)

#### Configuration Roadmap

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Access users include IPoE users and PPPoE users. The address assignment for IPoE and PPPoE users differs in the access mode. This section describes only the IPv4 address pool configurations. For details about the IPoE access configurations, see [Example for Configuring IPoE Access to a VPN (Web Authentication)](dc_ne_ipox_cfg_0084.html).

The configuration roadmap is as follows:

1. Configure a local address pool, including its gateway address, address range, and the DNS server address.
2. Configure a domain named **isp1** to which users belong, including the authentication and accounting modes.
3. Configure a BAS interface, including the user access mode.

#### Data Preparation

To complete the configuration, you need the following data:

* Name, address range, gateway address, and DNS server address of the address pool
* Name of the domain to which users belong
* Authentication and accounting schemes
* User authentication mode (RADIUS authentication)

#### Procedure

1. Configure a DHCPv4 server.
   
   
   
   # Configure an address pool.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] ip pool pool1 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool1] gateway 10.10.10.2 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] section 0 10.10.10.3 10.10.10.100
   ```
   ```
   [*HUAWEI-ip-pool-pool1] dns-server 10.20.20.1
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] quit
   ```
   
   # Configure an authentication mode in the authentication scheme view.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] authentication-scheme clcl
   ```
   ```
   [*HUAWEI-aaa-authen-clcl] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-clcl] commit
   ```
   ```
   [~HUAWEI-aaa-authen-clcl] quit
   ```
   
   # Configure an accounting mode in the accounting scheme view.
   
   ```
   [~HUAWEI-aaa] accounting-scheme ccll
   ```
   ```
   [*HUAWEI-aaa-accounting-ccll] accounting-mode none
   ```
   ```
   [*HUAWEI-aaa-accounting-ccll] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-ccll] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~HUAWEI-aaa] radius-server group rd
   ```
   ```
   [*HUAWEI-radius-rd] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*HUAWEI-radius-rd] radius-server accounting 10.7.66.66 1813
   ```
   ```
   [*HUAWEI-radius-rd] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-radius-rd] radius-server retransmit 2
   ```
   ```
   [*HUAWEI-radius-rd] commit
   ```
   ```
   [~HUAWEI-radius-rd] quit
   ```
   
   # Configure a domain named **isp1**.
   
   ```
   [~HUAWEI-aaa] domain isp1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] authentication-scheme clcl
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] accounting-scheme ccll
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] radius-server group rd
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] user-vlan 1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-vlan-1-1] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-bas] access-type layer2-subscriber
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-bas] authentication-method bind
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-bas] default-domain authentication isp1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1-bas] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1-bas] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] quit
   ```
   # Configure an IP address for GE0/3/0 connecting the device to the DNS server.
   ```
   [~HUAWEI] interface GigabitEthernet 0/3/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/3/0] ip address 10.20.20.2 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/3/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/3/0] quit
   ```
2. Verify the configuration.
   
   
   
   # Check the configuration of the local address pool **pool1**.
   
   ```
   [~HUAWEI] display ip pool name pool1
   ```
   ```
     Pool-Name      : pool1
     Pool-No        : 19 
     Pool-constant-index :- 
     Lease          : 3 Days 0 Hours 0 Minutes
     Frameip-Lease-Manage: disable
     NetBois Type   : N-Node
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
     Gateway        : 10.10.10.2      Mask             : 255.255.255.0
     Vpn instance   : --              Unnumbered gateway: -
     Profile-Name   : -               Server-Name      : -
     Total Idle     : 198             Have Dhcp IP     : 1
     Timeouts       : 0
     Timeout Count  :0               Sub Option Count:0
     Option Count   :0               Force-reply Count:0
     Auto-Blocked Times: 0            IP Allocation Failures: 0
     Codes: CFLCT(conflicted)       Wait-Request-Time: --
     IP Loose Check : 0
   
     ------------------------------------------------------------------------------------------------
     ID           start             end total  used  idle CFLCT disable reserved static-bind  delayed
     -------------------------------------------------------------------------------------------------
      0      10.10.10.3    10.10.10.100    98     0    98     0       0        0           0        0
     -------------------------------------------------------------------------------------------------
   ```
   
   # Check the configuration of the domain **isp1**.
   
   ```
   [~HUAWEI] display domain isp1
   ```
   ```
    ------------------------------------------------------------------------------
     Domain-name                     : isp1
     Domain-state                    : Active
     Authentication-scheme-name      : default0
     Accounting-scheme-name          : default0
     Authorization-scheme-name       :
     Primary-DNS-IP-address          : -
     Second-DNS-IP-address           : -
     Web-server-URL-parameter        : No
     Portal-server-URL-parameter     : No
     Primary-NBNS-IP-address         : -
     Second-NBNS-IP-address          : -
     User-group-name                 : -
     Idle-data-attribute (time, flow) : 0,60
     Install-BOD-Count               : 0
     Report-VSM-User-Count           : 0
     Value-added-service             :  default
     User-access-limit               : 279552
     Online-number                   : 0
     Web-IP-address                  : -
     Web-URL                         : -
     Portal-server-IP                : -
     Portal-URL                      : -
     Portal-force-times              : 2
     PPPoE-user-URL                  : Disable
     IPUser-ReAuth-Time (second) : 300
     mscg-name-portal-key            : -
     Portal-user-first-url-key       : -
     Ancp auto qos adapt             : Disable
     Service-type                    : STB
     RADIUS-server-template          : -
     Two-acct-template               : -
     HWTACACS-server-template        : -
     Bill Flow                       : Disable
     Tunnel-acct-2867                : Disabled
     Flow Statistic:
     Flow-Statistic-Up               : Yes
     Flow-Statistic-Down             : Yes
     Source-IP-route                 : Disable
     IP-warning-threshold            : -
     Multicast Forwarding            : Yes
     Multicast Virtual               : No
     Max-multilist num               : 4
     Multicast-profile               : -
     IP-address-pool-name            : pool1
     Quota-out                     : Offline
     ------------------------------------------------------------------------------
   ```

#### Configuration Files

* Configuration files
  ```
  #
   sysname HUAWEI
  
  #
  ip pool pool1 bas local
   gateway 10.10.10.2 255.255.255.0
   section 0 10.10.10.3 10.10.10.100
   dns-server 10.20.20.1
  #
  radius-server group rd                                                       
   radius-server authentication 10.7.66.66 1812 weight 0                                             
   radius-server accounting 10.7.66.66 1813 weight 0                                                        
   radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
   radius-server retransmit 2                                                    
  # 
  aaa
   authentication-scheme clcl
    authentication-mode radius
   #
   accounting-scheme ccll
    accounting-mode none
   authorization-scheme default
   #
   domain isp1
    authentication-scheme clcl
    accounting-scheme ccll
    radius-server group rd
    ip-pool pool1
   #
  interface GigabitEthernet0/1/0.1
   statistic enable
   user-vlan 1
   bas
   #
    access-type layer2-subscriber default-domain authentication isp1
    authentication-method bind
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.20.20.2 255.255.255.0
  #
  return
  ```