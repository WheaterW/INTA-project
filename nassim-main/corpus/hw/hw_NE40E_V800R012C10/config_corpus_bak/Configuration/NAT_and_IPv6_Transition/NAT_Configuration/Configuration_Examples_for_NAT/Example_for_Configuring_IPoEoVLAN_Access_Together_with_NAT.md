Example for Configuring IPoEoVLAN Access Together with NAT
==========================================================

This section provides an example for configuring IPoEoVLAN access together with NAT so that home users can access the Internet through NAT processing.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported only in user access scenarios.

In [Figure 1](#EN-US_TASK_0172374660__fig_dc_ne_cfg_nat_0114), home users access a BRAS using IPoE. The BRAS implements user authentication, authorization, and accounting. It also provides the NAT service to convert between the private and public IP addresses of home users, so that the home users can access the Internet.

Home users of user group 1 can access the Internet.

**Figure 1** Example for configuring IPoEoVLAN access together with NAT![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents Eth-Trunk2.1.


  
![](images/fig_dc_ne_cfg_nat_0114.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure NAT user information and RADIUS authentication on the BRAS.
3. Configure a NAT diversion policy.
4. Configure a BAS interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of a NAT instance
* NAT address pool's number and start and end IP addresses
* User group name
* ACL and UCL numbers
* NAT traffic diversion policy information

#### Procedure

1. Create a NAT instance named **nat1**.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] service-location 1
   ```
   ```
   [*HUAWEI-service-location-1] location slot 3
   ```
   ```
   [*HUAWEI-service-location-1] commit
   ```
   ```
   [~HUAWEI-service-location-1] quit
   ```
   ```
   [~HUAWEI] service-instance-group group1
   ```
   ```
   [*HUAWEI-service-instance-group-group1] service-location 1
   ```
   ```
   [*HUAWEI-service-instance-group-group1] commit
   ```
   ```
   [~HUAWEI-service-instance-group-group1] quit
   ```
   ```
   [~HUAWEI] nat instance nat1 id 1
   ```
   ```
   [*HUAWEI-nat-instance-nat1] service-instance-group group1
   ```
   ```
   [*HUAWEI-nat-instance-nat1] commit
   ```
   ```
   [~HUAWEI-nat-instance-nat1] quit
   ```
2. Configure a NAT address pool.
   
   
   ```
   [~HUAWEI] nat instance nat1 id 1
   ```
   ```
   [~HUAWEI-nat-instance-nat1] nat address-group address-group1 group-id 1 11.1.1.1 mask 26
   ```
   ```
   [*HUAWEI-nat-instance-nat1] commit
   ```
   ```
   [~HUAWEI-nat-instance-nat1] quit
   ```
3. Configure NAT user information.
   1. Create a user group named **group1**.
      
      
      ```
      [~HUAWEI] user-group group1
      ```
   2. Configure the BRAS service on the device so that users can go online. For details, see [IPoE Access Configuration](dc_ne_ipox_cfg_0031.html).
      
      
      ```
      [~HUAWEI] ip pool pool1 bas local
      ```
      ```
      [*HUAWEI-ip-pool-pool1] gateway 10.64.0.1 255.255.0.0
      ```
      ```
      [*HUAWEI-ip-pool-pool1] section 0 10.64.0.2 10.64.255.254
      ```
      ```
      [*HUAWEI-ip-pool-pool1] dns-server 192.168.8.2
      ```
      ```
      [*HUAWEI-ip-pool-pool1] commit
      ```
      ```
      [~HUAWEI-ip-pool-pool1] quit
      ```
      ```
      [~HUAWEI] radius-server group rd1
      ```
      ```
      [*HUAWEI-radius-rd3] radius-server authentication 192.168.8.9 1812
      ```
      ```
      [*HUAWEI-radius-rd3] radius-server accounting 192.168.8.9 1813
      ```
      ```
      [*HUAWEI-radius-rd3] radius-server type standard
      ```
      ```
      [*HUAWEI-radius-rd3] radius-server shared-key-cipher YsHsjx_202206
      ```
      ```
      [*HUAWEI-radius-rd3] commit
      ```
      ```
      [~HUAWEI-radius-rd3] quit
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
      ```
      [~HUAWEI-aaa] accounting-scheme acct1
      ```
      ```
      [*HUAWEI-aaa-accounting-acct1] accounting-mode radius
      ```
      ```
      [~HUAWEI-aaa-accounting-acct1] commit
      ```
      ```
      [~HUAWEI-aaa-accounting-acct1] quit
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
      [*HUAWEI-aaa-domain-isp1] ip-pool pool1
      ```
      ```
      [*HUAWEI-aaa-domain-isp1] user-group group1
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
4. Configure a traffic classification rule, a NAT behavior, and a NAT traffic diversion policy and apply the policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A UCL number ranges from 6000 to 9999.
   
   
   
   1. Configure ACL-based traffic classification rule and set the ACL number to 6001 and ACL rule number to 1.
      
      
      ```
      [~HUAWEI] acl number 6001
      ```
      ```
      [*HUAWEI-acl-ucl-6001] rule 1 permit ip source user-group group1
      ```
      ```
      [*HUAWEI-acl-ucl-6001] commit
      ```
      ```
      [~HUAWEI-acl-ucl-6001] quit
      ```
   2. Configure a traffic classifier.
      
      
      ```
      [~HUAWEI] traffic classifier c1 operator or
      ```
      ```
      [*HUAWEI-classifier-c1] if-match acl 6001
      ```
      ```
      [*HUAWEI-classifier-c1] commit
      ```
      ```
      [~HUAWEI-classifier-c1] quit
      ```
   3. Configure a traffic behavior named **b1** and bind the traffic behavior to the NAT instance named **nat1**.
      
      
      ```
      [~HUAWEI] traffic behavior b1 
      ```
      ```
      [*HUAWEI-behavior-b1] nat bind instance nat1
      ```
      ```
      [*HUAWEI-behavior-b1] commit
      ```
      ```
      [~HUAWEI-behavior-b1] quit
      ```
   4. Configure a NAT diversion policy and associate the ACL rule with the traffic behavior.
      
      
      ```
      [~HUAWEI] traffic policy p1
      ```
      ```
      [*HUAWEI-trafficpolicy-p1] share-mode
      ```
      ```
      [*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1 precedence 1
      ```
      ```
      [*HUAWEI-trafficpolicy-p1] commit
      ```
      ```
      [~HUAWEI-trafficpolicy-p1] quit
      ```
   5. Apply the NAT diversion policy in the system view.
      
      
      ```
      [~HUAWEI] traffic-policy p1 inbound
      ```
      ```
      [*HUAWEI] commit
      ```
5. Configure a BAS interface.
   
   
   ```
   [~HUAWEI] interface Eth-Trunk 2.1
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1] user-vlan 1 2
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1-1-2] quit
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1] bas
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1-bas] access-type layer2-subscriber default-domain authentication isp1
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1-bas] client-option82
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1-bas] option82-relay-mode include allvalue
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1-bas] authentication-method bind
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1-bas] quit
   ```
   ```
   [*HUAWEI-Eth-Trunk2.1] quit
   ```

#### Configuration Files

* BRAS configuration file
  
  ```
  #
  service-location 1
   location slot 3
  #
  service-instance-group group1
   service-location 1
  #
  nat instance nat1 id 1
   service-instance-group group1
   nat address-group group1 group-id 1 11.1.1.1 mask 26 
  #
  radius-server group rd1
   radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#    
   radius-server authentication 192.168.8.9 1812 weight 0
   radius-server accounting 192.168.8.9 1813 weight 0
   radius-server type standard
  #
  ip pool pool1 bas local
   gateway 10.64.0.1 255.255.0.0
   section 0 10.64.0.2 10.64.255.254 
   dns-server 192.168.8.2
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1
    accounting-mode radius
   #
   domain isp1
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool pool1
    user-group group1
   #
   user-group group1
  #
  acl number 6001
   rule 1 permit ip source user-group group1
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat1
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1 precedence 1
  #
  traffic-policy p1 inbound
  #
  interface Eth-Trunk2.1
   user-vlan 1 2
   # 
   bas
    access-type layer2-subscriber default-domain authentication isp1
    client-option82
    option82-relay-mode include allvalue 
    authentication-method bind
   #
  #
   return
  ```