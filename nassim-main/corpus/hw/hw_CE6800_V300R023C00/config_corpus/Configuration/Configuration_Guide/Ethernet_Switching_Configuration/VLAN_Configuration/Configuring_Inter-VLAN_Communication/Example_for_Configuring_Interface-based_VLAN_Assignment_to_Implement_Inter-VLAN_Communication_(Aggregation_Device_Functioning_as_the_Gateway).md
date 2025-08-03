Example for Configuring Interface-based VLAN Assignment to Implement Inter-VLAN Communication (Aggregation Device Functioning as the Gateway)
=============================================================================================================================================

Example for Configuring Interface-based VLAN Assignment to Implement Inter-VLAN Communication (Aggregation Device Functioning as the Gateway)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001562013296__fig523919715818), PC1 and PC2 belong to VLAN 2 and VLAN 3 respectively and are connected to DeviceA at the aggregation layer through DeviceB at the access layer. PC3 belongs to VLAN 4 and is connected to DeviceA through DeviceC at the access layer. No configuration is performed on DeviceC, and DeviceC functions as a hub and supports plug-and-play. DeviceA functions as the gateway of PC1, PC2, and PC3 to allow PCs to communicate with each other and access the upper-layer device.

**Figure 1** Network diagram for configuring the aggregation device as the gateway![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001562172580.png)

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
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 2 3
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
2. Configure DeviceA at the aggregation layer.
   
   
   
   # Create VLANs.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2 to 5
   [*DeviceA] commit
   ```
   
   # Add interfaces connected to DeviceB and DeviceC to corresponding VLANs.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 2 3
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] port default vlan 4
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   # Configure VLANIF interfaces as gateways of PCs.
   
   ```
   [~DeviceA] interface vlanif 2
   [*DeviceA-Vlanif2] ip address 192.168.2.1 24
   [*DeviceA-Vlanif2] quit
   [*DeviceA] interface vlanif 3
   [*DeviceA-Vlanif3] ip address 192.168.3.1 24
   [*DeviceA-Vlanif3] quit
   [*DeviceA] interface vlanif 4
   [*DeviceA-Vlanif4] ip address 192.168.4.1 24
   [*DeviceA-Vlanif4] quit
   [*DeviceA] commit
   ```
   
   # Add the interface connected to the upper-layer device to the corresponding VLAN.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 5
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure a VLANIF interface to allow devices on internal network segments to access the upper-layer device.
   
   ```
   [~DeviceA] interface vlanif 5
   [*DeviceA-Vlanif5] ip address 192.168.5.1 24
   [*DeviceA-Vlanif5] quit
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
100GE1/0/1              trunk           1  2-3
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 2 to 5
  #
  interface Vlanif2
   ip address 192.168.2.1 255.255.255.0
  #
  interface Vlanif3  
   ip address 192.168.3.1 255.255.255.0 
  # 
  interface Vlanif4  
   ip address 192.168.4.1 255.255.255.0 
  # 
  interface Vlanif5  
   ip address 192.168.5.1 255.255.255.0 
  #
  interface 100GE1/0/1
   port default vlan 5
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 3
  #
  interface 100GE1/0/3
   port default vlan 4
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
   port link-type trunk
   port trunk allow-pass vlan 2 to 3 
  # 
  interface 100GE1/0/2
    
   port default vlan 2 
  # 
  interface 100GE1/0/3
    
   port default vlan 3 
  # 
  return
  ```