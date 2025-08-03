Example for Configuring Proxy ND Anyway
=======================================

This section provides an example for configuring proxy ND anyway in a scenario where VMs are on the same network segment but different physical networks and the gateways connected to the VMs have the same address.

#### Networking Requirements

In scenarios where servers are partitioned into VMs, to allow flexible deployment and migration of VMs on multiple servers or gateways, the common solution is to configure Layer 2 interworking between multiple gateways. However, this approach may lead to larger Layer 2 domains on the network and risks of broadcast storms. To resolve this problem, a common way is to enable any proxy ND on a VM gateway so that the gateway sends its own MAC address to the source VM and the traffic sent from the source VM to other VMs is transmitted over routes.

On the network shown in [Figure 1](#EN-US_TASK_0172365194__fig_dc_vrp_nd_feature_002904), the routes between DeviceA and DeviceB are reachable. If DeviceA or DeviceB does not need to determine whether routes destined for the peer device exist and the other VMs on the same subnet do not reply with packets carrying their MAC address to the request VM, configure proxy ND anyway to allow the VMs in different subnets to communicate with each other.**Figure 1** Proxy ND anyway![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE 0/1/1.


  
![](images/fig_dc_vrp_nd_feature_003706.png)  



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VLAN so that the VMs which need to communicate with each other reside in the same VLAN.
2. Configure interface attributes and bind the interfaces to the VLAN.
3. Assign IPv6 addresses to interfaces.
4. Configure proxy ND anyway on a device's VLANIF interface. After receiving an NS message (for the destination VM's MAC address) sent by the VM, the device that has proxy ND anyway enabled responds to the message with its own MAC address. The VM then forwards data to the device.
5. Configure advertisement of IPv6 NDP Vlink direct routes.

#### Data Preparation

To complete the configuration, you need the following data:

* ID of the VLAN to which devices and VMs belong
* IPv6 addresses of VM-side interfaces
* IPv6 addresses of VMs

#### Procedure

1. Create a VLAN.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configure the same VLAN ID on DeviceA and DeviceB.
   
   
   # Configure DeviceA.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
   
   # Configure DeviceB.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] vlan 10
   ```
   ```
   [*DeviceB-vlan10] commit
   ```
   ```
   [~DeviceB-vlan10] quit
   ```
2. Configure interface attributes and bind the interfaces to the VLAN.
   
   # Configure DeviceA.
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] vlan 10
   ```
   ```
   [*DeviceA-vlan10] port gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan10] commit
   ```
   ```
   [~DeviceA-vlan10] quit
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] vlan 10
   ```
   ```
   [*DeviceB-vlan10] port gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-vlan10] commit
   ```
   ```
   [~DeviceB-vlan10] quit
   ```
3. Assign IPv6 addresses to interfaces.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configure the same VLANIF interface address on DeviceA and DeviceB.
   
   
   # Configure DeviceA.
   ```
   [~DeviceA] interface vlanif 10
   ```
   ```
   [*DeviceA-Vlanif10] ipv6 enable
   ```
   ```
   [*DeviceA-Vlanif10] ipv6 address 2001:db8:300:400::3 64
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] interface vlanif 10
   ```
   ```
   [*DeviceB-Vlanif10] ipv6 enable
   ```
   ```
   [*DeviceB-Vlanif10] ipv6 address 2001:db8:300:400::3 64
   ```
4. Enable proxy ND anyway and configure the advertisement of IPv6 NDP Vlink direct routes.
   
   # Configure DeviceA.
   ```
   [*DeviceA-Vlanif10] ipv6 nd proxy anyway enable
   ```
   ```
   [*DeviceA-Vlanif10] quit
   ```
   ```
   [*DeviceA] ipv6 nd vlink-direct-route advertise
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   [*DeviceB-Vlanif10] ipv6 nd proxy anyway enable
   ```
   ```
   [*DeviceB-Vlanif10] quit
   ```
   ```
   [*DeviceB] ipv6 nd vlink-direct-route advertise
   ```
   ```
   [*DeviceB] commit
   ```
5. Configure VMs.
   
   
   
   # Configure the IPv6 address of VM1 as 2001:db8:300:400::1/64.
   
   # Configure the IPv6 address of VM2 as 2001:db8:300:400::2/64.
6. Verify the configuration.
   
   
   
   After the configurations are complete, VM1 and VM2 can communicate with each other.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 10
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type access
   port default vlan 10
  #
  interface Vlanif10
   ipv6 enable
   ipv6 address 2001:DB8:300:400::3/64
   ipv6 nd proxy anyway enable
  #
   ipv6 nd vlink-direct-route advertise
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 10
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type access
   port default vlan 10
  #
  interface Vlanif10
   ipv6 enable
   ipv6 address 2001:DB8:300:400::3/64
   ipv6 nd proxy anyway enable
  #
   ipv6 nd vlink-direct-route advertise
  #
  return
  ```