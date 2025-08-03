Example for Configuring Interface- and VLAN-based Traffic Suppression
=====================================================================

This section provides an example for configuring interface- and VLAN-based traffic suppression in order to prevent interface- and VLAN-based MAC address attacks and control the number of access users. A networking diagram is provided to help you understand the configuration procedure. This example covers the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

In addition to user traffic management and bandwidth allocation, an Ethernet requires broadcast, multicast, and unknown unicast traffic to be suppressed to ensure the secure transmission of unicast traffic and properly utilize bandwidth resources. If these types of traffic are not suppressed, forwarding a large volume of such traffic consumes numerous bandwidth resources, reducing network performance and even causing a communication interruption.

On the network shown in [Figure 1](#EN-US_TASK_0172372583__fig_dc_ne_traff-supress_cfg_501001), interface1 and interface2 on the Router are both added to VLAN 10 and connected to PCs. Unicast traffic on interface1 and multicast and broadcast traffic on interface2 need to be suppressed to improve security.

**Figure 1** Networking diagram for configuring traffic suppression![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_ne_traff-supress_cfg_501001.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN and add interfaces to it.
2. Configure traffic suppression.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN ID: 10
* Interface numbers: GE0/1/0 and GE0/2/0
* Committed information rate (CIR)

#### Procedure

1. Add interfaces to the specified VLAN.
   
   
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
   [~Device] interface gigabitethernet0/1/0
   ```
   ```
   [~Device-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*Device-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*Device-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Device] interface GigabitEthernet0/2/0
   ```
   ```
   [*Device-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*Device-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*Device-GigabitEthernet0/2/0] quit
   ```
   ```
   [*Device] vlan 10
   ```
   ```
   [*Device-vlan10] port GigabitEthernet0/1/0
   ```
   ```
   [*Device-vlan10] port GigabitEthernet0/2/0
   ```
   ```
   [*Device-vlan10] commit
   ```
2. Enable traffic suppression for the VLAN.
   
   
   ```
   [~Device-vlan10] suppression inbound enable
   ```
   ```
   [*Device-vlan10] commit
   ```
   ```
   [~Device-vlan10] quit
   ```
3. Configure traffic suppression on the interfaces.
   
   
   ```
   [~Device] interface gigabitethernet0/1/0
   ```
   ```
   [~Device-GigabitEthernet0/1/0] broadcast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
   [*Device-GigabitEthernet0/1/0] multicast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
   [*Device-GigabitEthernet0/1/0] unknown-unicast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
   [*Device-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Device] interface gigabitethernet0/2/0
   ```
   ```
   [*Device-GigabitEthernet0/2/0] broadcast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
   [*Device-GigabitEthernet0/2/0] multicast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
   [*Device-GigabitEthernet0/2/0] unknown-unicast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
   [*Device-GigabitEthernet0/2/0] quit
   ```
   ```
   [*Device] commit
   ```
4. Verify the configuration.
   
   
   
   Run the **display this** command in the interface view to check the configuration.
   
   For example, check the configuration of GE0/1/0.
   
   ```
   [~Device-GigabitEthernet0/1/0] display this
   ```
   ```
   #
   ```
   ```
   interface GigabitEthernet0/1/0
   ```
   ```
    portswitch
   ```
   ```
    undo shutdown
   ```
   ```
    port default vlan 10
   ```
   ```
    broadcast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
    multicast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
    unknown-unicast-suppression cir 38400 cbs 7200000 inbound vlan 10
   ```
   ```
   #
   ```

#### Configuration Files

```
#
```
```
sysname Device
```
```
#
```
```
vlan batch 10
```
```
#
```
```
vlan 10
```
```
 suppression inbound enable   
```
```
#
```
```
interface GigabitEthernet0/1/0
```
```
 undo shutdown
```
```
 portswitch
```
```
 port GigabitEthernet0/1/0
```
```
 broadcast-suppression cir 38400 cbs 7200000 inbound vlan 10
```
```
 multicast-suppression cir 38400 cbs 7200000 inbound vlan 10
```
```
 unknown-unicast-suppression cir 38400 cbs 7200000 inbound vlan 10
```
```
#
```
```
interface GigabitEthernet0/2/0
```
```
 undo shutdown
```
```
 portswitch
```
```
 port GigabitEthernet0/2/0
```
```
 broadcast-suppression cir 38400 cbs 7200000 inbound vlan 10
```
```
 multicast-suppression cir 38400 cbs 7200000 inbound vlan 10
```
```
 unknown-unicast-suppression cir 38400 cbs 7200000 inbound vlan 10
```
```
#
```
```
return
```