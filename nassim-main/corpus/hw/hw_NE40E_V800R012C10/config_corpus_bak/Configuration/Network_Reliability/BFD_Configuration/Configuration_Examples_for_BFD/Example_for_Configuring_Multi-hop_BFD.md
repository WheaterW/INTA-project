Example for Configuring Multi-hop BFD
=====================================

This section provides an example for configuring multi-hop BFD to monitor a multi-hop link on a network for quick fault detection.

#### Networking Requirements

A BFD session can be configured to monitor a multi-hop link on a network for quick fault detection. As shown in [Figure 1](#EN-US_TASK_0172361691__fig_dc_vrp_bfd_cfg_006301), a BFD session in asynchronous mode is established to detect faults in the multi-hop link between DeviceA and DeviceC.

**Figure 1** Multi-hop BFD![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.

  
![](figure/en-us_image_0000001458469528.png)  




#### Precautions

BFD sessions must be established on both ends.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BFD session on DeviceA to monitor the multi-hop link from DeviceA to DeviceC.
2. Configure a BFD session on DeviceC to monitor the multi-hop link from DeviceC to DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address monitored by BFD
* Name of the BFD session for monitoring the multi-hop link
* Local and remote discriminators of the BFD session

#### Procedure

1. Configure DeviceA, DeviceB, and DeviceC to be routable.
   
   
   
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
   [~DeviceA] interface GigabitEthernet 0/1/0
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
   
   # Assign IP addresses to the interfaces on DeviceB.
   
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
   [~DeviceB] interface GigabitEthernet 0/1/0
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
   [~DeviceB] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
   
   # Assign an IP address to the interface on DeviceC.
   
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
   [~DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ip address 10.2.1.2 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
   
   # Configure static routes.
   
   ```
   [~DeviceA] ip route-static 10.2.1.0 255.255.255.0 10.1.1.2
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceC] ip route-static 10.1.1.0 255.255.255.0 10.2.1.1 
   ```
   ```
   [*DeviceC] commit
   ```
2. Configure BFD to monitor the multi-hop link between DeviceA and DeviceC.
   
   
   
   # Enable BFD on DeviceA and establish a BFD session to monitor the link between DeviceA and DeviceC. You do not need to bind the BFD session to an interface.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd atoc bind peer-ip 10.2.1.2
   ```
   ```
   [*DeviceA-bfd-session-atoc] discriminator local 10
   ```
   ```
   [*DeviceA-bfd-session-atoc] discriminator remote 20
   ```
   ```
   [*DeviceA-bfd-session-atoc] commit
   ```
   ```
   [~DeviceA-bfd-session-atoc] quit
   ```
   
   # Enable BFD on DeviceC and establish a BFD session to monitor the link between DeviceC and DeviceA. You do not need to bind the BFD session to an interface.
   
   ```
   [~DeviceC] bfd
   ```
   ```
   [*DeviceC-bfd] quit
   ```
   ```
   [*DeviceC] bfd ctoa bind peer-ip 10.1.1.1
   ```
   ```
   [*DeviceC-bfd-session-ctoa] discriminator local 20
   ```
   ```
   [*DeviceC-bfd-session-ctoa] discriminator remote 10
   ```
   ```
   [*DeviceC-bfd-session-ctoa] commit
   ```
   ```
   [~DeviceC-bfd-session-ctoa] quit
   ```
3. Verify the configuration.
   
   
   
   After completing the configurations, run the **display bfd session all verbose** command on DeviceA and DeviceC. The command output shows that a multi-hop BFD session is established and its status is Up.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (Multi Hop)  State : Up                       Name : atoc
   ------------------------------------------------------------------------------
     Local Discriminator    : 10             Remote Discriminator    : 20
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Peer Ip Address
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.2.1.2
     Bind Interface         : -   
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 4784             TTL                    : 254  
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : 0                Config PST      : Disable
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
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   Run the **display bfd session all verbose** command on DeviceA and DeviceC. The command output shows that the status of the BFD session is Down.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
     (Multi Hop)  State : Down                       Name : atoc
   ------------------------------------------------------------------------------
     Local Discriminator    : 10             Remote Discriminator    : 20
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Peer Ip Address
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.2.1.2
     Bind Interface         : -   
     FSM Board Id           : 1                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): -                Actual Rx Interval (ms): -
     Local Detect Multi     : 3                Detect Interval (ms)   : -
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 4784             TTL                    : 254  
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST      : Disable
     Active Multi           : -
     Last Local Diagnostic  : Control Detection Time Expired
     Bind Application       : No Application Bind
     Session TX TmrID       : 2584985432       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------
          Total UP/DOWN Session Number : 0/1
   
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ip route-static 10.2.1.0 255.255.255.0 10.1.1.2
  ```
  ```
  #
  ```
  ```
  bfd atoc bind peer-ip 10.2.1.2
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
  #
  ip route-static 10.1.1.0 255.255.255.0 10.2.1.1
  ```
  ```
  #
  ```
  ```
  bfd ctoa bind peer-ip 10.1.1.1
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