Example for Associating a BFD Session with an Interface
=======================================================

This section provides an example for associating a BFD session with an interface to trigger rapid route convergence if a fault occurs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361718__fig_dc_vrp_bfd_cfg_200301), transmission devices are deployed between DeviceA and DeviceB, each with a BFD session configured. Association between the BFD session status and interface status is configured so that the status change of the BFD session between DeviceA's GE 0/1/0 and DeviceB's GE 0/1/0 affects the protocol status of the interface and triggers fast route convergence when the link between transmission devices fails.

**Figure 1** Association between a BFD session and an interface![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE 0/1/0.

![](figure/en-us_image_0000001461337564.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BFD session on DeviceA.
2. Configure a BFD session on DeviceB.
3. Associate the BFD session and an interface on DeviceA.
4. Associate the BFD session and an interface on DeviceB.

#### Precautions

BFD sessions must be established on both ends.


#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address monitored by BFD
* Local interface that sends and receives BFD packets
* Local and remote discriminators of the BFD session

#### Procedure

1. Assign IP addresses to the interfaces on DeviceA and DeviceB.
   
   
   
   # Assign an IP address to the interface on DeviceA.
   
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
   
   # Assign an IP address to the interface on DeviceB.
   
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
   
   After the configuration is complete, DeviceA and DeviceB can ping each other. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] ping 10.1.1.2
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
   
   
   
   # Enable BFD on DeviceA and establish a BFD session to monitor the link between DeviceA and DeviceB.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd pis bind peer-ip default-ip interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-bfd-session-pis] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-pis] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-pis] commit
   ```
   ```
   [~DeviceA-bfd-session-pis] quit
   ```
   
   # Enable BFD on DeviceB and establish a BFD session to monitor the link between DeviceB and DeviceA.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd pis bind peer-ip default-ip interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-bfd-session-pis] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-pis] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-pis] commit
   ```
   ```
   [~DeviceB-bfd-session-pis] quit
   ```
   
   # After completing the configuration, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA and DeviceB. The command output shows that a single-hop BFD session is established and its status is Up. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : pis
   ------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 224.0.0.184
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
3. Associate the BFD sessions with the interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd pis
   ```
   ```
   [*DeviceA-bfd-session-pis] process-interface-status
   ```
   ```
   [*DeviceA-bfd-session-pis] commit
   ```
   ```
   [~DeviceA-bfd-session-pis] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd pis
   ```
   ```
   [*DeviceB-bfd-session-pis] process-interface-status
   ```
   ```
   [*DeviceB-bfd-session-pis] commit
   ```
   ```
   [~DeviceB-bfd-session-pis] quit
   ```
4. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA and DeviceB. The command output shows that the value of **Proc Interface Status** is **Enable**. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : pis
   ------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 224.0.0.184
     Bind Interface         : GigabitEthernet0/1/0
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Enable       Process PST            : Disable
     WTR Interval (ms)      : 0                 Config PST             : Disable
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
   
   Run the **shutdown** operation on GE 0/1/0 of DeviceC to simulate a transmission device fault. The BFD session goes down.
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
   
   Run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) and [**display interface**](cmdqueryname=display+interface) commands on DeviceA. The command output shows that the BFD session is down and GE 0/1/0 is up.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Down                  Name : pis
   ------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 224.0.0.184
     Bind Interface         : GigabitEthernet0/1/0
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 2100             Actual Rx Interval (ms): 2100
     Local Detect Multi     : 3                Detect Interval (ms)   : 0
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Enable           Process PST            : Disable
     WTR Interval (ms)      : 0                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : Control Detection Time Expired
     Bind Application       : No Application Bind
     Session TX TmrID       : 2725402068       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
   
        Total UP/DOWN Session Number : 0/1
   ```
   ```
   [~DeviceA] display interface gigabitethernet 0/1/0
   ```
   ```
   GigabitEthernet0/1/0 current state : UP (ifindex: 20)
   Line protocol current state : DOWN (BFD status down)  
   Description: 
   Route Port,The Maximum Transmit Unit is 1500
   Internet Address is 10.1.1.2/24
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-7890
   Current BW: 100 Mbits
   Last physical up time   : 2010-07-31 09:35:03
   Last physical down time : 2010-08-03 02:58:22
   Current system time: 2010-08-03 03:02:48
   Statistics last cleared:never
       Last 300 seconds input rate 0 bits/sec, 4 packets/sec
       Last 300 seconds output rate 0 bits/sec, 4 packets/sec
       Input: 0 bytes, 662126 packets
       Output: 0 bytes, 661789 packets
       Input:
         Unicast: 662111 packets, Multicast: 12 packets
         Broadcast: 3 packets, JumboOctets: 0 packets
         CRC: 0 packets, Symbol: 0 packets
         Overrun: 0 packets, InRangeLength: 0 packets
         LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
         Fragment: 0 packets, Undersized Frame: 0 packets
         RxPause: 0 packets
       Output:
         Unicast: 661784 packets, Multicast: 3 packets
         Broadcast: 2 packets, JumboOctets: 0 packets
         Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
         System: 0 packets, Overruns: 0 packets
         TxPause: 0 packets
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
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
  bfd pis bind peer-ip default-ip interface GigabitEthernet0/1/0
   discriminator local 1
   discriminator remote 2
   process-interface-status
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
  bfd pis bind peer-ip default-ip interface GigabitEthernet0/1/0
   discriminator local 2
   discriminator remote 1
   process-interface-status
  #
  return
  ```