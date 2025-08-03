Example for Configuring Interface-based VLAN Assignment to Implement Intra-VLAN Communication (Through Multiple Devices)
========================================================================================================================

Example for Configuring Interface-based VLAN Assignment to Implement Intra-VLAN Communication (Through Multiple Devices)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176662423__fig523919715818), Host1, Host2, Host5, and Host6 belong to VLAN 2, and Host3, Host4, Host7, and Host8 belong to VLAN 3. The interfaces on the link between DeviceA and DeviceC and those on the link between DeviceC and DeviceB allow packets sourced from VLAN 2 and VLAN 3 to pass through. This ensures that hosts in the same VLAN on DeviceA and DeviceB can directly communicate with each other at Layer 2, but hosts in different VLANs cannot.

**Figure 1** Networking diagram of configuring interface-based VLAN assignment for intra-VLAN communication through multiple devices![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 5 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, and 100GE 1/0/5, respectively.


  
![](figure/en-us_image_0000001130622934.png "Click to enlarge")

#### Procedure

1. On DeviceA and DeviceB, configure the interfaces connecting to hosts as access interfaces, add Host1, Host2, Host5, and Host6 to VLAN 2, and add Host3, Host4, Host7, and Host8 to VLAN 3.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2 3
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 2
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] port default vlan 3
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] portswitch
   [*DeviceA-100GE1/0/4] port link-type access
   [*DeviceA-100GE1/0/4] port default vlan 3
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 2 3
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type access
   [*DeviceB-100GE1/0/1] port default vlan 2
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type access
   [*DeviceB-100GE1/0/2] port default vlan 2
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type access
   [*DeviceB-100GE1/0/3] port default vlan 3
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] interface 100ge 1/0/4
   [*DeviceB-100GE1/0/4] portswitch
   [*DeviceB-100GE1/0/4] port link-type access
   [*DeviceB-100GE1/0/4] port default vlan 3
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] commit
   ```
2. Configure the link between DeviceA and DeviceC and that between DeviceB and DeviceC as trunk links.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/5
   [~DeviceA-100GE1/0/5] portswitch
   [*DeviceA-100GE1/0/5] port link-type trunk
   [*DeviceA-100GE1/0/5] port trunk allow-pass vlan 2 3
   [*DeviceA-100GE1/0/5] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/5
   [~DeviceB-100GE1/0/5] portswitch
   [*DeviceB-100GE1/0/5] port link-type trunk
   [*DeviceB-100GE1/0/5] port trunk allow-pass vlan 2 3
   [*DeviceB-100GE1/0/5] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 2 3
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type trunk
   [*DeviceC-100GE1/0/1] port trunk allow-pass vlan 2 3
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch
   [*DeviceC-100GE1/0/2] port link-type trunk
   [*DeviceC-100GE1/0/2] port trunk allow-pass vlan 2 3
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Run the [**display vlan**](cmdqueryname=display+vlan) command to check the VLAN status. The following example shows the command output on DeviceA.

```
[~DeviceA] display vlan 2
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
MAC-LRN: MAC-address learning;  STAT: Statistic;
BC: Broadcast; MC: Multicast;   UC: Unknown-unicast;
FWD: Forward;  DSD: Discard;
--------------------------------------------------------------------------------

VID          Ports
--------------------------------------------------------------------------------
   2         UT:100GE1/0/1(U)   100GE1/0/2(U)
             TG:100GE1/0/5(U)

VID  Type     Status  Property  MAC-LRN STAT    BC  MC  UC  Description
--------------------------------------------------------------------------------
   2 common   enable  default   enable  disable FWD FWD FWD VLAN 0002
```

# Run the [**display port vlan**](cmdqueryname=display+port+vlan) command to check information about allowed VLANs on involved interfaces. The following example shows the command output on 100GE 1/0/5 of DeviceA.

```
[~DeviceA] display port vlan 100ge 1/0/5
Port                    Link Type    PVID  Trunk VLAN List                      Port Description
---------------------------------------------------------------------------------------------------------------
100GE1/0/5              trunk           1  1-3
```

# Hosts in VLAN 2 can ping one another, as can those in VLAN 3. However, hosts in VLAN 2 cannot ping hosts in VLAN 3.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 2 to 3
  #
  interface 100GE1/0/1
   port default vlan 2
  #
  interface 100GE1/0/2
   port default vlan 2
  #
  interface 100GE1/0/3
   port default vlan 3
  #
  interface 100GE1/0/4
   port default vlan 3
  #
  interface 100GE1/0/5
   port link-type trunk
   port trunk allow-pass vlan 2 to 3
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 2 to 3
  #
  interface 100GE1/0/1
   port default vlan 2
  #
  interface 100GE1/0/2
   port default vlan 2
  #
  interface 100GE1/0/3
   port default vlan 3
  #
  interface 100GE1/0/4
   port default vlan 3
  #
  interface 100GE1/0/5
   port link-type trunk
   port trunk allow-pass vlan 2 to 3
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 2 to 3
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 3
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 3
  #
  return
  ```