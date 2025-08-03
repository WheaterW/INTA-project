Example for Configuring Basic RIPng Functions
=============================================

Example for Configuring Basic RIPng Functions

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176744259__fig_dc_vrp_ripng_cfg_002701), RIPng must be enabled on all interfaces of DeviceA, DeviceB, DeviceC, and DeviceD, and these interfaces are interconnected through RIPng.

**Figure 1** Network diagram of basic RIPng function configuration![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176744279.png)

#### Precautions

During the configuration, note the following:

* RIPng takes effect on an interface only after IPv6 is enabled.
* If a RIPng process is bound to a VPN instance, the interfaces running the RIPng process are also bound to the VPN instance.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface to ensure network connectivity.
2. Enable RIPng and configure basic RIPng functions on each device.

#### Procedure

1. Assign an IPv6 address to each interface.
2. Configure basic RIPng functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ripng 1
   [*DeviceA-ripng-1] quit
   [*DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ripng 1 enable
   [*DeviceA-ripng-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ripng 1
   [*DeviceB-ripng-1] quit
   [*DeviceB] interface 100ge1/0/1
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ripng 1 enable
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge1/0/2
   [*DeviceB-100GE1/0/2] ipv6 enable
   [*DeviceB-100GE1/0/2] ripng 1 enable
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge1/0/3
   [*DeviceB-100GE1/0/3] ipv6 enable
   [*DeviceB-100GE1/0/3] ripng 1 enable
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ripng 1
   [*DeviceC-ripng-1] quit
   [*DeviceC] interface 100ge1/0/2
   [*DeviceC-100GE1/0/2] ipv6 enable
   [*DeviceC-100GE1/0/2] ripng 1 enable
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ripng 1
   [*DeviceD-ripng-1] quit
   [*DeviceD] interface 100ge1/0/3
   [*DeviceD-100GE1/0/3] ipv6 enable
   [*DeviceD-100GE1/0/3] ripng 1 enable
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Check neighbor relationships of DeviceA.

```
[~DeviceA] display ripng 1 neighbor

Neighbor : FE80::A0A:201:1 100GE1/0/1
Protocol : RIPNG
```

The command output shows that DeviceA has established neighbor relationships with other devices on the network.

# Check routing information of DeviceB.

```
[~DeviceB] display ripng 1 route
Route Flags: A - Aging, S - Suppressed, G - Garbage-collect
-----------------------------------------------------------
Peer FE80::F54C:0:9FDB:1  on 100GE1/0/1
Dest 2001:DB8:1::1/96,
    via FE80::F54C:0:9FDB:1, cost  1, tag 0, A, 3 Sec
Peer FE80::D472:0:3C23:1  on 100GE1/0/2
Dest 2001:DB8:2::2/96,
    via FE80::D472:0:3C23:1, cost  1, tag 0, A, 4 Sec
Peer FE80::D472:0:3C23:1  on 100GE1/0/3
Dest 2001:DB8:3::2/96,
    via FE80::D472:0:3C23:1, cost  1, tag 0, A, 4 Sec
```

The command output shows that DeviceB has learned routing information on the network.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/96
   ripng 1 enable
  #
  ripng 1
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
   ipv6 address 2001:db8:1::2/96
   ripng 1 enable
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/96
   ripng 1 enable
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/96
   ripng 1 enable
  #
  ripng 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/96
   ripng 1 enable
  #
  ripng 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/96
   ripng 1 enable
  #
  ripng 1
  #
  return
  ```