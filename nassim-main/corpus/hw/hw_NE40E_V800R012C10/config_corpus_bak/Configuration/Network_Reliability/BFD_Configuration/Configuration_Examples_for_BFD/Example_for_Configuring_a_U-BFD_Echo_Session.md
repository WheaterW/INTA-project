Example for Configuring a U-BFD Echo Session
============================================

This section provides an example for configuring a U-BFD echo session on a BFD-capable device to rapidly detect faults in direct links on a network.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172361712__fig_dc_vrp_bfd_cfg_011301), Device A supports BFD, whereas Device B does not. To rapidly detect faults in the direct link between Device A and Device B, configure a U-BFD echo session on Device A. After receiving a U-BFD echo session packet from Device A, Device B immediately loops back the packet, implementing rapid link fault detection.

**Figure 1** Configuring a U-BFD echo session![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 in this example are GE 0/1/0.


  
![](images/fig_dc_vrp_bfd_cfg_011301.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to the interfaces through which Device A and Device B are directly connected.
2. Configure a U-BFD echo session on Device A.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address monitored by a U-BFD echo session
* Local discriminator of a U-BFD echo session
* Minimum interval at which U-BFD echo session packets are received

#### Procedure

1. Assign IP addresses to the interfaces through which Device A and Device B are directly connected.
   
   
   
   # Assign an IP address to Device A's interface through which Device A is directly connected to Device B.
   
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
   
   # Assign an IP address to Device B's interface through which Device B is directly connected to Device A.
   
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
2. Configure a U-BFD echo session on Device A.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd atob bind peer-ip 10.1.1.2 interface gigabitEthernet0/1/0 one-arm-echo
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-atob] min-echo-rx-interval 100
   ```
   ```
   [*DeviceA-bfd-session-atob] commit
   ```
   ```
   [~DeviceA-bfd-session-atob] quit
   ```
   ```
   [~DeviceA] quit
   ```
3. Verify the configuration.
   
   
   
   After completing the configuration, run the **display bfd session all verbose** command on Device A. The command output shows that a U-BFD echo session has been established and its status is up.
   
   ```
   <DeviceA> display bfd session all verbose
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
     (One Hop)   State : Up                  Name : atob
   --------------------------------------------------------------------------------
     Local Discriminator    : 1                Remote Discriminator   : -
     Session Detect Mode    : Asynchronous One-arm-echo Mode
     BFD Bind Type          : Interface(gigabitEthernet0/1/0)
     Bind Session Type      : Static 
     Bind Peer IP Address   : 10.1.1.2         
     Bind Interface         : GigabitEthernet0/1/0
     Track Interface        : -  
     FSM Board Id           : 10               TOS-EXP                : 7
     Echo Rx Interval (ms)  : 100 
     Actual Tx Interval (ms): 100              Actual Rx Interval (ms): 100 
     Local Detect Multi     : 3                Detect Interval (ms)   : 300 
     Echo Passive           : Disable          Acl Number             : - 
     Destination Port       : 3784             TTL                    : 255 
     Proc Interface Status  : Disable          Process PST            : Disable    
     WTR Interval (ms)      : -                Config PST             : Disable    
     Active Multi           : 3                  
     Last Local Diagnostic  : No Diagnostic
     Bind Application       : No Application Bind
     Session TX TmrID       : -                Session Detect TmrID   : - 
     Session Init TmrID     : -                Session WTR TmrID      : - 
     Session Echo Tx TmrID  : -   
     Session Not Up Reason  : -  
     Session Description    : - 
     Track Group Name       : -
   --------------------------------------------------------------------------------
          Total UP/DOWN Session Number : 1/0
   ```

#### Configuration Files

* Device A configuration file
  
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
  interface gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  bfd atob bind peer-ip 10.1.1.2 interface gigabitEthernet0/1/0 one-arm-echo
  ```
  ```
   discriminator local 1
  ```
  ```
   min-echo-rx-interval 100
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
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
  interface gigabitethernet0/1/0
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
  return
  ```