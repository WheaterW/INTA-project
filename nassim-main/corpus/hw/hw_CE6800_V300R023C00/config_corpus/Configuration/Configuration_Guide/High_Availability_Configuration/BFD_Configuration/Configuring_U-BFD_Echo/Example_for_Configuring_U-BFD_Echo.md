Example for Configuring U-BFD Echo
==================================

Example for Configuring U-BFD Echo

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176661905__fig_dc_vrp_bfd_cfg_011301), DeviceA supports BFD, whereas DeviceB does not. To rapidly detect faults on the direct link between DeviceA and DeviceB, configure a U-BFD Echo session on DeviceA. When DeviceB receives a BFD packet from DeviceA, it immediately loops back the packet for fast link fault detection.

**Figure 1** Network diagram for configuring a U-BFD Echo session![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001176661937.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to the interfaces directly connecting DeviceA and DeviceB.
2. Configure a U-BFD Echo session on DeviceA to monitor the direct link between DeviceA and DeviceB.

#### Procedure

1. Assign IP addresses to the interfaces directly connecting DeviceA and DeviceB.# Assign an IP address to DeviceA's interface.
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
   
   # Assign an IP address to DeviceB's interface.
   
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
2. Configure a U-BFD Echo session on DeviceA.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd atob bind peer-ip 10.1.1.2 interface 100ge 1/0/1 one-arm-echo
   [*DeviceA-bfd-session-atob] discriminator local 1
   [*DeviceA-bfd-session-atob] min-echo-rx-interval 100
   [*DeviceA-bfd-session-atob] quit
   [*DeviceA] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display bfd session all verbose** command on DeviceA to check the BFD session status.

```
<DeviceA> display bfd session all verbose
(w): State in WTR 
(*): State is invalid
--------------------------------------------------------------------------------
  Name : atob                  (Single Hops)   State : Up                  
--------------------------------------------------------------------------------
  Local Discriminator    : 1                Remote Discriminator   : -
  Session Detect Mode    : Asynchronous One-arm-echo Mode
  BFD Bind Type          : Interface(100ge 1/0/1)
  
  Bind Session Type      : Static 
  Bind Peer IP Address   : 10.1.1.2         
  Bind Interface         : 100ge 1/0/1
  
  Track Interface        : -  
  FSM Board ID          : -               TOS-EXP                : 7
  Echo Rx Interval (ms)  : 100 
  Actual Tx Interval (ms): 100              Actual Rx Interval (ms): 100 
  Local Detect Multi     : 3                Detect Interval (ms)   : 300 
  Echo Passive           : Disable          Acl Number             : - 
  Destination Port       : 3784             TTL                    : 255 
  Proc Interface Status  : Disable          Process PST            : Disable    
  Config PST             : Disable    
  Active Multi           : 3                  
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : No Application Bind
  Session TX TmrID       : -                Session Detect TmrID   : - 
  Session Init TmrID     : -                Session WTR TmrID      : - 
  Session Echo Tx TmrID  : -   
  Session Not Up Reason  : -  
  Session Description    : - 
--------------------------------------------------------------------------------

       Total UP/DOWN Session Number : 1/0
```

The command output shows that a U-BFD Echo session has been established on DeviceA and is in the **Up** state.


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
  bfd atob bind peer-ip 10.1.1.2 interface 100ge 1/0/1 one-arm-echo
   discriminator local 1
   min-echo-rx-interval 100
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
  return
  ```