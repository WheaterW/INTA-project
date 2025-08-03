Example for Configuring a BFD Session for IPv6 with Automatically Negotiated Discriminators
===========================================================================================

Example for Configuring a BFD Session for IPv6 with Automatically Negotiated Discriminators

#### Networking Requirements

A BFD session for IPv6 can be created to monitor an IPv6 link on a network for quick fault detection. In [Figure 1](#EN-US_TASK_0000001176661899__fig_dc_vrp_bfd_cfg_200601), BFD monitors the direct link between DeviceA and DeviceB in asynchronous mode.

**Figure 1** Configuring a BFD session for IPv6 with automatically negotiated discriminators![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001176661935.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IPv6 addresses to the interfaces connecting DeviceA and DeviceB.
2. Enable BFD globally on DeviceA and DeviceB, and then configure a single-hop BFD session for IPv6 with automatically negotiated discriminators on each device.


#### Procedure

1. Assign IPv6 addresses to the interfaces connecting DeviceA and DeviceB.# Assign an IPv6 address to DeviceA's interface.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8::1 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Assign an IPv6 address to DeviceB's interface.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8::2 64
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
2. Configure a single-hop BFD session for IPv6 with automatically negotiated discriminators on DeviceA and DeviceB.# Configure DeviceA.
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd ipv6session bind peer-ipv6 2001:db8::2 interface 100ge 1/0/1 source-ipv6 2001:db8::1 auto
   [*DeviceA-bfd-session-ipv6session] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd ipv6session bind peer-ipv6 2001:db8::1 interface 100ge 1/0/1 source-ipv6 2001:db8::2 auto
   [*DeviceB-bfd-session-ipv6session] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check that DeviceA and DeviceB can ping each other. The command output on DeviceA is used as an example.

```
[~DeviceA] ping ipv6 2001:db8::2
PING 2001:db8::2 : 56  data bytes, press CTRL_C to break
    Reply from 2001:db8::2
    bytes=56 Sequence=1 hop limit=64 time=3 ms
    Reply from 2001:db8::2
    bytes=56 Sequence=2 hop limit=64 time=1 ms
    Reply from 2001:db8::2
    bytes=56 Sequence=3 hop limit=64 time=1 ms
    Reply from 2001:db8::2
    bytes=56 Sequence=4 hop limit=64 time=1 ms
    Reply from 2001:db8::2
    bytes=56 Sequence=5 hop limit=64 time=1 ms
  ---2001:db8::2 ping statistics---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max=1/1/3 ms
```

# Check detailed BFD session information on DeviceA and DeviceB. The command output on DeviceA is used as an example.

```
[~DeviceA] display bfd session all verbose
2020-01-01 11:21:06.8
(w): State in WTR 
(*): State is invalid
  Total UP/DOWN Session Number : 1/0
--------------------------------------------------------------------------------
  Name : ipv6session                    (Single Hops) State : Up                    
------------------------------------------------------------------------------
  Local Discriminator    : 16386            Remote Discriminator   : 16387
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Interface(100GE1/0/1)
  Bind Session Type      : Static_Auto
  Bind Peer IP Address   : 2001:DB8::2
  Bind Interface         : 100GE1/0/1
  Bind Source IP Address : 2001:DB8::1 
  FSM Board ID           : 1               TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000      Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 1000             Actual Rx Interval (ms): 1000
  WTR Interval (ms)      : -                Detect Interval (ms)   : 3000
  Local Detect Multi     : 3                Active Multi           : -
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 3784             TTL                    : 255
  Proc Interface Status  : Disable          Process PST            : Disable
  Config PST             : Disable
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : AUTO 
  Session Description    : - 
------------------------------------------------------------------------------
```

The command output shows that a single-hop BFD session for IPv6 with automatically negotiated discriminators has been established and is in the **Up** state.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8::1/64
  #
  bfd ipv6session bind peer-ipv6 2001:db8::2 interface 100ge 1/0/1 source-ipv6 2001:db8::1 auto
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
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8::2/64
  #
  bfd ipv6session bind peer-ipv6 2001:db8::1 interface 100ge 1/0/1 source-ipv6 2001:db8::2 auto
  #
  return
  ```