Example for Configuring EDSG Service Bandwidth Limiting Locally
===============================================================

This section describes how to locally configure an EDSG service policy and apply it to an AAA domain. All users in the AAA domain use the EDSG service policy to implement differentiated accounting and rate limit for users who access different subnets.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001138599523__fig_dc_ne_cfg_edsg_000801), PPPoE users go online from domain1. PPPoE users' traffic fees and bandwidth requirements for accessing network 1 (192.168.100.0/24) and network 2 (192.168.200.0/24) differ greatly. The upstream and downstream bandwidths for accessing network 1 are limited to 1 Mbit/s, and those for accessing network 2 are limited to 2 Mbit/s.

**Figure 1** EDSG service networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, subinterface3.1, and subinterface3.2 represent GE0/1/2, GE0/1/1, GE0/1/0, GE0/1/0.1, and GE0/1/0.2, respectively.


  
![](figure/en-us_image_0000001091577708.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the VAS function.
2. Configure a RADIUS server.
3. Configure an EDSG traffic policy.
4. Configure AAA authentication and accounting schemes.
5. Configure a mode in which EDSG service policies are downloaded.
6. Configure EDSG service policies.
7. Configure a service policy group.
8. Configure a local address pool.
9. Configure an AAA domain.
10. Configure interfaces.


#### Data Preparation

To complete the configuration, you need the following data:

* Parameters related to the RADIUS server, including the IP address and port number.
* EDSG traffic policy parameters, such as the service group name, ACL rule, traffic classifier, traffic behavior, and traffic policy
* RADIUS server group name, IP address and port number of a RADIUS authentication server, and IP address and port number of a RADIUS accounting server used for an EDSG service policy
* Authentication scheme name, authentication mode, accounting scheme name, and accounting mode used for an EDSG service policy
* EDSG service policy parameters, such as the mode in which EDSG service policies are downloaded, EDSG service policy name, name of the bound RADIUS server group, authentication scheme, accounting scheme, and bandwidths for uplink and downlink traffic rate limiting for EDSG services
* Name of the service policy group bound to the domain, name of the local address pool, gateway, and range of the user address pool.


#### Procedure

1. Enable the VAS function.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] value-added-service enable
   ```
   ```
   [*HUAWEI] commit
   ```
2. Configure policy servers.
   
   
   
   # Set the RADIUS server group name to **rad\_group1**, the RADIUS authentication server's IP address and port number to 10.10.10.2 and 1812, the RADIUS accounting server's IP address and port number to 10.10.10.2 and 1813, and the shared key for the RADIUS authentication and accounting servers to **YsHsjx\_202206**.
   
   ```
   [~HUAWEI] radius-server group rad_group1
   ```
   ```
   [*HUAWEI-radius-rad_group1] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-radius-rad_group1] radius-server authentication 10.10.10.2 1812
   ```
   ```
   [*HUAWEI-radius-rad_group1] radius-server accounting 10.10.10.2 1813
   ```
   ```
   [*HUAWEI-radius-rad_group1] commit
   ```
   ```
   [~HUAWEI-radius-rad_group1] quit
   ```
3. Configure an EDSG traffic policy.
   1. Create service groups.
      
      
      ```
      [~HUAWEI] service-group s_1m
      [*HUAWEI] service-group s_2m
      [*HUAWEI] commit
      ```
   2. Configure ACL rules for service groups.
      
      
      
      # Configure ACL 6020 and define ACL rules for the service group **s\_1m**.
      
      ```
      [~HUAWEI] acl number 6020
      ```
      ```
      [*HUAWEI-acl-ucl-6020] rule 10 permit ip source service-group s_1m destination ip-address 192.168.100.0 0.0.0.255
      ```
      ```
      [*HUAWEI-acl-ucl-6020] rule 11 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group s_1m
      ```
      ```
      [*HUAWEI-acl-ucl-6020] commit
      ```
      ```
      [~HUAWEI-acl-ucl-6020] quit
      ```
      
      # Configure ACL 6021 and define ACL rules for the service group **s\_2m**.
      
      ```
      [~HUAWEI] acl number 6021
      ```
      ```
      [*HUAWEI-acl-ucl-6021] rule 15 permit ip source service-group s_2m destination ip-address 192.168.200.0 0.0.0.255
      ```
      ```
      [*HUAWEI-acl-ucl-6021] rule 16 permit ip source ip-address 192.168.200.0 0.0.0.255 destination service-group s_2m
      ```
      ```
      [*HUAWEI-acl-ucl-6021] commit
      ```
      ```
      [~HUAWEI-acl-ucl-6021] quit
      ```
   3. Configure traffic classifiers.
      
      
      
      # Configure a traffic classifier named **c1**.
      
      ```
      [~HUAWEI] traffic classifier c1
      ```
      ```
      [*HUAWEI-classifier-c1] if-match acl 6020
      ```
      ```
      [*HUAWEI-classifier-c1] commit
      ```
      ```
      [~HUAWEI-classifier-c1] quit
      ```
      
      # Configure a traffic classifier named **c2**.
      
      ```
      [~HUAWEI] traffic classifier c2
      ```
      ```
      [*HUAWEI-classifier-c2] if-match acl 6021
      ```
      ```
      [*HUAWEI-classifier-c2] commit
      ```
      ```
      [~HUAWEI-classifier-c2] quit
      ```
   4. Configure traffic behaviors.
      
      
      
      # Configure a traffic behavior named **b1**.
      
      ```
      [~HUAWEI] traffic behavior b1
      ```
      ```
      [*HUAWEI-behavior-b1] commit
      ```
      ```
      [~HUAWEI-behavior-b1] quit
      ```
      
      # Configure a traffic behavior named **b2**.
      
      ```
      [~HUAWEI] traffic behavior b2
      ```
      ```
      [*HUAWEI-behavior-b2] commit
      ```
      ```
      [~HUAWEI-behavior-b2] quit
      ```
   5. Configure an EDSG traffic policy.
      
      
      
      # Configure an EDSG traffic policy named **traffic\_policy\_edsg**, and associate traffic classifiers **c1** and **c2** with traffic behaviors **b1** and **b2**, respectively.
      
      ```
      [~HUAWEI] traffic policy traffic_policy_edsg
      ```
      ```
      [*HUAWEI-policy-traffic_policy_edsg] share-mode
      ```
      ```
      [*HUAWEI-policy-traffic_policy_edsg] classifier c1 behavior b1
      ```
      ```
      [*HUAWEI-policy-traffic_policy_edsg] classifier c2 behavior b2
      ```
      ```
      [*HUAWEI-policy-traffic_policy_edsg] commit
      ```
      ```
      [~HUAWEI-policy-traffic_policy_edsg] quit
      ```
   6. Apply the EDSG traffic policy globally.
      
      
      ```
      [~HUAWEI] traffic-policy traffic_policy_edsg inbound
      ```
      ```
      [*HUAWEI] traffic-policy traffic_policy_edsg outbound
      ```
      ```
      [~HUAWEI] commit
      ```
4. Configure AAA authentication and accounting schemes.
   
   
   
   # Configure two AAA authentication schemes, one with the authentication mode set to RADIUS, and that of the other one set to none.
   
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
   [~HUAWEI-aaa] authentication-scheme none
   ```
   ```
   [*HUAWEI-aaa-authen-none] authentication-mode none
   ```
   ```
   [*HUAWEI-aaa-authen-none] commit
   ```
   ```
   [~HUAWEI-aaa-authen-none] quit
   ```
   
   
   
   # Configure an AAA accounting scheme named **acct1** and specify RADIUS accounting as the accounting mode.
   
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
5. Configure the mode in which EDSG service policies are downloaded as local download.
   
   
   ```
   [~HUAWEI] service-policy download local
   ```
   ```
   [*HUAWEI] commit
   ```
6. Configure EDSG service policies.
   1. Configure an EDSG service policy for access to network 1.
      
      
      
      # Create an EDSG service policy named **service\_edsg1**.
      
      ```
      [~HUAWEI] service-policy name service_edsg1 edsg
      ```
      
      # Bind the service group **s\_1m** to the EDSG service policy **service\_edsg1**.
      
      ```
      [*HUAWEI-service-policy-service_edsg1] service-group s_1m
      ```
      ```
      [~HUAWEI-service-policy-service_edsg1] commit
      ```
      
      # Bind the RADIUS server group **rad\_group1** to the EDSG service policy **service\_edsg1**.
      
      ```
      [~HUAWEI-service-policy-service_edsg1] radius-server group rad_group1
      ```
      
      # Bind the authentication scheme **none** to the EDSG service policy **service\_edsg1**.
      
      ```
      [~HUAWEI-service-policy-service_edsg1] authentication-scheme none
      ```
      
      # Bind the accounting scheme **acct1** to the EDSG service policy **service\_edsg1**.
      
      ```
      [*HUAWEI-service-policy-service_edsg1] accounting-scheme acct1
      ```
      
      # Set the bandwidth for uplink traffic rate limit to 1 Mbit/s for the EDSG service policy **service\_edsg1**.
      
      ```
      [*HUAWEI-service-policy-service_edsg1] rate-limit cir 1000 inbound
      ```
      
      # Set the bandwidth for downlink traffic rate limit to 1 Mbit/s for the EDSG service policy **service\_edsg1**.
      
      ```
      [*HUAWEI-service-policy-service_edsg1] rate-limit cir 1000 outbound
      ```
      ```
      [*HUAWEI-service-policy-service_edsg1] commit
      ```
      ```
      [~HUAWEI-service-policy-service_edsg1] quit
      ```
   2. Configure an EDSG service policy for access to network 2.
      
      
      
      # Create an EDSG service policy named **service\_edsg2**.
      
      ```
      [~HUAWEI] service-policy name service_edsg2 edsg
      ```
      
      # Bind the service group **s\_2m** to the EDSG service policy **service\_edsg2**.
      
      ```
      [*HUAWEI-service-policy-service_edsg2] service-group s_2m
      ```
      ```
      [~HUAWEI-service-policy-service_edsg2] commit
      ```
      
      # Bind the RADIUS server group **rad\_group1** to the EDSG service policy **service\_edsg2**.
      
      ```
      [~HUAWEI-service-policy-service_edsg2] radius-server group rad_group1
      ```
      
      # Bind the authentication scheme **auth1** to the EDSG service policy **service\_edsg2**.
      
      ```
      [~HUAWEI-service-policy-service_edsg2] authentication-scheme auth1
      ```
      
      # Bind the accounting scheme **acct1** to the EDSG service policy **service\_edsg2**.
      
      ```
      [*HUAWEI-service-policy-service_edsg2] accounting-scheme acct1
      ```
      
      # Set the bandwidth for uplink traffic rate limit to 2 Mbit/s for the EDSG service policy **service\_edsg2**.
      
      ```
      [*HUAWEI-service-policy-service_edsg2] rate-limit cir 2000 inbound
      ```
      
      # Set the bandwidth for downlink traffic rate limit to 2 Mbit/s for the EDSG service policy **service\_edsg2**.
      
      ```
      [*HUAWEI-service-policy-service_edsg2] rate-limit cir 2000 outbound
      ```
      ```
      [*HUAWEI-service-policy-service_edsg2] commit
      ```
      ```
      [~HUAWEI-service-policy-service_edsg2] quit
      ```
7. Configure a service policy group.
   
   
   ```
   [~HUAWEI] service-policy-group group1
   ```
   ```
   [*HUAWEI-service-policy-group-group1] service-policy service_edsg1
   ```
   ```
   [*HUAWEI-service-policy-group-group1] service-policy service_edsg2
   ```
   ```
   [*HUAWEI-service-policy-group-group1] commit
   ```
   ```
   [~HUAWEI-service-policy-group-group1] quit
   ```
8. Configure a local address pool.
   
   
   
   # Configure a local address pool named **edsg\_pool**, set the gateway address to 172.31.0.1/16, and specify the address range as 172.31.0.2 to 172.31.255.255.
   
   ```
   [~HUAWEI] ip pool edsg_pool bas local
   ```
   ```
   [*HUAWEI-ip-pool-edsg_pool] gateway 172.31.0.1 255.255.0.0
   ```
   ```
   [*HUAWEI-ip-pool-edsg_pool] commit
   ```
   ```
   [~HUAWEI-ip-pool-edsg_pool] section 0 172.31.0.2 172.31.255.255
   ```
   ```
   [*HUAWEI-ip-pool-edsg_pool] quit
   ```
   ```
   [*HUAWEI] commit
   ```
9. Bind the local address pool and RADIUS server group to an AAA domain.
   
   
   
   # Bind the local address pool **edsg\_pool**, RADIUS server group **rad\_group1**, and service policy group **group1** to the AAA domain.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [*HUAWEI-aaa] domain domain1
   ```
   ```
   [*HUAWEI-aaa-domain-domain1] ip-pool edsg_pool
   ```
   ```
   [*HUAWEI-aaa-domain-domain1] radius-server group rad_group1
   ```
   ```
   [*HUAWEI-aaa-domain-domain1] service-policy-group group1
   ```
   ```
   [*HUAWEI-aaa-domain-domain1] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-domain-domain1] quit
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
10. Configure interfaces.
    1. Configure a BAS interface.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       For details about how to configure a BAS interface, see [Example for Configuring PPPoE Access for IPv4 Users](dc_ne_pppoe_cfg_0013.html) in *HUAWEI NE40E-M2 series Configuration Guide - User Access*.
       
       ```
       [~HUAWEI] interface GigabitEthernet0/1/2.1
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/2.1] user-vlan 1000 2000
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/2.1] user-vlan 1 1000 qinq 100
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/2.1] bas
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain pre-authentication domain1
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/2.1-bas] authentication-method ppp web
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/2.1-bas] quit
       ```
       ```
       [*HUAWEI-GigabitEthernet10/1/2.1] commit
       ```
       ```
       [~HUAWEI-GigabitEthernet10/1/2.1] quit
       ```
    2. Configure an uplink interface.
       
       
       ```
       [~HUAWEI] interface GigabitEthernet0/1/0.1
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/0.1] vlan-type dot1q 1
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/0.1] ip address 192.168.100.1 255.255.255.0
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/0.1] commit
       ```
       ```
       [~HUAWEI-GigabitEthernet0/1/0.1] quit
       ```
    3. Configure the interface connecting the BRAS to the policy server, AAA server, and portal server.
       
       
       ```
       [~HUAWEI] interface GigabitEthernet0/1/1
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/1] ip address 10.10.10.1 255.255.255.0
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/1] commit
       ```
       ```
       [~HUAWEI-GigabitEthernet0/1/1] quit
       ```
11. Verify the configuration. 
    
    
    
    # Check the ID of the online user.
    
    ```
    <HUAWEI> display value-added-service user edsg
    ```
    ```
    The used user id table are:
       128000
    
    ```
    
    # View the service group name and service status information of the user with an ID of 128000.
    
    ```
    <HUAWEI> display value-added-service user user-id 128000 edsg 
    ```
    ```
    -------------------------------------------------------                        
      User access index                  : 128000                                    
      User name                          : user1                                  
     -------------------------------------------------------                        
      Traffic rate mode                  : Separate                                 
      Traffic statistic mode             : Separate                                 
      Inbound rate limit mode            : Car                                      
      Outbound rate limit mode           : Car                                      
      Service change mode                : Stop-start                               
     -------------------------------------------------------                        
      User edsg service table:                                                       
     -------------------------------------------------------                        
      Index          Service name        State                                      
     -------------------------------------------------------                        
      0                service_edsg1       Active                                     
      1                service_edsg2       Active                                     
     -------------------------------------------------------
    
    ```
    
    # View detailed information about the EDSG service with a service index of 0 and a user ID of 128000.
    
    ```
    <HUAWEI> display value-added-service user user-id 128000 edsg service-index 0
    ```
    ```
    -------------------------------------------------------
      Service index                      : 0
      Service name                       : service_edsg1
      Service type                       : EDSG
      Service state                      : Active
      Service group                      : s_1m
      Service group priority             : 0
      Authentication method              : None
      Account method                     : Radius
      Radius server template             : rad_group1
      Account session id                 : HUAWEI05001SSG000100d39d7b128000
      Service online time(HH:MM:SS)      : 00:04:36
      Up committed information rate      : 1000(kbps)
      Up Peak information rate           : 1000(kbps)
      Up committed burst size            : 187000(bytes)
      Up Peak burst size                 : 187000(bytes)
      Down committed information rate    : 1000(kbps)
      Down Peak information rate         : 1000(kbps)
      Down committed burst size          : 187000(bytes)
      Down Peak burst size               : 187000(bytes)
      Up flow packets(high, low)         : (0, 0)
      Up flow bytes(high, low)           : (0, 0)
      Down flow packets(high, low)       : (0, 0)
      Down flow bytes(high, low)         : (0, 0)
     ----------------------------------------------
    
    ```
    
    # View traffic information of the online user.
    
    ```
    <HUAWEI> display access-user domain domain1 verbose
    ```
    ```
    -------------------------------------------------------------------
    Active EDSG services by order:
     Service0 info : service_edsg1
     Service1 info : service_edsg2
    
    Flow Statistic:
      If flow info contain l2-head : Yes
      Flow-Statistic-Up : Yes
      Flow-Statistic-Down : Yes
      Up packets number(high,low) : (0,0)
      Up bytes number(high,low) : (0,0)
      Down packets number(high,low) : (0,0)
      Down bytes number(high,low) : (0,0)
      IPV6 Up packets number(high,low) : (0,0)
      IPV6 Up bytes number(high,low) : (0,0)
      IPV6 Down packets number(high,low) : (0,0)
      IPV6 Down bytes number(high,low) : (0,0)
    
    Value-added-service Flow Statistic:
      EDSG(service0) Up packets number(high,low) : (0,0)
      EDSG(service0) Up bytes number(high,low) : (0,0)
      EDSG(service0) Down packets number(high,low) : (0,0)
      EDSG(service0) Down bytes number(high,low) : (0,0)
      EDSG(service1) Up packets number(high,low) : (0,0)
      EDSG(service1) Up bytes number(high,low) : (0,0)
      EDSG(service1) Down packets number(high,low) : (0,0)
      EDSG(service1) Down bytes number(high,low) : (0,0)
    ```

#### Configuration Files

HUAWEI configuration file

```
#
sysname HUAWEI
#
value-added-service enable
#
service-policy download local
#
radius-server group rad_group1
 radius-server authentication 10.10.10.2 1812 weight 0
 radius-server accounting 10.10.10.2 1813 weight 0
 radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#    
#
ip pool edsg_pool bas local
 gateway 172.31.0.1 255.255.0.0
 section 0 172.31.0.2 172.31.255.255
#
service-policy name service_edsg1 edsg
 radius-server group rad_group1
 service-group s_1m
 authentication-scheme none
 accounting-scheme acct1
 rate-limit cir 1000 inbound
 rate-limit cir 1000 outbound
#
service-policy name service_edsg2 edsg
 radius-server group rad_group1
 service-group s_2m
 authentication-scheme auth1
 accounting-scheme acct1
 rate-limit cir 2000 inbound
 rate-limit cir 2000 outbound
#
service-policy-group group1
 service-policy service_edsg1
 service-policy service_edsg2
#
aaa
 authentication-scheme auth1
  authentication-mode radius
 authentication-scheme none
  authentication-mode none
 accounting-scheme acct1
  accounting-mode radius
 domain domain1
  ip-pool edsg_pool
  radius-server group rad_group1
  service-policy-group group1
  authentication-scheme auth1
#
service-group s_1m
service-group s_2m
#
acl number 6020
 rule 10 permit ip source service-group s_1m destination ip-address 192.168.100.0 0.0.0.255
 rule 11 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group s_1m
#
acl number 6021
 rule 15 permit ip source service-group s_2m destination ip-address 192.168.200.0 0.0.0.255
 rule 16 permit ip source ip-address 192.168.200.0 0.0.0.255 destination service-group s_2m
#
traffic classifier c1 operator or
 if-match acl 6020 precedence 1
#
traffic classifier c2 operator or
 if-match acl 6021 precedence 1
#
traffic behavior b1
#
traffic behavior b2
#
traffic policy traffic_policy_edsg           
 share-mode
 classifier c1 behavior b1 precedence 1
 classifier c2 behavior b2 precedence 2
#
traffic-policy traffic_policy_edsg inbound
traffic-policy traffic_policy_edsg outbound
#
interface GigabitEthernet0/1/0.1
 vlan-type dot1q 1
 ip address 192.168.100.1 255.255.255.0
#
interface GigabitEthernet0/1/1
 ip address 10.10.10.1 255.255.255.0
#
interface GigabitEthernet0/1/2.1
 user-vlan 1000 2000
 user-vlan 1 1000 qinq 100
 bas
  access-type layer2-subscriber default-domain pre-authentication domain1
  authentication-method ppp web
#
return

```