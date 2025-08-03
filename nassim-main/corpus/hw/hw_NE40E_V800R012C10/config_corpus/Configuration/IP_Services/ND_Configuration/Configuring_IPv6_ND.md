Configuring IPv6 ND
===================

IPv6 neighbor discovery (ND) is a group of messages and processes that identify relationships between neighboring nodes. IPv6 ND provides similar functions as the Address Resolution Protocol (ARP) and ICMP router discovery in IPv4, as well as the additional neighbor reachability detection function.

#### Pre-configuration Tasks

Before configuring IPv6 ND, complete the following tasks:

* Connect interfaces and configure physical parameters for them to ensure that their physical status is up.
* Configure link layer protocol parameters for interfaces.
* Enable IPv6 in the interface view.
* Configure IPv6 addresses for interfaces.


[Configuring Static ND Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0009.html)

You can obtain the mappings between IPv6 and MAC addresses of neighbors after configuring static ND entries. ND entries indicate the mappings between IPv6 and MAC addresses. If a device is not enabled to send ND messages, it cannot obtain ND entries. To enable such a device to obtain ND entries, configure static ND on the device.

[(Optional) Configuring an Aging Time for ND Entries in the Stale State](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0010.html)

You can configure a shorter aging time for ND entries in the Stale state to speed up their aging.

[(Optional) Configuring an Aging Time for ND Entries in the Incomplete State](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0071.html)

Configuring a short aging time for ND entries in the Incomplete state can speed up their aging.

[(Optional) Configuring a Neighbor Reachability Detection Interval](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0011.html)

A device can send NS messages to detect whether its neighbors are reachable. Therefore, you can set the NS message transmission interval to control the neighbor reachability detection frequency. Frequent NS message transmissions help rapidly determine whether neighbors are reachable, but also affect system performance. Therefore, it is recommended that the interval not be set too short.

[(Optional) Configuring the Maximum Number of Dynamic ND Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0037.html)

Configuring the maximum number of dynamic ND entries protects against RA flood attacks.

[(Optional) Configuring Strict Prefix Learning for Dynamic ND Entries](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0002.html)

You can configure strict prefix learning for dynamic ND entries to determine whether an interface learns valid NS messages carrying different network prefixes.

[(Optional) Configuring Probe Parameters for ND Entries in the PROBE State](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0042.html)

This section describes how to configure probe parameters for ND entries in the PROBE state to enhance probe reliability.

[(Optional) Configuring Generation of ND Entries Upon Receipt of NA Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0001.html)

The generation of ND entries upon receipt of NA messages enhances network reliability.

[(Optional) Configuring an Interval for Recording ND Logs and Sending ND Traps](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0044.html)

Through logs and traps for potential attacks, administrators can obtain ND running in real time, taking measures on the attacks.

[(Optional) Configuring Dual-Device ND Hot Backup](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0020.html)

Dual-device ND hot backup can be enabled to achieve backup of ND entries between devices. This allows fast service switching in case of a network node or link failure, enhancing service reliability.

[(Optional) Configuring Attack Detection for ND Messages with a Fixed Source MAC Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0039.html)



[(Optional) Configuring MAC Address Check for ND](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0040.html)



[(Optional) Configuring ND Fast Reply](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0041.html)



[(Optional) Disabling ND-MAC Association](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0026.html)

By default, the device supports ND-MAC association, which implements fast ND entry updating and ensures real-time and stable user traffic. However, after learning ND entries, a VLANIF interface synchronizes them on the device. As a result, a large number of ND entries exist on all interface boards. To resolve this issue, disable ND-MAC association in scenarios where ND entry synchronization is not required on the device.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0012.html)

After configuring IPv6 neighbor discovery, verify the configuration.