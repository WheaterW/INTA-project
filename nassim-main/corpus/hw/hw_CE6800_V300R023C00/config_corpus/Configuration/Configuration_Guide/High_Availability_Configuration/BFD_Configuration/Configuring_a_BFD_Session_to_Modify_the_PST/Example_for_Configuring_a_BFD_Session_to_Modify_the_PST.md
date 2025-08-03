Example for Configuring a BFD Session to Modify the PST
=======================================================

Example for Configuring a BFD Session to Modify the PST

#### Networking Requirements

If a BFD session is enabled to modify the port state table (PST) of an interface, the BFD session will modify the interface status in the PST when it detects that the interface goes down, allowing the underlying layer to detect the fault based on the PST change. In [Figure 1](#EN-US_TASK_0000001621812918__fig_dc_vrp_bfd_cfg_200501), a BFD session monitors the direct link between DeviceA and DeviceB in asynchronous mode.

**Figure 1** Network diagram of configuring a BFD session to modify the PST![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001670572809.png)

#### Precautions

A BFD session must be established on both ends.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to the interfaces connecting DeviceA and DeviceB.
2. Enable BFD globally and configure single-hop BFD on DeviceA and DeviceB.
3. Configure BFD sessions to modify the PST on DeviceA and DeviceB.


#### Procedure

1. Assign IP addresses to the interfaces connecting DeviceA and DeviceB.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
2. Enable BFD globally and configure single-hop BFD on DeviceA and DeviceB.
   
   # Configure a BFD session between DeviceA and DeviceB.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd pst bind peer-ip 10.1.1.2 interface 100ge 1/0/1
   [*DeviceA-bfd-session-pst] discriminator local 1
   [*DeviceA-bfd-session-pst] discriminator remote 2
   [*DeviceA-bfd-session-pst] quit
   [*DeviceA] commit
   ```
   
   # Configure a BFD session between DeviceB and DeviceA.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd pst bind peer-ip 10.1.1.1 interface 100ge 1/0/1
   [*DeviceB-bfd-session-pst] discriminator local 2
   [*DeviceA-bfd-session-pst] discriminator remote 1
   [*DeviceB-bfd-session-pst] quit
   [*DeviceB] commit
   ```
3. Configure BFD sessions to modify the PST on DeviceA and DeviceB.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd pst
   [*DeviceA-bfd-session-pst] process-pst
   [*DeviceA-bfd-session-pst] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd pst
   [*DeviceB-bfd-session-pst] process-pst
   [*DeviceB-bfd-session-pst] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check that DeviceA and DeviceB can ping each other. The command output on DeviceA is used as an example.
```
<DeviceA> ping 10.1.1.2
PING 10.1.1.2 : 56  data bytes, press CTRL_C to break
    Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=3 ms
    Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=1 ms
    Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=1 ms
    Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
    Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=1 ms

  --- 10.1.1.2 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 1/1/3 ms          
```

# Run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceB to check the BFD session status.

```
[~DeviceB] display bfd session all verbose
(w): State in WTR 
(*): State is invalid
------------------------------------------------------------------------------
  (Single Hops)   State : Up                    Name : pst
------------------------------------------------------------------------------
  Local Discriminator    : 2                Remote Discriminator   : 1
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Interface(100GE1/0/1)
  BFD Bind Type          :
Bind Session Type      : Static
  Bind Peer IP Address   : 10.1.1.1
  Bind Interface         : 100GE1/0/1
  Bind Interface         : 
  FSM Board ID           : 1               TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000      Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
  WTR Interval (ms)      : 0                Detect Interval (ms)   : 30
  Local Detect Multi     : 3                Active Multi           : 3               
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 3784             TTL                    : 255
  Proc Interface Status  : Disable          Process PST         : Enable
  Config PST             : Enable    
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : No Application Bind
  Session TX TmrID       : 0                Session Detect TmrID   : 0
  Session Init TmrID     : -                Session WTR TmrID      : -
  Session Echo Tx TmrID  : -
  Session Description    : -
------------------------------------------------------------------------------

     Total UP/DOWN Session Number : 1/0
```

The command output on DeviceB shows that a single-hop BFD session has been established on DeviceB and is in the up state, and **Enable** is displayed in the **Process PST** field.


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
  bfd pst bind peer-ip 10.1.1.2 interface 100GE1/0/1
   discriminator local 1
   discriminator remote 2
   process-pst
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
  bfd pst bind peer-ip 10.1.1.1 interface 100GE1/0/1
   discriminator local 2
   discriminator remote 1
   process-pst
  #
  return
  ```