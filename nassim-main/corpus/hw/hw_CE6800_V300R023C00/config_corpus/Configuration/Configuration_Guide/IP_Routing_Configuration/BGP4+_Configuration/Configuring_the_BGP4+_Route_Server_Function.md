Configuring the BGP4+ Route Server Function
===========================================

This section describes how to configure the route server function. The function reduces network resource consumption on border routers.

#### Prerequisites

Before configuring the BGP4+ route server function, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

In some scenarios on the live network, EBGP full-mesh connections are required to implement network traffic interworking. Full-mesh connections between border devices have high requirements on costs and device performance and are not conducive to the expansion of the network topology and the number of devices. The route server function is similar to the RR function used in IBGP full-mesh connection scenarios. It allows one or more routing devices to advertise routes to their clients (border devices) without changing route attributes, such as AS\_Path, Nexthop, and MED, reducing the consumption of full-mesh connections on the border router.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the BGP-IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Enable the route server function for a specified EBGP peer.
   
   
   ```
   [peer](cmdqueryname=peer+route-server-client) { ipv6-address | group-name } route-server-client
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, verify it.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command to check information about routes in the BGP4+ routing table.