Configuring MBGP Route Dampening
================================

Configuring MBGP route dampening suppresses unstable MBGP routes.

#### Usage Scenario

MBGP route dampening is designed to suppress unstable routes. After MBGP route dampening is configured, an MBGP device does not add any unstable routes to its MBGP routing table or advertise them to its MBGP peers.

A primary cause of route instability is route flapping. A route is considered to be flapping when it repeatedly appears and then disappears in the routing table. MBGP is applied to complex networks where routes change frequently. Frequent route flapping consumes bandwidth and CPU resources and even seriously affects network operations. To prevent the impact of frequent route flapping, MBGP uses route dampening to suppress unstable routes.

Specified-requirement route dampening is a type of route dampening that is used to differentiate routes based on routing policies. This allows MBGP to use different route dampening parameters to suppress unstable routes. Different route dampening parameters can also be configured for different nodes in the same route-policy. When route flapping occurs, MBGP can use specific route dampening parameters to suppress the routes that match the route-policy. For example, on a network, a long dampening period of time can be set for routes with a long mask, and a short dampening period of time is set for routes with a short mask (such as an 8-bit mask).


#### Pre-configuration Tasks

Before configuring MBGP route dampening, [configure an MBGP peer](dc_vrp_multicast_cfg_1003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run [**dampening**](cmdqueryname=dampening) [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* ] \* [ **update-standard** ]
   
   
   
   MBGP route dampening parameters are set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**dampening**](cmdqueryname=dampening) command is valid only for EBGP routes.
   
   The value of *suppress* must be greater than that of *reuse* and smaller than that of *ceiling*.
   
   If routes are differentiated based on policies and the [**dampening**](cmdqueryname=dampening) command is run to reference a route-policy, MBGP allows you to use different route dampening parameters to suppress different routes.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After the configuration is complete, verify the configuration.

* Run the [**display bgp multicast routing-table dampened**](cmdqueryname=display+bgp+multicast+routing-table+dampened) command to check dampened MBGP routes.
* Run the [**display bgp multicast routing-table dampening parameter**](cmdqueryname=display+bgp+multicast+routing-table+dampening+parameter) command to check configured MBGP route dampening parameters.
* Run the [**display bgp multicast routing-table flap-info**](cmdqueryname=display+bgp+multicast+routing-table+flap-info) [ *ip-address* [ *mask* [ **longer-match** ] | *mask-length* [ **longer-match** ] ] | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | **regular-expression** *as-regular-expression* ] command to check MBGP route flapping statistics.