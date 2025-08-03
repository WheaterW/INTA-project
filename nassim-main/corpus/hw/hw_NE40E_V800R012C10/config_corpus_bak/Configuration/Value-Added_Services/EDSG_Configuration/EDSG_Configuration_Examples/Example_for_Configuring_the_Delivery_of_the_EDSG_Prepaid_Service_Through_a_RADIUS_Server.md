Example for Configuring the Delivery of the EDSG Prepaid Service Through a RADIUS Server
========================================================================================

This section provides an example for configuring the delivery of the EDSG prepaid service through a RADIUS server.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172375079__fig_dc_ne_cfg_edsg_000801), PPPoE users access network 1 at 192.168.100.0/24 and network 2 at 192.168.200.0/24. Different fees need to be charged for traffic over networks 1 and 2. The users have different bandwidth requirements for networks 1 and 2. The uplink and downlink traffic bandwidths for access to network 1 and network 2 are limited to 1 Mbit/s and 2 Mbit/s, respectively. In addition, the prepaid function needs to be enabled for the users. To meet these requirements, configure two EDSG services on the BRAS to implement differentiated accounting, rate limit, and prepaid functions on traffic over network 1 and network 2. EDSG allows carriers to provide flexible service and accounting policies for different user requirements.

**Figure 1** EDSG service networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, subinterface3.1, and subinterface3.2 represent GE0/1/2, GE0/1/1, GE0/1/0, GE0/1/0.1, and GE0/1/0.2, respectively.


  
![](images/fig_dc_ne_cfg_edsg_0003.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

The AAA server shown in [Figure 1](#EN-US_TASK_0172375079__fig_dc_ne_cfg_edsg_000801) also functions as a policy server and delivers services through RADIUS.



#### Configuration Roadmap

1. Enable the VAS function.
2. Configure policy servers.
3. Configure an EDSG traffic policy.
4. Configure AAA authentication and accounting schemes.
5. Configure a mode in which EDSG service policies are downloaded.
6. Configure EDSG service policies.
7. Configure a local address pool.
8. Bind the local address pool and RADIUS server group to an AAA domain.
9. Configure the prepaid function.
10. Configure interfaces.
11. Configure access users.
12. Set user 1's prepaid time to 120s on the RADIUS server.
13. Set user 2's prepaid traffic volume to 100 Mbytes on the RADIUS server.


#### Data Preparation

To complete the configuration, you need the following data:

* Policy server parameters, such as the IP address and port number
* EDSG traffic policy parameters, such as the service group name, ACL rule, traffic classifier, traffic behavior, and traffic policy
* RADIUS server group name, IP address and port number of a RADIUS authentication server, and IP address and port number of a RADIUS accounting server used for an EDSG service policy
* Authentication scheme name, authentication mode, accounting scheme name, and accounting mode used for an EDSG service policy
* Name of the local address pool used in the domain, gateway address, and address pool range
* EDSG service policy parameters, such as the mode in which EDSG service policies are downloaded, EDSG service policy name, name of the bound RADIUS server group, RADIUS authentication scheme, RADIUS accounting scheme, and bandwidths for uplink and downlink traffic rate limiting for EDSG services
* RADIUS server group name, IP address and port number of a RADIUS authentication server, and IP address and port number of a RADIUS accounting server used for a prepaid profile
* Authentication scheme name, authentication mode, accounting scheme name, and accounting mode used for a prepaid profile
* Prepaid function parameters, such as the prepaid profile name, bound RADIUS server group, authentication scheme, accounting scheme, password used for the BRAS to apply for an EDSG service quota from the RADIUS server group, time and traffic volume thresholds, and policy used when the service quota is exhausted.


#### Procedure

1. Enable the VAS function.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] value-added-service enable
   ```
   ```
   [~HUAWEI] commit
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
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      You must run the [**service-group**](cmdqueryname=service-group) command to create service groups regardless of whether the BRAS obtains an EDSG service policy from local configurations or a RADIUS server.
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
      [~HUAWEI] traffic classifier c1 operator or
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
      [~HUAWEI] traffic classifier c2 operator or
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
      [~HUAWEI] traffic-policy traffic_policy_edsg outbound
      ```
      ```
      [~HUAWEI] commit
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
   [*HUAWEI-aaa-accounting-acct1] quit
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
5. Configure a mode in which EDSG service policies are downloaded.
   
   
   
   # Configure the mode "first from local configurations and then from an RADIUS server." In this mode, the BRAS first attempts to obtain an EDSG service policy from local configurations. If no EDSG service policy is locally configured, the BRAS obtains an EDSG service policy from an RADIUS server.
   
   ```
   [~HUAWEI] service-policy download local radius rad_group1 password cipher YsHsjx_202206
   ```
   ```
   [~HUAWEI] commit
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
9. Configure the prepaid function.
   1. Configure a prepaid profile for access to network 1.
      
      
      
      # Create a prepaid profile named **prepaid1**.
      
      ```
      [~HUAWEI] prepaid-profile prepaid1
      ```
      
      # Bind the RADIUS server group **rad\_group1** to the prepaid profile **prepaid1**.
      
      ```
      [~HUAWEI-prepaid-profile-prepaid1] radius-server group rad_group1
      ```
      
      # Bind the authentication scheme **auth1** to the prepaid profile **prepaid1**.
      
      ```
      [~HUAWEI-prepaid-profile-prepaid1] authentication-scheme auth1
      ```
      
      # Bind the accounting scheme **acct1** to the prepaid profile **prepaid1**.
      
      ```
      [~HUAWEI-prepaid-profile-prepaid1] accounting-scheme acct1
      ```
      
      # Configure a password used for the BRAS to apply for an EDSG service quota from the RADIUS server group.
      
      ```
      [~HUAWEI-prepaid-profile-prepaid1] password cipher YsHsjx_202206
      ```
      
      # Set the time threshold for the BRAS to reapply for a time quota for EDSG services from the RADIUS server to 60s.
      
      ```
      [*HUAWEI-prepaid-profile-prepaid1] threshold time 60 seconds
      ```
      
      # Set the traffic volume threshold for the BRAS to reapply for a traffic volume quota for EDSG services from the RADIUS server to 10 Mbytes.
      
      ```
      [*HUAWEI-prepaid-profile-prepaid1] threshold volume 10 mbytes
      ```
      ```
      [*HUAWEI-prepaid-profile-prepaid1] commit
      ```
      ```
      [~HUAWEI-prepaid-profile-prepaid1] quit
      ```
   2. Configure a prepaid profile for access to network 2.
      
      
      
      # Create a prepaid profile named **prepaid2**.
      
      ```
      [~HUAWEI] prepaid-profile prepaid2
      ```
      
      # Bind the RADIUS server group **rad\_group1** to the prepaid profile **prepaid2**.
      
      ```
      [~HUAWEI-prepaid-profile-prepaid2] radius-server group rad_group1
      ```
      
      # Bind the authentication scheme **auth1** to the prepaid profile **prepaid2**.
      
      ```
      [~HUAWEI-prepaid-profile-prepaid2] authentication-scheme auth1
      ```
      
      # Bind the accounting scheme **acct1** to the prepaid profile **prepaid2**.
      
      ```
      [~HUAWEI-prepaid-profile-prepaid2] accounting-scheme acct1
      ```
      
      # Configure a password used for the BRAS to apply for an EDSG service quota from the RADIUS server group.
      
      ```
      [~HUAWEI-prepaid-profile-prepaid2] password cipher YsHsjx_202206
      ```
      
      # Set the time threshold for the BRAS to re-apply for a time quota for EDSG services from the RADIUS server to 300s.
      
      ```
      [*HUAWEI-prepaid-profile-prepaid2] threshold time 300 seconds
      ```
      
      # Set the traffic volume threshold for the BRAS to re-apply for a traffic volume quota for EDSG services from the RADIUS server to 20 Mbytes.
      
      ```
      [*HUAWEI-prepaid-profile-prepaid2] threshold volume 20 mbytes
      ```
      ```
      [*HUAWEI-prepaid-profile-prepaid2] commit
      ```
      ```
      [~HUAWEI-prepaid-profile-prepaid2] quit
      ```
   3. Configure a policy used when the quota is exhausted.
      
      
      
      # Configure a deactivation policy for access to network 1.
      
      ```
      [~HUAWEI] prepaid-profile prepaid1
      ```
      ```
      [~HUAWEI-prepaid-profile-prepaid1] quota-out service deactivate
      ```
      ```
      [~HUAWEI-prepaid-profile-prepaid1] commit
      ```
      ```
      [~HUAWEI-prepaid-profile-prepaid1] quit
      ```
      # Configure a redirect policy for access to network 2.
      1. Create an HTTP redirect profile named **http\_redirect\_profile**.
         
         ```
         [~HUAWEI] http-redirect-profile http_redirect_profile
         ```
      2. Configure http://www.huawei.com as a redirect web page.
         
         ```
         [~HUAWEI-redirect-profile-http_redirect_profile] web-server url http://www.huawei.com
         ```
      3. Configure post as the HTTP access mode for the web server.
         
         ```
         [~HUAWEI-redirect-profile-http_redirect_profile] web-server mode post
         ```
         ```
         [~HUAWEI-redirect-profile-http_redirect_profile] commit
         ```
         ```
         [~HUAWEI-redirect-profile-http_redirect_profile] quit
         ```
      4. Configure a redirect policy and specify **http\_redirect\_profile**.
         
         ```
         [~HUAWEI] prepaid-profile prepaid2
         ```
         ```
         [~HUAWEI-prepaid-profile-prepaid2] quota-out redirect http_redirect_profile
         ```
         ```
         [~HUAWEI-prepaid-profile-prepaid2] commit
         ```
         ```
         [~HUAWEI-prepaid-profile-prepaid2] quit
         ```
   4. Apply the prepaid profiles in the EDSG service policy view.
      
      
      
      # Apply the prepaid profile **prepaid1** to the EDSG service policy **service\_edsg1**.
      
      ```
      [~HUAWEI] service-policy name service_edsg1 edsg
      ```
      ```
      [~HUAWEI-service-policy-service_edsg1] prepaid-profile prepaid1
      ```
      ```
      [~HUAWEI-service-policy-service_edsg1] commit
      ```
      ```
      [~HUAWEI-service-policy-service_edsg1] commit
      ```
      
      # Apply the prepaid profile **prepaid2** to the EDSG service policy **service\_edsg2**.
      
      ```
      [~HUAWEI] service-policy name service_edsg2 edsg
      ```
      ```
      [~HUAWEI-service-policy-service_edsg2] prepaid-profile prepaid2
      ```
      ```
      [~HUAWEI-service-policy-service_edsg2] commit
      ```
      ```
      [~HUAWEI-service-policy-service_edsg2] quit
      ```
10. Configure interfaces.
    1. Configure a VT.
       
       
       ```
       [~HUAWEI] interface Virtual-Template 1
       ```
       ```
       [*HUAWEI-Virtual-Template1] commit
       ```
       ```
       [~HUAWEI-Virtual-Template1] quit
       ```
    2. Configure a BAS interface.
       
       
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
       [*HUAWEI-GigabitEthernet0/1/2.1] pppoe-server bind virtual-template 1
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
    3. Configure an uplink interface.
       
       
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
       ```
       [~HUAWEI] interface GigabitEthernet0/1/0.2
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/0.2] vlan-type dot1q 1
       ```
       ```
       [*HUAWEI-GigabitEthernet10/1/0.2] ip address 192.168.200.1 255.255.255.0
       ```
       ```
       [*HUAWEI-GigabitEthernet0/1/0.2] commit
       ```
       ```
       [~HUAWEI-GigabitEthernet0/1/0.2] quit
       ```
    4. Configure the interface connecting the BRAS to the policy server, AAA server, and portal server.
       
       
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
11. Configure access users. (This step is performed on the RADIUS server.)
    
    
    
    # Configure the RADIUS server to deliver the RADIUS attribute User-Password with a value of **YsHsjx\_202206** for PPPoE user 1 and PPPoE user 2.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The shared key configured for a RADIUS server group determines the value of the User-Password attribute.
    
    # Configure the RADIUS server to deliver the RADIUS attribute Huawei-Account-Info (vendor ID=2011; attribute number=184) with a value of Aservice\_edsg1;d1;huawei for PPPoE user 1.
    
    # Configure the RADIUS server to deliver the RADIUS attribute Huawei-Account-Info (vendor ID=2011; attribute number=184) with a value of Aservice\_edsg2;d2;huawei for PPPoE user 2.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The Huawei-Account-Info attribute starting with **A** followed by the service policy name **service\_edsg1** is used in authentication response packets to deliver EDSG services that automatically take effect after being delivered; **d1** and **huawei** indicate the authentication name and password, respectively, to be used for service authentication.
    
    The Huawei-Account-Info attribute starting with **A** followed by the service policy name **service\_edsg2** is used in authentication response packets to deliver EDSG services that automatically take effect after being delivered; **d2** and **huawei** indicate the authentication name and password, respectively, to be used for service authentication.
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    For details about the RADIUS attribute dictionary used in this step, see User Access > Appendix: RADIUS Attributes > RADIUS Attribute Dictionary.
    
    The RADIUS attribute names displayed in this step must be the same as those in the RADIUS attribute dictionary loaded to the RADIUS server. If they are different, change the RADIUS attribute names to be the same as those in the RADIUS attribute dictionary based on the vendor ID and attribute number.
12. Set user 1's prepaid time to 120s on the RADIUS server.
    
    
    
    # Configure the RADIUS server to deliver the RADIUS attribute Session-Timeout with a value of 120s for user 1. This attribute indicates the remaining service time.
    
    # Obtain the ID of the online user.
    
    ```
    <HUAWEI> display value-added-service user edsg
    ```
    ```
    The used user id table are:
       128000
       128001
    
    ```
    
    # View detailed information about the EDSG service when the user has used the EDSG service for 60s and the BRAS sends CoA messages to the RADIUS server in advance to apply for a new time.
    
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
      Account session id                 : HUAWEI05001SSG000100f5fcb5128034
      Service online time(HH:MM:SS)      : 00:01:00
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
      Prepaid state                      : Monitoring
      Time quota                         : 60(seconds)
      Time threshold                     : 120(seconds)
     -------------------------------------------------------  
    
    ```
    
    # View service deactivation information. The command output shows that the user service has been deactivated after 120s.
    
    ```
    <HUAWEI> display service deactivate-record
    ```
    ```
     -------------------------------------------------------------------
      Policy name        : service_edsg1
      User ID            : 128000
      Service index      : 0
      Access time        : 2013-10-17 17:41:03
      Deactivate time    : 2013-10-17 17:45:33
      Deactivate reason  : The server does not reply with prepaid authorization response
    
    ```
13. Set user 2's prepaid traffic volume to 100 Mbytes on the RADIUS server.
    
    
    
    # Configure the RADIUS server to deliver the RADIUS attribute Huawei-Remanent-Volume (Vendor ID=2011, Attribute number=15) with a value of 100M for user 2. The RADIUS attribute Huawei-Remanent-Volume indicates the remaining traffic volume of user 2.
    
    # View the status information of the prepaid profile **prepaid2**.
    
    ```
    <HUAWEI> display prepaid-profile name prepaid2
    ```
    ```
      ------------------------------------------------                              
      Prepaid-profile-index        : 1                                              
      Prepaid-profile-name         : prepaid2                                       
      Prepaid-password             : ******                                         
      Reference-count              : 0                                              
      Authentication-scheme-name   : auth1                                          
      Accounting-scheme-name       : acct1                                          
      Radius-server-template       : rad_group1                                         
      Time-threshold               : 300(s)                                          
      Volume-threshold             : 20(Mbytes)                                     
      Quota-out-action             : service deactivate                             
      HTTP-redirect-profile        : http_redirect_profile                                              
      ------------------------------------------------                               
    ```
    
    # View detailed information about the EDSG service with a service index of 0 and a user ID of 128001.
    
    ```
    <HUAWEI> display value-added-service user user-id 128001 edsg service-index 0
    ```
    ```
    -------------------------------------------------------
      Service index                      : 0
      Service name                       : service_edsg2
      Service type                       : EDSG
      Service state                      : Active
      Service group                      : s_2m
      Service group priority             : 0
      Authentication method              : None
      Account method                     : Radius
      Radius server template             : rad_group1
      Account session id                 : HUAWEI05001SSG000100f5fcb5128034
      Service online time(HH:MM:SS)      : 00:04:28
      Up committed information rate      : 6000(kbps)
      Up Peak information rate           : 6000(kbps)
      Up committed burst size            : 1122000(bytes)
      Up Peak burst size                 : 1122000(bytes)
      Down committed information rate    : 6000(kbps)
      Down Peak information rate         : 6000(kbps)
      Down committed burst size          : 1122000(bytes)
      Down Peak burst size               : 1122000(bytes)
      Up flow packets(high, low)         : (0, 248230)
      Up flow bytes(high, low)           : (0, 25815920)
      Down flow packets(high, low)       : (0, 0)
      Down flow bytes(high, low)         : (0, 0)
      Prepaid state                      : Exhausted      
      Volume quota                      : (0, 8966321)(bytes) 
      Volume threshold                  : (0, 104857600)(bytes)
      HTTP redirect profile              : http_redirect_profile
      Source                             : Diameter
     -------------------------------------------------------
    
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
aaa
 authentication-scheme auth1                                                    
 #  
 accounting-scheme acct1                                                        
 #
# 
http-redirect-profile http_redirect_profile                                     
 web-server url http://www.huawei.com                                              
 web-server mode post                                                           
#                                               
prepaid-profile prepaid1                                                        
 password cipher $$e:TY%^%glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$%^%#:978                                
 authentication-scheme auth1                                                    
 accounting-scheme acct1                                                        
 radius-server group rad_group1                                                     
 threshold time 60 seconds                                                      
 threshold volume 10 mbytes
 quota-out service deactivate                                                     
#                                         
prepaid-profile prepaid2                                                        
 password cipher $$e:TY%(k.Ef$%^%#:978^%glhJ;yPG#$=tC&(Is%q!S_";                               
 authentication-scheme auth1                                                    
 accounting-scheme acct1                                                        
 radius-server group rad_group1                                                     
 threshold time 300 seconds                                                     
 threshold volume 20 mbytes                                                     
 quota-out redirect http_redirect_profile                                       
#                              
service-policy download local radius rad_group1 password cipher $J;yPG#$=tC&(Is%q!S_";$e:TY%(k.Ef$%^%#:978^%glh
#
service-policy name service_edsg1 edsg
 radius-server group rad_group1
 service-group s_1m
 authentication-scheme auth1
 accounting-scheme acct1
 rate-limit cir 1000 inbound
 rate-limit cir 1000 outbound
 prepaid-profile prepaid1
#
service-policy name service_edsg2 edsg
 radius-server group rad_group1
 service-group s_2m
 authentication-scheme auth1
 accounting-scheme acct1
 rate-limit cir 2000 inbound
 rate-limit cir 2000 outbound
 prepaid-profile prepaid2
#
interface GigabitEthernet0/1/1
 ip address 10.10.10.1 255.255.255.0
#
#
interface Virtual-Template1
interface GigabitEthernet0/1/2.1
 user-vlan 1000 2000
 user-vlan 1 1000 qinq 100
 pppoe-server bind virtual-template 1
 bas
 #
  access-type layer2-subscriber default-domain pre-authentication domain1
  authentication-method ppp web  
#
interface GigabitEthernet0/1/0.1
 vlan-type dot1q 1
 ip address 192.168.100.1 255.255.255.0
#
interface GigabitEthernet0/1/0.2
 vlan-type dot1q 2
 ip address 192.168.200.1 255.255.255.0
#
return

```