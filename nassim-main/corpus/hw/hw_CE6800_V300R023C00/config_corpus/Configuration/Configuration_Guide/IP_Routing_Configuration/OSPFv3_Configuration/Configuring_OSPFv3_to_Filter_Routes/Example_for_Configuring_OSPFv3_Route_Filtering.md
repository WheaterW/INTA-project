Example for Configuring OSPFv3 Route Filtering
==============================================

Example for Configuring OSPFv3 Route Filtering

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001608937697__fig_dc_vrp_ospf_cfg_009401), DeviceA, DeviceB, DeviceC, DeviceD and DeviceE run OSPFv3 to implement interworking, and DeviceE and DeviceF run RIPng to implement interworking. OSPFv3 and RIPng are configured to import routes from each other on DeviceE so that all Devices can communicate with each other. PC1 is connected to the network through DeviceC; PC2 and PC3 are connected to the network through DeviceD; PC4 and PC5 are connected to the network through DeviceF. The requirements are as follows:

* Configure DeviceE to filter imported routes so that the network segment where PC4 resides cannot access PC1, PC2, or PC3.
* Configure route filtering on DeviceC so that the network segment where PC1 resides cannot access PC2.
* Configure route filtering on DeviceD so that the network segment where PC2 resides and the network segment where PC3 resides cannot access PC5.

**Figure 1** Network diagram of configuring OSPFv3 route filtering![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001558098598.png)

#### Precautions

Note the following during the configuration:

* Router IDs must be manually specified during OSPFv3 configuration.
* During route filtering, the keyword **export** filters the imported external routes to be advertised and takes effect only on ASBRs.
* The route filtering function filters the routing information in the routing table rather than the LSAs advertised by OSPFv3.
* Route communication is bidirectional. After a destination network segment is filtered out through the route filtering function, other network segments connected to the device cannot access the devices on the destination network segment, and nor can the devices on the destination network segment access the devices on the source network segment.
* If an ACL is used to filter routes, its last rule must be configured to permit all source addresses; otherwise, all network segment routes may be filtered out.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable OSPFv3 or RIPng on each device according to the networking diagram.
2. Configure OSPFv3 and RIPng to import routes from each other.
3. Configure ACLv6 rules and route filtering.

#### Procedure

1. Assign an IPv6 address to each interface. For detailed configurations, see Configuration Scripts.
2. Configure basic OSPFv3 functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   [*DeviceA-ospfv3-1] area 0
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   [*DeviceA-ospfv3-1] area 1
   [*DeviceA-ospfv3-1-area-0.0.0.1] quit
   [*DeviceA-ospfv3-1] area 2
   [*DeviceA-ospfv3-1-area-0.0.0.2] quit
   [*DeviceA] interface 100ge1/0/1 
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0 
   [*DeviceA-100GE1/0/1] quit 
   [*DeviceA] interface 100ge1/0/2 
   [*DeviceA-100GE1/0/2] ospfv3 1 area 2
   [*DeviceA-100GE1/0/2] quit 
   [*DeviceA] interface 100ge1/0/3 
   [*DeviceA-100GE1/0/3] ospfv3 1 area 1
   [*DeviceA-100GE1/0/3] quit 
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   [*DeviceB-ospfv3-1] area 0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] area 3
   [*DeviceB-ospfv3-1-area-0.0.0.3] quit
   [*DeviceB] interface 100ge1/0/1 
   [*DeviceB-100GE1/0/1] ospfv3 1 area 0 
   [*DeviceB-100GE1/0/1] quit 
   [*DeviceB] interface 100ge1/0/2 
   [*DeviceB-100GE1/0/2] ospfv3 1 area 3
   [*DeviceB-100GE1/0/2] quit 
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   [*DeviceC-ospfv3-1] area 2
   [*DeviceC-ospfv3-1-area-0.0.0.2] quit
   [*DeviceC] interface 100ge1/0/1 
   [*DeviceC-100GE1/0/1] ospfv3 1 area 2
   [*DeviceC-100GE1/0/1] quit 
   [*DeviceC] interface 100ge1/0/2 
   [*DeviceC-100GE1/0/2] ospfv3 1 area 2
   [*DeviceC-100GE1/0/2] quit 
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ospfv3 1
   [*DeviceD-ospfv3-1] router-id 4.4.4.4
   [*DeviceD-ospfv3-1] area 3
   [*DeviceD-ospfv3-1-area-0.0.0.3] quit
   [*DeviceD] interface 100ge1/0/1 
   [*DeviceD-100GE1/0/1] ospfv3 1 area 3 
   [*DeviceD-100GE1/0/1] quit 
   [*DeviceD] interface 100ge1/0/2 
   [*DeviceD-100GE1/0/2] ospfv3 1 area 3
   [*DeviceD-100GE1/0/2] quit 
   [*DeviceD] interface 100ge1/0/3 
   [*DeviceD-100GE1/0/3] ospfv3 1 area 3
   [*DeviceD-100GE1/0/3] quit 
   [*DeviceD] commit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] ospfv3 1
   [*DeviceE-ospfv3-1] router-id 5.5.5.5
   [*DeviceE-ospfv3-1] area 1
   [*DeviceE-ospfv3-1-area-0.0.0.1] quit
   [*DeviceE] interface 100ge1/0/1 
   [*DeviceE-100GE1/0/1] ospfv3 1 area 1 
   [*DeviceE-100GE1/0/1] quit 
   [*DeviceE] ripng 1
   [*DeviceE-ripng-1] quit
   [*DeviceE] interface 100ge1/0/2 
   [*DeviceE-100GE1/0/2] ripng 1 enable
   [*DeviceE-100GE1/0/2] quit 
   [*DeviceE] commit
   ```
   
   # Configure DeviceF.
   
   ```
   [~DeviceF] ripng 1
   [*DeviceF-ripng-1] quit
   [*DeviceF] interface 100ge1/0/1 
   [*DeviceF-100GE1/0/1] ripng 1 enable 
   [*DeviceF-100GE1/0/1] quit 
   [*DeviceF] interface 100ge1/0/2 
   [*DeviceF-100GE1/0/2] ripng 1 enable
   [*DeviceF-100GE1/0/2] quit 
   [*DeviceF] interface 100ge1/0/3 
   [*DeviceF-100GE1/0/3] ripng 1 enable
   [*DeviceF-100GE1/0/3] quit 
   [*DeviceF] commit
   ```
3. Configure OSPFv3 and RIPng to import routes from each other.
   
   
   ```
   [~DeviceE] ospfv3 1
   [*DeviceE-ospfv3-1] import-route direct
   [*DeviceE-ospfv3-1] import-route ripng 1
   [*DeviceE-ospfv3-1] quit
   [*DeviceE] ripng 1
   [*DeviceE-ripng-1] import-route direct
   [*DeviceE-ripng-1] import-route ospfv3 1
   [*DeviceE-ripng-1] quit
   [*DeviceE] commit
   ```
4. Configure ACLv6 rules and route filtering.
   
   
   
   # Configure DeviceE to filter imported routes so that the network segment where PC4 resides cannot access PC1, PC2, or PC3.
   
   
   
   ```
   [~DeviceE] acl ipv6 number 2000
   [*DeviceE-acl6-basic-2000] rule 0 deny source 2001:DB8:10:4::1 96
   [*DeviceE-acl6-basic-2000] rule 5 permit
   [*DeviceE-acl6-basic-2000] commit
   [~DeviceE-acl6-basic-2000] quit
   [~DeviceE] ospfv3 1
   [*DeviceE-ospfv3-1] filter-policy 2000 export ripng 1
   [*DeviceE-ospfv3-1] quit
   [*DeviceE] commit
   ```
   
   # Configure route filtering on DeviceC so that the network segment where PC1 resides cannot access PC2.
   
   ```
   [~DeviceC] acl ipv6 number 2000
   [*DeviceC-acl6-basic-2000] rule 0 deny source 2001:DB8:10:2::1 96
   [*DeviceC-acl6-basic-2000] rule 5 permit
   [*DeviceC-acl6-basic-2000] commit
   [~DeviceC-acl6-basic-2000] quit
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] filter-policy 2000 import
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] commit
   ```
   
   # Configure route filtering on DeviceD so that the network segment where PC2 resides and the network segment where PC3 resides cannot access PC5.
   
   ```
   [~DeviceD] acl ipv6 number 2000
   [*DeviceD-acl6-basic-2000] rule 0 deny source 2001:DB8:10:5::1 96
   [*DeviceD-acl6-basic-2000] rule 5 permit
   [*DeviceD-acl6-basic-2000] commit
   [~DeviceD-acl6-basic-2000] quit
   [~DeviceD] ospfv3 1
   [*DeviceD-ospfv3-1] filter-policy 2000 import
   [*DeviceD-ospfv3-1] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# On DeviceF, use the source address 2001:DB8:10:4::1 to ping destination addresses 2001:DB8:10:3::1, 2001:DB8:10:2::1, and 2001:DB8:10:1::1. The ping operations fail, indicating that the network segment where PC4 resides cannot access the network segments where PC1, PC2, and PC3 reside.

```
[~DeviceF] ping ipv6 -a 2001:DB8:10:4::1 2001:DB8:10:3::1
  PING 2001:DB8:10:3::1 : 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 2001:DB8:10:3::1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
    round-trip min/avg/max=0/0/0 ms
```
```
[~DeviceF] ping ipv6 -a 2001:DB8:10:4::1 2001:DB8:10:2::1
  PING 2001:DB8:10:2::1 : 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 2001:DB8:10:2::1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
    round-trip min/avg/max=0/0/0 ms
```
```
[~DeviceF] ping ipv6 -a 2001:DB8:10:4::1 2001:DB8:10:1::1
  PING 2001:DB8:10:1::1 : 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 2001:DB8:10:1::1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
    round-trip min/avg/max=0/0/0 ms
```

# On DeviceC, use the source address 2001:DB8:10:3::1 to ping the destination address 2001:DB8:10:2::1. The ping operation fails, indicating that the network segment where PC1 resides cannot access the network segment where PC2 resides.

```
[~DeviceC] ping ipv6 -a 2001:DB8:10:3::1 2001:DB8:10:2::1
  PING 2001:DB8:10:2::1 : 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 2001:DB8:10:2::1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
    round-trip min/avg/max=0/0/0 ms
```

# On DeviceD, use source addresses 2001:DB8:10:1::1 and 2001:DB8:10:2::1 to ping the destination address 2001:DB8:10:5::1. The ping operations fail, indicating that the network segment where PC2 resides and the network segment where PC3 resides cannot access PC5.

```
[~DeviceD] ping ipv6 -a 2001:DB8:10:1::1 2001:DB8:10:5::1
  PING 2001:DB8:10:5::1 : 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 2001:DB8:10:5::1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
    round-trip min/avg/max=0/0/0 ms
```
```
[~DeviceD] ping ipv6 -a 2001:DB8:10:2::1 2001:DB8:10:5::1
  PING 2001:DB8:10:5::1 : 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 2001:DB8:10:5::1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
    round-trip min/avg/max=0/0/0 ms
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::1/96
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::1/96
   ospfv3 1 area 0.0.0.2
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::1/96
   ospfv3 1 area 0.0.0.1
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
   area 0.0.0.1
   area 0.0.0.2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::2/96
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::1/96
   ospfv3 1 area 0.0.0.3
  #
  ospfv3 1 
   router-id 2.2.2.2
   area 0.0.0.0
   area 0.0.0.3
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  acl ipv6 number 2000   
   rule 0 deny source 2001:DB8:10:2::1/96
   rule 5 permit
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::2/96
   ospfv3 1 area 0.0.0.2
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:10:3::1/96
   ospfv3 1 area 0.0.0.2
  #
  ospfv3 1  
   router-id 3.3.3.3
   filter-policy 2000 import   
   area 0.0.0.2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  acl ipv6 number 2000   
   rule 0 deny source 2001:DB8:10:5::1/96
   rule 5 permit
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::2/96
   ospfv3 1 area 0.0.0.3
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:10:1::1/96
   ospfv3 1 area 0.0.0.3
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:10:2::1/96
   ospfv3 1 area 0.0.0.3
  #
  ospfv3 1    
   router-id 4.4.4.4
   filter-policy 2000 import    
   area 0.0.0.3
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  acl ipv6 number 2000   
   rule 0 deny source 2001:DB8:10:4::1/96
   rule 5 permit
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::2/96
   ospfv3 1 area 0.0.0.1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:5::1/96
   ripng 1 enable
  #
  ospfv3 1
   router-id 5.5.5.5
   import-route direct
   import-route ripng 1
   filter-policy 2000 export ripng 1
   area 0.0.0.1
  #
  ripng 1
   import-route direct 
   import-route ospfv3 1 
  #
  return
  ```
* DeviceF
  
  ```
  #
  sysname DeviceF
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:5::2/96
   ripng 1 enable
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:10:4::1/96
   ripng 1 enable
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:10:5::1/96
   ripng 1 enable
  #
  ripng 1
  #
  return
  ```