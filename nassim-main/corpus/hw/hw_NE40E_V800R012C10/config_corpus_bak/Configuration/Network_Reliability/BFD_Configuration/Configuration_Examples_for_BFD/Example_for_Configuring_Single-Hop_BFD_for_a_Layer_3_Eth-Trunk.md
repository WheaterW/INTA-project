Example for Configuring Single-Hop BFD for a Layer 3 Eth-Trunk
==============================================================

This section provides an example for establishing single-hop BFD sessions on Eth-Trunk interfaces to monitor the directly connected link between the Eth-Trunk interfaces.

#### Networking Requirements

Eth-Trunks enhance link reliability. A BFD session can be configured to monitor an Eth-Trunk link on a network for quick fault detection. As shown in [Figure 1](#EN-US_TASK_0172361684__fig_dc_vrp_bfd_cfg_006001), the Eth-Trunk connecting DeviceA and DeviceB consists of two GE links.

This example requires BFD to be performed over the Eth-Trunk.

**Figure 1** Single-hop BFD for a Layer 3 Eth-Trunk![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.

  
![](figure/en-us_image_0000001458789380.png)  




#### Precautions

BFD sessions must be established on both ends.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Eth-Trunk interface on both the local and remote devices.
2. Configure single-hop BFD for an Eth-Trunk.

#### Data Preparation

To complete the configuration, you need the following data:

* Local Eth-Trunk interface that sends and receives BFD control packets
* Peer IP address monitored by BFD (the IP address of the Eth-Trunk interface)
* Name of the BFD session for monitoring the Eth-Trunk
* Local and remote discriminators of the BFD session

#### Procedure

1. Configure an Eth-Trunk interface.
   
   
   
   # Create an Eth-Trunk interface on DeviceA.
   
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
   [~DeviceA] interface eth-trunk 1
   ```
   ```
   [*DeviceA-Eth-Trunk1] undo shutdown
   ```
   ```
   [*DeviceA-Eth-Trunk1] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-Eth-Trunk1] commit
   ```
   ```
   [~DeviceA-Eth-Trunk1] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-Gigabitethernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] eth-trunk 1
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] commit
   ```
   ```
   [~DeviceA-Gigabitethernet0/1/0] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-Gigabitethernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-Gigabitethernet0/2/0] eth-trunk 1
   ```
   ```
   [*DeviceA-Gigabitethernet0/2/0] commit
   ```
   ```
   [~DeviceA-Gigabitethernet0/2/0] quit
   ```
   
   # Create an Eth-Trunk interface on DeviceB.
   
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
   [~DeviceB] interface eth-trunk 1
   ```
   ```
   [*DeviceB-Eth-Trunk1] undo shutdown
   ```
   ```
   [*DeviceB-Eth-Trunk1] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-Eth-Trunk1] commit
   ```
   ```
   [~DeviceB-Eth-Trunk1] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-Gigabitethernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-Gigabitethernet0/1/0] eth-trunk 1
   ```
   ```
   [*DeviceB-Gigabitethernet0/1/0] commit
   ```
   ```
   [~DeviceB-Gigabitethernet0/1/0] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceB-Gigabitethernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceB-Gigabitethernet0/2/0] eth-trunk 1
   ```
   ```
   [*DeviceB-Gigabitethernet0/2/0] commit
   ```
   ```
   [~DeviceB-Gigabitethernet0/2/0] quit
   ```
   
   After completing the configurations, run the **display interface eth-trunk** command on DeviceA or DeviceB. The command output shows that the interface is up.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display interface eth-trunk 1
   ```
   ```
   Eth-Trunk1 current state : UP (ifindex: 19)
   Line protocol current state : UP
   Last line protocol up time : 2015-08-04 08:34:41
   Link quality grade : GOOD
   Description: 
   Route Port,Hash arithmetic : According to flow,Maximal BW: 100M, Current BW: 100
   M, The Maximum Transmit Unit is 1500
   Internet Address is 10.1.1.1/24
   IP Sending Frames' Format is ***, Hardware address is xxxx-xxxx-xxxx
   Current system time: 2010-08-04 08:35:02
   Physical is ETH_TRUNK
       Last 300 seconds input rate 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate 0 bits/sec, 0 packets/sec
       Input: 0 packets,0 bytes
              0 unicast,0 broadcast,0 multicast
              0 errors,0 drops
       Output:0 packets,0 bytes
              0 unicast,0 broadcast,0 multicast
              0 errors,0 drops
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   
   -----------------------------------------------------
   PortName                Status              Weight
   -----------------------------------------------------
   Gigabitethernet0/1/0    UP                  1
   Gigabitethernet0/2/0    UP                  1
   -----------------------------------------------------
   The Number of Ports in Trunk : 2
   The Number of UP Ports in Trunk : 2 
   
   ```
   
   Eth-Trunk interfaces on DeviceA and DeviceB can ping each other.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] ping -a 10.1.1.1 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=31 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=31 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=62 ms
   ```
   ```
     --- 10.1.1.2 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 31/49/62 ms
   ```
2. Configure single-hop BFD for an Eth-Trunk.
   
   
   
   # Enable BFD on DeviceA and establish a BFD session to monitor the link between DeviceA and DeviceB. Bind the BFD session to the Eth-Trunk interface.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd atob bind peer-ip 10.1.1.2 interface eth-trunk 1
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator local 10
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator remote 20
   ```
   ```
   [*DeviceA-bfd-session-atob] commit
   ```
   ```
   [~DeviceA-bfd-session-atob] quit
   ```
   
   # Enable BFD on DeviceB and establish a BFD session to monitor the link between DeviceB and DeviceA. Bind the BFD session to the Eth-Trunk interface.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd btoa bind peer-ip 10.1.1.1 interface eth-trunk 1
   ```
   ```
   [*DeviceB-bfd-session-btoa] discriminator local 20
   ```
   ```
   [*DeviceB-bfd-session-btoa] discriminator remote 10
   ```
   ```
   [*DeviceB-bfd-session-btoa] commit
   ```
   ```
   [~DeviceB-bfd-session-btoa] quit
   ```
3. Verify the configuration.
   
   
   
   After completing the configurations, run the **display bfd session all verbose** command on DeviceA and DeviceB. The command output shows that a single-hop BFD session is established and its status is Up.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
      (One Hop) State : Up                       Name : atob
   ------------------------------------------------------------------------------
     Local Discriminator    : 10               Remote Discriminator    : 20
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(Eth-Trunk1)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.2
     Bind Interface         : Eth-Trunk1
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
     Session TX TmrID       : 2584985432       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
          Total UP/DOWN Session Number : 1/0
   
   ```
   
   # Run the **shutdown** command on GE 0/1/0 of DeviceA to simulate a link fault.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-Gigabitethernet0/1/0] shutdown
   ```
   ```
   [*DeviceA-Gigabitethernet0/1/0] commit
   ```
   ```
   [~DeviceA-Gigabitethernet0/1/0] quit
   ```
   
   Run the **display bfd session all verbose** and **display interface eth-trunk** commands on DeviceA and DeviceB. The command output shows that the BFD session and Eth-Trunk interface are up.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   (One Hop) State : Up                        Name : atob
   ------------------------------------------------------------------------------
     Local Discriminator    : 10              Remote Discriminator   : 20
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(Eth-Trunk1)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.2
     Bind Interface         : Eth-Trunk1
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255  
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : 0                Local Demand Mode      : Disable
     Active Multi           : 3
     Last Local Diagnostic  : Control Detection Time Expired
     Bind Application       : No Application Bind
     Session TX TmrID       : 2584985432       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
   Total UP/DOWN Session Number : 1/0
   
   ```
   ```
   [~DeviceA] display interface eth-trunk 1
   ```
   ```
   Eth-Trunk1 current state : UP
   Line protocol current state : UP
   Description : 
   Hash arithmetic : According to flow,Maximal BW: 200M, Current BW: 0M
   The Maximum Transmit Unit is 1500 bytes
   Internet Address is 10.1.1.1/24
   IP Sending Frames' Format is ***, Hardware address is xxxx-xxxx-xxxx
   Physical is ETH_TRUNK
   Last 300 seconds input rate 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate 0 bits/sec, 0 packets/sec
       Realtime 0 seconds input rate 0 bits/sec, 0 packets/sec
       Realtime 0 seconds output rate 0 bits/sec, 0 packets/sec
       Input: 0 packets,0 bytes,
              0 unicast,0 broadcast,0 multicast
              0 errors,0 drops,0 unknownprotocol
       Output:0 packets,0 bytes,
              0 unicast,0 broadcast,0 multicast
              0 errors,0 drops
   -----------------------------------------------------
   PortName                Status              Weight
   -----------------------------------------------------
   Gigabitethernet0/1/0    DOWN                1
   Gigabitethernet0/2/0    UP                  1
   -----------------------------------------------------
   The Number of Ports in Trunk : 2
   The Number of UP Ports in Trunk : 1 
   ```
   
   # Run the **shutdown** command on GE 0/2/0 of DeviceA to simulate a link fault.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-Gigabitethernet0/2/0] shutdown
   ```
   ```
   [*DeviceA-Gigabitethernet0/2/0] commit
   ```
   ```
   [~DeviceA-Gigabitethernet0/2/0] quit
   ```
   
   Run the **display bfd session all verbose** and **display interface eth-trunk** commands on DeviceA and DeviceB. The command output shows that the BFD session and Eth-Trunk interface are both down.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
      (One Hop) State : Down                       Name : atob
   ------------------------------------------------------------------------------
     Local Discriminator    : 10               Remote Discriminator    : 20
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(Eth-Trunk1)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.2
     Bind Interface         : Eth-Trunk1
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255  
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : 0                Local Demand Mode      : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : 2584985432       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
          Total UP/DOWN Session Number : 0/1
   
   ```
   ```
   [~DeviceA] display interface eth-trunk 1
   ```
   ```
   Eth-Trunk1 current state : DOWN
   Line protocol current state : DOWN
   Description : 
   Hash arithmetic : According to flow,Maximal BW: 200M, Current BW: 0M
   The Maximum Transmit Unit is 1500 bytes
   Internet Address is 10.1.1.1/24
   IP Sending Frames' Format is ***, Hardware address is xxxx-xxxx-xxxx
   Physical is ETH_TRUNK
   Last 300 seconds input rate 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate 0 bits/sec, 0 packets/sec
       Realtime 0 seconds input rate 0 bits/sec, 0 packets/sec
       Realtime 0 seconds output rate 0 bits/sec, 0 packets/sec
       Input: 0 packets,0 bytes,
              0 unicast,0 broadcast,0 multicast
              0 errors,0 drops,0 unknownprotocol
       Output:0 packets,0 bytes,
              0 unicast,0 broadcast,0 multicast
              0 errors,0 drops
   -----------------------------------------------------
   PortName                Status              Weight
   -----------------------------------------------------
   Gigabitethernet0/1/0    DOWN                1
   Gigabitethernet0/2/0    DOWN                1
   -----------------------------------------------------
   The Number of Ports in Trunk : 2
   The Number of UP Ports in Trunk : 0 
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  bfd
  ```
  ```
  #
  ```
  ```
  interface Eth-Trunk1
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  bfd atob bind peer-ip 10.1.1.2 interface Eth-Trunk 1
  ```
  ```
   discriminator local 10
  ```
  ```
   discriminator remote 20
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  bfd
  ```
  ```
  #
  ```
  ```
  interface Eth-Trunk1
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  bfd btoa bind peer-ip 10.1.1.1 interface Eth-Trunk 1
  ```
  ```
   discriminator local 20
  ```
  ```
   discriminator remote 10
  ```
  ```
  return
  ```