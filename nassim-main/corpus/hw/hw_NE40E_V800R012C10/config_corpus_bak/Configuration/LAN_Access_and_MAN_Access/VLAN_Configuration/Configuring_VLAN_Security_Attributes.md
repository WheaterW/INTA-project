Configuring VLAN Security Attributes
====================================

Configuring VLAN security attributes ensures reliable transmission of user data. Currently, the NE40E supports two security attributes. You can configure security attributes as required.

#### Applicable Environment

[Table 1](#EN-US_TASK_0172363119__tab_dc_vrp_vlan_cfg_002301) lists VLAN security attribute schemes.

**Table 1** Security schemes for VLANs
| Security Scheme | Description | Advantage | Disadvantage | Usage Scenario |
| --- | --- | --- | --- | --- |
| Disabling a port from broadcasting packets to other ports in the same VLAN | If a port in a VLAN receives a broadcast or unknown unicast packet, it will broadcast the packet to other ports in the VLAN. If the broadcast or unknown unicast packet is malicious, system resources waste and device performance deteriorates or even the device malfunctions. Disabling the port from broadcasting packets to other ports in the VLAN prevents malicious attacks. | - | - | This security scheme is applicable to topology-stable networks or networks on which MAC addresses are configured and forwarding paths are specified. |
| Disabling MAC address learning in a VLAN | If a device has only one inbound port and one outbound port, MAC address learning in a VLAN can be disabled. | * MAC address entries are saved. * Security is guaranteed. | This security scheme requires that the network has fixed users and forwarding paths have been established by using dynamic MAC address learning or by manually configuring MAC addresses.  If there are a large number of users connected to a switch, each user needs to be configured with a static forwarding path. This imposes a configuration burden on network administrators.  This security scheme prohibits new users from visiting the network. | This security scheme is applicable to topology-stable networks or networks on which MAC addresses are configured and forwarding paths are specified. |

#### Pre-configuration Tasks

Before configuring VLAN security attributes, complete the following task:

* Creating VLANs



[Disabling a Port from Broadcasting Packets to Other Ports in the Same VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0024.html)

Disabling a port from broadcasting packets to other ports in the same VLAN prevents malicious attacks and improves network security.

[Disabling MAC Address Learning in a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0025.html)

If a device has only one inbound port and one outbound port, or the network topology is stable, MAC address learning in a VLAN can be disabled.

[Verifying the VLAN Security Attribute Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0026.html)

After VLAN security attributes are configured, you can check whether a VLAN is enabled with the broadcast function and the MAC address learning function.