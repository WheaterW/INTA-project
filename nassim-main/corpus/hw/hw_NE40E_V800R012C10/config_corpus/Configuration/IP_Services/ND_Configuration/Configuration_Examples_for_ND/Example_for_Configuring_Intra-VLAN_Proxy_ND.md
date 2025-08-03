Example for Configuring Intra-VLAN Proxy ND
===========================================

This section provides an example for configuring intra-VLAN proxy ND in a scenario where hosts are on the same network segment and VLAN but the VLAN is configured with user isolation.

#### Networking Requirements

If hosts belong to the same VLAN but the VLAN is configured with Layer 2 port isolation, intra-VLAN proxy ND needs to be enabled on the associated VLAN interfaces to enable host interworking.

On the network shown in [Figure 1](#EN-US_TASK_0172365195__fig_dc_vrp_nd_feature_002904), the device is connected to HostA and HostB. The interfaces connected to HostA and HostB belong to the same sub-VLAN, which is configured with Layer 2 port isolation. Therefore, HostA and HostB cannot directly communicate with each other at Layer 2. If HostA and HostB need to communicate with each other, enable intra-VLAN proxy ND on the device.

**Figure 1** Intra-VLAN proxy ND![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_nd_feature_003711.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create and configure a super VLAN and a sub-VLAN.
2. Add interfaces to the sub-VLAN.
3. Create a VLANIF interface for the super VLAN and assign an IPv6 address to the VLANIF interface.
4. Enable intra-VLAN proxy ND on the VLANIF interface in the super VLAN.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of the VLANIF interface
* IPv6 addresses of HostA and HostB

#### Procedure

1. Configure a super VLAN and a sub-VLAN.
   
   
   
   # Configure a sub-VLAN.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] vlan 2
   ```
   ```
   [*Device-vlan2] commit
   ```
   ```
   [~Device-vlan2] quit
   ```
   
   # Add interfaces to the sub-VLAN.
   
   ```
   [~Device] interface gigabitethernet 0/1/1
   ```
   ```
   [~Device-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*Device-GigabitEthernet0/1/1] port default vlan 2
   ```
   ```
   [*Device-GigabitEthernet0/1/1] port isolate-state enable vlan 2
   ```
   ```
   [*Device-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Device] interface gigabitethernet 0/1/2
   ```
   ```
   [*Device-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*Device-GigabitEthernet0/1/2] port default vlan 2
   ```
   ```
   [*Device-GigabitEthernet0/1/2] port isolate-state enable vlan 2
   ```
   ```
   [*Device-GigabitEthernet0/1/2] quit
   ```
   ```
   [*Device] commit
   ```
   
   # Configure a super VLAN, and add the sub-VLAN to the super VLAN.
   
   ```
   [~Device] vlan 3
   ```
   ```
   [*Device-vlan3] aggregate-vlan
   ```
   ```
   [*Device-vlan3] access-vlan 2
   ```
   ```
   [*Device-vlan3] quit
   ```
   ```
   [*Device] commit
   ```
2. Create and configure a VLANIF interface.
   
   
   
   # Create VLANIF 3.
   
   ```
   [~Device] interface Vlanif 3
   ```
   
   # Assign an IPv6 address to VLANIF 3.
   
   ```
   [*Device-Vlanif3] ipv6 enable
   ```
   ```
   [*Device-Vlanif3] ipv6 address 2001:db8:300:400::4 64
   ```
3. Enable intra-VLAN proxy ND on the VLANIF interface.
   
   
   ```
   [*Device-Vlanif3] ipv6 nd proxy inner-access-vlan enable
   ```
   ```
   [*Device-Vlanif3] commit
   ```
4. Configure the IPv6 addresses of hosts.
   
   
   
   # Configure the IPv6 address of HostA as 2001:db8:300:400::1/64.
   
   # Configure the IPv6 address of HostB as 2001:db8:300:400::3/64.
5. Verify the configuration.
   
   
   
   After the configuration is complete, HostA and HostB can ping each other.

#### Configuration Files

Device configuration file

```
#
sysname Device
#
vlan batch 2 to 3 
#
vlan 3
 aggregate-vlan
 access-vlan 2
#
interface Vlanif3
 ipv6 enable
 ipv6 address 2001:DB8:300:400::4/64
 ipv6 nd proxy inner-access-vlan enable
#
interface GigabitEthernet0/1/1
 portswitch
 port default vlan 2
 port isolate-state enable vlan 2
#
interface GigabitEthernet0/1/2
 portswitch
 port default vlan 2
 port isolate-state enable vlan 2
#
return

```