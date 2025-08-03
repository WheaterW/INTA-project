Example for Configuring Local VLAN Mirroring
============================================

Example for Configuring Local VLAN Mirroring

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001564126405__fig1032713294329), HostA and HostB belong to VLAN 10 and access the Internet through DeviceA, which is directly connected to the monitoring device Server. Internet access traffic of hosts in VLAN 10 needs to be monitored on the Server.

**Figure 1** Networking diagram of local VLAN mirroring![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, and 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001513046346.png)

#### Procedure

1. Create VLAN 10 on DeviceA, and add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 10.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Configure 100GE 1/0/3 on DeviceA as an observing port.
   
   
   ```
   [~DeviceA] observe-port 1 interface 100ge 1/0/3
   [*DeviceA] commit
   ```
3. Configure VLAN mirroring on DeviceA to copy packets received by interfaces in VLAN 10 to the observing port.
   
   
   ```
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] mirroring observe-port 1 inbound
   [*DeviceA-vlan10] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the mirroring configuration

```
[~DeviceA] display port-mirroring
  VLAN mirroring:
  -----------------------------------------------------------------------------
  VLAN                  Direction        ObservePort : Interface
  -----------------------------------------------------------------------------
  VLAN 10               Inbound                    1 : 100GE1/0/3
  -----------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10
#
observe-port 1 interface 100GE1/0/3
#
vlan 10
 mirroring observe-port 1 inbound
#
interface 100GE1/0/1
 port default vlan 10
#
interface 100GE1/0/2
 port default vlan 10
#
return
```