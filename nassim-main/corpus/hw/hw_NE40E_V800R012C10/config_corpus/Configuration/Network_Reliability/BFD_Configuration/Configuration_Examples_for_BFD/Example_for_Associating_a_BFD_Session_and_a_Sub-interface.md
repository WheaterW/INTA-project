Example for Associating a BFD Session and a Sub-interface
=========================================================

This section provides an example for associating a BFD session with a sub-interface to improve service reliability on the sub-interface.

#### Networking Requirements

On the large metro Ethernet network shown in [Figure 1](#EN-US_TASK_0172361721__fig_dc_vrp_bfd_cfg_200401), a large number of VLAN services are configured on an interface's sub-interfaces and high reliability is required. Establish a BFD session to monitor the interface's link continuity, and associate the BFD session with the sub-interface. This configuration improves service reliability on the sub-interface and saves BFD session resources.

**Figure 1** Association between a BFD session and a sub-interface![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE 0/1/0.

  
![](figure/en-us_image_0000001508389137.png)  




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BFD session on DeviceA.
2. Configure a BFD session on DeviceB.
3. Associate the BFD session status with the sub-interface status on DeviceA.
4. Associate the BFD session status with the sub-interface status on DeviceB.

#### Precautions

BFD sessions must be established on both ends.


#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address monitored by BFD
* Local interface that sends and receives BFD control packets
* Local and remote discriminators of the BFD session

#### Procedure

1. Assign IP addresses to interfaces on DeviceA and DeviceB, and create sub-interfaces.
   
   
   
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
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] ip address 10.2.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] quit
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
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0.1] ip address 10.2.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0.1] quit
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
   [*DeviceA] bfd pissub bind peer-ip default-ip interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-bfd-session-pissub] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-pissub] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-pissub] commit
   ```
   ```
   [~DeviceA-bfd-session-pissub] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd pissub bind peer-ip default-ip interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-bfd-session-pissub] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-pissub] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-pissub] commit
   ```
   ```
   [~DeviceB-bfd-session-pissub] quit
   ```
   
   # After completing the configurations, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA and DeviceB. The command output shows that a single-hop BFD session is established and its status is Up. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : pissub
   ---------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.2
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
3. Associate the BFD sessions with the sub-interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd pissub 
   ```
   ```
   [*DeviceA-bfd-session-pissub] process-interface-status sub-if
   ```
   ```
   [*DeviceA-bfd-session-pissub] commit
   ```
   ```
   [~DeviceA-bfd-session-pissub] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [*DeviceB] bfd pissub
   ```
   ```
   [*DeviceB-bfd-session-pissub] process-interface-status sub-if
   ```
   ```
   [*DeviceB-bfd-session-pissub] commit
   ```
   ```
   [~DeviceB-bfd-session-pissub] quit
   ```
4. Verify the configuration.
   
   
   
   # After completing the configuration, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA and DeviceB. The command output shows that the value of **Proc Interface Status** is **Enable (Sub-If)**. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : pissub
   ------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.2
     Bind Interface         : GigabitEthernet0/1/0
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Enable (Sub-If) Process PST            : Disable
     WTR Interval (ms)      : 0                Local Demand Mode      : Disable
     Active Multi           : 3
     Last Local Diagnostic  : Control Detection Time Expired
     Bind Application       : No Application Bind
     Session TX TmrID       : 0                Session Detect TmrID   : 0
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 1/0
   
   ```
   
   # Run the **shutdown** command on GE 0/1/0 of Device B. The command output shows that the BFD session is down.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) and [**display interface**](cmdqueryname=display+interface) commands on DeviceA. The command output shows that the BFD session is down and GE 0/1/0.1 is up.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Down                  Name : pissub
   ------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.2
     Bind Interface         : GigabitEthernet0/1/0
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Enable (Sub-If)  Process PST            : Disable
     WTR Interval (ms)      : 0                Local Demand Mode      : Disable
     Active Multi           : 3
     Last Local Diagnostic  : Control Detection Time Expired
     Bind Application       : No Application Bind
     Session TX TmrID       : 0                Session Detect TmrID   : 0
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 0/1
   ```
   ```
   [~DeviceA] display interface gigabitethernet 0/1/0.1
   ```
   ```
   GigabitEthernet0/1/0.1 current state : DOWN (ifindex: 33)
   Line protocol current state : DOWN (Main BFD status down)
   Last line protocol up time :  2013-07-29 15:39:29
   Description: 
   Route Port,The Maximum Transmit Unit is 9600
   Internet Address is 10.2.1.1/24
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-7890
   Last physical up time   :  2013-07-29 15:39:23
   Last physical down time : 2013-07-29 15:38:41
   Current system time: 2013-07-30 09:15:33
   Statistics last cleared:never
         Last 600 seconds input rate: 23513 bits/sec, 2 packets/sec
         Last 600 seconds output rate: 64319 bits/sec, 3 packets/sec
         Input peak rate 26099 bits/sec, Record time: 2013-07-29 15:40:58
         Output peak rate 64809 bits/sec, Record time: 2013-07-30 03:59:41
         Input: 183126871 bytes, 182525 packets 
         Output: 509287017 bytes, 244628 packets
       Input:
         Unicast: 55 packets, Multicast: 160762 packets
         Broadcast: 21708 packets, JumboOctets: 31031 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 53 packets, Multicast: 243990 packets
         Broadcast: 585 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
   
   
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
  interface GigabitEthernet0/1/0.1
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
  #
  bfd pissub bind peer-ip default-ip interface GigabitEthernet0/1/0
   discriminator local 1
   discriminator remote 2
   process-interface-status sub-if
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
  interface GigabitEthernet0/1/0.1
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  bfd pissub bind peer-ip default-ip interface GigabitEthernet0/1/0
   discriminator local 2
   discriminator remote 1
   process-interface-status sub-if
  #
  return
  ```