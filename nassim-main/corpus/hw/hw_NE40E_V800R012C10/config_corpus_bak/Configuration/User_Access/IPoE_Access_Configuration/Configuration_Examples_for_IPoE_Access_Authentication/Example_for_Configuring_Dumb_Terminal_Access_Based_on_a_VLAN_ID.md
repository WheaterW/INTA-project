Example for Configuring Dumb Terminal Access Based on a VLAN ID
===============================================================

This section provides an example for configuring dumb terminal access based on a VLAN ID. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

Dumb terminals refer to printers and access control devices on a campus network. Generally, these devices do not proactively apply to the BRAS for IP addresses. Dumb terminals access the Internet in static user mode and are authenticated based on the VLAN ID of the associated sub-interface.

On the network shown in [Figure 1](#EN-US_TASK_0172374063__fig_dc_ne_cfg_01360001), the printer accesses the Router through interface1 in static user mode. The fixed IP address is 172.30.0.8.

**Figure 1** Configuring dumb terminal access based on a VLAN ID![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/2.1 and GE 0/1/1, respectively.


  
![](images/fig_dc_ne_cfg_01360001_vlan.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an authentication scheme, with local authentication specified.
2. Configure an address pool, with the IP address 172.30.0.8 reserved for the printer.
3. Configure an authentication domain named **printer**.
4. Configure a BAS interface, with the default authentication domain set to **printer**.
5. Configure a static user.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Address pool name, gateway address, and DNS server address
* Domain name
* BAS interface parameters

#### Procedure

1. Configure an authentication scheme, with local authentication specified.
   
   
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
   [~HUAWEI-aaa] default-user-name include ip-address .
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
   [*HUAWEI-local-aaa-server] user 172.30.0.8@printer password cipher YsHsjx_202206 authentication-type b
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
   [~HUAWEI-ip-pool-pool1] quit
   ```
5. Configure a domain.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain printer
   ```
   ```
   [*HUAWEI-aaa-domain-printer] authentication-scheme local
   ```
   ```
   [*HUAWEI-aaa-domain-printer] accounting-scheme default0
   ```
   ```
   [*HUAWEI-aaa-domain-printer] commit
   ```
   ```
   [~HUAWEI-aaa-domain-printer] ip-pool pool1
   ```
   ```
   [~HUAWEI-aaa-domain-printer] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
6. Configure a BAS interface.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/2.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] user-vlan 100
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1-vlan-100-100] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] default-domain authentication printer
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] authentication-method bind
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] ip-trigger
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] arp-trigger
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1-bas] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, binding authentication is configured. A username and password for authentication are automatically generated. The automatically generated username and password must be the same as those configured locally because local authentication is used. The username and password configured using the [**default-user-name**](cmdqueryname=default-user-name) and [**default-password**](cmdqueryname=default-password) commands in the AAA view are used as the automatically generated username and password. For details, see the configuration files.
7. Configure a static user.
   
   
   ```
   [~HUAWEI] static-user 172.30.0.8 interface gigabitethernet 0/1/2.1 vlan 100 detect
   ```
   ```
   [~HUAWEI] static-user detect interval 1
   ```
   ```
   [*HUAWEI] commit
   ```
8. Verify the configuration.
   
   
   
   After completing the preceding configurations, run the [**display access-user domain**](cmdqueryname=display+access-user+domain) command to check online user information in the domain **printer**. The command output shows that the user has gone online successfully.
   
   ```
   [~HUAWEI] display access-user domain printer
   ```
   ```
     -------------------------------------------------------------------------------------------
     UserID  Username                Interface      IP address      MAC             IPv6 address
     -------------------------------------------------------------------------------------------
     20      172.30.0.8@printer      GE0/1/2.1      172.30.0.8      00e0-fc12-3456       -
     -------------------------------------------------------------------------------------------
     Total users                        : 1
   ```

#### Configuration Files

```
#
sysname HUAWEI
#
license
 active bas slot 1
#
ip pool pool1 bas local
 gateway 172.30.0.1 255.255.255.0
 section 0 172.30.0.2 172.30.0.200
 excluded-ip-address 172.30.0.8
#
aaa
 default-password cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%#
 default-user-name include ip-address .
 #
 authentication-scheme local
  authentication-mode local
 #
 domain printer
  authentication-scheme local
  accounting-scheme default0
  ip-pool pool1
#
interface GigabitEthernet0/1/2
 undo shutdown
#
interface GigabitEthernet0/1/2.1
 user-vlan 100
 bas
 #
  access-type layer2-subscriber default-domain authentication printer
  authentication-method bind
  ip-trigger
  arp-trigger
 #
#
static-user 172.30.0.8 172.30.0.8 gateway 172.30.0.1 interface GigabitEthernet0/1/2.1 vlan 100 detect 
#
static-user detect interval 1
#
local-aaa-server
user 172.30.0.8@printer password cipher %^%#d{TmT/d*SRizc%=,Z\cY)V1*Z&(O7<yDEHLM}Bm>%^%# authentication-type B block fail-times 3 interval 5
#
return
```