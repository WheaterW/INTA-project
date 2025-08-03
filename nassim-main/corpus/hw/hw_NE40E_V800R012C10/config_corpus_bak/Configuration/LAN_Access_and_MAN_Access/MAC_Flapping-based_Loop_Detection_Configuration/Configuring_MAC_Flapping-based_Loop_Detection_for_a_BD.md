Configuring MAC Flapping-based Loop Detection for a BD
======================================================

After MAC flapping-based loop detection is configured for a bridge domain (BD), the devices can detect loops on AC-side interfaces, and block interfaces or report alarms.

#### Usage Scenario

The user network is dual-homed to the BD network. When forwarding packets, the provider edges (PEs) learn the source MAC addresses of the packets, create MAC address entries, and establish mapping between the MAC addresses and AC-side interfaces. Due to redundant links, a PE may receive user packets with the same source MAC address through different interfaces, causing MAC address entry flapping or even damaging MAC address entries. In this situation, you can deploy MAC flapping-based loop detection on each PE and configure a blocking policy for AC-side interfaces to prevent such loops. The blocking policy can be either of the following:

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

Before configuring MAC flapping-based loop detection for a BD, complete the following task:

* Complete related configuration on the edge devices of the BD network. For details, see [EVC Configuration](dc_vrp_evc_cfg_0000.html) in *NE40E Configuration Guide - LAN Access and MAN Access*.


[Enabling MAC Flapping-based Loop Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0400.html)

After MAC flapping-based loop detection is enabled on devices, the devices can detect loops based on MAC address entry flapping and block interfaces to eliminate the loops.

[(Optional) Configuring a Blocking Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0500.html)

After deploying MAC flapping-based loop detection, you can configure a blocking policy for AC-side interfaces (AC is short for attachment circuit).

[Verifying the Configuration of MAC Flapping-based Loop Detection for a BD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mflp_cfg_0600.html)

After configuring MAC flapping-based loop detection for a BD network, verify the configuration.