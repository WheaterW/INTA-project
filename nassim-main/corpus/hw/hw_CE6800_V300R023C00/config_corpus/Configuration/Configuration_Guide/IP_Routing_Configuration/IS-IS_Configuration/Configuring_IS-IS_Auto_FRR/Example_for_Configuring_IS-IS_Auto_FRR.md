Example for Configuring IS-IS Auto FRR
======================================

Example for Configuring IS-IS Auto FRR

#### Networking Requirements

With IS-IS auto FRR, devices can rapidly switch traffic from a faulty link to a backup link, without waiting for route convergence, preventing traffic interruptions.

On the network shown in [Figure 1](#EN-US_TASK_0000001176743781__en-us_task_0275863838_fig165001814508), all devices are Level-1-2 devices and run IS-IS. It is required that DeviceA rapidly switch traffic to the backup link if DeviceC or link T fails.

**Figure 1** Network diagram of IS-IS auto FRR![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001229682583.png)

#### Configuration Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each routing device.
2. Enable basic IS-IS functions on each routing device.
3. Configure a high cost (in compliance with the traffic protection inequality of IS-IS auto FRR) on 100GE 1/0/2 of DeviceA so that link T is preferentially selected for traffic forwarding.
4. Enable IS-IS auto FRR on DeviceA.

#### Procedure

1. Configure IPv4 addresses for interfaces on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface  100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.0.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176743781__en-us_task_0275863838_postreq24192593172748).
2. Enable IS-IS and specify a NET on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-1-2
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface  100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] isis enable 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176743781__en-us_task_0275863838_postreq24192593172748).
3. Set the cost of 100GE 1/0/2 on DeviceA to 30 and check the IS-IS routing information.
   
   
   
   # Set cost of 100GE 1/0/2 on DeviceA to 30.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] isis cost 30
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Check information about the link used to forward traffic from DeviceA to DeviceD. The command output shows that IS-IS preferentially selects link T to transmit the traffic because link T has a lower cost.
   
   ```
   [~DeviceA] display isis route 10.4.1.0 verbose                                                           
   Route Information for ISIS(1)
   --------------------------------------------------------------------------------
   
   Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                        U-Up/Down Bit Set
   
   ISIS(1) Level-1 Forwarding Table
   --------------------------------------------------------------------------------
   
    IPV4 Dest  : 10.4.1.0/24        Int. Cost : 30            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/L/-
    Priority   : Low                Age       : 00:09:34
    NextHop    :                    Interface :               ExitIndex :
       10.0.1.2                           100GE1/0/1                    0x00000007
   
   ISIS(1) Level-2 Forwarding Table
   --------------------------------------------------------------------------------
   
    PV4 Dest  : 10.4.1.0/24        Int. Cost : 30            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : -/-/-/-
    Priority   : Low                Age       : 00:00:00
    NextHop    :                    Interface :               ExitIndex :
   ```
4. Enable IS-IS auto FRR.
   
   
   
   # Enable IS-IS auto FRR on DeviceA.
   
   
   
   ```
   [~DeviceA] isis
   [*DeviceA-isis-1] frr
   [*DeviceA-isis-1-frr] loop-free-alternate
   [*DeviceA-isis-1-frr] quit
   [*DeviceA-isis-1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check information about the routes used by DeviceA to forward traffic to DeviceD.

```
[~DeviceA] display isis route  10.4.1.0 verbose

Route Information for ISIS(1)
--------------------------------------------------------------------------------

Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                   U-Up/Down Bit Set

ISIS(1) Level-1 Forwarding Table
--------------------------------------------------------------------------------

 IPV4 Dest  : 10.4.1.0/24        Int. Cost : 30            Ext. Cost : NULL
 Admin Tag  : -                  Src Count : 1             Flags     : A/-/L/-
 Priority   : Low                Age       : 00:00:25
 NextHop    :                    Interface :               ExitIndex :
    10.0.1.2                           100GE1/0/1                    0x00000007
    (B)10.1.1.2                        100GE1/0/2                    0x00000008

ISIS(1) Level-2 Forwarding Table
--------------------------------------------------------------------------------

 IPV4 Dest  : 10.4.1.0/24        Int. Cost : 30            Ext. Cost : NULL
 Admin Tag  : -                  Src Count : 3             Flags     : -/-/-/-
 Priority   : Low                Age       : 00:00:00
 NextHop    :                    Interface :               ExitIndex : -
```

The command output shows that a backup route is generated for IS-IS auto FRR.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   network-entity 10.0000.0000.0001.00
   frr
    loop-free-alternate level-1
    loop-free-alternate level-2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   isis cost 30
  #
  return
  ```
* DeviceB
  
  ```
  #
   sysname DeviceB
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.1 255.255.255.0
   isis enable 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.1.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.3.1.1 255.255.255.0
   isis enable 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.3.1.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.4.1.1 255.255.255.0
   isis enable 1
  #
  return
  ```