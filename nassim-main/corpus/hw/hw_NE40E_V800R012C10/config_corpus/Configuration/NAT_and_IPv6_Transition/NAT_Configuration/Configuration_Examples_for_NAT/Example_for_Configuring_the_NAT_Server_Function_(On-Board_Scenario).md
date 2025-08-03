Example for Configuring the NAT Server Function (On-Board Scenario)
===================================================================

This section provides an example for configuring the NAT Server function. By specifying an internal NAT server and configuring the mapping entries between the internal server's private IP address/port and public IP address/port, an external host can access the internal server.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374604__fig_dc_ne_cfg_01333001), the Router performs the NAT function to help PCs within the enterprise network access the Internet. The Router uses GE 0/1/1 to connect to an internal network and GE 0/1/2 to connect to the Internet.

The internal network address of the enterprise network is 192.168.0.0/16. The internal server address is 192.168.10.10/32. Only PCs on the network segment of 192.168.10.0/24 can access the Internet. External PCs can access the internal server. Five public IP addresses 1.1.1.101/32 through 1.1.1.105/32 are assigned to the enterprise. The internal server of the enterprise has an independent public address 1.1.1.100. The internal server can be accessed from the external network address 3.3.3.2 through 1:1 NAT.

**Figure 1** Network diagram of the NAT internal server![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configurations in this example are mainly performed on NATA and DeviceB.

Interfaces 1 through 3 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_ne_nat_cfg_0008.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure a NAT traffic diversion policy.
3. Configure an internal NAT server.


#### Data Preparation

To complete the configuration, you need the following data:

* Service-location group index: 1
* Service-instance group name: group1
* NAT instance name: nat1; NAT instance index: 1
* NAT address pool name for NATA: address-group1; NAT address pool ID: 1; IP address segment: 1.1.1.101 to 1.1.1.105
* ACL number: 3001
* Traffic classifier name: classifier1
* Traffic behavior name: behavior1
* Traffic policy name: policy1
* Name (GE0/1/1) and IP address (192.168.10.1/24) of an interface to which a NAT traffic diversion policy is applied
* Private IP address of the internal NAT server: 192.168.10.10; public IP address of the internal NAT server: 1.1.1.100


#### Procedure

1. Configure basic NAT functions.
   1. Create a NAT instance named **nat1** and bind it to the service board.
      
      
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
      [~NATA] service-location 1
      ```
      ```
      [*NATA-service-location-1] location slot 3
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
   2. Configure a NAT address pool and specify a range of IP addresses of 1.1.1.101 through 1.1.1.105 in the pool.
      
      
      ```
      [~NATA] nat instance nat1
      ```
      ```
      [~NATA-nat-instance-nat1] nat address-group address-group1 group-id 1 1.1.1.101 1.1.1.105
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
     1. Configure a traffic classification rule based on ACL 3001.
        
        Configure ACL rule 1 to allow only hosts on the internal network segment 192.168.10.0/24 to access the Internet.
        
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
     2. Configure a traffic classifier named **classifier1** and define an ACL-based matching rule.
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
     3. Configure a traffic behavior named **behavior1**, which binds traffic to the NAT instance.
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
     5. Apply the NAT traffic diversion policy in the interface view.
        ```
        [~NATA] interface gigabitEthernet 0/1/1
        ```
        ```
        [~NATA-GigabitEthernet0/1/1] ip address 192.168.10.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/1/1] traffic-policy policy1 inbound
        ```
        ```
        [*NATA-GigabitEthernet0/1/1] commit
        ```
        ```
        [~NATA-GigabitEthernet0/1/1] quit
        ```
     6. Configure the IP address of GE 0/1/2.
        ```
        [~NATA] interface gigabitEthernet 0/1/2
        ```
        ```
        [*NATA-GigabitEthernet0/1/2] ip address 2.2.2.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/1/2] commit
        ```
        ```
        [~NATA-GigabitEthernet0/1/2] quit
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
     2. Apply the ACL policy to GE 0/1/2.
        ```
        [~NATA] interface gigabitEthernet 0/1/2
        ```
        ```
        [~NATA-GigabitEthernet0/1/2] ip address 2.2.2.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/1/2] nat bind acl 3001 instance nat1
        ```
        ```
        [*NATA-GigabitEthernet0/1/2] commit
        ```
        ```
        [~NATA-GigabitEthernet0/1/2] quit
        ```
     3. Configure an IP address for GE 0/1/1.
        ```
        [~NATA] interface gigabitEthernet 0/1/1
        ```
        ```
        [*NATA-GigabitEthernet0/1/1] ip address 192.168.10.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/1/1] commit
        ```
        ```
        [~NATA-GigabitEthernet0/1/1] quit
        ```
3. Define the internal server address as 192.168.10.10 and external address as 1.1.1.100. Use the address-level mode to ensure 1:1 relationship between the public and private IP addresses.
   
   
   ```
   [~NATA] nat instance nat1
   ```
   ```
   [~NATA-nat-instance-nat1] nat server-mode enable
   ```
   ```
   [*NATA-nat-instance-nat1] nat server global 1.1.1.100 inside 192.168.10.10
   ```
   ```
   [*NATA-nat-instance-nat1] commit
   ```
   ```
   [~NATA-nat-instance-nat1] quit
   ```
4. Configure a default route as a static route and set the next hop address of the default route to 2.2.2.2.
   
   
   ```
   [~NATA] ip route-static 0.0.0.0 0.0.0.0 2.2.2.2
   ```
   ```
   [*NATA] commit
   ```
5. Verify the configuration.
   
   
   
   # Display server mapping entries of all users.
   
   ```
   <NATA> display nat server-map
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...
   Slot: 3
   Total number:  2.
     NAT Instance: nat1          
     Protocol:ANY, VPN:--->-   
     Server:192.168.10.10[1.1.1.100]->ANY  
     Tag:0x0, TTL:-, Left-Time:-      
     CPE IP:192.168.10.10                                                                                                                                             
     NAT Instance: nat1        
     Protocol:ANY, VPN:--->-      
     Server reverse:ANY->1.1.1.100[192.168.10.10] 
     Tag:0x0, TTL:-, Left-Time:-   
     CPE IP:192.168.10.10  
   ```

#### Configuration Files

* NATA configuration file (traffic diversion policy on the inbound interface)
  
  ```
  #
   sysname NATA
  #
  service-location 1
   location slot 3
  #
  service-instance-group group1
   service-location 1
  #
  nat instance nat1 id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 1.1.1.101 1.1.1.105 
   nat server-mode enable
   nat server global 1.1.1.100 inside 192.168.10.10
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
   classifier classifier1 behavior behavior1 precedence 1
  #
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface GigabitEthernet 0/1/2
   undo shutdown
   ip address 2.2.2.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.0 0.0.0.255
  #
  ip route-static 0.0.0.0 0.0.0.0 2.2.2.2
  #
   return
  ```
* NATA configuration file (traffic diversion policy on the outbound interface)
  
  ```
  #
   sysname NATA
  #
  service-location 1
   location slot 3
  #
  service-instance-group group1
   service-location 1
  #
  nat instance nat1 id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 1.1.1.101 1.1.1.105 
   nat server-mode enable
   nat server global 1.1.1.100 inside 192.168.10.10
  #
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
  #
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
  #
  interface GigabitEthernet 0/1/2
   undo shutdown
   ip address 2.2.2.1 255.255.255.0
   nat bind acl 3001 instance nat1
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.0 0.0.0.255
  #
  ip route-static 0.0.0.0 0.0.0.0 2.2.2.2
  #
   return
  ```
* DeviceB configuration file
  
  ```
  #
   sysname DeviceB
  #
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 3.3.3.1 255.255.255.0
  #
  interface GigabitEthernet 0/1/3
   undo shutdown
   ip address 2.2.2.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.0 0.0.0.255
    network 3.3.3.0 0.0.0.255
  #
   return
  ```