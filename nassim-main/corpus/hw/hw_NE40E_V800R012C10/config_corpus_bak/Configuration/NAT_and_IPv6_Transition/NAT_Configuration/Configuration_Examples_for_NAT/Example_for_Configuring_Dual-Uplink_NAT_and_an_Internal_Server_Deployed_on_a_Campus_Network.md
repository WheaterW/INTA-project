Example for Configuring Dual-Uplink NAT and an Internal Server Deployed on a Campus Network
===========================================================================================

This section provides an example for configuring dual-uplink NAT and an internal server deployed on a campus network so that hosts on an internal network can access an external network server through different outbound interfaces.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374654__w1), NAT-Device's interface 1 connects to a campus network, interface 2 connects to the Internet, and interface 3 connects to an education network. Hosts on the campus network access the education network through outbound interface 3 and the Internet through outbound interface 2. The internal server within the campus network is assigned a private IP address 192.168.4.1/24 and a public IP address 2.1.1.3.

[Figure 1](#EN-US_TASK_0172374654__w1) shows IP addresses of interfaces. The configuration requirements are as follows:

* Only education network users can access the internal server within the campus network.
* Users within the campus must preferentially access the education network, and must access the Internet only if the education network resources are insufficient.
* When the campus network data is sent to an external network through an outbound interface, the outbound interface selected based on a destination IP address takes preference over that selected based on a source IP address.
* Hosts and the server on the campus network segment 192.168.0.0/16 can access one another, without NAT conversion.
* When a device on the education network or Internet is configured to advertise routes, bidirectional NAT traffic must pass through the same network-side interface on the NAT device. For traffic exchanged between the education network and campus network, the route destined to the education network has a higher priority than that destined to the Internet. For traffic exchanged between the Internet and campus network, the route destined to the Internet has a higher priority than that destined to the education network.

**Figure 1** Networking for configuring dual-uplink NAT and an internal server on a campus network![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/2/0, GE 0/2/1, and GE 0/2/2, respectively.


  
![](images/fig_dc_ne_nat_cfg_00720001a.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure an internal server.
3. Configure redirection.
4. Configure a NAT traffic diversion policy.
5. Apply the NAT traffic diversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* NAT instance names (nat1 and nat2), indexes (1 and 2), and public address pool and education network address pool assigned to nat1 and nat2, respectively
* NAT-Device's address pool names (address-group1 and address-group2) and address pool numbers (1 and 2)
* ACL numbers (3001 through 3005)
* Names (GE 0/2/0, GE 0/2/2, and GE 0/2/1) and IP addresses (192.168.1.1/24, 2.1.1.1/24, and 1.1.1.1/24) of interfaces, respectively, to which a NAT traffic diversion policy is applied
* Private IP address (192.168.4.1) and public IP address (2.1.1.3) of an internal server within the campus network

#### Procedure

1. Configure basic NAT functions.
   1. Create NAT instances named **nat1** and **nat2**.
      
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname NAT-Device
      [*HUAWEI] commit
      ```
      
      
      ```
      [~NAT-Device] service-location 1
      [*NAT-Device-service-location-1] location slot 3
      [*NAT-Device-service-location-1] commit
      [~NAT-Device-service-location-1] quit
      [~NAT-Device] service-instance-group group1
      [*NAT-Device-service-instance-group-group1] service-location 1
      [*NAT-Device-service-instance-group-group1] commit
      [~NAT-Device-service-instance-group-group1] quit
      [~NAT-Device] nat instance nat1 id 1
      [*NAT-Device-nat-instance-nat1] service-instance-group group1
      [*NAT-Device-nat-instance-nat1] commit
      [~NAT-Device-nat-instance-nat1] quit
      [~NAT-Device] nat instance nat2 id 2
      [*NAT-Device-nat-instance-nat2] service-instance-group group1
      [*NAT-Device-nat-instance-nat2] commit
      [~NAT-Device-nat-instance-nat2] quit
      ```
   2. Configure NAT address pools.
      
      
      * In the NAT instance named **nat1**, configure an address pool used in NAT processing to access non-education-network addresses.
      * In the NAT instance named **nat2**, configure an address pool used in NAT processing to access education network addresses.
      ```
      [~NAT-Device] nat instance nat1 id 1
      [~NAT-Device-nat-instance-nat1] nat address-group address-group1 group-id 1 1.1.1.10 1.1.1.100
      [*NAT-Device-nat-instance-nat1] redirect ip-nexthop 1.1.1.2 outbound
      [*NAT-Device-nat-instance-nat1] commit
      [~NAT-Device-nat-instance-nat1] quit
      ```
      ```
      [~NAT-Device] nat instance nat2 id 2
      [~NAT-Device-nat-instance-nat2] nat address-group address-group2 group-id 2 2.1.1.50 2.1.1.100
      [*NAT-Device-nat-instance-nat2] redirect ip-nexthop 2.1.1.2 outbound
      [*NAT-Device-nat-instance-nat2] commit
      [~NAT-Device-nat-instance-nat2] quit
      ```
2. Configure an internal server in the NAT instance named **nat2** and assign the private and public IP addresses of **192.168.4.1** and **2.1.1.3**, respectively.
   
   
   ```
   [~NAT-Device] nat instance nat2 id 2
   [~NAT-Device-nat-instance-nat2] nat server-mode enable
   [*NAT-Device-nat-instance-nat2] nat server global 2.1.1.3 inside 192.168.4.1
   [*NAT-Device-nat-instance-nat2] commit
   [~NAT-Device-nat-instance-nat2] quit
   ```
3. Configure a NAT traffic diversion policy.
   1. Configure an ACL numbered **3000** to allow hosts on the campus network to access the education network and Internet.
      
      
      ```
      [~NAT-Device] acl 3000
      [*NAT-Device-acl4-advance-3000] rule 1 permit ip
      [*NAT-Device-acl4-advance-3000] commit
      [~NAT-Device-acl4-advance-3000] quit
      ```
   2. Configure an ACL numbered **3001** to allow hosts on the campus network to access the Internet.
      
      
      ```
      [~NAT-Device] acl 3001
      [*NAT-Device-acl4-advance-3001] rule 1 permit ip destination 1.1.1.2 0.0.0.0
      [*NAT-Device-acl4-advance-3001] commit
      [~NAT-Device-acl4-advance-3001] quit
      ```
   3. Configure an ACL numbered **3002** to allow hosts on the campus network to access the education network.
      
      
      ```
      [~NAT-Device] acl 3002
      [*NAT-Device-acl4-advance-3002] rule 1 permit ip destination 2.1.1.2 0.0.0.0
      [*NAT-Device-acl4-advance-3002] commit
      [~NAT-Device-acl4-advance-3002] quit
      ```
   4. Configure an ACL numbered **3003** to allow hosts on the campus network to access one another.
      
      
      ```
      [~NAT-Device] acl 3003
      [*NAT-Device-acl4-advance-3003] rule 1 permit ip destination 192.168.0.0 0.0.255.255
      [*NAT-Device-acl4-advance-3003] commit
      [~NAT-Device-acl4-advance-3003] quit
      ```
   5. Configure an ACL numbered **3004** to allow hosts on the campus network segment 192.168.2.0/24 to access external networks.
      
      
      ```
      [~NAT-Device] acl 3004
      [*NAT-Device-acl4-advance-3004] rule 1 permit ip source 192.168.2.0 0.0.0.255
      [*NAT-Device-acl4-advance-3004] commit
      [~NAT-Device-acl4-advance-3004] quit
      ```
   6. Configure an ACL numbered 3005 to allow hosts on the campus network segment 192.168.3.0/24 to access external networks.
      
      
      ```
      [~NAT-Device] acl 3005
      [*NAT-Device-acl4-advance-3005] rule 1 permit ip source 192.168.3.0 0.0.0.255
      [*NAT-Device-acl4-advance-3005] commit
      [~NAT-Device-acl4-advance-3005] quit
      ```
   7. Configure traffic classifiers for data that needs to be redirected.
      
      
      ```
      [~NAT-Device] traffic classifier redirectover1 operator or
      [*NAT-Device-classifier-redirectover1] if-match acl 3001
      [*NAT-Device-classifier-redirectover1] commit
      [~NAT-Device-classifier-redirectover1] quit
      ```
      
      
      ```
      [~NAT-Device] traffic classifier redirectover2 operator or
      [*NAT-Device-classifier-redirectover2] if-match acl 3002
      [*NAT-Device-classifier-redirectover2] commit
      [~NAT-Device-classifier-redirectover2] quit
      ```
      
      
      ```
      [~NAT-Device] traffic classifier redirectover3 operator or
      [*NAT-Device-classifier-redirectover3] if-match acl 3003
      [*NAT-Device-classifier-redirectover3] commit
      [~NAT-Device-classifier-redirectover3] quit
      ```
      
      
      ```
      [~NAT-Device] traffic classifier redirectover4 operator or
      [*NAT-Device-classifier-redirectover4] if-match acl 3004
      [*NAT-Device-classifier-redirectover4] commit
      [~NAT-Device-classifier-redirectover4] quit
      ```
      
      
      ```
      [~NAT-Device] traffic classifier redirectover5 operator or
      [*NAT-Device-classifier-redirectover5] if-match acl 3005
      [*NAT-Device-classifier-redirectover5] commit
      [~NAT-Device-classifier-redirectover5] quit
      ```
   8. Configure traffic behaviors for data that needs to be redirected. Set the redirection next-hop IP address to 1.1.1.2 in a traffic behavior named **redirectover1** and 2.1.1.2 in a traffic behavior named **redirectover2**.
      
      
      ```
      [~NAT-Device] traffic behavior redirectover1
      [*NAT-Device-behavior-redirectover1] redirect ip-nexthop 1.1.1.2
      [*NAT-Device-behavior-redirectover1] commit
      [~NAT-Device-behavior-redirectover1] quit
      ```
      
      
      ```
      [~NAT-Device] traffic behavior redirectover2
      [*NAT-Device-behavior-redirectover2] redirect ip-nexthop 2.1.1.2
      [*NAT-Device-behavior-redirectover2] commit
      [~NAT-Device-behavior-redirectover2] quit
      ```
      
      
      ```
      [~NAT-Device] traffic behavior redirectover3
      [*NAT-Device-behavior-redirectover3] commit
      [~NAT-Device-behavior-redirectover3] quit
      ```
   9. Bind the traffic classifiers with the traffic behaviors in a traffic policy.
      
      
      * Data flows destined for 1.1.1.2/32 pass through the outbound interface 2 and are assigned a priority value of 1 (higher).
      * Data flows destined for 2.1.1.2/32 pass through the outbound interface 3 and are assigned a priority value of 2 (higher).
      * Data flows exchanged by users on the network segment of 192.168.0.0/16 within the campus network are assigned a priority value of 3 and are not processed by NAT.
      * Data flows originating from the network segment 192.168.2.0/24 pass through the outbound interface 2 and are assigned a priority value of 4 (lower).
      * Data flows originating from the network segment 192.168.3.0/24 pass through the outbound interface 3 and are assigned a priority value of 5 (lower).
      ```
      [~NAT-Device] traffic policy redirect
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover1 behavior redirectover1 precedence 1
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover2 behavior redirectover2 precedence 2
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover3 behavior redirectover3 precedence 3
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover4 behavior redirectover1 precedence 4
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover5 behavior redirectover2 precedence 5
      [*NAT-Device-trafficpolicy-redirect] commit
      [~NAT-Device-trafficpolicy-redirect] quit
      ```
4. Apply the NAT traffic diversion policy.
   1. Apply the NAT traffic diversion policy to GE 0/2/0 to redirect incoming data flows.
      
      
      ```
      [~NAT-Device] interface gigabitEthernet 0/2/0
      [~NAT-Device-GigabitEthernet0/2/0] ip address 192.168.1.1 255.255.255.0
      [*NAT-Device-GigabitEthernet0/2/0] traffic-policy redirect inbound
      [*NAT-Device-GigabitEthernet0/2/0] commit
      [~NAT-Device-GigabitEthernet0/2/0] quit
      ```
   2. Apply the traffic classification policy to GE 0/2/2 that is an outbound interface connected to the education network, and bind the policy to the NAT instance named **nat2**.
      
      
      ```
      [~NAT-Device] interface gigabitEthernet 0/2/2
      [~NAT-Device-GigabitEthernet0/2/2] ip address 2.1.1.1 255.255.255.0
      [*NAT-Device-GigabitEthernet0/2/2] nat bind acl 3000 instance nat2
      [*NAT-Device-GigabitEthernet0/2/2] commit
      [~NAT-Device-GigabitEthernet0/2/2] quit
      ```
   3. Apply the traffic classification policy to GE 0/2/1 that is the outbound interface connected to the Internet, and bind the policy to the NAT instance named **nat1**.
      
      
      ```
      [~NAT-Device] interface gigabitEthernet 0/2/1
      [~NAT-Device-GigabitEthernet0/2/1] ip address 1.1.1.1 255.255.255.0
      [*NAT-Device-GigabitEthernet0/2/1] nat bind acl 3000 instance nat1
      [*NAT-Device-GigabitEthernet0/2/1] commit
      [~NAT-Device-GigabitEthernet0/2/1] quit
      ```

#### Configuration Files

```
# 
sysname NAT-Device 
# 
service-location 1
 location slot 3
# 
service-instance-group group1 
 service-location 1 
#
nat instance nat1 id 1     
 service-instance-group group1
 nat address-group address-group1 group-id 1 1.1.1.50 1.1.1.100 
 redirect ip-nexthop 1.1.1.2 outbound
# 
nat instance nat2 id 2
 service-instance-group group1
 nat address-group address-group2 group-id 2 2.1.1.50 2.1.1.100
 nat server-mode enable
 nat server global 2.1.1.3 inside 192.168.4.1
 redirect ip-nexthop 2.1.1.2 outbound
#
acl number 3000  
 rule 1 permit ip                                                              
# 
acl number 3001    
 rule 1 permit ip destination 1.1.1.0 0.0.0.255 
#     
acl number 3002       
 rule 1 permit ip destination 2.1.1.0 0.0.0.255   
#      
acl number 3003   
 rule 1 permit ip destination 192.168.0.0 0.0.255.255  
#
acl number 3004     
 rule 1 permit ip source 192.168.2.0 0.0.0.255    
#  
acl number 3005   
 rule 1 permit ip source 192.168.3.0 0.0.0.255  
# 
traffic classifier redirectover1 operator or  
 if-match acl 3001 precedence 1   
#        
traffic classifier redirectover2 operator or  
 if-match acl 3002 precedence 1     
#       
traffic classifier redirectover3 operator or   
 if-match acl 3003 precedence 1       
#
traffic classifier redirectover4 operator or  
 if-match acl 3004 precedence 1   
#
traffic classifier redirectover5 operator or   
 if-match acl 3005 precedence 1   
#                  
traffic behavior redirectover1  
 redirect ip-nexthop 1.1.1.2     
#           
traffic behavior redirectover2   
 redirect ip-nexthop 2.1.1.2        
#
traffic behavior redirectover3     
#                       
traffic policy redirect     
 classifier redirectover1 behavior redirectover1 precedence 1
 classifier redirectover2 behavior redirectover2 precedence 2 
 classifier redirectover3 behavior redirectover3 precedence 3 
 classifier redirectover4 behavior redirectover1 precedence 4
 classifier redirectover5 behavior redirectover2 precedence 5
#
interface GigabitEthernet 0/2/0 
 undo shutdown 
 ip address 192.168.1.1 255.255.255.0
 traffic-policy redirect inbound
#
interface GigabitEthernet 0/2/2 
 undo shutdown 
 ip address 2.1.1.1 255.255.255.0
 nat bind acl 3000 instance nat2
#  
interface GigabitEthernet 0/2/1 
 undo shutdown 
 ip address 1.1.1.1 255.255.255.0
 nat bind acl 3000 instance nat1
#  
return
```