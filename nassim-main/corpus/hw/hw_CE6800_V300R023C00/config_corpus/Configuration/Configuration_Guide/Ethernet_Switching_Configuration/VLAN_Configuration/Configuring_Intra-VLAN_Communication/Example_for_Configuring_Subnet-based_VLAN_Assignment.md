Example for Configuring Subnet-based VLAN Assignment
====================================================

Example for Configuring Subnet-based VLAN Assignment

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130782648__fig17135183813121), PC1, PC2, and PC3 are located on different network segments. It is necessary for PCs on different network segments to be added to different VLANs. In this example, PC1, PC2, and PC3 need to be added to VLAN 100, VLAN 200, and VLAN 300, respectively.

**Figure 1** Networking diagram of configuring subnet-based VLAN assignment![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001176742353.png)![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this example.




#### Procedure

1. Create VLANs and associate subnets with the VLANs.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 100 200 300
   [*DeviceA] vlan 100
   [*DeviceA-vlan100] ip-subnet-vlan 1 ip 192.168.1.2 24 priority 2
   [*DeviceA-vlan100] quit
   [*DeviceA] vlan 200
   [*DeviceA-vlan200] ip-subnet-vlan 1 ip 192.168.2.2 24 priority 3
   [*DeviceA-vlan200] quit
   [*DeviceA] vlan 300
   [*DeviceA-vlan300] ip-subnet-vlan 1 ip 192.168.3.2 24 priority 4
   [*DeviceA-vlan300] quit
   [*DeviceA] commit
   ```
2. Set 100GE 1/0/1 to a hybrid interface, configure the interface to allow packets from VLAN 100, VLAN 200, and VLAN 300 to pass through, and enable subnet-based VLAN assignment on the interface.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type hybrid
   [*DeviceA-100GE1/0/1] port hybrid untagged vlan 100
   [*DeviceA-100GE1/0/1] port hybrid untagged vlan 200
   [*DeviceA-100GE1/0/1] port hybrid untagged vlan 300
   [*DeviceA-100GE1/0/1] ip-subnet-vlan enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display ip-subnet-vlan vlan all**](cmdqueryname=display+ip-subnet-vlan+vlan+all) command on DeviceA to check information about subnets associated with VLANs.

```
[~DeviceA] display ip-subnet-vlan vlan all
 IP-subnet-VLAN count: 3                 total count: 3
 ----------------------------------------------------------------
 VLAN    Index  IpAddress            SubnetMask          Priority
 ----------------------------------------------------------------
  100        1  192.168.1.2          255.255.255.0              2
  200        1  192.168.2.2          255.255.255.0              3
  300        1  192.168.3.2          255.255.255.0              4
 ----------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 100 200 300
#
vlan 100
 ip-subnet-vlan 1 ip 192.168.1.2 255.255.255.0 priority 2
#
vlan 200
 ip-subnet-vlan 1 ip 192.168.2.2 255.255.255.0 priority 3
#
vlan 300
 ip-subnet-vlan 1 ip 192.168.3.2 255.255.255.0 priority 4
#
interface 100GE1/0/1
 port link-type hybrid
 port hybrid untagged vlan 100
 port hybrid untagged vlan 200
 port hybrid untagged vlan 300
 ip-subnet-vlan enable
#
return
```