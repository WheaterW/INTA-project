Example for Configuring Centralized NAT (Dedicated Board Scenario)
==================================================================

This section provides an example for configuring the centralized NAT function to implement many-to-many IP address translation between private and public networks and allow PCs on a specified network segment to access the Internet.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section uses the NE40E-M2K and NE40E-M2K-B as an example.

On the network shown in [Figure 1](#EN-US_TASK_0000001092838006__en-us_task_0172374586_fig_dc_ne_cfg_nat_005701), the Router performs the NAT function to help PCs within the enterprise network access the Internet. The Router uses GE 0/2/0 to connect to the enterprise network. The Router is connected to the Internet through GE 0/2/1. The company has five public IP addresses ranging from 11.11.11.101/32 to 11.11.11.105/32.

[Figure 1](#EN-US_TASK_0000001092838006__en-us_task_0172374586_fig_dc_ne_cfg_nat_005701) shows IP addresses of interfaces. The configuration requirements are as follows:

* Only PCs on the network segment of 192.168.10.0/24 can access the Internet.
* Many-to-many NAT needs to be performed for IP addresses between the private and public networks.

**Figure 1** NAT networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/0 and GE 0/2/1, respectively.


  
![](images/fig_dc_ne_cfg_nat_0009.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure a NAT traffic diversion policy.
3. Configure a NAT conversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* Service-location group index: 1
* Slot ID (1) of NATA's service board
* Name of a service-instance group (group1)
* NAT instance name (nat1) and index (1)
* NATA's NAT address pool name (address-group1), address pool number (1), a range of public IP addresses (11.11.11.101 through 11.11.11.105)
* ACL number (3001)
* Traffic classifier (classifier1)
* Traffic behavior (behavior1)
* Traffic policy (policy1)
* Name and IP address of each interface to which a NAT traffic diversion policy is applied


#### Procedure

1. Configure basic NAT functions.
   1. Set the maximum number of sessions that can be created on the service board in slot 1 to 6M.
      
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname NATA
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~NATA] vsm on-board-mode disable
      ```
      ```
      [*NATA] commit
      ```
      ```
      [~NATA] license
      ```
      ```
      [~NATA-license] active nat session-table size 6 slot 
      ```
      ```
      [*NATA-license] active nat bandwidth-enhance 40 slot 
      ```
      ```
      [*NATA-license] commit
      ```
      ```
      [~NATA-license] quit
      ```
   2. Create a NAT instance named **nat1** and bind it to the service board.
      
      
      ```
      [~NATA] service-location 1
      ```
      ```
      [*NATA-service-location-1] location slot  
      ```
      ```
      [*NATA-service-location-1] commit
      ```
      ```
      [~NATA-service-location-1] quit
      ```
      ```
      [~NATA] service-instance-group group1
      ```
      ```
      [*NATA-service-instance-group-group1] service-location 1
      ```
      ```
      [*NATA-service-instance-group-group1] commit
      ```
      ```
      [~NATA-service-instance-group-group1] quit
      ```
      ```
      [~NATA] nat instance nat1 id 1
      ```
      ```
      [*NATA-nat-instance-nat1] service-instance-group group1
      ```
      ```
      [*NATA-nat-instance-nat1] commit
      ```
      ```
      [~NATA-nat-instance-nat1] quit
      ```
   3. Configure a NAT address pool with addresses ranging from 11.11.11.101 to 11.11.11.105. Configure port pre-allocation and set the address pool translation mode to 3-tuple.
      
      
      ```
      [~NATA] nat instance nat1
      ```
      ```
      [~NATA-nat-instance-nat1] nat address-group address-group1 group-id 1
      ```
      ```
      [*NATA-nat-instance-nat1-nat-address-group-address-group1] section 1 11.11.11.101 11.11.11.105
      ```
      ```
      [*NATA-nat-instance-nat1-nat-address-group-address-group1] quit
      ```
      ```
      [*NATA-nat-instance-nat1] port-range 1024
      ```
      ```
      [*NATA-nat-instance-nat1] nat filter mode full-cone
      ```
      ```
      [*NATA-nat-instance-nat1] commit 
      ```
      ```
      [~NATA-nat-instance-nat1] quit
      ```
2. Configure a NAT traffic diversion policy.
   
   Apply a NAT traffic diversion policy on either an inbound or outbound interface as required.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A NAT traffic diversion policy on an inbound interface and that on an outbound interface are mutually exclusive on a device.
   
   * Apply the NAT traffic diversion policy to the inbound interface.
     1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
        ```
        [~NATA] acl 3001
        ```
        ```
        [*NATA-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
        ```
        ```
        [*NATA-acl4-advance-3001] commit
        ```
        ```
        [~NATA-acl4-advance-3001] quit
        ```
     2. Configure a traffic classifier.
        ```
        [~NATA] traffic classifier classifier1
        ```
        ```
        [*NATA-classifier-classifier1] if-match acl 3001
        ```
        ```
        [*NATA-classifier-classifier1] commit
        ```
        ```
        [~NATA-classifier-classifier1] quit
        ```
     3. Configure a traffic behavior named **behavior1**, which binds traffic to the NAT instance named **nat1**.
        ```
        [~NATA] traffic behavior behavior1
        ```
        ```
        [*NATA-behavior-behavior1] nat bind instance nat1
        ```
        ```
        [*NATA-behavior-behavior1] commit
        ```
        ```
        [~NATA-behavior-behavior1] quit
        ```
     4. Configure a NAT traffic policy named **policy1** to associate the ACL rule with the traffic behavior.
        ```
        [~NATA] traffic policy policy1
        ```
        ```
        [*NATA-trafficpolicy-policy1] classifier classifier1 behavior behavior1
        ```
        ```
        [*NATA-trafficpolicy-policy1] commit
        ```
        ```
        [~NATA-trafficpolicy-policy1] quit
        ```
     5. Apply the NAT traffic diversion policy in the view of GE 0/2/0.
        ```
        [~NATA] interface gigabitEthernet 0/2/0
        ```
        ```
        [~NATA-GigabitEthernet0/2/0] ip address 192.168.10.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/2/0] traffic-policy policy1 inbound
        ```
        ```
        [*NATA-GigabitEthernet0/2/0] commit
        ```
        ```
        [~NATA-GigabitEthernet0/2/0] quit
        ```
   * Apply the NAT traffic diversion policy to the outbound interface.
     1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
        ```
        [~NATA] acl 3001
        ```
        ```
        [*NATA-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
        ```
        ```
        [*NATA-acl4-advance-3001] commit
        ```
        ```
        [~NATA-acl4-advance-3001] quit
        ```
     2. Apply the ACL-based traffic classification policy in the view of GE 0/2/1.
        ```
        [~NATA] interface gigabitEthernet 0/2/1
        ```
        ```
        [~NATA-GigabitEthernet0/2/1] ip address 1.1.1.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/2/1] nat bind acl 3001 instance nat1
        ```
        ```
        [*NATA-GigabitEthernet0/2/1] commit
        ```
        ```
        [~NATA-GigabitEthernet0/2/1] quit
        ```
3. Configure a NAT conversion policy.
   
   
   ```
   [~NATA] nat instance nat1
   ```
   ```
   [~NATA-nat-instance-nat1] nat outbound 3001 address-group address-group1
   ```
   ```
   [*NATA-nat-instance-nat1] commit
   ```
   ```
   [~NATA-nat-instance-nat1] quit
   ```
4. Verify the configuration.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After centralized NAT is configured, routes to NAT public addresses need to be advertised so that the Internet can learn such routes.
   
   
   
   # Check NAT user information.
   
   ```
   [~NATA] display nat user-information slot  verbose
   This operation will take a few minutes. Press 'Ctrl+C' to break ...             
   Slot:                                                                  
   Total number:  1.                                                          
     ---------------------------------------------------------------------------   
     User Type                             :  NAT444                  
     CPE IP                                :  192.168.10.100 
     User ID                               :  -                
     VPN Instance                          :  -               
     Address Group                         :  address-group1  
     NoPAT Address Group                   :  -  
     NAT Instance                          :  nat1      
     Public IP                             :  11.11.11.103  
     NoPAT Public IP                       :  -             
     
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512  
     Total/TCP/UDP/ICMP Session Current    :  1/0/1/0                
     Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512     
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0      
     Total/TCP/UDP/ICMP Port Limit         :  0/0/0/0   
     Total/TCP/UDP/ICMP Port Current       :  1/0/1/0  
     Nat ALG Enable                        :  NULL
     Port Reuse                            :  False
     Token/TB/TP                           :  0/0/0  
     Port Forwarding Flag                  :  Non Port Forwarding 
     Port Forwarding Ports                 :  0 0 0 0 0
     Create Time                           :  2020-01-02 20:44:50
     Aging Time(s)                         :  -      
     Left Time(s)                          :  - 
     Port Limit Discard Count              :  0 
     Session Limit Discard Count           :  0
     Fib Miss Discard Count                :  0
     -->Transmit Packets                   :  16507153
     -->Transmit Bytes                     :  1881815442
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

* NATA configuration file when a NAT traffic diversion policy is used on an inbound interface
  
  ```
  #
  sysname NATA
  #
  vsm on-board-mode disable
  #
  license 
   active nat session-table size 6 slot  active nat bandwidth-enhance 40 slot 
  #
  service-location 1 
   location slot  
  #
  service-instance-group group1      
   service-location 1      
  #
  nat instance nat1 id 1      
   port-range 1024
   service-instance-group group1      
   nat address-group address-group1 group-id 1 
    section 1 11.11.11.101 11.11.11.105     
   nat outbound 3001 address-group address-group1
   
   nat filter mode full-cone
  #
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
  #
  traffic classifier classifier1 operator or
   if-match acl 3001 precedence 1
  #
  traffic behavior behavior1
   nat bind instance nat1
  #
  traffic policy policy1
   share-mode
   classifier classifier1 behavior behavior1 precedence 1
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface GigabitEthernet 0/2/1
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
  #
  return
  ```
* NATA configuration file when a NAT traffic diversion policy is used on an outbound interface
  
  ```
  #
  sysname NATA
  #
  vsm on-board-mode disable
  #
  license 
   active nat session-table size 6 slot  active nat bandwidth-enhance 40 slot 
  #
  service-location 1      
   location slot  
  #
  service-instance-group group1      
   service-location 1      
  #
  nat instance nat1 id 1  
   port-range 1024    
   service-instance-group group1      
   nat address-group address-group1 group-id 1 
    section 1 11.11.11.101 11.11.11.105
   nat outbound 3001 address-group address-group1 
   nat filter mode full-cone
  #
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
  #
  interface GigabitEthernet 0/2/1
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
   nat bind acl 3001 instance nat1 precedence 0
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
  #
  return
  ```