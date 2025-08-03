Example for Configuring Distributed NAT Load Balancing
======================================================

This section provides an example for configuring distributed NAT load balancing. After distributed NAT load balancing is configured, IP addresses of multiple home users can be balanced to different CPUs for NAT in the same NAT service instance.

#### Networking Requirements

In the distributed NAT scenario shown in [Figure 1](#EN-US_TASK_0000001139835263__en-us_task_0172374595_fig_dc_ne_cfg_nat_005701), home users access a BRAS through PPPoE, IPoE, web authentication, or other ways. The BRAS implements user authentication, authorization, and accounting. It also provides NAT services to convert between the private addresses of home users and external public addresses in the CPU-based load balancing mode for home users to access the Internet.

It is required that IP addresses of the home users (PC1 and PC2 in [Figure 1](#EN-US_TASK_0000001139835263__en-us_task_0172374595_fig_dc_ne_cfg_nat_005701)) in the user group **group1** be evenly distributed to CPUs 0 and 1 of the NAT service board for NAT, so that these users can access the Internet.

**Figure 1** Distributed NAT load balancing![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 on the BRAS in this example represents GE 0/2/0.


  
![](images/fig_dc_ne_cfg_nat_0013.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a NAT load balancing instance.
2. Configure a CGN global static address pool.
3. Bind the NAT instance to the global address pool.
4. Configure NAT user information and RADIUS authentication on the BRAS.
5. Configure a NAT traffic diversion policy.
6. Configure a NAT traffic conversion policy.
7. Configure a user-side interface.

#### Data Preparation

To complete the configuration, you need the following data:

* NAT load balancing instance
* Name and ID of the NAT address pool and name of the global static address pool to be bound
* User group name, ACL number, and UCL number
* Information about the NAT traffic diversion policy


#### Procedure

1. Create a NAT load balancing instance.
   
   1. Set the maximum number of sessions that can be created on the CPU of the NAT service board to 6M.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname BRAS
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~BRAS] vsm on-board-mode disable
      ```
      ```
      [*BRAS] commit
      ```
      ```
      [~BRAS] license
      ```
      ```
      [~BRAS-license] active nat session-table size 6 slot 1 
      ```
      ```
      [~BRAS-license] active nat session-table size 6 slot 2 
      ```
      ```
      [~BRAS-license] active nat bandwidth-enhance 40 slot 1
      ```
      ```
      [~BRAS-license] active nat bandwidth-enhance 40 slot 2
      ```
      ```
      [~BRAS-license] quit
      ```
   2. Create a service-instance group named **groupa** and bind it to service-location groups **1** and **2**.
      
      ```
      [~BRAS] service-location 1
      ```
      ```
      [*BRAS-service-location-1] location slot 1 
      ```
      ```
      [*BRAS-service-location-1] commit
      ```
      ```
      [~BRAS-service-location-1] quit
      ```
      ```
      [~BRAS] service-location 2
      ```
      ```
      [*BRAS-service-location-2] location slot 2 
      ```
      ```
      [*BRAS-service-location-2] commit
      ```
      ```
      [~BRAS-service-location-2] quit
      ```
      ```
      [~BRAS] service-instance-group groupa
      ```
      ```
      [*BRAS-service-instance-group-groupa] service-location 1
      ```
      ```
      [*BRAS-service-instance-group-groupa] service-location 2
      ```
      ```
      [*BRAS-service-instance-group-groupa] commit
      ```
      ```
      [~BRAS-service-instance-group-groupa] quit
      ```
   3. Create a NAT instance named **cpe1** and bind it to the service-instance group **groupa**.
      
      ```
      [~BRAS] nat instance cpe1 id 11
      ```
      ```
      [*BRAS-nat-instance-cpe1] service-instance-group groupa
      ```
      ```
      [*BRAS-nat-instance-cpe1] commit
      ```
      ```
      [~BRAS-nat-instance-cpe1] quit
      ```
2. Configure a CGN global static address pool in PAT mode.
   
   # Create an address segment 11.11.11.1/24 in the view of the global static address pool **pool1**.
   
   ```
   [~BRAS] nat ip-pool pool1
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] section 0 11.11.11.1 mask 24
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] nat-instance subnet length initial 25 extend 27
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] nat-instance ip used-threshold upper-limit 60 lower-limit 40
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] nat alarm ip threshold 60
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] commit
   ```
   ```
   [~BRAS-nat-ip-pool-pool1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) When users are online, if you want to change the address segment of a global address pool or the length of an assigned address segment, run the **section lock** command first. For example:
   ```
   [~BRAS] nat ip-pool pool1
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] section 0 11.11.11.1 mask 24
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] section 0 lock
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] commit
   ```
   ```
   [~BRAS-nat-ip-pool-pool1] reset nat user nat-ip-pool pool1 section 0
   ```
   ```
   [~BRAS-nat-ip-pool-pool1] undo section 0
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] commit
   ```
   ```
   [~BRAS-nat-ip-pool-pool1] nat-instance subnet initial 24 extend 24
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] commit
   ```
   ```
   [~BRAS-nat-ip-pool-pool1] section 0 1.2.3.4 mask 24
   ```
   ```
   [*BRAS-nat-ip-pool-pool1] commit
   ```
   ```
   [~BRAS-nat-ip-pool-pool1] quit
   ```
3. Bind a dynamic address pool in the NAT instance to the global static address pool.
   
   # In the view of the NAT instance **cpe1**, configure a dynamic address pool named **group1** and bind it to the global static address pool **pool1**.
   
   ```
   [~BRAS] nat instance cpe1
   ```
   ```
   [~BRAS-nat-instance-cpe1] nat address-group group1 group-id 1 bind-ip-pool pool1
   ```
   ```
   [*BRAS-nat-instance-cpe1] commit
   ```
   ```
   [~BRAS-nat-instance-cpe1] quit
   ```
4. Configure NAT user information.
   
   1. Configure the BRAS service on the device so that users can go online. For details, see [AAA and User Management Configuration (Access Users)](dc_ne_aaa_cfg_0035.html) in *HUAWEI NE40E Configuration Guide-User Access*.
      
      ```
      [~BRAS] ip pool baspool1 bas local
      ```
      ```
      [~BRAS-ip-pool-baspool1] gateway 10.110.10.101 255.255.255.0
      ```
      ```
      [~BRAS-ip-pool-baspool1] section 1 10.110.10.1 10.110.10.100
      ```
      ```
      [*BRAS-ip-pool-baspool1] dns-server 192.168.7.252
      ```
      ```
      [*BRAS-ip-pool-baspool1] commit
      ```
      ```
      [~BRAS-ip-pool-baspool1] quit
      ```
      ```
      [~BRAS] radius-server group rd1
      ```
      ```
      [*BRAS-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
      ```
      ```
      [*BRAS-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
      ```
      ```
      [*BRAS-radius-rd1] radius-server shared-key huawei
      ```
      ```
      [*BRAS-radius-rd1] commit
      ```
      ```
      [~BRAS-radius-rd1] radius-server type plus11
      ```
      ```
      [~BRAS-radius-rd1] radius-server traffic-unit kbyte
      ```
      ```
      [~BRAS-radius-rd1] quit
      ```
      ```
      [~BRAS-aaa] aaa
      ```
      ```
      [~BRAS-aaa] authentication-scheme auth1
      ```
      ```
      [*BRAS-aaa-authen-auth1] authentication-mode radius
      ```
      ```
      [*BRAS-aaa-authen-auth1] commit
      ```
      ```
      [~BRAS-aaa-authen-auth1] quit
      ```
      ```
      [~BRAS-aaa] accounting-scheme acct1
      ```
      ```
      [*BRAS-aaa-accounting-acct1] accounting-mode radius
      ```
      ```
      [*BRAS-aaa-accounting-acct1] commit
      ```
      ```
      [~BRAS-aaa-accounting-acct1] quit
      ```
      ```
      [~BRAS-aaa] domain isp1
      ```
      ```
      [*BRAS-aaa-domain-isp1] authentication-scheme auth1
      ```
      ```
      [*BRAS-aaa-domain-isp1] accounting-scheme acct1
      ```
      ```
      [*BRAS-aaa-domain-isp1] radius-server group rd1
      ```
      ```
      [*BRAS-aaa-domain-isp1] commit
      ```
      ```
      [~BRAS-aaa-domain-isp1] ip-pool baspool1
      ```
      ```
      [*BRAS-aaa-domain-isp1] commit
      ```
      ```
      [~BRAS-aaa-domain-isp1] quit
      ```
   2. Create a user group named **group1**.
      
      ```
      [~BRAS] user-group group1
      ```
   3. Specify the domain to which the users belong.
      
      ```
      [~BRAS] aaa
      ```
      ```
      [~BRAS-aaa] domain isp1
      ```
      ```
      [*BRAS-aaa-domain-isp1] user-group group1 bind nat instance cpe1
      ```
      ```
      [*BRAS-aaa-domain-isp1] commit
      ```
      ```
      [~BRAS-aaa-domain-isp1] quit
      ```
      ```
      [~BRAS-aaa] quit
      ```
5. Configure a NAT traffic diversion policy.
   
   1. Configure an ACL numbered **6001** and set an ACL rule to match the traffic from the user group **group1** so that the traffic can be diverted to the NAT service board.
      
      ```
      [~BRAS] acl 6001
      ```
      ```
      [*BRAS-acl-ucl-6001] rule 1 permit ip source user-group group1
      ```
      ```
      [*BRAS-acl-ucl-6001] commit
      ```
      ```
      [~BRAS-acl-ucl-6001] quit
      ```
   2. Configure a traffic classifier.
      
      ```
      [~BRAS] traffic classifier c1
      ```
      ```
      [*BRAS-classifier-c1] if-match acl 6001
      ```
      ```
      [*BRAS-classifier-c1] commit
      ```
      ```
      [~BRAS-classifier-c1] quit
      ```
   3. Configure a traffic behavior named **b1**, which binds traffic to the NAT instance named **cpe1**.
      
      ```
      [~BRAS] traffic behavior b1
      ```
      ```
      [*BRAS-behavior-b1] nat bind instance cpe1
      ```
      ```
      [*BRAS-behavior-b1] commit
      ```
      ```
      [~BRAS-behavior-b1] quit
      ```
   4. Define a NAT policy to associate the ACL rule with the traffic behavior.
      
      ```
      [~BRAS] traffic policy p1
      ```
      ```
      [*BRAS-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*BRAS-trafficpolicy-p1] commit
      ```
      ```
      [~BRAS-trafficpolicy-p1] quit
      ```
   5. Apply the NAT traffic diversion policy in the system view.
      
      ```
      [~BRAS] traffic-policy p1 inbound
      ```
      ```
      [*BRAS] commit
      ```
6. Configure a NAT traffic conversion policy.
   
   1. Configure an ACL numbered **3001** and set an ACL rule to match users' private addresses for NAT.
      ```
      [~BRAS] acl 3001
      ```
      ```
      [*BRAS-acl4-advance-3001] rule 10 permit ip source 10.110.10.0 0.0.0.255
      ```
      ```
      [*BRAS-acl4-advance-3001] commit
      ```
      ```
      [~BRAS-acl4-advance-3001] quit
      ```
   2. Configure a NAT traffic conversion policy.
      ```
      [~BRAS] nat instance cpe1
      ```
      ```
      [~BRAS-nat-instance-cpe1] nat outbound 3001 address-group group1
      ```
      ```
      [*BRAS-nat-instance-cpe1] commit
      ```
      ```
      [~BRAS-nat-instance-cpe1] quit
      ```
7. Configure a user-side interface.
   ```
   [~BRAS] interface Virtual-Template 1
   ```
   ```
   [*BRAS-Virtual-Template1] ppp authentication-mode auto
   ```
   ```
   [*BRAS-Virtual-Template1] commit
   ```
   ```
   [~BRAS-Virtual-Template1] quit
   ```
   ```
   [~BRAS] interface GigabitEthernet 0/2/0.1
   ```
   ```
   [*BRAS-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0.1] user-vlan 1
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0.1-vlan-1-1] quit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0.1] pppoe-server bind Virtual-Template 1
   ```
   ```
   [*BRAS-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0.1] bas
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0.1-bas] access-type layer2-subscriber default-domain authentication isp1
   ```
   ```
   [*BRAS-GigabitEthernet0/2/0.1-bas] authentication-method ppp
   ```
   ```
   [*BRAS-GigabitEthernet0/2/0.1-bas] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0.1-bas] quit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0.1] quit
   ```
8. Verify the configuration.
   
   # Display detailed user information on CPU 0 of the service board in slot 1.
   
   ```
   [~BRAS] display nat user-information slot 1  verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...              
   Slot: 1                                                                 
   Total number:  1.                                                           
     ---------------------------------------------------------------  
     User Type                             :  NAT444                                
     CPE IP                                :  10.110.10.100                           
     User ID                               :  2                                     
     VPN Instance                          :  -                                     
     Address Group                         :  group1                                     
     NoPAT Address Group                   :  - 
     NAT Instance                          :  cpe1                                  
     Public IP                             :  11.11.11.1                           
     Start Port                            :  1152                                  
     Port Range                            :  0                                    
     Port Total                            :  5                                    
     Extend Port Alloc Times               :  0                                     
     Extend Port Alloc Number              :  0                                     
     First/Second/Third Extend Port Start  :  0/0/0                                 
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512                  
     Total/TCP/UDP/ICMP Session Current    :  5/5/0/0                               
     Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512                  
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0                               
     Total/TCP/UDP/ICMP Port Limit         :  0/0/0/0                               
     Total/TCP/UDP/ICMP Port Current       :  5/5/0/0                               
     Nat ALG Enable                        :  NULL                                   
     Token/TB/TP                           :  0/0/0                                 
     Port Forwarding Flag                  :  Non Port Forwarding                   
     Port Forwarding Ports                 :  0 0 0 0 0                             
     Aging Time(s)                         :  -                                     
     Left Time(s)                          :  -                                     
     Port Limit Discard Count              :  0                                     
     Session Limit Discard Count           :  0                                     
     Fib Miss Discard Count                :  0                                     
     -->Transmit Packets                   :  15                                    
     -->Transmit Bytes                     :  660                                   
     -->Drop Packets                       :  0                                     
     <--Transmit Packets                   :  40                                    
     <--Transmit Bytes                     :  1740                                  
     <--Drop Packets                       :  0                                     
   ---------------------------------------------------------------
   ```
   
   # Display load balancing statistics of the NAT instance named **cpe1** on the service board in slot 1.
   
   ```
   [~BRAS] display nat statistics global nat-instance cpe1 slot 1
   ```
   ```
   Slot: 1                                                            
   --------------------------------------------------------------------------- 
    Session table number                           :10 
    User table number                              :1 
    Total setup sessions                           :10 
    Total teardown sessions                        :10 
   --------------------------------------------------------------------------- 
   
   Slot: 2                                                            
   --------------------------------------------------------------------------- 
    Session table number                           :10 
    User table number                              :1
    Total setup sessions                           :10
    Total teardown sessions                        :10 
   ---------------------------------------------------------------------------
   ```

#### Configuration Files

BRAS configuration file

```
# 
sysname BRAS 
#
vsm on-board-mode disable
# 
license 
 active nat session-table size 6 slot 1  
 active nat session-table size 6 slot 2  
 active nat bandwidth-enhance 40 slot 1
 active nat bandwidth-enhance 40 slot 2
#
user-group group1
#
ip pool baspool1 bas local
 gateway 10.110.10.101 255.255.255.0
 section 1 10.110.10.1 10.110.10.100
 dns-server  192.168.7.252
# 
radius-server group rd1 
 radius-server authentication 192.168.7.249 1645 weight 0 
 radius-server accounting 192.168.7.249 1646 weight 0 
 radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%# 
 radius-server type plus11 
 radius-server traffic-unit kbyte 
# 
interface Virtual-Template1 
 ppp authentication-mode auto 
# 
service-location 1       
 location slot 1  
# 
service-location 2       
 location slot 2  
#
service-instance-group groupa       
 service-location 1       
 service-location 2 
# 
nat ip-pool pool1 
 section 0 11.11.11.1 mask 24 
 nat-instance subnet length initial 25 extend 27 
 nat-instance ip used-threshold upper-limit 60 lower-limit 40 
 nat alarm ip threshold 60 
#
acl number 3001 
 rule 10 permit ip source 10.110.10.0 0.0.0.255 
#
acl number 6001 
 rule 1 permit ip source user-group group1 
#
nat instance cpe1 id 11      
 service-instance-group groupa       
 nat address-group group1 group-id 1 bind-ip-pool pool1
 nat outbound 3001 address-group group1 
# 
traffic classifier c1 operator or
 if-match acl 6001 precedence 1
#
traffic behavior b1
 nat bind instance cpe1
#
traffic policy p1 
 classifier c1 behavior b1 precedence 1
# 
traffic-policy p1 inbound 
# 
aaa 
 authentication-scheme auth1 
  authentication-mode RADIUS 
# 
 accounting-scheme acct1 
  accounting-mode RADIUS 
# 
 domain isp1 
  authentication-scheme auth1 
  accounting-scheme acct1 
  radius-server group rd1 
  ip-pool baspool1 
  user-group group1 bind nat instance cpe1 
# 
interface GigabitEthernet0/2/0.1 
 user-vlan 1 
 pppoe-server bind Virtual-Template 1 
 bas 
  access-type layer2-subscriber default-domain authentication isp1 
  authentication-method ppp 
#
return

```