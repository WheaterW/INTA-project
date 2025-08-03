Example for Configuring Basic IPv6 IS-IS Functions
==================================================

Example for Configuring Basic IPv6 IS-IS Functions

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176742093__fig_dc_vrp_isis_cfg_008901), Devices A, B, C, and D belong to the same AS. It is required that IPv6 IS-IS run on them to implement IPv6 interworking.

* Devices A, B, and C belong to area 10, and DeviceD belongs to area 20.
* DeviceA and DeviceB are Level-1 devices; DeviceC is a Level-1-2 device; DeviceD is a Level-2 device.

**Figure 1** Network diagram of basic IPv6 IS-IS functions![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176742135.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 on each device and configure an IPv6 address for each interface.
2. Enable IS-IS, set a level, and set a NET for each device.

#### Procedure

1. Enable IPv6 on each device and configure an IPv6 address for each interface.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1::2 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176742093__postreq24192593172748).
2. Enable IS-IS, set a level, and set a NET for each device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-1
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] ipv6 enable
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis ipv6 enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1 
   [*DeviceB-isis-1] is-level level-1
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   [*DeviceB-isis-1] ipv6 enable
   [*DeviceB-isis-1] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] isis ipv6 enable 1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 1
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   [*DeviceC-isis-1] ipv6 enable
   [*DeviceC-isis-1] quit
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] isis ipv6 enable 1
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] isis ipv6 enable 1
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] isis ipv6 enable 1
   [*DeviceC-100GE1/0/3] isis circuit-level level-2
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 1 
   [*DeviceD-isis-1] is-level level-2
   [*DeviceD-isis-1] network-entity 20.0000.0000.0004.00
   [*DeviceD-isis-1] ipv6 enable
   [*DeviceD-isis-1] quit
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] isis ipv6 enable 1
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] isis ipv6 enable 1
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Check the IS-IS routing table of DeviceA.

```
[~DeviceA] display isis route

                         Route information for ISIS(1)
                         -----------------------------

                        ISIS(1) Level-1 Forwarding Table
                        --------------------------------

IPV6 Dest.         ExitInterface                 NextHop                  Cost         Flags
----------------------------------------------------------------------------------------
 ::/0              100GE1/0/1          FE80::A83E:0:3ED2:1      10           A/-/-
 2001:db8:1::/64   100GE1/0/1          Direct                   10           D/L/-
 2001:db8:2::/64   100GE1/0/1          FE80::A83E:0:3ED2:1      20           A/-/-

     Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                 U-Up/Down Bit Set
```

The command output shows that DeviceA has the routes to each network segment of the Level-1 area.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  isis 1
   is-level level-1
   ipv6 enable topology standard
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   isis ipv6 enable 1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   is-level level-1
   ipv6 enable topology standard
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   isis ipv6 enable 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  isis 1
   ipv6 enable topology standard
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   isis ipv6 enable 1
   isis circuit-level level-2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  isis 1
   is-level level-2
   ipv6 enable topology standard
   network-entity 20.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   isis ipv6 enable 1
  #
  return
  ```