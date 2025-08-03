Example for Activating the EDSG Services Downloaded from Local Configurations Through RADIUS
============================================================================================

This section provides an example for activating the EDSG services downloaded from local configurations through RADIUS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172375075__fig_dc_ne_cfg_edsg_000801), PPPoE users access network 1 at 192.168.100.0/24 and network 2 at 192.168.200.0/24. Different fees need to be charged for traffic over networks 1 and 2. The users have different bandwidth requirements for networks 1 and 2. The uplink and downlink traffic bandwidths for access to network 1 and network 2 are limited to 1 Mbit/s and 2 Mbit/s, respectively.

**Figure 1** EDSG service networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, subinterface3.1, and subinterface3.2 represent GE0/1/2, GE0/1/1, GE0/1/0, GE0/1/0.1, and GE0/1/0.2, respectively.


  
![](images/fig_dc_ne_cfg_edsg_0003.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

The AAA server shown in [Figure 1](#EN-US_TASK_0172375075__fig_dc_ne_cfg_edsg_000801) also functions as a policy server and delivers services through RADIUS.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the VAS function.
2. Configure policy servers.
3. Configure an EDSG traffic policy.
4. Configure RADIUS authentication and accounting schemes.
5. Configure a mode in which EDSG service policies are downloaded.
6. Configure EDSG service policies.
7. Configure a local address pool.
8. Bind the local address pool and RADIUS server group to an AAA domain.
9. Configure interfaces.
10. Configure access users.


#### Data Preparation

To complete the configuration, you need the following data:

* Policy server parameters, such as the IP address and port number
* EDSG traffic policy parameters, such as the service group name, ACL rule, traffic classifier, traffic behavior, and traffic policy
* RADIUS server group name, IP address and port number of a RADIUS authentication server, and IP address and port number of a RADIUS accounting server used for an EDSG service policy
* Authentication scheme name, authentication mode, accounting scheme name, and accounting mode used for an EDSG service policy
* Name of the local address pool used in the domain, gateway address, and address pool range
* EDSG service policy parameters, such as the mode in which EDSG service policies are downloaded, EDSG service policy name, name of the bound RADIUS server group, authentication scheme, accounting scheme, and bandwidths for uplink and downlink traffic rate limiting for EDSG services


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
   [*HUAWEI-radius-rad_group1] radius-server authentication 10.10.10.2 1812
   ```
   ```
   [*HUAWEI-radius-rad_group1] radius-server accounting 10.10.10.2 1813
   ```
   ```
   [*HUAWEI-radius-rad_group1] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-radius-rad_group1] commit
   ```
   ```
   [*HUAWEI-radius-rad_group1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For details about how to configure a RADIUS server group, see [Configuring a Device as a RADIUS Client](dc_ne_aaa_cfg_0600.html) in *HUAWEI NE40E-M2 series Configuration Guide - User Access*.
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
   3. Define traffic classifiers.
      
      
      
      # Define a traffic classifier named **c1**.
      
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
      
      # Define a traffic classifier named **c2**.
      
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
   4. Define traffic behaviors.
      
      
      
      # Define a traffic behavior named **b1**.
      
      ```
      [~HUAWEI] traffic behavior b1
      ```
      ```
      [*HUAWEI-behavior-b1] commit
      ```
      ```
      [~HUAWEI-behavior-b1] quit
      ```
      
      # Define a traffic behavior **b2**.
      
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
      [*HUAWEI] commit
      ```
4. Configure AAA authentication and accounting schemes.
   
   
   
   # Configure an AAA authentication scheme named **auth1** and specify RADIUS authentication as the authentication mode.
   
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
5. Configure a mode in which EDSG service policies are downloaded.
   
   
   
   # Configure the mode "first from local configurations and then from an RADIUS server." In this mode, the BRAS first attempts to obtain an EDSG service policy from local configurations. If no EDSG service policy is locally configured, the BRAS obtains an EDSG service policy from an RADIUS server.
   
   ```
   [~HUAWEI] service-policy download local radius rad_group1 password cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An EDSG service policy can be downloaded in four modes: from local configurations, from a RADIUS server, first from local configurations and then from a RADIUS server, and first from a RADIUS server and then from local configurations. You can run the [**service-policy download**](cmdqueryname=service-policy+download) command to configure a mode in which EDSG service policies are downloaded.
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
      
      # Bind the RADIUS server group **rad\_group1** to the EDSG service policy **service\_edsg1**.
      
      ```
      [*HUAWEI-service-policy-service_edsg1] radius-server group rad_group1
      ```
      
      # Bind the authentication scheme **auth1** to the EDSG service policy **service\_edsg1**.
      
      ```
      [*HUAWEI-service-policy-service_edsg1] authentication-scheme auth1
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
      
      # Bind the RADIUS server group **rad\_group1** to the EDSG service policy **service\_edsg2**.
      
      ```
      [*HUAWEI-service-policy-service_edsg2] radius-server group rad_group1
      ```
      
      # Bind the authentication scheme **auth1** to the EDSG service policy **service\_edsg2**.
      
      ```
      [*HUAWEI-service-policy-service_edsg2] authentication-scheme auth1
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
7. Configure a local address pool.
   
   
   
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
8. Bind the local address pool and RADIUS server group to an AAA domain. By default, the rate of EDSG service traffic is separately limited and is not affected by user bandwidth. Only non-service traffic is counted as user traffic. To change EDSG service traffic rate limiting and statistics collection policies, run the [**edsg traffic-mode rate**](cmdqueryname=edsg+traffic-mode+rate) { **separate** | **together** } **statistic together** command.
   
   
   
   # Bind the local address pool **edsg\_pool** and the RADIUS server group **rad\_group1** to an AAA domain.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain domain1
   ```
   ```
   [*HUAWEI-aaa-domain-domain1] radius-server group rad_group1
   ```
   ```
   [*HUAWEI-aaa-domain-domain1] commit
   ```
   ```
   [~HUAWEI-aaa-domain-domain1] ip-pool edsg_pool
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
9. Configure interfaces.
   1. Configure a BAS interface.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For details about how to configure a BAS interface, see [Example for Configuring PPPoE Access for IPv4 Users](dc_ne_pppoe_cfg_0013.html) in *HUAWEI NE40E-M2 series Configuration Guide - User Access*.
      
      ```
      [~HUAWEI] interface GigabitEthernet0/1/2.1
      ```
      ```
      [*HUAWEI-GigabitEthernet10/1/2.1] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1] user-vlan 1000 2000
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1] user-vlan 1 1000 qinq 100
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1] bas
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain pre-authentication domain1
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
      [~HUAWEI-GigabitEthernet0/1/1] ip address 10.10.10.1 255.255.255.0
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1] quit
      ```
10. Configure access users. (This step is performed on the RADIUS server.)
    
    
    
    # Configure the RADIUS server to deliver the RADIUS attribute User-Password with a value of **YsHsjx\_202206** for PPPoE user 1.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The shared key configured for a RADIUS server group determines the value of the User-Password attribute.
    
    # Configure the RADIUS server to deliver the RADIUS attribute Huawei-Account-Info (vendor ID=2011; attribute number=184) with the value of Aservice\_edsg1;d1;huawei and Aservice\_edsg2;d2;huawei for PPPoE user 1.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The Huawei-Account-Info attribute starting with **A** followed by the service policy name **service\_edsg1** is used in authentication response packets to deliver EDSG services that automatically take effect after being delivered; **d1** and **huawei** indicate the authentication name and password, respectively, to be used for service authentication.
    
    The Huawei-Account-Info attribute starting with **A** followed by the service policy name **service\_edsg2** is used in authentication response packets to deliver EDSG services that automatically take effect after being delivered; **d2** and **huawei** indicate the authentication name and password, respectively, to be used for service authentication.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    For details about the RADIUS attribute dictionary used in this step, see User Access > Appendix: RADIUS Attributes > RADIUS Attribute Dictionary.
    
    The RADIUS attribute names displayed in this step must be the same as those in the RADIUS attribute dictionary loaded to the RADIUS server. If they are different, change the RADIUS attribute names to be the same as those in the RADIUS attribute dictionary based on the vendor ID and attribute number.
11. Verify the configuration.
    
    
    
    # Obtain the ID of the online user.
    
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
    Flow Statistic:
      If flow info contain l2-head  : Yes
      Flow-Statistic-Up             : Yes
      Flow-Statistic-Down           : Yes
      Up packets number(high,low)   : (0,12799800)
      Up bytes number(high,low)     : (2,4094944316)
      Down packets number(high,low) : (0,12634395)
      Down bytes number(high,low)   : (2,4145535568)
      IPV6 Up packets number(high,low)     : (0,0)
      IPV6 Up bytes number(high,low)       : (0,0)
      IPV6 Down packets number(high,low)   : (0,0)
      IPV6 Down bytes number(high,low)     : (0,0)
    
    Value-added-service Flow Statistic:
      EDSG(service1) Up packets number(high,low)   : (0,12774777)
      EDSG(service1) Up bytes number(high,low)     : (2,4069869415)
      EDSG(service1) Down packets number(high,low) : (0,0)
      EDSG(service1) Down bytes number(high,low)   : (0,0)
    
    ```

#### Configuration Files

HUAWEI configuration file

```
#
sysname HUAWEI
#
value-added-service enable
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
aaa
 authentication-scheme auth1
 accounting-scheme acct1
  accounting-mode radius
 domain domain1
  ip-pool edsg_pool
  radius-server group rad_group1
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
service-policy download local radius rad_group1 password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978 
#
service-policy name service_edsg1 edsg
 radius-server group rad_group1
 service-group s_1m
 authentication-scheme auth1
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