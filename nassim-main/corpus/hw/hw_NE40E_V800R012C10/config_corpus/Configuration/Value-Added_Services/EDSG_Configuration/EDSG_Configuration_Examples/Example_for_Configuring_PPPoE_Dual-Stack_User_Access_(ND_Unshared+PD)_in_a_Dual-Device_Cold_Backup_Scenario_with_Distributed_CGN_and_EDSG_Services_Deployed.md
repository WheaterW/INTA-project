Example for Configuring PPPoE Dual-Stack User Access (ND Unshared+PD) in a Dual-Device Cold Backup Scenario with Distributed CGN and EDSG Services Deployed
===========================================================================================================================================================

This section provides an example for configuring PPPoE dual-stack user access (ND unshared+PD) in a dual-device cold backup scenario with distributed CGN and EDSG services deployed.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001220590118__fig624412481872), User1 and User2 access BRAS1 through SW1. BRAS1 uses RADIUS for authentication and accounting. It assigns to the users IPv4 addresses through the local address pool, IPv6 prefixes through DHCPv6 IA\_PD, and IPv6 addresses through ND.

EDSG services need to be deployed to meet users' different requirements for network service traffic. ACLs need to be configured to match destination addresses of user traffic so that network segments accessed by users can be differentiated, thereby implementing independent rate limiting and accounting for different network segments. To enable private network users to access the Internet, deploy distributed CGN on the network to translate private addresses into public addresses. In addition, deploy dual-device cold backup to improve network reliability. This function allows the users to go online through the other device if a device fails.

**Figure 1** PPPoE dual-stack user access (ND unshared+PD) in a dual-device cold backup scenario with distributed CGN and EDSG services deployed![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent Eth-Trunk 2 and GE 0/1/0, respectively.


  
![](figure/en-us_image_0000001269767213.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure AAA schemes, and specify RADIUS authentication and RADIUS accounting.
2. Configure RADIUS.
3. Configure address pools.
4. Configure devices to generate DUIDs in DUID-LLT mode.
5. Configure a domain.
6. Configure interfaces.
7. Configure EDSG services.
8. Configure distributed CGN services.
9. Enable the devices to advertise public routes.


#### Data Preparation

To complete the configuration, you need the following data:

* User access parameters
* CGN service parameters
* EDSG service parameters

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration on BRAS2 is similar to that on BRAS1. The configuration procedure on BRAS1 is used as an example. For details about the configuration on BRAS2, see the configuration file.



#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure two authentication schemes, one with the authentication mode set to RADIUS, and that of the other one set to none.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*HUAWEI] commit
   [~BRAS1] aaa
   [~BRAS1-aaa] authentication-scheme auth1
   [*BRAS1-aaa-authen-auth1] authentication-mode radius
   [*BRAS1-aaa-authen-auth1] quit
   [~BRAS1-aaa] authentication-scheme none
   [*BRAS1-aaa-authen-none] authentication-mode none
   [*BRAS1-aaa-authen-none] quit
   [*BRAS1-aaa] commit
   ```
   
   # Configure an accounting scheme and set the accounting mode to RADIUS.
   
   ```
   [~BRAS1-aaa] accounting-scheme acct1
   [*BRAS1-aaa-accounting-acct1] accounting-mode radius
   [*BRAS1-aaa-accounting-acct1] quit
   [*BRAS1-aaa] commit
   [*BRAS1-aaa] quit
   ```
2. Configure RADIUS.
   
   
   
   # Create UDP sockets with the local port numbers 1645, 1646, and 3799 and with any local IP address.
   
   ```
   [~BRAS1] radius local-ip all
   [*BRAS1] commit
   ```
   
   # Configure a RADIUS server group.
   
   
   
   ```
   [~BRAS1] radius-server group rd1
   [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
   [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
   [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   [*BRAS1-radius-rd1] commit 
   [~BRAS1-radius-rd1] radius-server calling-station-id include mac
   [~BRAS1-radius-rd1] radius-server user-name original
   [*BRAS1-radius-rd1] commit 
   [~BRAS1-radius-rd1] radius-server class-as-car
   [*BRAS1-radius-rd1] quit
   [*BRAS1] commit
   ```
   
   
   
   # Configure a RADIUS authorization server.
   
   ```
   [~BRAS1] radius-server authorization 192.168.8.249 shared-key-cipher YsHsjx_202206 server-group rd1
   [*BRAS1] commit
   ```
3. Configure address pools.
   
   
   
   # Configure a local address pool for IPv4 users.
   
   ```
   [~BRAS1] ip pool pool_v4 bas local
   [*BRAS1-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0
   [*BRAS1-ip-pool-pool_v4] commit
   [~BRAS1-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.200 
   [~BRAS1-ip-pool-pool_v4] dns-server 10.179.155.161 10.179.155.177
   [*BRAS1-ip-pool-pool_v4] quit
   [*BRAS1] commit
   ```
   
   # Configure address pools for IPv6 users.
   
   ```
   [~BRAS1] ipv6 prefix pre_nd_1 delegation
   [*BRAS1-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48
   [*BRAS1-ipv6-prefix-pre_nd] slaac-unshare-only
   [*BRAS1-ipv6-prefix-pre_nd] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 pool pool_nd_1 bas delegation
   [*BRAS1-ipv6-pool-pool_nd] prefix pre_nd
   [*BRAS1-ipv6-pool-pool_nd] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_nd] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 prefix pre_pd_1 delegation
   [*BRAS1-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48
   [*BRAS1-ipv6-prefix-pre_pd] commit
   [~BRAS1-ipv6-prefix-pre_pd] pd-unshare-only
   [~BRAS1-ipv6-prefix-pre_pd] quit
   [~BRAS1] ipv6 pool pool_pd bas delegation
   [*BRAS1-ipv6-pool-pool_pd] prefix pre_pd_1
   [*BRAS1-ipv6-pool-pool_pd] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_pd] quit
   [*BRAS1] commit
   ```
4. Configure the device to generate a DUID in DUID-LLT mode. (This step is not required if a DUID has been configured on the device.)
   
   
   ```
   [~BRAS1] dhcpv6 duid llt
   [*BRAS1] commit
   ```
5. Configure a domain.
   
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain isp1
   [*BRAS1-aaa-domain-isp1] authentication-scheme auth1
   [*BRAS1-aaa-domain-isp1] accounting-scheme acct1
   [*BRAS1-aaa-domain-isp1] radius-server group rd1
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] prefix-assign-mode unshared  
   [~BRAS1-aaa-domain-isp1] ip-pool pool_v4
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_nd
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_pd
   [~BRAS1-aaa-domain-isp1] accounting-start-delay 10 online user-type ppp
   [*BRAS1-aaa-domain-isp1] accounting-start-delay traffic-forward before-start-accounting
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] user-basic-service-ip-type ipv4
   [~BRAS1-aaa-domain-isp1] quit
   [~BRAS1-aaa] quit
   ```
6. Configure interfaces.
   
   
   
   # Configure a VT.
   
   ```
   [~BRAS1] interface virtual-template 5
   [*BRAS1-virtual-template5] ppp authentication-mode chap
   [*BRAS1-virtual-template5] quit
   [*BRAS1] commit
   ```
   
   # Configure the Eth-Trunk interface to work in static LACP mode and set a protocol packet timeout period.
   
   ```
   [~BRAS1] interface Eth-Trunk2
   [*BRAS1-Eth-Trunk2] mode lacp-static
   [*BRAS1-Eth-Trunk2] lacp timeout fast
   [*BRAS1-Eth-Trunk2] commit
   ```
   
   # Configure IPv6 on the Eth-Trunk interface's sub-interface.
   
   ```
   [~BRAS1-Eth-Trunk2] interface Eth-Trunk2.10
   [*BRAS1-Eth-Trunk2.10] ipv6 enable
   [*BRAS1-Eth-Trunk2.10] ipv6 address auto link-local
   [*BRAS1-Eth-Trunk2.10] pppoe-server bind Virtual-Template 5
   [*BRAS1-Eth-Trunk2.10] commit
   [~BRAS1-Eth-Trunk2.10] user-vlan 1000 4000 qinq 2000 2001
   [~BRAS1-Eth-Trunk2.10-user-vlan-1000-4000-qinq-2000-2001] quit
   ```
   
   # Configure a BAS interface. In a dual-device cold backup scenario, configure delayed access for users with even-numbered MAC addresses and delayed access for users with odd-numbered MAC addresses on BRAS1 and BRAS2, respectively.
   
   ```
   [~BRAS1-Eth-Trunk2.10] bas
   [~BRAS1-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain authentication isp1
   [*BRAS1-Eth-Trunk2.10-bas] client-option82 basinfo-insert cn-telecom
   [*BRAS1-Eth-Trunk2.10-bas] commit
   [~BRAS1-Eth-Trunk2.10-bas] access-delay 100 even-mac
   [~BRAS1-Eth-Trunk2.10-bas] quit
   ```
   
   # Configure the network-side interface.
   
   ```
   [~BRAS1] interface gigabitEthernet 0/1/0
   [*BRAS1-GigabitEthernet0/1/0] ipv6 enable 
   [*BRAS1-GigabitEthernet0/1/0] ipv6 address 2001:db8:8::7 128
   [*BRAS1-GigabitEthernet0/1/0] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/1/0] ip address 10.2.1.1 24
   [*BRAS1-GigabitEthernet0/1/0] quit
   [*BRAS1-GigabitEthernet0/1/0] commit
   ```
7. Configure EDSG services.
   
   
   
   # Enable the value-added service function.
   
   ```
   [~BRAS1] value-added-service enable
   [*BRAS1] commit
   ```
   
   # Configure the HW-Policy-Name attribute to support EDSG service delivery.
   
   ```
   [~BRAS1] radius-attribute hw-policy-name support-type edsg
   [*BRAS1] commit
   ```
   
   # Configure an EDSG traffic policy.
   
   1. Create a service group.
      ```
      [~BRAS1] service-group edsg
      [*BRAS1] commit
      ```
   2. Configure ACL rules for the service group.
      ```
      [~BRAS1] acl number 6100
      [*BRAS1-acl4-basic-6100] description edsg
      [*BRAS1-acl4-basic-6100] rule 5 permit ip source service-group edsg destination ip-address 192.168.100.0 0.0.0.255
      [*BRAS1-acl4-basic-6100] rule 10 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group edsg
      [*BRAS1-acl4-basic-6100] quit
      [*BRAS1] commit
      [~BRAS1] acl ipv6 number 6100
      [*BRAS1-acl6-ucl-6100] rule 5 permit ipv6 source service-group edsg destination ipv6-address 2001:db8::/32
      [*BRAS1-acl6-ucl-6100] rule 10 permit ipv6 source ipv6-address 2001:db8::/32 destination service-group edsg
      [*BRAS1-acl6-ucl-6100] quit
      [*BRAS1] commit
      ```
   3. Configure a traffic classifier.
      ```
      [~BRAS1] traffic classifier edsg-c1
      [*BRAS1-classifier-edsg-c1] if-match acl 6100
      [*BRAS1-classifier-edsg-c1] if-match ipv6 acl 6100
      [*BRAS1-classifier-edsg-c1] quit
      [*BRAS1] commit
      ```
   4. Configure a traffic behavior.
      ```
      [~BRAS1] traffic behavior edsg-b1
      [*BRAS1-edsg-b1] quit
      [*BRAS1] commit
      ```
   5. Configure an EDSG traffic policy.
      ```
      [~BRAS1] traffic policy p1
      [*BRAS1-traffic-policy-p1] classifier edsg-c1 behavior edsg-b1 precedence 1
      [*BRAS1-traffic-policy-p1] quit
      [*BRAS1] commit
      ```
   6. Apply the EDSG traffic policy globally.
      ```
      [~BRAS1] traffic-policy p1 inbound
      [*BRAS1] traffic-policy p1 outbound
      [*BRAS1] commit
      ```
   
   # Configure an EDSG service policy.
   
   ```
   [~BRAS1] service-policy name service_edsg1 edsg
   [*BRAS1-service-policy-service_edsg1] commit
   [~BRAS1-service-policy-service_edsg1] radius-server group rd1
   [~BRAS1-service-policy-service_edsg1] authentication-scheme none
   [*BRAS1-service-policy-service_edsg1] accounting-scheme acct1
   [*BRAS1-service-policy-service_edsg1] service-group edsg
   [*BRAS1-service-policy-service_edsg1] rate-limit cir 100000 pir 100000 inbound
   [*BRAS1-service-policy-service_edsg1] rate-limit cir 100000 pir 100000 outbound
   [*BRAS1-service-policy-service_edsg1] quit
   [*BRAS1-service-policy-service_edsg1] commit
   ```
8. Configure distributed CGN services.
   
   
   
   # Set the session table sizes of the CPUs on the NAT service boards in slots 3 and 2 to 16M.
   
   ```
   [~BRAS1] license
   [*BRAS1-license] active nat session-table size 16 slot 3 engine 0
   [*BRAS1-license] active nat session-table size 16 slot 2 engine 0
   [*BRAS1-license] active nat bandwidth-enhance slot 3 engine 0
   [*BRAS1-license] active nat bandwidth-enhance slot 2 engine 0
   [*BRAS1-license] quit
   [*BRAS1] commit
   ```
   
   # Create service-location group 1 and bind it to service boards.
   
   ```
   [~BRAS1] service-location 1
   [*BRAS1-service-location-1] location slot 3 engine 0 backup slot 2 engine 0
   [*BRAS1-service-location-1] quit
   [*BRAS1] commit
   ```
   
   # Create service-location group 2 and bind it to service boards.
   
   ```
   [~BRAS1] service-location 2
   [*BRAS1-service-location-2] location slot 2 engine 0 backup slot 3 engine 0
   [*BRAS1-service-location-2] quit
   [*BRAS1] commit
   ```
   
   # Create service instance groups and bind service-location groups to them.
   
   ```
   [~BRAS1] service-instance-group nat444-group1
   [*BRAS1-service-instance-group-nat444-1] service-location 1
   [*BRAS1-service-instance-group-nat444-1] quit
   [*BRAS1-service-instance-group-nat444-1] commit
   [~BRAS1] service-instance-group nat444-group2
   [*BRAS1-service-instance-group-nat444-2] service-location 2
   [*BRAS1-service-instance-group-nat444-2] quit
   [*BRAS1-service-instance-group-nat444-2] commit
   ```
   
   # Create a NAT instance named **nat444-1**, bind the service instance group **nat444-group1** to it to specify the corresponding service board resources, and configure a port range.
   
   ```
   [~BRAS1] nat instance nat444-1 id 1
   [*BRAS1-nat-instance-nat444-1] service-instance-group nat444-group1
   [*BRAS1-nat-instance-nat444-1] port-range 4096 
   ```
   
   # Configure public addresses.
   
   ```
   [*BRAS1-nat-instance-nat444-1] nat address-group pppoe-public-1 group-id 1
   [*BRAS1-nat-instance-nat444-1-nat-address-group-pppoe-public-1] section 0 10.1.1.0 mask 24
   [*BRAS1-nat-instance-nat444-1-nat-address-group-pppoe-public-1] section 1 10.3.1.0 mask 24
   [*BRAS1-nat-instance-nat444-1-nat-address-group-pppoe-public-1] quit
   [*BRAS1-nat-instance-nat444-1] nat outbound 3000 address-group pppoe-public-1
   ```
   
   # Enable ALG for all protocols and configure the 3-tuple mode.
   
   ```
   [*BRAS1-nat-instance-nat444-1] nat alg all
   [*BRAS1-nat-instance-nat444-1] nat filter mode full-cone
   [*BRAS1-nat-instance-nat444-1] quit
   [*BRAS1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The procedure for configuring a NAT instance named **nat444-2** is similar to that for configuring a NAT instance named **nat444-1**. For details, see the configuration files.
   
   # Configure user groups from which the users go online.
   
   ```
   [~BRAS1] user-group pppoe-nat-1
   [*BRAS1] user-group pppoe-nat-2
   [*BRAS1] commit
   ```
   
   # Bind NAT instances to user groups in an AAA domain.
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain isp1
   [~BRAS1-aaa-domain-isp1] user-group pppoe-nat-1 bind nat instance nat444-1
   [*BRAS1-aaa-domain-isp1] user-group pppoe-nat-2 bind nat instance nat444-2
   [*BRAS1-aaa-domain-isp1] quit
   [*BRAS1-aaa] quit
   [*BRAS1] commit
   ```
   
   # Configure a NAT traffic policy.
   
   1. Define ACL rules for specified user groups.
      ```
      [~BRAS1] acl number 6000
      [*BRAS1-acl4-basic-6000] description for_pppoe-nat-1
      [*BRAS1-acl4-basic-6000] rule 5 permit ip source user-group pppoe-nat-1
      [*BRAS1-acl4-basic-6000] quit
      [*BRAS1] commit
      [~BRAS1] acl number 6001
      [*BRAS1-acl4-basic-6001] description for_pppoe-nat-2
      [*BRAS1-acl4-basic-6001] rule 5 permit ip source user-group pppoe-nat-2
      [*BRAS1-acl4-basic-6001] quit
      [*BRAS1] commit
      [~BRAS1] acl number 6002
      [*BRAS1-acl4-basic-6002] description for_pppoe-no-nat
      [*BRAS1-acl4-basic-6002] rule 5 permit ip source user-group pppoe-nat-2 destination ip-address 192.168.200.0 0.0.0.255
      [*BRAS1-acl4-basic-6002] rule 10 permit ip source user-group pppoe-nat-2 destination ip-address 10.168.200.0 0.0.0.255
      [*BRAS1-acl4-basic-6002] quit
      [*BRAS1] commit
      ```
   2. Configure traffic classifiers.
      ```
      [~BRAS1] traffic classifier nat-c1
      [*BRAS1-classifier-nat-c1] if-match acl 6000
      [*BRAS1-classifier-nat-c1] quit
      [*BRAS1] commit
      [~BRAS1] traffic classifier nat-c2
      [*BRAS1-classifier-nat-c2] if-match acl 6001
      [*BRAS1-classifier-nat-c2] quit
      [*BRAS1] commit
      [~BRAS1] traffic classifier no-nat
      [*BRAS1-classifier-no-nat] if-match acl 6002
      [*BRAS1-classifier-no-nat] quit
      [*BRAS1] commit
      ```
   3. Configure traffic behaviors.
      ```
      [~BRAS1] traffic behavior nat-b1
      [*BRAS1-nat-b1]  nat bind instance nat444-1
      [*BRAS1-nat-b1] quit
      [*BRAS1] commit
      [~BRAS1] traffic behavior nat-b2
      [*BRAS1-nat-b2]  nat bind instance nat444-2
      [*BRAS1-nat-b2] quit
      [*BRAS1] commit
      [~BRAS1] traffic behavior no-nat
      [*BRAS1-no-nat] quit
      [*BRAS1] commit
      ```
   4. Configure a NAT traffic policy.
      ```
      [~BRAS1] traffic policy p1
      [~BRAS1-traffic-policy-p1] classifier no-nat behavior no-nat precedence 2
      [*BRAS1-traffic-policy-p1] classifier nat-c1 behavior nat-b1 precedence 3
      [*BRAS1-traffic-policy-p1] classifier nat-c2 behavior nat-b2 precedence 4
      [*BRAS1-traffic-policy-p1] quit
      [*BRAS1] commit
      ```
   5. Apply the NAT traffic policy in the upstream direction.
      ```
      [~BRAS1] traffic-policy p1 inbound
      [*BRAS1] commit
      ```
9. Enable the device to advertise public routes.
   
   
   ```
   [~BRAS1] bgp 65008
   [*BRAS1-bgp] ipv4-family unicast
   [*BRAS1-bg-af-ipv4] network 0 10.1.1.0 255.255.255.0
   [*BRAS1-bg-af-ipv4] network 0 10.3.1.0 255.255.255.0
   [*BRAS1-bg-af-ipv4] quit
   [*BRAS1-bg] quit
   [~BRAS1] commit
   ```

#### Configuration Files

* BRAS1 configuration file

```
#
sysname BRAS1
# 
license  
 active nat session-table size 16 slot 3 engine 0  
 active nat session-table size 16 slot 2 engine 0  
 active nat bandwidth-enhance slot 3 engine 0
 active nat bandwidth-enhance slot 2 engine 0
#
radius local-ip all
#
radius-attribute hw-policy-name support-type edsg
#
radius-server group rd1                                                       
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^%
#                                                                               
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server class-as-car                                                     
 radius-server calling-station-id include mac                                   
 radius-server user-name original                                               
# 
radius-server authorization 192.168.8.249 shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% server-group rd1
#
service-location 1  
 location slot 3 engine 0 backup slot 2 engine 0 
# 
service-location 2  
 location slot 2 engine 0 backup slot 3 engine 0 
# 
service-instance-group nat444-group1  
 service-location 1 
#
service-instance-group nat444-group2  
 service-location 2 
# 
nat instance nat444-1 id 1  
 service-instance-group nat444-group1  
 port-range 4096  
 nat address-group pppoe-public-1 group-id 1   
 section 0 10.1.1.0 mask 24
 section 1 10.3.1.0 mask 24  
 nat outbound 3000 address-group pppoe-public-1  
 nat alg all  
 nat filter mode full-cone 
#
nat instance nat444-2 id 1  
 service-instance-group nat444-group2  
 port-range 4096  
 nat address-group pppoe-public-2 group-id 1   
 section 0 10.1.1.0 mask 24
 section 1 10.3.1.0 mask 24  
 nat outbound 3000 address-group pppoe-public-2  
 nat alg all  
 nat filter mode full-cone 
# 
user-group pppoe-nat-1 
user-group pppoe-nat-2 
#                                                                               
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.179.155.161 10.179.155.177                                       
#                                                                               
ipv6 prefix pre_nd_1 delegation                                                   
 prefix 2001:DB8:1::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd_1 bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_nd                                                                  
#                                                                               
ipv6 prefix pre_pd_1 delegation                                                   
 prefix 2001:DB8:2::/48                                                         
 pd-unshare-only                                                                
#                                                                               
ipv6 pool pool_pd bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_pd_1                                                                  
# 
value-added-service enable
#
service-group edsg
#                                                                               
acl number 6100                                                                 
 description edsg                                                               
 rule 5 permit ip source service-group edsg destination ip-address 192.168.100.0 0.0.0.255   
 rule 10 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group edsg
#                                                                                
acl ipv6 number 6100                                                            
 rule 5 permit ipv6 source service-group edsg destination ipv6-address 2001:DB8::/32
 rule 10 permit ipv6 source ipv6-address 2001:DB8::/32 destination service-group edsg
#
acl number 6000                                                                 
 description for_pppoe-nat-1                                                               
 rule 5 permit ip source user-group pppoe-nat-1
#
acl number 6001                                                                 
 description for_pppoe-nat-2                                                               
 rule 5 permit ip source user-group pppoe-nat-2
#
acl number 6002                                                                 
 description for_pppoe-no-nat                                                             
 rule 5 permit ip source user-group pppoe-nat-2 destination ip-address 192.168.200.0 0.0.0.255
 rule 10 permit ip source user-group pppoe-nat-2 destination ip-address 10.168.200.0 0.0.0.255
#
dhcpv6 duid 00010001280ef7a400e0fc904b50
#                                                                               
traffic classifier edsg-c1 operator or                                          
 if-match acl 6100 precedence 1                                                 
 if-match ipv6 acl 6100 precedence 2                                            
#
traffic classifier nat-c1 operator or                                          
 if-match acl 6000 precedence 1                                                                                  
# 
traffic classifier nat-c2 operator or                                          
 if-match acl 6001 precedence 1                                                                                  
# 
traffic classifier no-nat operator or                                          
 if-match acl 6002 precedence 1                                                                                  
# 
traffic behavior edsg-b1
#
traffic behavior nat-b1
 nat bind instance nat444-1
#
traffic behavior nat-b2
 nat bind instance nat444-2
# 
traffic behavior no-nat
# 
traffic policy p1                                                               
 share-mode                                                                     
 classifier edsg-c1 behavior edsg-b1 precedence 1
 classifier no-nat behavior no-nat precedence 2
 classifier nat-c1 behavior nat-b1 precedence 3
 classifier nat-c2 behavior nat-b2 precedence 4
#                                                                              
aaa
 #
 authentication-scheme auth1
  authentication-mode radius
 #
 authentication-scheme none
  authentication-mode none
 #
 accounting-scheme acct1
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1                                                     
  prefix-assign-mode unshared                                                   
  ip-pool pool_v4                                                               
  ipv6-pool pool_nd                                                             
  ipv6-pool pool_pd
  user-group pppoe-nat-1 bind nat instance nat444-1
  user-group pppoe-nat-2 bind nat instance nat444-2   
  accounting-start-delay 10 online user-type ppp                                
  accounting-start-delay traffic-forward before-start-accounting                
  user-basic-service-ip-type ipv4                                               
#  
interface Virtual-Template5
 ppp authentication-mode chap
#                                                                               
interface Eth-Trunk2
 mode lacp-static                                                               
 lacp timeout fast                                                              
#                                                                               
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                   
 statistic enable
 pppoe-server bind Virtual-Template 5                                                                 
 user-vlan 1000 4000 qinq 2000 2001                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1            
  client-option82 basinfo-insert cn-telecom                                     
  access-delay 100 even-mac                                                     
 #                                                                              
#                                                                               
interface GigabitEthernet0/1/0                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.2.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:8::7/128                                                 
 ipv6 address auto link-local
#    
traffic-policy p1 inbound
traffic-policy p1 outbound
#
service-policy name service_edsg1 edsg                                          
 authentication-scheme none  
 accounting-scheme acct1                                                 
 radius-server group rd1   
 service-group edsg                                                
 rate-limit cir 100000 pir 100000 inbound                                       
 rate-limit cir 100000 pir 100000 outbound                                      
#   
bgp 65008 
 #  
  ipv4-family unicast     
  network 0 10.1.1.0 255.255.255.0   
  network 0 10.3.1.0 255.255.255.0   
#
return
```

* BRAS2 configuration file

```
#
sysname BRAS2
# 
license  
 active nat session-table size 16 slot 3 engine 0  
 active nat session-table size 16 slot 2 engine 0  
 active nat bandwidth-enhance slot 3 engine 0
 active nat bandwidth-enhance slot 2 engine 0
#
radius local-ip all
#
radius-attribute hw-policy-name support-type edsg
#
radius-server group rd1                                                       
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^%
#                                                                               
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server class-as-car                                                     
 radius-server calling-station-id include mac                                   
 radius-server user-name original                                               
# 
radius-server authorization 192.168.8.249 shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% server-group rd1
#
service-location 1  
 location slot 3 engine 0 backup slot 2 engine 0 
# 
service-location 2  
 location slot 2 engine 0 backup slot 3 engine 0 
# 
service-instance-group nat444-group1  
 service-location 1 
#
service-instance-group nat444-group2  
 service-location 2 
# 
nat instance nat444-1 id 1  
 service-instance-group nat444-group1  
 port-range 4096  
 nat address-group pppoe-public-1 group-id 1   
 section 0 10.1.1.0 mask 24
 section 1 10.3.1.0 mask 24  
 nat outbound 3000 address-group pppoe-public-1  
 nat alg all  
 nat filter mode full-cone 
#
nat instance nat444-2 id 1  
 service-instance-group nat444-group2  
 port-range 4096  
 nat address-group pppoe-public-2 group-id 1   
 section 0 10.1.1.0 mask 24
 section 1 10.3.1.0 mask 24  
 nat outbound 3000 address-group pppoe-public-2  
 nat alg all  
 nat filter mode full-cone 
# 
user-group pppoe-nat-1 
user-group pppoe-nat-2 
#                                                                               
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.179.155.161 10.179.155.177                                       
#                                                                               
ipv6 prefix pre_nd delegation                                                   
 prefix 2001:DB8:1::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_nd                                                                  
#                                                                               
ipv6 prefix pre_pd delegation                                                   
 prefix 2001:DB8:2::/48                                                         
 pd-unshare-only                                                                
#                                                                               
ipv6 pool pool_pd bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_pd_1                                                                  
# 
value-added-service enable
#
service-group edsg
#                                                                               
acl number 6100                                                                 
 description edsg                                                               
 rule 5 permit ip source service-group edsg destination ip-address 192.168.100.0 0.0.0.255   
 rule 10 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group edsg
#                                                                                
acl ipv6 number 6100                                                            
 rule 5 permit ipv6 source service-group edsg destination ipv6-address 2001:DB8::/32
 rule 10 permit ipv6 source ipv6-address 2001:DB8::/32 destination service-group edsg
#
acl number 6000                                                                 
 description for_pppoe-nat-1                                                               
 rule 5 permit ip source user-group pppoe-nat-1
#
acl number 6001                                                                 
 description for_pppoe-nat-2                                                               
 rule 5 permit ip source user-group pppoe-nat-2
#
acl number 6002                                                                 
 description for_pppoe-no-nat                                                             
 rule 5 permit ip source user-group pppoe-nat-2 destination ip-address 192.168.200.0 0.0.0.255
 rule 10 permit ip source user-group pppoe-nat-2 destination ip-address 10.168.200.0 0.0.0.255
#
dhcpv6 duid 00010001280ef7a400e0fc904b50
#                                                                               
traffic classifier edsg-c1 operator or                                          
 if-match acl 6100 precedence 1                                                 
 if-match ipv6 acl 6100 precedence 2                                            
#
traffic classifier nat-c1 operator or                                          
 if-match acl 6000 precedence 1                                                                                  
# 
traffic classifier nat-c2 operator or                                          
 if-match acl 6001 precedence 1                                                                                  
# 
traffic classifier no-nat operator or                                          
 if-match acl 6002 precedence 1                                                                                  
# 
traffic behavior edsg-b1
#
traffic behavior nat-b1
 nat bind instance nat444-1
#
traffic behavior nat-b2
 nat bind instance nat444-2
# 
traffic behavior no-nat
# 
traffic policy p1                                                               
 share-mode                                                                     
 classifier edsg-c1 behavior edsg-b1 precedence 1
 classifier no-nat behavior no-nat precedence 2
 classifier nat-c1 behavior nat-b1 precedence 3
 classifier nat-c2 behavior nat-b2 precedence 4
#                                                                                
aaa
 #
 authentication-scheme auth1
  authentication-mode radius
 #
 authentication-scheme none
  authentication-mode none
 #
 accounting-scheme acct1
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1                                                     
  prefix-assign-mode unshared                                                   
  ip-pool pool_v4                                                               
  ipv6-pool pool_nd                                                             
  ipv6-pool pool_pd
  user-group pppoe-nat-1 bind nat instance nat444-1
  user-group pppoe-nat-2 bind nat instance nat444-2   
  accounting-start-delay 10 online user-type ppp                                
  accounting-start-delay traffic-forward before-start-accounting                
  user-basic-service-ip-type ipv4                                               
#  
interface Virtual-Template5
 ppp authentication-mode chap
#                                                                               
interface Eth-Trunk2
 mode lacp-static                                                               
 lacp timeout fast                                                              
#                                                                               
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                   
 statistic enable
 pppoe-server bind Virtual-Template 5                                                                 
 user-vlan 1000 4000 qinq 2000 2001                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1            
  client-option82 basinfo-insert cn-telecom                                     
  access-delay 100 odd-mac                                                     
 #                                                                              
#                                                                               
interface GigabitEthernet0/1/0                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.4.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:9::7/128                                                 
 ipv6 address auto link-local
#    
traffic-policy p1 inbound
traffic-policy p1 outbound
#
service-policy name service_edsg1 edsg                                          
 authentication-scheme none  
 accounting-scheme acct1                                                 
 radius-server group rd1   
 service-group edsg                                                
 rate-limit cir 100000 pir 100000 inbound                                       
 rate-limit cir 100000 pir 100000 outbound                                      
# 
bgp 65008 
 #  
  ipv4-family unicast     
  network 0 10.1.1.0 255.255.255.0   
  network 0 10.3.1.0 255.255.255.0   
#
return
```