Configuring MAC Flapping-based Loop Detection for a VPLS Network
================================================================

After MAC flapping-based loop detection is configured on a virtual private LAN service (VPLS) network, the devices can detect loops on AC-side interfaces or pseudo wires (PWs), and block interfaces or PWs or report alarms.

#### Usage Scenario

On a VPLS network, PWs are established over Multiprotocol Label Switching (MPLS) tunnels between virtual private network (VPN) sites to transparently transmit Layer 2 packets. When forwarding packets, the provider edges (PEs) learn the source MAC addresses of the packets, create MAC address entries, and establish mapping between the MAC addresses and AC-side interfaces and mapping between the MAC addresses and PWs. Due to redundant links, a PE may receive user packets with the same source MAC address through different interfaces, causing MAC address entry flapping or even damaging MAC address entries. In this situation, you can deploy MAC flapping-based loop detection on each PE and configure a blocking policy for AC-side interfaces to prevent such loops. The blocking policy can be either of the following:

* Blocking interfaces based on their blocking priorities: If a device detects a loop, it blocks the interface with a lower blocking priority.
* Blocking interfaces based on their trusted or untrusted states: If a device detects a loop, it blocks the untrusted interface.

MAC flapping-based loop detection can also detect PW-side loops. The principles of blocking PWs are similar to those of blocking AC-side interfaces.

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

Before configuring MAC flapping-based loop detection on a VPLS network, configure VPLS on the edge devices of the VPLS network. For details, see [VPLS Configuration](dc_vrp_vpls_cfg_5000.html) in *NE40E Configuration Guide - VPN*.



[Enabling MAC Flapping-based Loop Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0004.html)

After MAC flapping-based loop detection is enabled on devices, the devices can detect loops based on MAC address entry flapping and block interfaces or pseudo wires (PWs) to eliminate the loops.

[(Optional) Configuring a Blocking Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0005.html)

After deploying MAC flapping-based loop detection, you can configure a blocking policy for AC-side interfaces or PWs (AC is short for attachment circuit, and PW for pseudo wire).

[(Optional) Configuring Traffic Suppression of MAC Flapping-based Loop Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0010.html)

If a loop occurs on a network, broadcast storms will occur in the broadcast domain. To prevent other broadcast domains from being affected, traffic suppression of MAC flapping-based loop detection must be enabled.

[(Optional) Configure a Device to Globally Block Spoke PWs by Default After Loops Are Detected Based on MAC Flapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0018.html)

Hub PWs on a hierarchical virtual private LAN service (HVPLS) network may be incorrectly configured as spoke PWs. To eliminate loops after they are detected based on MAC flapping, configure a device to globally block spoke PWs by default.

[Verifying the Configuration of MAC Flapping-based Loop Detection for a VPLS Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0006.html)

After configuring MAC flapping-based loop detection for a virtual private LAN service (VPLS) network, verify the configuration.