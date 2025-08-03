Example for Configuring Ethernet Layer 3 Leased Line Access
===========================================================

This section provides an example for configuring Ethernet Layer 3 leased line access. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374051__fig_dc_ne_cfg_01359601), the networking requirements are as follows:

* An Ethernet Layer 3 leased line user accesses the Internet through GE 0/1/6.1.
* The username is **layer3lease1@isp1** for the leased line.
* The network segment for the Layer 3 leased line user is 11.11.11.0/24.
* RADIUS authentication and RADIUS accounting are used. The IP address of the RADIUS server is 192.168.8.249. The authentication port number is 1812 and the accounting port number is 1813. The RADIUS+1.1 protocol is adopted, and the key is **Huawei**.
* The network-side interface is GE 0/1/1.

**Figure 1** Configuring Ethernet Layer 3 leased line access![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/6.1 and GE 0/1/1, respectively.


  
![](images/fig_dc_ne_cfg_01359601.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure RADIUS authentication and accounting schemes.
2. Configure a RADIUS server group.
3. Configure an authentication domain.
4. Configure a VLAN and an IP address for a sub-interface.
5. Configure a BAS interface and an upstream interface.
6. Configure a static route.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP address and port numbers of the RADIUS authentication and accounting server
* Gateway and DNS server addresses
* Domain name
* VLAN ID and IP address of the sub-interface
* BAS interface parameters
* Static route

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
   [*HUAWEI-radius-rd1] radius-server authentication 192.168.8.249 1812
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server accounting 192.168.8.249 1813
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
4. Configure a domain.
   
   
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
   [~HUAWEI-aaa-domain-isp1] quit
   ```
   ```
   [~HUAWEI-aaa]quit
   ```
5. Configure a VLAN.
   
   
   
   # Configure a VLAN.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   * If the access interface is an Ethernet sub-interface, you must configure a VLAN. If the access interface is an Ethernet main interface, you cannot configure a VLAN.
   * You can configure only one VLAN for a Layer 3 leased line.
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/6.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/6.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/6.1] control-vid 1 dot1q-termination
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/6.1] dot1q termination vid 3
   ```
6. Configure an IP address.
   
   
   ```
   [*HUAWEI-GigabitEthernet0/1/6.1] ip address 192.168.1.1 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/6.1] commit
   ```
7. Configure a BAS interface.
   
   
   ```
   [~HUAWEI-GigabitEthernet0/1/6.1] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/6.1-bas] access-type layer3-leased-line user-name layer3lease1 password cipher YsHsjx_202206 default-domain authentication isp1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/6.1-bas] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/6.1-bas] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/6.1] quit
   ```
8. Configure a static route.
   
   
   ```
   [~HUAWEI] ip route-static 11.11.11.0 255.255.255.0 192.168.1.2
   ```
   ```
   [*HUAWEI] commit
   ```

#### Configuration Files

```
#
sysname HUAWEI
#
radius-server group rd1
 radius-server shared-key-cipher %^%#`E)v.Q@BHVzxxZ;ij{>&_M0!TGP7YRA@8a7mq<\/%^%#
 radius-server authentication 192.168.8.249 1812 weight 0
 radius-server accounting 192.168.8.249 1813 weight 0
 radius-server type plus11
#
aaa
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
#
interface GigabitEthernet0/1/6
 undo shutdown
#
interface GigabitEthernet0/1/6.1
 ip address 192.168.1.1 255.255.255.0
 encapsulation dot1q-termination
 control-vid 1 dot1q-termination
 dot1q termination vid 3
 bas
 #
  access-type layer3-leased-line user-name layer3lease1 password cipher %^%#4*RHO=w*}.d\>j09'Z:%=:co~p\w9'G-^|-zR'N4%^%# default-domain authentication isp1
 #
#
ip route-static 11.11.11.0 255.255.255.0 192.168.1.2
#
return
```