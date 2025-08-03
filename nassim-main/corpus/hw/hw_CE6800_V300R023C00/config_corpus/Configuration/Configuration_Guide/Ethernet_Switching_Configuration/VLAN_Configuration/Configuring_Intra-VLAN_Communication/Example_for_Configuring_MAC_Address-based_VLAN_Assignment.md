Example for Configuring MAC Address-based VLAN Assignment
=========================================================

Example for Configuring MAC Address-based VLAN Assignment

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130622862__fig67001658141112), Host1, Host2, and Host3 are added to VLAN 10 based on their MAC addresses. They can communicate with each other and also access the Internet. Hosts with MAC addresses not associated with VLAN 10 cannot access the Internet or communicate with authorized hosts in VLAN 10.

**Figure 1** Networking diagram of configuring MAC address-based VLAN assignment![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001130782702.png)
![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this example.



#### Procedure

1. Create VLAN 10 and associate host MAC addresses with the VLAN.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] mac-vlan mac-address 00e0-fc00-1111
   [*DeviceA-vlan10] mac-vlan mac-address 00e0-fc00-2222
   [*DeviceA-vlan10] mac-vlan mac-address 00e0-fc00-3333
   [*DeviceA-vlan10] quit
   [*DeviceA] commit
   ```
2. On DeviceA, add all four interfaces to VLAN 10 and enable MAC address-based VLAN assignment on 100GE 1/0/2 to 100GE 1/0/4.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type hybrid
   [*DeviceA-100GE1/0/1] port hybrid tagged vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type hybrid
   [*DeviceA-100GE1/0/2] port hybrid untagged vlan 10
   [*DeviceA-100GE1/0/2] mac-vlan enable
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type hybrid
   [*DeviceA-100GE1/0/3] port hybrid untagged vlan 10
   [*DeviceA-100GE1/0/3] mac-vlan enable
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] portswitch
   [*DeviceA-100GE1/0/4] port link-type hybrid
   [*DeviceA-100GE1/0/4] port hybrid untagged vlan 10
   [*DeviceA-100GE1/0/4] mac-vlan enable
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display mac-vlan vlan 10** command to view MAC addresses associated with VLAN 10.

```
[~DeviceA] display mac-vlan vlan 10
Total MAC VLAN address count: 3
---------------------------------------------------
MAC Address     Mask            VLAN    Priority
---------------------------------------------------
00e0-fc00-1111  ffff-ffff-ffff    10           0
00e0-fc00-2222  ffff-ffff-ffff    10           0
00e0-fc00-3333  ffff-ffff-ffff    10           0
```

# Authorized hosts Host1, Host2, and Host3 on the network can communicate with each other and access the Internet. Hosts with MAC addresses not associated with VLAN 10 cannot access the Internet or communicate with the authorized hosts.


#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10
#
vlan 10
 mac-vlan mac-address 00e0-fc00-1111
 mac-vlan mac-address 00e0-fc00-2222
 mac-vlan mac-address 00e0-fc00-3333
#
interface 100GE1/0/1
 port link-type hybrid
 port hybrid tagged vlan 10
#
interface 100GE1/0/2
 port link-type hybrid
 port hybrid untagged vlan 10
 mac-vlan enable
#
interface 100GE1/0/3
 port link-type hybrid
 port hybrid untagged vlan 10
 mac-vlan enable
#
interface 100GE1/0/4
 port link-type hybrid
 port hybrid untagged vlan 10
 mac-vlan enable
#
return
```