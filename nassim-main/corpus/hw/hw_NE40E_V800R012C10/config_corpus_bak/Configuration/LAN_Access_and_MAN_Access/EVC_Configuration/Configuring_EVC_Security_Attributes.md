Configuring EVC Security Attributes
===================================

The NE40E supports various security attributes that can be deployed in a BD to help devices securely transmit packets.

#### Usage Scenario

[Table 1](#EN-US_TASK_0172363377__tab_4) describes the security functions that can be deployed in a BD to help devices securely transmit packets.

**Table 1** Security functions
| **Security Function** | **Description** | **Usage Scenario** |
| --- | --- | --- |
| Disabling an EVC Layer 2 sub-interface in a BD from forwarding packets | When an EVC Layer 2 sub-interface in a BD receives broadcast, unknown unicast, or unknown multicast packets, it broadcasts the packets to other interfaces in the BD.  If these packets are malicious, the device resources are occupied, causing the device performance to deteriorate or device breakdown. Disabling an EVC Layer 2 sub-interface from broadcasting received packets to other interfaces in the BD prevents malicious attacks. | This function applies to networks without user changes or networks with static MAC address-based forwarding paths. |
| Disabling MAC address learning in a BD | If a BD has only one inbound interface and one outbound interface, to save MAC address entries, the MAC address learning function can be disabled in the BD.  This function helps efficiently use the MAC address table space and improves security. | This function applies to networks without user changes or networks with static MAC address-based forwarding paths.  If static MAC addresses are used and a great number of users access a switch, information about each user must be configured to establish a forwarding path. This increases the workload of the network administrator. New users cannot access a device that has this function enabled. |
| Split horizon | A BD is a broadcast domain, in which an EVC Layer 2 sub-interface broadcasts received packets within the domain. To reduce the broadcast volume, EVC Layer 2 sub-interfaces that do not need to communicate can be isolated from one another in the same BD To meet this requirement, enable split horizon to isolate EVC Layer 2 sub-interfaces from one another in the BD. | Split horizon applies to all Layer 2 networks. |

#### Pre-configuration Tasks

Before configuring EVC security attributes, [create a BD](dc_vrp_evc_cfg_0004.html).



[Disabling an Interface from Broadcasting Packets to Other Interfaces in a Bridge Domain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0013.html)

You can disable an EVC Layer 2 sub-interface from broadcasting packets to other EVC Layer 2 sub-interfaces in a bridge domain. This function helps devices from being attacked and improves network security.

[Disabling Devices in a Bridge Domain from Learning One Another's MAC Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0014.html)

If a bridge domain has only one inbound interface and one outbound interface, the MAC address learning function can be disabled in the bridge domain.

[Configuring Split Horizon in a Bridge Domain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0021.html)

A bridge domain is a broadcast domain, in which bridge domain members broadcast received unknown unicast, multicast, or broadcast packets within the domain. To reduce the broadcast traffic volume, enable split horizon in the bridge domain, which isolates bridge domain member interfaces from one another if they do not need to communicate.

[Checking the Configurations](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0022.html)

After configuring EVC security attributes, you can check bridge domain configurations, including whether the broadcast forwarding, MAC address learning, and split horizon are enabled.