Example for Configuring BOD
===========================

This section provides an example for configuring BOD. You can learn about the configuration process based on the BOD networking diagram. This example covers networking requirements, configuration roadmap, data preparation, configuration procedure, and configuration files.

#### Networking Requirements

As shown in [Figure 1](#EN-US_CONCEPT_0172374993__fig_dc_ne_cfg_01136201), the networking requirements are as follows:

* The basic value-added service policy for users in domain **isp1** is to implement RADIUS charging and allow users in this domain to access network segment 192.168.100.0/24.
* The IP address and port number of the RADIUS authentication server are 10.10.10.2 and 1812, respectively. The IP address and port number of the RADIUS accounting server are 10.10.10.2 and 1813, respectively. The default values are used for other parameters.
* The IP address and port number of the Diameter server are 10.10.10.3 and 3288, respectively.

#### Networking Diagram

**Figure 1** BOD networking diagram![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/10, GE 0/2/8, and GE 0/2/9, respectively.


  
![](images/fig_dc_ne_cfg_01.png)  


#### Configuration Roadmap

1. Configure an authentication scheme and an accounting scheme.
2. Configure a RADIUS server group.
3. Configure an address pool.
4. Configure a policy server.
5. Configure a value-added service accounting mode.
6. Configure a QoS profile.
7. Configure a BOD service policy.
8. Configure an AAA domain.
9. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP addresses and port numbers of the RADIUS authentication server and accounting server
* Address pool name, gateway address, server group name, and IP addresses on different network segments
* BOD traffic policy
* QoS profile and BOD service template
* Domain name
* Interface parameters

#### Configuration Procedure

1. Configure AAA.
   
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
   
   # Configure a RADIUS server group.
   
   ```
   [~HUAWEI] radius-server group group1
   ```
   ```
   [*HUAWEI-radius-group1] radius-server authentication 10.10.10.2 1812
   ```
   ```
   [*HUAWEI-radius-group1] radius-server accounting 10.10.10.2 1813
   ```
   ```
   [*HUAWEI-radius-group1] radius-server shared-key-cipher huawei
   ```
   ```
   [*HUAWEI-radius-group1] commit
   ```
   ```
   [~HUAWEI-radius-group1] quit
   ```
2. Configure an address pool.
   
   ```
   [~HUAWEI] ip pool pool1 bas local
   ```
   ```
   [~HUAWEI-ip-pool-pool1] gateway 172.16.100.1 24
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] section 0 172.16.100.2 172.16.100.200
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] quit
   ```
3. Enable the value-added service function.
   
   ```
   [~HUAWEI] value-added-service enable
   ```
   ```
   [*HUAWEI] commit
   ```
4. Configure value-added service policies.
   
   # Configure a policy server.
   
   ```
   [~HUAWEI] diameter enable
   ```
   ```
   [~HUAWEI] diameter-local huawei interface GigabitEthernet 0/5/0 host test107 realm huawei.com product NE40E
   ```
   ```
   [~HUAWEI] diameter-peer huawei ip 10.10.10.3 port 3288 host pcrf realm huawei.com
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~HUAWEI] diameter-server group huawei
   ```
   ```
   [~HUAWEI-diameter-group-huawei] diameter-link local huawei peer huawei client-port 4097 weight 5
   ```
   ```
   [*HUAWEI-diameter-group-huawei] commit
   ```
   ```
   [~HUAWEI-diameter-group-huawei] quit
   ```
5. Configure a value-added service accounting mode.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] radius-server group group1
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] value-added-service account-type radius group1
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
6. Configure a QoS profile.
   
   # Configure a QoS profile named **qos-prof1**.
   
   ```
   [~HUAWEI] qos-profile qos-prof1
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof1] car cir 5000 inbound
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof1] car cir 5000 outbound
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof1] commit
   ```
   ```
   [~HUAWEI-qos-profile-qos-prof1] quit
   ```
7. Configure a BOD service policy named **bod1**.
   
   ```
   [~HUAWEI] value-added-service policy bod1 bod 
   ```
   ```
   [~HUAWEI-bod1] accounting-scheme acct1
   ```
   ```
   [~HUAWEI-bod1] qos-profile qos-prof1
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof1] commit
   ```
   ```
   [~HUAWEI-qos-profile-qos-prof1] quit
   ```
   ```
   [~HUAWEI-bod1] quit
   ```
8. Configure an AAA domain named **isp1**.
   
   # Configure an AAA domain named **isp1**.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp1
   ```
   
   # Configure an authentication scheme in the domain.
   
   ```
   [~HUAWEI-aaa-domain-isp1] authentication-scheme auth1
   ```
   
   # Configure an accounting scheme in the domain.
   
   ```
   [~HUAWEI-aaa-domain-isp1] accounting-scheme acct1
   ```
   
   # Configure a RADIUS server group named **group1** in the domain.
   
   ```
   [~HUAWEI-aaa-domain-isp1] radius-server group group1
   ```
   
   # Configure an accounting type in the domain.
   
   ```
   [~HUAWEI-aaa-domain-isp1] value-added-service account-type radius group1
   ```
   
   # Configure a Diameter server group named **huawei** in the domain.
   
   ```
   [~HUAWEI-aaa-domain-isp1] diameter-server group huawei
   ```
   
   # Configure an address pool in the domain.
   
   ```
   [*HUAWEI-aaa-domain-isp1] ip-pool pool1
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
9. Configure interfaces.
   
   # Create a virtual template (VT).
   
   ```
   [~HUAWEI] interface Virtual-Template 1
   ```
   ```
   [*HUAWEI-Virtual-Template1] commit
   ```
   ```
   [~HUAWEI-Virtual-Template1] quit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/10
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/10]  pppoe-server bind virtual-template 1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/10] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/10]  bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/10-bas]  access-type layer2-subscriber
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/10-bas]  commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/10] quit
   ```
   
   # Configure an upstream interface.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/2/8.1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/8.1] vlan-type dot1q 1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/8.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/8.1] ip address 192.168.100.1 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/8.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/8.1] quit
   ```
   
   # Configure the interface that is connected to both the RADIUS and Diameter servers.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/2/9
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/9] ip address 10.10.10.1 255.255.255.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/9] commit
   ```
10. Verify the configuration.
    
    Run the [**display value-added-service policy**](cmdqueryname=display+value-added-service+policy) command to check value-added service policy information.
    
    ```
    <HUAWEI> display value-added-service policy
    ```
    ```
     ------------------------------------------------------------------
      Index   Service Policy Name               Used Num  Type  User Num
      ------------------------------------------------------------------
      1      bod1                                  1       BOD    1
      ------------------------------------------------------------------
      Total 2,2 printed 
    
    ```
    
    Run the [**display value-added-service user**](cmdqueryname=display+value-added-service+user) command to check value-added service information.
    
    ```
    <HUAWEI> display value-added-service user user-id 168 bod
    ```
    ```
    -------------------------------------------------------------------------
     Bod user service table:
    
     Service user id                              : 168
     Service type                                 : Diameter user bod
     Service policy                               : bod1
     Account method                               : Radius
     Account start time                           : 2016-11-22 13:10:32
     Normal-server-group                          : --
     Flow up packets(high,low)                    : (0,0)
     Flow up bytes(high,low)                      : (0,0)
     Flow down packets(high,low)                  : (0,0)
     Flow down bytes(high,low)                    : (0,0)
     IPV6 Flow up packets(high,low)               : (0,0)
     IPV6 Flow up bytes(high,low)                 : (0,0)
     IPV6 Flow down packets(high,low)             : (0,0)
     IPV6 Flow down bytes(high,low)               : (0,0)
     Up committed information rate <kbps>         : 5000
     Up Peak information rate <kbps>              : No limit
     Up committed burst size <bytes>              : -
     Up Peak burst size <bytes>                   : -
     Down committed information rate <kbps>       : 5000
     Down Peak information rate <kbps>            : No limit
     Down committed burst size <bytes>            : -
     Down Peak burst size <bytes>                 : -
    
    ```
    
    Run the [**display diameter-group bind-info**](cmdqueryname=display+diameter-group+bind-info) command to check the bindings between AAA domains and Diameter server groups.
    
    ```
    <HUAWEI> display diameter-group bind-info
    ```
    ```
    -----------------------------------------------------------------------------
     |          Domain Name                |       Diameter Group Name           |
     -----------------------------------------------------------------------------
     |                                isp1 |                              huawei |
     -----------------------------------------------------------------------------
    
    ```
    
    Run the [**display diameter configuration**](cmdqueryname=display+diameter+configuration) command to check Diameter-related configuration.
    
    ```
    <HUAWEI> display diameter configuration
    ```
    ```
    -- Diameter Configuration ---------------------------------------------------
        Diameter function is Enabled
        Diameter Gx use XML data dictionary
        Diameter predefined-rule support-type edsg is Disabled
        Diameter GX application version is R940
     -----------------------------------------------------------------------------
     -- Diameter local information -----------------------------------------------
        Diameter local number         : 1
     -----------------------------------------------------------------------------
      |  Local index                  : 0
      |  Local name                   : abc
      |  Local interface name         : GigabitEthernet0/1/0
      |  Local IP Address             : 10.137.83.222
      |  Local IPv6 Address           : 2001:DB8:3::1
      |  Local host name              : nanjing222
      |  Local realm name             : huawei
      |  Local product name           : testa
     -----------------------------------------------------------------------------
     -- Diameter peer information  -----------------------------------------------
        Diameter peer number          : 1
     -----------------------------------------------------------------------------
      |  Peer index                   : 0
      |  Peer name                    : peer
      |  Peer IPv4 address            : 10.137.83.56
      |  Peer port                    : 3868
      |  Peer host name               : pcrf.huawei.com
      |  Peer realm name              : huawei.com
     -----------------------------------------------------------------------------
     -- Diameter server group Configuration --------------------------------------
        Diameter server group number  : 1
     -----------------------------------------------------------------------------
      |  Group index                  : 0
      |  Group name                   : test
      |  Group active state           : Active
      |  Group Reference number       : 1
     -----------------------------------------------------------------------------
      |  Connection group number      : 1
     -----------------------------------------------------------------------------
      || Connection group index       : 0
      || Local index                  : 0
      || Local name                   : abc
      || Local interface name         : GigabitEthernet0/1/0
      || Local IP Address             : 10.137.83.222
      || Local host name              : nanjing222
      || Local realm name             : huawei
      || Local product name           : testa
      || Peer index                   : 0
      || Peer name                    : peer
      || Peer IPv4 address            : 10.137.83.56
      || Peer port                    : 3868
      || Peer host name               : pcrf.huawei.com
      || Peer realm name              : huawei.com
     -----------------------------------------------------------------------------
      || Connection number            : 1
     -----------------------------------------------------------------------------
      |||Connection index             : 0
      |||Client port                  : 3896
      |||Link State                   : Up
     -----------------------------------------------------------------------------
      |  Total connection number      : 1
     -----------------------------------------------------------------------------
    ```

#### Configuration Files

```
#
sysname HUAWEI
#
value-added-service enable
#
diameter enable
#
diameter-local huawei interface GigabitEthernet0/2/9 host test107 realm huawei.com product NE40E
#
diameter-peer huawei ip 10.10.10.3 port 3288 host pcrf realm huawei.com
#
radius-server group group1
 radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
 radius-server authentication 10.10.10.2 1812 weight 0
 radius-server accounting 10.10.10.2 1813 weight 0
#
diameter-server group huawei
 diameter-link local huawei peer huawei client-port 4097 weight 5
#
ip pool pool1 bas local
 gateway 172.16.100.1 255.255.255.0
 section 0 172.16.100.2 172.16.100.200
#
dot1x-template 1
#
aaa
 authentication-scheme auth1
 #
 authorization-scheme default
 #
 accounting-scheme acct1
 #
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  ip-pool pool1
  diameter-server group huawei
  value-added-service account-type radius group1
  radius-server group group1
#
qos-profile qos-prof1
 car cir 5000 cbs 935000 green pass red discard inbound
 car cir 5000 cbs 935000 green pass red discard outbound
#
value-added-service policy bod1 bod
 accounting-scheme acct1
 qos-profile qos-prof1
#
interface Virtual-Template1
 ppp authentication-mode auto
#
interface GigabitEthernet0/2/8.1
 vlan-type dot1q 1
 ip address 192.168.100.1 255.255.255.0
#
interface GigabitEthernet0/2/9
 undo shutdown
 ip address 10.10.10.1 255.255.255.0
#
interface GigabitEthernet0/1/10z
 pppoe-server bind Virtual-Template 1
 undo shutdown
 bas
 #
  access-type layer2-subscriber
 #
#
return

```