Configuring IPv6 Multicast Load Splitting
=========================================

IPv6 multicast load splitting is applicable to the scenario where multiple equal-cost IPv6 unicast routes of the same type exist. If multiple equal-cost routes exist on a network, IPv6 multicast load splitting can be performed for multicast traffic based on different policies. This optimizes network traffic transmission in the case of multiple IPv6 multicast data flows.

#### Context

IPv6 multicast routing is based on the Reverse Path Forwarding (RPF) check. Based on RPF check results, the Router selects only one route for forwarding IPv6 multicast data. In the case of heavy IPv6 multicast traffic, network congestion may occur, which will affect IPv6 multicast services.

IPv6 multicast load splitting extends multicast route selection rules. It solves the problem that the multicast route selection completely depends on the RPF check. After multicast load splitting is configured on a network with multiple equal-cost and optimal routes, devices may select all the equal-cost routes for forwarding IPv6 multicast data.


#### Pre-configuration Tasks

Before configuring IPv6 multicast load splitting, complete the following tasks:

* Configure an IPv6 unicast routing protocol to ensure that IPv6 unicast routes are reachable.
* Configure basic IPv6 multicast functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast ipv6 load-splitting**](cmdqueryname=multicast+ipv6+load-splitting) { **stable-preferred** | **source** | **group** | **source-group** | **balance-ucmp** }
   
   
   
   IPv6 multicast load splitting is configured.
   
   
   
   * **stable-preferred**: indicates stable-preferred load splitting. This policy applies to the scenario where IPv6 multicast services are stable.
     
     When equal-cost routes are added or deleted, the Router automatically balances the load; however, when IPv6 multicast routing entries are deleted, the Router does not automatically adjust the load.
   * **group**: indicates group address-based load splitting. This policy applies to the scenario of one source to multiple groups.
   * **source**: indicates source address-based load splitting. This policy applies to the scenario of one group to multiple sources.
   * **source-group**: indicates source and group addresses-based load splitting. This policy applies to the scenario of multiple sources to multiple groups.
   * **balance-ucmp**: Indicates link bandwidth-based load splitting. This policy is applicable to the scenario in which links have different bandwidth values.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.