Example for Configuring a DAA Service
=====================================

This section provides an example for configuring a DAA service.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0172375028__fig_dc_me_cfg_01136201):

* The domain to which users belong is isp1, and the limited bandwidth is 20 Mbit/s.
* The accounting mode is RADIUS accounting; the user group to which the users belong is isp1; tariff level 1 is used for the users who access the network segment 192.168.100.0/24 and the limited bandwidth is 10 Mbit/s; tariff level 5 is used for the users who access the network segment 192.168.200.0/24 and the limited bandwidth is 5 Mbit/s.
* The IP address and port number of the RADIUS authentication server are 10.10.10.2 and 1812, respectively. The IP address and port number of the RADIUS accounting server are 10.10.10.2 and 1813, respectively. The default values are used for other parameters.

#### Networking Diagram

**Figure 1** DAA service networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, sub-interface3.1, and sub-interface3.2 represent GE 0/1/1, GE 0/1/2, GE 0/1/0.1, and GE 0/1/0.2, respectively.


  
![](images/fig_dc_me_cfg_01.png)

#### Configuration Roadmap

1. Configure AAA.
2. Configure an address pool.
3. Enable the value-added service function.
4. Configure a user group.
5. Configure a DAA traffic policy.
6. Configure QoS profiles.
7. Configure a DAA service policy.
8. Configure an AAA domain.
9. Configure interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Authentication scheme name and authentication mode
* Accounting scheme name and accounting mode
* RADIUS server group name, and IP addresses and port numbers of the RADIUS authentication and accounting servers
* Address pool name, gateway address, user group name, and IP addresses of different network segments
* ACL rules and DAA traffic policy
* QoS profiles and DAA service policy
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
   [*HUAWEI-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [*HUAWEI-aaa] accounting-scheme acct1
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
   
   # Configure a RADIUS server group.
   
   ```
   [*HUAWEI] radius-server group group1
   ```
   ```
   [*HUAWEI-radius-group1] radius-server authentication 10.10.10.2 1812
   ```
   ```
   [*HUAWEI-radius-group1] radius-server accounting 10.10.10.2 1813
   ```
   ```
   [*HUAWEI-radius-group1] radius-server shared-key huawei
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
   [*HUAWEI-ip-pool-pool1] gateway 172.16.100.1 24
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] section 0 172.16.100.2 172.16.100.200
   ```
   ```
   [*HUAWEI-ip-pool-pool1] quit
   ```
   ```
   [*HUAWEI] commit
   ```
3. Enable the value-added service function.
   
   ```
   [~HUAWEI] value-added-service enable
   ```
   ```
   [*HUAWEI] commit
   ```
4. Configure a user group.
   
   ```
   [~HUAWEI] user-group isp1
   ```
5. Configure a DAA traffic policy.
   
   # Configure user ACL 6000.
   
   ```
   [~HUAWEI] acl number 6000
   ```
   ```
   [*HUAWEI-acl-ucl-6000] rule 5 permit ip source user-group isp1 destination ip-address 192.168.100.0 0.0.0.255
   ```
   ```
   [*HUAWEI-acl-ucl-6000] rule 10 permit ip source ip-address 192.168.100.0 0.0.0.255 destination user-group isp1
   ```
   ```
   [*HUAWEI-acl-ucl-6000] quit
   ```
   
   # Configure user ACL 6001.
   
   ```
   [*HUAWEI] acl number 6001
   ```
   ```
   [*HUAWEI-acl-ucl-6001] rule 10 permit ip source user-group isp1 destination ip-address 192.168.200.0 0.0.0.255
   ```
   ```
   [*HUAWEI-acl-ucl-6001] rule 15 permit ip source ip-address 192.168.200.0 0.0.0.255 destination user-group isp1
   ```
   ```
   [*HUAWEI-acl-ucl-6001] quit
   ```
   
   # Configure a traffic classifier named **tc1**.
   
   ```
   [*HUAWEI] traffic classifier tc1
   ```
   ```
   [*HUAWEI-classifier-tc1] if-match acl 6000
   ```
   ```
   [*HUAWEI-classifier-tc1] quit
   ```
   
   # Configure a traffic classifier named **tc2**.
   
   ```
   [*HUAWEI] traffic classifier tc2
   ```
   ```
   [*HUAWEI-classifier-tc2] if-match acl 6001
   ```
   ```
   [*HUAWEI-classifier-tc2] quit
   ```
   
   # Configure a traffic behavior named **tb1**, and set an action for tariff level 1.
   
   ```
   [*HUAWEI] traffic behavior tb1
   ```
   ```
   [*HUAWEI-behavior-tb1] tariff-level 1
   ```
   ```
   [*HUAWEI-behavior-tb1] car
   ```
   ```
   [*HUAWEI-behavior-tb1] traffic-statistic
   ```
   ```
   [*HUAWEI-behavior-tb1] quit
   ```
   
   # Configure a traffic behavior named **tb2**, and set an action for tariff level 5.
   
   ```
   [*HUAWEI] traffic behavior tb2
   ```
   ```
   [*HUAWEI-behavior-tb2] tariff-level 5
   ```
   ```
   [*HUAWEI-behavior-tb2] car
   ```
   ```
   [*HUAWEI-behavior-tb2] traffic-statistic
   ```
   ```
   [*HUAWEI-behavior-tb2] quit
   ```
   
   # Configure a DAA traffic policy named **traffic\_policy\_daa1**, and associate **tc1** and **tc2** with **tb1** and **tb2**, respectively.
   
   ```
   [*HUAWEI] traffic policy traffic_policy_daa1
   ```
   ```
   [*HUAWEI-trafficpolicy-traffic_policy_daa1] classifier tc1 behavior tb1
   ```
   ```
   [*HUAWEI-trafficpolicy-traffic_policy_daa1] classifier tc2 behavior tb2
   ```
   ```
   [*HUAWEI-trafficpolicy-traffic_policy_daa1] quit
   ```
   
   # Apply the DAA traffic policy globally.
   
   ```
   [*HUAWEI] accounting-service-policy traffic_policy_daa1
   ```
6. Configure QoS profiles.
   
   # Configure a QoS profile named **qos-prof1**.
   
   ```
   [*HUAWEI] qos-profile qos-prof1
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof1] car cir 5000 inbound
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof1] car cir 5000 outbound
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof1] quit
   ```
   
   # Configure a QoS profile named **qos-prof2**.
   
   ```
   [*HUAWEI] qos-profile qos-prof2
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof2] car cir 10000 inbound
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof2] car cir 10000 outbound
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof2] quit
   ```
   
   # Configure a QoS profile named **qos-prof3**.
   
   ```
   [*HUAWEI] qos-profile qos-prof3
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof3] car cir 20000 inbound
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof3] car cir 20000 outbound
   ```
   ```
   [*HUAWEI-qos-profile-qos-prof3] commit
   ```
   ```
   [~HUAWEI-qos-profile-qos-prof3] quit
   ```
7. Configure a DAA service policy.
   
   # Configure a DAA service policy named **vp-daa**, which is configured in a domain from which users go online or carried in an authentication response packet delivered by a RADIUS server.
   
   ```
   [~HUAWEI] value-added-service policy vp-daa daa
   ```
   ```
   [~HUAWEI-vas-policy-vp-daa] accounting-scheme acct1
   ```
   
   # Configure QoS profiles for traffic levels.
   
   ```
   [~HUAWEI-vas-policy-vp-daa] tariff-level 1 qos-profile qos-prof2
   ```
   ```
   [~HUAWEI-vas-policy-vp-daa] tariff-level 5 qos-profile qos-prof1
   ```
   ```
   [~HUAWEI-vas-policy-vp-daa] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When priority scheduling based on tariff levels is enabled, the tariff levels configured here must be consistent with those configured in [5](#EN-US_CONCEPT_0172375028__step5).
8. Configure an AAA domain.
   
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
   [*HUAWEI-aaa-domain-isp1] radius-server group group1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] user-group isp1
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] value-added-service policy vp-daa
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] value-added-service account-type radius group1
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] qos-profile qos-prof3 inbound
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] qos-profile qos-prof3 outbound
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a RADIUS server is used to deliver a DAA service policy, you may not bind a DAA service policy to a domain. The RADIUS server delivers a DAA service policy name through the HW-Policy-Name (26-95) attribute carried in an authentication response packet.
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
   [~HUAWEI] interface GigabitEthernet 0/1/2
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2]  pppoe-server bind virtual-template 1
   ```
   ```
   [*HUAWEI-Virtual-Template1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2]  bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2-bas] access-type layer2-subscriber default-domain authentication isp1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2-bas] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2] quit
   ```
   
   # Configure upstream interfaces.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] vlan-type dot1q 1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] ip address 192.168.100.1 255.255.255.0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0.2
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.2] vlan-type dot1q 2
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.2] ip address 192.168.200.1 255.255.255.0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.2] quit
   ```
   
   # Configure an interface for connecting to the RADIUS server.
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] ip address 10.10.10.1 255.255.255.0
   ```
10. Verify the configuration.
    
    Run the [**display value-added-service policy**](cmdqueryname=display+value-added-service+policy) command to check information about value-added service policies.
    
    ```
    <HUAWEI>display value-added-service policy
    ```
    ```
    ------------------------------------------------------------------
      Index   Service Policy Name               Used Num   Type  User Num
      ------------------------------------------------------------------
      0      vp-daa                                  1      DAA     1
      ------------------------------------------------------------------  
      Total 1,1 printed
    
    ```
    
    Run the [**display value-added-service user**](cmdqueryname=display+value-added-service+user) command to check information about all users using value-added services.
    
    ```
    <HUAWEI> display value-added-service user daa
    ```
    ```
    ----------------------------------------------------------------
     The used user id table are:
           95      
     ----------------------------------------------------------------
    Total users:1
    
    ```
    
    Run the [**display value-added-service user user-id**](cmdqueryname=display+value-added-service+user+user-id) command to check information about a specified user using the DAA service.
    
    ```
    <HUAWEI> display value-added-service user user-id 95 daa tariff-level 1
    ```
    ```
    ------------------------------------------------------------------------- 
    Daa user service table: 
    Service user id                            : 95 
    Service type                               : Default dsg 
    Service IP type                            : IPv4 
    Service policy                             : vp-daa 
    Account method                             : Radius 
    Account start time                         : 2017-04-07 08:14:36 
    Normal-server-group                        : -- 
    Flow up packets(high,low)                  : (0,0) 
    Flow up bytes(high,low)                    : (0,0) 
    Flow down packets(high,low)                : (0,0) 
    Flow down bytes(high,low)                  : (0,0) 
    IPV6 Flow up packets(high,low)             : (0,0) 
    IPV6 Flow up bytes(high,low)               : (0,0) 
    IPV6 Flow down packets(high,low)           : (0,0) 
    IPV6 Flow down bytes(high,low)             : (0,0) 
    Up committed information rate <kbps>       : 10000
    Up Peak information rate <kbps>            : No limit
    Up committed burst size <bytes>            : - 
    Up Peak burst size <bytes>                 : - 
    Down committed information rate <kbps>     : 10000
    Down Peak information rate <kbps>          : No limit
    Down committed burst size <bytes>          : - 
    Down Peak burst size <bytes>               : - 
    ```

#### Configuration Files

```
#
sysname HUAWEI
#
 user-group isp1
#
 value-added-service enable
#
qos-profile qos-prof3
 car cir 20000 cbs 1870000 green pass red discard inbound
 car cir 20000 cbs 1870000 green pass red discard outbound
qos-profile qos-prof2
 car cir 10000 cbs 1870000 green pass red discard inbound
 car cir 10000 cbs 1870000 green pass red discard outbound
qos-profile qos-prof1
 car cir 5000 cbs 935000 green pass red discard inbound
 car cir 5000 cbs 935000 green pass red discard outbound
#
radius-server group group1
 radius-server authentication 10.10.10.2 1812 weight 0
 radius-server accounting 10.10.10.2 1813 weight 0
#
acl number 6000
 rule 5 permit ip source user-group isp1 destination ip-address 192.168.100.0 0.0.0.255
 rule 10 permit ip source ip-address 192.168.100.0 0.0.0.255 destination user-group isp1
#
acl number 6001
 rule 10 permit ip source user-group isp1 destination ip-address 192.168.200.0 0.0.0.255
 rule 15 permit ip source ip-address 192.168.200.0 0.0.0.255 destination user-group isp1
#
traffic classifier tc2 operator or
 if-match acl 6001
traffic classifier tc1 operator or
 if-match acl 6000
#
traffic behavior tb1
 tariff-level 1
 car
 traffic-statistic
traffic behavior tb2
 tariff-level 5
 car
 traffic-statistic
#
traffic policy traffic_policy_daa1
 share-mode
 classifier tc1 behavior tb1
 classifier tc2 behavior tb2
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
  value-added-service policy vp-daa
  radius-server group group1
  user-group isp1
  qos-profile qos-prof3 inbound
  qos-profile qos-prof3 outbound
#
value-added-service policy vp-daa daa
 accounting-scheme acct1
 user-group isp1
 tariff-level 1 qos-profile qos-prof2
 tariff-level 5 qos-profile qos-prof1
#
interface Virtual-Template1
 ppp authentication-mode auto
#
interface GigabitEthernet0/1/0.1
 vlan-type dot1q 1
 ip address 192.168.100.1 255.255.255.0
#
interface GigabitEthernet0/1/0.2
 vlan-type dot1q 2
 ip address 192.168.200.1 255.255.255.0
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 10.10.10.1 255.255.255.0
interface GigabitEthernet0/1/2
 pppoe-server bind Virtual-Template 1
 undo shutdown
 bas
 #
  access-type layer2-subscriber default-domain authentication isp1
 #
#
 accounting-service-policy traffic_policy_daa1
#
return

```