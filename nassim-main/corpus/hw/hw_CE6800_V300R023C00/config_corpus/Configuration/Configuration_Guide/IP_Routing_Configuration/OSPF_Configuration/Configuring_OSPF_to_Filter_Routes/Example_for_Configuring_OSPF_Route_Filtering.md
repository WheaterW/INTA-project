Example for Configuring OSPF Route Filtering
============================================

Example for Configuring OSPF Route Filtering

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001535276928__fig_dc_vrp_ospf_cfg_009401), DeviceA, DeviceB, DeviceC, DeviceD and DeviceE run OSPF to implement interworking, and DeviceE and DeviceF run RIP to implement interworking. OSPF and RIP are configured to import routes from each other on DeviceE so that all Devices can communicate with each other. PC1 is connected to the network through DeviceC; PC2 and PC3 are connected to the network through DeviceD; PC4 and PC5 are connected to the network through DeviceF. The requirements are as follows:

* Configure DeviceE to filter imported routes so that the network segment where PC4 resides cannot access PC1, PC2, or PC3.
* Configure route filtering on DeviceC so that the network segment where PC1 resides cannot access PC2.
* Configure route filtering on DeviceD so that the network segment where PC2 resides and the network segment where PC3 resides cannot access PC5.

**Figure 1** Network diagram of configuring OSPF route filtering![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001535596636.png)

#### Precautions

During the configuration, note the following:

* During route filtering, the keyword **export** filters the imported external routes to be advertised and takes effect only on ASBRs.
* The route filtering function filters the routing information in the routing table rather than the LSAs advertised by OSPF.
* Route communication is bidirectional. After a destination network segment is filtered out through the route filtering function, other network segments connected to the device cannot access the devices on the destination network segment, and nor can the devices on the destination network segment access the devices on the source network segment.
* If an ACL is used to filter routes, its last rule must be configured to permit all source addresses; otherwise, all network segment routes may be filtered out.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable OSPF or RIP on each device according to the networking diagram.
2. Configure OSPF and RIP to import routes from each other.
3. Configure ACL rules and route filtering.

#### Procedure

1. Assign an IP address to each interface. For detailed configurations, see Configuration Scripts.
2. Configure basic OSPF functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] router id 1.1.1.1
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] area 1
   [*DeviceA-ospf-1-area-0.0.0.1] network 10.4.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.1] quit
   [*DeviceA-ospf-1] area 2
   [*DeviceA-ospf-1-area-0.0.0.2] network 10.2.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.2] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] router id 2.2.2.2
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] area 3
   [*DeviceB-ospf-1-area-0.0.0.3] network 10.3.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.3] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] router id 3.3.3.3
   [*DeviceC] ospf 1
   [*DeviceC-ospf-1] area 2
   [*DeviceC-ospf-1-area-0.0.0.2] network 10.2.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.2] network 10.10.3.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.2] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] router id 4.4.4.4
   [*DeviceD] ospf 1
   [*DeviceD-ospf-1] area 3
   [*DeviceD-ospf-1-area-0.0.0.3] network 10.3.1.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.3] network 10.10.1.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.3] network 10.10.2.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.3] quit
   [*DeviceD-ospf-1] quit
   [*DeviceD] commit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] router id 5.5.5.5
   [*DeviceE] ospf 1
   [*DeviceE-ospf-1] area 1
   [*DeviceE-ospf-1-area-0.0.0.1] network 10.4.1.0 0.0.0.255
   [*DeviceE-ospf-1-area-0.0.0.1] quit
   [*DeviceE-ospf-1] quit
   [*DeviceE] commit
   [~DeviceE] rip 1
   [*DeviceE-rip-1] network 10.0.0.0
   [*DeviceE-rip-1] version 2
   [*DeviceE-rip-1] quit
   [*DeviceE] commit
   ```
   
   # Configure DeviceF.
   
   ```
   [~DeviceF] rip 1
   [*DeviceF-rip-1] network 10.0.0.0
   [*DeviceF-rip-1] network 172.16.0.0
   [*DeviceF-rip-1] network 192.168.1.0
   [*DeviceF-rip-1] version 2
   [*DeviceF-rip-1] quit
   [*DeviceF] commit
   ```
3. Configure OSPF and RIP to import routes from each other.
   
   
   ```
   [~DeviceE] ospf 1
   [*DeviceE-ospf-1] import-route direct
   [*DeviceE-ospf-1] import-route rip 1
   [*DeviceE-ospf-1] quit
   [*DeviceE] rip 1
   [*DeviceE-rip-1] import-route direct
   [*DeviceE-rip-1] import-route ospf 1
   [*DeviceE-rip-1] quit
   [*DeviceE] commit
   ```
4. Configure ACL rules and route filtering.
   
   
   
   # Configure DeviceE to filter imported routes so that the network segment where PC4 resides cannot access PC1, PC2, or PC3.
   
   
   
   ```
   [~DeviceE] acl number 2000
   [*DeviceE-acl4-basic-2000] rule 0 deny source 172.16.1.0 0.0.0.255
   [*DeviceE-acl4-basic-2000] rule 5 permit
   [*DeviceE-acl4-basic-2000] commit
   [~DeviceE-acl4-basic-2000] quit
   [~DeviceE] ospf 1
   [*DeviceE-ospf-1] filter-policy 2000 export rip 1
   [*DeviceE-ospf-1] quit
   [*DeviceE] commit
   ```
   
   # Configure route filtering on DeviceC so that the network segment where PC1 resides cannot access PC2.
   
   ```
   [~DeviceC] acl number 2000
   [*DeviceC-acl4-basic-2000] rule 0 deny source 10.10.2.0 0.0.0.255
   [*DeviceC-acl4-basic-2000] rule 5 permit
   [*DeviceC-acl4-basic-2000] commit
   [~DeviceC-acl4-basic-2000] quit
   [~DeviceC] ospf 1
   [*DeviceC-ospf-1] filter-policy 2000 import
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   # Configure route filtering on DeviceD so that the network segment where PC2 resides and the network segment where PC3 resides cannot access PC5.
   
   ```
   [~DeviceD] acl number 2000
   [*DeviceD-acl4-basic-2000] rule 0 deny source 192.168.1.0 0.0.0.255
   [*DeviceD-acl4-basic-2000] rule 5 permit
   [*DeviceD-acl4-basic-2000] commit
   [~DeviceD-acl4-basic-2000] quit
   [~DeviceD] ospf 1
   [*DeviceD-ospf-1] filter-policy 2000 import
   [*DeviceD-ospf-1] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# On DeviceF, use the source address 172.16.1.1 to ping the destination addresses 10.10.3.1, 10.10.2.1, and 10.10.1.1. The ping operations fail, indicating that the network segment where PC4 resides cannot access the network segments where PC1, PC2, and PC3 reside.

```
[~DeviceF] ping -a 172.16.1.1 10.10.3.1
  PING 10.10.3.1: 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 10.10.3.1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
```
```
[~DeviceF] ping -a 172.16.1.1 10.10.2.1
  PING 10.10.2.1: 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 10.10.2.1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
```
```
[~DeviceF] ping -a 172.16.1.1 10.10.1.1
  PING 10.10.1.1: 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 10.10.1.1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
```

# On DeviceC, use the source address 10.10.3.1 to ping the destination address 10.10.2.1. The ping operation fails, indicating that the network segment where PC1 resides cannot access the network segment where PC2 resides.

```
[~DeviceC] ping -a 10.10.3.1 10.10.2.1
  PING 10.10.2.1: 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 10.10.2.1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
```

# On DeviceD, use the source addresses 10.10.1.1 and 10.10.2.1 to ping the destination address 192.168.1.1. The ping operations fail, indicating that the network segment where PC2 resides and the network segment where PC3 resides cannot access PC5.

```
[~DeviceD] ping -a 10.10.1.1 192.168.1.1
  PING 192.168.1.1: 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 192.168.1.1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
```
```
[~DeviceD] ping -a 10.10.2.1 192.168.1.1
  PING 192.168.1.1: 56  data bytes, press CTRL_C to break
    Request time out
    Request time out
    Request time out
    Request time out
    Request time out

  --- 192.168.1.1 ping statistics ---
    5 packet(s) transmitted
    0 packet(s) received
    100.00% packet loss
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  router id 1.1.1.1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.4.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
   area 0.0.0.1
    network 10.4.1.0 0.0.0.255
   area 0.0.0.2
    network 10.2.1.0 0.0.0.255
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  router id 2.2.2.2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.3.1.1 255.255.255.0
  #
  ospf 1 
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
   area 0.0.0.3
    network 10.3.1.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  acl number 2000   
   rule 0 deny source 10.10.2.0 0.0.0.255
   rule 5 permit
  #
  router id 3.3.3.3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.2.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.10.3.1 255.255.255.0
  #
  ospf 1  
   filter-policy 2000 import   
   area 0.0.0.2
    network 10.2.1.0 0.0.0.255
    network 10.10.3.0 0.0.0.255
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  acl number 2000   
   rule 0 deny source 192.168.1.0 0.0.0.255
   rule 5 permit
  #
  router id 4.4.4.4
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.3.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.10.1.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.10.2.1 255.255.255.0
  #
  ospf 1    
   filter-policy 2000 import    
   area 0.0.0.3
    network 10.3.1.0 0.0.0.255
    network 10.10.1.0 0.0.0.255
    network 10.10.2.0 0.0.0.255
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  router id 5.5.5.5
  #
  acl number 2000   
   rule 0 deny source 172.16.1.0 0.0.0.255
   rule 5 permit
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.4.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.5.1.1 255.255.255.0
  #
  ospf 1
   import-route direct
   import-route rip 1
   filter-policy 2000 export rip 1
   area 0.0.0.1
    network 10.4.1.0 0.0.0.255
  #
  rip 1
   version 2
   network 10.0.0.0
   import-route direct 
   import-route ospf 1 
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
   ip address 10.5.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  rip 1 
   version 2
   network 10.0.0.0
   network 172.16.0.0
   network 192.168.1.0
  #
  return
  ```