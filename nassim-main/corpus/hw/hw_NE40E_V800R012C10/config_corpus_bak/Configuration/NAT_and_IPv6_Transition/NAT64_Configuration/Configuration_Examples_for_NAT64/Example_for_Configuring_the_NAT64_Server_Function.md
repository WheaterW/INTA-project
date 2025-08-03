Example for Configuring the NAT64 Server Function
=================================================

This section provides an example for configuring the NAT64 server function, which allows an external IPv4 user to proactively communicate with a private IPv6 server.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0237370586__fig_dc_ne_cfg_nat64_004201), it is required that the internal NAT64 server function be deployed on the NAT64 device and a static mapping between an internal IPv6 user's private IPv6 address+prefix and a public IPv4 address be configured, so that the external IPv4 user can use the public IPv4 address of the internal IPv6 user to access the internal IPv6 user.

**Figure 1** Configuring the internal NAT64 server function![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE0/2/1.


  
![](figure/en-us_image_0238555108.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic NAT64 functions.
2. Configure the internal NAT64 server function.
3. Configure an address for the interface on the private network side.

#### Data Preparation

* Slot ID of a service board
* ID of a service-location group
* NAT64 instance name and ID
* NAT64 address pool number and start and end IP addresses
* NAT64 IPv6 prefix (64:FF9B::/96)

#### Procedure

1. Configure basic NAT64 functions.
   1. Configure the NAT64 license function on a service board.
      
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname NAT64
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~NAT64] vsm on-board-mode disable
      ```
      ```
      [*NAT64] commit
      ```
      ```
      [~NAT64] license
      ```
      ```
      [*NAT64-license] active nat64 vsuf slot 1
      ```
      ```
      [*NAT64-license] active nat64 vsuf slot 2
      ```
      ```
      [*NAT64-license] active nat session-table size 16 slot 1 
      ```
      ```
      [*NAT64-license] active nat session-table size 16 slot 2 
      ```
      ```
      [*NAT64-license] commit
      ```
      ```
      [~NAT64-license] quit
      ```
   2. Configure a service-location group and bind it to the service boards.
      
      
      ```
      [~NAT64] service-location 1
      ```
      ```
      [*NAT64-service-location-1] location slot 3
      ```
      ```
      [*NAT64-service-location-1] commit
      ```
      ```
      [~NAT64-service-location-1] quit
      ```
   3. Create a service-instance group and bind it to the service-location group.
      
      
      ```
      [~NAT64] service-instance-group instance-group1
      ```
      ```
      [*NAT64-instance-group-instance-group1] service-location 1
      ```
      ```
      [*NAT64-instance-group-instance-group1] commit
      ```
      ```
      [~NAT64-instance-group-instance-group1] quit
      ```
   4. Configure a NAT64 instance and bind the service-instance group to the NAT64 instance so that the NAT64 instance is bound to the NAT service boards.
      
      
      ```
      [~NAT64] nat64 instance nat1 id 1
      ```
      ```
      [*NAT64-nat64-instance-nat1] service-instance-group instance-group1
      ```
      ```
      [*NAT64-nat64-instance-nat1] commit
      ```
      ```
      [~NAT64-nat64-instance-nat1] quit
      ```
   5. Configure a NAT64 public address pool, with addresses ranging from 1.1.1.1 to 1.1.1.5.
      
      
      ```
      [~NAT64] nat64 instance nat1 id 1
      ```
      
      
      ```
      [*NAT64-nat64-instance-nat1] nat64 address-group address-group1 group-id 1
      ```
      ```
      [*NAT64-nat64-instance-nat1-nat64-address-group-address-group1] section 1 1.1.1.1 1.1.1.5
      ```
      ```
      [*NAT64-nat64-instance-nat1-nat64-address-group-address-group1] commit
      ```
      ```
      [~NAT64-nat64-instance-nat1-nat64-address-group-address-group1] quit
      ```
   6. Configure a NAT64 IPv6 prefix of 64:FF9B::/96. This prefix must be the same as the prefix of the DNS64 server.
      
      
      ```
      [~NAT64] nat64 instance nat1 id 1
      ```
      
      
      ```
      [*NAT64-nat64-instance-nat1] nat64 prefix 64:FF9B:: prefix-length 96 1
      ```
      ```
      [*NAT64-nat64-instance-nat1] commit
      ```
      ```
      [~NAT64-nat64-instance-nat1] quit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This IPv6 prefix is set according to a standard. The prefix of the DNS64 server must be the same as the IPv6 prefix.
2. Configure the internal NAT64 server function.
   
   
   ```
   [~NAT64] nat64 instance nat1 id 1
   ```
   
   
   ```
   [*NAT64-nat64-instance-nat1] nat64 server global 1.1.1.10 inside 2001:db8::1:1112 prefix-id 1
   ```
   ```
   [*NAT64-nat64-instance-nat1] commit
   ```
   ```
   [~NAT64-nat64-instance-nat1] quit
   ```
3. Configure an address for the interface on the private network side.
   
   
   ```
   [~NAT64] interface GigabitEthernet0/2/1
   ```
   ```
   [*NAT64-GigabitEthernet0/2/1] ipv6 enable
   ```
   ```
   [*NAT64-GigabitEthernet0/2/1] ipv6 address 2001:db8::1:110e 96
   ```
   ```
   [*NAT64-GigabitEthernet0/2/1] commit
   ```
   ```
   [~NAT64-GigabitEthernet0/2/1] quit
   ```
4. Verify the configuration.
   
   
   
   # Display the NAT64 Server information.
   
   ```
   <NAT64> display nat server-map
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...             
   Slot: 3                                                              
   Total number:  2.                                                               
     NAT64 Instance: nat1                                                          
     Protocol:ANY, VPN:--->-                                                       
     Server reverse:ANY->1.1.1.10[2001:DB8::1:1112]                            
     Tag:0x0, TTL:-, Left-Time:-                                                   
     CPE IP:2001:DB8::1:1111                                                       
     outbound: false                                                               
     prefixId: 1                                                                   
   
     NAT64 Instance: nat1                                                          
     Protocol:ANY, VPN:--->-                                                       
     Server:[2001:DB8::1:1112][1.1.1.10]->ANY                                  
     Tag:0x0, TTL:-, Left-Time:-                                                   
     CPE IP:2001:DB8::1:1111                                                       
     outbound: false                                                               
     prefixId: 1          
   ```

#### Configuration File

```
#
sysname NAT64
#
vsm on-board-mode disable
#
license
 active nat session-table size 16 slot 1
 active nat session-table size 16 slot 2 
 active nat64 vsuf slot 1
 active nat64 vsuf slot 2
#
service-location 1
 location slot 3
#
service-instance-group instance-group1
 service-location 1
#
nat64 instance nat1 id 1
 service-instance-group instance-group1
 nat64 address-group address-group1 group-id 1 
  section 1 1.1.1.1 1.1.1.5
 nat64 prefix 64:FF9B:: prefix-length 96 1
 nat64 server global 1.1.1.10 inside 2001:db8::1:1112 prefix-id 1
#
interface GigabitEthernet0/2/1
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8::1:110e 96
#
return
```