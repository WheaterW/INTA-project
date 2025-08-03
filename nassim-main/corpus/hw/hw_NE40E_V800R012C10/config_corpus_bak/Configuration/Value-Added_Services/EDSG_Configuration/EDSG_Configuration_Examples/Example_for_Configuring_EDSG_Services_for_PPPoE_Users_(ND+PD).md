Example for Configuring EDSG Services for PPPoE Users (ND+PD)
=============================================================

After PPPoE users send access requests to a BRAS and are authenticated, EDSG services are delivered by the RADIUS server through user authentication packets. You can configure the uplink and downlink bandwidths for EDSG service policies and use ACL rules to match the destination addresses and distinguish network segments for user access, achieving independent rate limiting for different network segments.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0257901159__fig_dc_ne_cfg_edsg_000801), PPPoE users access network 1 and network 2. Different fees need to be charged for traffic over networks 1 and 2. The users have different bandwidth requirements for networks 1 and 2. The uplink and downlink traffic bandwidths for access to network 1 and network 2 are limited to 1 Mbit/s and 2 Mbit/s, respectively. The RADIUS server functions as both an AAA server and an EDSG service policy server. The EDSG service policy server uses RADIUS to deliver EDSG service policies in which parameters, such as the authentication mode, accounting mode, and bandwidths for uplink and downlink traffic rate limit, are specified.

**Figure 1** EDSG service networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, subinterface2.1, and subinterface2.2 represent GE0/1/2.100, GE0/1/1.1, and GE0/1/1.2, respectively.


  
![](figure/en-us_image_0257901160.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable the VAS function.
2. Configure AAA schemes and a RADIUS server.
3. Configure an EDSG traffic policy.
4. Configure a mode in which EDSG service policies are downloaded.
5. Configure the RADIUS server to deliver EDSG service policies. (This step is performed on the RADIUS server.)
6. Configure address pools.
7. Configure an AAA domain.
8. Configure interfaces.
9. Configure IP routes. IS-IS is used as an example.
10. Configure access users. (This step is performed on the RADIUS server.)


#### Data Preparation

To complete the configuration, you need the following data:

* Policy server parameters, such as the IP address and port number
* EDSG traffic policy parameters, such as the service group name, ACL rule, traffic classifier, traffic behavior, and traffic policy
* Name of the local address pool used in the domain, gateway address, and address pool range
* EDSG service policy parameters, such as the mode in which EDSG service policies are downloaded, EDSG service policy name, name of the bound RADIUS server group, RADIUS authentication scheme, RADIUS accounting scheme, and bandwidths for uplink and downlink traffic rate limiting for EDSG services


#### Procedure

1. Set the host name of the BRAS to **HUAWEI**.
   
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname HUAWEI
   ```
   ```
   [*Device] commit
   ```
2. Configure the BRAS to generate DUIDs in DUID-LLT mode. (This step is not required if a DUID has been configured on the BRAS.)
   
   
   ```
   [~HUAWEI] dhcpv6 duid llt
   ```
   ```
   [*HUAWEI] commit
   ```
3. Enable the VAS function.
   
   
   ```
   [~HUAWEI] value-added-service enable
   ```
   ```
   [*HUAWEI] commit
   ```
4. Configure AAA.
   
   
   
   # Configure an authentication scheme and set the authentication mode to RADIUS.
   
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
   
   # Configure an accounting scheme and set the accounting mode to RADIUS.
   
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
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   
   
   
   # Configure a RADIUS server that functions as both an AAA server and an EDSG service policy server.
   
   ```
   [~HUAWEI] radius-server group radius
   ```
   ```
   [*HUAWEI-radius-radius] radius-server authentication 10.10.10.2 1812
   ```
   ```
   [*HUAWEI-radius-radius] radius-server accounting 10.10.10.2 1813
   ```
   ```
   [*HUAWEI-radius-radius] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-radius-radius] commit
   ```
   ```
   [~HUAWEI-radius-radius] quit
   ```
5. Configure an EDSG traffic policy.
   1. Create service groups.
      
      
      ```
      [~HUAWEI] service-group s_1m
      [*HUAWEI] service-group s_2m
      [*HUAWEI] commit
      ```
   2. Configure ACL rules for service groups.
      
      
      
      # Configure an IPv4 ACL numbered 6020 for the service group **s\_1m** to match the IPv4 packets between the service group **s\_1m** and network 1.
      
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
      
      # Configure an IPv6 ACL numbered 6020 for the service group **s\_1m** to match the IPv6 packets between the service group **s\_1m** and network 1.
      
      ```
      [~HUAWEI] acl ipv6 number 6020
      ```
      ```
      [*HUAWEI-acl6-ucl-6020] rule 10 permit ipv6 source service-group s_1m destination ipv6-address 2001:db8::2/64
      ```
      ```
      [*HUAWEI-acl6-ucl-6020] rule 20 permit ipv6 source ipv6-address 2001:db8::2/64 destination service-group s_1m
      ```
      ```
      [*HUAWEI-acl6-ucl-6020] commit
      ```
      ```
      [~HUAWEI-acl6-ucl-6020] quit
      ```
      
      # Configure an IPv4 ACL numbered 6021 for the service group **s\_2m** to match the IPv4 packets between the service group **s\_2m** and network 2.
      
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
      
      # Configure an IPv6 ACL numbered 6021 for the service group **s\_2m** to match the IPv6 packets between the service group **s\_2m** and network 2.
      
      ```
      [~HUAWEI] acl ipv6 number 6021
      ```
      ```
      [*HUAWEI-acl6-ucl-6021] rule 15 permit ipv6 source service-group s_2m destination ipv6-address 2001:db8:1::2/64
      ```
      ```
      [*HUAWEI-acl6-ucl-6021] rule 25 permit ipv6 source ipv6-address 2001:db8:1::2/64 destination service-group s_2m
      ```
      ```
      [*HUAWEI-acl6-ucl-6021] commit
      ```
      ```
      [~HUAWEI-acl6-ucl-6021] quit
      ```
   3. Configure traffic classifiers.
      
      
      
      # Configure a traffic classifier named **c1**.
      
      ```
      [~HUAWEI] traffic classifier c1 operator or
      ```
      ```
      [*HUAWEI-classifier-c1] if-match acl 6020
      ```
      ```
      [*HUAWEI-classifier-c1] if-match ipv6 acl 6020
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
      [*HUAWEI-classifier-c2] if-match ipv6 acl 6021
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
      [*HUAWEI] commit
      ```
6. Configure a mode in which EDSG service policies are downloaded.
   
   
   
   # Configure the RADIUS mode for downloading EDSG service policies. In this mode, EDSG service policies are downloaded from the RADIUS server through authentication packets.
   
   ```
   [~HUAWEI] service-policy download radius radius password cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI] commit
   ```
7. Configure EDSG service policies. (This step is performed on the RADIUS server.)
   1. Configure an EDSG service policy for access to network 1.
      
      
      
      # Configure the RADIUS server to deliver the RADIUS attribute User-Password with a value of **YsHsjx\_202206** for the service policy **service\_edsg1**.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The shared key configured for a RADIUS server group determines the value of the User-Password attribute.
      
      
      # Configure the RADIUS server to deliver the RADIUS attribute Huawei-AVpair (vendor ID=2011; attribute number=188) for the service policy **service\_edsg1**.
      * <service:service-group>: The service group **s\_1m** is bound to the service policy **service\_edsg1**.
        
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
      * <service:service-group>: The service group **s\_2m** is bound to the service policy **service\_edsg2**.
        
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
8. Configure an IPv4 address pool.
   
   
   ```
   [~HUAWEI] ip pool edsg_pool bas local
   ```
   ```
   [*HUAWEI-ip-pool-edsg_pool] gateway 172.16.100.1 24
   ```
   ```
   [*HUAWEI-ip-pool-edsg_pool] commit
   ```
   ```
   [~HUAWEI-ip-pool-edsg_pool] section 0 172.16.100.2 172.16.100.200
   ```
   ```
   [*HUAWEI-ip-pool-edsg_pool] dns-server 10.179.155.161 10.179.155.177
   ```
   ```
   [*HUAWEI-ip-pool-edsg_pool] commit
   ```
   ```
   [~HUAWEI-ip-pool-edsg_pool] quit
   ```
9. Configure IPv6 address pools.
   
   # Configure a delegation prefix pool for ND users.
   ```
   [~HUAWEI] ipv6 prefix pre_nd delegation
   ```
   ```
   [~HUAWEI-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48 delegating-prefix-length 64
   ```
   ```
   [~HUAWEI-ipv6-prefix-pre_nd] slaac-unshare-only
   ```
   ```
   [*HUAWEI-ipv6-prefix-pre_nd] commit
   ```
   ```
   [~HUAWEI-ipv6-prefix-pre_nd] quit
   ```
   
   # Configure a delegation address pool for ND users.
   ```
   [~HUAWEI] ipv6 pool pool_nd bas delegation
   ```
   ```
   [~HUAWEI-ipv6-pool-pool_nd] prefix pre_nd
   ```
   ```
   [*HUAWEI-ipv6-pool-pool_nd] commit
   ```
   ```
   [~HUAWEI-ipv6-pool-pool_nd] dns-server 2001:db8::2:2 2001:db8::2:3
   ```
   ```
   [~HUAWEI-ipv6-pool-pool_nd] quit
   ```
   
   # Configure a delegation prefix pool for PD users.
   ```
   [~HUAWEI] ipv6 prefix pre_pd delegation
   ```
   ```
   [~HUAWEI-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
   ```
   ```
   [~HUAWEI-ipv6-prefix-pre_pd] pd-unshare-only
   ```
   ```
   [~HUAWEI-ipv6-prefix-pre_pd] quit
   ```
   
   # Configure a delegation address pool for PD users.
   ```
   [~HUAWEI] ipv6 pool pool_pd bas delegation
   ```
   ```
   [~HUAWEI-ipv6-pool-pool_pd] prefix pre_pd
   ```
   ```
   [*HUAWEI-ipv6-pool-pool_pd] commit
   ```
   ```
   [~HUAWEI-ipv6-pool-pool_pd] dns-server 2001:db8::2:2 2001:db8::2:3
   ```
   ```
   [~HUAWEI-ipv6-pool-pool_pd] quit
   ```
10. Bind the address pools, AAA schemes, and RADIUS server group to an AAA domain.
    
    
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
    [*HUAWEI-aaa-domain-isp1] radius-server group radius
    ```
    ```
    [*HUAWEI-aaa-domain-isp1] commit
    ```
    ```
    [~HUAWEI-aaa-domain-isp1] prefix-assign-mode unshared
    ```
    ```
    [~HUAWEI-aaa-domain-isp1] ip-pool edsg_pool
    ```
    ```
    [~HUAWEI-aaa-domain-isp1] ipv6-pool pool_nd
    ```
    ```
    [~HUAWEI-aaa-domain-isp1] ipv6-pool pool_pd
    ```
    ```
    [~HUAWEI-aaa-domain-isp1] quit
    ```
    ```
    [~HUAWEI-aaa] quit
    ```
11. Configure interfaces.
    
    
    
    # Create a VT.
    
    ```
    [~HUAWEI] interface Virtual-Template 1
    ```
    ```
    [*HUAWEI] ppp authentication-mode chap
    ```
    ```
    [*HUAWEI-Virtual-Template1] commit
    ```
    ```
    [~HUAWEI-Virtual-Template1] quit
    ```
    
    # Configure a BAS interface for PPPoE users.
    
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/2.100
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.100] pppoe-server bind virtual-template 1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.100] ipv6 enable
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.100] ipv6 address auto link-local
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/2.100] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.100] user-vlan 3074 qinq 3074
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2-vlan-3074-3074-QinQ-3074-3074] bas
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.100-bas] access-type layer2-subscriber default-domain authentication isp1
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.100-bas] authentication-method ppp web
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.100-bas] quit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/2.100] quit
    ```
    
    # Configure network-side interfaces and enable IPv6 on these interfaces.
    
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/1.1
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] ipv6 enable
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] ipv6 address 2001:db8:0200:2:2102:2205:1:1 64
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] ipv6 address auto link-local
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] ip address 192.168.100.1 24
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.1] quit
    ```
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/1.2
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.2] ipv6 enable
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.2] ipv6 address 2001:db8:0201:2:2102:2205:1:1 64
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.2] ipv6 address auto link-local
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.2] ip address 192.168.200.1 24
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.2] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.2] quit
    ```
    # Configure the loopback 0 interface and enable IPv6 on this interface.
    ```
    [~HUAWEI] interface Loopback0
    ```
    ```
    [*HUAWEI-LoopBack0] ipv6 enable
    ```
    ```
    [*HUAWEI-LoopBack0] ipv6 address 2001:db8:0200::2205 128
    ```
    ```
    [*HUAWEI-LoopBack0] ipv6 address auto link-local
    ```
    ```
    [*HUAWEI-LoopBack0] ip address 10.10.10.10 16
    ```
    ```
    [*HUAWEI-LoopBack0] commit
    ```
    ```
    [~HUAWEI-LoopBack0] quit
    ```
12. Configure basic IS-IS functions.
    
    # Create an IS-IS process, and enable IPv6 for this process.
    ```
    [~HUAWEI] isis 100
    ```
    ```
    [*HUAWEI-isis-100] cost-style wide
    ```
    ```
    [*HUAWEI-isis-100] ipv6 enable topology ipv6                
    ```
    ```
    [*HUAWEI-isis-100] ipv6 preference 105
    ```
    ```
    [*HUAWEI-isis-100] commit
    ```
    ```
    [~HUAWEI-isis-100] quit
    ```
    
    # Configure IS-IS interfaces. (The cost values can be planned as needed.)
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/1.1
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.1] isis enable 100
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] isis ipv6 enable 100
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] isis ipv6 cost 61
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.1] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.1] quit
    ```
    ```
    [~HUAWEI] interface GigabitEthernet 0/1/1.2
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.2] isis enable 100
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.2] isis ipv6 enable 100
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.2] isis ipv6 cost 62
    ```
    ```
    [*HUAWEI-GigabitEthernet0/1/1.2] commit
    ```
    ```
    [~HUAWEI-GigabitEthernet0/1/1.2] quit
    ```
    ```
    [~HUAWEI] interface loopback0
    ```
    ```
    [~HUAWEI-LoopBack0] isis enable 100
    ```
    ```
    [*HUAWEI-LoopBack0] isis ipv6 enable 100
    ```
    ```
    [*HUAWEI-LoopBack0] commit
    ```
    ```
    [~HUAWEI-LoopBack0] quit
    ```
13. Configure access users. (This step is performed on the RADIUS server.)
    
    
    
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
14. Verify the configuration.
    
    
    
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
dhcpv6 duid llt
#
value-added-service enable
#
radius-server group radius
 radius-server shared-key-cipher %^%#yp(NBJ@lRGH\VOIu>g^5;;Wg@}YoR7/BfHIm:/@~%^%#
 radius-server authentication 10.10.10.2 1812 weight 0
 radius-server accounting 10.10.10.2 1813 weight 0
#
service-group s_1m
service-group s_2m
#
acl number 6020
 rule 10 permit ip source service-group s_1m destination ip-address 192.168.100.0 0.0.0.255
 rule 20 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group s_1m
#
acl ipv6 number 6020
 rule 10 permit ipv6 source service-group s_1m destination ipv6-address 2001:db8::2/64
 rule 20 permit ipv6 source ipv6-address 2001:db8::2/64 destination service-group s_1m
#
acl number 6021
 rule 15 permit ip source service-group s_2m destination ip-address 192.168.200.0 0.0.0.255
 rule 25 permit ip source ip-address 192.168.200.0 0.0.0.255 destination service-group s_2m
#
acl ipv6 number 6021
 rule 15 permit ipv6 source service-group s_2m destination ipv6-address 2001:db8:1::2/64
 rule 25 permit ipv6 source ipv6-address 2001:db8:1::2/64 destination service-group s_2m
#
traffic classifier c1 operator or
 if-match acl 6020 precedence 1
 if-match ipv6 acl 6020 precedence 2
#
traffic classifier c2 operator or
 if-match acl 6021 precedence 1
 if-match ipv6 acl 6021 precedence 2
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
ip pool edsg_pool bas local
 gateway 172.16.100.1 255.255.255.0
 section 0 172.16.100.2 172.16.100.200
 dns-server 10.179.155.161 10.179.155.177
#
ipv6 prefix pre_nd delegation
 prefix 2001:DB8:1::/48 delegating-prefix-length 64
 slaac-unshare-only
#
ipv6 prefix pre_pd delegation
 prefix 2001:DB8:2::/48 delegating-prefix-length 60
 pd-unshare-only
#
ipv6 pool pool_nd bas delegation
 dns-server 2001:DB8::2:2 2001:DB8::2:3
 prefix pre_nd
#
ipv6 pool pool_pd bas delegation
 dns-server 2001:DB8::2:2 2001:DB8::2:3
 prefix pre_pd
#
aaa
 authentication-scheme auth1
  authentication-mode radius
 #
 accounting-scheme acct1
  accounting-mode radius
 #
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group radius
  prefix-assign-mode unshared
  ip-pool edsg_pool
  ipv6-pool pool_nd
  ipv6-pool pool_pd
 #
#
isis 100
 cost-style wide
 #
 ipv6 enable topology ipv6
 ipv6 preference 105
 #
#
interface Virtual-Template 1
 ppp authentication-mode chap
#
interface GigabitEthernet0/1/2.100
 ipv6 enable
 ipv6 address auto link-local
 user-vlan 3074 qinq 3074
 pppoe-server bind Virtual-Template 1
 bas
 #
  access-type layer2-subscriber default-domain authentication isp1
  authentication-method ppp web
 #
#
interface GigabitEthernet0/1/1.1
 ipv6 enable
 ipv6 address 2001:DB8:200:2:2102:2205:1:1/64
 ipv6 address auto link-local
 ip address 192.168.100.1 24
 isis enable 100
 isis ipv6 enable 100
 isis ipv6 cost 61
 #
#
interface GigabitEthernet0/1/1.2
 ipv6 enable
 ipv6 address 2001:DB8:201:2:2102:2205:1:1/64
 ipv6 address auto link-local
 ip address 192.168.200.1 24
 isis enable 100
 isis ipv6 enable 100
 isis ipv6 cost 62 
 #
#
interface LoopBack0
 ipv6 enable
 ip address 10.10.10.10 255.255.0.0
 ipv6 address 2001:DB8:200::2205/128
 ipv6 address auto link-local
 isis enable 100
 isis ipv6 enable 100
#
return
```