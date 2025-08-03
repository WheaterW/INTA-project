Example for Enabling BFD to Modify the PST
==========================================

This section provides an example for enabling BFD to modify the port status table (PST). After the configuration is complete, an upper-layer protocol switches traffic to a backup link if a link fault occurs.

#### Networking Requirements

If BFD is enabled to modify the PST of an interface, BFD will modify the PST when it detects that the interface goes down. This function allows the underlying layer to detect the fault based on the change in the PST.

LDP FRR and IP FRR can obtain a BFD detection result based on a PST change.

On the network shown in [Figure 1](#EN-US_TASK_0172361724__fig_dc_vrp_bfd_cfg_200501), a BFD session in asynchronous mode is established to detect faults in the link between DeviceA and DeviceB.

**Figure 1** Enabling BFD to modify the PST![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE 0/1/0.

![](figure/en-us_image_0000001508150189.png "Click to enlarge")



#### Precautions

BFD sessions must be established on both ends.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable BFD globally on DeviceA and DeviceB.
2. Create single-hop BFD sessions and bind them to the outbound interfaces on DeviceA and DeviceB.
3. Enable BFD to modify the PST.


#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address monitored by BFD
* Local and remote discriminators of the BFD session
* Name of the BFD session


#### Procedure

1. Assign IP addresses to the interfaces on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceB] quit
   ```
   
   After the configuration is complete, DeviceA and DeviceB can ping each other. The following example uses the command output on DeviceA.
   
   ```
   <DeviceA> ping 10.1.1.2
   ```
   ```
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
2. Configure single-hop BFD.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd pst bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-bfd-session-pst] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-pst] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-pst] commit
   ```
   ```
   [~DeviceA-bfd-session-pst] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd pst bind peer-ip 10.1.1.1 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-bfd-session-pst] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-pst] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-pst] commit
   ```
   ```
   [~DeviceB-bfd-session-pst] quit
   ```
   
   After completing the configurations, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA and DeviceB. The command output shows that a single-hop BFD session is established and its status is Up. The following example uses the command output on DeviceB.
   
   ```
   [~DeviceB] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : pst
   ------------------------------------------------------------------------------
     Local Discriminator    : 2                Remote Discriminator   : 1
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.1
     Bind Interface         : GigabitEthernet0/1/0
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : 0                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : 0                Session Detect TmrID   : 0
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 1/0
   ```
3. Enable BFD to modify the PST on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd pst
   ```
   ```
   [*DeviceA-bfd-session-pst] process-pst
   ```
   ```
   [*DeviceA-bfd-session-pst] commit
   ```
   ```
   [~DeviceA-bfd-session-pst] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd pst
   ```
   ```
   [*DeviceB-bfd-session-pst] process-pst
   ```
   ```
   [*DeviceB-bfd-session-pst] commit
   ```
   ```
   [~DeviceB-bfd-session-pst] quit
   ```
4. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA and DeviceB. The command output shows that the value of **Process PST** is **Enable**. The following example uses the command output on DeviceB.
   
   ```
   [~DeviceB] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : pst
   ------------------------------------------------------------------------------
     Local Discriminator    : 2                Remote Discriminator   : 1
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.1
     Bind Interface         : GigabitEthernet0/1/0
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST         : Enable
     WTR Interval (ms)      : 0                Local Demand Mode      : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
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
   ip address 10.1.1.1 255.255.255.0
  #
  bfd pst bind peer-ip 10.1.1.2 interface GigabitEthernet0/1/0
   discriminator local 1
   discriminator remote 2
   process-pst 
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
   ip address 10.1.1.2 255.255.255.0
  #
  bfd pst bind peer-ip 10.1.1.1 interface GigabitEthernet0/1/0
   discriminator local 2
   discriminator remote 1
   process-pst
  #
  return
  ```