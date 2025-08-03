Configuring the Route Server Function
=====================================

This section describes how to configure the route server function. The function reduces network resource consumption on border routers.

#### Usage Scenario

In some scenarios on the live network, EBGP full-mesh connections are required to implement network traffic interworking. Full-mesh connections between border devices have high requirements on cost and device performance, and are not conducive to the expansion of the network topology and the number of devices. The route server function is similar to the RR function used in IBGP full-mesh connection scenarios. It allows one or more routing devices to advertise routes to their clients (border devices) without changing path attributes, such as AS\_Path, Nexthop, and MED, reducing the consumption of full-mesh connections on each border router.


#### Pre-configuration Tasks

Before configuring the route server function, complete the following tasks:

* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
3. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **unicast** command to enter the IPv6 unicast address family view.
4. Run the [**peer**](cmdqueryname=peer+route-server-client) { *ipv6-address* | *group-name* } **route-server-client** command to enable the route server function for a specified EBGP peer.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command to view routes in the BGP4+ routing table.