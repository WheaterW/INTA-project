Configuring the Route Server Function
=====================================

This section describes how to configure the route server function. The function reduces network resource consumption onASBRs.

#### Usage Scenario

In some scenarios on the live network, to achieve network traffic interworking, EBGP full-mesh connections may be required. However, establishing full-mesh connections among border devices is costly and places high requirements on the performance of the devices, which adversely affects the network topology and device expansion. The route server function is similar to the RR function used in IBGP full-mesh connection scenarios and allows devices to advertise routes to their clients (border devices) without changing route attributes, such as AS\_Path, Nexthop, and MED. This reduces network resource consumption on the border devices.


#### Pre-configuration Tasks

Before configuring the route server function, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+route-server-client) { *ipv4-address* | *group-name* } **route-server-client**
   
   
   
   The route server function is enabled on the device, and an EBGP peer is specified as its client.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to view routes in the BGP routing table.