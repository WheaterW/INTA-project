Configuring Basic VRRP6 Functions
=================================

VRRP6 works in either master/backup or load balancing mode, implementing device backup and efficient and stable data forwarding.

#### Usage Scenario

A VRRP6 group consists of two or more devices and functions as an egress gateway for hosts. If a device fails, another device takes over. VRRP6 ensures continuous and reliable network communication.


#### Pre-configuration Tasks

Before configuring basic VRRP6 functions, configure network layer attributes for interfaces to ensure network connectivity.


[Creating a VRRP6 Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0104.html)

You can create a VRRP6 group and set VRRP6 priorities to determine the master and backup Routers. The master Router transmits service traffic. You can create multiple VRRP6 groups to load-balance service traffic.

[(Optional) Configuring VRRP6 Stability Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0105.html)

To help a VRRP6 group work stably, enable the preemption function, set a preemption delay, and configure an interval for sending VRRP6 Advertisement packets. The configuration can minimize the impact of network flapping resulting from frequent master/backup VRRP6 switchovers on data forwarding.

[(Optional) Optimizing a VRRP6 Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0106.html)

To optimize a VRRP6 group, enable the ping to a virtual IPv6 address, set the interval at which the master device in the VRRP6 group sends NA packets, and disable a device from checking the hop count in VRRP6 Advertisement packets.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0107.html)

After configuring basic functions for a VRRP6 group, you can check information about the VRRP6 group.