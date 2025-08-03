Example for Configuring the NAT Server Function (Dedicated Board Scenario)
==========================================================================

This section provides an example for configuring the NAT Server function. By specifying an internal NAT server and configuring the mapping entries between the internal server's private IP address/port and public IP address/port, an external host can access the internal server.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

In [Figure 1](#EN-US_TASK_0000001139739805__en-us_task_0172374601_fig_dc_ne_cfg_01333001), the Router performs the NAT function to help PCs within the enterprise network access the Internet. A service board is installed in slot 1 of the router. The Router uses GE0/2/0 to connect to an internal network and GE0/3/0 to connect to the Internet.

The internal network address of the enterprise network is 192.168.0.0/16. The enterprise provides the FTP service. The internal FTP server address is 192.168.10.10/32. Only PCs on the network segment of 192.168.10.0/24 can access the Internet. External PCs can access the internal server. Five public IP addresses 1.1.1.101/32 through 1.1.1.105/32 are assigned to the enterprise. In addition, the internal server has an independent public IP address 1.1.1.100. Through 1:1 NAT, the internal FTP server can be accessed from the external IP address 3.3.3.2.

**Figure 1** Network diagram of the NAT internal server![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configurations in this example are mainly performed on NATA and DeviceB.

Interfaces 1 and 2 in this example represent GE 0/2/0 and GE 0/3/0, respectively.


  
![](images/fig_dc_ne_nat_cfg_0008.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Configure a NAT traffic diversion policy.
3. Configure a NAT conversion policy.
4. Configure an internal NAT server.


#### Data Preparation

To complete the configuration, you need the following data:

* Service-location group index: 1
* Slot ID (1) of the NATA's NAT service board
* Name of a service-instance group (group1)
* NAT instance name (nat1) and index (1)
* NATA's NAT address pool name (address-group1), address pool number (1), a range of public IP addresses (1.1.1.101 through 1.1.1.105)
* ACL number (3001)
* Traffic classifier (classifier1)
* Traffic behavior (behavior1)
* Traffic policy (policy1)
* Name (GE 0/2/0) and IP address (192.168.10.1/24) of an interface to which a NAT traffic diversion policy is applied
* Internal NAT server's private IP address (192.168.10.10) and public IP address (1.1.1.100)


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
      [~NATA-license] active nat session-table size 6 slot 1
      ```
      ```
      [~NATA-license] active nat bandwidth-enhance 40 slot 1
      ```
      ```
      [~NATA-license] quit
      ```
   2. Create a NAT instance named **nat1** and bind it to the service board.
      
      
      ```
      [~NATA] service-location 1
      ```
      ```
      [*NATA-service-location-1] location slot 1
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
   3. Configure a NAT address pool and specify a range of IP addresses of 1.1.1.101 through 1.1.1.105 in the pool.
      
      
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
        [*NATA-policy-policy1] classifier classifier1 behavior behavior1
        ```
        ```
        [*NATA-policy-policy1] commit
        ```
        ```
        [~NATA-policy-policy1] quit
        ```
     5. Apply the NAT traffic diversion policy in the GE 0/2/0 interface view.
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
     6. Configure an IP address for GE 0/3/0.
        ```
        [~NATA] interface gigabitEthernet 0/3/0
        ```
        ```
        [*NATA-GigabitEthernet0/3/0] ip address 2.2.2.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/3/0] commit
        ```
        ```
        [~NATA-GigabitEthernet0/3/0] quit
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
     2. Apply the ACL policy to GE 0/3/0.
        ```
        [~NATA] interface gigabitEthernet 0/3/0
        ```
        ```
        [~NATA-GigabitEthernet0/3/0] ip address 2.2.2.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/3/0] nat bind acl 3001 instance nat1
        ```
        ```
        [*NATA-GigabitEthernet0/3/0] commit
        ```
        ```
        [~NATA-GigabitEthernet0/3/0] quit
        ```
     3. Configure an IP address for GE 0/2/0.
        ```
        [~NATA] interface gigabitEthernet 0/2/0
        ```
        ```
        [*NATA-GigabitEthernet0/2/0] ip address 192.168.10.1 24
        ```
        ```
        [*NATA-GigabitEthernet0/2/0] commit
        ```
        ```
        [~NATA-GigabitEthernet0/2/0] quit
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
4. Configure an internal server with the private IP address 192.168.10.10 and the public IP address 1.1.1.100.
   
   
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
5. Configure a default route as a static route and set the next hop address of the default route to 2.2.2.2.
   
   
   ```
   [~NATA] ip route-static 0.0.0.0 0.0.0.0 2.2.2.2
   ```
   ```
   [*NATA] commit
   ```
6. Verify the configuration.
   
   
   
   # Display server mapping entries of all users.
   
   ```
   <NATA> display nat server-map
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...
   Slot: 1
   Total number:  2.
     NAT Instance: nat1   
     Protocol:ANY, VPN:--->-      
     Server:192.168.10.10[1.1.1.100]->ANY   
     Tag:0x0, TTL:-, Left-Time:-    
     CPE IP:192.168.10.10
     outbound: false
     extendable: false                                                                                                                                          
     NAT Instance: nat1     
     Protocol:ANY, VPN:--->-    
     Server reverse:ANY->1.1.1.100[192.168.10.10] 
     Tag:0x0, TTL:-, Left-Time:-    
     CPE IP:192.168.10.10
     outbound: false
     extendable: false  
   ```

#### Configuration Files

* NATA configuration file (traffic diversion policy on the inbound interface)
  
  ```
  #
   sysname NATA
  #
  vsm on-board-mode disable
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
   nat address-group address-group1 group-id 1 1.1.1.101 1.1.1.105 
   nat outbound 3001 address-group address-group1
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
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface GigabitEthernet 0/3/0
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
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1
  #
  service-location 1
   location slot 1 
  #
  service-instance-group group1
   service-location 1
  #
  nat instance nat1 id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 1.1.1.101 1.1.1.105 
   nat outbound 3001 address-group address-group1
   nat server-mode enable
   nat server global 1.1.1.100 inside 192.168.10.10
  #
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
  #
  interface GigabitEthernet 0/3/0
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
  interface GigabitEthernet 0/3/0
   undo shutdown
   ip address 2.2.2.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.0 0.0.0.255
    network 3.3.3.0 0.0.0.255
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 3.3.3.1 255.255.255.0
  #
   return
  ```