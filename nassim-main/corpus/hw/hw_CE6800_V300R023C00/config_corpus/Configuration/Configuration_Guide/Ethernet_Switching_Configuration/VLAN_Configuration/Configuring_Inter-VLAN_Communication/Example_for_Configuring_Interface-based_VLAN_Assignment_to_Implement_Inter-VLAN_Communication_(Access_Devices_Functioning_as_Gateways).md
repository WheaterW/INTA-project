Example for Configuring Interface-based VLAN Assignment to Implement Inter-VLAN Communication (Access Devices Functioning as Gateways)
======================================================================================================================================

Example for Configuring Interface-based VLAN Assignment to Implement Inter-VLAN Communication (Access Devices Functioning as Gateways)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001611053957__fig523919715818), PC1 and PC2 belong to VLAN 2 and VLAN 3 respectively and are connected to DeviceA at the aggregation layer through DeviceB at the access layer. PC3 belongs to VLAN 4 and is connected to DeviceA through DeviceC at the access layer. DeviceB functions as the gateway of PC1 and PC2, and DeviceC functions as the gateway of PC3. Static routes are configured on the devices to allow PCs to communicate with each other and access the upper-layer device.

**Figure 1** Network diagram for configuring access devices as gateways![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001562064608.png)

#### Procedure

1. Configure DeviceB at the access layer.
   
   
   
   # Create VLANs.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 2 3
   [*DeviceB] commit
   ```
   
   # Add interfaces to corresponding VLANs.
   
   ```
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] portswitch
   [~DeviceB-100GE1/0/2] port link-type access
   [~DeviceB-100GE1/0/2] port default vlan 2
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type access
   [*DeviceB-100GE1/0/3] port default vlan 3
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
   
   # Configure VLANIF interfaces as gateways of PCs.
   
   
   
   ```
   [~DeviceB] interface vlanif 2
   [*DeviceB-Vlanif2] ip address 192.168.2.1 24
   [*DeviceB-Vlanif2] quit
   [*DeviceB] interface vlanif 3
   [*DeviceB-Vlanif3] ip address 192.168.3.1 24
   [*DeviceB-Vlanif3] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceB for communication with DeviceA.
   
   ```
   [~DeviceB] vlan batch 5
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type access
   [*DeviceB-100GE1/0/1] port default vlan 5
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface Vlanif 5
   [*DeviceB-Vlanif5] ip address 192.168.5.2 24
   [*DeviceB-Vlanif5] quit
   [*DeviceB] ip route-static 0.0.0.0 0.0.0.0 192.168.5.1
   [*DeviceB] commit
   ```
2. Configure DeviceC at the access layer.
   
   
   
   # Create a VLAN.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 4
   [*DeviceC] commit
   ```
   
   # Add an interface to the VLAN.
   
   ```
   [~DeviceC] interface 100ge 1/0/2
   [~DeviceC-100GE1/0/2] portswitch
   [~DeviceC-100GE1/0/2] port link-type access
   [~DeviceC-100GE1/0/2] port default vlan 4
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
   
   # Configure a VLANIF interface as the gateway of a PC.
   
   
   
   ```
   [~DeviceC] interface vlanif 4
   [*DeviceC-Vlanif4] ip address 192.168.4.1 24
   [*DeviceC-Vlanif4] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceC for communication with DeviceA.
   
   ```
   [~DeviceC] vlan batch 5
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type access
   [*DeviceC-100GE1/0/1] port default vlan 5
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface Vlanif 5
   [*DeviceC-Vlanif5] ip address 192.168.5.3 24
   [*DeviceC-Vlanif5] quit
   [*DeviceC] ip route-static 0.0.0.0 0.0.0.0 192.168.5.1
   [*DeviceC] commit
   ```
3. Configure DeviceA at the aggregation layer.
   
   
   
   # Create a VLAN.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 5
   [*DeviceA] commit
   ```
   
   # Add interfaces to the VLAN.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 5
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 5
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] port default vlan 5
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   # Configure a VLANIF interface for communication with the upper-layer device.
   
   ```
   [~DeviceA] interface vlanif 5
   [*DeviceA-Vlanif5] ip address 192.168.5.1 24
   [*DeviceA-Vlanif5] quit
   [*DeviceA] commit
   ```
   
   # Configure return specific routes to implement mutual access between internal network segments.
   
   ```
   [~DeviceA] ip route-static 192.168.2.0 255.255.255.0 192.168.5.2
   [*DeviceA] ip route-static 192.168.3.0 255.255.255.0 192.168.5.2 
   [*DeviceA] ip route-static 192.168.4.0 255.255.255.0 192.168.5.3
   [*DeviceA] commit
   ```
   
   # Configure a default route to allow devices on internal network segments to access the upper-layer device.
   
   ```
   [~DeviceA] ip route-static 0.0.0.0 0.0.0.0 192.168.5.4 
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display vlan**](cmdqueryname=display+vlan) command to check the VLAN status. The following example uses the command output on DeviceB.

```
[~DeviceB] display vlan 2
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
   2         UT:100GE1/0/2(U)   100GE1/0/3(U)
             TG:100GE1/0/1(U)

VID  Type     Status  Property  MAC-LRN STAT    BC  MC  UC  Description
--------------------------------------------------------------------------------
   2 common   enable  default   enable  disable FWD FWD FWD VLAN 0002
```

# Run the [**display port vlan**](cmdqueryname=display+port+vlan) command to check information about allowed VLANs on an interface. The following example uses the command output about 100GE 1/0/1 on DeviceB.

```
[~DeviceB] display port vlan 100ge 1/0/1
Port                    Link Type    PVID  Trunk VLAN List                      Port Description
---------------------------------------------------------------------------------------------------------------
100GE1/0/1               access          1  2-3
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 5
  #
  interface Vlanif5
   ip address 192.168.5.1 255.255.255.0
  #
  interface 100GE1/0/1
   port default vlan 5
  #
  interface 100GE1/0/2
   port default vlan 5
  #
  interface 100GE1/0/3
   port default vlan 5
  #
  ip route-static 0.0.0.0 0.0.0.0 192.168.5.1
  ip route-static 192.168.2.0 255.255.255.0 192.168.5.2
  ip route-static 192.168.3.0 255.255.255.0 192.168.5.2
  ip route-static 192.168.4.0 255.255.255.0 192.168.5.3
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 2 to 3 5
  #
  interface Vlanif2
   ip address 192.168.2.1 255.255.255.0
  #
  interface Vlanif3
   ip address 192.168.3.1 255.255.255.0
  #
  interface Vlanif5
   ip address 192.168.5.2 255.255.255.0
  #
  interface 100GE1/0/1
   port default vlan 5
  #
  interface 100GE1/0/2
   port default vlan 2
  #
  interface 100GE1/0/3
   port default vlan 3
  #
  ip route-static 0.0.0.0 0.0.0.0 192.168.5.1
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 4 to 5
  #
  #
  interface Vlanif4
   ip address 192.168.4.1 255.255.255.0
  #
  interface Vlanif5
   ip address 192.168.5.3 255.255.255.0
  #
  interface 100GE1/0/1
   port default vlan 5
  #
  interface 100GE1/0/2
   port default vlan 4
  #
  ip route-static 0.0.0.0 0.0.0.0 192.168.5.1
  #
  return
  ```