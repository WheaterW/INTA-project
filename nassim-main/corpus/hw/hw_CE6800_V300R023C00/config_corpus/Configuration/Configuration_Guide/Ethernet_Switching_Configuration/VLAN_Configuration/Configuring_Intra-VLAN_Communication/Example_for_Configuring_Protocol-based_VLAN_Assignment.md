Example for Configuring Protocol-based VLAN Assignment
======================================================

Example for Configuring Protocol-based VLAN Assignment

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176742331__fig880859125815), PC1 and PC2 use IPv4 and IPv6, respectively. PCs using different protocols need to be added to different VLANs. In this example, PC1 needs to be added to VLAN 10, and PC2 needs to be added to VLAN 20.

**Figure 1** Networking diagram for configuring protocol-based VLAN assignment![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130622910.png)![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this example.




#### Procedure

1. Create VLAN 10 and VLAN 20 and associate them with the IPv4 and IPv6 protocols, respectively.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10 20
   [*DeviceA] vlan 10
   [*DeviceA-vlan10] protocol-vlan ipv4
   [*DeviceA-vlan10] quit
   [*DeviceA] vlan 20
   [*DeviceA-vlan20] protocol-vlan ipv6
   [*DeviceA-vlan20] quit
   [*DeviceA] commit
   ```
2. Associate 100GE 1/0/2 and 100GE 1/0/3 with VLAN 10 and VLAN 20, respectively.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] protocol-vlan vlan 10 all priority 5
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type hybrid
   [*DeviceA-100GE1/0/2] port hybrid untagged vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] protocol-vlan vlan 20 all priority 6
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type hybrid
   [*DeviceA-100GE1/0/3] port hybrid untagged vlan 20
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display protocol-vlan vlan all**](cmdqueryname=display+protocol-vlan+vlan+all) command to check the types and indexes of the protocols associated with VLANs.

```
[~DeviceA] display protocol-vlan vlan all
----------------------------------------------------------------
VLAN           Protocol Index    Protocol Type
----------------------------------------------------------------
10             0                 ipv4
20             0                 ipv6
```

# Run the [**display protocol-vlan interface all**](cmdqueryname=display+protocol-vlan+interface+all) command to check the protocol-based VLAN configuration on all interfaces.

```
[~DeviceA] display protocol-vlan interface all
-------------------------------------------------------------------------------
Interface                   VLAN    Index     Protocol Type           Priority
-------------------------------------------------------------------------------
100GE1/0/2                  10      0         ipv4                    5
100GE1/0/3                  20      0         ipv6                    6
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10 20
#
vlan 10
 protocol-vlan 0 ipv4
#
vlan 20
 protocol-vlan 0 ipv6
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10 20
#
interface 100GE1/0/2
 port link-type hybrid
 port hybrid untagged vlan 10
 protocol-vlan vlan 10 0 priority 5
#
interface 100GE1/0/3
 port link-type hybrid
 port hybrid untagged vlan 20
 protocol-vlan vlan 20 0 priority 6
#
return
```