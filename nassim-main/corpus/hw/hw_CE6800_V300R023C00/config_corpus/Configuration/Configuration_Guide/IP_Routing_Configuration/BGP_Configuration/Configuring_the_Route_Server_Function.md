Configuring the Route Server Function
=====================================

This section describes how to configure the route server function. The function reduces network resource consumption on border routers.

#### Prerequisites

Before configuring the BGP route server function, complete the following tasks:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

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
3. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Enable the route server function for a specified EBGP peer.
   
   
   ```
   [peer](cmdqueryname=peer+route-server-client) { ipv4-address | group-name } route-server-client
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify it:

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to check information about routes in the BGP routing table.