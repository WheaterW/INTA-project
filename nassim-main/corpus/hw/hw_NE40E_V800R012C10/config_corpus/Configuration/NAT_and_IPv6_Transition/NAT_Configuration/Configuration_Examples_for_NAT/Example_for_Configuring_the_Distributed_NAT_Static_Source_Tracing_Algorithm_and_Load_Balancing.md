Example for Configuring the Distributed NAT Static Source Tracing Algorithm and Load Balancing
==============================================================================================

This section provides an example for configuring the distributed NAT static source tracing algorithm and load balancing. After the configuration is performed, IP addresses of multiple home users can be balanced to different CPUs for NAT in the multiple NAT service instances.

#### Networking Requirements

![](../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

In the distributed NAT scenario shown in [Figure 1](#EN-US_TASK_0000001590438665__en-us_task_0000001582265705_fig14191727184), home users access the Internet through the BRAS using PPPoE, IPoE, web authentication, or other ways. As well as implementing user authentication, authorization, and accounting, the BRAS also provides the NAT service to translate home users' private IP addresses into public ones. To improve network reliability, load balancing is implemented based on different CPUs. In addition, the static source tracing algorithm is used to find private IP addresses based on public IP addresses and port numbers so that home users can access the Internet. By using this algorithm, the BRAS does not need to send source tracing logs to record information about intranet users' access to the external network, thereby enhancing network security.

The configuration requirements are as follows:

* Load balancing can be implemented by configuring multiple user groups and binding each user group to a NAT instance.
* Each home user (such as PC1 and PC2 in [Figure 1](#EN-US_TASK_0000001590438665__en-us_task_0000001582265705_fig14191727184)) dials up to access the user groups bound to load balancing.
* IP addresses of multiple home users can be balanced to different CPUs for NAT in the multiple NAT service instances.

**Figure 1** Distributed NAT static source tracing and load balancing  
![](../images/en-us_image_0000001589475969.png)
![](../public_sys-resources/note_3.0-en-us.png) 

Interface1 on the BRAS in this example represents GE 0/2/0.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create NAT load balancing instances.
2. Configure the NAT static source tracing algorithm mapping.
3. Bind a dynamic NAT address pool to a global address pool.
4. Configure NAT user information and RADIUS authentication on the BRAS.
5. Configure a NAT traffic diversion policy.
6. Configure a NAT traffic conversion policy.
7. Configure a user-side interface.

#### Data Preparation

To complete the configuration, you need the following data:

* NAT instance.
* User group name and UCL number
* Information about the NAT traffic diversion policy
* IDs of the private and public address pools for the static source tracing algorithm
* Private and public address segments of the static source tracing algorithm
* Port number range and port range size of the public address pool in the static source tracing algorithm


#### Procedure

1. Create a NAT instance.
   
   1. Configure licenses.
      
      ```
      <HUAWEI>system-view
      ```
      ```
      [~HUAWEI]sysname BRAS
      ```
      ```
      [*HUAWEI]commit
      ```
      ```
      [~BRAS]vsm on-board-mode disable
      ```
      ```
      [*BRAS]commit
      ```
      ```
      [~BRAS]license
      ```
      ```
      [*BRAS-license]active nat session-table size 32 slot 1 
      ```
      ```
      [*BRAS-license]active nat session-table size 32 slot 2 
      ```
      ```
      [*BRAS-license]active nat bandwidth-enhance 40 slot 1
      ```
      ```
      [*BRAS-license]active nat bandwidth-enhance 40 slot 2
      ```
      ```
      [*BRAS-license]commit
      ```
      ```
      [~BRAS-license]quit
      ```
   2. Bind service-instance groups **group1** and **group2** to service-location groups **1** and **2**, respectively.
      
      ```
      [~BRAS]service-location 1
      ```
      ```
      [*BRAS-service-location-1]location slot 1 
      ```
      ```
      [*BRAS-service-location-1]commit
      ```
      ```
      [~BRAS-service-location-1]quit
      ```
      ```
      [~BRAS]service-location 2
      ```
      ```
      [*BRAS-service-location-2]location slot 2 
      ```
      ```
      [*BRAS-service-location-2]commit
      ```
      ```
      [~BRAS-service-location-2]quit
      ```
      ```
      [~BRAS]service-instance-group group1
      ```
      ```
      [*BRAS-service-instance-group-group1]service-location 1
      ```
      ```
      [*BRAS-service-instance-group-group1]commit
      ```
      ```
      [~BRAS-service-instance-group-group1]quit
      ```
      ```
      [~BRAS]service-instance-group group2
      ```
      ```
      [*BRAS-service-instance-group-group2]service-location 2
      ```
      ```
      [*BRAS-service-instance-group-group2]commit
      ```
      ```
      [~BRAS-service-instance-group-group2]quit
      ```
2. Configure the NAT static source tracing algorithm mapping.
   ```
   [~BRAS]nat static-mapping
   ```
   ```
   [*BRAS-nat-static-mapping]inside-pool 1
   ```
   ```
   [*BRAS-nat-static-mapping-inside-pool-1]section 1 192.168.0.10 192.168.0.110
   ```
   ```
   [*BRAS-nat-static-mapping-inside-pool-1]quit
   ```
   ```
   [*BRAS-nat-static-mapping]inside-pool 2
   ```
   ```
   [*BRAS-nat-static-mapping-inside-pool-2]section 1 192.168.0.130 192.168.0.230
   ```
   ```
   [*BRAS-nat-static-mapping-inside-pool-2]quit
   ```
   ```
   [*BRAS-nat-static-mapping]global-pool 1
   ```
   ```
   [*BRAS-nat-static-mapping-global-pool-1]section 1 10.1.1.5 10.1.1.125
   ```
   ```
   [*BRAS-nat-static-mapping-global-pool-1]quit
   ```
   ```
   [*BRAS-nat-static-mapping]global-pool 2
   ```
   ```
   [*BRAS-nat-static-mapping-global-pool-2]section 1 10.1.1.130 10.1.1.250
   ```
   ```
   [*BRAS-nat-static-mapping-global-pool-2]quit
   ```
   ```
   [*BRAS-nat-static-mapping]static-mapping 1 inside-pool 1 global-pool 1 port-range 256 1023 port-size 256
   ```
   ```
   [*BRAS-nat-static-mapping]static-mapping 2 inside-pool 2 global-pool 2 port-range 256 1023 port-size 256
   ```
   ```
   [*BRAS-nat-static-mapping]commit
   ```
   ```
   [~BRAS-nat-static-mapping]quit
   ```
3. Bind the static NAT and the service-instance groups to the NAT instances.
   
   ```
   [~BRAS]nat instance nat1 id 1
   ```
   ```
   [*BRAS-nat-instance-nat1]service-instance-group group1
   ```
   ```
   [*BRAS-nat-instance-nat1]nat bind static-mapping 1
   ```
   ```
   [*BRAS-nat-instance-nat1]commit
   ```
   ```
   [~BRAS-nat-instance-nat1]quit
   ```
   ```
   [~BRAS]nat instance nat2 id 2
   ```
   ```
   [*BRAS-nat-instance-nat2]service-instance-group group2
   ```
   ```
   [*BRAS-nat-instance-nat2]nat bind static-mapping 2
   ```
   ```
   [*BRAS-nat-instance-nat2]commit
   ```
   ```
   [~BRAS-nat-instance-nat2]quit
   ```
4. Configure NAT user information and RADIUS authentication on the BRAS.
   1. Configure the BRAS service on the device so that users can go online. For details, see [AAA and User Management Configuration (Access Users)](../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0035.html) in *HUAWEI NE40E Configuration Guide-User Access*.
      
      ```
      [~BRAS]ip pool baspool1 bas local
      ```
      ```
      [*BRAS-ip-pool-baspool1]gateway 192.168.0.2 255.255.255.128
      ```
      ```
      [*BRAS-ip-pool-baspool1]section 1 192.168.0.10 192.168.0.110
      ```
      ```
      [*BRAS-ip-pool-baspool1]dns-server 192.168.7.252
      ```
      ```
      [*BRAS-ip-pool-baspool1]commit
      ```
      ```
      [~BRAS-ip-pool-baspool1]quit
      ```
      ```
      [~BRAS]ip pool baspool2 bas local
      ```
      ```
      [*BRAS-ip-pool-baspool2]gateway 192.168.0.129 255.255.255.128
      ```
      ```
      [*BRAS-ip-pool-baspool2]section 1 192.168.0.130 192.168.0.230
      ```
      ```
      [*BRAS-ip-pool-baspool2]dns-server 192.168.7.252
      ```
      ```
      [*BRAS-ip-pool-baspool2]commit
      ```
      ```
      [~BRAS-ip-pool-baspool2]quit
      ```
      ```
      [~BRAS]radius-server group rd1
      ```
      ```
      [*BRAS-radius-rd1]radius-server authentication 192.168.7.249 1645 weight 0
      ```
      ```
      [*BRAS-radius-rd1]radius-server accounting 192.168.7.249 1646 weight 0
      ```
      ```
      [*BRAS-radius-rd1]radius-server shared-key YsHsjx_202206
      ```
      ```
      [*BRAS-radius-rd1]commit
      ```
      ```
      [~BRAS-radius-rd1]radius-server type plus11
      ```
      ```
      [~BRAS-radius-rd1]radius-server traffic-unit kbyte
      ```
      ```
      [~BRAS-radius-rd1]quit
      ```
      ```
      [~BRAS-aaa]aaa
      ```
      ```
      [~BRAS-aaa]authentication-scheme auth1
      ```
      ```
      [*BRAS-aaa-authen-auth1]authentication-mode radius
      ```
      ```
      [*BRAS-aaa-authen-auth1]commit
      ```
      ```
      [~BRAS-aaa-authen-auth1]quit
      ```
      ```
      [~BRAS-aaa]accounting-scheme acct1
      ```
      ```
      [*BRAS-aaa-accounting-acct1]accounting-mode radius
      ```
      ```
      [*BRAS-aaa-accounting-acct1]commit
      ```
      ```
      [~BRAS-aaa-accounting-acct1]quit
      ```
      ```
      [~BRAS-aaa]domain isp1
      ```
      ```
      [*BRAS-aaa-domain-isp1]authentication-scheme auth1
      ```
      ```
      [*BRAS-aaa-domain-isp1]accounting-scheme acct1
      ```
      ```
      [*BRAS-aaa-domain-isp1]radius-server group rd1
      ```
      ```
      [*BRAS-aaa-domain-isp1]commit
      ```
      ```
      [~BRAS-aaa-domain-isp1]quit
      ```
   2. Configure user groups 1 and 2.
      
      ```
      [~BRAS]user-group group1
      ```
      ```
      [*BRAS]user-group group2
      ```
      ```
      [*BRAS]commit
      ```
   3. Specify the domain to which the users belong.
      
      ```
      [~BRAS]aaa
      ```
      ```
      [~BRAS-aaa]domain isp1
      ```
      ```
      [*BRAS-aaa]commit
      ```
      ```
      [~BRAS-aaa-domain-isp1]ip-pool baspool1
      ```
      ```
      [~BRAS-aaa-domain-isp1]ip-pool baspool2
      ```
      ```
      [~BRAS-aaa-domain-isp1]user-group group2 bind nat instance nat2 ip-pool baspool2
      ```
      ```
      [*BRAS-aaa-domain-isp1]user-group group1 bind nat instance nat1 ip-pool baspool1 
      ```
      ```
      [*BRAS-aaa-domain-isp1]commit
      ```
      ```
      [~BRAS-aaa-domain-isp1]quit
      ```
      ```
      [~BRAS-aaa]quit
      ```
5. Configure a NAT traffic diversion policy.
   
   1. Configure an ACL numbered **6001** and set an ACL rule to match the traffic from the user group **group1** so that the traffic can be diverted to the NAT service board.
      
      ```
      [~BRAS]acl 6001
      ```
      ```
      [*BRAS-acl-ucl-6001]rule 1 permit ip source user-group group1
      ```
      ```
      [*BRAS-acl-ucl-6001]commit
      ```
      ```
      [~BRAS-acl-ucl-6001]quit
      ```
   2. Configure an ACL numbered **6002** and set an ACL rule to match the traffic from the user group **group2** so that the traffic can be diverted to the NAT service board.
      
      ```
      [~BRAS]acl 6002
      ```
      ```
      [*BRAS-acl-ucl-6002]rule 2 permit ip source user-group group2
      ```
      ```
      [*BRAS-acl-ucl-6002]commit
      ```
      ```
      [~BRAS-acl-ucl-6002]quit
      ```
   3. Configure a traffic classifier for **group1**.
      
      ```
      [~BRAS]traffic classifier c1 operator or
      ```
      ```
      [*BRAS-classifier-c1]if-match acl 6001 precedence 1
      ```
      ```
      [*BRAS-classifier-c1]commit
      ```
      ```
      [~BRAS-classifier-c1]quit
      ```
   4. Configure a traffic classifier for **group2**.
      
      ```
      [~BRAS]traffic classifier c2 operator or
      ```
      ```
      [*BRAS-classifier-c2]if-match acl 6002 precedence 1
      ```
      ```
      [*BRAS-classifier-c2]commit
      ```
      ```
      [~BRAS-classifier-c2]quit
      ```
   5. Configure a traffic behavior named **b1**, which binds traffic to the NAT instance.
      
      ```
      [~BRAS]traffic behavior b1
      ```
      ```
      [*BRAS-behavior-b1]nat bind instance nat1
      ```
      ```
      [*BRAS-behavior-b1]commit
      ```
      ```
      [~BRAS-behavior-b1]quit
      ```
   6. Configure a traffic behavior named **b2**, which binds traffic to the NAT instance.
      
      ```
      [~BRAS]traffic behavior b2
      ```
      ```
      [*BRAS-behavior-b2]nat bind instance nat2
      ```
      ```
      [*BRAS-behavior-b2]commit
      ```
      ```
      [~BRAS-behavior-b2]quit
      ```
   7. Configure a NAT policy for **group1**, and associate the ACL rule with the traffic behavior.
      
      ```
      [~BRAS]traffic policy p1
      ```
      ```
      [*BRAS-trafficpolicy-p1]classifier c1 behavior b1 precedence 1
      ```
      ```
      [*BRAS-trafficpolicy-p1]commit
      ```
      ```
      [~BRAS-trafficpolicy-p1]quit
      ```
   8. Configure a NAT policy for **group2**, and associate the ACL rule with the traffic behavior.
      
      ```
      [~BRAS]traffic policy p1
      ```
      ```
      [*BRAS-trafficpolicy-p1]classifier c2 behavior b2 precedence 2
      ```
      ```
      [*BRAS-trafficpolicy-p1]commit
      ```
      ```
      [~BRAS-trafficpolicy-p1]quit
      ```
   9. Apply the NAT traffic diversion policy in the system view.
      
      ```
      [~BRAS]traffic-policy p1 inbound
      ```
      ```
      [*BRAS]commit
      ```
6. Configure a user-side interface.
   ```
   [~BRAS]interface GigabitEthernet 0/2/0
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0]bas
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0-bas]access-type layer2-subscriber default-domain authentication isp1
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0-bas]authentication-method bind 
   ```
   ```
   [*BRAS-GigabitEthernet0/2/0-bas]commit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0-bas]quit
   ```
   ```
   [~BRAS-GigabitEthernet0/2/0]quit
   ```
7. Verify the configuration.
   
   # Display detailed information about users of CPU 0 on the service board in slot 1.
   
   ```
   [~BRAS]display nat user-information slot 1  verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...              
   Slot: 1                                                                 
   Total number:  1.                                                           
     ---------------------------------------------------------------  
     User Type                             :  NAT444
     CPE IP                                :  192.168.0.110
     User ID                               :  0
     VPN Instance                          :  -
     Address Group                         :  -
     NoPAT Address Group                   :  -
     NAT Instance                          :  nat1
     Public IP                             :  10.1.1.38
     NoPAT Public IP                       :  -
     Start Port                            :  512
     Port Range                            :  256
     Port Total                            :  256
     Radius Specific PCP Port              :  NO
     PCP authentication                    :  True
     Extend Port Alloc Times               :  0
     Extend Port Alloc Number              :  0
     First/Second/Third Extend Port Start  :  0/0/0
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512
     Total/TCP/UDP/ICMP Session Current    :  0/0/0/0
     Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0
     Total/TCP/UDP/ICMP Port Limit         :  0/0/0/0
     Total/TCP/UDP/ICMP Port Current       :  0/0/0/0
     Nat ALG Enable                        :  NULL
     Port Reuse                            :  False
     Token/TB/TP                           :  0/0/0
     Port Forwarding Flag                  :  Non Port Forwarding
     Port Forwarding Ports                 :  0 0 0 0 0
     Create Time                           :  2023-04-27 15:44:01
     Aging Time(s)                         :  -
     Left Time(s)                          :  -
     Port Limit Discard Count              :  0
     Session Limit Discard Count           :  0
     Fib Miss Discard Count                :  0
     -->Transmit Packets                   :  0
     -->Transmit Bytes                     :  0
     -->Drop Packets                       :  0
     <--Transmit Packets                   :  0
     <--Transmit Bytes                     :  0
     <--Drop Packets                       :  0
     Fast-forwarding Statistics ID         :  -
     -->Hit Fast-fwd session Packets       :  -
     -->NP transmit to multi-core Packets  :  -
     <--Hit Fast-fwd session Packets       :  -
     <--NP transmit to multi-core Packets  :  -
     ---------------------------------------------------------------------------
   ```
   # Display detailed information about users of CPU 1 on the service board in slot 2.
   ```
   [~BRAS]display nat user-information slot 2  verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...              
   Slot: 2                                                                 
   Total number:  1.                                                           
     ---------------------------------------------------------------  
     User Type                             :  NAT444
     CPE IP                                :  192.168.0.221
     User ID                               :  2052
     VPN Instance                          :  -
     Address Group                         :  -
     NoPAT Address Group                   :  -
     NAT Instance                          :  nat2
     Public IP                             :  10.1.1.160
     NoPAT Public IP                       :  -
     Start Port                            :  512
     Port Range                            :  256
     Port Total                            :  256
     Radius Specific PCP Port              :  NO
     PCP authentication                    :  True
     Extend Port Alloc Times               :  0
     Extend Port Alloc Number              :  0
     First/Second/Third Extend Port Start  :  0/0/0
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512
     Total/TCP/UDP/ICMP Session Current    :  0/0/0/0
     Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0
     Total/TCP/UDP/ICMP Port Limit         :  0/0/0/0
     Total/TCP/UDP/ICMP Port Current       :  0/0/0/0
     Nat ALG Enable                        :  NULL
     Port Reuse                            :  False
     Token/TB/TP                           :  0/0/0
     Port Forwarding Flag                  :  Non Port Forwarding
     Port Forwarding Ports                 :  0 0 0 0 0
     Create Time                           :  2023-04-27 15:54:45
     Aging Time(s)                         :  -
     Left Time(s)                          :  -
     Port Limit Discard Count              :  0
     Session Limit Discard Count           :  0
     Fib Miss Discard Count                :  0
     -->Transmit Packets                   :  0
     -->Transmit Bytes                     :  0
     -->Drop Packets                       :  0
     <--Transmit Packets                   :  0
     <--Transmit Bytes                     :  0
     <--Drop Packets                       :  0
     Fast-forwarding Statistics ID         :  -
     -->Hit Fast-fwd session Packets       :  -
     -->NP transmit to multi-core Packets  :  -
     <--Hit Fast-fwd session Packets       :  -
     <--NP transmit to multi-core Packets  :  -
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
 active nat session-table size 32 slot 1  
 active nat session-table size 32 slot 2  
 active nat bandwidth-enhance 40 slot 1
 active nat bandwidth-enhance 40 slot 2
#
user-group group1
#
user-group group2
#
ip pool baspool1 bas local
 gateway 192.168.0.2 255.255.255.128
 section 1 192.168.0.10 192.168.0.110
 dns-server  192.168.7.252
# 
ip pool baspool2 bas local
 gateway 192.168.0.129 255.255.255.128
 section 1 192.168.0.130 192.168.0.230
 dns-server 192.168.7.252
# 
radius-server group rd1 
 radius-server authentication 192.168.7.249 1645 weight 0 
 radius-server accounting 192.168.7.249 1646 weight 0 
 radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%# 
 radius-server type plus11 
 radius-server traffic-unit kbyte 
#
nat static-mapping
 inside-pool 1
  section 1 192.168.0.10 192.168.0.110
 inside-pool 2
  section 1 192.168.0.130 192.168.0.230
 global-pool 1
  section 1 10.1.1.5 10.1.1.125
 global-pool 2
  section 1 10.1.1.130 10.1.1.250
 static-mapping 1 inside-pool 1 global-pool 1 port-range 256 1023 port-size 256
 static-mapping 2 inside-pool 2 global-pool 2 port-range 256 1023 port-size 256
#
service-location 1       
 location slot 1  
# 
service-location 2       
 location slot 2  
#
service-instance-group group1
 service-location 1
#
service-instance-group group2
 service-location 2 
#
acl number 6001 
 rule 1 permit ip source user-group group1 
#
acl number 6002 
 rule 2 permit ip source user-group group2
#
nat instance nat1 id 1   
 service-instance-group group1 
 nat bind static-mapping 1
# 
nat instance nat2 id 2   
 service-instance-group group2 
 nat bind static-mapping 2
# 
traffic classifier c1 operator or
 if-match acl 6001 precedence 1
#
traffic classifier c2 operator or
 if-match acl 6002 precedence 1
#
traffic behavior b1
 nat bind instance nat1
#
traffic behavior b2
 nat bind instance nat2
#
traffic policy p1 
 share-mode
 classifier c1 behavior b1 precedence 1
 classifier c2 behavior b2 precedence 2
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
  ip-pool baspool2
  user-group group1 bind nat instance nat1 ip-pool baspool1
  user-group group2 bind nat instance nat2 ip-pool baspool2
# 
interface GigabitEthernet0/2/0
 undo shutdown
 bas 
  access-type layer2-subscriber default-domain authentication isp1 
  authentication-method bind 
#
return
```