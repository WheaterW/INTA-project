Configuring MAC Flapping-based Loop Detection for a VLAN
========================================================

After MAC flapping-based loop detection is configured on a virtual private LAN service (VLAN) network, the devices can detect loops on AC-side interfaces or pseudo wires (PWs), and block interfaces or PWs or report alarms.

#### Usage Scenario

Generally, redundant links are used on an Ethernet network
to provide link backup and enhance network reliability. Redundant
links, however, may produce loops and cause broadcast storms and MAC
address entry flapping. As a result, the communication quality deteriorates,
and communication services may even be interrupted. To eliminate loops
on the network, the spanning tree protocols or Layer 2 loop detection
technology was introduced. If you want to apply a spanning tree protocol,
the protocol must be supported and you need to configure it on each
user network device. If you want to apply the Layer 2 loop detection
technology, user network devices must allow Layer 2 loop detection
packets to pass. Therefore, the spanning tree protocols or the Layer
2 loop detection technology cannot be used to eliminate loops on user
networks with unknown connections or user networks that do not support
the spanning tree protocols or Layer 2 loop detection technology.

MAC flapping-based loop detection is introduced to address
this problem. It does not require protocol packet negotiation between
devices. A device independently checks whether a loop occurs on the
network based on MAC address entry flapping.

You can deploy MAC flapping-based loop detection on network edge devices and configure a blocking policy for interfaces to prevent loops. The blocking policy can be either of the following:

* Blocking interfaces based on their blocking priorities: If a device detects a loop, it blocks the interface with a lower blocking priority.
* Blocking interfaces based on their trusted or untrusted states: If a device detects a loop, it blocks the untrusted interface.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After MAC flapping-based loop detection
is configured on a device and the device receives packets with fake
source MAC addresses from attackers, the device may mistakenly conclude
that a loop has occurred and block an interface based on the configured
blocking policy. Therefore, key user traffic may be blocked. It is
recommended that you disable MAC flapping-based loop detection on
properly running devices. If you have to use MAC flapping-based loop
detection to detect whether links operate properly during site deployment,
be sure to disable this function after this stage.

#### Pre-configuration Tasks

Before configuring MAC flapping-based loop detection for a VLAN, complete the following task:

* Complete related VLAN configuration on the edge devices of the VLAN network. For details, see [VLAN Configuration](dc_vrp_vlan_cfg_00000.html) in *NE40E Configuration Guide - LAN Access and MAN Access*.


[Enabling MAC Flapping-based Loop Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0102.html)

After MAC flapping-based loop detection is enabled on devices, the devices can detect loops based on MAC address entry flapping and block interfaces or pseudo wires (PWs) to eliminate the loops.

[(Optional) Configuring Interface Blocking Priorities](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0103.html)

You can configure blocking priorities for interfaces so that a specific interface is preferentially blocked when a loop is detected.

[(Optional) Configuring the Precise Loop Blocking Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0104.html)

Precise loop blocking determines trusted and untrusted interfaces by analyzing the frequency of MAC address entry flapping. When a MAC address entry changes repeatedly, precise blocking can precisely locate and block the untrusted interface with a loop. 

[(Optional) Configuring Traffic Suppression of MAC Flapping-based Loop Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0105.html)

If a loop occurs on a network, the broadcast domain encounters broadcast storms. To prevent other broadcast domains from being affected, traffic suppression of MAC flapping-based loop detection must be enabled.

[Verifying the Configuration of MAC Flapping-based Loop Detection for a VLAN Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0106.html)

After configuring MAC flapping-based loop detection for a virtual local area network (VLAN) network, verify the configuration.