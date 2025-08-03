Example for Configuring Transparent Transmission of Protocol Packets in a VLAN
==============================================================================

Example for Configuring Transparent Transmission of Protocol Packets in a VLAN

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001414326377__fig880859125815), when multiple devices in the same VLAN communicate with the same server through DeviceA, DeviceA needs to process data first. As a result, the processing capability of the core switch decreases, which affects the communication effect and increases the communication cost. After transparent transmission of protocol packets in a VLAN is enabled on DeviceA to solve this problem, DeviceA directly forwards the data from the specified VLAN without sending the data to the CPU first. This improves DeviceA's running performance, reduces the communication cost, and minimizes the probability of malicious attacks on the device.

**Figure 1** Networking diagram of configuring transparent transmission of protocol packets in a VLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001363166870.png)

#### Procedure

1. Configure DeviceA.
   
   
   
   # Create a VLAN and enable transparent transmission of protocol packets in the VLAN.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] protocol-transparent
   [*DeviceA-vlan10] quit
   [*DeviceA] commit
   ```
   # Add interfaces to the VLAN.
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type hybrid
   [*DeviceA-100GE1/0/1] port hybrid tagged vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type hybrid
   [*DeviceA-100GE1/0/2] port hybrid tagged vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Configure DeviceB.
   
   
   
   # Add downlink interfaces to VLAN 10 and configure the uplink interface to allow packets from VLAN 10 to pass through.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan 10 
   [*DeviceB-vlan10] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type access
   [*DeviceB-100GE1/0/1] port default vlan 10
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type access
   [*DeviceB-100GE1/0/2] port default vlan 10
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 10
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# After the configuration is complete, enter the view of VLAN 10 on DeviceA, and run the [**display this**](cmdqueryname=display+this) command in the VLAN view. The command output shows that transparent transmission of protocol packets is enabled in the VLAN.

```
[~DeviceA] vlan 10
[~DeviceA-vlan10] display this
# 
vlan 10 
 protocol-transparent 
# 
return
```

#### Configuration Scripts

# DeviceA

```
#
sysname DeviceA
#
vlan 10
 protocol-transparent
#
interface 100GE1/0/1
 port link-type hybrid
 port hybrid tagged vlan 10
#
interface 100GE1/0/2
 port link-type hybrid
 port hybrid tagged vlan 10
#
return
```
# DeviceB
```
# 
sysname DeviceB 
# 
vlan batch 10 
# 
interface 100GE1/0/1
 port default vlan 10 
# 
interface 100GE1/0/2
 port default vlan 10 
# 
interface 100GE1/0/3
 port link-type trunk  
 port trunk allow-pass vlan 10 
# 
return
```