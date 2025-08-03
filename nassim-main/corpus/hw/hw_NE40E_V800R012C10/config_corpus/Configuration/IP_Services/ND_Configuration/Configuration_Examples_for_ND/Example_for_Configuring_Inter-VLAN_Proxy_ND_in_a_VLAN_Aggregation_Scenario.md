Example for Configuring Inter-VLAN Proxy ND in a VLAN Aggregation Scenario
==========================================================================

This section provides an example for configuring inter-VLAN proxy ND to allow devices in different VLANs to communicate with each other in a VLAN aggregation scenario.

#### Networking Requirements

If hosts are on the same network segment and physical network but belong to different VLANs, inter-VLAN proxy ND must be enabled on the associated VLAN interfaces to enable Layer 3 interworking between the hosts.

On the network shown in [Figure 1](#EN-US_TASK_0172365198__fig_dc_vrp_nd_feature_002903), the device is connected to HostA, HostB, HostC, and HostD. These four hosts are on the same network segment, but HostA and HostB belong to VLAN 2 and HostC and HostD belong to VLAN 3. VLAN 2 and VLAN 3 constitute super VLAN 4, and the hosts in VLAN 2 and VLAN 3 that function as sub-VLANs cannot communicate with each other. To address this problem, enable inter-VLAN proxy ND on the VLANIF interface of the super VLAN.

**Figure 1** Inter-VLAN proxy ND in a VLAN aggregation scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE 0/1/1, GE 0/1/2, GE 0/2/1, and GE 0/2/2, respectively.


  
![](images/fig_dc_vrp_nd_feature_003714.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a super VLAN and sub-VLANs.
2. Add interfaces to the sub-VLANs.
3. Create a VLANIF interface for the super VLAN and assign an IPv6 address to the VLANIF interface.
4. Enable inter-VLAN proxy ND.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses of hosts in different VLANs
* IDs of the sub-VLANs and super VLAN
* IPv6 address of the VLANIF interface in the super VLAN

#### Procedure

1. Configure a super VLAN and sub-VLANs.
   
   
   1. # Configure sub-VLAN 2.
      
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
      [*Device-vlan2] quit
      ```
      ```
      [*Device] commit
      ```
   2. # Add GE 0/1/1 and GE 0/1/2 to sub-VLAN 2.
      
      ```
      [~Device] interface gigabitethernet 0/1/1
      ```
      ```
      [~Device-GigabitEthernet0/1/1] portswitch 
      ```
      ```
      [*Device-GigabitEthernet0/1/1] port link-type access
      ```
      ```
      [*Device-GigabitEthernet0/1/1] port default vlan 2
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
      [*Device-GigabitEthernet0/1/2] port link-type access
      ```
      ```
      [*Device-GigabitEthernet0/1/2] port default vlan 2
      ```
      ```
      [*Device-GigabitEthernet0/1/2] quit
      ```
      ```
      [*Device] commit
      ```
   3. # Configure sub-VLAN 3.
      
      ```
      [~Device] vlan 3
      ```
      ```
      [*Device-vlan3] quit
      ```
      ```
      [*Device] commit
      ```
   4. # Add GE 0/2/1 and GE 0/2/2 to sub-VLAN 3.
      
      ```
      [~Device] interface gigabitethernet 0/2/1
      ```
      ```
      [~Device-GigabitEthernet0/2/1] portswitch 
      ```
      ```
      [*Device-GigabitEthernet0/2/1] port link-type access
      ```
      ```
      [**Device-GigabitEthernet0/2/1] port default vlan 3
      ```
      ```
      [*Device-GigabitEthernet0/2/1] quit
      ```
      ```
      [*Device] interface gigabitethernet 0/2/2
      ```
      ```
      [*Device-GigabitEthernet0/2/2] portswitch 
      ```
      ```
      [*Device-GigabitEthernet0/2/2] port link-type access
      ```
      ```
      [*Device-GigabitEthernet0/2/2] port default vlan 3
      ```
      ```
      [*Device-GigabitEthernet0/2/2] quit
      ```
      ```
      [*Device] commit
      ```
   5. # Configure super VLAN 4 and add sub-VLAN 2 and sub-VLAN 3 to super VLAN 4.
      
      ```
      [~Device] vlan 4
      ```
      ```
      [*Device-vlan4] aggregate-vlan
      ```
      ```
      [*Device-vlan4] access-vlan 2
      ```
      ```
      [*Device-vlan4] access-vlan 3
      ```
      ```
      [*Device-vlan4] quit
      ```
      ```
      [*Device] commit
      ```
2. Create and configure VLANIF 4.
   
   
   
   # Create VLANIF 4.
   
   ```
   [~Device] interface Vlanif 4
   ```
   
   # Assign an IPv6 address to VLANIF 4.
   
   ```
   [*Device-Vlanif4] ipv6 enable 
   ```
   ```
   [*Device-Vlanif4] ipv6 address 2001:db8:300:400::5 64
   ```
3. Enable inter-VLAN proxy ND on VLANIF 4.
   
   
   ```
   [*Device-Vlanif4] ipv6 nd proxy inter-access-vlan enable 
   ```
   ```
   [*Device-Vlanif4] quit
   ```
   ```
   [*Device] commit
   ```
4. Configure the IPv6 addresses of hosts.
   
   
   
   # Configure the IPv6 address of HostA as 2001:db8:300:400::1/64.
   
   # Configure the IPv6 address of HostB as 2001:db8:300:400::2/64.
   
   # Configure the IPv6 address of HostC as 2001:db8:300:400::3/64.
   
   # Configure the IPv6 address of HostD as 2001:db8:300:400::4/64.
5. Verify the configuration.
   
   
   
   After the configuration is complete, hosts in sub-VLAN 2 and sub-VLAN 3 can ping each other.

#### Configuration Files

Device configuration file

```
#
sysname Device
#
vlan batch 2 to 4
#
vlan 4
 aggregate-vlan
 access-vlan 2 to 3
#
interface Vlanif4
 ipv6 enable
 ipv6 address 2001:DB8:300:400::5/64
 ipv6 nd proxy inter-access-vlan enable
#
interface GigabitEthernet0/1/1
 portswitch
 undo shutdown
 port link-type access
 port default vlan 2
#
interface GigabitEthernet0/1/2
 portswitch
 undo shutdown
 port link-type access
 port default vlan 2
#
interface GigabitEthernet0/2/1
 portswitch
 undo shutdown
 port link-type access
 port default vlan 3
#
interface GigabitEthernet0/2/2
 portswitch
 undo shutdown
 port link-type access
 port default vlan 3
#
return

```