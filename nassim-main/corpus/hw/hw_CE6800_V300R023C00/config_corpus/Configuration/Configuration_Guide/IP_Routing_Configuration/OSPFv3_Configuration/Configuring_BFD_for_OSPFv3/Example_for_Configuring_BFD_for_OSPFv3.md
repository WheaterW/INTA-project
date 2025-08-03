Example for Configuring BFD for OSPFv3
======================================

Example for Configuring BFD for OSPFv3

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176742713__en-us_task_0275858002_fig_dc_vrp_ospfv3_cfg_206901):

* OSPFv3 runs on DeviceA, DeviceB, and DeviceC.
* BFD is enabled in an OSPFv3 process on each of DeviceA, DeviceB, and DeviceC.
* Service traffic is transmitted over the primary link (DeviceA -> DeviceB). The link (DeviceA -> DeviceC -> DeviceB) functions as the backup link.
* If the primary link fails, BFD can quickly detect the fault and notify OSPFv3 of the fault so that service traffic can be transmitted through the backup link.

**Figure 1** Network diagram of configuring BFD for OSPFv3![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001184761434.png)

#### Precautions

To improve security, you are advised to deploy OSPFv3 authentication. For details, see "Configuring OSPFv3 Authentication." OSPFv3 area authentication is used as an example. For details, see "Example for Configuring Basic OSPFv3 Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic OSPFv3 functions on each device.
2. Configure BFD for OSPFv3.

#### Procedure

1. Assign an IPv6 address to each interface involved. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176742713__en-us_task_0275858002_postreq1488919183427).
2. Configure basic OSPFv3 functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge1/0/2
   [*DeviceA-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] interface 100ge1/0/1
   [*DeviceB-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge1/0/2
   [*DeviceB-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge1/0/3
   [*DeviceB-100GE1/0/3] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] interface 100ge1/0/1
   [*DeviceC-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge1/0/2
   [*DeviceC-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
   
   # After the preceding configurations are complete, run the [**display ospfv3 peer**](cmdqueryname=display+ospfv3+peer) command. This example uses DeviceA. The command output shows that neighbor relationships are set up.
   
   ```
   [~DeviceA] display ospfv3 peer
   OSPFv3 Process (1)
   Total number of peer(s): 2
    Peer(s) in full state: 1
    OSPFv3 Area (0.0.0.0)
   Neighbor ID      Pri State            Dead Time  Interface          Instance ID
   2.2.2.2            1 Full/DR          00:00:38   100GE1/0/1              0
   3.3.3.3            1 Init/-           00:00:37   100GE1/0/2              0
   ```
   
   # Check the OSPFv3 routing table of DeviceA. The routing table should contain the routes to DeviceB and DeviceC.
   
   ```
   [~DeviceA] display ospfv3 routing
   Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
           N - NSSA
   Flags : A - Added to URT6, LT - Locator Routing
   
   OSPFv3 Process (1)
        Destination                                                         Metric
     Next-hop
        2001:DB8:1::/64                                                          1
          directly connected, 100GE1/0/1, Flags : A
        2001:DB8:2::/64                                                          2
          via FE80::3AE9:7BFF:FE31:307, 100GE1/0/2, Flags : A
          via FE80::3AE9:7BFF:FE21:300, 100GE1/0/1, Flags : A
        2001:DB8:3::/64                                                          1
          directly connected, 100GE1/0/2, Flags : A
        2001:DB8:4::1/64                                                         1
          via FE80::3AE9:7BFF:FE21:300, 100GE1/0/1
   ```
   
   The command output shows that the next hop of the route to 2001:DB8:4::1/64 is 100GE 1/0/1. Traffic is transmitted over the primary link DeviceA -> DeviceB.
3. Configure BFD for OSPFv3.
   
   
   
   # Enable BFD on DeviceA globally.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] bfd all-interfaces enable
   [*DeviceA-ospfv3-1] bfd all-interfaces min-transmit-interval 100 min-receive-interval 100 detect-multiplier 4
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] commit
   ```
   
   # Enable BFD on DeviceB globally.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] bfd all-interfaces enable
   [*DeviceB-ospfv3-1] bfd all-interfaces min-transmit-interval 100 min-receive-interval 100 detect-multiplier 4
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] commit
   ```
   
   # Enable BFD on DeviceC globally.
   
   ```
   [~DeviceC] bfd
   [*DeviceC-bfd] quit
   [*DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] bfd all-interfaces enable
   [*DeviceC-ospfv3-1] bfd all-interfaces min-transmit-interval 100 min-receive-interval 100 detect-multiplier 4
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# After the preceding configurations are complete, run the [**display ospfv3 bfd session**](cmdqueryname=display+ospfv3+bfd+session) command on DeviceA or DeviceB. You can view that the status of the BFD session is **Up**.

This example uses DeviceB.

```
[~DeviceB] display ospfv3 bfd session  - STALE
* - STALE

OSPFv3 Process (1)

 Neighbor-Id      Interface                       BFD-Status
 1.1.1.1          100GE1/0/1                        Up
 3.3.3.3          100GE1/0/2                        Up
```

# Run the [**shutdown**](cmdqueryname=shutdown) command on 100GE 1/0/1 of DeviceB to simulate a primary link failure.

```
[~DeviceB] interface 100ge1/0/1
[~DeviceB-100GE1/0/1] shutdown
[*DeviceB-100GE1/0/1] commit
```

# Check the routing table on DeviceA. The command output shows that the next hop of the route to 2001:DB8:4::1/64 is changed to 100GE 1/0/2 after the primary link fails, and traffic is switched to the backup link.

```
[~DeviceA] display ospfv3 routing
Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
        N - NSSA
Flags : A - Added to URT6, LT - Locator Routing

OSPFv3 Process (1)
     Destination                                                         Metric
  Next-hop
     2001:DB8:2::/64                                                          2
       via FE80::3AE9:7BFF:FE31:307, 100GE1/0/2, Flags : A
     2001:DB8:3::/64                                                          1
       directly connected, 100GE1/0/2, Flags : A
     2001:DB8:4::/64                                                          3
       via FE80::3AE9:7BFF:FE31:307, 100GE1/0/2, Flags : A
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
   bfd
  #
  ospfv3 1
   router-id 1.1.1.1
   bfd all-interfaces enable
   bfd all-interfaces min-transmit-interval 100 min-receive-interval 100 detect-multiplier 4
   area 0.0.0.0
  #
  interface 100GE1/0/1 
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::3/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
   bfd
  #
  ospfv3 1
   router-id 2.2.2.2
   bfd all-interfaces enable
   bfd all-interfaces min-transmit-interval 100 min-receive-interval 100 detect-multiplier 4
   area 0.0.0.0
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
   ipv6 address 2001:db8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  ospfv3 1
   router-id 3.3.3.3
   bfd all-interfaces enable
   bfd all-interfaces min-transmit-interval 100 min-receive-interval 100 detect-multiplier 4
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::3/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```