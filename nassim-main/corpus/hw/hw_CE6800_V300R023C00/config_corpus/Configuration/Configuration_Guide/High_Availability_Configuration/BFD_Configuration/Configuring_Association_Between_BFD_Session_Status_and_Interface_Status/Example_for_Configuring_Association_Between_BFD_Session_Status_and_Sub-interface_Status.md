Example for Configuring Association Between BFD Session Status and Sub-interface Status
=======================================================================================

Example for Configuring Association Between BFD Session Status and Sub-interface Status

#### Networking Requirements

On the large metro Ethernet network shown in [Figure 1](#EN-US_TASK_0000001176661895__fig_dc_vrp_bfd_cfg_200401), a large number of VLAN services are configured on an interface's sub-interface and high reliability is required. Establish a BFD session to monitor the interface's link connectivity, and associate the BFD session status with the sub-interface status. This configuration improves service reliability on the sub-interface and saves BFD session resources.

**Figure 1** Configuring the association between BFD session status and sub-interface status![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1, and interface 1.1 represents 100GE1/0/1.1.


  
![](figure/en-us_image_0000001176741841.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to the interfaces connecting DeviceA and DeviceB.
2. Enable BFD globally on DeviceA and DeviceB and configure a single-hop BFD session on each device.
3. Associate the BFD session status with the sub-interface status.

#### Procedure

1. Assign IP addresses to the interfaces on DeviceA and DeviceB, and create a sub-interface on each device.# Configure DeviceA.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/1.1
   [*DeviceA-100GE1/0/1.1] ip address 10.2.1.1 24
   [*DeviceA-100GE1/0/1.1] dot1q termination vid 10
   [*DeviceA-100GE1/0/1.1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/1.1
   [*DeviceB-100GE1/0/1.1] ip address 10.2.1.2 24
   [*DeviceB-100GE1/0/1.1] dot1q termination vid 10
   [*DeviceB-100GE1/0/1.1] quit
   [*DeviceB] commit
   ```
2. Configure single-hop BFD.# Configure DeviceA.
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd pissub bind peer-ip default-ip interface 100ge 1/0/1
   [*DeviceA-bfd-session-pissub] discriminator local 1
   [*DeviceA-bfd-session-pissub] discriminator remote 2
   [*DeviceA-bfd-session-pissub] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd pissub bind peer-ip default-ip interface 100ge 1/0/1
   [*DeviceB-bfd-session-pissub] discriminator local 2
   [*DeviceB-bfd-session-pissub] discriminator remote 1
   [*DeviceB-bfd-session-pissub] quit
   [*DeviceB] commit
   ```
3. Associate the BFD session status with the sub-interface status.# Configure DeviceA.
   ```
   [~DeviceA] bfd pissub 
   [*DeviceA-bfd-session-pissub] process-interface-status sub-if
   [*DeviceA-bfd-session-pissub] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] bfd pissub
   [*DeviceB-bfd-session-pissub] process-interface-status sub-if
   [*DeviceB-bfd-session-pissub] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check detailed BFD session information on DeviceA and DeviceB. The command output on DeviceA is used as an example.

```
[~DeviceA] display bfd session all verbose
(w): State in WTR 
(*): State is invalid  Total UP/DOWN Session Number : 1/0
------------------------------------------------------------------------------
  Name : pissub                       (Single Hops) State : Up     
------------------------------------------------------------------------------
  Local Discriminator    : 1                Remote Discriminator    : 2
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Interface(100GE1/0/1)
  Bind Session Type      : Static
  Bind Peer IP Address   : 224.0.0.184
  Bind Interface         : 100GE1/0/1
  FSM Board ID           : 1               TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000      Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 1000             Actual Rx Interval (ms): 1000
  WTR Interval (ms)      : -                Detect Interval (ms)   : 3000
  Local Detect Multi     : 3                Active Multi           : -
  Echo Passive           : Disable          Acl Number             : - 
  Destination Port       : 3784             TTL                    : 255 
  Proc Interface Status  : Disable          Process PST            : Disable    
  Config PST             : Disable    
  Active Multi           : 3
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : No Application Bind
  Session Description    : - 
------------------------------------------------------------------------------
```

The command output shows that a single-hop BFD session has been established on DeviceA and is in the **Up** state.

# Run the **shutdown** command on 100GE1/0/1 of DeviceB.

```
[~DeviceB] interface 100ge 1/0/1
[~DeviceB-100GE1/0/1] shutdown
[~DeviceB-100GE1/0/1] quit
[*DeviceB] commit
```

# Check the status of 100GE1/0/1.1 on DeviceA.

```
[~DeviceA] display interface 100ge 1/0/1.1
100GE1/0/1.1 current state : DOWN (ifindex: 33)
Line protocol current state : DOWN (Main BFD status down)
...
```

The command output shows that 100GE1/0/1.1 is in the **DOWN (Main BFD status down)** state on DeviceA.

# Check detailed BFD session information on DeviceA.

```
[~DeviceA] display bfd session all verbose
(w): State in WTR  (*): State is invalid
  Total UP/DOWN Session Number : 0/1
------------------------------------------------------------------------------
  Name : pissub                       (Single Hops) State : Down     
------------------------------------------------------------------------------
  Local Discriminator    : 1                Remote Discriminator    : 2
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Interface(100GE1/0/1)
  Bind Session Type      : Static
  Bind Peer IP Address   : 224.0.0.184
  Bind Interface         : 100GE1/0/1
  FSM Board ID           : 1               TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000      Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 1000             Actual Rx Interval (ms): 1000
  WTR Interval (ms)      : 0                Detect Interval (ms)   : 3000
  Local Detect Multi     : 3                Active Multi           : -
  Echo Passive           : Disable          Acl Number             : - 
  Destination Port       : 3784             TTL                    : 255 
  Proc Interface Status  : Disable          Process PST            : Disable    
  Config PST             : Disable    
  Active Multi           : 3
  Last Local Diagnostic  : Control Detection Time Expired
  Bind Application       : No Application Bind
  Session Description    : - 
------------------------------------------------------------------------------
```

The command output shows that the BFD session is in the **Down** state on DeviceA.


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
  interface 100GE1/0/1.1
   ip address 10.2.1.1 255.255.255.0
   encapsulation dot1q-termination
  #
  bfd pissub bind peer-ip default-ip interface 100GE1/0/1
   discriminator local 1
   discriminator remote 2
   process-interface-status sub-if
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
  interface 100GE1/0/1.1
   ip address 10.2.1.2 255.255.255.0
   encapsulation dot1q-termination
  #
  bfd pissub bind peer-ip default-ip interface 100GE1/0/1
   discriminator local 2
   discriminator remote 1
   process-interface-status sub-if
  #
  return
  ```