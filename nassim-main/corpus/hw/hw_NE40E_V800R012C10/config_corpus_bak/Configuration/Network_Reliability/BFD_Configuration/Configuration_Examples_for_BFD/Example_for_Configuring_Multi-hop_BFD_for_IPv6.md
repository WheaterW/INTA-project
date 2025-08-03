Example for Configuring Multi-hop BFD for IPv6
==============================================

This section provides an example for configuring multi-hop BFD for IPv6 to monitor an IPv6 link on a network for quick fault detection.

#### Networking Requirements

To rapidly detect faults in an IPv6 link on a network, establish a multi-hop BFD session for IPv6. On the network shown in [Figure 1](#EN-US_TASK_0172361697__fig_dc_vrp_bfd_cfg_200701), a multi-hop BFD session in asynchronous mode is established to detect faults in the link between DeviceA and DeviceC.

**Figure 1** Multi-hop BFD for IPv6![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_bfd_cfg_200701.png)  


#### Precautions

BFD sessions for IPv6 must be established on both ends.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable BFD globally on DeviceA and DeviceC.
2. Configure multi-hop BFD for IPv6 on DeviceA to monitor the link from DeviceA to DeviceC.
3. Configure multi-hop BFD for IPv6 on DeviceC to monitor the link from DeviceC to DeviceA.


#### Data Preparation

To complete the configuration, you need the following data:

* Peer IPv6 address monitored by BFD
* Local and remote discriminators of the BFD session
* Name of the BFD session


#### Procedure

1. Assign an IPv6 address to each interface on DeviceA, DeviceB, and DeviceC, and configure Open Shortest Path First version 3 (OSPFv3) to ensure that these devices communicate with each other.
   
   
   
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
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
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
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-ospfv3-1] area 0
   ```
   ```
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospfv3-1] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::1 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] ospfv3 1
   ```
   ```
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-ospfv3-1] area 0
   ```
   ```
   [*DeviceC-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceC-ospfv3-1] quit
   ```
   ```
   [~DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::2 64
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   
   After the configuration is complete, DeviceA and DeviceC can ping each other. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] ping ipv6 2001:db8:2::2
   ```
   ```
   PING 2001:db8:2::2 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:2::2
       bytes=56 Sequence=1 hop limit=64 time=22 ms
       Reply from 2001:db8:2::2
       bytes=56 Sequence=2 hop limit=64 time=1 ms
       Reply from 2001:db8:2::2
       bytes=56 Sequence=3 hop limit=64 time=1 ms
       Reply from 2001:db8:2::2
       bytes=56 Sequence=4 hop limit=64 time=1 ms
   
       Reply from 2001:db8:2::2
       bytes=56 Sequence=5 hop limit=64 time=1 ms
     ---2001:db8:2::2 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=1/5/22 ms
   ```
2. Configure multi-hop BFD for IPv6 on DeviceA and DeviceC.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd ipv6session bind peer-ipv6 2001:db8:2::2
   ```
   ```
   [*DeviceA-bfd-session-ipv6session] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-ipv6session] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-ipv6session] commit
   ```
   ```
   [~DeviceA-bfd-session-ipv6session] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bfd
   ```
   ```
   [*DeviceC-bfd] quit
   ```
   ```
   [*DeviceC] bfd ipv6session bind peer-ipv6 2001:db8:1::1
   ```
   ```
   [*DeviceC-bfd-session-ipv6session] discriminator local 2
   ```
   ```
   [*DeviceC-bfd-session-ipv6session] discriminator remote 1
   ```
   ```
   [*DeviceC-bfd-session-ipv6session] commit
   ```
   ```
   [~DeviceC-bfd-session-ipv6session] quit
   ```
3. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA and DeviceC. The command output shows that a multi-hop BFD session for IPv6 is established and its status is Up. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (Multi Hop) State : UP                  Name : ipv6session
   ------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Peer IP Address
     Bind Session Type      : Static
     Bind Peer IP Address   : 2001:db8:2::2
     Bind Interface         : -
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 4784             TTL                    : 254
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : 0                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : 2720409460       Session Detect TmrID   : -
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
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   ospfv3 1 area 0.0.0.0
  #
  bfd ipv6session bind peer-ipv6 2001:db8:2::2
   discriminator local 1
   discriminator remote 2
  return
  
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   ospfv3 1 area 0.0.0.0
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  bfd ipv6session bind peer-ipv6 2001:db8:1::1/64
   discriminator local 2
   discriminator remote 1
  return
  ```