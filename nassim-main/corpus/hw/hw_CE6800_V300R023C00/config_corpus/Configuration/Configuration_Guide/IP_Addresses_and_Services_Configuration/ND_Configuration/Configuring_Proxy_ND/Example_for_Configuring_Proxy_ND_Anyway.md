Example for Configuring Proxy ND Anyway
=======================================

Example for Configuring Proxy ND Anyway

#### Networking Requirements

In scenarios where servers are partitioned into VMs, the flexible deployment and migration of VMs on multiple servers or gateways can be achieved by configuring Layer 2 interconnection between multiple gateways. However, this approach may lead to larger Layer 2 domains on the network and the risk of broadcast storms. To resolve this issue, enable proxy ND anyway on a VM gateway. In this way, the gateway sends its interface MAC address to a source VM and communication between VMs is implemented through route forwarding.

As shown in [Figure 1](#EN-US_TASK_0000001130782314__fig12417825103810), there is a reachable route between DeviceA and DeviceB. If DeviceA or DeviceB is not required to determine whether a route to a destination VM exists and the other VMs in the same subnet do not respond to an NS message from a source VM, you can configure proxy ND anyway on the devices to allow the two VMs in different subnets to communicate.

**Figure 1** Typical network diagram of proxy ND anyway![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 1/0/1.


  
![](figure/en-us_image_0000001176662215.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN so that the VMs that need to communicate are in the VLAN.
2. Configure interface attributes and associate the interface with the VLAN.
3. Assign an IPv6 address to each interface.
4. Configure proxy ND anyway on each device's VLANIF interface.
5. Configure each device to advertise IPv6 NDP Vlink direct routes.

#### Data Preparation

To complete the configuration, you need the following data:

* ID of the VLAN to which the devices and VMs belong
* IPv6 addresses of device interfaces connected to VMs
* IPv6 addresses of VMs

#### Procedure

1. Create a VLAN.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Configure the same VLAN ID on DeviceA and DeviceB.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] commit
   [*DeviceA-vlan10] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceB] vlan 10
   [*DeviceB-vlan10] commit
   [*DeviceB-vlan10] quit
   ```
2. Configure interface attributes and associate the interface with the VLAN.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1 
   [~DeviceA-100ge1/0/1] portswitch
   [*DeviceA-100ge1/0/1] port link-type access
   [*DeviceA-100ge1/0/1] quit
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] port 100ge 1/0/1 
   [*DeviceA-vlan10] commit
   [~DeviceA-vlan10] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100ge1/0/1] portswitch
   [*DeviceB-100ge1/0/1] port link-type access
   [*DeviceB-100ge1/0/1] quit
   [*DeviceB] vlan 10
   [*DeviceB-vlan10] port 100ge 1/0/1
   [*DeviceB-vlan10] commit
   [~DeviceB-vlan10] quit
   ```
3. Assign an IPv6 address to each interface.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Configure the same VLANIF interface address on DeviceA and DeviceB.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ipv6 enable
   [*DeviceA-Vlanif10] ipv6 address 2001:db8:300:400::3 64
   [*DeviceA-Vlanif10] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface vlanif 10
   [*DeviceB-Vlanif10] ipv6 enable
   [*DeviceB-Vlanif10] ipv6 address 2001:db8:300:400::3 64
   [*DeviceB-Vlanif10] commit
   ```
4. Enable proxy ND anyway and configure each device to advertise IPv6 NDP Vlink direct routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA-Vlanif10] ipv6 nd proxy anyway enable
   [*DeviceA-Vlanif10] quit
   [*DeviceA] ipv6 nd direct-route enable
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [*DeviceB-Vlanif10] ipv6 nd proxy anyway enable
   [*DeviceB-Vlanif10] quit
   [*DeviceB] ipv6 nd direct-route enable
   [*DeviceB] commit
   ```
5. Configure VMs.
   
   
   
   # Set the IPv6 address of VM1 to 2001:db8:300:400::1/64.
   
   # Set the IPv6 address of VM2 to 2001:db8:300:400::2/64.

#### Verifying the Configuration

# After the configuration is complete, check that VM1 and VM2 can ping each other.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 10
  #
  interface Vlanif10
   ipv6 enable
   ipv6 address 2001:DB8:300:400::3/64
   ipv6 nd proxy anyway enable
  #
  interface 100GE 1/0/1
   port link-type access
   port default vlan 10
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 10
  #
  interface Vlanif10
   ipv6 enable
   ipv6 address 2001:DB8:300:400::3/64
   ipv6 nd proxy anyway enable
  #
  interface 100GE 1/0/1
   port link-type access
   port default vlan 10
  #
  return
  ```