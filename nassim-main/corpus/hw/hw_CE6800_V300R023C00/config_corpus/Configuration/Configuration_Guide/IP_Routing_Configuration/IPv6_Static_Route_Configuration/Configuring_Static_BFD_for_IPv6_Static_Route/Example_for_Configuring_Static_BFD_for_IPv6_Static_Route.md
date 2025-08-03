Example for Configuring Static BFD for IPv6 Static Route
========================================================

Example for Configuring Static BFD for IPv6 Static Route

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176743131__fig_dc_vrp_static-route_disjoin_cfg_003001), DeviceA is connected to DeviceB through a switch. You can configure the default static route on DeviceA so that DeviceA can communicate with other devices. In addition, a BFD session needs to be configured between DeviceA and DeviceB to rapidly detect link faults.

**Figure 1** Network diagram of static BFD for IPv6 static route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176663241.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for interfaces on each device.
2. On DeviceA, configure an IPv6 static route to DeviceB.
3. Configure static BFD for IPv6 static route.

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
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1::1 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176743131__postreq24192593172748).
2. Configure a BFD session between DeviceA and DeviceB.
   
   
   
   # On DeviceA, configure a BFD session to DeviceB.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd aa bind peer-ipv6 2001:db8:1::2
   [*DeviceA-bfd-session-aa] discriminator local 10
   [*DeviceA-bfd-session-aa] discriminator remote 20
   [*DeviceA-bfd-session-aa] quit
   [*DeviceA] commit
   ```
   
   # On DeviceB, configure a BFD session to DeviceA.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd bb bind peer-ipv6 2001:db8:1::1
   [*DeviceB-bfd-session-bb] discriminator local 20
   [*DeviceB-bfd-session-bb] discriminator remote 10
   [*DeviceB-bfd-session-bb] quit
   [*DeviceB] commit
   ```
3. Configure a default static route and bind the route to the BFD session.
   
   
   
   # On DeviceA, configure a default static route to the external network and bind it to the BFD session named **aa**.
   
   ```
   [~DeviceA] ipv6 route-static 0::0 0 2001:db8:1::2 track bfd-session aa
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display bfd session all** command on DeviceA to check the BFD status.

```
[~DeviceA] display bfd session all
S: Static session
D: Dynamic session
IP: IP session
IF: Single-hop session
PEER: Multi-hop session
AUTO: Automatically negotiated session
(w): State in WTR  (): State is invalid
--------------------------------------------------------------------------------
Local Remote PeerIpAddr      State     Type        InterfaceName
--------------------------------------------------------------------------------
10    20     2001:db8:1::2   Up       S_IP_PEER         -
--------------------------------------------------------------------------------
 Total UP/DOWN Session Number : 1/0
```

The command output shows that a BFD session has been established and is in the **Up** state.

# Check the IPv6 routing table of DeviceA.

```
[~DeviceA] display ipv6 routing-table
Routing Table : _public_
         Destinations : 5        Routes : 5

 Destination  : ::                         PrefixLength : 0
 NextHop      : 2001:db8:1::2              Preference   : 60
 Cost         : 0                          Protocol     : Static
 RelayNextHop : ::                         TunnelID     : 0x0
 Interface    : 100GE1/0/1                  Flags        : RD

 Destination  : 2001:DB8::1                     PrefixLength : 128
 NextHop      : 2001:DB8::1                     Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : InLoopBack0                     Flags        : D

 Destination  : 2001:db8:1::                    PrefixLength : 64
 NextHop      : 2001:db8:1::1                   Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : 100GE1/0/1                       Flags        : D

 Destination  : 2001:db8:1::1                   PrefixLength : 128
 NextHop      : 2001:DB8::1                     Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : 100GE1/0/1                       Flags        : D

 Destination  : FE80::                          PrefixLength : 10
 NextHop      : ::                              Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : NULL0                           Flags        : D
```

The command output shows that the static route to 0::0/0 exists in the routing table.

# Run the **shutdown** command on 100GE 1/0/1 of DeviceB to simulate a link fault.

```
[~DeviceB] interface 100ge 1/0/1
[~DeviceB-100GE1/0/1] shutdown
[*DeviceB] commit
```

# Check the IPv6 routing table of DeviceA.

```
[~DeviceA] display ipv6 routing-table
Routing Table : _public_
         Destinations : 1        Routes : 1

 Destination  : 2001:DB8::1                     PrefixLength : 128
 NextHop      : 2001:DB8::1                     Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : InLoopBack0                     Flags        : D
```

The command output shows that the default static route 0::0/0 does not exist. This is because the static route has been bound to a BFD session, and BFD immediately notifies that the bound static route becomes unavailable after detecting a link fault.


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
   ipv6 address 2001:db8:1::1/64
  #
  ipv6 route-static :: 0 2001:db8:1::2 track bfd-session aa
  #
  bfd aa bind peer-ipv6 2001:db8:1::2
   discriminator local 10
   discriminator remote 20
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
   ipv6 address 2001:db8:1::2/64
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
  #
  bfd bb bind peer-ipv6 2001:db8:1::1
   discriminator local 20
   discriminator remote 10
  #
  return
  ```