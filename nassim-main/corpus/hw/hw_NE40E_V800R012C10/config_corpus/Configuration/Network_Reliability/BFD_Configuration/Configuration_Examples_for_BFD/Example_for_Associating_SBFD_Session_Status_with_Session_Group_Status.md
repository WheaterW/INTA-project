Example for Associating SBFD Session Status with Session Group Status
=====================================================================

In this example, the SBFD session status is associated with the session group status to implement fast switching upon multiple points of failure on a segmented cascaded network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001343300977__fig_dc_vrp_bfd_cfg_200401), transmission devices exist on the link. When the link between transmission devices fails, fast switching upon multiple points of failure is required on the segmented cascaded network. BFD session 1 is established between DeviceA and DeviceB, and BFD session 2 is established between DeviceB and DeviceD. DeviceB is the SBFD reflector and establishes an SBFD session with DeviceC. BFD session 1 and BFD session 2 are added to the session group on DeviceB. After the SBFD reflector discriminator is associated with the session group, the status change of the BFD session group on DeviceB affects the status of the session between DeviceB and DeviceC.

**Figure 1** Association between the SBFD session status and the session group status![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.

![](figure/en-us_image_0000001359569081.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create BFD session 1 between DeviceA and DeviceB, and BFD session 2 between DeviceB and DeviceD.
2. Add BFD sessions to a session group on DeviceB.
3. Configure DeviceB as an SBFD reflector.
4. Configure DeviceC as an SBFD initiator.
5. Associate the SBFD session status with the session group status on DeviceB.

#### Precautions

* A BFD session needs to be established.
* An SBFD session needs to be established.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address monitored by BFD
* Local interface that sends and receives BFD packets
* Local and remote discriminators of BFD sessions
* SBFD initiator and reflector

#### Procedure

1. Configure IP addresses for interfaces on each device.
   
   
   
   # Assign an IP address to the interface on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface gigabitethernet 0/1/0
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   [*DeviceA-GigabitEthernet0/1/0] commit
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface gigabitethernet 0/1/0
   [*DeviceB-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   [*DeviceB-GigabitEthernet0/1/0] commit
   [*DeviceB-GigabitEthernet0/1/0] quit
   [~DeviceB] interface gigabitethernet 0/2/0
   [*DeviceB-GigabitEthernet0/2/0] ipv6 enable
   [*DeviceB-GigabitEthernet0/2/0] ipv6 address 2001:DB8:11::2 64
   [*DeviceB-GigabitEthernet0/2/0] commit
   [*DeviceB-GigabitEthernet0/2/0] quit
   [~DeviceB] interface gigabitethernet 0/3/0
   [*DeviceB-GigabitEthernet0/3/0] ip address 10.3.1.1 24
   [*DeviceB-GigabitEthernet0/3/0] commit
   [~DeviceB-GigabitEthernet0/3/0] quit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] interface gigabitethernet 0/2/0
   [*DeviceC-GigabitEthernet0/2/0] ipv6 enable
   [*DeviceC-GigabitEthernet0/2/0] ipv6 address 2001:DB8:11::1 64
   [*DeviceC-GigabitEthernet0/2/0] commit
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] interface gigabitethernet 0/3/0
   [*DeviceD-GigabitEthernet0/3/0] ip address 10.3.1.2 24
   [*DeviceD-GigabitEthernet0/3/0] commit
   [~DeviceD-GigabitEthernet0/3/0] quit
   ```
2. Configure single-hop BFD.
   
   
   
   # Configure a BFD session between DeviceA and DeviceB.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd singlehop1 bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/0
   [*DeviceA-bfd-session-singlehop1] discriminator local 1
   [*DeviceA-bfd-session-singlehop1] discriminator remote 2
   [*DeviceA-bfd-session-singlehop1] commit
   [~DeviceA-bfd-session-singlehop1] quit
   ```
   
   # Configure a BFD session between DeviceB and DeviceA, and between DeviceB and DeviceD.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd singlehop1 bind peer-ip 10.1.1.1 interface gigabitethernet 0/1/0
   [*DeviceB-bfd-session-singlehop1] discriminator local 2
   [*DeviceB-bfd-session-singlehop1] discriminator remote 1
   [*DeviceB-bfd-session-singlehop1] commit
   [~DeviceB-bfd-session-singlehop1] quit
   [*DeviceB] bfd singlehop2 bind peer-ip 10.3.1.2 interface gigabitethernet 0/3/0
   [*DeviceB-bfd-session-singlehop2] discriminator local 3
   [*DeviceB-bfd-session-singlehop2] discriminator remote 4
   [*DeviceB-bfd-session-singlehop2] commit
   [~DeviceB-bfd-session-singlehop2] quit
   ```
   
   # Configure a BFD session between DeviceD and DeviceB.
   
   ```
   [~DeviceD] bfd
   [*DeviceD-bfd] quit
   [*DeviceD] bfd singlehop2 bind peer-ip 10.3.1.1 interface gigabitethernet 0/3/0
   [*DeviceD-bfd-session-singlehop2] discriminator local 4
   [*DeviceD-bfd-session-singlehop2] discriminator remote 3
   [*DeviceD-bfd-session-singlehop2] commit
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
   [*DeviceB-bfd-track-manager] group a
   [*DeviceB-bfd-track-manager-group-a] bfd session singlehop1
   [*DeviceB-bfd-track-manager-group-a] bfd session singlehop2
   [*DeviceB-bfd-track-manager-group-a] commit
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
4. Configure SBFD for SRv6 TE Policy.
   
   
   
   # Enable BFD and SBFD on DeviceB and configure it as an SBFD reflector.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] sbfd
   [*DeviceB-sbfd] reflector discriminator 167772160
   [*DeviceB-sbfd] quit
   [*DeviceB] commit
   ```
   
   # Configure an SRv6 TE Policy.
   
   ```
   [~DeviceB] segment-routing ipv6
   [*DeviceB-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*DeviceB-segment-routing-ipv6] locator asl ipv6-prefix 2001:DB8:20::1 64 static 32
   [*DeviceB-segment-routing-ipv6-locator] opcode ::1 end psp
   [*DeviceB-segment-routing-ipv6-locator] quit
   [*DeviceB-segment-routing-ipv6] quit
   [*DeviceB] commit
   ```
   
   # Configure IS-IS.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] is-level level-1
   [*DeviceB-isis-1] cost-style wide-compatible
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   [*DeviceB-isis-1] ipv6 enable topology ipv6
   [*DeviceB-isis-1] segment-routing ipv6 locator as1
   [*DeviceB-isis-1] quit
   [*DeviceB] interface LoopBack 1
   [*DeviceB-LoopBack1] ipv6 enable
   [*DeviceB-LoopBack1] ipv6 address 2001:DB8:2::2 64 
   [*DeviceB-LoopBack1] isis ipv6 enable 1
   [*DeviceB-LoopBack1] quit
   [*DeviceB] interface gigabitethernet0/2/0
   [*DeviceB-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*DeviceB-GigabitEthernet0/2/0] quit
   [*DeviceB] commit
   ```
   
   # Enable BFD and SBFD on DeviceC and configure it as an SBFD initiator.
   
   ```
   [~DeviceC] bfd
   [*DeviceC-bfd] quit
   [*DeviceC] sbfd
   [*DeviceC-sbfd] destination ipv6 2001:DB8:2::2 remote-discriminator 167772160
   [*DeviceC-sbfd] commit
   [*DeviceC-sbfd] quit
   ```
   
   Configure a global TE IPv6 router ID.
   
   ```
   [~DeviceC] te ipv6-router-id 2001:DB8:1::1 
   [*DeviceC] commit
   ```
   
   # Configure an SRv6 TE Policy.
   
   ```
   [~DeviceC] segment-routing ipv6
   [*DeviceC-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*DeviceC-segment-routing-ipv6] locator asl ipv6-prefix 2001:DB8:10::1 64 static 32
   [*DeviceC-segment-routing-ipv6-locator] quit
   [*DeviceC-segment-routing-ipv6] srv6-te-policy locator as1 
   [*DeviceC-segment-routing-ipv6] segment-list list1
   [*DeviceC-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:20::1
   [*DeviceC-segment-routing-ipv6-segment-list-list1] quit
   [*DeviceC-segment-routing-ipv6-segment] srv6-te policy policy1 endpoint 2001:DB8:2::2 color 101
   [*DeviceC-segment-routing-ipv6-policy-policy1] bfd seamless enable
   [*DeviceC-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*DeviceC-segment-routing-ipv6-policy-policy1-path] segment-list list1
   [*DeviceC-segment-routing-ipv6-policy-policy1-path] quit
   [*DeviceC-segment-routing-ipv6-policy-policy1] quit
   [*DeviceC-segment-routing-ipv6] quit
   [*DeviceC] commit
   ```
   
   # Configure IS-IS.
   
   ```
   [~DeviceC] isis 1
   [*DeviceC-isis-1] is-level level-1
   [*DeviceC-isis-1] cost-style wide-compatible
   [*DeviceC-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceC-isis-1] ipv6 enable topology ipv6
   [*DeviceC-isis-1] segment-routing ipv6 locator as1
   [*DeviceC-isis-1] quit
   [*DeviceC] interface LoopBack 2
   [*DeviceC-LoopBack2] ipv6 enable
   [*DeviceC-LoopBack2] ipv6 address 2001:DB8:1::1 64 
   [*DeviceC-LoopBack2] isis ipv6 enable 1
   [*DeviceC-LoopBack2] quit
   [*DeviceC] interface gigabitethernet0/2/0
   [*DeviceC-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*DeviceC-GigabitEthernet0/2/0] quit
   [*DeviceC] commit
   ```
   
   # After completing the configuration, run the **display bfd session all verbose** command on DeviceC. The command output shows that an SBFD session has been established and is in the Up state. The following example uses the command output on DeviceC.
   
   ```
   [~DeviceC] display bfd session all verbose
   (w): State in WTR
   (*): State is invalid
   --------------------------------------------------------------------------------
   State : Up                    Name : dyn_16385
   --------------------------------------------------------------------------------
   Local Discriminator    : 16385            Remote Discriminator   : 167772160
   Session Detect Mode    : Seamless Mode Without Echo Function
       BFD Bind Type      : SID_LIST
   Bind Session Type      : Dynamic
   SID_LIST Id            : 1                Color                  : 101
   Bind Peer IP Address   : 2001:db8:2::2
   Bind Interface         : -
   FSM Board Id           : 3                TOS-EXP                : 7
   Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
   Actual Tx Interval (ms): 10             Actual Rx Interval (ms): 10
   Local Detect Multi     : 3                Detect Interval (ms)   : 30
   Echo Passive           : Disable          Acl Number             : -
   Destination Port       : 7784             TTL                    : 255
   Proc Interface Status  : Disable          Process PST            : Enable
   WTR Interval (ms)      : 1000             Config PST             : Enable
   Active Multi           : 50
   Last Local Diagnostic  : No Diagnostic
   Bind Application       : SRPOLICY6
   Session TX TmrID       : -                Session Detect TmrID   : -
   Session Init TmrID     : -                Session WTR TmrID      : -
   Session Echo Tx TmrID  : -
   Session Description    : -
   Track Group Name       : -
   --------------------------------------------------------------------------------
    
     Total UP/DOWN Session Number : 1/0
   ```
5. Associate the SBFD reflector with the session group status.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd-track-manager 
   [*DeviceB-bfd-track-manager]sbfd reflector 167772160 track group a
   [*DeviceB-bfd-track-manager] commit
   [~DeviceB-bfd-track-manager] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **shutdown** command on GE 0/1/0 and GE 0/3/0 of DeviceB. Both BFD sessions **singlehop1** and **singlehop2** go down.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   [~DeviceB-GigabitEthernet0/1/0] shutdown
   [*DeviceB-GigabitEthernet0/1/0] commit
   [~DeviceB-GigabitEthernet0/1/0] quit
   [~DeviceB] interface gigabitethernet 0/3/0
   [~DeviceB-GigabitEthernet0/3/0] shutdown
   [*DeviceB-GigabitEthernet0/3/0] commit
   [~DeviceB-GigabitEthernet0/3/0] quit
   ```
   
   # Run the **display bfd track-manager all** command on DeviceB. The command output shows that the status of BFD session group **a** is Down.
   
   ```
   [~DeviceB] display bfd track-manager all
   --------------------------------------------------------------------------------
     Group Name                    : a
     Group Name Index              : 1
     Group State                   : Down
     Group Down Count              : 1
     Last Down Time                : 2022-06-17 10:55:11
     Last Up Time                  : 2022-06-17 10:53:39
     Group Session Count           : 1
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
         Local Discriminator       : 6
         Session State             : Down
         BFD Bind Type             : Interface(GigabitEthernet0/3/0)
         Process PST               : Disable
   ```
   
   Run the **display bfd session all verbose** command on DeviceC. The command output shows that the SBFD session associated with the session group goes down.
   
   ```
   [~DeviceC]display bfd session all verbose
   (w): State in WTR
   (*): State is invalid
   --------------------------------------------------------------------------------
   State : Down                  Name : dyn_16385
   --------------------------------------------------------------------------------
   Local Discriminator    : 16385            Remote Discriminator   : 167772160
   Session Detect Mode    : Seamless Mode Without Echo Function
   BFD Bind Type          : SID_LIST
   Bind Session Type      : Dynamic
   SID_LIST Id            : 1                Color                  : 101
   Bind Peer IP Address   : 2001:db8:2::2
   Bind Interface         : -
   FSM Board Id           : 3                TOS-EXP                : 7
   Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
   Actual Tx Interval (ms): 1000             Actual Rx Interval (ms): 1000
   Local Detect Multi     : 3                Detect Interval (ms)   : 50000
   Echo Passive           : Disable          Acl Number             : -
   Destination Port       : 7784             TTL                    : 255
   Proc Interface Status  : Disable          Process PST            : Enable
   WTR Interval (ms)      : 1000             Config PST             : Enable
   Active Multi           : 50
   Last Local Diagnostic  : Control Detection Time Expired
   Bind Application       : SRPOLICY6
   Session TX TmrID       : -                Session Detect TmrID   : -
   Session Init TmrID     : -                Session WTR TmrID      : -
   Session Echo Tx TmrID  : -
   Session Not Up Reason  : In negotiation
   Session Description    : -
   Track Group Name       : -
   --------------------------------------------------------------------------------
    
     Total UP/DOWN Session Number : 0/1
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
  sbfd
   reflector discriminator 167772160
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator asl ipv6-prefix 2001:DB8:20::1 64 static 32
    opcode ::1 end psp
  # 
  isis 1
   is-level level-1
   cost-style wide-compatible
   network-entity 10.0000.0000.0002.00
  #
  ipv6 enable topology ipv6
   segment-routing ipv6 locator asl
  #
  interface GigabitEthernet0/2/0
   ipv6 enable
   ipv6 address 2001:DB8:11::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/1/0
   undo shutdown 
   ip address 10.1.1.2 255.255.255.0 
  #
  interface GigabitEthernet0/3/0 
   undo shutdown 
   ip address 10.3.1.1 255.255.255.0
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   isis ipv6 enable 1
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
   sbfd reflector 167772160 track group a
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
  sbfd
   destination ipv6 2001:DB8:2::2 remote-discriminator 167772160
  #
  te ipv6-router-id 2001:DB8:1::1
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator asl ipv6-prefix 2001:DB8:10::1 64 static 32
   srv6-te-policy locator asl
   segment-list list1
    index 5 sid ipv6 2001:DB8:20::1
   srv6-te policy policy1 endpoint 2001:DB8:2::2 color 101
    bfd seamless enable
    candidate-path preference 100
     segment-list list1
  #
  isis 1
   is-level level-1
   cost-style wide-compatible
   network-entity 10.0000.0000.0001.00
  #
  ipv6 enable topology ipv6
   segment-routing ipv6 locator asl
  #
  interface GigabitEthernet0/2/0
   undo shutdown 
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   ipv6 enable
   ipv6 address 2001:DB8:11::1/64
   isis ipv6 enable 1
  #
  interface LoopBack2
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   isis ipv6 enable 1
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
  bfd singlehop bind peer-ip 10.3.1.1 interface GigabitEthernet0/3/0 
   discriminator local 4 
   discriminator remote 3
  # 
  return
  ```