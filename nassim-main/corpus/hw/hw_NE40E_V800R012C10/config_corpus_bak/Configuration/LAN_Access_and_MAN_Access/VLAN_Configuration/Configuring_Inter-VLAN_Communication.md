Configuring Inter-VLAN Communication
====================================

Configuring inter-VLAN communication allows users in different VLANs to communicate with each other.

#### Usage Scenario

Currently, schemes listed in [Table 1](#EN-US_TASK_0172363105__tab_dc_vrp_vlan_cfg_001701) are provided for inter-VLAN communication. You can choose one of them based on the real world situation.

**Table 1** Schemes for inter-VLAN communication
| Inter-VLAN Communication Scheme | Advantage | Disadvantage | Usage Scenario |
| --- | --- | --- | --- |
| Sub-interface | After sub-interfaces are configured, users in different VLANs and network segments can communicate with each other as long as routes are reachable. | * Both Layer 2 and Layer 3 devices are required, which increases expenditure. * If multiple users on a network belong to different VLANs, each VLAN requires a sub-interface on a Layer 3 device. Each sub-interface needs to be assigned an IP address. This increases configuration workload and uses up a large number of IP addresses. | This scheme is applicable to small-scale networks on which users belong to different network segments. |
| VLANIF interface | After sub-interfaces are configured, users in different VLANs and network segments can communicate with each other as long as routes are reachable.  Inter-VLAN communication can also be implemented by Layer 3 switches if routes are reachable. This scheme boasts of low operating costs. | If multiple users on a network belong to different VLANs, each VLAN requires a VLANIF interface. Each VLANIF interface needs to be assigned an IP address. This increases configuration workload and uses a lot of IP addresses. | This scheme is applicable to small-scale networks on which users belong to different network segments and IP addresses of these users are seldom changed. |
| VLAN mapping | This scheme is easily configured and does not rely on routes. | IP addresses of users in different VLANs must belong to the same network segment. | This scheme is applicable to large-scale networks on which multiple users belong to one network segment. |

#### Pre-configuration Tasks

Before configuring communication between VLANs, complete the following task:

* Creating VLANs



[Configuring Sub-interfaces for Inter-VLAN Communication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0019.html)

If users belong to different VLANs and reside on different network segments, sub-interfaces can be created on an Layer 3 device and assigned IP addresses to allow these users to communicate with each other at the network layer.

[Configuring VLANIF Interfaces for Inter-VLAN Communication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0020.html)

Configuring VLANIF interfaces for inter-VLAN communication saves expenditure and helps implement fast forwarding.

[Configuring VLAN Mapping for Inter-VLAN Communication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0059.html)

The configuration of VLAN mapping is simple and independent of Layer 3 routing. 

[Verifying the Inter-VLAN Communication Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0021.html)

After inter-VLAN communication is configured, you can check whether users in different VLANs can communicate with each other and check information about VLANs to which users belong.