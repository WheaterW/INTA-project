Example for Configuring Outbound-Interface NAT Load Balancing on an Enterprise Network
======================================================================================

This section provides an example for configuring dual outbound interfaces on NAT-Device so that external network users access an internal server through different interfaces and internal user traffic destined for the Internet is load-balanced.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374651__w1), NAT-Device functions as an enterprise network gateway and is dual-homed to the Internet through interfaces 2 and 3. NAT is configured to convert private IP addresses to public IP addresses. The enterprise network wants to provide web and FTP server access services for Internet users. The web server is assigned 192.168.4.1/16 and 192.168.5.1/16, and the FTP server is assigned 192.168.2.1/16 and 192.168.3.1/16.

[Figure 1](#EN-US_TASK_0172374651__w1) shows IP addresses of interfaces. The configuration requirements are as follows:

* External network users can access the web and FTP servers within the enterprise network.
* Internal users and servers can access one another, without NAT conversion.
* The traffic sent from the enterprise network to the Internet is load-balanced based on source IP addresses.

**Figure 1** Networking for configuring outbound-interface NAT load balancing on an enterprise network![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/2/0, GE 0/2/1, and GE 0/2/2, respectively.


  
![](images/fig_dc_ne_nat_cfg_00730001a.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure load balancing.
2. Configure basic NAT functions.
3. Configure internal servers.
4. Enable the NAT ALG function for the web and FTP protocols.
5. Configure a NAT traffic diversion policy.
6. Apply the NAT traffic diversion policy.
7. Configure default routes.

#### Data Preparation

To complete the configuration, you need the following data:

* NAT instance names (nat1 and nat2) and indexes (1 and 2)
* Address pool name (address-group1) and ID (1)
* Private IP addresses of the FTP server and web server in NAT instance **nat1** (192.168.2.1 and 192.168.4.1, respectively) and in NAT instance **nat2** (192.168.3.1 and 192.168.5.1, respectively)
* IP addresses (192.168.0.1/16, 10.11.1.1/24, and 10.11.2.1/24) of GE 0/2/0, GE 0/2/1, and GE 0/2/2
* ACL numbers (3000 through 3005)
* NAT traffic diversion policy applied to GE 0/2/0; ACL 3000 and NAT instance **nat1** bound to GE 0/2/1; ACL 3000 and NAT instance **nat1** bound to GE 0/2/2

#### Procedure

1. Configure basic NAT functions.
   1. Enable the NAT device to load-balance received packets based on source IP addresses in all slots.
      
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname NAT-Device
      [*HUAWEI] commit
      [~NAT-Device] load-balance hash-key ip source-ip slot all
      [*NAT-Device] commit
      ```
   2. Create NAT instances named **nat1** and **nat2**.
      
      
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
   3. Assign IP addresses to interfaces.
      
      
      ```
      [~NAT-Device] interface gigabitEthernet 0/2/0
      [~NAT-Device-GigabitEthernet0/2/1] ip address 192.168.0.1 16
      [*NAT-Device-GigabitEthernet0/2/1] commit
      [~NAT-Device-GigabitEthernet0/2/1] quit
      [~NAT-Device] interface gigabitEthernet 0/2/1
      [~NAT-Device-GigabitEthernet0/2/1] ip address 10.11.1.1 24
      [*NAT-Device-GigabitEthernet0/2/1] commit
      [~NAT-Device-GigabitEthernet0/2/1] quit
      [~NAT-Device] interface gigabitEthernet 0/2/2
      [~NAT-Device-GigabitEthernet0/2/2] ip address 10.11.2.1 24
      [*NAT-Device-GigabitEthernet0/2/2] commit
      [~NAT-Device-GigabitEthernet0/2/2] quit
      ```
   4. Configure NAT address pools.
      
      
      ```
      [~NAT-Device] nat instance nat1 id 1
      [~NAT-Device-nat-instance-nat1] nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet 0/2/1
      [*NAT-Device-nat-instance-nat1] commit
      [~NAT-Device-nat-instance-nat1] quit
      [~NAT-Device] nat instance nat2 id 2
      [~NAT-Device-nat-instance-nat2] nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet 0/2/2
      [*NAT-Device-nat-instance-nat2] commit
      [~NAT-Device-nat-instance-nat2] quit
      ```
2. Configure the mapping between the public and private IP addresses of the internal NAT server.
   
   
   ```
   [~NAT-Device] nat instance nat1 id 1
   [~NAT-Device-nat-instance-nat1] nat server protocol tcp global unnumbered interface GigabitEthernet 0/2/1 ftp inside 192.168.2.1 ftp
   [~NAT-Device-nat-instance-nat1] nat server protocol tcp global unnumbered interface GigabitEthernet 0/2/1 www inside 192.168.4.1 www
   [*NAT-Device-nat-instance-nat1] commit
   [~NAT-Device-nat-instance-nat1] quit
   [~NAT-Device] nat instance nat2 id 2
   [~NAT-Device-nat-instance-nat2] nat server protocol tcp global unnumbered interface GigabitEthernet 0/2/2 ftp inside 192.168.3.1 ftp
   [~NAT-Device-nat-instance-nat2] nat server protocol tcp global unnumbered interface GigabitEthernet 0/2/2 www inside 192.168.5.1 www
   [*NAT-Device-nat-instance-nat2] commit
   [~NAT-Device-nat-instance-nat2] quit
   ```
3. Configure the NAT ALG function. Enable the NAT ALG function for FTP and DNS in each NAT instance. Configure a DNS mapping entry that contains a domain name, a public IP address, and a private IP address in each NAT instance for NAT processing that is performed after the DNS server resolves the IP address of the internal server.
   
   
   ```
   [~NAT-Device] nat instance nat1
   [~NAT-Device-nat-instance-nat1] nat alg ftp
   [*NAT-Device-nat-instance-nat1] nat alg dns
   [*NAT-Device-nat-instance-nat1] nat dns-mapping domain www.huawei.com global-address 10.11.1.1 inside-address 192.168.4.1
   [*NAT-Device-nat-instance-nat1] commit
   [~NAT-Device-nat-instance-nat1] quit
   ```
   ```
   [~NAT-Device] nat instance nat2
   [~NAT-Device-nat-instance-nat2] nat alg ftp
   [*NAT-Device-nat-instance-nat2] nat alg dns
   [*NAT-Device-nat-instance-nat2] nat dns-mapping domain www.huawei.com global-address 10.11.2.1 inside-address 192.168.5.1
   [*NAT-Device-nat-instance-nat2] commit
   [~NAT-Device-nat-instance-nat2] quit
   ```
4. Configure the redirection function by specifying a redirection next-hop IP address for private-to-public traffic in each NAT instance.
   
   
   ```
   [~NAT-Device] nat instance nat1
   [~NAT-Device-nat-instance-nat1] redirect ip-nexthop 10.11.1.2 outbound
   [*NAT-Device-nat-instance-nat1] commit
   [~NAT-Device-nat-instance-nat1] quit
   ```
   ```
   [~NAT-Device] nat instance nat2
   [~NAT-Device-nat-instance-nat2] redirect ip-nexthop 10.11.2.2 outbound
   [*NAT-Device-nat-instance-nat2] commit
   [~NAT-Device-nat-instance-nat2] quit
   ```
5. Configure a NAT traffic diversion policy.
   1. Configure an ACL numbered **3000** to allow hosts on the enterprise network to access the Internet.
      
      
      ```
      [~NAT-Device] acl 3000
      [*NAT-Device-acl4-advance-3000] rule 1 permit ip
      [*NAT-Device-acl4-advance-3000] commit
      [~NAT-Device-acl4-advance-3000] quit
      ```
   2. Configure an ACL numbered **3001** to allow hosts on the enterprise network to access one another.
      
      
      ```
      [~NAT-Device] acl 3001
      [*NAT-Device-acl4-advance-3001] rule 1 permit ip source 192.168.0.0 0.0.255.255
      [*NAT-Device-acl4-advance-3001] commit
      [~NAT-Device-acl4-advance-3001] rule 1 permit ip destination 2.1.1.0 0.0.0.255
      [*NAT-Device-acl4-advance-3001] commit
      [~NAT-Device-acl4-advance-3001] quit
      ```
   3. Configure an ACL numbered **3002** to allow the host at 192.168.2.1/32 on the enterprise network to access the Internet.
      
      
      ```
      [~NAT-Device] acl 3002
      [*NAT-Device-acl4-advance-3002] rule 1 permit ip source 192.168.2.1 0.0.0.0
      [*NAT-Device-acl4-advance-3002] commit
      [~NAT-Device-acl4-advance-3002] rule 1 permit ip destination 2.1.1.0 0.0.0.255
      [*NAT-Device-acl4-advance-3002] commit
      [~NAT-Device-acl4-advance-3002] quit
      ```
   4. Configure an ACL numbered **3003** to allow the host at 192.168.3.1/32 on the enterprise network to access the Internet.
      
      
      ```
      [~NAT-Device] acl 3003
      [*NAT-Device-acl4-advance-3003] rule 1 permit ip source 192.168.3.1 0.0.0.0
      [*NAT-Device-acl4-advance-3003] commit
      [~NAT-Device-acl4-advance-3003] rule 1 permit ip destination 2.1.1.0 0.0.0.255
      [*NAT-Device-acl4-advance-3003] commit
      [~NAT-Device-acl4-advance-3003] quit
      ```
   5. Configure an ACL numbered **3004** to allow the host at 192.168.4.1/32 on the enterprise network to access the Internet.
      
      
      ```
      [~NAT-Device] acl 3004
      [*NAT-Device-acl4-advance-3004] rule 1 permit ip source 192.168.4.1 0.0.0.0
      [*NAT-Device-acl4-advance-3004] commit
      [~NAT-Device-acl4-advance-3004] rule 1 permit ip destination 2.1.1.0 0.0.0.255
      [*NAT-Device-acl4-advance-3004] commit
      [~NAT-Device-acl4-advance-3004] quit
      ```
   6. Configure an ACL numbered **3005** to allow the host at 192.168.5.1/32 on the enterprise network to access the Internet.
      
      
      ```
      [~NAT-Device] acl 3005
      [*NAT-Device-acl4-advance-3005] rule 1 permit ip source 192.168.5.1 0.0.0.0
      [*NAT-Device-acl4-advance-3005] commit
      [~NAT-Device-acl4-advance-3005] rule 1 permit ip destination 2.1.1.0 0.0.0.255
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
   8. Configure traffic behaviors for data that needs to be redirected. Set the redirection next-hop IP address to 10.11.1.2 in a traffic behavior named **redirectover2** and 10.11.2.2 in a traffic behavior named **redirectover3**.
      
      
      ```
      [~NAT-Device] traffic behavior redirectover1
      [*NAT-Device-behavior-redirectover1] commit
      [~NAT-Device-behavior-redirectover1] quit
      ```
      
      
      ```
      [~NAT-Device] traffic behavior redirectover2
      [*NAT-Device-behavior-redirectover2] redirect ip-nexthop 10.11.1.2
      [*NAT-Device-behavior-redirectover2] commit
      [~NAT-Device-behavior-redirectover2] quit
      ```
      
      
      ```
      [~NAT-Device] traffic behavior redirectover3
      [*NAT-Device-behavior-redirectover3] redirect ip-nexthop 10.11.2.2
      [*NAT-Device-behavior-redirectover3] commit
      [~NAT-Device-behavior-redirectover3] quit
      ```
   9. Bind the traffic classifiers with the traffic behaviors in a traffic policy.
      
      
      * Data flows exchanged by users on the network segment of 192.168.0.0/16 within the enterprise network are assigned a priority value of 1 (higher) and are not processed by NAT.
      * Data flows with the source IP address 192.168.2.1/32 pass through outbound interface 2 and are assigned a priority value of 2.
      * Data flows with the source IP address 192.168.3.1/32 pass through outbound interface 3 and are assigned a priority value of 3.
      * Data flows with the source IP address 192.168.4.1/32 pass through outbound interface 2 and are assigned a priority value of 4.
      * Data flows with the source IP address 192.168.5.1/32 pass through outbound interface 3 and are assigned a priority value of 5.
      ```
      [~NAT-Device] traffic policy redirect
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover1 behavior redirectover1 precedence 1
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover2 behavior redirectover2 precedence 2
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover3 behavior redirectover3 precedence 3
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover4 behavior redirectover2 precedence 4
      [*NAT-Device-trafficpolicy-redirect] classifier redirectover5 behavior redirectover3 precedence 5
      [*NAT-Device-trafficpolicy-redirect] commit
      [~NAT-Device-trafficpolicy-redirect] quit
      ```
6. Apply the traffic classification policy to interfaces.
   
   
   ```
   [~NAT-Device] interface gigabitEthernet 0/2/0
   [*NAT-Device-GigabitEthernet0/2/0] traffic-policy redirect inbound
   [*NAT-Device-GigabitEthernet0/2/0] commit
   [~NAT-Device-GigabitEthernet0/2/0] quit
   [~NAT-Device] interface gigabitEthernet 0/2/1
   [*NAT-Device-GigabitEthernet0/2/1] nat bind acl 3000 instance nat1
   [*NAT-Device-GigabitEthernet0/2/1] commit
   [~NAT-Device-GigabitEthernet0/2/1] quit
   [~NAT-Device] interface gigabitEthernet 0/2/2
   [*NAT-Device-GigabitEthernet0/2/2] nat bind acl 3000 instance nat2
   [*NAT-Device-GigabitEthernet0/2/2] commit
   [~NAT-Device-GigabitEthernet0/2/2] quit
   ```
7. Configure default routes.
   
   
   ```
   [~NAT-Device] ip route-static 0.0.0.0 0.0.0.0 10.11.1.2
   [*NAT-Device] ip route-static 0.0.0.0 0.0.0.0 10.11.2.2
   [*NAT-Device] commit
   ```

#### Configuration Files

```
# 
sysname NAT-Device 
# 
load-balance hash-key ip source-ip slot all
#
service-location 1
 location slot 3  
# 
service-instance-group group1 
 service-location 1 
#
nat instance nat1 id 1
 service-instance-group group1
 nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet 0/2/1
 nat server protocol tcp global unnumbered interface GigabitEthernet 0/2/1 ftp inside 192.168.2.1 ftp
 nat server protocol tcp global unnumbered interface GigabitEthernet 0/2/1 www inside 192.168.4.1 www
 nat alg ftp
 nat alg dns
 redirect ip-nexthop 10.11.1.2 outbound
 nat dns-mapping domain www.huawei.com global-address 10.11.1.1 inside-address 192.168.4.1
# 
nat instance nat2 id 2
 service-instance-group group1
 nat address-group address-group1 group-id 1 unnumbered interface GigabitEthernet 0/2/2
 nat server protocol tcp global unnumbered interface GigabitEthernet 0/2/2 ftp inside 192.168.3.1 ftp
 nat server protocol tcp global unnumbered interface GigabitEthernet 0/2/2 www inside 192.168.5.1 www
 nat alg ftp
 nat alg dns
 redirect ip-nexthop 10.11.2.2 outbound
 nat dns-mapping domain www.huawei.com global-address 10.11.2.1 inside-address 192.168.5.1
#
acl number 3000                            
 rule 1 permit ip                                                              
#
acl number 3001
 rule 1 permit ip source 192.168.0.0 0.0.255.255 
 rule 1 permit ip destination 2.1.1.0 0.0.0.255
#
acl number 3002 
 rule 1 permit ip source 192.168.2.1 0.0.0.0
 rule 1 permit ip destination 2.1.1.0 0.0.0.255
# 
acl number 3003 
 rule 1 permit ip source 192.168.3.1 0.0.0.0  
 rule 1 permit ip destination 2.1.1.0 0.0.0.255
#
acl number 3004   
 rule 1 permit ip source 192.168.4.1 0.0.0.0
 rule 1 permit ip destination 2.1.1.0 0.0.0.255
#
acl number 3005
 rule 1 permit ip source 192.168.5.1 0.0.0.0
 rule 1 permit ip destination 2.1.1.0 0.0.0.255
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
#                     
traffic behavior redirectover2  
 redirect ip-nexthop 10.11.1.2  
#
traffic behavior redirectover3  
 redirect ip-nexthop 10.11.2.2  
#        
traffic policy redirect  
 classifier redirectover1 behavior redirectover1 precedence 1 
 classifier redirectover2 behavior redirectover2 precedence 2
 classifier redirectover3 behavior redirectover3 precedence 3  
 classifier redirectover4 behavior redirectover2 precedence 4 
 classifier redirectover5 behavior redirectover3 precedence 5 
#
interface GigabitEthernet 0/2/0 
 undo shutdown 
 ip address 192.168.0.1 255.255.0.0
 traffic-policy redirect inbound 
#
interface GigabitEthernet 0/2/1 
 undo shutdown 
 ip address 10.11.1.1 255.255.255.0
 nat bind acl 3000 instance nat1 
#
interface GigabitEthernet 0/2/2 
 undo shutdown 
 ip address 10.11.2.1 255.255.255.0 
 nat bind acl 3000 instance nat2 
# 
ip route-static 0.0.0.0 0.0.0.0 10.11.1.2 
ip route-static 0.0.0.0 0.0.0.0 10.11.2.2 
#  
return
```