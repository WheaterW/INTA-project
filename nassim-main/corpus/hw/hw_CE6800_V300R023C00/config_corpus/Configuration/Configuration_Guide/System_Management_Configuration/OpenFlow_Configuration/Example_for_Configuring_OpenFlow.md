Example for Configuring OpenFlow
================================

Example for Configuring OpenFlow

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563989989__fig_1), DeviceA is an OpenFlow-compatible device, and there are reachable routes between the controller and DeviceA. To manage and control DeviceA through the controller, you can configure OpenFlow connection parameters on the controller and DeviceA. This will allow them to establish an OpenFlow connection and exchange information.

**Figure 1** OpenFlow networking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001563750129.png)

#### Procedure

1. Configure OpenFlow connection parameters on the controller.
   
   
   
   For details about configuring OpenFlow connection parameters on the controller, see the controller configuration guide.
2. Configure an OpenFlow agent.
   
   
   
   # Configure IP addresses for interfaces on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 20
   [*DeviceA-vlan20] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 10.1.1.2 24
   [*DeviceA-Vlanif20] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk pvid vlan 20
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface loopback 1
   [*DeviceA-LoopBack1] ip address 10.10.10.10 32
   [*DeviceA-LoopBack1] commit
   [~DeviceA-LoopBack1] quit
   ```
   
   # Configure the OpenFlow agent on DeviceA.
   
   ```
   [~DeviceA] sdn agent 
   [*DeviceA-sdn-agent] source-ip 10.10.10.10
   [*DeviceA-sdn-agent] controller-ip 10.1.2.1
   [*DeviceA-sdn-agent-ctrl-10.1.2.1] quit
   [*DeviceA-sdn-agent] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display sdn openflow session** command on DeviceA, after the configuration is complete, to check whether the OpenFlow connection between the controller and DeviceA is in Registered state. If it is in Registered state, the OpenFlow connection is successfully established.

```
[~DeviceA] display sdn openflow session

--------------------------------------------------------------------------------
Agent         : 10.10.10.10
Controller    : 10.1.2.1
UpTime        : 0d21h09m32s
State         : Registered
Role          : Master
VPN-instance  : _public_
--------------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
sdn agent
 source-ip 10.10.10.10
 controller-ip 10.1.2.1
#
vlan 20
#
interface Vlanif20
 ip address 10.1.1.2 255.255.255.0
#
interface 100GE 1/0/1
 port link-type trunk
 port trunk pvid vlan 20
 port trunk allow-pass vlan 20
#
interface LoopBack1
 ip address 10.10.10.10 255.255.255.255
#
return
```