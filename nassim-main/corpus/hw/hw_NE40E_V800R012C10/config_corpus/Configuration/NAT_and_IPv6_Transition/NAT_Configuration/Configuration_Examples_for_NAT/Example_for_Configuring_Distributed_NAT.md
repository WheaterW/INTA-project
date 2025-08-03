Example for Configuring Distributed NAT
=======================================

This section provides an example for configuring the distributed NAT function to implement multiple-to-multiple conversions between private addresses of home users and external public addresses, so that users can access the Internet after NAT. You can view the networking diagram to understand the configuration procedures. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

As shown in [Figure 1](#EN-US_TASK_0000001140094137__en-us_task_0172374588_fig_dc_ne_cfg_nat_0012), home users access the Internet through the BRAS using PPPoE, IPoE, web authentication, or other ways. As well as implementing user authentication, authorization, and accounting, the BRAS also provides the NAT service to translate home users' private IP addresses into public ones.

IP addresses of interfaces are shown in [Figure 1](#EN-US_TASK_0000001140094137__en-us_task_0172374588_fig_dc_ne_cfg_nat_0012). The configuration requirements are as follows:

* Household users of user group 1 can access the Internet.
* Household users of user group 2 cannot access the Internet.

**Figure 1** Network diagram of basic NAT applications![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/0.1 and GE 0/2/0.2, respectively.


  
![](images/fig_dc_ne_cfg_nat_0012.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure NAT user information and RADIUS authentication on the BRAS.
3. Configure a NAT traffic diversion policy.
4. Configure a NAT conversion policy.
5. Configure user-side interfaces.
6. Advertise UNRs to the dynamic routing protocol.

#### Data Preparation

* Name of a NAT instance
* NAT address pool's number and start and end IP addresses
* User group name
* ACL number and UCL number
* Information about the NAT traffic diversion policy

#### Procedure

1. Set the dedicated NAT working mode.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS_NAT
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS_NAT] vsm on-board-mode disable
   ```
   ```
   [*BRAS_NAT] commit
   ```
2. Set the maximum number of sessions that can be created on the service board in slot 1 to 6M.
   
   
   ```
   [~BRAS_NAT] license
   ```
   ```
   [~BRAS_NAT-license] active nat session-table size 6 slot 1
   ```
   ```
   [*BRAS_NAT-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS_NAT-license] commit
   ```
   ```
   [~BRAS_NAT-license] quit
   ```
3. Create a NAT instance named **nat1** with ID 1 and bind the NAT instance to the service board.
   
   
   ```
   [~BRAS_NAT] service-location 1
   ```
   ```
   [*BRAS_NAT-service-location-1] location slot 1
   ```
   ```
   [*BRAS_NAT-service-location-1] commit
   ```
   ```
   [~BRAS_NAT-service-location-1] quit
   ```
   ```
   [~BRAS_NAT] service-instance-group group1
   ```
   ```
   [*BRAS_NAT-service-instance-group-group1] service-location 1
   ```
   ```
   [*BRAS_NAT-service-instance-group-group1] commit
   ```
   ```
   [~BRAS_NAT-service-instance-group-group1] quit
   ```
   ```
   [~BRAS_NAT] nat instance nat1 id 1
   ```
   ```
   [*BRAS_NAT-nat-instance-nat1] service-instance-group group1
   ```
   ```
   [*BRAS_NAT-nat-instance-nat1] commit
   ```
   ```
   [~BRAS_NAT-nat-instance-nat1] quit
   ```
4. Configure a NAT address pool and specify a range of IP addresses of 11.11.11.101 through 11.11.11.105 in the pool.
   
   
   ```
   [~BRAS_NAT] nat instance nat1
   ```
   ```
   [~BRAS_NAT-nat-instance-nat1] nat address-group address-group1 group-id 1
   ```
   ```
   [*BRAS_NAT-nat-instance-nat1-nat-address-group-address-group1] section 1 11.11.11.101 11.11.11.105
   ```
   ```
   [*BRAS_NAT-nat-instance-nat1-nat-address-group-address-group1] commit
   ```
   ```
   [~BRAS_NAT-nat-instance-nat1-nat-address-group-address-group1] quit
   ```
   ```
   [~BRAS_NAT-nat-instance-nat1] quit
   ```
5. Configure NAT user information.
   1. Configure address pools.
      
      
      ```
      [~BRAS_NAT] ip pool pool1 bas local
      ```
      ```
      [*BRAS_NAT-ip-pool-pool1] gateway 10.110.10.101 255.255.255.0
      ```
      ```
      [*BRAS_NAT-ip-pool-pool1] commit
      ```
      ```
      [~BRAS_NAT-ip-pool-pool1] section 1 10.110.10.1 10.110.10.100
      ```
      ```
      [~BRAS_NAT-ip-pool-pool1] dns-server 192.168.7.252
      ```
      ```
      [*BRAS_NAT-ip-pool-pool1] commit
      ```
      ```
      [~BRAS_NAT-ip-pool-pool1] quit
      ```
      ```
      [~BRAS_NAT] ip pool pool2 bas local
      ```
      ```
      [*BRAS_NAT-ip-pool-pool2] gateway 10.110.12.101 255.255.255.0
      ```
      ```
      [*BRAS_NAT-ip-pool-pool2] commit
      ```
      ```
      [~BRAS_NAT-ip-pool-pool2] section 2 10.110.12.1 10.110.12.100
      ```
      ```
      [~BRAS_NAT-ip-pool-pool2] dns-server 192.168.7.252
      ```
      ```
      [*BRAS_NAT-ip-pool-pool2] commit
      ```
      ```
      [~BRAS_NAT-ip-pool-pool2] quit
      ```
   2. Configure a RADIUS server.
      
      
      ```
      [~BRAS_NAT] radius-server group rd1
      ```
      ```
      [*BRAS_NAT-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
      ```
      ```
      [*BRAS_NAT-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
      ```
      ```
      [*BRAS_NAT-radius-rd1] radius-server shared-key YsHsjx_202206
      ```
      ```
      [*BRAS_NAT-radius-rd1] commit
      ```
      ```
      [~BRAS_NAT-radius-rd1] radius-server type plus11
      ```
      ```
      [~BRAS_NAT-radius-rd1] radius-server traffic-unit kbyte
      ```
      ```
      [~BRAS_NAT-radius-rd1] quit
      ```
   3. Configure authentication and accounting schemes.
      
      
      ```
      [~BRAS_NAT] aaa
      ```
      ```
      [~BRAS_NAT-aaa] authentication-scheme auth1
      ```
      ```
      [*BRAS_NAT-aaa-authen-auth1] authentication-mode radius
      ```
      ```
      [*BRAS_NAT-aaa-authen-auth1] commit
      ```
      ```
      [~BRAS_NAT-aaa-authen-auth1] quit
      ```
      ```
      [~BRAS_NAT-aaa] accounting-scheme acct1
      ```
      ```
      [*BRAS_NAT-aaa-accounting-acct1] accounting-mode radius
      ```
      ```
      [~BRAS_NAT-aaa-accounting-acct1] commit
      ```
      ```
      [~BRAS_NAT-aaa-accounting-acct1] quit
      ```
      ```
      [~BRAS_NAT-aaa] domain isp1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] authentication-scheme auth1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] accounting-scheme acct1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] radius-server group rd1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] commit
      ```
      ```
      [~BRAS_NAT-aaa-domain-isp1] ip-pool pool1
      ```
      ```
      [~BRAS_NAT-aaa-domain-isp1] quit
      ```
      ```
      [~BRAS_NAT-aaa] domain isp2
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp2] authentication-scheme auth1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp2] accounting-scheme acct1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp2] radius-server group rd1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp2] commit
      ```
      ```
      [~BRAS_NAT-aaa-domain-isp2] ip-pool pool2
      ```
      ```
      [~BRAS_NAT-aaa-domain-isp2] quit
      ```
      ```
      [~BRAS_NAT-aaa] quit
      ```
   4. Configure user groups named **group1** and **group2**.
      
      
      ```
      [~BRAS_NAT] user-group group1
      ```
      ```
      [*BRAS_NAT] user-group group2
      ```
      ```
      [*BRAS_NAT] commit
      ```
   5. Specify the domains to which the users belong.
      
      
      ```
      [~BRAS_NAT] aaa
      ```
      ```
      [~BRAS_NAT-aaa] domain isp1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] user-group group1 bind nat instance nat1
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp1] commit
      ```
      ```
      [~BRAS_NAT-aaa-domain-isp1] quit
      ```
      ```
      [~BRAS_NAT-aaa] domain isp2
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp2] user-group group2
      ```
      ```
      [*BRAS_NAT-aaa-domain-isp2] commit
      ```
      ```
      [~BRAS_NAT-aaa-domain-isp2] quit
      ```
      ```
      [~BRAS_NAT-aaa] quit
      ```
6. Configure a traffic classification rule, a NAT behavior, and a NAT traffic diversion policy. Then apply the policy.
   1. Configure ACLs numbered 6001 and 6002 and ACL rules numbered 1 and 2.
      
      
      ```
      [~BRAS_NAT] acl 6001
      ```
      ```
      [*BRAS_NAT-acl-ucl-6001] rule 1 permit ip source user-group group1
      ```
      ```
      [*BRAS_NAT-acl-ucl-6001] commit
      ```
      ```
      [~BRAS_NAT-acl-ucl-6001] quit
      ```
      ```
      [~BRAS_NAT] acl 6002
      ```
      ```
      [*BRAS_NAT-acl-ucl-6002] rule 2 permit ip source user-group group2
      ```
      ```
      [*BRAS_NAT-acl-ucl-6002] commit
      ```
      ```
      [~BRAS_NAT-acl-ucl-6002] quit
      ```
   2. Configure a traffic classifier.
      
      
      ```
      [~BRAS_NAT] traffic classifier c1
      ```
      ```
      [*BRAS_NAT-classifier-c1] if-match acl 6001
      ```
      ```
      [*BRAS_NAT-classifier-c1] commit
      ```
      ```
      [~BRAS_NAT-classifier-c1] quit
      ```
      ```
      [~BRAS_NAT] traffic classifier c2
      ```
      ```
      [*BRAS_NAT-classifier-c2] if-match acl 6002
      ```
      ```
      [*BRAS_NAT-classifier-c2] commit
      ```
      ```
      [~BRAS_NAT-classifier-c2] quit
      ```
   3. Configure two traffic behaviors: b1 and b2. The action of b1 binds traffic to the NAT instance named **nat1**, and the action of b2 is deny.
      
      
      ```
      [~BRAS_NAT] traffic behavior b1 
      ```
      ```
      [*BRAS_NAT-behavior-b1] nat bind instance nat1
      ```
      ```
      [*BRAS_NAT-behavior-b1] commit
      ```
      ```
      [~BRAS_NAT-behavior-b1] quit
      ```
      ```
      [~BRAS_NAT] traffic behavior b2
      ```
      ```
      [*BRAS_NAT-behavior-b2] deny
      ```
      ```
      [*BRAS_NAT-behavior-b2] commit
      ```
      ```
      [~BRAS_NAT-behavior-b2] quit
      ```
   4. Define a NAT policy to associate the ACL rule with the traffic behavior.
      
      
      ```
      [~BRAS_NAT] traffic policy p1
      ```
      ```
      [*BRAS_NAT-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*BRAS_NAT-trafficpolicy-p1] classifier c2 behavior b2
      ```
      ```
      [*BRAS_NAT-trafficpolicy-p1] commit
      ```
      ```
      [~BRAS_NAT-trafficpolicy-p1] quit
      ```
   5. Apply the NAT traffic diversion policy in the system view.
      
      
      ```
      [~BRAS_NAT] traffic-policy p1 inbound
      ```
      ```
      [*BRAS_NAT] commit
      ```
7. Configure a NAT conversion policy to perform NAT for user traffic.
   
   
   1. Configure an ACL numbered 3001 to match user traffic.
      ```
      [~BRAS_NAT] acl 3001
      ```
      ```
      [*BRAS_NAT-acl4-advance-3001] rule 10 permit ip source 10.110.10.0 0.0.0.255
      ```
      ```
      [*BRAS_NAT-acl4-advance-3001] commit
      ```
      ```
      [~BRAS_NAT-acl4-advance-3001] quit
      ```
   2. Configure a NAT conversion policy.
      ```
      [~BRAS_NAT] nat instance nat1 id 1
      ```
      ```
      [~BRAS_NAT-nat-instance-nat1] nat outbound 3001 address-group address-group1
      ```
      ```
      [*BRAS_NAT-nat-instance-nat1] commit
      ```
      ```
      [~BRAS_NAT-nat-instance-nat1] quit
      ```
8. Configure a user-side sub-interface.
   
   
   ```
   [~BRAS_NAT] interface Virtual-Template 1
   ```
   ```
   [*BRAS_NAT-Virtual-Template1] ppp authentication-mode auto
   ```
   ```
   [*BRAS_NAT-Virtual-Template1] commit
   ```
   ```
   [~BRAS_NAT-Virtual-Template1] quit
   ```
   
   
   ```
   [~BRAS_NAT] interface GigabitEthernet 0/2/0.1
   ```
   ```
   [*BRAS_NAT-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.1] user-vlan 1
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.1-vlan-1-1] quit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.1] pppoe-server bind Virtual-Template 1
   ```
   ```
   [*BRAS_NAT-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.1] bas
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.1-bas] access-type layer2-subscriber default-domain authentication isp1
   ```
   ```
   [*BRAS_NAT-GigabitEthernet0/2/0.1-bas] authentication-method ppp
   ```
   ```
   [*BRAS_NAT-GigabitEthernet0/2/0.1-bas] commit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.1-bas] quit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [~BRAS_NAT] interface GigabitEthernet 0/2/0.2
   ```
   ```
   [*BRAS_NAT-GigabitEthernet0/2/0.2] commit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.2] user-vlan 2
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.2-vlan-2-2] quit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.2] pppoe-server bind Virtual-Template 1
   ```
   ```
   [*BRAS_NAT-GigabitEthernet0/2/0.2] commit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.2] bas
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.2-bas] access-type layer2-subscriber default-domain authentication isp2
   ```
   ```
   [*BRAS_NAT-GigabitEthernet0/2/0.2-bas] authentication-method ppp
   ```
   ```
   [*BRAS_NAT-GigabitEthernet0/2/0.2-bas] commit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.2-bas] quit
   ```
   ```
   [~BRAS_NAT-GigabitEthernet0/2/0.2] quit
   ```
9. Configure the route of the NAT address pool as the static black-hole route and advertise it to the routing protocol. In this example, OSPF with process ID as 1 is used. (Assume that OSPF is used as an IGP to advertise routes on the enterprise's internal network.)
   
   
   ```
   [~BRAS_NAT] ip route-static 11.11.11.0 24 null 0
   ```
   ```
   [*BRAS_NAT] commit
   ```
   ```
   [~BRAS_NAT] ospf 1
   ```
   ```
   [*BRAS_NAT-ospf-1] import-route static
   ```
   ```
   [*BRAS_NAT-ospf-1] commit
   ```
   ```
   [~BRAS_NAT-ospf-1] quit
   ```
10. Verify the configuration.
    
    
    * Check NAT user information on the device.
      
      ```
      <BRAS_NAT> display nat user-information slot 1 verbose
      ```
      ```
      This operation will take a few minutes. Press 'Ctrl+C' to break ...             
      Slot: 1                                                               
      Total number:  1.                                                               
        ---------------------------------------------------------------------------   
        User Type                             :  NAT444                               
        CPE IP                                :  10.110.10.100                        
        User ID                               :  2                                    
        VPN Instance                          :  -                                    
        Address Group                         :  address-group1                                     
        NAT Instance                          :  nat1                                  
        Public IP                             :  11.11.11.101                           
        Start Port                            :  -                                 
        Port Range                            :  -                                  
        Port Total                            :  -                                  
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
        Token/TB/TP                           :  0/0/0                                
        Port Forwarding Flag                  :  Non Port Forwarding                  
        Port Forwarding Ports                 :  0 0 0 0 0                            
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
        ---------------------------------------------------------------------------  
      ```

#### Configuration Files

* BRAS configuration file
  
  ```
  #
  sysname BRAS_NAT
  #
  vsm on-board-mode disable
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
  interface GigabitEthernet2/0/0.1
   user-vlan 1
   pppoe-server bind Virtual-Template 1
   bas
    access-type layer2-subscriber default-domain authentication isp1
    authentication-method ppp
  #
  interface GigabitEthernet2/0/0.2
   user-vlan 2
   pppoe-server bind Virtual-Template 1
   bas
    access-type layer2-subscriber default-domain authentication isp2
    authentication-method ppp
  #
  ip pool pool1 bas local
   gateway 10.110.10.101 255.255.255.0
   section 1 10.110.10.1 10.110.10.100
   dns-server  192.168.7.252
  #
  ip pool pool2 bas local
   gateway 10.110.12.101 255.255.255.0
   section 2 10.110.12.1 10.110.12.100
   dns-server  192.168.7.252
  #
  license
   active nat session-table size 6 slot 1
   active nat bandwidth-enhance 40 slot 1
  #
  service-location 1
   location slot 1
  #
  service-instance-group group1
   service-location 1
  #
  nat instance nat1 id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 
    section 1 11.11.11.101 11.11.11.105
   nat outbound 3001 address-group address-group1
  #
  user-group group1
  user-group group2
  #
  acl number 3001
   rule 10 permit ip source 10.110.10.0 0.0.0.255
  #
  acl number 6001
   rule 1 permit ip source user-group group1
  #
  acl number 6002
   rule 2 permit ip source user-group group2
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
   deny
  #
  traffic policy p1
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
    ip-pool pool1
    user-group group1 bind nat instance nat1
  #
   domain isp2
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool pool2
    user-group group2
  #
  ip route-static 11.11.11.0 255.255.255.0 NULL0
  #
  ospf 1
   import-route static
  #
   return
  ```