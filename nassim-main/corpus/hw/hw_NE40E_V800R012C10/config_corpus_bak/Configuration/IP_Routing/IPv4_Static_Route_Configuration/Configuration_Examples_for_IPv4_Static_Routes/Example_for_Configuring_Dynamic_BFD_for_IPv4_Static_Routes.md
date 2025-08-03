Example for Configuring Dynamic BFD for IPv4 Static Routes
==========================================================

Dynamic BFD for IPv4 static routes can fast detect link failures.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365455__fig_dc_vrp_static-route_disjoin_cfg_002001), DeviceA is connected to DeviceB through SwitchC. It is required that DeviceA communicate with other Devices through static default routes and that a BFD session be established between DeviceA and DeviceB to detect link failures.

**Figure 1** Configuring BFD for static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_002001.png)

#### Precautions

When configuring dynamic BFD for static routes, note the following:

* BFD has been enabled globally.
* The parameters configured on the two ends of a BFD session must be consistent.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. On DeviceA, configure an IPv4 static route to DeviceB.
2. Configure dynamic BFD for static routes.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address to be detected by BFD
* Default values of the local detection multiplier and of the minimum intervals at which BFD Control packets are sent and received

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365455__section_dc_vrp_static-route_disjoin_cfg_002005) in this section.
2. Configure static routes.
   
   
   
   # On DeviceA, configure a static route to 2.2.2.2/32.
   
   ```
   [~DeviceA] ip route-static 2.2.2.2 32 10.10.1.2
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Check the IP routing table of DeviceA. The following command output shows that the static route exists in the routing table.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 10        Routes : 10
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  Direct 0    0             D  127.0.0.1       LoopBack0
           2.2.2.2/32  Static 60   0             RD 10.10.1.2       GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
         10.10.1.0/24  Direct 0    0             D  10.10.1.1       GigabitEthernet0/1/0
         10.10.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
         10.10.1.2/32  Direct 0    0             D  10.10.1.2       GigabitEthernet0/1/0
       10.10.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
   ```
   
   # On DeviceB, configure a static route to 1.1.1.1/32.
   
   ```
   [~DeviceB] ip route-static 1.1.1.1 32 10.10.1.1
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure dynamic BFD for static routes.
   
   
   
   # On DeviceA, bind the static route to the BFD session.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] ip route-static bfd 10.10.1.2 local-address 10.10.1.1
   ```
   ```
   [*DeviceA] ip route-static 2.2.2.2 32 10.10.1.2 bfd enable
   ```
   ```
   [*DeviceA] commit
   ```
   
   # On DeviceB, bind the static route to the BFD session.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] ip route-static bfd 10.10.1.1 local-address 10.10.1.2
   ```
   ```
   [*DeviceB] ip route-static 1.1.1.1 32 10.10.1.1 bfd enable
   ```
   ```
   [*DeviceB] commit
   ```
4. Verify the configuration.
   
   
   
   # After the preceding configuration, on DeviceA and DeviceB, you can view that the BFD session has been established and is Up and that the static routes have been bound to the BFD session.
   
   Use the command output DeviceA as an example.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (Multi Hop) State : Up                    Name : dyn_8193
   ------------------------------------------------------------------------------
     Local Discriminator    : 8193             Remote Discriminator   : 8193
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Peer IP Address
     Bind Session Type      : Dynamic
     Bind Peer IP Address   : 10.10.1.2
     Bind Interface         : -
     Bind Source IP Address : 10.10.1.1
     FSM Board Id           : 0                TOS-EXP                : 7
     Min Tx Interval (ms)   : 50               Min Rx Interval (ms)   : 50
     Actual Tx Interval (ms): 50               Actual Rx Interval (ms): 50
     Local Detect Multi     : 3                Detect Interval (ms)   : 150
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 4784             TTL                    : 253
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : 0                Local Demand Mode      : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : STATICRT
     Session TX TmrID       : 0                Session Detect TmrID   : 0
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 1/0
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 7.7.7.7 255.255.255.0
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  ip route-static bfd 10.10.1.2 local-address 10.10.1.1
  ip route-static 2.2.2.2 32 10.10.1.2 bfd enable
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 8.8.8.8 255.255.255.0
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  ip route-static bfd 10.10.1.1 local-address 10.10.1.2
  ip route-static 1.1.1.1 32 10.10.1.1 bfd enable
  #
  return
  ```