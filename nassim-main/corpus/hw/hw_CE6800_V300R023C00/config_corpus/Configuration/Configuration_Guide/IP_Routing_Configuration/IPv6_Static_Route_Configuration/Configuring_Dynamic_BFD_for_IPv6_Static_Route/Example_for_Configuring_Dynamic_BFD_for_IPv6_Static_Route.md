Example for Configuring Dynamic BFD for IPv6 Static Route
=========================================================

Example for Configuring Dynamic BFD for IPv6 Static Route

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176743133__fig_dc_vrp_static-route_disjoin_cfg_002401), DeviceA is connected to DeviceB through a switch. A static default route is configured on DeviceA, and a BFD session is configured between DeviceA and DeviceB to detect link faults.

**Figure 1** Network diagram of dynamic BFD for IPv6 static route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001176743149.png)

#### Precautions

During the configuration, note the following:

* Ensure that BFD has been enabled globally.
* Ensure that the parameters configured on both ends of a BFD session are consistent.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for interfaces on each device.
2. On DeviceA, configure an IPv6 static route to DeviceB.
3. Configure dynamic BFD for IPv6 static route.

#### Procedure

1. Configure IPv6 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:200::1 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:7::1 64
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176743133__postreq24192593172748).
2. Configure IPv6 static routes on devices.
   
   
   
   # On DeviceA, configure a static route to 2001:db8:8::/64.
   
   ```
   [~DeviceA] ipv6 route-static 2001:db8:8:: 64 2001:db8:200::2
   [*DeviceA] commit
   ```
   
   # Check the IPv6 routing table of DeviceA. The command output shows that the IPv6 static route to 2001:db8:8::/64 exists in the routing table.
   
   ```
   [~DeviceA] display ipv6 routing-table
   Routing Table : _public_
            Destinations : 6        Routes : 6
   
   Destination  : 2001:db8:7::                            PrefixLength : 64
   NextHop      : 2001:db8:7::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                               Flags        : D
   
   Destination  : 2001:db8:7::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                               Flags        : D
   
   Destination  : 2001:db8:8::                           PrefixLength : 64
   NextHop      : 2001:db8:200::2                         Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : 2001:db8:200::2                         TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : RD
   
   Destination  : 2001:db8:200::                          PrefixLength : 64
   NextHop      : 2001:db8:200::1                         Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : D
   
   Destination  : 2001:db8:200::1                         PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D
   ```
   
   The command output shows that the IPv6 static route to 2001:db8:8::/64 exists in the routing table.
   
   # On DeviceB, configure a static route to 2001:db8:7::/64.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:7:: 64 2001:db8:200::1
   [*DeviceB] commit
   ```
3. Configure dynamic BFD for IPv6 static route.
   
   
   
   # On DeviceA, bind the static route to a BFD session.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] ipv6 route-static bfd 2001:db8:200::2 local-address 2001:db8:200::1
   [*DeviceA] ipv6 route-static 2001:db8:8:: 64 2001:db8:200::2 bfd enable
   [*DeviceA] commit
   ```
   
   # On DeviceB, bind the static route to a BFD session.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] ipv6 route-static bfd 2001:db8:200::1 local-address 2001:db8:200::2
   [*DeviceB] ipv6 route-static 2001:db8:7:: 64 2001:db8:200::1 bfd enable
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the BFD session status on DeviceA.

```
[~DeviceA] display bfd session all verbose
(w): State in WTR  (): State is invalid 
------------------------------------------------------------------------------
  (Multi Hop) State : Up                   Name : dyn_16385
------------------------------------------------------------------------------
  Local Discriminator    : 16385            Remote Discriminator   : 16385
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Peer IP Address
  Bind Session Type      : Dynamic
  Bind Peer IP Address  : 2001:db8:200::2
  Bind Interface         : -
  Bind Source IP Address : 2001:db8:200::1
  FSM Board Id           : 3                TOS-EXP                : 7
  Min Tx Interval (ms) :50              Min Rx Interval (ms)  :50
  Actual Tx Interval (ms): 50               Actual Rx Interval (ms): 50
  Local Detect Multi   : 3               Detect Interval (ms)   : 150
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 4784             TTL                    : 253
  Proc Interface Status  : Disable          Process PST            : Disable
  WTR Interval (ms)      : 0                Local Demand Mode      : Disable
  Active Multi           : 3
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : STATICRTV6
  Session TX TmrID       : 0                Session Detect TmrID   : 0
  Session Init TmrID     : -                Session WTR TmrID      : -
  Session Echo Tx TmrID  : -
  Session Description    : -
------------------------------------------------------------------------------

     Total UP/DOWN Session Number : 1/0
```

The command output shows that the BFD session has been established and is in the **Up** state on DeviceA.


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
   ipv6 address 2001:db8:200::1/64
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:7::1/64
  #
  ipv6 route-static bfd 2001:db8:200::2 local-address 2001:db8:200::1
  ipv6 route-static 2001:db8:8:: 64 2001:db8:200::2 bfd enable
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
   ipv6 address 2001:db8:200::2/64
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:8::1/64
  #
  ipv6 route-static bfd 2001:db8:200::1 local-address 2001:db8:200::2
  ipv6 route-static 2001:db8:7:: 64 2001:db8:200::1 bfd enable
  #
  return
  ```