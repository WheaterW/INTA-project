Example for Configuring a Multi-Hop BFD Session for IPv6
========================================================

Example for Configuring a Multi-Hop BFD Session for IPv6

#### Networking Requirements

A multi-hop BFD session for IPv6 can be created to monitor an IPv6 link on a network for quick fault detection. In [Figure 1](#EN-US_TASK_0000001130782128__fig_dc_vrp_bfd_cfg_200701), BFD monitors the multi-hop link between DeviceA and DeviceC in asynchronous mode.

**Figure 1** Configuring multi-hop BFD for IPv6![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001130622374.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IPv6 addresses to interfaces on DeviceA, DeviceB, and DeviceC, and configure Open Shortest Path First version 3 (OSPFv3) to ensure that these devices can communicate with one another.
2. Enable BFD globally on DeviceA and DeviceC. Then, configure a multi-hop BFD session for IPv6 on DeviceA to detect the multi-hop link from DeviceA to DeviceC and one on DeviceC to detect the multi-hop link from DeviceC to DeviceA.


#### Procedure

1. Assign IPv6 addresses to interfaces on DeviceA, DeviceB, and DeviceC, and configure OSPFv3 to ensure that these devices can communicate with one another.# Configure DeviceA.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] router-id 10.1.1.1
   [*DeviceA-ospfv3-1] area 0
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1::1 64
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 10.1.1.2
   [*DeviceB-ospfv3-1] area 0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:1::2 64
   [*DeviceB-100GE1/0/1] ospfv3 1 area 0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ipv6 enable
   [*DeviceB-100GE1/0/2] ipv6 address 2001:db8:2::1 64
   [*DeviceB-100GE1/0/2] ospfv3 1 area 0
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] router-id 10.1.1.3
   [*DeviceC-ospfv3-1] area 0
   [*DeviceC-ospfv3-1-area-0.0.0.0] quit
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] commit
   [~DeviceC] interface 100ge 1/0/2
   [~DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ipv6 enable
   [*DeviceC-100GE1/0/2] ipv6 address 2001:db8:2::2 64
   [*DeviceC-100GE1/0/2] ospfv3 1 area 0
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
2. Enable BFD globally on DeviceA and DeviceC, and configure a multi-hop BFD session on each device.# Configure DeviceA.
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd ipv6session bind peer-ipv6 2001:db8:2::2
   [*DeviceA-bfd-session-ipv6session] discriminator local 1
   [*DeviceA-bfd-session-ipv6session] discriminator remote 2
   [*DeviceA-bfd-session-ipv6session] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   ```
   [~DeviceC] bfd
   [*DeviceC-bfd] quit
   [*DeviceC] bfd ipv6session bind peer-ipv6 2001:db8:1::1
   [*DeviceC-bfd-session-ipv6session] discriminator local 2
   [*DeviceC-bfd-session-ipv6session] discriminator remote 1
   [*DeviceC-bfd-session-ipv6session] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check that DeviceA and DeviceC can ping each other. The command output on DeviceA is used as an example.

```
[~DeviceA] ping ipv6 2001:db8:2::2
PING 2001:db8:2::2 : 56  data bytes, press CTRL_C to break
    Reply from 2001:db8:2::2
    bytes=56 Sequence=1 hop limit=64 time=22 ms
    Reply from 2001:db8:2::2
    bytes=56 Sequence=2 hop limit=64 time=1 ms
    Reply from 2001:db8:2::2
    bytes=56 Sequence=3 hop limit=64 time=1 ms
    Reply from 2001:db8:2::2
    bytes=56 Sequence=4 hop limit=64 time=1 ms

    Reply from 2001:db8:2::2
    bytes=56 Sequence=5 hop limit=64 time=1 ms
  ---2001:db8:2::2 ping statistics---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max=1/5/22 ms
```

# Check detailed BFD session information on DeviceA and DeviceC. The command output on DeviceA is used as an example.

```
[~DeviceA] display bfd session all verbose
2020-01-01 11:21:06.8
(w): State in WTR 
(*): State is invalid
Total UP/DOWN Session Number : 1/0
--------------------------------------------------------------------------------
  Name : ipv6session                    (Multiple Hops) State : Up                    
------------------------------------------------------------------------------
  Local Discriminator    : 1                Remote Discriminator   : 2
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Peer IP Address
  Bind Session Type      : Static
  Bind Peer IP Address   : 2001:DB8:2::2
  Bind Interface         : -
  FSM Board ID           : 1               TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000      Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 1000             Actual Rx Interval (ms): 1000
  WTR Interval (ms)      : -                Detect Interval (ms)   : 3000
  Local Detect Multi     : 3                Active Multi           : -
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 4784             TTL                    : 254
  Proc Interface Status  : Disable          Process PST            : Disable
  Config PST             : Disable
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : No Application Bind
  Session Description    : - 
------------------------------------------------------------------------------
```

The command output shows that a multi-hop BFD session has been established and is in the **Up** state.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  ospfv3 1
   router-id 10.1.1.1
   area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   ospfv3 1 area 0.0.0.0
  #
  bfd ipv6session bind peer-ipv6 2001:DB8:2::2
   discriminator local 1
   discriminator remote 2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1
   router-id 10.1.1.2
   area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  ospfv3 1
   router-id 10.1.1.3
   area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  bfd ipv6session bind peer-ipv6 2001:DB8:1::1
   discriminator local 2
   discriminator remote 1
  #
  return
  ```