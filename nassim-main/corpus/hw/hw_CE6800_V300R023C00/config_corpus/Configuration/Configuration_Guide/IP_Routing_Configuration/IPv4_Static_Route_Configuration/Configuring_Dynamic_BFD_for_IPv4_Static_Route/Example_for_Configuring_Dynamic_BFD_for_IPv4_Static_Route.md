Example for Configuring Dynamic BFD for IPv4 Static Route
=========================================================

Example for Configuring Dynamic BFD for IPv4 Static Route

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176662503__fig264403810430), DeviceA is connected to DeviceB through a switch. You can configure the default static route on DeviceA so that DeviceA can communicate with other devices. Configure a BFD session between DeviceA and DeviceB to detect link faults.

**Figure 1** Network diagram of dynamic BFD for IPv4 static route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001176742461.png)

#### Precautions

Note the following during the configuration:

* Ensure that BFD has been enabled globally.
* Ensure that the parameters configured on both ends of a BFD session are consistent.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each device.
2. On DeviceA, configure an IPv4 static route to DeviceB.
3. Configure dynamic BFD for IPv4 static route.

#### Procedure

1. Configure IPv4 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.10.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface LoopBack0
   [*DeviceA-LoopBack0] ip address 1.1.1.1 255.255.255.255
   [*DeviceA-LoopBack0] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176662503__postreq24192593172748).
2. Configure a static route on each device.
   
   
   
   # On DeviceA, configure a static route to 2.2.2.2/32, with DeviceB as a next hop.
   
   ```
   [~DeviceA] ip route-static 2.2.2.2 32 10.10.1.2
   [*DeviceA] commit
   ```
   
   
   
   # On DeviceB, configure a static route to 1.1.1.1/32, with DeviceA as a next hop.
   
   ```
   [~DeviceB] ip route-static 1.1.1.1 32 10.10.1.1
   [*DeviceB] commit
   ```
3. Configure dynamic BFD for static route.
   
   
   
   # On DeviceA, configure dynamic BFD for IPv4 static route destined for 2.2.2.2/32.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] ip route-static bfd 10.10.1.2 local-address 10.10.1.1
   [*DeviceA] ip route-static 2.2.2.2 32 10.10.1.2 bfd enable
   [*DeviceA] commit
   ```
   
   # On DeviceB, configure dynamic BFD for IPv4 static route destined for 1.1.1.1/32.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] ip route-static bfd 10.10.1.1 local-address 10.10.1.2
   [*DeviceB] ip route-static 1.1.1.1 32 10.10.1.1 bfd enable
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# On DeviceA, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command. The command output shows that the BFD state is **Up**.

```
[~DeviceA] display bfd session all verbose
(w): State in WTR  (): State is invalid ------------------------------------------------------------------------------
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
  Min Tx Interval (ms)   : 50            Min Rx Interval (ms) : 50
  Actual Tx Interval (ms): 50               Actual Rx Interval (ms): 50
  Local Detect Multi     : 3             Detect Interval (ms)   : 150
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 4784             TTL                    : 253
  Proc Interface Status  : Disable          Process PST            : Disable
  WTR Interval (ms)      : 0                Local Demand Mode      : Disable
  Active Multi           : 3
  Last Local Diagnostic  : No Diagnostic
  Bind Application     : STATICRT
  Session TX TmrID       : 0                Session Detect TmrID   : 0
  Session Init TmrID     : -                Session WTR TmrID      : -
  Session Echo Tx TmrID  : -
  Session Description    : -
------------------------------------------------------------------------------

     Total UP/DOWN Session Number : 1/0
```

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
   ip address 10.10.1.1 255.255.255.0
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  ip route-static bfd 10.10.1.2 local-address 10.10.1.1
  ip route-static 2.2.2.2 32 10.10.1.2 bfd enable
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
   ip address 10.10.1.2 255.255.255.0
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  ip route-static bfd 10.10.1.1 local-address 10.10.1.2
  ip route-static 1.1.1.1 32 10.10.1.1 bfd enable
  #
  return
  ```