Example for Configuring DHCP Snooping in a VLAN Mapping Scenario
================================================================

Example for Configuring DHCP Snooping in a VLAN Mapping Scenario

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512681146__fig8627748238), PC1 and PC2 connected to DeviceA belong to VLAN 5, and PC3 and PC4 connected to DeviceC belong to VLAN 6. PC1, PC2, PC3, and PC4 are on the same network segment. It is required that PCs in different VLANs communicate with each other through 1 to 1 VLAN mapping on DeviceB.

**Figure 1** Network diagram of configuring VLAN-based VLAN mapping (1 to 1)![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](../images/en-us_image_0000001513040418.png)

#### Configuration Roadmap

1. Configure VLAN-based VLAN mapping. For configuration details, see [Example for Configuring VLAN-based VLAN Mapping (1 to 1)](../vrp_vlan_cfg_0057.html).
2. Configure DHCP snooping on DeviceB where VLAN mapping is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

VLAN-based VLAN mapping can be configured only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.



#### Procedure

1. Configure DHCP snooping on DeviceB. Configure VLAN mapping on 100GE 1/0/1 and configure 100GE 1/0/1 and 100GE 1/0/2 to allow packets from VLAN 6 to pass through.
   
   
   
   # Enable DHCP snooping globally.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*DeviceB] commit
   [~DeviceB] dhcp enable
   [*DeviceB] dhcp snooping enable
   [*DeviceB] commit
   ```
   
   # Enable DHCP snooping on 100GE 1/0/1 connected to the user side.
   
   ```
   [~DeviceB] interface 100GE 1/0/1
   [*DeviceB-100GE1/0/1] dhcp snooping enable
   [*DeviceB-100GE1/0/1] quit
   ```
   
   
   
   # Configure the interface connected to the DHCP server as a trusted one.
   
   ```
   [~DeviceB] interface 100GE 1/0/2
   [*DeviceB-100GE1/0/2] dhcp snooping trusted
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the information about the DHCP snooping binding table on DeviceB.

```
[~DeviceB] display dhcp snooping user-bind all
DHCP Dynamic Bind-table:
Flags:O - outer vlan ,I - inner vlan   
IP Address       MAC Address     VLAN(O/I)/(BD-VLAN)        Interface          Lease            
------------------------------------------------------------------------------------------------------- 
10.1.1.141      00e0-fc12-3456    6/-/--                    100GE1/0/1           2022.03.27-07:31
------------------------------------------------------------------------------------------------------- 
Print count:           1          Total count:           1 
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 5
  #
  interface 100GE1/0/1
   port link-type access
   port default vlan 5
  #
  interface 100GE1/0/2
   port link-type access
   port default vlan 5
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 5
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan batch 6
  #
  dhcp enable
  #
  dhcp snooping enable
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 6
   port vlan-mapping vlan 5 map-vlan 6
   dhcp snooping enable 
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 6
   dhcp snooping trusted
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 6
  #
  interface 100GE1/0/1
   port link-type access
   port default vlan 6
  #
  interface 100GE1/0/2
   port link-type access
   port default vlan 6
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 6
  #
  return
  ```