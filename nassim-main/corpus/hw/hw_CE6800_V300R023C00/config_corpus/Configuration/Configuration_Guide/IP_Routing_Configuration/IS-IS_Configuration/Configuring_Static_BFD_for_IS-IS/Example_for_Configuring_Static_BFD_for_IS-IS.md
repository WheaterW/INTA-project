Example for Configuring Static BFD for IS-IS
============================================

Example for Configuring Static BFD for IS-IS

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130784138__fig_dc_vrp_isis_cfg_008601), DeviceA and DeviceB are connected through a Layer 2 switch. IS-IS runs on DeviceA, DeviceB, and DeviceC. It is required that BFD be used to detect the IS-IS neighbor relationship between DeviceA and DeviceB so that BFD notifies a failure of the link between the two devices to IS-IS upon detection of the failure.

**Figure 1** Network diagram of static BFD for IS-IS![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130784188.png)

#### Configuration Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic IS-IS functions on each device.
2. Enable BFD on DeviceA and DeviceB.

#### Procedure

1. Configure IPv4 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784138__postreq24192593172748).
2. Configure basic IS-IS functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-2
   [*DeviceA-isis-1] network-entity aa.1111.1111.1111.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784138__postreq24192593172748).
   
   After the preceding configurations are performed, an IS-IS neighbor relationship is established between DeviceA and DeviceB.
   
   ```
   [~DeviceA] display isis peer
   Peer information for ISIS(1)
   ----------------------------------------------------------------------------------
                                                                   
   System ID        Interface        Circuit ID          State HoldTime Type      PRI
   ---------------------------------------------------------------------------------
   2222.2222.2222  100GE1/0/1           2222.2222.2222.00    Up    23s      L2       64
   Total Peer(s): 1
   ```
   
   The IS-IS routing table of DeviceA has the routes to DeviceB and DeviceC.
   
   ```
   [~DeviceA] display isis route
    
   Route Information for ISIS(1)
   --------------------------------------------------------------------------------
   
   Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                      U-Up/Down Bit Set
   ISIS(1) Level-2 Forwarding Table
   -------------------------------------------------------------------------
   
   IPV4 Destination    IntCost   ExtCost ExitInterface   NextHop        Flags
   -------------------------------------------------------------------------
   10.1.1.0/24         10        NULL    100GE1/0/1         Direct         D/-/L/-
   10.2.1.0/24       20       NULL   100GE1/0/1      10.1.1.2      A/-/-/-
   ```
3. Configure static BFD for IS-IS.
   
   
   
   # Enable BFD and configure a BFD session on DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd atob bind peer-ip 10.1.1.2 interface 100ge 1/0/1
   [*DeviceA-bfd-session-atob] discriminator local 1
   [*DeviceA-bfd-session-atob] discriminator remote 2
   [*DeviceA-bfd-session-atob] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784138__postreq24192593172748).
   
   After the configuration is complete, run the **display bfd session** command on DeviceA. The command output shows that the BFD session is up.
   
   ```
   [~DeviceA] display bfd session all
   S: Static session
   D: Dynamic session
   IP: IP session
   IF: Single-hop session
   PEER: Multi-hop session
   AUTO: Automatically negotiated session
   VXLAN: VXLAN session
   (w): State in WTR 
   (*): State is invalid
   Total UP/DOWN Session Number : 1/0
   ------------------------------------------------------------------------
   Local   Remote   PeerIpAddr    State      Type       Interface Name           
   ------------------------------------------------------------------------
   1       2        10.1.1.2      Up         S_IP_IF    100GE1/0/1
   ```
4. Enable static BFD on each involved IS-IS interface.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] isis bfd static
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] quit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784138__postreq24192593172748).

#### Verifying the Configuration

# Enable debugging on DeviceA.

```
<DeviceA> debugging isis adjacency 1 interface 100GE1/0/1
<DeviceA> debugging isis circuit-information 1 interface 100GE1/0/1
<DeviceA> terminal debugging
<DeviceA> terminal monitor
```

# Run the [**shutdown**](cmdqueryname=shutdown) command on 100GE1/0/1 of DeviceB to simulate a link failure.

```
[~DeviceB] interface 100ge 1/0/1
[~DeviceB-100GE1/0/1] shutdown
[*DeviceB] commit
```

# Check the log information on DeviceA.

```
ISIS adjacency state change. (SysInstance=1, SysLevel=1, CircI
ndex=2, CircIfIndex=20, LspId=2222.2222.2222.00.00, AdjState=1, IfIndex=20, IfNa
me=100GE1/0/1, Reason=BFD detected that the neighbor went Down, SubReason=14)
```

According to the preceding information, the IS-IS neighbor relationship with DeviceB has been deleted because BFD detected the link failure.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  isis 1
   is-level level-2
   network-entity aa.1111.1111.1111.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   isis bfd static
  #
  bfd atob bind peer-ip 10.1.1.2 interface 100GE1/0/1
   discriminator local 1
   discriminator remote 2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  isis 1
   is-level level-2
   network-entity aa.2222.2222.2222.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
   isis bfd static
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.1 255.255.255.0
   isis enable 1
  #
  bfd btoa bind peer-ip 10.1.1.1 interface 100GE1/0/1
   discriminator local 2
   discriminator remote 1
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
   network-entity aa.3333.3333.3333.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
  #
  return
  ```