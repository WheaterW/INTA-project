Example for Configuring IS-IS Route Summarization
=================================================

Example for Configuring IS-IS Route Summarization

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130624354__fig_dc_vrp_isis_cfg_011101), DeviceA, DeviceB, and DeviceC run IS-IS for interworking. DeviceB leaks the routes to three network segments (172.16.1.0/24, 172.16.2.0/24, and 172.16.3.0/24) from the Level-1 area to the Level-2 area. It is required that the routes to the three network segments be summarized on DeviceB into the route 172.16.0.0/16 to reduce the number of routes to be maintained by DeviceB and prevent interface-state alteration in the Level-1 area from triggering route convergence in the Level-2 area.

**Figure 1** Network diagram of IS-IS route summarization![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001176743861.png)

#### Configuration Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic IS-IS functions on each device and check the IS-IS routing table.
2. Configure DeviceB to summarize routes and check its IS-IS routing table.

#### Procedure

1. Configure IPv4 addresses for interfaces on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 172.16.1.2 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130624354__postreq24192593172748).
2. Configure basic IS-IS functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-2
   [*DeviceA-isis-1] network-entity 20.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   [*DeviceB-isis-1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] isis enable 1
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] isis enable 1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 1
   [*DeviceC-isis-1] is-level level-1
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   [*DeviceC-isis-1] quit
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] isis enable 1
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   The configurations of 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4 on DeviceC are the same as the configuration of 100GE 1/0/1. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130624354__postreq24192593172748).
   
   # Check the IS-IS routing table of DeviceA.
   
   ```
   [~DeviceA] display isis route
   
   Route Information for ISIS(1)
   --------------------------------------------------------------------------------
   
   Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                      U-Up/Down Bit Set
   
   ISIS(1) Level-2 Forwarding Table
   --------------------------------------------------------------------------------
   
   IPV4 Destination      IntCost    ExtCost ExitInterface     NextHop         Flags
   --------------------------------------------------------------------------------
   172.16.1.0/24              30       NULL 100GE1/0/1           172.16.4.2      A/-/-/-
   172.16.2.0/24              30       NULL 100GE1/0/1           172.16.4.2      A/-/-/-
   172.16.3.0/24              30       NULL 100GE1/0/1           172.16.4.2      A/-/-/-
   172.16.4.0/24              10       NULL 100GE1/0/1           Direct          D/-/L/-
   172.17.1.0/24              20       NULL 100GE1/0/1           172.16.4.2      A/-/-/-
   ```
3. Configure route summarization on DeviceB.
   
   
   
   # Configure DeviceB to summarize routes 172.16.1.0/24, 172.16.2.0/24, and 172.16.3.0/24 into 172.16.0.0/16.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] summary 172.16.0.0 255.255.0.0 level-1-2
   [*DeviceB-isis-1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the IS-IS routing table of DeviceA. The command output contains information about the summary route 172.16.0.0/16 rather than the specific routes 172.16.1.0/24, 172.16.2.0/24, and 172.16.3.0/24.

```
[~DeviceA] display isis route
Route Information for ISIS(1)
--------------------------------------------------------------------------------

Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                    U-Up/Down Bit Set

ISIS(1) Level-2 Forwarding Table
--------------------------------------------------------------------------------

IPV4 Destination      IntCost    ExtCost ExitInterface     NextHop         Flags
--------------------------------------------------------------------------------
172.16.0.0/16              20       NULL 100GE1/0/1           172.16.4.2      A/-/-/-
172.16.4.0/24              10       NULL 100GE1/0/1           Direct          D/-/L/-
172.17.1.0/24              20       NULL 100GE1/0/1           172.16.4.2      A/-/-/-

```

#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  isis 1
   is-level level-2
   network-entity 20.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.4.1 255.255.255.0
   isis enable 1
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
   summary 172.16.0.0 255.255.0.0 level-1-2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.4.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.17.1.2 255.255.255.0
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
   is-level level-1
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.4.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.16.2.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 172.16.3.1 255.255.255.0
   isis enable 1
  #
  return
  ```