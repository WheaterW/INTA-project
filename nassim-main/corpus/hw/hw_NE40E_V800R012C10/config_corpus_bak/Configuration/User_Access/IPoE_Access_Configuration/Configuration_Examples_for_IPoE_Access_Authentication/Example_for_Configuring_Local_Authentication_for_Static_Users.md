Example for Configuring Local Authentication for Static Users
=============================================================

This section provides an example for configuring local authentication for static users. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374019__fig_dc_ne_ipox_cfg_000001), the networking requirements are as follows:

* A user accesses the network through GE 0/2/0.1 on the Router as a static user with an IP address of 172.30.0.8 and a MAC address of 00e0-fc12-3456.
* Local authentication is performed for the user.
* The system uses the MAC address carried in the user packet to generate a username.

**Figure 1** Configuring local authentication for static users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0.1, respectively.


  
![](images/fig_dc_ne_ipox_cfg_000001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an authentication scheme.
2. Configure an address pool.
3. Configure an authentication domain.
4. Configure a BAS interface and an upstream interface.
5. Configure a static user.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and local authentication mode
* Address pool name, gateway address, and DNS server address
* Domain name
* BAS interface parameters

#### Procedure

1. Configure an authentication scheme.
   
   
   ```
   <HUAWEI> system-view 
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] authentication-scheme local
   ```
   ```
   [*HUAWEI-aaa-authen-local] authentication-mode local
   ```
   ```
   [*HUAWEI-aaa-authen-local] commit
   ```
   ```
   [~HUAWEI-aaa-authen-local] quit
   ```
2. Configure the modes for generating usernames and passwords.
   
   
   ```
   [~HUAWEI-aaa] default-user-name include mac-address .
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] default-password cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
3. Configure a local account.
   
   
   ```
   [~HUAWEI] local-aaa-server
   ```
   ```
   [*HUAWEI-local-aaa-server] user 00e0-fc12-3456@isp1 password cipher YsHsjx_202206 authentication-type b
   ```
   ```
   [*HUAWEI-local-aaa-server] commit
   ```
   ```
   [~HUAWEI-local-aaa-server] quit
   ```
4. Configure an address pool.
   
   
   ```
   [~HUAWEI] ip pool pool1 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool1] gateway 172.30.0.1 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] section 0 172.30.0.2 172.30.0.200
   ```
   ```
   [~HUAWEI-ip-pool-pool1] excluded-ip-address 172.30.0.8
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] quit
   ```
5. Configure a domain.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] authentication-scheme local
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] accounting-scheme default0
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
6. Configure a BAS interface.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/2/0.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0.1] user-vlan 2005 qinq 510
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0.1-vlan-2005-2005-QinQ-510-510] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0.1] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0.1-bas] access-type layer2-subscriber
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0.1-bas] authentication-method bind
   [*HUAWEI-GigabitEthernet0/2/0.1-bas] default-domain authentication isp1
   [*HUAWEI-GigabitEthernet0/2/0.1-bas] commit
   [~HUAWEI-GigabitEthernet0/2/0.1-bas] ip-trigger
   [~HUAWEI-GigabitEthernet0/2/0.1-bas] arp-trigger
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0.1-bas] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0.1] quit
   ```
7. Configure a static user.
   
   
   ```
   [~HUAWEI] static-user 172.30.0.8 interface GigabitEthernet 0/2/0.1 vlan 2005 qinq 510 mac-address 00e0-fc12-3456 detect
   ```
8. Configure an upstream interface.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] ip address 192.168.8.1 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] commit
   ```
9. Verify the configuration.
   
   
   
   # After completing the configurations, run the [**display access-user domain**](cmdqueryname=display+access-user+domain) command to check user information in the domain. The command output shows that the user has gone online successfully.
   
   ```
   <HUAWEI> display access-user domain isp1
   ```
   ```
   ------------------------------------------------------------------------------
     UserID  Username                Interface      IP address       MAC
             IPv6 address
     ------------------------------------------------------------------------------
     20      00e0-fc12-3456@isp1     GE0/2/0.1      172.30.0.8       00e0-fc12-3456
             -
     ------------------------------------------------------------------------------
     Total users                        : 1
   ```

#### Configuration Files

```
#
sysname HUAWEI
#
ip pool pool1 bas local
 gateway 172.30.0.1 255.255.255.0
 section 0 172.30.0.2 172.30.0.200
 excluded-ip-address 172.30.0.8
#
aaa
 default-password cipher %^%#oNUw%i-|"WcBgt8=fSVID7F<=K_N+.(ip[H\:a{D%^%#
 default-user-name include mac-address .  
 #
 authentication-scheme local
  authentication-mode local
 #
 domain isp1
  authentication-scheme local
  accounting-scheme default0
  ip-pool pool1
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 192.168.8.1 255.255.255.0
#
interface GigabitEthernet0/2/0.1
 user-vlan 2005 qinq 510  
 bas
 #
  access-type layer2-subscriber default-domain authentication isp1
  authentication-method bind
  ip-trigger
  arp-trigger 
#
static-user 172.30.0.8 172.30.0.8 gateway 172.30.0.1 interface GigabitEthernet0/2/0.1 vlan 2005 qinq 510 mac-address 00e0-fc12-3456 detect
#
local-aaa-server
 user 00e0-fc12-3456@isp1 password cipher %^%#-;Y`5xisf(pJ|7O@]x=({F5*>\If$&5m]dS^\UgF%^%# authentication-type B block fail-times 3 interval 5
#
return
```