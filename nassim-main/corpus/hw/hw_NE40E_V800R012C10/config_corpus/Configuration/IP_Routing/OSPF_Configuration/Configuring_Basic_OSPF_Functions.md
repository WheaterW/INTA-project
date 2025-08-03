Configuring Basic OSPF Functions
================================

Before constructing OSPF networks, you need to configure basic OSPF functions.

#### Usage Scenario

When OSPF is configured on multiple Routers in the same area, most configuration data, such as the timer, filter, and aggregation, must be planned uniformly in the area. Incorrect configurations may cause neighboring Routers to fail to send messages to each other or even causing routing information congestion and self-loops.

The OSPF-relevant commands that are configured in the interface view take effect regardless of whether OSPF is enabled. After OSPF is disabled, the OSPF-relevant commands also exist on interfaces.


#### Pre-configuration Tasks

Before configuring basic OSPF functions, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.


[Enabling OSPF](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2021.html)

After an OSPF process is created, a router ID is configured for the Router, an interface on which OSPF runs and the area to which the interface belongs are specified, routes can be discovered and calculated in the AS.

[(Optional) Configuring an Interface to Fill in DD Packets with Its Own MTU](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2026.html)

You can configure an interface to fill in the Interface MTU field of a DD packet with the interface MTU.

[(Optional) Creating OSPF Virtual Links](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2053.html)

This section describes how to create logical links between backbone areas and to ensure the OSPF network connectivity.

[(Optional) Configuring the Router to Comply with Route Selection Rules Defined in a Standard Protocol](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2022.html)

You can configure the Router to comply with the route selection rule defined in RFC 1583 or RFC 2328.

[(Optional) Setting the OSPF Preference](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2023.html)

When multiple routing protocols discover routes to the same destination address, you can set the OSPF preference to control the route selection result.

[(Optional) Restricting the Flooding of OSPF Update LSAs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2032.html)

To maintain stable OSPF neighbor relationships, you can restrict the flooding of update LSAs on a local device, so that its neighbors will not discard Hello packets due to a great number of update LSAs.

[(Optional) Configuring an Alarm Threshold for the Number of LSAs Learned by OSPF](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_3001.html)

You can configure an alarm threshold for the number of LSAs learned by OSPF so that an alarm is reported when this threshold is reached or exceeded.

[(Optional) Configuring the Maximum Number of Packet Retransmission Attempts](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2024.html)

When no response to DD packets, LSU packets, or LSR packets is received, the retransmission mechanism is used and the maximum number of packet retransmission attempts is set to prevent dead loops caused by repeated transmissions.

[(Optional) Setting the Interval at Which LSAs Are Retransmitted Between Adjacent Routers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2025.html)

You can set an appropriate interval at which LSAs are retransmitted based on network conditions in order to accelerate convergence.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0007.html)

After configuring basic OSPF functions, verify information about OSPF neighbors, interfaces, and routes.