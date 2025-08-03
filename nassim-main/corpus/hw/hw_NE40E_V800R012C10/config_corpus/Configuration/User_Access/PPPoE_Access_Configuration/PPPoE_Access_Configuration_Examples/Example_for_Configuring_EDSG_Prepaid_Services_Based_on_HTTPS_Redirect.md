Example for Configuring EDSG Prepaid Services Based on HTTPS Redirect
=====================================================================

EDSG services can be configured on a BRAS to deliver differentiated charging, rate limiting, and prepaid functions for PPPoE users. This section provides an example for configuring EDSG prepaid services based on HTTPS redirect.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0272391694__fig670517384389), PPPoE users' traffic fees for accessing network 1 and network 2 differ greatly. The upstream and downstream bandwidths for accessing network 1 (192.168.100.0/24) are limited to 1 Mbit/s, and those for accessing network 2 (192.168.200.0/24) are limited to 2 Mbit/s. If a carrier wants users to pay in advance and reserve the time or volume quota, two EDSG services can be configured on DeviceA to provide differentiated charging, rate limiting, and prepaid functions for access to network 1 and network 2, thereby ensuring the carrier's operating revenue.

**Figure 1** Configuring EDSG prepaid services based on HTTPS redirect![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 and sub-interfaces 3.1 and 3.2 in this example represent GE 0/1/2, GE 0/1/1, GE 0/1/0, GE 0/1/0.1, and GE 0/1/0.2, respectively.


  
![](figure/en-us_image_0272391695.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a cipher suite, and configure a self-signed RSA certificate or import an HTTPS redirect certificate.
2. Enable the VAS function.
3. Configure a policy server.
4. Configure an EDSG traffic policy.
5. Configure a local address pool.
6. Configure an AAA authentication scheme and accounting scheme, and bind the address pool to the RADIUS server group in the AAA domain.
7. Configure a mode in which EDSG service policies are downloaded.
8. Configure EDSG service policies.
9. Configure the prepaid function.
10. Configure BAS interfaces, upstream interfaces, and an interface connecting the BRAS to servers.
11. Configure online users.
12. Configure user 1's prepaid time on the AAA server.
13. Configure user 2's prepaid volume on the AAA server.

#### Data Preparation

To complete the configuration, you need the following data:

* Names of the imported HTTPS redirect certificate and key file
* Policy server-related parameters, such as the IP address and port number
* EDSG traffic policy-related parameters, such as the service group name, ACL rule, traffic classifier, traffic behavior, and traffic policy
* RADIUS server group name, RADIUS authentication server's IP address and port number, and RADIUS accounting server's IP address and port number used by EDSG service policies
* Authentication scheme name, RADIUS authentication mode, accounting scheme name, and RADIUS accounting mode used by EDSG service policies
* Local address pool name, gateway address, and IP address range of the address pool
* EDSG service policy-related parameters, such as the mode in which EDSG service policies are downloaded, EDSG service policy name, name of the bound RADIUS server group, authentication scheme, accounting scheme, and bandwidths for upstream and downstream traffic rate limiting for EDSG services
* RADIUS server group name, RADIUS authentication server's IP address and port number, and RADIUS accounting server's IP address and port number used by prepaid profiles
* Authentication scheme name, authentication mode, accounting scheme name, and accounting mode used by prepaid profiles
* Prepaid profile-related parameters, such as the prepaid profile name, name of the bound RADIUS server group, authentication scheme, accounting scheme, password used to apply for a prepaid service quota from the RADIUS server group, thresholds of the remaining time and volume, and policies to be used when the service quota is exhausted

#### Procedure

1. Configure a cipher suite, and configure a self-signed RSA certificate or import an HTTPS redirect certificate.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA 
   [*HUAWEI] commit 
   [~DeviceA] user-group huawei
   [~DeviceA] access https-redirect  
   [*DeviceA-access-https-redirect] self-signed rsa modulus 2048 
   [*DeviceA-access-https-redirect] cipher-suite support c02f c02b 1301 1302 
   [*DeviceA-access-https-redirect] commit 
   [~DeviceA-access-https-redirect] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can run the **access https-redirect import certificate** command to import an HTTPS redirect certificate. You can either configure a self-signed RSA certificate or import an HTTPS redirect certificate. If both of them are configured, the imported HTTPS redirect certificate takes effect.
   
   For security purposes, you are advised not to use weak security algorithms. If you have to use a weak security algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
2. Enable the VAS function.
   ```
   [~DeviceA] value-added-service enable
   ```
   ```
   [*DeviceA] commit
   ```
3. Configure a policy server.
   
   # Set the RADIUS server group name to **rad\_group1**, the RADIUS authentication server's IP address and port number to 10.10.10.2 and 1812, the RADIUS accounting server's IP address and port number to 10.10.10.2 and 1813, and the shared key for the RADIUS authentication and accounting servers to **YsHsjx\_202206**.
   
   ```
   [~DeviceA] radius-server group rad_group1
   [*DeviceA-radius-rad_group1] radius-server authentication 10.10.10.2 1812
   [*DeviceA-radius-rad_group1] radius-server accounting 10.10.10.2 1813
   [*DeviceA-radius-rad_group1] commit
   [~DeviceA-radius-rad_group1] radius-server shared-key-cipher YsHsjx_202206
   [*DeviceA-radius-rad_group1] commit
   [~DeviceA-radius-rad_group1] quit
   ```
4. Configure an EDSG traffic policy.
   1. Create service groups.
      ```
      [~DeviceA] service-group s_1m
      [*DeviceA] service-group s_2m
      [*DeviceA] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      A service group must be created regardless of whether an EDSG traffic policy is locally configured or delivered by the RADIUS server.
   2. Configure ACL rules for service groups.
      
      # Configure an ACL numbered 6020 to allow HTTPS redirect for the TCP packets originating from the service group **s\_1m** and whose destination address is the network segment address of network 1 and destination port number is 443.
      
      ```
      [~DeviceA] acl number 6020
      [*DeviceA-acl-ucl-6020] rule permit tcp source service-group s_1m destination ip-address 192.168.100.0 0.0.0.255 destination-port eq 443
      [*DeviceA-acl-ucl-6020] commit
      [~DeviceA-acl-ucl-6020] quit
      ```
      
      # Configure an ACL numbered 6021 to allow HTTPS redirect for the TCP packets originating from the service group **s\_2m** and whose destination address is the network segment address of network 2 and destination port number is 443.
      
      ```
      [~DeviceA] acl number 6021
      [*DeviceA-acl-ucl-6021] rule permit tcp source service-group s_2m destination ip-address 192.168.200.0 0.0.0.255 destination-port eq 443
      [*DeviceA-acl-ucl-6021] commit
      [~DeviceA-acl-ucl-6021] quit
      ```
   3. Configure traffic classifiers.
      
      # Configure a traffic classifier named **c1**.
      
      ```
      [~DeviceA] traffic classifier c1 operator or
      [*DeviceA-classifier-c1] if-match acl 6020
      [*DeviceA-classifier-c1] commit
      [~DeviceA-classifier-c1] quit
      ```
      
      # Configure a traffic classifier named **c2**.
      
      ```
      [~DeviceA] traffic classifier c2 operator or
      [*DeviceA-classifier-c2] if-match acl 6021
      [*DeviceA-classifier-c2] commit
      [~DeviceA-classifier-c2] quit
      ```
   4. Configure traffic behaviors.
      
      # Configure a traffic behavior named **b1**.
      
      ```
      [~DeviceA] traffic behavior b1
      [*DeviceA-behavior-b1] https-redirect
      [*DeviceA-behavior-b1] commit
      [~DeviceA-behavior-b1] quit
      ```
      
      # Configure a traffic behavior named **b2**.
      
      ```
      [~DeviceA] traffic behavior b2
      [*DeviceA-behavior-b2] https-redirect
      [*DeviceA-behavior-b2] commit
      [~DeviceA-behavior-b2] quit
      ```
   5. Configure a traffic policy.
      
      # Configure an EDSG traffic policy named **traffic\_policy\_edsg**, and bind traffic classifiers **c1** and **c2** to traffic behaviors **b1** and **b2**, respectively.
      
      ```
      [~DeviceA] traffic policy traffic_policy_edsg
      [*DeviceA-policy-traffic_policy_edsg] share-mode
      [*DeviceA-policy-traffic_policy_edsg] classifier c1 behavior b1
      [*DeviceA-policy-traffic_policy_edsg] classifier c2 behavior b2
      [*DeviceA-policy-traffic_policy_edsg] commit
      [~DeviceA-policy-traffic_policy_edsg] quit
      ```
   6. Apply the EDSG traffic policy globally.
      ```
      [~DeviceA] traffic-policy traffic_policy_edsg inbound
      [*DeviceA] traffic-policy traffic_policy_edsg outbound
      [*DeviceA] commit
      ```
5. Configure a local address pool.
   
   # Configure a local address pool named **edsg\_pool**. Then, set the gateway address to 172.31.0.0/16 and specify the address segment ranging from 172.31.0.1 to 172.31.255.255 for user access.
   
   ```
   [~DeviceA] ip pool edsg_pool bas local
   [*DeviceA-ip-pool-edsg_pool] gateway 172.31.0.0 255.255.0.0
   [*DeviceA-ip-pool-edsg_pool] commit
   [~DeviceA-ip-pool-edsg_pool] section 0 172.31.0.1 172.31.255.255
   [~DeviceA-ip-pool-edsg_pool] quit
   ```
6. Configure an AAA authentication scheme and accounting scheme, and bind the address pool to the RADIUS server group in the AAA domain.
   
   # Configure an AAA authentication scheme named **auth1** and set the authentication mode to RADIUS authentication.
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] authentication-scheme auth1
   [*DeviceA-aaa-authen-auth1] authentication-mode radius
   [*DeviceA-aaa-authen-auth1] quit
   ```
   
   # Configure an AAA accounting scheme named **acct1** and set the accounting mode to RADIUS accounting.
   
   ```
   [*DeviceA-aaa] accounting-scheme acct1
   [*DeviceA-aaa-accounting-acct1] accounting-mode radius
   [*DeviceA-aaa-accounting-acct1] quit
   [*DeviceA-aaa] commit
   ```
   
   # Bind the address pool to the RADIUS server group in the AAA domain.
   
   ```
   [~DeviceA-aaa] domain domain1
   [*DeviceA-aaa-domain-domain1] commit
   [~DeviceA-aaa-domain-domain1] ip-pool edsg_pool
   [~DeviceA-aaa-domain-domain1] radius-server group rad_group1
   [*DeviceA-aaa-domain-domain1] commit
   [~DeviceA-aaa-domain-domain1] quit
   [~DeviceA-aaa] quit
   ```
7. Configure a mode in which EDSG service policies are downloaded.
   
   # Configure the BRAS to choose locally configured EDSG service policies in priority. If no EDSG service policy is locally configured, the BRAS then selects the EDSG service policies downloaded from the RADIUS server.
   
   ```
   [~DeviceA] service-policy download local radius rad_group1 password cipher YsHsjx_202206
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure EDSG service policies.
   1. Configure an EDSG service policy for access to network 1.
      
      # Create an EDSG service policy named **service\_edsg1**.
      
      ```
      [~DeviceA] service-policy name service_edsg1 edsg
      ```
      
      # Configure the EDSG service policy **service\_edsg1**.
      
      ```
      [~DeviceA-service-policy-service_edsg1] service-group s_1m
      [~DeviceA-service-policy-service_edsg1] radius-server group rad_group1
      [~DeviceA-service-policy-service_edsg1] authentication-scheme auth1
      [~DeviceA-service-policy-service_edsg1] accounting-scheme acct1
      [~DeviceA-service-policy-service_edsg1] rate-limit cir 1000 inbound
      [~DeviceA-service-policy-service_edsg1] rate-limit cir 1000 outbound
      [~DeviceA-service-policy-service_edsg1] quit
      ```
   2. Configure an EDSG service policy for access to network 2.
      
      # Configure the EDSG service policy **service\_edsg2**.
      
      ```
      [~DeviceA] service-policy name service_edsg2 edsg
      [~DeviceA-service-policy-service_edsg2] service-group s_2m
      [~DeviceA-service-policy-service_edsg2] radius-server group rad_group1
      [~DeviceA-service-policy-service_edsg2] authentication-scheme auth1
      [~DeviceA-service-policy-service_edsg2] accounting-scheme acct1
      [~DeviceA-service-policy-service_edsg2] rate-limit cir 2000 inbound
      [~DeviceA-service-policy-service_edsg2] rate-limit cir 2000 outbound
      [~DeviceA-service-policy-service_edsg2] quit
      ```
9. Configure the prepaid function.
   1. Configure a prepaid profile for user access to network 1.
      ```
      [~DeviceA] prepaid-profile prepaid1
      [~DeviceA-prepaid-profile-prepaid1] radius-server group rad_group1
      [~DeviceA-prepaid-profile-prepaid1] authentication-scheme auth1
      [~DeviceA-prepaid-profile-prepaid1] accounting-scheme acct1
      [~DeviceA-prepaid-profile-prepaid1] password cipher YsHsjx_202206
      [*DeviceA-prepaid-profile-prepaid1] threshold time 60 seconds
      [*DeviceA-prepaid-profile-prepaid1] threshold volume 10 mbytes
      [*DeviceA-prepaid-profile-prepaid1] commit
      [~DeviceA-prepaid-profile-prepaid1] quit
      ```
   2. Configure a prepaid profile for user access to network 2.
      ```
      [~DeviceA] prepaid-profile prepaid2
      [~DeviceA-prepaid-profile-prepaid2] radius-server group rad_group1
      [~DeviceA-prepaid-profile-prepaid2] authentication-scheme auth1
      [~DeviceA-prepaid-profile-prepaid2] accounting-scheme acct1
      [~DeviceA-prepaid-profile-prepaid2] password cipher YsHsjx_202206
      [*DeviceA-prepaid-profile-prepaid2] threshold time 300 seconds
      [*DeviceA-prepaid-profile-prepaid2] threshold volume 20 mbytes
      [*DeviceA-prepaid-profile-prepaid2] commit
      [~DeviceA-prepaid-profile-prepaid2] quit
      ```
   3. Configure the policies to be used when the quota is exhausted.
      
      # Configure the BRAS to deactivate services when the quota for user access to network 1 is exhausted.
      
      ```
      [~DeviceA] prepaid-profile prepaid1
      [~DeviceA-prepaid-profile-prepaid1] quota-out service deactivate
      [~DeviceA-prepaid-profile-prepaid1] quit
      ```
      
      # Configure the BRAS to perform HTTPS redirect when the quota for user access to network 2 is exhausted.
      
      ```
      [~DeviceA] http-redirect-profile http_redirect_profile
      [~DeviceA-redirect-profile-http_redirect_profile] web-server url http://www.huawei.com
      [~DeviceA-redirect-profile-http_redirect_profile] web-server mode post
      [~DeviceA-redirect-profile-http_redirect_profile] quit
      [~DeviceA] prepaid-profile prepaid2
      [~DeviceA-prepaid-profile-prepaid2] quota-out redirect http_redirect_profile
      [~DeviceA-prepaid-profile-prepaid2] quit
      ```
   4. Apply prepaid profiles in the EDSG service policy view.
      
      # Apply the prepaid profile **prepaid1** to the EDSG service policy **service\_edsg1**.
      
      ```
      [~DeviceA] service-policy name service_edsg1 edsg
      [~DeviceA-service-policy-service_edsg1] prepaid-profile prepaid1
      [~DeviceA-service-policy-service_edsg1] quit
      ```
      
      # Apply the prepaid profile **prepaid2** to the EDSG service policy **service\_edsg2**.
      
      ```
      [~DeviceA] service-policy name service_edsg2 edsg
      [~DeviceA-service-policy-service_edsg2] prepaid-profile prepaid2
      [~DeviceA-service-policy-service_edsg2] quit
      ```
10. Configure BAS interfaces, upstream interfaces, and an interface connecting the BRAS to servers.
    1. Create a virtual template.
       ```
       [~DeviceA] interface Virtual-Template 1
       [*DeviceA-Virtual-Template1] commit
       [~DeviceA-Virtual-Template1] quit
       ```
    2. Configure BAS interfaces.
       ```
       
       [~DeviceA] interface GigabitEthernet0/1/2.1
       [*DeviceA-GigabitEthernet0/1/2.1] commit
       [~DeviceA-GigabitEthernet0/1/2.1] user-vlan 1 1000 qinq 100
       [~DeviceA-GigabitEthernet0/1/2.1-vlan-1-1000-QinQ-100-100] quit
       [~DeviceA-GigabitEthernet0/1/2.1] pppoe-server bind virtual-template 1
       [*DeviceA-GigabitEthernet0/1/2.1] commit
       [~DeviceA-GigabitEthernet0/1/2.1] bas
       [~DeviceA-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain pre-authentication domain1
       [*DeviceA-GigabitEthernet0/1/2.1-bas] authentication-method ppp web
       [*DeviceA-GigabitEthernet0/1/2.1-bas] commit
       [~DeviceA-GigabitEthernet0/1/2.1-bas] quit
       [~DeviceA-GigabitEthernet0/1/2.1] quit
       ```
    3. Configure upstream interfaces.
       ```
       [~DeviceA] interface GigabitEthernet0/1/0.1
       [*DeviceA-GigabitEthernet0/1/0.1] vlan-type dot1q 1
       [*DeviceA-GigabitEthernet0/1/0.1] ip address 192.168.100.1 255.255.255.0
       [*DeviceA-GigabitEthernet0/1/0.1] commit
       [~DeviceA-GigabitEthernet0/1/0.1] quit
       [*DeviceA] interface GigabitEthernet0/1/0.2
       [*DeviceA-GigabitEthernet0/1/0.2] vlan-type dot1q 1
       [*DeviceA-GigabitEthernet0/1/0.2] ip address 192.168.200.1 255.255.255.0
       [*DeviceA-GigabitEthernet0/1/0.2] commit
       [~DeviceA-GigabitEthernet0/1/0.2] quit
       ```
    4. Configure an interface connecting the BRAS to the policy server, AAA server, and portal server.
       ```
       [~DeviceA] interface GigabitEthernet0/1/1
       [~DeviceA-GigabitEthernet0/1/1] ip address 10.10.10.1 255.255.255.0
       [*DeviceA-GigabitEthernet0/1/1] commit
       [~DeviceA-GigabitEthernet0/1/1] quit
       ```
11. Configure online users.
    
    # Configure the RADIUS server to deliver the RADIUS attribute User-Password with a value of **YsHsjx\_202206** for PPPoE user 1 and PPPoE user 2.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The shared key configured for a RADIUS server group determines the value of the User-Password attribute.
    
    # Configure the AAA server to deliver the RADIUS attribute HW-Account-Info containing Aservice\_edsg1 for user 1.
    
    # Configure the AAA server to deliver the RADIUS attribute HW-Account-Info containing Aservice\_edsg2 for user 2.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The HW-Account-Info attribute starting with **A** followed by a service policy name is used in authentication response packets to deliver EDSG services that automatically take effect after being delivered.
12. Set user 1's prepaid time on the AAA server.
    
    # Configure the AAA server to deliver the RADIUS attribute Session-Timeout with a value of 120s for user 1. This attribute indicates the remaining available time of the EDSG service.
    
    # Display the online user IDs of the EDSG service.
    
    ```
    <DeviceA> display value-added-service user edsg
    The used user id tables are: 
        128000 
        128001 
    ```
    
    # Display information about the EDSG service with a user ID of 128000 and a service index of 0 when the user has used the EDSG service for 60s.
    
    ```
    <DeviceA> display value-added-service user user-id 128000 edsg service-index 0   
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
    
    # Display service deactivation records. The command output shows that the EDSG service automatically becomes invalid after the user has been online for more than 120s.
    
    ```
    <DeviceA> display service deactivate-record
     ------------------------------------------------------------------- 
      Policy name        : service_edsg1 
      User ID            : 128000 
      Service index      : 0 
      Access time        : 2013-10-17 17:41:03 
      Deactivate time    : 2013-10-17 17:45:33 
      Deactivate reason  : The server does not reply with prepaid authorization response 
    ```
    
    # Display information about HTTPS redirect with a cipher suite configured.
    
    ```
    <DeviceA> system-view
    [~DeviceA] display access https-redirect information
    ---------------------------------------------  
    Certificate source        : Imported  
    ---------------------------------------------  
    Imported certificate info  
    --------------------------------------------- 
    Last import time         : 2020-03-27 16:16:01  
    Last delete time         : 2020-03-27 03:17:04  
    Imported cert file       : cert.der key der key.der  
    Imported cert file size  : 924 (Bytes)  
    Certificate valid time   : 2020-03-27 03:26:44---2021-03-27 03:26:44  
    Pub key                  : RSA (1024 Bits)  
    ---------------------------------------------  
    Self-signed certificate info  
    ---------------------------------------------  
    Pub key                  : RSA (2048 Bits)  
    ---------------------------------------------  
    Supported cipher-suites   
    ---------------------------------------------  
    c02b: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256(TLS1.2)
    c02f: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256(TLS1.2)  
    1301: TLS_AES_128_GCM_SHA256(TLS1.3)  
    1302: TLS_AES_256_GCM_SHA384(TLS1.3)  
    --------------------------------------------- 
    ```
13. Configure user 2's prepaid volume on the AAA server.
    
    # Configure the AAA server to deliver the RADIUS attribute HW-Remanent-Volume with a value of 100 MB for user 2. This attribute indicates the remaining available volume of the user.
    
    # Display status information of the prepaid profile **prepaid2**.
    
    ```
    <DeviceA> display prepaid-profile name prepaid2
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
       Service Volumequota apply direction: both
      ------------------------------------------------                                     
    ```
    
    # Display detailed information about the EDSG service with a user ID of 128001 and a service index of 0.
    
    ```
    <DeviceA> display value-added-service user user-id 128001 edsg service-index 0
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

```
# 
sysname DeviceA 
# 
radius-server group rad_group1 
 radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%# 
 radius-server authentication 10.10.10.2 1812 weight 0 
 radius-server accounting 10.10.10.2 1813 weight 0  
# 
ip pool edsg_pool bas local 
 gateway 172.31.0.0 255.255.0.0 
 section 0 172.31.0.1 172.31.255.255
#                               
service-policy download local radius rad_group1 password cipher %^%#_;S_ObuBtODzOCB>_@#1|r!6-f+>*9wXMO'wBv`2%^%# 
#
access https-redirect
 self-signed rsa modulus 2048
 cipher-suite support c02f c02b 1301 1302
# 
value-added-service enable 
# 
service-group s_1m 
service-group s_2m 
# 
acl number 6020 
 rule 5 permit tcp source service-group s_1m destination ip-address 192.168.100.0 0.0.0.255 destination-port eq 443  
# 
acl number 6021 
 rule permit tcp source service-group s_2m destination ip-address 192.168.200.0 0.0.0.255 destination-port eq 443 
# 
traffic classifier c1 operator or 
 if-match acl 6020 
# 
traffic classifier c2 operator or 
 if-match acl 6021 
# 
traffic behavior b1 
 https-redirect
# 
traffic behavior b2 
 https-redirect
# 
traffic policy traffic_policy_edsg            
 share-mode 
 classifier c1 behavior b1 
 classifier c2 behavior b2  
# 
aaa 
 #
 authentication-scheme auth1 
  authentication-mode radius 
 #
 accounting-scheme acct1 
  accounting-mode radius 
 #
 domain domain1 
  radius-server group rad_group1 
  ip-pool edsg_pool
#  
http-redirect-profile http_redirect_profile                                      
 web-server url http://www.huawei.com                                               
 web-server mode post                                                            
#                                                
prepaid-profile prepaid1                                                         
 password cipher %^%#w^Mc//[^xWxy<`A;jX:)+XW8(CHcPWNdpsP@:^n'%^%#                                
 authentication-scheme auth1                                                     
 accounting-scheme acct1                                                         
 radius-server group rad_group1                                                      
 threshold time 60 seconds                                                       
 threshold volume 10 mbytes                                                      
#                                          
prepaid-profile prepaid2                                                         
 password cipher %^%#9f(T=Ew#*(aAnoEm{<vWpE{NJ6{IH+8V*]M.ZRV*%^%#                                
 uthentication-scheme auth1                                                     
 accounting-scheme acct1                                                         
 radius-server group rad_group1                                                      
 threshold time 300 seconds                                                      
 threshold volume 20 mbytes                                                      
 quota-out redirect http_redirect_profile                                        
# 
service-policy name service_edsg1 edsg 
 service-group s_1m
 radius-server group rad_group1 
 authentication-scheme auth1 
 accounting-scheme acct1 
 rate-limit cir 1000 inbound 
 rate-limit cir 1000 outbound 
 prepaid-profile prepaid1 
# 
service-policy name service_edsg2 edsg 
 service-group s_2m
 radius-server group rad_group1 
 authentication-scheme auth1 
 accounting-scheme acct1 
 rate-limit cir 2000 inbound 
 rate-limit cir 2000 outbound 
 prepaid-profile prepaid2 
# 
interface GigabitEthernet0/1/1 
 ip address 10.10.10.1 255.255.255.0 
# 
interface GigabitEthernet0/1/0.1 
 vlan-type dot1q 1 
 ip address 192.168.100.1 255.255.255.0 
# 
interface GigabitEthernet0/1/0.2 
 vlan-type dot1q 2 
 ip address 192.168.200.1 255.255.255.0 
# 
interface GigabitEthernet0/1/2
#
interface GigabitEthernet0/1/2.1
 user-vlan 1 1000 qinq 100 
 bas 
 # 
  access-type layer2-subscriber default-domain pre-authentication domain1 
  authentication-method ppp web   
# 
traffic-policy traffic_policy_edsg inbound 
traffic-policy traffic_policy_edsg outbound
# 
return
```