Example for Configuring a Multi-Hop BFD Session for IPv4
========================================================

Example for Configuring a Multi-Hop BFD Session for IPv4

#### Networking Requirements

A multi-hop BFD session for IPv4 can be configured to monitor a multi-hop link on a network for quick fault detection. In [Figure 1](#EN-US_TASK_0000001176661877__fig_dc_vrp_bfd_cfg_006301), BFD monitors the multi-hop link between DeviceA and DeviceC in asynchronous mode.

**Figure 1** Configuring multi-hop BFD for IPv4![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001130782150.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IPv4 addresses to interfaces on DeviceA, DeviceB, and DeviceC to ensure that the devices can reach each other.
2. Configure a BFD session on DeviceA to monitor the multi-hop path from DeviceA to DeviceC. Configure a BFD session on DeviceC to monitor the multi-hop path from DeviceC to DeviceA.

#### Procedure

1. Configure static routes to ensure that the devices are reachable from each other.
   
   # Assign an IPv4 address to DeviceA's interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1 
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Assign IPv4 addresses to DeviceB's interfaces.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 10.2.1.1 24
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # Assign an IPv4 address to DeviceC's interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] ip address 10.2.1.2 24
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   # Configure static routes.
   
   ```
   [~DeviceA] ip route-static 10.2.1.0 255.255.255.0 10.1.1.2
   [*DeviceA] commit
   [~DeviceC] ip route-static 10.1.1.0 255.255.255.0 10.2.1.1
   [*DeviceC] commit
   ```
2. Configure multi-hop BFD between DeviceA and DeviceC.
   
   # Enable BFD on DeviceA, and configure a BFD session to monitor the link from DeviceA to DeviceC. You do not need to bind the BFD session to an interface.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd atoc bind peer-ip 10.2.1.2
   [*DeviceA-bfd-session-atoc] discriminator local 10
   [*DeviceA-bfd-session-atoc] discriminator remote 20
   [*DeviceA-bfd-session-atoc] quit
   [*DeviceA] commit
   ```
   
   # Enable BFD on DeviceC, and configure a BFD session to monitor the link from DeviceC to DeviceA. You do not need to bind the BFD session to an interface.
   
   ```
   [~DeviceC] bfd
   [*DeviceC-bfd] quit
   [*DeviceC] bfd ctoa bind peer-ip 10.1.1.1
   [*DeviceC-bfd-session-ctoa] discriminator local 20
   [*DeviceC-bfd-session-ctoa] discriminator remote 10
   [*DeviceC-bfd-session-ctoa] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Check detailed BFD session information on DeviceA and DeviceC. The command output on DeviceA is used as an example.

```
[~DeviceA] display bfd session all verbose
2020-01-01 11:21:06.8 
(w): State in WTR  
(*): State is invalid   
Total UP/DOWN Session Number : 1/0
------------------------------------------------------------------------------
  Name : atoc                         (Multiple Hops)  State : Up      
------------------------------------------------------------------------------
  Local Discriminator    : 10             Remote Discriminator    : 20
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Peer Ip Address
  Bind Session Type      : Static
  Bind Peer IP Address   : 10.2.1.2
  Bind Interface         : -   
  FSM Board ID           : 1               TOS-EXP               : 7
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

# Run the **shutdown** command on DeviceA's interface 100GE 1/0/1 to simulate a link fault.

```
[~DeviceA] interface 100ge 1/0/1
[~DeviceA-100GE1/0/1] shutdown
[~DeviceA-100GE1/0/1] quit
```

# Check the BFD session state on DeviceA and DeviceC. The command output on DeviceA is used as an example.

```
[DeviceA] display bfd session all verbose
2020-01-01 11:21:06.8
(w): State in WTR  
(*): State is invalid   
Total UP/DOWN Session Number : 1/0
------------------------------------------------------------------------------
  Name : atoc                         (Multiple Hops)  State : Down   
------------------------------------------------------------------------------
  Local Discriminator    : 10             Remote Discriminator    : 20
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Peer Ip Address
  Bind Session Type      : Static
  Bind Peer IP Address   : 10.2.1.2
  Bind Interface         : -   
  FSM Board ID           : 1               TOS-EXP               : 7
  Min Tx Interval (ms)   : 1000      Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 1000             Actual Rx Interval (ms): 1000
  WTR Interval (ms)      : -                Detect Interval (ms)   : 3000
  Local Detect Multi     : 3                Active Multi           : -
  Destination Port       : 4784             TTL                    : 254
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : No Application Bind
  Session Not Up Reason  : In negotiation  
  Session Description    : - 
------------------------------------------------------------------------------
```

The command output shows that the BFD session is in the **Down** state.


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
   ip address 10.1.1.1 255.255.255.0
  #
  #
  ip route-static 10.2.1.0 255.255.255.0 10.1.1.2
  #
  bfd atoc bind peer-ip 10.2.1.2
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
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.1 255.255.255.0
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
  interface 100GE1/0/1
   undo portswitch
   ip address 10.2.1.2 255.255.255.0
  #
  ip route-static 10.1.1.0 255.255.255.0 10.2.1.1
  #
  bfd ctoa bind peer-ip 10.1.1.1
   discriminator local 20
   discriminator remote 10
  #
  return
  ```