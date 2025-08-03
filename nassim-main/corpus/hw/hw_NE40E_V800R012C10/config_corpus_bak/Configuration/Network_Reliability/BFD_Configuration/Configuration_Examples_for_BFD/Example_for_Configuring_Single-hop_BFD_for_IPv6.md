Example for Configuring Single-hop BFD for IPv6
===============================================

This section provides an example for configuring single-hop BFD for IPv6 to monitor an IPv6 link on a network for quick fault detection.

#### Networking Requirements

To rapidly detect faults in an IPv6 link on a network, establish a single-hop BFD session for IPv6. On the network shown in [Figure 1](#EN-US_TASK_0172361694__fig_dc_vrp_bfd_cfg_200601), a single-hop BFD session in asynchronous mode is established to detect faults in the link between DeviceA and DeviceB.

**Figure 1** Single-hop BFD for IPv6![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE 0/1/0.

  
![](figure/en-us_image_0000001508150193.png)  




#### Precautions

BFD sessions for IPv6 must be established on both ends.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable BFD globally on DeviceA and DeviceB.
2. Create single-hop BFD sessions for IPv6 and bind them to the outbound interfaces on DeviceA and DeviceB.


#### Data Preparation

To complete the configuration, you need the following data:

* Peer IPv6 address monitored by BFD
* Local and remote discriminators of the BFD session
* Name of the BFD session


#### Procedure

1. Assign IPv6 addresses to interfaces on DeviceA and DeviceB.
   
   
   
   # Assign an IPv6 address to the interface on DeviceA.
   
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
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8::1 32
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Assign an IPv6 address to the interface on DeviceB.
   
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
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8::2 32
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   After the configuration is complete, DeviceA and DeviceB can ping each other. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] ping ipv6 2001:db8::2
   ```
   ```
   PING 2001:db8::2 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8::2
       bytes=56 Sequence=1 hop limit=64 time=3 ms
       Reply from 2001:db8::2
       bytes=56 Sequence=2 hop limit=64 time=1 ms
       Reply from 2001:db8::2
       bytes=56 Sequence=3 hop limit=64 time=1 ms
       Reply from 2001:db8::2
       bytes=56 Sequence=4 hop limit=64 time=1 ms
       Reply from 2001:db8::2
       bytes=56 Sequence=5 hop limit=64 time=1 ms
     ---2001:db8::2 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=1/1/3 ms
   ```
2. Configure single-hop BFD for IPv6.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd ipv6session bind peer-ipv6 2001:db8::2 interface gigabitethernet 0/1/0
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
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd ipv6session bind peer-ipv6 2001:db8::1 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-bfd-session-ipv6session] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-ipv6session] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-ipv6session] commit
   ```
   ```
   [~DeviceB-bfd-session-ipv6session] quit
   ```
3. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA and DeviceB. The command output shows that a single-hop BFD session for IPv6 is established and its status is Up. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : ipv6session
   ------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 2001:db8::2
     Bind Interface         : GigabitEthernet0/1/0
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : 0                Config PST      : Disable
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
   ipv6 enable
   ipv6 address 2001:db8::1/32
  #
  bfd ipv6session bind peer-ipv6 2001:db8::2 interface GigabitEthernet0/1/0
   discriminator local 1
   discriminator remote 2
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
   ipv6 enable
   ipv6 address 2001:db8::2/32
  #
  bfd ipv6session bind peer-ipv6 2001:db8::1 interface GigabitEthernet0/1/0
   discriminator local 2
   discriminator remote 1
  #
  return
  ```