Example for Configuring RUI+EDSG in Shared Address Pool Mode
============================================================

This section provides an example for configuring RUI+EDSG in shared address pool mode. A networking diagram is provided to help you understand the configuration procedure. This example covers networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Usage Scenario

As IP technologies develop rapidly, various value-added services are widely used on the Internet. Carrier-grade services, such as emerging IPTV, NGN, 4G, VIP customers' private line, and VPN interconnection, place higher requirements for IP network reliability. IP network reliability for carrier-grade services covers device, link, and network reliability. On a transport network, the availability of network devices must reach 99.999%. In other words, the downtime for maintenance during the continuous running of a device in a year is less than 5 minutes. High reliability is a basic requirement for carrier-grade devices and is the foundation upon which telecom carriers must build their networks.

The NE40E is an edge router used to carry multiple services. It plays a vital role on a network. It is uplinked to the core layer to implement the Layer 3 routing function and downlinked to the aggregation layer to terminate Layer 2 user packets for user access. Additionally, it carries multiple services including Triple Play services (HSI, VoIP, and IPTV), requiring high reliability. The NE40E provides service-level high-reliability technologies. Non-stop data flow forwarding does not mean that user services are not interrupted. Instead, if user traffic is switched to a standby device after a network node or link fails and user information is not synchronized to the standby device, user services are still interrupted. High reliability has been considered when the NE40E is designed to function as a network edge service aggregation and control device. This ensures that users' HSI, IPTV, and VoIP services are not interrupted if a network node or link fault occurs. Dual-device hot backup is designed based on this reliability scenario.

#### Requirements on Hardware

User access boards are installed.

#### Requirements on Interconnected Devices

* Upstream device: There are no special requirements. The upstream device is generally a core-layer CR that can exchange routes normally and supports MPLS and MPLS L3VPN. It is recommended that the upstream device be able to provide MPLS L2VPN capabilities. In multi-device hot backup scenarios, MPLS tunnels are best suited to function as protection tunnels. This is because an MPLS protection tunnel can be established from the IP core network if a direct link cannot be deployed between NE40Es.
* Downstream device: An aggregation switch is used as the downstream device to learn MAC addresses from Layer 2 VLAN packets.
#### Solution Limitations

* In shared address pool mode, an address pool (an IP network segment) is planned based on services. Each service (for example, Internet access or VoIP service) corresponds to a domain's configuration. If terminals that go online through different access links have the same service (for example, Internet access service), the terminals share address pool resources in a domain. This mode is called multi-link address pool sharing.
* In actual deployment, planning address pools based on links is difficult. The reason is that the number of public addresses is limited, and dividing address pools causes address resources to be wasted. Therefore, address pools are divided based on authentication domains. This allows an address pool on an MSCG to be shared among multiple links or backup groups. In this case, forwarding control cannot be performed by advertising or withdrawing address pool routes. To implement forwarding control, using a shared address pool and tunnel protection is recommended.
#### Networking Requirements

Carriers can divide networks into different subnets based on traffic destination addresses. When different users access the subnets, different rate limiting and accounting are performed for the users. EDSG implements subnet division, rate limit, and accounting management on BRASs. As applications accessed by users become diversified, high reliability is required for EDSG services. To meet this requirement, deploy RUI so that EDSG service traffic is smoothly switched to the standby device if the master device fails. RUI ensures normal traffic accounting without the need of users' re-dialup.

On the network shown in [Figure 1](#EN-US_TASK_0172374416__fig_ne_rui_edsg_cfg_002), the user goes online from Device A (master device) through PPPoE dialup. Device A and Device B implement RUI over VRRP and BFD. Device A backs up EDSG services to Device B (backup device). If Device A fails, service traffic is switched to Device B. Traffic statistics on Device A and Device B remain consistent.

**Figure 1** Example for configuring RUI+EDSG in shared address pool mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_ne_rui_edsg_cfg_002.png)  

| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE0/1/0 | 10.0.1.1/24 |
| DeviceA | GE0/2/0 | 10.0.0.1/24 |
| DeviceA | GE0/3/0 | 10.1.1.6/24 |
| DeviceA | Loopback0 | 1.1.1.1/32 |
| DeviceA | Loopback1 | 22.22.22.22/32 |
| DeviceB | GE0/1/0 | 10.0.1.2/24 |
| DeviceB | GE0/2/0 | 10.0.2.1/24 |
| DeviceB | GE0/3/0 | 10.1.1.7/24 |
| DeviceB | Loopback0 | 2.2.2.2/32 |
| DeviceB | Loopback1 | 88.88.88.88/32 |





#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic user access functions and ensure that the two devices have the same configuration. For details, see "User Access" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide*.
2. Configure routes to ensure IP connectivity between devices. For details, see "IP Routing" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide*.
3. Establish a multi-device backup platform.
4. Configure an RBS, address pools, and an RBP.
5. Configure a protection path for returned network-side traffic.
6. Bind an RBP to an interface from which the user goes online.
7. Configure EDSG services on Device A and Device B. For details, see "Value-added Service" in *HUAWEI NE40E-M2 series Universal Service Router Multiservice Control Gateway Configuration Guide*.

#### Data Preparation

To complete the configuration, you need the following data:

* VRRP ID
* Interface IP addresses of Routers that back up each other
* Backup ID, which is used together with an RBS to identify the RBP to which the user belongs
* Address pool names
* EDSG-related parameters
* User authentication mode (RADIUS authentication)

#### Procedure

1. Establish a multi-device backup platform. The configuration on Device A is used as an example. The configuration of Device B is similar to the configuration on Device A.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, only RUI-related configuration is described.
   
   # Configure a BFD session named **bfd** on the access side to rapidly detect interface or link faults and trigger a master/backup VRRP switchover. 10.0.1.2 is the IP address of GE 0/1/0.2 on Device B.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] bfd 
   ```
   ```
   [*DeviceA] commit 
   ```
   ```
   [~DeviceA-bfd] quit 
   ```
   ```
   [*DeviceA] bfd bfd bind peer-ip 10.0.1.2 
   ```
   ```
   [*DeviceA-bfd-session-bfd] discriminator local 1 
   ```
   ```
   [*DeviceA-bfd-session-bfd] discriminator remote 2 
   ```
   ```
   [*DeviceA-bfd-session-bfd] commit 
   ```
   ```
   [~DeviceA-bfd-session-bfd] quit 
   ```
   
   # Configure a VRRP group on GE0/1/0.2, and configure the VRRP group to track the BFD session and network-side interface status.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0.2 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] vlan-type dot1q 200
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] ip address 10.0.1.1 255.255.255.0 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] vrrp vrid 1 virtual-ip 10.0.1.100 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] admin-vrrp vrid 1 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] vrrp vrid 1 priority 120 
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] vrrp vrid 1 preempt-mode timer delay 600
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] vrrp vrid 1 track bfd-session 1 peer
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] vrrp vrid 1 track interface gigabitethernet 0/2/0 reduced 50
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] vrrp recover-delay 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.2] commit 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.2] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Different priorities must be configured for devices in a VRRP group. The device with a higher priority is the master device.
2. Configure an RBS, address pools, and an RBP.
   
   
   
   # Configure an RBS.
   
   ```
   [~DeviceA] remote-backup-service service1 
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] peer 88.88.88.88 source 22.22.22.22 port 2046 
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] track interface gigabitethernet 0/2/0 
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] commit 
   ```
   ```
   [~DeviceA-rm-backup-srv-service1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can run the **track bfd-session** command in the RBS view to track the peer BFD sessions established on the network side of the active and standby devices, achieving rapid peer status detection. For configuration details, see the corresponding command reference.
   
   
   # Configure a primary address pool and a backup address pool on Device A (master device).
   ```
   [~DeviceA] ip pool hsi bas local
   [*DeviceA-ip-pool-hsi] gateway 1.1.1.1 24
   [*DeviceA-ip-pool-hsi] commit
   [~DeviceA-ip-pool-hsi] section 0 1.1.1.2 1.1.1.254
   [*DeviceA-ip-pool-hsi] commit 
   [~DeviceA-ip-pool-hsi] quit
   ```
   ```
   [~DeviceA] ip pool hsi-main-bak bas local rui-slave
   [*DeviceA-ip-pool-hsi-main-bak] gateway 2.2.2.2 24
   [*DeviceA-ip-pool-hsi-main-bak] commit 
   [~DeviceA-ip-pool-hsi-main-bak] section 0 2.2.2.3 2.2.2.254
   [*DeviceA-ip-pool-hsi-main-bak] commit 
   [~DeviceA-ip-pool-hsi-main-bak] quit
   ```
   
   # Configure a primary address pool named **hsi-main** and a backup address pool named **local** on Device B.
   
   ```
   [~DeviceB] ip pool hsi-main bas local
   [*DeviceB-ip-pool-hsi-main] gateway 2.2.2.2 24
   [*DeviceB-ip-pool-hsi-main] commit 
   [~DeviceB-ip-pool-hsi-main] section 0 2.2.2.3 2.2.2.254
   [*DeviceB-ip-pool-hsi-main] commit 
   [~DeviceB-ip-pool-hsi-main] quit
   ```
   
   # Configure a secondary address pool named **hsi-bak** and specify it as a hybrid address pool.
   
   ```
   [~DeviceB] ip pool hsi-bak bas local rui-slave
   [*DeviceB-ip-pool-hsi-bak] gateway 1.1.1.1 24
   [*DeviceB-ip-pool-hsi-bak] commit
   [~DeviceB-ip-pool-hsi-bak] section 0 1.1.1.2 1.1.1.254
   [*DeviceB-ip-pool-hsi-bak] commit 
   [~DeviceB-ip-pool-hsi-bak] quit
   ```
   
   # Configure an RBP on Device A and Device B.
   
   ```
   [~DeviceA] remote-backup-profile profile1 
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] peer-backup hot 
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] vrrp-id 1 interface gigabitethernet 0/1/0.2 
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] backup-id 10 remote-backup-service service1 
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] service-type bras 
   ```
   ```
   [*DeviceA-rm-backup-prf-profile1] commit 
   ```
   ```
   [~DeviceA-rm-backup-prf-profile1] quit 
   ```
   ```
   [~DeviceB] remote-backup-profile profile1 
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] peer-backup hot 
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] vrrp-id 1 interface gigabitethernet 0/1/0.2 
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] backup-id 10 remote-backup-service service1 
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] service-type bras 
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] ip-pool hsi include hsi-bak node 5
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] ip-pool hsi-main include hsi-main-bak node 10
   ```
   ```
   [*DeviceB-rm-backup-prf-profile1] commit 
   ```
   ```
   [~DeviceB-rm-backup-prf-profile1] quit 
   ```
3. Bind the configured address pools to the RBS and configure a protection path for returned network-side traffic.
   
   
   ```
   [~DeviceA] remote-backup-service service1 
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] ip-pool hsi
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] ip-pool hsi-bak
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] protect redirect ip-nexthop 10.1.1.7 interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] commit 
   ```
   ```
   [~DeviceB] remote-backup-service service1 
   ```
   ```
   [*DeviceB-rm-backup-srv-service1] ip-pool hsi-main
   ```
   ```
   [*DeviceB-rm-backup-srv-service1] ip-pool hsi-main-bak
   ```
   ```
   [*DeviceB-rm-backup-srv-service1] protect redirect ip-nexthop 10.1.1.6 interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] commit 
   ```
4. Bind the RBP to GE 0/1/0.1 from which users go online. The configuration on Device A is used as an example. The configuration of Device B is similar to the configuration of Device A.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0.1 
   ```
   ```
   [*A-GigabitEthernet0/1/0.1] remote-backup-profile profile1 
   ```
   ```
   [*DeviceA-rm-backup-srv-service1] commit 
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] quit 
   ```
5. Configure EDSG services.
   1. Enable the value-added service function.
      
      
      ```
      [~DeviceA] value-added-service enable
      ```
      ```
      [*DeviceA] commit
      ```
   2. Configure a policy server.
      
      # Set parameters as follows:
      * RADIUS server group name: rad\_group1
      * RADIUS authentication server's IP address: 10.10.10.2
      * RADIUS authentication server's interface number: 1812
      * RADIUS accounting server's IP address: 10.10.10.2
      * RADIUS accounting server's interface number: 1813
      * Shared key for the RADIUS authentication and accounting servers: YsHsjx\_202206
      ```
      [~DeviceA] radius-server group rad_group1
      ```
      ```
      [*DeviceA-radius-rad_group1] radius-server authentication 10.10.10.2 1812
      ```
      ```
      [*DeviceA-radius-rad_group1] radius-server accounting 10.10.10.2 1813
      ```
      ```
      [*DeviceA-radius-rad_group1] radius-server shared-key-cipher YsHsjx_202206
      ```
      ```
      [*DeviceA-radius-rad_group1] commit
      ```
      ```
      [~DeviceA-radius-rad_group1] quit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For details about how to configure a RADIUS server group, see [Configuring a Device as a RADIUS Client](dc_ne_aaa_cfg_0600.html) in *HUAWEI NE40E-M2 series Configuration Guide - User Access*.
   3. Configure an EDSG traffic policy.
      
      
      1. Create service groups.
         
         ```
         [~DeviceA] service-group s_1m
         [*DeviceA] service-group s_2m
         [*DeviceA] commit
         ```
         ![](../../../../public_sys-resources/note_3.0-en-us.png) 
         
         You must run the [**service-group**](cmdqueryname=service-group) command to create service groups regardless of whether the device obtains EDSG service policies from local configurations or a RADIUS server.
      2. Configure an ACL and define ACL rules for each service group.
         
         # Configure ACL 6020 and define ACL rules for the service group named **s\_1m**.
         
         ```
         [~DeviceA] acl number 6020
         ```
         ```
         [*DeviceA-acl-ucl-6020] rule 10 permit ip source service-group s_1m destination ip-address 192.168.100.0 0.0.0.255
         ```
         ```
         [*DeviceA-acl-ucl-6020] rule 20 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group s_1m
         ```
         ```
         [*DeviceA-acl-ucl-6020] commit
         ```
         ```
         [~DeviceA-acl-ucl-6020] quit
         ```
         
         # Configure ACL 6021 and define ACL rules for the service group named **s\_2m**.
         
         ```
         [~DeviceA] acl number 6021
         ```
         ```
         [*DeviceA-acl-ucl-6021] rule 15 permit ip source service-group s_2m destination ip-address 192.168.200.0 0.0.0.255
         ```
         ```
         [*DeviceA-acl-ucl-6021] rule 25 permit ip source ip-address 192.168.200.0 0.0.0.255 destination service-group s_2m
         ```
         ```
         [*DeviceA-acl-ucl-6021] commit
         ```
         ```
         [~DeviceA-acl-ucl-6021] quit
         ```
      3. Define traffic classifiers.
         
         # Define a traffic classifier named **c1**.
         
         ```
         [~DeviceA] traffic classifier c1 operator or
         ```
         ```
         [*DeviceA-classifier-c1] if-match acl 6020
         ```
         ```
         [*DeviceA-classifier-c1] commit
         ```
         ```
         [~DeviceA-classifier-c1] quit
         ```
         
         # Define a traffic classifier named **c2**.
         
         ```
         [~DeviceA] traffic classifier c2 operator or
         ```
         ```
         [*DeviceA-classifier-c2] if-match acl 6021
         ```
         ```
         [*DeviceA-classifier-c2] commit
         ```
         ```
         [~DeviceA-classifier-c2] quit
         ```
      4. Define traffic behaviors.
         
         # Define a traffic behavior named **b1**.
         
         ```
         [~DeviceA] traffic behavior b1
         ```
         ```
         [*DeviceA-behavior-b1] commit
         ```
         ```
         [~DeviceA-behavior-b1] quit
         ```
         
         # Define a traffic behavior **b2**.
         
         ```
         [~DeviceA] traffic behavior b2
         ```
         ```
         [*DeviceA-behavior-b2] commit
         ```
         ```
         [~DeviceA-behavior-b2] quit
         ```
      5. Configure an EDSG traffic policy.
         
         # Configure an EDSG traffic policy named **traffic\_policy\_edsg**, and associate **c1** and **c2** with **b1** and **b2**, respectively.
         
         ```
         [~DeviceA] traffic policy traffic_policy_edsg
         ```
         ```
         [*DeviceA-policy-traffic_policy_edsg] share-mode
         ```
         ```
         [*DeviceA-policy-traffic_policy_edsg] classifier c1 behavior b1
         ```
         ```
         [*DeviceA-policy-traffic_policy_edsg] classifier c2 behavior b2
         ```
         ```
         [*DeviceA-policy-traffic_policy_edsg] commit
         ```
         ```
         [~DeviceA-policy-traffic_policy_edsg] quit
         ```
      6. Apply the EDSG traffic policy globally.
         
         ```
         [~DeviceA] traffic-policy traffic_policy_edsg inbound
         ```
         ```
         [~DeviceA] traffic-policy traffic_policy_edsg outbound
         ```
         ```
         [~DeviceA] commit
         ```
   4. Configure an AAA authentication scheme and accounting scheme.
      
      
      
      # Configure an AAA authentication scheme named **auth1** and specify RADIUS authentication as the authentication mode.
      
      ```
      [~DeviceA] aaa
      ```
      ```
      [*DeviceA-aaa] authentication-scheme auth1
      ```
      ```
      [*DeviceA-aaa-authen-auth1] authentication-mode radius
      ```
      ```
      [*DeviceA-aaa-authen-auth1] commit
      ```
      ```
      [~DeviceA-aaa-authen-auth1] quit
      ```
      
      
      
      # Configure an AAA accounting scheme named **acct1** and specify RADIUS accounting as the accounting mode.
      
      ```
      [~DeviceA-aaa] accounting-scheme acct1
      ```
      ```
      [*DeviceA-aaa-accounting-acct1] accounting-mode radius
      ```
      ```
      [*DeviceA-aaa-accounting-acct1] quit
      ```
      ```
      [*DeviceA-aaa] commit
      ```
      ```
      [~DeviceA-aaa] quit
      ```
   5. Configure a mode in which EDSG service policies are obtained.
      
      
      
      # Configure the device to obtain EDSG service policies from local configurations and then from a RADIUS server if no EDSG service policy is obtained from local configurations.
      
      ```
      [~DeviceA] service-policy download local radius rad_group1 password cipher YsHsjx_202206
      ```
      ```
      [*DeviceA] commit
      ```
   6. Configure EDSG service policies.
      
      
      1. Configure an EDSG service policy for the access to network 1.
         
         # Create an EDSG service policy named **service\_edsg1**.
         
         ```
         [~DeviceA] service-policy name service_edsg1 edsg
         ```
         
         # Bind **s\_1m** to **service\_edsg1**.
         
         ```
         [*DeviceA-service-policy-service_edsg1] service-group s_1m
         ```
         
         # Bind **rad\_group1** to **service\_edsg1**.
         
         ```
         [*DeviceA-service-policy-service_edsg1] radius-server group rad_group1
         ```
         
         # Bind **auth1** to **service\_edsg1**.
         
         ```
         [*DeviceA-service-policy-service_edsg1] authentication-scheme auth1
         ```
         
         # Bind **acct1** to **service\_edsg1**.
         
         ```
         [*DeviceA-service-policy-service_edsg1] accounting-scheme acct1
         ```
         
         # Set the uplink traffic rate limit for **service\_edsg1** to 1 Mbit/s.
         
         ```
         [*DeviceA-service-policy-service_edsg1] rate-limit cir 1000 inbound
         ```
         
         # Set the downlink traffic rate limit for **service\_edsg1** to 1 Mbit/s.
         
         ```
         [*DeviceA-service-policy-service_edsg1] rate-limit cir 1000 outbound
         ```
         ```
         [*DeviceA-service-policy-service_edsg1] commit
         ```
         ```
         [~DeviceA-service-policy-service_edsg1] quit
         ```
      2. Configure an EDSG service policy for the access to network 2.
         
         # Create an EDSG service policy named **service\_edsg2**.
         
         ```
         [~DeviceA] service-policy name service_edsg2 edsg
         ```
         
         # Bind **s\_2m** to **service\_edsg2**.
         
         ```
         [*DeviceA-service-policy-service_edsg2] service-group s_2m
         ```
         
         # Bind **rad\_group1** to **service\_edsg2**.
         
         ```
         [*DeviceA-service-policy-service_edsg2] radius-server group rad_group1
         ```
         
         # Bind **auth1** to **service\_edsg2**.
         
         ```
         [*DeviceA-service-policy-service_edsg2] authentication-scheme auth1
         ```
         
         # Bind **acct1** to **service\_edsg2**.
         
         ```
         [*DeviceA-service-policy-service_edsg2] accounting-scheme acct1
         ```
         
         # Set the uplink traffic rate limit for **service\_edsg2** to 2 Mbit/s.
         
         ```
         [*DeviceA-service-policy-service_edsg2] rate-limit cir 2000 inbound
         ```
         
         # Set the downlink traffic rate limit for **service\_edsg2** to 2 Mbit/s.
         
         ```
         [*DeviceA-service-policy-service_edsg2] rate-limit cir 2000 outbound
         ```
         ```
         [*DeviceA-service-policy-service_edsg2] commit
         ```
         ```
         [~DeviceA-service-policy-service_edsg2] quit
         ```
   7. Bind the local address pool and RADIUS server group to an AAA domain.
      
      
      
      # Bind **edsg\_pool** and **rad\_group1** to an AAA domain.
      
      ```
      [~DeviceA] aaa
      ```
      ```
      [*DeviceA-aaa] domain domain1
      ```
      ```
      [*DeviceA-aaa-domain-domain1] ip-pool edsg_pool
      ```
      ```
      [*DeviceA-aaa-domain-domain1] radius-server group rad_group1
      ```
      ```
      [*DeviceA-aaa-domain-domain1] quit
      ```
      ```
      [*DeviceA-aaa] commit
      ```
      ```
      [~DeviceA-aaa] quit
      ```
   8. Configure the prepaid function.
      
      
      1. Configure a prepaid profile for the access to network 1.
         
         # Create a prepaid profile named **prepaid1**.
         
         ```
         [~DeviceA] prepaid-profile prepaid1
         ```
         
         # Bind **rad\_group1** to **prepaid1**.
         
         ```
         [~DeviceA-prepaid-profile-prepaid1] radius-server group rad_group1
         ```
         
         # Bind **auth1** to the prepaid profile.
         
         ```
         [*DeviceA-prepaid-profile-prepaid1] authentication-scheme auth1
         ```
         
         # Bind **acct1** to the prepaid profile.
         
         ```
         [*DeviceA-prepaid-profile-prepaid1] accounting-scheme acct1
         ```
         
         # Configure a password used for the device to apply for an EDSG service quota from the RADIUS server group.
         
         ```
         [*DeviceA-prepaid-profile-prepaid1] password cipher YsHsjx_202206
         ```
         
         # Set the time threshold for the device to reapply for a time quota for EDSG services from the RADIUS server to 60s.
         
         ```
         [*DeviceA-prepaid-profile-prepaid1] threshold time 60 seconds
         ```
         
         # Set the traffic volume threshold for the BRAS to reapply for a traffic volume quota for EDSG services from the RADIUS server to 10 Mbytes.
         
         ```
         [*DeviceA-prepaid-profile-prepaid1] threshold volume 10 mbytes
         ```
         ```
         [*DeviceA-prepaid-profile-prepaid1] commit
         ```
         ```
         [~DeviceA-prepaid-profile-prepaid1] quit
         ```
      2. Configure a prepaid profile for the access to network 2.
         
         # Create a prepaid profile named **prepaid2**.
         
         ```
         [~DeviceA] prepaid-profile prepaid2
         ```
         
         # Bind **rad\_group1** to **prepaid2**.
         
         ```
         [~DeviceA-prepaid-profile-prepaid2] radius-server group rad_group1
         ```
         
         # Bind auth1 to the prepaid profile.
         
         ```
         [*DeviceA-prepaid-profile-prepaid2] authentication-scheme auth1
         ```
         
         # Bind acct1 to the prepaid profile.
         
         ```
         [*DeviceA-prepaid-profile-prepaid2] accounting-scheme acct1
         ```
         
         # Configure a password used for the device to apply for an EDSG service quota from the RADIUS server group.
         
         ```
         [*DeviceA-prepaid-profile-prepaid2] password cipher YsHsjx_202206
         ```
         
         # Set the time threshold for the device to reapply for a time quota for EDSG services from the RADIUS server to 300s.
         
         ```
         [*DeviceA-prepaid-profile-prepaid2] threshold time 300 seconds
         ```
         
         # Set the traffic volume threshold for the device to reapply for a traffic volume quota for EDSG services from the RADIUS server to 20 Mbytes.
         
         ```
         [*DeviceA-prepaid-profile-prepaid2] threshold volume 20 mbytes
         ```
         ```
         [*DeviceA-prepaid-profile-prepaid2] commit
         ```
         ```
         [~DeviceA-prepaid-profile-prepaid2] quit
         ```
      3. Apply the prepaid profiles in the EDSG service policy view.
         
         # Apply **prepaid1** to **service\_edsg1**.
         
         ```
         [~DeviceA] service-policy name service_edsg1 edsg
         ```
         ```
         [*DeviceA-service-policy-service_edsg1] prepaid-profile prepaid1
         ```
         ```
         [*DeviceA-service-policy-service_edsg1] commit
         ```
         ```
         [~DeviceA-service-policy-service_edsg1] quit
         ```
         
         # Apply **prepaid2** to **service\_edsg2**.
         
         ```
         [~DeviceA] service-policy name service_edsg2 edsg
         ```
         ```
         [*DeviceA-service-policy-service_edsg2] prepaid-profile prepaid2
         ```
         ```
         [*DeviceA-service-policy-service_edsg2] commit
         ```
         ```
         [~DeviceA-service-policy-service_edsg2] quit
         ```
   9. Configure interfaces.
      
      
      1. Create a virtual template interface.
         
         ```
         [~DeviceA] interface Virtual-Template 1
         ```
         ```
         [*DeviceA-Virtual-Template1] commit
         ```
         ```
         [~DeviceA-Virtual-Template1] quit
         ```
      2. Configure a BAS interface.
         
         ```
         [*DeviceA] interface GigabitEthernet0/1/2.1
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/2.1] user-vlan 1000 2000
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/2.1] user-vlan 1 1000 qinq 100
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/2.1] pppoe-server bind virtual-template 1
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/2.1] bas
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain pre-authentication domain1
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/2.1-bas] authentication-method ppp web 
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/2.1-bas] quit
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/2.1] commit
         ```
         ```
         [~DeviceA-GigabitEthernet0/1/2.1] quit
         ```
      3. Configure an uplink interface.
         
         ```
         [~DeviceA] interface GigabitEthernet0/1/0.1
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/0.1] vlan-type dot1q 1
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/0.1] ip address 192.168.100.1 255.255.255.0
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/0.1] commit
         ```
         ```
         [~DeviceA-GigabitEthernet0/1/0.1] quit
         ```
      4. Configure the interface connected to the policy server, AAA server, and portal server.
         
         ```
         [~DeviceA] interface GigabitEthernet0/1/1
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/1] ip address 10.10.10.1 255.255.255.0
         ```
         ```
         [*DeviceA-GigabitEthernet0/1/1] commit
         ```
         ```
         [~DeviceA-GigabitEthernet0/1/1] quit
         ```
   10. Configure users to go online.
       
       
       
       # Configure the AAA server to deliver the RADIUS attribute User-Password with a value of **YsHsjx\_202206** for PPPoE users (users 1 and 2).
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The shared key configured for a RADIUS server group determines the content of the User-Password attribute.
       
       # Configure the AAA server to deliver the RADIUS attribute HW-Account-Info containing **Aservice\_edsg1** for user 1.
       
       # Configure the AAA server to deliver the RADIUS attribute HW-Account-Info containing **Aservice\_edsg2** for user 2.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The content of the HW-Account-Info attribute starts with "A" followed by a service name. This attribute is used in user authentication response packets to deliver EDSG services that automatically take effect (directly activated after delivery).
6. Verify the configuration.
   
   
   
   After successfully configuring the RBP, run the **display remote-backup-profile** command. According to the command output, the RBS type is **bras**, the RBP named **profile1** is bound to **GigabitEthernet0/1/0.1** from which users go online, and Device A is in the **Master** state.
   
   ```
   <~DeviceA> display remote-backup-profile profile1 
   ```
   ```
   -----------------------------------------------
    Profile-Index        : 0x803
    Profile-Name         : profile1
    Service            : bras
    Remote-backup-service: service1
    Backup-ID            : 10
    track protocol       : VRRP
    VRRP-ID              : 1
    VRRP-Interface       : GigabitEthernet0/1/0.2
    Interface            :
                           GigabitEthernet0/1/0.1
    State           	 : Master
    Peer-state      	 : Slave
    Backup mode          : hot
    Slot-Number          : 1
    Card-Number          : 0
    Port-Number          : 0
    IP-Pool              : hsi
    Traffic threshold    : 50(MB)
    Traffic interval     : 10(minutes)     
   
   ```
   ```
   <~DeviceB> display remote-backup-profile profile1 
   ```
   ```
   -----------------------------------------------
    Profile-Index        : 0x803
    Profile-Name         : profile1
    Service            : bras
    Remote-backup-service: service1
    Backup-ID            : 10
    track protocol       : VRRP
    VRRP-ID              : 1
    VRRP-Interface       : GigabitEthernet0/1/0.2
    Interface            :
                           GigabitEthernet0/1/0.1
    State              : Slave
    Peer-state      	 : Master
    Backup mode          : hot
    Slot-Number          : 1
    Card-Number          : 0
    Port-Number          : 0
    IP-Pool              : hsi
    Traffic threshold    : 50(MB)
    Traffic interval     : 10(minutes)     
   ```
   
   After successfully configuring the RBS, run the **display remote-backup-service** command. The command output shows that the TCP connection is in the **Connected** state.
   
   ```
   <~DeviceA> display remote-backup-service service1 
   ----------------------------------------------------------
    Service-Index    : 0
    Service-Name     : service1
    TCP-State        : Connected
    Peer-ip          : 88.88.88.88
    Source-ip        : 22.22.22.22
    TCP-Port         : 2046
    Track-BFD        : --
    Track-interface0 : GigabitEthernet0/2/0
    Track-interface1 : --
   ----------------------------------------------------------
   
   ip pool:
            hsi metric 10
            hsi-bak metric 10
   ipv6 pool:  
   NAT instance : nat1
   ----------------------------------------------------------
    Rbs-ID         : 0
    Protect-type   : ip-redirect
    Next-hop       : 10.1.1.7
    Vlanid         : 0
    Peer-ip        : 10.1.1.7
    Vrfid          : 0
    Tunnel-index   : 0x0
    Tunnel-state   : UP
    Tunnel-OperFlag: NORMAL
    Spec-interface : GigabitEthernet0/3/0
    Out-interface  : GigabitEthernet0/3/0
    User-number    : 0
   
   ```
   
   After users go online, run the **display backup-user** command to check information about backup users.
   
   ```
   <~HUAWEI> display backup-user
   ```
   ```
     Remote-backup-service: service1
     Total Users Numer: 10
   ------------------------------------------------------------------------
    100     101     102     103     104     105     106     107     108     109
   ------------------------------------------------------------------------
   
   ```
   
   Run the **display access-user interface** command to view online user information on a specified interface.
   
   ```
   <~HUAWEI> display access-user interface GigabitEthernet 0/1/0.1
   ```
   ```
     ------------------------------------------------------------------------------
     UserID  Username                Interface      IP address       MAC
             Vlan          IPv6 address             Access type
     ------------------------------------------------------------------------------
     120     user@lsh                GE0/1/0.1      2.2.2.10         00e0-fc12-0101
             50/-            -                       IPoE
     101      user@lsh                GE0/1/0.1      2.2.2.9         00e0-fc12-0102          -
             50/-            -                       IPoE
     102      user@lsh                GE0/1/0.1      2.2.2.8         00e0-fc12-0103          -
             50/-            -                       IPoE
     103      user@lsh                GE0/1/0.1      2.2.2.7         00e0-fc12-0104          -
             50/-            -                       IPoE
     104      user@lsh                GE0/1/0.1      2.2.2.6         00e0-fc12-0105          -
             50/-            -                       IPoE
     105      user@lsh                GE0/1/0.1      2.2.2.5         00e0-fc12-0106          -
             50/-            -                       IPoE
     106      user@lsh                GE0/1/0.1      2.2.2.4         00e0-fc12-0107          -
             50/-            -                       IPoE
     107      user@lsh                GE0/1/0.1      2.2.2.3         00e0-fc12-0108          -
             50/-            -                       IPoE
     108      user@lsh                GE0/1/0.1      2.2.2.2         00e0-fc12-0109          -
             50/-            -                       IPoE
     109      user@lsh                GE0/1/0.1      2.2.2.11        00e0-fc12-0110          -
             50/-            -                       IPoE
     --------------------------------------------------------------------------
     Normal users                       : 0
     RUI Local users                    : 10
     RUI Remote users                   : 0
     Total users                        : 10
   ```
   
   Check the EDSG service status on the active and standby devices.
   
   ```
   <HUAWEI> display service-policy configuration name service_edsg1
   ------------------------------------------------
   Service-policy-index         : 0
     Service-policy-name          : service1
     Service-policy-type          : EDSG
     Policy-storage-type          : configuration
     Reference-count              : 0
     Service-class-inbound        : ef
     Service-class-outbound       : ef
     Authentication-scheme-name   : -
     Accounting-scheme-name       : default1
     Radius-server-template       : template1
     Service-group-name           : -
     Service-group-priority       : -
     Inbound-cir                  : 100(kbps)
     Inbound-pir                  : 100(kbps)
     Inbound-cbs                  : 100(bytes)
     Inbound-pbs                  : 3000(bytes)
     Outbound-cir                 : 10000(kbps)
     Outbound-pir                 : -
     Outbound-cbs                 : -
     Outbound-pbs                 : -
     Prepaid-profile-name         : -
     Diameter monitor key         : -
     Inbound-match-usergroup      : no
     Outbound-match-usergroup     : no
    ------------------------------------------------ 
   
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
   sysname DeviceA
  #
   bfd
  #
  ip pool hsi bas local 
   gateway 1.1.1.1 255.255.255.0 
   section 0 1.1.1.2 1.1.1.254 
  #
  ip pool hsi-main-bak bas local rui-slave 
   gateway 2.2.2.2 255.255.255.0
   section 0 2.2.2.3 2.2.2.254 
  #
  aaa
   domain userdomain1 
   authentication-scheme default0 
   accounting-scheme default0 
   ip-pool hsi 
   ip-pool hsi-main-bak
  #
  bfd bfd bind peer-ip 10.0.1.2 
   discriminator local 1 
   discriminator remote 2  
  #
  interface gigabitethernet 0/1/0.2 
   vlan-type dot1q 200 
   ip address 10.0.1.1 255.255.255.0 
   vrrp vrid 1 virtual-ip 10.0.1.100 
   admin-vrrp vrid 1 
   vrrp vrid 1 priority 120 
   vrrp vrid 1 preempt-mode timer delay 600
   vrrp vrid 1 track bfd-session 1 peer 
   vrrp vrid 1 track interface gigabitethernet 0/2/0 reduced 50
   vrrp recover-delay 20
  #
  remote-backup-service service1 
   peer 88.88.88.88 source 22.22.22.22 port 2046 
   track interface gigabitethernet 0/2/0  
   ip-pool hsi
   ip-pool hsi-bak
   protect redirect ip-nexthop 10.1.1.7 interface gigabitethernet 0/3/0
  #
  remote-backup-profile profile1 
   service-type bras
   backup-id 10 remote-backup-service service1 
   peer-backup hot 
   vrrp-id 1 interface gigabitethernet 0/1/0.2 
  #
  interface gigabitethernet 0/1/0.1
   user-vlan 50 
   remote-backup-profile profile1 
   bas 
   access-type layer2-subscriber 
   authentication-method  web 
   vlan-type dot1q 1
   ip address 192.168.100.1 255.255.255.0
  #
  interface gigabitethernet 0/3/0
   undo shutdown 
   ip address 10.1.1.6 255.255.255.0 
  #
  value-added-service enable
  #
  radius-server group rad_group1
   radius-server authentication 10.10.10.2 1812 weight 0
   radius-server accounting 10.10.10.2 1813 weight 0
   radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#    
  #
  ip pool edsg_pool bas local
   gateway 172.16.1.0 255.255.0.0
   section 0 172.16.1.0 172.16.1.255
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
   if-match acl 6020
  #
  traffic classifier c2 operator or
   if-match acl 6021
  #
  traffic behavior b1
  #
  traffic behavior b2
  #
  traffic policy traffic_policy_edsg           
   share-mode
   classifier c1 behavior b1
   classifier c2 behavior b2
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
   web-server url http://www.sample.com                                              
   web-server mode post                                                           
  #                                               
  prepaid-profile prepaid1                                                        
   password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#                               
   authentication-scheme auth1                                                    
   accounting-scheme acct1                                                        
   radius-server group rad_group1                                                     
   threshold time 60 seconds                                                      
   threshold volume 10 mbytes                                                     
  #                                         
  prepaid-profile prepaid2                                                        
   password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#                               
   authentication-scheme auth1                                                    
   accounting-scheme acct1                                                        
   radius-server group rad_group1                                                     
   threshold time 300 seconds                                                     
   threshold volume 20 mbytes                                                     
   quota-out redirect http_redirect_profile                                       
  #                              
  service-policy download local radius rad_group1 password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
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
  interface Virtual-Template 1
  #
  interface GigabitEthernet0/1/2.1
   pppoe-server bind virtual-template 1
   user-vlan 1000 2000
   user-vlan 1 1000 qinq 100
   bas
   #
    access-type layer2-subscriber default-domain pre-authentication domain1
    authentication-method ppp web  
  #
   return 
  ```
* Device B configuration file
  
  ```
  #
   sysname DeviceB
  #
   bfd
  #
  ip pool hsi-main bas local 
   gateway 2.2.2.2 255.255.255.0 
   section 0 2.2.2.3 2.2.2.254 
  #
  ip pool hsi-bak bas local rui-slave 
   gateway 1.1.1.1 255.255.255.0
   # LOCAL
     section 0 1.1.1.2 1.1.1.254
   # REMOTE
     dhcp-server group gm1
  #
  aaa
   domain userdomain1 
   authentication-scheme default0 
   accounting-scheme default0 
  #
  bfd bfd bind peer-ip 10.0.1.1 
   discriminator local 2 
   discriminator remote 1 
   commit 
  #
  interface gigabitethernet 0/1/0.2 
   vlan-type dot1q 200 
   ip address 10.0.1.2 255.255.255.0 
   vrrp vrid 1 virtual-ip 10.0.1.100 
   admin-vrrp vrid 1 
   vrrp vrid 1 track bfd-session 2 peer 
   vrrp vrid 1 track interface gigabitethernet 0/2/0 reduced 50
   vrrp recover-delay 20
  #
  remote-backup-service service1 
   peer 22.22.22.22 source 88.88.88.88 port 2046 
   track interface gigabitethernet 0/2/0  
   ip-pool hsi-main 
   ip-pool hsi-main-bak
   protect redirect ip-nexthop 10.1.1.6 interface gigabitethernet 0/3/0
  #
  remote-backup-profile profile1 
   peer-backup hot 
   service-type bras
   backup-id 10 remote-backup-service service1 
   peer-backup hot 
   vrrp-id 1 interface gigabitethernet 0/1/0.2 
   ip-pool hsi include hsi-bak node 5
   ip-pool hsi-main include hsi-main-bak node 10
  #
  interface gigabitethernet 0/1/0.1
   user-vlan 50 
   remote-backup-profile profile1 
   bas 
   access-type layer2-subscriber 
   authentication-method  web 
   vlan-type dot1q 1
   ip address 192.168.100.1 255.255.255.0
  #
  interface gigabitethernet 0/3/0
   undo shutdown 
   ip address 10.1.1.7 255.255.255.0 #
  value-added-service enable
  #
  radius-server group rad_group1
   radius-server authentication 10.10.10.2 1812 weight 0
   radius-server accounting 10.10.10.2 1813 weight 0
   radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#    
  #
  ip pool edsg_pool bas local
   gateway 172.16.1.0 255.255.0.0
   section 0 172.16.1.0 172.16.1.255
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
   if-match acl 6020
  #
  traffic classifier c2 operator or
   if-match acl 6021
  #
  traffic behavior b1
  #
  traffic behavior b2
  #
  traffic policy traffic_policy_edsg           
   share-mode
   classifier c1 behavior b1
   classifier c2 behavior b2
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
   web-server url http://www.sample.com                                              
   web-server mode post                                                           
  #                                               
  prepaid-profile prepaid1                                                        
   password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#   
   authentication-scheme auth1                                                    
   accounting-scheme acct1                                                        
   radius-server group rad_group1                                                     
   threshold time 60 seconds                                                      
   threshold volume 10 mbytes                                                     
  #                                         
  prepaid-profile prepaid2                                                        
   password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#  
   authentication-scheme auth1                                                    
   accounting-scheme acct1                                                        
   radius-server group rad_group1                                                     
   threshold time 300 seconds                                                     
   threshold volume 20 mbytes                                                     
   quota-out redirect http_redirect_profile                                       
  #                              
  service-policy download local radius rad_group1 password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
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
  interface Virtual-Template 1
  #
  interface GigabitEthernet0/1/2.1
   pppoe-server bind virtual-template 1
   user-vlan 1000 2000
   user-vlan 1 1000 qinq 100
   bas
   #
    access-type layer2-subscriber default-domain pre-authentication domain1
    authentication-method ppp web  
  #
   return 
  ```