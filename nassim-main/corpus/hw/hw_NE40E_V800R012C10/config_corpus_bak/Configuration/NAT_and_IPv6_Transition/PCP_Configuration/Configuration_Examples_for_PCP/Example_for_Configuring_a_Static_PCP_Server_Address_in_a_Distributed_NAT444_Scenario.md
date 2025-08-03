Example for Configuring a Static PCP Server Address in a Distributed NAT444 Scenario
====================================================================================

This section provides an example for configuring static PCP server address in a distributed NAT444 scenario to implement multiple-to-multiple conversions between private addresses of home users and external public addresses, so that users can access the Internet after NAT and PCP connections can be established. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374862__fig_dc_ne_cfg_pcp_0001), a private IPv4 user accesses the Internet after a BRAS performs NAT for the user. The CGN device is required to have a static PCP server address configured and establishes a PCP connection to the user.

The configuration requirements are as follows:

* The private IPv4 home user' PC can access the IPv4 Internet through the MAN.
* The private IPv4 addresses of residential users can be mapped to multiple public IP addresses in multiple-to-multiple translation mode.

**Figure 1** PCP server with a static IP address in a distributed NAT444 scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE 0/2/1.


  
![](images/fig_dc_ne_cfg_pcp_0001.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure NAT user information and RADIUS authentication on the BRAS.
3. Configure a NAT traffic diversion policy.
4. Configure a NAT traffic conversion policy.
5. Configure a static PCP server in a NAT444 instance.
6. Verify the configuration.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of a NAT instance
* NAT address pool's number and start and end IP addresses
* User group name
* ACL and UCL numbers
* NAT traffic diversion policy information
* Static PCP server address![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The static PCP server address must differ from a physical interface address, loopback interface address, or an address in the address pool of the NAT444 instance.

#### Procedure

1. Set the maximum number of sessions that can be created on the service board in slot 1 to 6M.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS_NAT
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS_NAT] vsm on-board-mode disable
   ```
   ```
   [*BRAS_NAT] commit
   ```
   ```
   [~BRAS_NAT] license
   ```
   ```
   [~BRAS_NAT-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*BRAS_NAT-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS_NAT-license] active pcp vsuf slot 1
   ```
   ```
   [*BRAS_NAT-license] commit
   ```
   ```
   [~BRAS_NAT-license] quit
   ```
   * Configure a NAT instance named **nat1** with the ID of **1** and bind it to a NAT board.
     
     ```
     [~BRAS_NAT] service-location 1
     ```
     ```
     [*BRAS_NAT-service-location-1] location slot 1
     ```
     ```
     [*BRAS_NAT-service-location-1] commit
     ```
     ```
     [~BRAS_NAT-service-location-1] quit
     ```
     ```
     [~BRAS_NAT] service-instance-group group1
     ```
     ```
     [*BRAS_NAT-service-instance-group-group1] service-location 1
     ```
     ```
     [*BRAS_NAT-service-instance-group-group1] commit
     ```
     ```
     [~BRAS_NAT-service-instance-group-group1] quit
     ```
     ```
     [~BRAS_NAT] nat instance nat1 id 1
     ```
     ```
     [*BRAS_NAT-nat-instance-nat1] service-instance-group group1
     ```
     ```
     [*BRAS_NAT-nat-instance-nat1] commit
     ```
     ```
     [~BRAS_NAT-nat-instance-nat1] quit
     ```
   * Configure an address pool and set the start IP address to 11.11.11.101 and the end IP address to 11.11.11.105.
     
     ```
     [~BRAS_NAT] nat instance nat1
     ```
     ```
     [~BRAS_NAT-nat-instance-nat1] nat address-group address-group1 group-id 1 11.11.11.101 11.11.11.105
     ```
     ```
     [*BRAS_NAT-nat-instance-nat1] commit
     ```
     ```
     [~BRAS_NAT-nat-instance-nat1] quit
     ```
2. Configure NAT user information.
   1. Configure the BRAS service to enable users to go online. For details, see *HUAWEI NE40E* Configuration Guide â User Access.
      
      
      ```
      [~BRAS_NAT] aaa
      ```
      ```
      [~BRAS_NAT-aaa] authentication-scheme auth1
      ```
      ```
      [*BRAS_NAT-aaa-authen-auth1] authentication-mode radius
      ```
      ```
      [*BRAS_NAT-aaa-authen-auth1] commit
      ```
      ```
      [~BRAS_NAT-aaa-authen-auth1] quit
      ```
      ```
      [~BRAS_NAT-aaa] accounting-scheme acct1
      ```
      ```
      [*BRAS_NAT-aaa-accounting-acct1] accounting-mode radius
      ```
      ```
      [~BRAS_NAT-aaa-accounting-acct1] commit
      ```
      ```
      [~BRAS_NAT-aaa-accounting-acct1] quit
      ```
      ```
      [~BRAS_NAT-aaa] domain isp1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] authentication-scheme auth1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] accounting-scheme acct1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] radius-server group rd1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] ip-pool pool1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] commit
      ```
      ```
      [~BRAS_NAT-aaa-domain-isp1] quit
      ```
      ```
      [~BRAS_NAT-aaa] quit
      ```
   2. Create a user group named **group1**.
      
      
      ```
      [~BRAS_NAT] user-group group1
      ```
      ```
      [~BRAS_NAT] commit
      ```
   3. Specify the domain of users.
      
      
      ```
      [~BRAS_NAT] aaa
      ```
      ```
      [~BRAS_NAT-aaa] domain isp1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] user-group group1 bind nat instance nat1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] commit
      ```
      ```
      [~BRAS_NAT-aaa-domain-isp1] quit
      ```
      ```
      [~BRAS_NAT-aaa] quit
      ```
3. Configure a NAT traffic diversion policy.
   
   
   1. Configure an ACL numbered 6001 and an ACL rule numbered 1.
      ```
      [~BRAS_NAT] acl 6001
      ```
      ```
      [*BRAS_NAT-ucl-6001] rule 1 permit ip source user-group group1
      ```
      ```
      [*BRAS_NAT-ucl-6001] commit
      ```
      ```
      [~BRAS_NAT-ucl-6001] quit
      ```
   2. Configure a traffic classifier.
      ```
      [~BRAS_NAT] traffic classifier classifier1
      ```
      ```
      [*BRAS_NAT-classifier-classifier1] if-match acl 6001
      ```
      ```
      [*BRAS_NAT-classifier-classifier1] commit
      ```
      ```
      [~BRAS_NAT-classifier-classifier1] quit
      ```
   3. Define a traffic behavior **behavior1** and bind it to the NAT instance **nat1**.
      ```
      [~BRAS_NAT] traffic behavior behavior1
      ```
      ```
      [*BRAS_NAT-behavior-behavior1] nat bind instance nat1
      ```
      ```
      [*BRAS_NAT-behavior-behavior1] commit
      ```
      ```
      [~BRAS_NAT-behavior-behavior1] quit
      ```
   4. Configure a NAT traffic policy named **policy1** and associate the ACL-based traffic classification rules with the traffic behavior.
      ```
      [~BRAS_NAT] traffic policy policy1
      ```
      ```
      [*BRAS_NAT-trafficpolicy-policy1] classifier classifier1 behavior behavior1
      ```
      ```
      [*BRAS_NAT-trafficpolicy-policy1] commit
      ```
      ```
      [~BRAS_NAT-trafficpolicy-policy1] quit
      ```
   5. Apply the NAT traffic diversion policy in the system view.
      ```
      [~BRAS_NAT] traffic-policy policy1 inbound
      ```
      ```
      [*BRAS_NAT] commit
      ```
      ```
      [~BRAS_NAT] quit
      ```
4. Configure a NAT444 traffic conversion policy.
   
   
   1. Configure an ACL numbered 3001 and an ACL rule numbered 1.
      ```
      [~BRAS_NAT] acl 3001
      ```
      ```
      [*BRAS_NAT-acl4-advance-3001] rule 10 permit ip source 10.110.10.0 0.0.0.255
      ```
      ```
      [*BRAS_NAT-acl4-advance-3001] commit
      ```
      ```
      [~BRAS_NAT-acl4-advance-3001] quit
      ```
   2. Configure a NAT444 traffic conversion policy.
      ```
      [~BRAS_NAT] nat instance nat1
      ```
      ```
      [~BRAS_NAT-nat-instance-nat1] nat outbound 3001 address-group address-group1
      ```
      ```
      [*BRAS_NAT-nat-instance-nat1] commit
      ```
      ```
      [~BRAS_NAT-nat-instance-nat1] quit
      ```
5. Configure a static PCP server in a NAT444 instance.
   
   
   ```
   [*BRAS_NAT-nat-instance-nat1] pcp server ipv4 10.1.1.1 255.255.255.255
   ```
   ```
   [*BRAS_NAT-nat-instance-nat1] commit
   ```
   ```
   [~BRAS_NAT-nat-instance-nat1] quit
   ```
6. Verify the configuration.
   
   
   ```
   [~BRAS_NAT] display nat instance nat1
   ```
   ```
   nat instance nat1 id 1
    service-instance-group 1
    nat address-group address-group1 group-id 1 11.11.11.101 11.11.11.105
    nat outbound 3001 address-group address-group1
    pcp server ipv4 10.1.1.1 255.255.255.255
   ```

#### Configuration File

BRAS\_NAT configuration file

```
#
sysname BRAS_NAT
#
radius-server group rd1
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
 radius-server type plus11
 radius-server traffic-unit kbyte
#
interface Virtual-Template1
 ppp authentication-mode auto
#
interface GigabitEthernet0/2/1.1
 user-vlan 1
 pppoe-server bind Virtual-Template 1
 bas
  access-type layer2-subscriber default-domain authentication isp1
  authentication-method ppp
#
ip pool pool1 bas local
 gateway 10.110.10.101 255.255.255.0
 section 1 10.110.10.1 10.110.10.100
 dns-server  192.168.7.252
#
vsm on-board-mode disable
#
license
 active nat session-table size 6 slot 1
 active nat bandwidth-enhance 40 slot 1
 active pcp vsuf slot 1
#
service-location 1
 location slot 1 
#
service-instance-group group1
 service-location 1
#
nat instance nat1 id 1
 service-instance-group group1
 nat address-group address-group1 group-id 1 11.11.11.101 11.11.11.105
 nat outbound 3001 address-group address-group1
 pcp server ipv4 10.1.1.1 255.255.255.255
#
user-group group1
#
acl 3001
 rule 10 permit ip source 10.110.10.0 0.0.0.255
#
acl 6001
 rule 1 permit ip source user-group group1
#
traffic classifier classifier1 operator or
 if-match acl 6001 precedence 1
#
traffic behavior behavior1
 nat bind instance nat1
#
traffic policy policy1
 classifier classifier1 behavior behavior1 precedence 1
#
traffic-policy policy1 inbound
#
aaa
 authentication-scheme auth1
  authentication-mode RADIUS
#
 accounting-scheme acct1
  accounting-mode RADIUS
#
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ip-pool pool1
  user-group group1 bind nat instance nat1
#
ip route-static 11.11.11.0 24 null 0
#
ospf 1
 import-route static
#
 return
```