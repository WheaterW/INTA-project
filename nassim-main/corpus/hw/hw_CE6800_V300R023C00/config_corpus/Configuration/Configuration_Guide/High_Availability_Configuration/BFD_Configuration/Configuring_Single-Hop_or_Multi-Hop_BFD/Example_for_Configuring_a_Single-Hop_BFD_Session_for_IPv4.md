Example for Configuring a Single-Hop BFD Session for IPv4
=========================================================

Example for Configuring a Single-Hop BFD Session for IPv4

#### Networking Requirements

A single-hop BFD session for IPv4 can be configured to monitor a direct IPv4 link on a network for quick fault detection. In [Figure 1](#EN-US_TASK_0000001176741785__fig_dc_vrp_bfd_cfg_006301), BFD monitors the direct link between DeviceA and DeviceB in asynchronous mode.

**Figure 1** Configuring single-hop BFD for IPv4![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001176741817.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IPv4 addresses to the interfaces connecting DeviceA and DeviceB.
2. Enable BFD globally on DeviceA and DeviceB, and configure a single-hop BFD session bound to the outbound interface on each device.


#### Procedure

1. Assign IPv4 addresses to the interfaces connecting DeviceA and DeviceB.# Assign an IPv4 address to DeviceA's interface.
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
   
   # Assign an IPv4 address to DeviceB's interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
2. Enable BFD globally and configure a single-hop BFD session.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd ipsession bind peer-ip 10.1.1.2 interface 100ge 1/0/1
   [*DeviceA-bfd-session-ipsession] discriminator local 1
   [*DeviceA-bfd-session-ipsession] discriminator remote 2
   [*DeviceA-bfd-session-ipsession] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd ipsession bind peer-ip 10.1.1.1 interface 100ge 1/0/1
   [*DeviceB-bfd-session-ipsession] discriminator local 2
   [*DeviceB-bfd-session-ipsession] discriminator remote 1
   [*DeviceB-bfd-session-ipsession] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check detailed BFD session information on DeviceA and DeviceB. The command output on DeviceA is used as an example.

```
[~DeviceA] display bfd session all verbose
2020-01-01 11:21:06.8 
(w): State in WTR  (*): State is invalid Total UP/DOWN Session Number : 1/0
--------------------------------------------------------------------------------
  Name : ipsession                    (Single Hops) State : Up                    
------------------------------------------------------------------------------
  Local Discriminator    : 1                Remote Discriminator   : 2
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Interface(100GE1/0/1)
  Bind Session Type      : Static
  Bind Peer IP Address   : 10.1.1.2
  Bind Interface         : 100GE1/0/1
  FSM Board ID           : 1                TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000      Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 1000             Actual Rx Interval (ms): 1000
  WTR Interval (ms)      : -                Detect Interval (ms)   : 3000
  Local Detect Multi     : 3                Active Multi           : -
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 3784             TTL                    : 255
  Proc Interface Status  : Disable          Process PST            : Disable
  Config PST             : Disable
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : No Application Bind
  Session Description    : - 
------------------------------------------------------------------------------
```

The command output shows that a single-hop BFD session for IPv4 has been established and is in the **Up** state.


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
  bfd ipsession bind peer-ip 10.1.1.2 interface 100GE1/0/1 
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
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  bfd ipsession bind peer-ip 10.1.1.1 interface 100GE1/0/1 
   discriminator local 2
   discriminator remote 1
  #
  return
  ```