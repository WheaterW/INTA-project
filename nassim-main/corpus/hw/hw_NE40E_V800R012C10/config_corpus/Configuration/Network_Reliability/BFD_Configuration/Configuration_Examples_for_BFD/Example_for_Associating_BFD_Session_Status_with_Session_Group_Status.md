Example for Associating BFD Session Status with Session Group Status
====================================================================

In this example, the BFD session status is associated with the session group status to implement fast switching upon multiple points of failure on a segmented cascaded network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001342880277__fig_dc_vrp_bfd_cfg_200401), transmission devices exist on the link. When the link between transmission devices fails, fast switching upon multiple points of failure is required on the segmented cascaded network. BFD session 1 is established between DeviceA and DeviceB, BFD session 2 is established between DeviceB and DeviceD, and BFD session 3 is established between DeviceB and DeviceC. BFD session 1 and BFD session 2 are added to the session group on DeviceB. After BFD session 3 is associated with the BFD session group, the status change of the BFD session group on DeviceB affects the status of the session between DeviceB and DeviceC.

**Figure 1** Association between the BFD session status and the session group status![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.

![](figure/en-us_image_0000001458469524.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BFD session 1 between DeviceA and DeviceB, BFD session 2 between DeviceB and DeviceD, and BFD session 3 between DeviceB and DeviceC.
2. Add BFD sessions to a session group on DeviceB.
3. Associate the session status with the session group status on DeviceB.

#### Precautions

BFD sessions must be established on both ends.


#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address monitored by BFD
* Local interface that sends and receives BFD packets
* Local and remote discriminators of BFD sessions

#### Procedure

1. Assign IP addresses to the directly connected interfaces on DeviceA, DeviceB, DeviceC, and DeviceD.
   
   
   
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
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/2/0
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
   ```
   [~DeviceB] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] ip address 10.3.1.1 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] quit
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
   [~DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ip address 10.2.1.2 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceD
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceD] interface gigabitethernet 0/3/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/3/0] undo shutdown
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ip address 10.3.1.2 24
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/3/0] quit
   ```
2. Configure single-hop BFD.
   
   
   
   # Configure a BFD session between DeviceA and DeviceB.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd singlehop1 bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-bfd-session-singlehop1] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-singlehop1] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-singlehop1] commit
   ```
   ```
   [~DeviceA-bfd-session-singlehop1] quit
   ```
   
   # Configure a BFD session between DeviceB and DeviceA, and between DeviceB and DeviceD.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd singlehop1 bind peer-ip 10.1.1.1 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-bfd-session-singlehop1] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-singlehop1] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-singlehop1] commit
   ```
   ```
   [~DeviceB-bfd-session-singlehop1] quit
   ```
   ```
   [*DeviceB] bfd singlehop bind peer-ip 10.3.1.2 interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceB-bfd-session-singlehop2] discriminator local 3
   ```
   ```
   [*DeviceB-bfd-session-singlehop2] discriminator remote 4
   ```
   ```
   [*DeviceB-bfd-session-singlehop2] commit
   ```
   ```
   [~DeviceB-bfd-session-singlehop2] quit
   ```
   
   # Configure a BFD session between DeviceD and DeviceB.
   
   ```
   [~DeviceD] bfd
   ```
   ```
   [*DeviceD-bfd] quit
   ```
   ```
   [*DeviceD] bfd singlehop2 bind peer-ip 10.3.1.1 interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceD-bfd-session-singlehop2] discriminator local 4
   ```
   ```
   [*DeviceD-bfd-session-singlehop2] discriminator remote 3
   ```
   ```
   [*DeviceD-bfd-session-singlehop2] commit
   ```
   ```
   [~DeviceD-bfd-session-singlehop2] quit
   ```
   
   # After completing the configurations, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceA, DeviceB, and DeviceD. The command output shows that a single-hop BFD session has been established on each device and its status is Up. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all verbose
   (w): State in WTR
   (*): State is invalid
   --------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : singlehop1
   --------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : 2
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.2
     Bind Interface         : gigabitethernet0/1/0
     Track Interface        : -
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 2027             Actual Rx Interval (ms): 2027
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : 4022103096       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   ------------------------------------------------------------------------------ 
    
        Total UP/DOWN Session Number : 1/0
   ```
3. Add BFD sessions to a session group on DeviceB.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd-track-manager 
   ```
   ```
   [*DeviceB-bfd-track-manager] group a
   ```
   ```
   [*DeviceB-bfd-track-manager-group-a] bfd session singlehop1
   ```
   ```
   [*DeviceB-bfd-track-manager-group-a] bfd session singlehop2
   ```
   ```
   [*DeviceB-bfd-track-manager-group-a] commit
   ```
   ```
   [~DeviceB-bfd-track-manager-group-a] quit
   ```
   
   # After completing the configuration, run the **display bfd track-manager all** command on DeviceB. The command output shows that a session group containing single-hop BFD sessions has been established and is in the Up state.
   
   ```
   [~DeviceB] display bfd track-manager all
   --------------------------------------------------------------------------------
     Group Name                    : a
     Group Name Index              : 1
     Group State                   : Up
     Group Down Count              : 10
     Last Down Time                : 2022-06-17 10:51:11
     Last Up Time                  : 2022-06-17 10:49:39
     Group Session Count           : 2
     Total Up/Down Session Number  : 2/0
   --------------------------------------------------------------------------------
         Group Session Number      : 1
         Session Name              : singlehop1
         Local Discriminator       : 2
         Session State             : Up
         BFD Bind Type             : Interface(GigabitEthernet0/1/0)
         Process PST               : Disable
   --------------------------------------------------------------------------------
         Group Session Number      : 2
         Session Name              : singlehop2
         Local Discriminator       : 3
         Session State             : Up
         BFD Bind Type             : Interface(GigabitEthernet0/3/0)
         Process PST               : Disable
   --------------------------------------------------------------------------------
   ```
4. Configuring Multi-hop BFD.
   
   
   
   # Configure a BFD session between DeviceB and DeviceC.
   
   ```
   [~DeviceB] bfd multihop bind peer-ip 10.2.1.2 
   ```
   ```
   [*DeviceB-bfd-session-multihop] discriminator local 5
   ```
   ```
   [*DeviceB-bfd-session-multihop] discriminator remote 6
   ```
   ```
   [*DeviceB-bfd-session-multihop] commit
   ```
   ```
   [~DeviceB-bfd-session-multihop] quit
   ```
   
   # Configure a BFD session between DeviceC and DeviceB.
   
   ```
   [~DeviceC] bfd multihop bind peer-ip 10.2.1.1 
   [*DeviceC-bfd-session-multihop] discriminator local 6
   [*DeviceC-bfd-session-multihop] discriminator remote 5
   [*DeviceC-bfd-session-multihop] commit
   [~DeviceC-bfd-session-multihop] quit
   ```
   
   # After completing the configuration, run the **display bfd session all verbose** command on DeviceB and DeviceC. The command output on each device shows that a multi-hop BFD session has been established and is in the Up state. The following example uses the command output on DeviceC.
   
   ```
   [~DeviceC] display bfd session all verbose
   (w): State in WTR
   (*): State is invalid
   --------------------------------------------------------------------------------
     (Multi Hop) State : Up                    Name : multihop
   --------------------------------------------------------------------------------
     Local Discriminator    : 6                Remote Discriminator   : 5
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Peer IP Address
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.2.1.1
     Bind Interface         : -
     Track Interface        : -
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 4784             TTL                    : 254
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : -                Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
     Total UP/DOWN Session Number : 1/0
   ```
5. Associate the BFD sessions with the session group.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd-track-manager 
   ```
   ```
   [*DeviceB-bfd-track-manager]bfd session multihop track group a
   ```
   ```
   [*DeviceB-bfd-track-manager] commit
   ```
   ```
   [~DeviceB-bfd-track-manager] quit
   ```
6. Verify the configuration.
   
   
   
   # After completing the configuration, run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command on DeviceB. The command output shows that the value of the **Track Group Name** field of the multi-hop BFD session is **a**.
   
   ```
   [~DeviceB] display bfd session all verbose
   (w): State in WTR
   (*): State is invalid
   --------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : singlehop1
   --------------------------------------------------------------------------------
     Local Discriminator    : 2                Remote Discriminator   : 1
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.1
     Bind Interface         : GigabitEthernet0/1/0
     Track Interface        : -
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 2000             Actual Rx Interval (ms): 2000
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : 4046440184       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   --------------------------------------------------------------------------------
    
   --------------------------------------------------------------------------------
     (One Hop)   State : Up                    Name : singlehop2
   --------------------------------------------------------------------------------
     Local Discriminator    : 3                Remote Discriminator   : 4
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/3/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.3.1.2
     Bind Interface         : GigabitEthernet0/3/0
     Track Interface        : -
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 2000             Actual Rx Interval (ms): 2000
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : 4046440184       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name       : -
   --------------------------------------------------------------------------------
    
   --------------------------------------------------------------------------------
     (Multi Hop) State : Up                    Name : multihop
   --------------------------------------------------------------------------------
     Local Discriminator    : 5                Remote Discriminator   : 6
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Peer IP Address
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.2.1.2
     Bind Interface         : -
     Track Interface        : -
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 4784             TTL                    : 254
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : -                Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Description    : -
     Track Group Name : a
   --------------------------------------------------------------------------------
    
       Total UP/DOWN Session Number : 3/0
   
   ```
   
   # Run the **shutdown** command on GE 0/1/0 and GE 0/3/0 of DeviceB. Both BFD sessions **singlehop1** and **singlehop2** go down.
   
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
   ```
   [~DeviceB] interface gigabitethernet 0/3/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] quit
   ```
   
   # Run the **display bfd track-manager all** and **display bfd session all verbose** commands on DeviceB. The command output shows that the BFD session group **a** and the multi-hop session associated with the BFD session group are down.
   
   ```
   [~DeviceB] display bfd track-manager all
   --------------------------------------------------------------------------------
     Group Name                    : a
     Group Name Index              : 1
     Group State                   : Down
     Group Down Count              : 11
     Last Down Time                : 2022-06-17 10:55:11
     Last Up Time                  : 2022-06-17 10:53:39
     Group Session Count           : 2
     Total Up/Down Session Number  : 0/2
   --------------------------------------------------------------------------------
         Group Session Number      : 1
         Session Name              : singlehop1
         Local Discriminator       : 2
         Session State             : Down
         BFD Bind Type             : Interface(GigabitEthernet0/1/0)
         Process PST               : Disable
   --------------------------------------------------------------------------------
         Group Session Number      : 2
         Session Name              : singlehop2
         Local Discriminator       : 3
         Session State             : Down
         BFD Bind Type             : Interface(GigabitEthernet0/3/0)
         Process PST               : Disable
   --------------------------------------------------------------------------------
   ```
   ```
   [~DeviceB] display bfd session all verbose
   (w): State in WTR
   (*): State is invalid
   --------------------------------------------------------------------------------
     (One Hop)   State : Down                  Name : singlehop1
   --------------------------------------------------------------------------------
     Local Discriminator    : 2                Remote Discriminator   : 1
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/1/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.1.1.1
     Bind Interface         : gigabitethernet0/1/0
     Track Interface        : -
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 2000             Actual Rx Interval (ms): 2000
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : Control Detection Time Expired
     Bind Application       : No Application Bind
     Session TX TmrID       : 4046440184       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Not Up Reason  : In negotiation
     Session Description    : -
     Track Group Name       : -
   --------------------------------------------------------------------------------
    
   --------------------------------------------------------------------------------
     (One Hop)   State : Down                  Name : singlehop2
   --------------------------------------------------------------------------------
     Local Discriminator    : 3                Remote Discriminator   : 4
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Interface(GigabitEthernet0/3/0)
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.3.1.2
     Bind Interface         : GigabitEthernet0/3/0
     Track Interface        : -
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 2000             Actual Rx Interval (ms): 2000
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 3784             TTL                    : 255
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : Control Detection Time Expired
     Bind Application       : No Application Bind
     Session TX TmrID       : 4046440184       Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Not Up Reason  : In negotiation
     Session Description    : -
     Track Group Name       : -
   --------------------------------------------------------------------------------
    
   --------------------------------------------------------------------------------
     (Multi Hop) State : Down                  Name : multihop
   --------------------------------------------------------------------------------
     Local Discriminator    : 5                Remote Discriminator   : 6
     Session Detect Mode    : Asynchronous Mode Without Echo Function
     BFD Bind Type          : Peer IP Address
     Bind Session Type      : Static
     Bind Peer IP Address   : 10.2.1.2
     Bind Interface         : -
     Track Interface        : -
     FSM Board Id           : 3                TOS-EXP                : 7
     Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
     Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10
     Local Detect Multi     : 3                Detect Interval (ms)   : 30
     Echo Passive           : Disable          Acl Number             : -
     Destination Port       : 4784             TTL                    : 254
     Proc Interface Status  : Disable          Process PST            : Disable
     WTR Interval (ms)      : -                Config PST             : Disable
     Active Multi           : 3
     Last Local Diagnostic  : Control Detection Time Expired
     Bind Application       : No Application Bind
     Session TX TmrID       : -                Session Detect TmrID   : -
     Session Init TmrID     : -                Session WTR TmrID      : -
     Session Echo Tx TmrID  : -
     Session Not Up Reason  : In negotiation
     Session Description    : -
     Track Group Name : a
   --------------------------------------------------------------------------------
    
       Total UP/DOWN Session Number : 0/3
   
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
  bfd singlehop1 bind peer-ip 10.1.1.2 interface GigabitEthernet0/1/0 
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
   ip address 10.1.1.2 255.255.255.0 
  # 
  interface GigabitEthernet0/2/0 
   undo shutdown 
   ip address 10.2.1.1 255.255.255.0
  # 
  interface GigabitEthernet0/3/0 
   undo shutdown 
   ip address 10.3.1.1 255.255.255.0
  # 
  bfd multihop bind peer-ip 10.2.1.2
   discriminator local 5
   discriminator remote 6
  #
  bfd singlehop1 bind peer-ip 10.1.1.1 interface GigabitEthernet0/1/0 
   discriminator local 2 
   discriminator remote 1 
  #
  bfd singlehop2 bind peer-ip 10.3.1.2 interface GigabitEthernet0/3/0 
   discriminator local 3 
   discriminator remote 4
  #
  bfd-track-manager
   group a
    bfd session singlehop1
    bfd session singlehop2
   bfd session multihop track group a
  #
  return
  ```
* DeviceC configuration file
  ```
  # 
  sysname DeviceC 
  # 
  bfd 
  # 
  interface GigabitEthernet0/2/0 
   undo shutdown 
   ip address 10.2.1.2 255.255.255.0 
  # 
  bfd multihop bind peer-ip 10.2.1.1
   discriminator local 6
   discriminator remote 5
  #
  return
  ```
* DeviceD configuration file
  ```
  # 
  sysname DeviceD 
  # 
  bfd 
  # 
  interface GigabitEthernet0/3/0 
   undo shutdown 
   ip address 10.3.1.2 255.255.255.0 
  # 
  bfd singlehop2 bind peer-ip 10.3.1.1 interface GigabitEthernet0/3/0 
   discriminator local 4 
   discriminator remote 3 
  #
  return
  ```