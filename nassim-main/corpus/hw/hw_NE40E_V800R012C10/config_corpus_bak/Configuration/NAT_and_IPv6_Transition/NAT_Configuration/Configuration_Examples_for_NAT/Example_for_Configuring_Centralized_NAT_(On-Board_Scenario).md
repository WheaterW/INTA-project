Example for Configuring Centralized NAT (On-Board Scenario)
===========================================================

This section provides an example for configuring the centralized NAT function to implement multiple-to-multiple translations from internal addresses of enterprise users to external addresses and allow only PCs on a specified network segment to access the Internet.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374587__fig132461399915), the Router performs the NAT function to help PCs within the enterprise network access the Internet. The NE40E uses GE 0/1/0 to connect to the enterprise network. The NE40E is connected to the Internet through GE 0/1/1. The company has five public IP addresses ranging from 11.11.11.101/32 to 11.11.11.105/32.

[Figure 1](#EN-US_TASK_0172374587__fig132461399915) shows IP addresses of interfaces. The configuration requirements are as follows:

* Only PCs on the network segment of 192.168.10.0/24 can access the Internet.
* Many-to-many NAT needs to be performed for IP addresses between the private and public networks.

**Figure 1** Example for configuring the centralized NAT function  
![](figure/en-us_image_0000001586004852.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure a NAT traffic diversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* Service-location group index: 1
* Service-instance group name: group1
* NAT instance name: nat1; NAT instance index: 1
* NAT address pool name for NAT device: address-group1; NAT address pool ID: 1; IP address segment: 11.11.11.101 to 11.11.11.105
* ACL number: 3001
* Name and IP address of the interface to which a NAT traffic diversion policy is applied


#### Procedure

1. Configure basic NAT functions.
   1. Create a NAT instance named **nat1** and bind it to the service board.
      
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname NAT
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~NAT] service-location 1
      ```
      ```
      [*NAT-service-location-1] location slot 3
      ```
      ```
      [*NAT-service-location-1] commit
      ```
      ```
      [~NAT-service-location-1] quit
      ```
      ```
      [~NAT] service-instance-group group1
      ```
      ```
      [*NAT-service-instance-group-group1] service-location 1
      ```
      ```
      [*NAT-service-instance-group-group1] commit
      ```
      ```
      [~NAT-service-instance-group-group1] quit
      ```
      ```
      [~NAT] nat instance nat1 id 1
      ```
      ```
      [*NAT-nat-instance-nat1] service-instance-group group1
      ```
      ```
      [*NAT-nat-instance-nat1] commit
      ```
      ```
      [~NAT-nat-instance-nat1] quit
      ```
   2. Configure a NAT address pool and specify a range of IP addresses of 11.11.11.101 through 11.11.11.105 in the pool.
      
      
      ```
      [~NAT] nat instance nat1 id 1
      ```
      ```
      [~NAT-nat-instance-nat1] nat address-group address-group1 group-id 1
      ```
      ```
      [*NAT-nat-instance-nat1-nat-address-group-address-group1] section 1 11.11.11.101 11.11.11.105
      ```
      ```
      [*NAT-nat-instance-nat1-nat-address-group-address-group1] commit
      ```
      ```
      [~NAT-nat-instance-nat1-nat-address-group-address-group1] quit
      ```
      ```
      [~NAT-nat-instance-nat1] quit
      ```
2. Configure a NAT traffic diversion policy.
   
   
   
   Apply a NAT traffic diversion policy on either an inbound or outbound interface as required.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A NAT traffic diversion policy on an inbound interface and that on an outbound interface are mutually exclusive on a device.
   
   
   
   * Apply the NAT traffic diversion policy to the inbound interface.
     1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
        ```
        [~NAT] acl 3001
        ```
        ```
        [*NAT-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
        ```
        ```
        [*NAT-acl4-advance-3001] commit
        ```
        ```
        [~NAT-acl4-advance-3001] quit
        ```
     2. Configure a traffic classifier.
        ```
        [~NAT] traffic classifier classifier1
        ```
        ```
        [*NAT-classifier-classifier1] if-match acl 3001
        ```
        ```
        [*NAT-classifier-classifier1] commit
        ```
        ```
        [~NAT-classifier-classifier1] quit
        ```
     3. Configure a traffic behavior named **behavior1**, which binds traffic to the NAT instance named **nat1**.
        ```
        [~NAT] traffic behavior behavior1
        ```
        ```
        [*NAT-behavior-behavior1] nat bind instance nat1
        ```
        ```
        [*NAT-behavior-behavior1] commit
        ```
        ```
        [~NAT-behavior-behavior1] quit
        ```
     4. Configure a NAT traffic policy named **policy1** to associate the ACL rule with the traffic behavior.
        ```
        [~NAT] traffic policy policy1
        ```
        ```
        [*NAT-trafficpolicy-policy1] classifier classifier1 behavior behavior1
        ```
        ```
        [*NAT-trafficpolicy-policy1] commit
        ```
        ```
        [~NAT-trafficpolicy-policy1] quit
        ```
     5. Apply the NAT traffic diversion policy in the GE 0/1/0 interface view.
        ```
        [~NAT] interface gigabitEthernet 0/1/0
        ```
        ```
        [~NAT-GigabitEthernet0/1/0] ip address 192.168.10.1 24
        ```
        ```
        [*NAT-GigabitEthernet0/1/0] traffic-policy policy1 inbound
        ```
        ```
        [*NAT-GigabitEthernet0/1/0] commit
        ```
        ```
        [~NAT-GigabitEthernet0/1/0] quit
        ```
   * Apply the NAT traffic diversion policy to the outbound interface.
     1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
        ```
        [~NAT] acl 3001
        ```
        ```
        [*NAT-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
        ```
        ```
        [*NAT-acl4-advance-3001] commit
        ```
        ```
        [~NAT-acl4-advance-3001] quit
        ```
     2. Apply the ACL-based traffic policy in the view of GE 0/1/1.
        ```
        [~NAT] interface gigabitEthernet 0/1/1
        ```
        ```
        [~NAT-GigabitEthernet0/1/1] ip address 1.1.1.1 24
        ```
        ```
        [*NAT-GigabitEthernet0/1/1] nat bind acl 3001 instance nat1
        ```
        ```
        [*NAT-GigabitEthernet0/1/1] commit
        ```
        ```
        [~NAT-GigabitEthernet0/1/1] quit
        ```
     3. Configure an IP address for GE 0/1/0.
        ```
        [~NAT] interface gigabitEthernet 0/1/0
        ```
        ```
        [~NAT-GigabitEthernet0/1/0] ip address 192.168.10.1 24
        ```
        ```
        [*NAT-GigabitEthernet0/1/0] commit
        ```
        ```
        [~NAT-GigabitEthernet0/1/0] quit
        ```
3. Verify the configuration.
   
   
   
   # Check NAT user information.
   
   ```
   [~NAT] display nat user-information slot 3 verbose
   This operation will take a few minutes. Press 'Ctrl+C' to break ...             
   Slot: 3 
   Total number:  1.                                                          
     ---------------------------------------------------------------------------   
     User Type                             : NAT444           
     CPE IP                                : 192.168.10.100    
     User ID                               : -
     VPN Instance                          : -
     Address Group                         : address-group1
     NoPAT Address Group                   : -
     NAT Instance                          : nat1
     Public IP                             : 11.11.11.102
     NoPAT Public IP                       : -
     Total/TCP/UDP/ICMP Session Limit      : 8192/10240/10240/512
     Total/TCP/UDP/ICMP Session Current    : 1/0/1/0
     Total/TCP/UDP/ICMP Rev Session Limit  : 8192/10240/10240/512
     Total/TCP/UDP/ICMP Rev Session Current: 0/0/0/0
     Nat ALG Enable                        : NULL
     Create Time                           :  2023-01-06 16:42:17 
     Aging Time(s)                         : -
     Left Time(s)                          : -
     Session Limit Discard Count           : 0
     -->Transmit Packets                   : 1379646
     -->Transmit Bytes                     : 127279644
     -->Drop Packets                       : 0
     <--Transmit Packets                   : 0
     <--Transmit Bytes                     : 0
     <--Drop Packets                       : 0
     Fast-forwarding Statistics ID         :  - 
     -->Hit Fast-fwd session Packets       :  - 
     -->NP transmit to multi-core Packets  :  -
     <--Hit Fast-fwd session Packets       :  -
     <--NP transmit to multi-core Packets  :  - 
     --------------------------------------------------------------------------- 
   ```

#### Configuration Files

* NAT device configuration file when a NAT traffic diversion policy is used on an inbound interface
  
  ```
  #
  sysname NAT
  #
  service-location 1
   location slot 3  #
  service-instance-group group1      
   service-location 1      
  #
  nat instance nat1 id 1      
   service-instance-group group1  
   nat address-group address-group1 group-id 1 
    section 1 11.11.11.101 11.11.11.105     
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
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
  #
  return
  ```
* NAT device configuration file when a NAT traffic diversion policy is used on an outbound interface
  
  ```
  #
  sysname NAT
  #
  service-location 1
   location slot 3  #
  service-instance-group group1      
   service-location 1      
  #
  nat instance nat1 id 1      
   service-instance-group group1  
   nat address-group address-group1 group-id 1 
    section 1 11.11.11.101 11.11.11.105     
  #
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
  #
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
   nat bind acl 3001 instance nat1 precedence 0
  #
  return
  ```