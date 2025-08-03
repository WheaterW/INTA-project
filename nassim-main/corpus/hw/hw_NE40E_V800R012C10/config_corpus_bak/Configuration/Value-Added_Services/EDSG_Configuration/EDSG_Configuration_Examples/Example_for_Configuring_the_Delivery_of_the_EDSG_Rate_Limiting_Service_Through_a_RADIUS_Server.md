Example for Configuring the Delivery of the EDSG Rate Limiting Service Through a RADIUS Server
==============================================================================================

This section provides an example for configuring the delivery of the EDSG rate limiting service through a RADIUS server. In this example, the RADIUS server uses authentication packets to deliver EDSG services, and the uplink and downlink bandwidths of EDSG service policies are configured.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172375078__fig_dc_ne_cfg_edsg_000801), PPPoE users access network 1 at 192.168.100.0/24 and network 2 at 192.168.200.0/24. Different fees need to be charged for traffic over networks 1 and 2. The users have different bandwidth requirements for networks 1 and 2. The uplink and downlink traffic bandwidths for access to network 1 and network 2 are limited to 1 Mbit/s and 2 Mbit/s, respectively. The AAA server uses RADIUS to deliver EDSG service policies in which parameters, such as the authentication scheme, accounting scheme, and bandwidths for uplink and downlink traffic rate limit, are specified.

**Figure 1** EDSG service networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, subinterface3.1, and subinterface3.2 represent GE0/1/2, GE0/1/1, GE0/1/0, GE0/1/0.1, and GE0/1/0.2, respectively.


  
![](images/fig_dc_ne_cfg_edsg_0003.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

The AAA server shown in [Figure 1](#EN-US_TASK_0172375078__fig_dc_ne_cfg_edsg_000801) also functions as a policy server and delivers services through RADIUS.



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
* EDSG service policy parameters, such as the mode in which an EDSG service policy is downloaded, policy name, bound RADIUS server group, authentication scheme, accounting scheme, and bandwidths for uplink and downlink traffic rate limiting for EDSG services


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
   [~HUAWEI-radius-rad_group1] quit
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
      [*HUAWEI-acl-ucl-6020] rule 20 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group s_1m
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
      [*HUAWEI-acl-ucl-6021] rule 25 permit ip source ip-address 192.168.200.0 0.0.0.255 destination service-group s_2m
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
      
      # Define a traffic behavior named **b2**.
      
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
   [*HUAWEI-aaa] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] commit
   ```
   
   
   
   # Configure an AAA accounting scheme named **acct1** and specify RADIUS accounting as the accounting mode.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] quit
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
5. Configure a mode in which EDSG service policies are downloaded.
   
   
   
   # Configure the RADIUS mode for downloading EDSG service policies. In this mode, EDSG service policies are downloaded from the RADIUS server through authentication packets.
   
   ```
   [~HUAWEI] service-policy download radius rad_group1 password cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI] commit
   ```
6. Configure EDSG service policies. (This step is performed on the RADIUS server.)
   1. Configure an EDSG service policy for access to network 1.
      
      
      
      # Configure the RADIUS server to deliver the RADIUS attribute User-Password with a value of **YsHsjx\_202206** for the service policy **service\_edsg1**.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The shared key configured for a RADIUS server group determines the value of the User-Password attribute.
      
      
      # Configure the RADIUS server to deliver the RADIUS attribute Huawei-AVpair (vendor ID=2011; attribute number=188) for the service policy **service\_edsg1**.
      * <service:service-group>: **service\_edsg1** is bound to the service group **s\_1m**.
        
        The value of Huawei-AVpair is **service:service-group=s\_1m**.
      * <service:authentication-scheme>: The authentication scheme **auth1** is set for the service policy **service\_edsg1**.
        
        The value of Huawei-AVpair is **service:authentication-scheme=auth1**.
      * <service:accounting-scheme>: The accounting scheme **acct1** is set for the service policy **service\_edsg1**.
        
        The value of Huawei-AVpair is **service:accounting-scheme=acct1**.
      * <service:radius-server-group>: The RADIUS server group **rad\_group1** is set for the service policy **service\_edsg1**.
        
        The value of Huawei-AVpair is **service:radius-server-group=rad\_group1**.
      
      # Configure the RADIUS server to deliver the RADIUS attribute HW-Input-Committed-Information-Rate (vendor ID=2011; attribute number=2) for the service policy **service\_edsg1**. The value of HW-Input-Committed-Information-Rate is 1000000 bits. This attribute indicates that the uplink bandwidth is set to 1 Mbit/s for the service policy **service\_edsg1**.
      
      # Configure the RADIUS server to deliver the RADIUS attribute HW-Output-Committed-Information-Rate (vendor ID=2011; attribute number=5) for the service policy **service\_edsg1**. The value of HW-Output-Committed-Information-Rate is 1000000 bits. This attribute indicates that the downlink bandwidth is set to 1 Mbit/s for the service policy **service\_edsg1**.
   2. Configure an EDSG service policy for access to network 2.
      
      
      
      # Configure the RADIUS server to deliver the RADIUS attribute User-Password with a value of **YsHsjx\_202206** for the service policy **service\_edsg2**.
      
      # Configure the RADIUS server to deliver the RADIUS attribute Huawei-AVpair (vendor ID=2011; attribute number=188) for the service policy **service\_edsg2**.
      * <service:service-group>: The service policy **service\_edsg2** is bound to the service group **s\_2m**.
        
        The value of Huawei-AVpair is **service:service-group=s\_2m**.
      * <service:authentication-scheme>: The authentication scheme **auth1** is set for the service policy **service\_edsg2**.
        
        The value of Huawei-AVpair is **service:authentication-scheme=auth1**.
      * <service:accounting-scheme>: The accounting scheme **acct1** is set for the service policy **service\_edsg2**.
        
        The value of Huawei-AVpair is **service:accounting-scheme=acct1**.
      * <service:radius-server-group>: The RADIUS server group **rad\_group1** is set for the service policy **service\_edsg2**.
        
        The value of Huawei-AVpair is **service:radius-server-group=rad\_group1**.
      
      # Configure the RADIUS server to deliver the RADIUS attribute HW-Input-Committed-Information-Rate (vendor ID=2011; attribute number=2) for the service policy **service\_edsg2**. The value of HW-Input-Committed-Information-Rate is 2000000 bits. This attribute indicates that the uplink bandwidth is set to 2 Mbit/s for the service policy **service\_edsg2**.
      
      # Configure the RADIUS server to deliver the RADIUS attribute HW-Output-Committed-Information-Rate (vendor ID=2011; attribute number=5) for the service policy **service\_edsg2**. The value of HW-Output-Committed-Information-Rate is 2000000 bits. This attribute indicates that the downlink bandwidth is set to 2 Mbit/s for the service policy **service\_edsg2**.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For details about the RADIUS attribute dictionary used in this step, see User Access > Appendix: RADIUS Attributes > RADIUS Attribute Dictionary.
      
      The RADIUS attribute names displayed in this step must be the same as those in the RADIUS attribute dictionary loaded to the RADIUS server. If they are different, change the RADIUS attribute names to be the same as those in the RADIUS attribute dictionary based on the vendor ID and attribute number.
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
   [*HUAWEI-ip-pool-edsg_pool] commit
   ```
   ```
   [~HUAWEI-ip-pool-edsg_pool] quit
   ```
8. Bind the local address pool and RADIUS server group to an AAA domain.
   
   
   
   # Bind the local address pool **edsg\_pool** and the RADIUS server group **rad\_group1** to an AAA domain.
   
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
   [*HUAWEI-aaa-domain-domain1] quit
   ```
   ```
   [*HUAWEI-aaa] commit
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
    
    
    
    # View the ID of the online user.
    
    ```
    <HUAWEI> display value-added-service user
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
      0              service_edsg1       Active                                     
      1              service_edsg2       Active                                     
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
      Authentication method              : auth1
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
    
    # View the user information in **domain1**.
    
    ```
    <HUAWEI> display access-user  domain  domain1  verbose
    ```
    ```
    -------------------------------------------------------------------           
    Basic:                                                                          
      User access index             : 128000                                        
      State                         : Used                                          
      User name                     : user1                                
      Domain name                   : domain1                                          
      User backup state             : No                                            
      RUI user state                : -                                             
      User access interface         : GigabitEthernet0/1/2.1                        
      User access PeVlan/CeVlan     : 100/100                                       
      User access slot              : 5                                             
      User MAC                      : 00e0-fc12-3456                                
      User IP address               : 172.31.24.253                                  
      User IP netmask               : 255.255.255.255                               
      User gateway address          : 172.31.0.1                                      
      User Authen IP Type           : ipv4/-/-                                      
      User Basic IP Type            : -/-/-                                         
      User access type              : PPPoE                                         
      User authentication type      : PPP authentication                            
      Agent-Circuit-Id              : -                                             
      Agent-Remote-Id               : -                                             
      Access-line-id Information(pppoe+): -                                         
      Access start time             : 2013-10-17 10:42:15                           
      User-Group                    : -                                             
      Next-hop                      : -                                             
      Policy-route-IPV6-address     : -                                             
                                                                                    
    AAA:                                                                            
      RADIUS-server-template        : rad_group1                                            
      Server-template of second acct: -                                             
      Current authen method         : RADIUS authentication                         
      Authen result                 : Success                                       
      Current author method         : Idle                                          
      Author result                 : Success                                       
      Action flag                   : Idle                                          
      Authen state                  : Authed                                        
      Author state                  : Idle                                          
      Configured accounting method  : RADIUS accounting                             
      Quota-out                     : Offline                                       
      Current accounting method     : RADIUS accounting                             
      Realtime-accounting-switch            : Close                                 
      Realtime-accounting-interval(sec)     : -                                     
      Realtime-accounting-send-update       : No                                    
      Realtime-accounting-traffic-update    : No                                    
      Accounting start time         : 2013-10-17 10:42:15                           
      Online time (h:min:sec)       : 00:07:45                                      
      Accounting state              : Accounting                                    
      MTU                           : 1492                                          
      MRU                           : 1492                                          
      Idle-cut direction            : Both                                          
      Idle-cut-data (time,rate,idle): 0 sec, 60 kbyte/min, 0 min 0 sec              
      Ipv4 Realtime speed           : 0 kbyte/min                                   
      Ipv4 Realtime speed inbound   : 0 kbyte/min                                   
      Ipv4 Realtime speed outbound  : 0 kbyte/min                                   
                                                                                    
    Dot1X:                                                                          
      User MSIDSN name              : -                                             
      EAP user                      : No                                            
      MD5 end                       : No                                            
                                                                                    
    VPN&Policy-route:                                                               
      Vpn-Instance                  : -                                             
                                                                                    
    Multicast Service:                                                              
      Multicast-profile             : -                                             
      Multicast-profile-ipv6        : -                                             
      Max Multicast List Number     : 4                                             
      IGMP enable                   : Yes                                           
                                                                                    
    ACL&QoS:                                                                        
      Link bandwidth auto adapt     : Disable                                       
      UpPriority                    : Unchangeable                                  
      DownPriority                  : Unchangeable                                  
                                                                                    
    EDSG information:                                                               
      Service info                  : Aservice_edsg1                                         
    Flow Statistic:                                                                 
      If flow info contain l2-head  : Yes                                           
      Flow-Statistic-Up             : Yes                                           
      Flow-Statistic-Down           : Yes                                           
      Up packets number(high,low)   : (0,0)                                         
      Up bytes number(high,low)     : (0,0)                                         
      Down packets number(high,low) : (0,0)                                         
      Down bytes number(high,low)   : (0,0)                                         
      IPV6 Up packets number(high,low)     : (0,0)                                  
      IPV6 Up bytes number(high,low)       : (0,0)                                  
      IPV6 Down packets number(high,low)   : (0,0)                                  
      IPV6 Down bytes number(high,low)     : (0,0)                                  
                                                                                    
    Dslam information :                                                             
      Circuit ID                       :-                                           
      Remote ID                        :-                                           
      Actual datarate upstream         :0(Kbps)                                     
      Actual datarate downstream       :0(Kbps)                                     
      Min datarate upstream            :0(Kbps)                                     
      Min datarate downstream          :0(Kbps)                                     
      Attainable datarate upstream     :0(Kbps)                                     
      Attainable datarate downstream   :0(Kbps)                                     
      Max datarate upstream            :0(Kbps)                                     
      Max datarate downstream          :0(Kbps)                                     
      Min lowpower datarate upstream   :0(Kbps)                                     
      Min lowpower datarate downstream :0(Kbps)                                     
      Max delay upstream               :0(s)                                        
      Max delay downstream             :0(s)                                        
      Actual delay upstream            :0(s)                                        
      Actual delay downstream          :0(s)                                        
      Access loop encapsulation        :0x000000                                    
      -------------------------------------------------------------------           
      Are you sure to display some information?(Y/N)[Y]:  
    
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
      Up packets number(high,low)   : (0,670580346)
      Up bytes number(high,low)     : (19,4229905664)
      Down packets number(high,low) : (0,670597972)
      Down bytes number(high,low)   : (21,3689402864)
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
  authentication-scheme radius
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
 rule 20 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group s_1m
 #
acl number 6021
 rule 15 permit ip source service-group s_2m destination ip-address 192.168.200.0 0.0.0.255
 rule 25 permit ip source ip-address 192.168.200.0 0.0.0.255 destination service-group s_2m
#
traffic classifier c1 operator or
 if-match acl 6020 precedence 1
#
traffic classifier c2 operator or
 if-match acl 6021  precedence 1
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
service-policy download radius rad_group1 password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978
#
interface GigabitEthernet0/1/1
 ip address 10.10.10.1 255.255.255.0
#
interface GigabitEthernet0/1/2.1 
 user-vlan 1000 2000
 user-vlan 1 1000 qinq 100
 bas
 #
  access-type layer2-subscriber default-domain pre-authentication domain1
  authentication-method ppp web  
#
interface GigabitEthernet0/1/0.1
 vlan-type dot1q 1
 ip address 192.168.100.1 255.255.255.0
#
return

```