Example for Configuring Ethernet Layer 2 Leased Line Access
===========================================================

This section provides an example for configuring Ethernet Layer 2 leased line access. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374048__fig_dc_ne_cfg_01359401), the networking requirements are as follows:

* Ethernet Layer 2 leased line users access the Internet through GE 0/1/2.1.
* The username and password of the leased line are **layer2lease1@isp1** and **Root\_123**, respectively.
* The VLAN ID for a leased line user ranges from 1 to 100.
* The leased line users obtain IP addresses from the Router through DHCP.
* RADIUS authentication and RADIUS accounting are used. The IP address of the RADIUS server is 192.168.7.249. The authentication port number is 1645, and the accounting port number is 1646. The RADIUS+1.1 protocol is used, and the shared key is **Huawei**.
* The IP address of the DNS server is 192.168.7.252.
* The network-side interface is GE 0/1/1.

**Figure 1** Configuring Ethernet Layer 2 leased line access![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/2.1 and GE 0/1/1, respectively.


  
![](images/fig_dc_ne_cfg_01359401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure RADIUS authentication and accounting schemes.
2. Configure a RADIUS server group.
3. Configure an address pool.
4. Configure an authentication domain.
5. Configure access interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP address and port numbers of the RADIUS authentication and accounting server
* Configure a username.
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
2. Configure an accounting scheme.
   
   
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
3. Configure a RADIUS server group.
   
   
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
   [*HUAWEI-radius-rd1] radius-server shared-key YsHsjx_202206
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] quit
   ```
4. Configure the IPoE user password.
   
   
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
5. Configure an address pool.
   
   
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
   [*HUAWEI-ip-pool-pool1] dns-server 192.168.7.252
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] quit
   ```
6. Configure a domain.
   
   
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
   [~HUAWEI-aaa]quit
   ```
7. Configure an access interface.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   If the access interface is an Ethernet sub-interface, you must configure a VLAN. If the access interface is an Ethernet main interface, you cannot configure a VLAN.
   
   You can configure multiple VLANs for an interface used for Layer 2 leased line access.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/2.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] user-vlan 1 100
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1-vlan-1-100] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1-bas] access-type layer2-leased-line user-name layer2lease1 password cipher YsHsjx_202206 default-domain authentication isp1
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

#### Configuration Files

```
#
sysname HUAWEI
#
radius-server group rd1
 radius-server shared-key-cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server type plus11
 radius-server traffic-unit kbyte
#
license
 active bas slot 1
#
interface GigabitEthernet0/1/2
 undo shutdown
#
interface GigabitEthernet0/1/2.1
 user-vlan 1 100
 bas
 #
  access-type layer2-leased-line user-name layer2lease1 password cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%# default-domain authentication isp1
 #
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
 #
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ip-pool pool1
#
return
```