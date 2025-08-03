Example for Configuring Centralized NAT Providing Backup for Distributed NAT
============================================================================

This section provides an example for configuring centralized NAT providing backup for distributed NAT.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

As shown in [Figure 1](#EN-US_TASK_0000001194921709__en-us_task_0172374591_fig_dc_ne_cfg_nat_0012), the BRAS is equipped with a dedicated board. The NAT device is attached to the CR to back up data for the BRAS. In normal cases, the BRAS implements NAT for user traffic. If the BRAS becomes faulty, user traffic is switched to the NAT device for NAT implementation.

It is required that computers with the IP addresses on the network segment 10.10.10.0/24 can access the Internet.

**Figure 1** Centralized NAT providing backup for distributed NAT![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1, interface 2, and interface 3 in this example represent GE 0/2/1, GE 0/2/2, and GE 0/2/0, respectively.


  
![](images/fig_dc_ne_nat_cfg_0016.png)

**Table 1** Interfaces and IP addresses
| Device Name | Interface Name | IP Address and Mask |
| --- | --- | --- |
| BRAS | GE 0/2/0.1 | â |
| GE 0/2/1 | 192.168.10.1/24 |
| CR | GE 0/2/2 | 192.168.10.2/24 |
| GE 0/2/1 | 192.168.11.1/24 |
| NAT device | GE 0/2/2 | 192.168.11.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. For the distributed NAT device, the configuration roadmap for centralize NAT providing backup for distributed NAT is as follows:
   1. Configure basic NAT functions.
   2. Configure NAT user information and RADIUS authentication on the BRAS.
   3. Configure a NAT traffic diversion policy.
   4. Configure a NAT conversion policy.
2. For the CR, the configuration roadmap for redirecting user traffic to the NAT device is as follows:
   
   1. Configure a traffic diversion policy.
   2. Configure an inbound interface redirection policy.
3. For the centralized NAT device, the configuration roadmap for centralized NAT is as follows:
   
   1. Configure basic NAT functions.
   2. Configure a NAT traffic diversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* Service-location group index: 1
* Slot ID of the NAT's service board: 1
* Service-instance group name: group1
* NAT instance name: nat1; NAT instance index: 1
* NAT address pool name for NAT device: address-group1; NAT address pool ID: 1; IP address segment: 11.11.11.101 to 11.11.11.105
* User group name: group1
* Private network address pool name: pool1
* Domain name: isp1
* ACL name: 6001
* Traffic classifier name: c1
* Traffic behavior name: b1
* Traffic policy name: p1
* Name and IP address of each interface to which a NAT traffic diversion policy is applied


#### Procedure

1. On the BRAS, configure centralized NAT providing backup for distributed NAT.
   1. Configure an IP address for an interface.
      
      
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
      [~BRAS] interface GigabitEthernet 0/2/1
      ```
      ```
      [*BRAS-GigabitEthernet0/2/1] ip address 192.168.10.1 24
      ```
      ```
      [~BRAS-GigabitEthernet0/2/1] commit
      ```
      ```
      [~BRAS-GigabitEthernet0/2/1] quit
      ```
   2. Configure basic NAT functions.
      
      
      1. Set the maximum number of sessions that can be created on the NAT service board in slot 1 to 6M.
         
         ```
         [~BRAS] vsm on-board-mode disable
         ```
         ```
         [~BRAS] license
         ```
         ```
         [~BRAS-license] active nat session-table size 6 slot 1
         ```
         ```
         [~BRAS-license] active nat bandwidth-enhance 40 slot 1
         ```
         ```
         [~BRAS-license] quit
         ```
      2. Create a NAT instance named **nat1** and bind it to the service board.
         
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
         [~BRAS] service-instance-group group1
         ```
         ```
         [*BRAS-service-instance-group-group1] service-location 1
         ```
         ```
         [*BRAS-service-instance-group-group1] commit
         ```
         ```
         [~BRAS-service-instance-group-group1] quit
         ```
         ```
         [~BRAS] nat instance nat1 id 1
         ```
         ```
         [*BRAS-nat-instance-nat1] service-instance-group group1
         ```
         ```
         [*BRAS-nat-instance-nat1] commit
         ```
         ```
         [~BRAS-nat-instance-nat1] quit
         ```
      3. Configure a NAT address pool and specify a range of IP addresses of 11.11.11.101 through 11.11.11.105 in the pool.
         
         ```
         [~BRAS] nat instance nat1
         ```
         ```
         [~BRAS-nat-instance-nat1] nat address-group address-group1 group-id 1
         ```
         ```
         [*BRAS-nat-instance-nat1-nat-address-group-address-group1] section 1 11.11.11.101 11.11.11.105
         ```
         ```
         [*BRAS-nat-instance-nat1-nat-address-group-address-group1] commit
         ```
         ```
         [~BRAS-nat-instance-nat1-nat-address-group-address-group1] quit
         ```
         ```
         [~BRAS-nat-instance-nat1] quit
         ```
   3. Configure NAT user information.
      
      
      1. Configure the BRAS service on the device so that users can go online. For details, see [AAA and User Management Configuration (Access Users)](dc_ne_aaa_cfg_0035.html) in *HUAWEI NE40E Configuration Guide-User Access*.
         
         ```
         [~BRAS] ip pool pool1 bas local
         ```
         ```
         [~BRAS-ip-pool-pool1] gateway 10.10.10.1 255.255.255.0
         ```
         ```
         [*BRAS-ip-pool-pool1] commit
         ```
         ```
         [~BRAS-ip-pool-pool1] section 1 10.10.10.1 10.10.10.100
         ```
         ```
         [~BRAS-ip-pool-pool1] dns-server 192.168.7.252
         ```
         ```
         [*BRAS-ip-pool-pool1] commit
         ```
         ```
         [~BRAS-ip-pool-pool1] quit
         ```
         ```
         [~BRAS] radius-server group rd1
         ```
         ```
         [*BRAS-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
         ```
         ```
         [*BRAS-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
         ```
         ```
         [*BRAS-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
         ```
         ```
         [*BRAS-radius-rd1] commit
         ```
         ```
         [~BRAS-radius-rd1] quit
         ```
         ```
         [~BRAS] aaa
         ```
         ```
         [~BRAS-aaa] authentication-scheme auth1
         ```
         ```
         [*BRAS-aaa-authen-acct1] authentication-mode radius
         ```
         ```
         [*BRAS-aaa-authen-acct1] quit
         ```
         ```
         [*BRAS-aaa] accounting-scheme acct1
         ```
         ```
         [*BRAS-aaa-accounting-acct1] accounting-mode radius
         ```
         ```
         [*BRAS-aaa-accounting-acct1] quit
         ```
         ```
         [*BRAS-aaa] commit
         ```
         ```
         [*BRAS-aaa] domain isp1
         ```
         ```
         [~BRAS-aaa-domain-isp1] authentication-scheme auth1
         ```
         ```
         [*BRAS-aaa-domain-isp1] accounting-scheme acct1
         ```
         ```
         [*BRAS-aaa-domain-isp1] commit
         ```
         ```
         [~BRAS-aaa-domain-isp1] ip-pool pool1
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
      2. Create a user group named **group1**.
         
         ```
         [~BRAS] user-group group1
         ```
      3. Configure the domain named **isp1**.
         
         ```
         [~BRAS] aaa
         ```
         ```
         [~BRAS-aaa] domain isp1
         ```
         ```
         [*BRAS-aaa-domain-isp1] radius-server group rd1
         ```
         ```
         [*BRAS-aaa-domain-isp1] user-group group1 bind nat instance nat1
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
      4. Configure a user access interface.
         
         ```
         [~BRAS] interface gigabitEthernet 0/2/0.1
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
         [~BRAS-GigabitEthernet0/2/0.1] bas
         ```
         ```
         [~BRAS-GigabitEthernet0/2/0.1-bas] access-type layer2-subscriber default-domain authentication isp1
         ```
         ```
         [*BRAS-GigabitEthernet0/2/0.1-bas] authentication-method bind
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
   4. Enable centralized NAT to provide backup.
      
      
      ```
      [~BRAS] nat instance nat1
      ```
      ```
      [~BRAS-nat-instance-nat1] nat centralized-backup enable
      ```
      ```
      [*BRAS-nat-instance-nat1] commit
      ```
      ```
      [~BRAS-nat-instance-nat1] quit
      ```
   5. Configure a NAT traffic diversion policy.
      
      
      1. Configure an ACL numbered 6001.
         
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
      2. Configure a traffic classifier named **c1**.
         
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
      3. Configure a traffic behavior named **b1**, which binds traffic to the NAT instance named **nat1**.
         
         ```
         [~BRAS] traffic behavior b1
         ```
         ```
         [*BRAS-behavior-b1] nat bind instance nat1
         ```
         ```
         [*BRAS-behavior-b1] commit
         ```
         ```
         [~BRAS-behavior-b1] quit
         ```
      4. Configure a NAT traffic diversion policy and associate the ACL rule with the traffic behavior.
         
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
      5. Apply the NAT traffic policy named **p1** in the system view.
         
         ```
         [~BRAS] traffic-policy p1 inbound
         ```
         ```
         [*BRAS] commit
         ```
   6. Configure a NAT conversion policy.
      
      
      1. Configure an ACL numbered 3001 to match user traffic.
         
         ```
         [~BRAS] acl 3001
         ```
         ```
         [*BRAS-acl4-advance-3001] rule 10 permit ip source 10.10.10.0 0.0.0.255
         ```
         ```
         [*BRAS-acl4-advance-3001] commit
         ```
         ```
         [~BRAS-acl4-advance-3001] quit
         ```
      2. Configure a NAT conversion policy.
         ```
         [~BRAS] nat instance nat1
         ```
         ```
         [~BRAS-nat-instance-nat1] nat outbound 3001 address-group address-group1
         ```
         ```
         [*BRAS-nat-instance-nat1] commit
         ```
         ```
         [~BRAS-nat-instance-nat1] quit
         ```
      3. Configure a static route.
         ```
         [~BRAS] ip route-static 0.0.0.0 255.255.255.255 192.168.10.2
         ```
         ```
         [*BRAS] commit
         ```
   7. Verify the configuration.
      
      
      
      # Check NAT user information.
      
      ```
      [~BRAS] display nat user-information slot 1 verbose
      ```
      ```
      This operation will take a few minutes. Press 'Ctrl+C' to break ...
      Slot: 1     
      Total number:  1.
        ---------------------------------------------------------------------------
        User Type                             :  NAT444
        CPE IP                                :  10.10.10.1
        User ID                               :  0
        VPN Instance                          :  -
        Address Group                         :  address-group1
        NoPAT Address Group                   :  -
        NAT Instance                          :  nat1
        Public IP                             :  11.11.11.101
        NoPAT Public IP                       :  -
        Start Port                            :  1024
        Port Range                            :  4096
        Port Total                            :  256
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
2. Configure policy-based routing on the CR to redirect user traffic to the NAT device.
   
   
   1. Configure a traffic diversion policy.
      
      ```
      [~CR] acl 2001
      ```
      ```
      [*CR-acl4-basic-2001] rule 10 permit source 10.10.10.0 0.0.0.255
      ```
      ```
      [*CR-acl4-basic-2001] commit
      ```
      ```
      [~CR-acl4-basic-2001] quit
      ```
      ```
      [~CR] traffic classifier c1
      ```
      ```
      [*CR-classifier-c1] if-match acl 2001
      ```
      ```
      [*CR-classifier-c1] commit
      ```
      ```
      [~CR-classifier-c1] quit
      ```
      ```
      [~CR] traffic behavior b1
      ```
      ```
      [*CR-behavior-b1] redirect ip-nexthop 192.168.11.2
      ```
      ```
      [*CR-behavior-b1] commit
      ```
      ```
      [~CR-behavior-b1] quit
      ```
      ```
      [~CR] traffic policy p1
      ```
      ```
      [*CR-policy-p1] classifier c1 behavior b1
      ```
      ```
      [*CR-policy-p1] commit
      ```
      ```
      [~CR-policy-p1] quit
      ```
   2. Configure an inbound interface redirection policy.
      
      ```
      [~CR] interface gigabitEthernet 0/2/2
      ```
      ```
      [~CR-GigabitEthernet0/2/2] ip address 192.168.10.2 24
      ```
      ```
      [*CR-GigabitEthernet0/2/2] traffic-policy p1 inbound
      ```
      ```
      [*CR-GigabitEthernet0/2/2] commit
      ```
      ```
      [~CR-GigabitEthernet0/2/2] quit
      ```
   3. Configure a static route.
      ```
      [~CR] ip route-static 11.11.11.0 255.255.255.0 192.168.10.1
      ```
      ```
      [*CR] commit
      ```
3. Configure centralized NAT on the NAT device.
   
   
   1. Configure basic NAT functions.
      
      ```
      [~CGN] service-location 1
      ```
      ```
      [*CGN-service-location-1] location slot 1
      ```
      ```
      [*CGN-service-location-1] commit
      ```
      ```
      [~CGN-service-location-1] quit
      ```
      ```
      [~CGN] service-instance-group group1
      ```
      ```
      [*CGN-service-instance-group-group1] service-location 1
      ```
      ```
      [*CGN-service-instance-group-group1] commit
      ```
      ```
      [~CGN-service-instance-group-group1] quit
      ```
      ```
      [~CGN] nat instance nat1 id 1
      ```
      ```
      [*CGN-nat-instance-nat1] service-instance-group group1
      ```
      ```
      [*CGN-nat-instance-nat1] nat address-group address-group1 group-id 1 10.34.161.101 10.34.161.105
      ```
      ```
      [*CGN-nat-instance-nat1] nat outbound any address-group address-group1
      ```
      ```
      [*CGN-nat-instance-nat1] commit
      ```
      ```
      [~CGN-nat-instance-nat1] quit
      ```
   2. Configure a NAT traffic diversion policy.
      
      ```
      [~CGN] acl 2001
      ```
      ```
      [*CGN-acl4-basic-2001] rule 0 permit source 10.10.10.0 0.0.0.255
      ```
      ```
      [*CGN-acl4-basic-2001] commit
      ```
      ```
      [~CGN-acl4-basic-2001] quit
      ```
      ```
      [~CGN] traffic classifier c1
      ```
      ```
      [*CGN-classifier-c1] if-match acl 2001
      ```
      ```
      [*CGN-classifier-c1] commit
      ```
      ```
      [~CGN-classifier-c1] quit
      ```
      ```
      [~CGN] traffic behavior b1
      ```
      ```
      [*CGN-behavior-b1] nat bind instance nat1
      ```
      ```
      [*CGN-behavior-b1] commit
      ```
      ```
      [~CGN-behavior-b1] quit
      ```
      ```
      [~CGN] traffic policy p1
      ```
      ```
      [*CGN-policy-p1] classifier c1 behavior b1
      ```
      ```
      [*CGN-policy-p1] commit
      ```
      ```
      [~CGN-policy-p1] quit
      ```
      ```
      [~CGN] interface gigabitEthernet 0/2/2
      ```
      ```
      [*CGN-GigabitEthernet0/2/2] ip address 192.168.11.2 24
      ```
      ```
      [*CGN-GigabitEthernet0/2/2] traffic-policy p1 inbound
      ```
      ```
      [*CGN-GigabitEthernet0/2/2] commit
      ```
      ```
      [~CGN-GigabitEthernet0/2/2] quit
      ```

#### Configuration Files

* BRAS configuration file
  
  ```
  #
  sysname BRAS
  #
  vsm on-board-mode disable
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1812 weight 0
   radius-server accounting 192.168.7.249 1813 weight 0
   radius-server shared-key-cipher %^%#glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$:978$$e:TY%^%
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ip address 192.168.11.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0.1
   user-vlan 1
   bas
    access-type layer2-subscriber default-domain authentication isp1
    authentication-method bind
  #
  ip pool pool1 bas local
   gateway 10.10.10.1 255.255.255.0
   section 1 10.10.10.1 10.10.10.100
   dns-server 192.168.7.252
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
   nat centralized-backup enable
   port-range 4096
  #
  user-group group1
  #
  acl number 3001
   rule 10 permit ip source 10.10.10.0 0.0.0.255
  #
  acl number 6001
   rule 1 permit ip source user-group group1
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat1
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 1
  #
  traffic-policy p1 inbound
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
     radius-server group rd1
     ip-pool pool1
     user-group group1 bind nat instance nat1
   #
  #
  ip route-static 0.0.0.0 255.255.255.255 192.168.10.2
  #
   return
  ```
* CR configuration file
  
  ```
  #
  sysname CR
  #
  acl number 2001
   rule 10 permit source 10.10.10.0 0.0.0.255
  #
  traffic classifier c1 operator or
   if-match acl 2001 precedence 1
  #
  traffic behavior b1
   redirect ip-nexthop 192.168.11.2
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 1
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ip address 192.168.10.2 255.255.255.0
   traffic-policy p1 inbound
  #
  ip route-static 11.11.11.0 255.255.255.0 192.168.10.1
  #
   return
  ```
* CGN configuration file
  
  ```
  #
  sysname CGN
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1
  #
  acl number 2001
   rule 0 permit source 10.10.10.0 0.0.0.255
  #
  service-location 1
   location slot 1
  #
  service-instance-group group1
   service-location 1
  #
  nat instance nat1 id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 10.34.161.101 10.34.161.105
   nat outbound any address-group address-group1
   port-range 4096
  #
  traffic classifier c1 operator or
   if-match acl 2001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat1
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 1
  #
  interface gigabitEthernet 0/2/2
   undo shutdown
   ip address 192.168.11.2 24
   traffic-policy p1 inbound
  #
   return
  ```