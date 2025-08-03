Example for Configuring IPoEoQ Access
=====================================

This section provides an example for configuring IPoEoQ access. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374016__fig_dc_ne_ipox_cfg_008601), the networking requirements are as follows:

* A user accesses the network through GE 0/1/2.2 on the Router in IPoEoQ mode. LAN switch 1 tags user packets with VLAN 1 and VLAN 2, and LAN switch 2 tags user packets with QinQ 100.
* The users belong to the domain **isp1**, and RADIUS authentication and RADIUS accounting are adopted.
* The address of the RADIUS server is 192.168.7.249. The authentication port number is 1812, and the accounting port number is 1813. The standard RADIUS protocol is adopted, and the shared key is **it-is-my-secret1**.
* The address of the DNS server is 192.168.7.252.

**Figure 1** Configuring IPoEoQ access![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2.2, respectively.


  
![](images/fig_dc_ne_ipox_cfg_008601.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure authentication and accounting schemes.
2. Configure a RADIUS server group.
3. Configure a user password.
4. Configure an address pool.
5. Configure an authentication domain.
6. Configure a BAS interface and an upstream interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP address and port numbers of the RADIUS authentication server and accounting server
* Address pool name, gateway address, and DNS server address
* Domain name
* BAS interface parameters

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view 
   ```
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
   [*HUAWEI-aaa-authen-auth1] commit
   ```
   ```
   [~HUAWEI-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-acct1] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
2. Configure a RADIUS server group.
   
   
   ```
   [~HUAWEI] radius-server group rd1
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server authentication 192.168.7.249 1812
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server accounting 192.168.7.249 1813
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] radius-server shared-key-cipher it-is-my-secret1
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] quit
   ```
3. Configure the IPoE user password.
   
   
   ```
   [~HUAWEI] aaa
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
4. Configure an address pool.
   
   
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
   [*HUAWEI-ip-pool-pool1] section 0 10.82.0.2 10.82.0.200
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
5. Configure an authentication domain.
   
   
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
6. Configure Ethernet interfaces.
   
   
   
   # Configure user-side VLANs.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/2.2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.2] user-vlan 1 2 qinq 100
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.2-vlan-1-2-QinQ-100-100] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.2-vlan-1-2-QinQ-100-100] quit
   ```
   
   
   
   # Configure a BAS interface.
   
   ```
   [~HUAWEI-GigabitEthernet0/1/2.2] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.2-bas] access-type layer2-subscriber
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.2-bas] default-domain authentication isp1
   [*HUAWEI-GigabitEthernet0/1/2.2-bas] authentication-method bind
   [*HUAWEI-GigabitEthernet0/1/2.2-bas] commit
   [~HUAWEI-GigabitEthernet0/1/2.2-bas] arp-trigger
   [~HUAWEI-GigabitEthernet0/1/2.2-bas] ip-trigger
   [~HUAWEI-GigabitEthernet0/1/2.2-bas] quit
   [~HUAWEI-GigabitEthernet0/1/2.2] quit
   ```
   
   # Configure an upstream interface.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] ip address 10.10.7.1 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] quit
   ```
   ```
   [~HUAWEI] quit
   ```
7. Verify the configuration.
   
   
   
   # After completing the configurations, run the [**display access-user domain**](cmdqueryname=display+access-user+domain) command to check user information in the domain. The command output shows that the users have gone online successfully.
   
   ```
   <HUAWEI> display access-user domain isp1
   ```
   ```
   ------------------------------------------------------------------------------
     UserID  Username                Interface      IP address        MAC
             IPv6 address
     ------------------------------------------------------------------------------
     20      user1@isp1              GE0/1/2.2      10.82.0.5         00e0-fc12-3456
             -
     21      user2@isp1              GE0/1/2.2      10.82.0.6         00e0-fc12-3457
             -
     ------------------------------------------------------------------------------
     Total users                        : 2
   ```

#### Configuration Files

```
#
sysname HUAWEI
#
radius-server group rd1
 radius-server shared-key-cipher %^%#clY:%[]x='-RMNJus[s/VJ:3YBq3<..|.{'xgbp+%^%#
 radius-server authentication 192.168.7.249 1812 weight 0
 radius-server accounting 192.168.7.249 1813 weight 0
#
ip pool pool1 bas local
 gateway 10.82.0.1 255.255.255.0
 section 0 10.82.0.2 10.82.0.200
 dns-server 192.168.7.252
#
aaa
 default-password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
 #
 authentication-scheme auth1
 #
 accounting-scheme acct1
 #
 domain default0
 #
 domain default1
 #
 domain default_admin
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ip-pool pool1
#
interface GigabitEthernet0/1/1
 ip address 10.10.7.1 255.255.255.0
#
interface GigabitEthernet0/1/2.2
 user-vlan 1 2 qinq 100
 bas
 #
  access-type layer2-subscriber default-domain authentication isp1
  authentication-method bind
  ip-trigger
  arp-trigger 
#
return
```