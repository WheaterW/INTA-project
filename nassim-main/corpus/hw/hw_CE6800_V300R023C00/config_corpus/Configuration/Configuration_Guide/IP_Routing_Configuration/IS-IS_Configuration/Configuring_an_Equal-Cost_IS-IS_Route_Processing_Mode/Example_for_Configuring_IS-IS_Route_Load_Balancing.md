Example for Configuring IS-IS Route Load Balancing
==================================================

Example for Configuring IS-IS Route Load Balancing

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130784134__fig_dc_vrp_isis_cfg_008301), DeviceA, DeviceB, DeviceC, and DeviceD are Level-2 devices in area 10 and run IS-IS to implement IP interworking. Load balancing is configured on DeviceA so that traffic from DeviceA to DeviceD is balanced between DeviceB and DeviceC.

**Figure 1** Network diagram of IS-IS route load balancing![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130624390.png)

#### Configuration Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv4 addresses for interfaces on each routing device.
2. Enable basic IS-IS functions on each device to implement interworking.
3. Disable load balancing on DeviceA and check its routing table.
4. Restore the default maximum number of routes for load balancing on DeviceA and check its routing table again.

#### Procedure

1. Configure IPv4 addresses for interfaces on each routing device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.2.1 255.255.255.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] ip address 172.16.1.1 255.255.255.0
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784134__postreq24192593172748).
2. Configure basic IS-IS functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-1
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] isis enable 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] isis enable 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784134__postreq24192593172748).
3. Disable load balancing on DeviceA by setting the maximum number of equal-cost routes for load balancing to 1.
   
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] maximum load-balancing 1
   [*DeviceA-isis-1] quit
   [*DeviceA] commit
   ```
   
   # Check the routing table of DeviceA.
   
   ```
   [~DeviceA] display isis route
   
   Route information for ISIS(1)
   ----------------------------------------------------------------------------
   Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                  U-Up/Down Bit Set
   
   ISIS(1) Level-2 Forwarding Table
   ----------------------------------------------------------------------------
   
   IPV4 Destination    IntCost   ExtCost ExitInterface   NextHop          Flags
   ---------------------------------------------------------------------------
   192.168.1.0/24      20        NULL    100GE1/0/2         10.1.2.2         A/-/-/-/-
   10.1.1.0/24         10        NULL    100GE1/0/1         Direct           D/-/L/-/-
   172.16.1.0/24       10        NULL    100GE1/0/3         Direct           D/-/L/-/-
   172.16.2.0/24       30        NULL    100GE1/0/1        10.1.1.2         A/-/-/-/-
   10.1.2.0/24         10        NULL    100GE1/0/2         Direct           D/-/L/-/-
   192.168.0.0/24      20        NULL    100GE1/0/1         10.1.1.2         A/-/-/-/-
   ```
   
   As shown in the preceding command output, the route to 172.16.2.0 has only one next hop (10.1.1.2) after the maximum number of equal-cost routes for load balancing is set to 1. IS-IS selects the route with next hop 10.1.1.2 as the optimal route because the system ID of DeviceB is smaller.
4. Restore the default maximum number of routes for load balancing on DeviceA.
   
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] undo maximum load-balancing
   [*DeviceA-isis-1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the routing table of DeviceA after restoring the default maximum number of routes for load balancing.

```
[~DeviceA] display isis route

Route information for ISIS(1)
----------------------------------------------------------------------------
Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                               U-Up/Down Bit Set

ISIS(1) Level-2 Forwarding Table
----------------------------------------------------------------------------

 IPV4 Destination    IntCost   ExtCost ExitInterface   NextHop          Flags
-----------------------------------------------------------------------------
 192.168.1.0/24      20        NULL    100GE1/0/2         10.1.2.2         A/-/-/-/-
 10.1.1.0/24         10        NULL    100GE1/0/1         Direct           D/-/L/-/-
 172.16.1.0/24       10        NULL    100GE1/0/3         Direct           D/-/L/-/-
 172.16.2.0/24       30        NULL    100GE1/0/1        10.1.1.2         A/-/-/-/-
                                       100GE1/0/2         10.1.2.2
 10.1.2.0/24         10        NULL    100GE1/0/2         Direct           D/-/L/-/-
 192.168.0.0/24      20        NULL    100GE1/0/1         10.1.1.2         A/-/-/-/-
```

As shown in the routing table, after the default maximum number of routes for load balancing is restored, the maximum number of equal-cost routes is 32. Therefore, the two next hops 10.1.1.2 (DeviceB) and 10.1.2.2 (DeviceC) are both valid and are displayed on DeviceA.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   is-level level-2
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
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
   is-level level-2
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.0.1 255.255.255.0
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
   is-level level-2
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
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
   is-level level-2
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.0.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.16.2.1 255.255.255.0
   isis enable 1
  #              
  return
  ```