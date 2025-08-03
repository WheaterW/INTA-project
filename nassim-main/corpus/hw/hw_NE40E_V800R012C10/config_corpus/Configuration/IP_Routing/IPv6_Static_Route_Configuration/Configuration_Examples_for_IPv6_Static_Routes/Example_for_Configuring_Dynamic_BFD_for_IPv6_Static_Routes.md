Example for Configuring Dynamic BFD for IPv6 Static Routes
==========================================================

Dynamic BFD for IPv6 static routes can fast detect link failures.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365496__fig_dc_vrp_static-route_disjoin_cfg_002401), Device A is connected to Device B through Switch C. A static default route is configured on Device A so that Device A can communicate with external devices. A BFD session is configured between Device A and Device B to detect whether a link fault occurs.

**Figure 1** Networking for configuring dynamic BFD for IPv6 static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_002401.png)

#### Precautions

When configuring dynamic BFD for IPv6 static routes, note the following points:

* BFD has been enabled globally.
* The parameters configured on the two ends of a BFD session must be consistent.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. On Device A, configure an IPv6 static route to Device B.
2. Configure dynamic BFD for IPv6 static routes.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IPv6 address to be detected by BFD
* Default values of the local detection multiplier and of the minimum intervals at which BFD Control packets are sent and received

#### Procedure

1. Configure an IPv6 address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365496__section_dc_vrp_static-route_disjoin_cfg_002405) in this section.
2. Configure IPv6 static routes.
   
   
   
   # On Device A, configure a static route to 2001:db8:8::1/64.
   
   ```
   [~DeviceA] ipv6 route-static 2001:db8:8:: 64 2001:db8:200::2
   ```
   ```
   [*DeviceA] commit
   ```
   
   # On Device A, check the IPv6 routing table. The following command output shows that static routes exist in the IPv6 routing table.
   
   ```
   [~DeviceA] display ipv6 routing-table
   ```
   ```
   Routing Table : _public_
            Destinations : 6        Routes : 6
   
   Destination  : 2001:db8:7::                            PrefixLength : 64
   NextHop      : 2001:db8:7::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:db8:7::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:db8:8::                           PrefixLength : 64
   NextHop      : 2001:db8:200::2                         Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : 2001:db8:200::2                         TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : RD
   
   Destination  : 2001:db8:200::                          PrefixLength : 64
   NextHop      : 2001:db8:200::1                         Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:db8:200::1                         PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D
   
   ```
   
   # On Device B, configure the static route to 2001:db8:7::1/64.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:7:: 64 2001:db8:200::1
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure dynamic BFD for static routes.
   
   
   
   # On Device A, bind a static route to a BFD session.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] ipv6 route-static bfd 2001:db8:200::2 local-address 2001:db8:200::1
   ```
   ```
   [*DeviceA] ipv6 route-static 2001:db8:8:: 64 2001:db8:200::2 bfd enable
   ```
   ```
   [*DeviceA] commit
   ```
   
   # On Device B, bind a static route to a BFD session.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] ipv6 route-static bfd 2001:db8:200::1 local-address 2001:db8:200::2
   ```
   ```
   [*DeviceB] ipv6 route-static 2001:db8:7:: 64 2001:db8:200::1 bfd enable
   ```
   ```
   [*DeviceB] commit
   ```
4. Verify the configuration.
   
   
   
   # After the configuration is complete, you can view that a BFD session has been established between Device A and Device B and is Up and that a static route is bound to it.
   
   Use the command output on Device A as an example.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
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
     Track Group Name       : -
   ------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 1/0
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:200::1/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:7::1/64
  #
  ipv6 route-static bfd 2001:db8:200::2 local-address 2001:db8:200::1
  ipv6 route-static 2001:db8:8:: 64 2001:db8:200::2 bfd enable
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:200::2/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:8::1/64
  #
  ipv6 route-static bfd 2001:db8:200::1 local-address 2001:db8:200::2
  ipv6 route-static 2001:db8:7:: 64 2001:db8:200::1 bfd enable
  #
  return
  ```