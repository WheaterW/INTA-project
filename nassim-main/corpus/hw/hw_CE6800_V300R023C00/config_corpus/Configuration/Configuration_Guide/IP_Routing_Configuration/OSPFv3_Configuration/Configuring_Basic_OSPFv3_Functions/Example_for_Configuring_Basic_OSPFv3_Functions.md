Example for Configuring Basic OSPFv3 Functions
==============================================

Example for Configuring Basic OSPFv3 Functions

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176742683__fig_dc_vrp_ospfv3_cfg_206301), OSPFv3 runs on all devices and the entire AS is divided into three areas. DeviceB and DeviceC function as ABRs to forward inter-area routes. After the configuration is complete, each device should learn the routes to all IPv6 prefixes in the AS.

**Figure 1** Network diagram of configuring basic OSPFv3 functions![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176742769.png)

#### Precautions

Note the following during the configuration:

* The backbone area is responsible for forwarding inter-area routes. In addition, the routing information between non-backbone areas must be forwarded through the backbone area. OSPFv3 defines the following rules for the backbone area:
  
  + Connectivity must be available between non-backbone areas and the backbone area.
  + Connectivity must be available over the backbone area.
* The intervals at which Hello, Dead, and Poll packets are sent on the local interface must be the same as those intervals on the remote interface. Otherwise, the OSPFv3 neighbor relationship cannot be established.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic OSPFv3 functions on each device.
2. Specify IPv6 links in different areas.
3. Configure ciphertext authentication mode for the OSPFv3 area.

#### Procedure

1. Assign an IPv6 address to each interface.
   
   
   
   Assign an IPv6 address to each interface involved according to [Figure 1](#EN-US_TASK_0000001176742683__fig_dc_vrp_ospfv3_cfg_206301). For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176742683__postreq15335648163219).
2. Configure basic OSPFv3 functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] interface 100ge1/0/3
   [*DeviceA-100GE1/0/3] ospfv3 1 area 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge1/0/2
   [*DeviceA-100GE1/0/2] ospfv3 1 area 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] interface 100ge1/0/1
   [*DeviceB-100GE1/0/1] ospfv3 1 area 0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge1/0/2
   [*DeviceB-100GE1/0/2] ospfv3 1 area 1
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] interface 100ge1/0/1
   [*DeviceC-100GE1/0/1] ospfv3 1 area 0
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
   [*DeviceD-ospfv3-1] quit
   [*DeviceD] interface 100ge1/0/2
   [*DeviceD-100GE1/0/2] ospfv3 1 area 2
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```
3. Configure ciphertext authentication mode for the OSPFv3 area.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] area 0.0.0.1
   [*DeviceA-ospfv3-1-area-0.0.0.0] authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [*DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] area 0.0.0.1
   [*DeviceB-ospfv3-1-area-0.0.0.0] authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB] commit
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Device B and Device A must be configured with the same password. Otherwise, the neighbor relationship cannot be established.

#### Verifying the Configuration

# Check information about the OSPFv3 neighbors of DeviceB. If the neighbor relationships are in the Full state, the neighbor relationships are established successfully.

```
[~DeviceB] display ospfv3 peer
   OSPFv3 Process (1)
   Total number of peer(s): 2
    Peer(s) in full state: 2
   OSPFv3 Area (0.0.0.1)
   Neighbor ID    Pri   State       Dead Time   Interface               Instance ID
   1.1.1.1        1     Full/ -     00:00:34    100GE1/0/2               0

   OSPFv3 Area (0.0.0.0)
   Neighbor ID    Pri   State       Dead Time   Interface               Instance ID
   3.3.3.3        1     Full/ -     00:00:32    100GE1/0/1               0
```

# Check information about the OSPFv3 neighbors of DeviceC.

```
[~DeviceC] display ospfv3 peer
   OSPFv3 Process (1)
   Total number of peer(s): 2
    Peer(s) in full state: 2
   OSPFv3 Area (0.0.0.0)
   Neighbor ID    Pri   State       Dead Time   Interface                Instance ID
   2.2.2.2        1     Full/ -     00:00:37    100GE1/0/1                0

   OSPFv3 Area (0.0.0.2)
   Neighbor ID    Pri   State       Dead Time   Interface                Instance ID
   4.4.4.4        1     Full/ -     00:00:33    100GE1/0/2                0
```

# Check the OSPFv3 routing table of DeviceD.

```
[~DeviceD] display ospfv3 routing
OSPFv3 Process (1)

   Destination                                   Metric
     Next-hop
  IA 2001:DB8:1::/64                                     2
           via FE80::1572:0:5EF4:1, 100GE1/0/2
  IA 2001:DB8:2::/64                                     3
           via FE80::1572:0:5EF4:1, 100GE1/0/2
     2001:DB8:3::/64                                     1
           directly-connected, 100GE1/0/2
  IA 2001:DB8:4::/64                                     4
           via FE80::1572:0:5EF4:1, 100GE1/0/2
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ospfv3 1 area 0.0.0.1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   ospfv3 1 area 0.0.0.1
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.1
   authentication-mode hmac-sha256 key-id 1 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%#
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
   ipv6 address 2001:db8:1::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   ospfv3 1 area 0.0.0.1
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
   area 0.0.0.1
   authentication-mode hmac-sha256 key-id 1 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%#
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   ospfv3 1 area 0.0.0.2
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0
   area 0.0.0.2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
   ospfv3 1 area 0.0.0.2
  #
  ospfv3 1
   router-id 4.4.4.4
   area 0.0.0.2
  #
  return
  ```