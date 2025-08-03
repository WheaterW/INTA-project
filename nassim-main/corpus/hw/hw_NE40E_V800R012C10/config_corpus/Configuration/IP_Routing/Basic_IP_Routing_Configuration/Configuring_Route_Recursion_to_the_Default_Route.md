Configuring Route Recursion to the Default Route
================================================

When the next hop of a route is not directly reachable, you can configure route recursion to the default route.

#### Usage Scenario

The next hops of routes may not be directly reachable. In this case, recursion is required so that such routes can be used for traffic forwarding. To allow routes to recurse to the default route, run the [**{ ip | ipv6 } route recursive-lookup default-route**](cmdqueryname=%7B+ip+%7C+ipv6+%7D+route+recursive-lookup+default-route) command.


#### Pre-configuration Tasks

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip route recursive-lookup default-route protocol**](cmdqueryname=ip+route+recursive-lookup+default-route+protocol) { **static** | **msr** } or [**ipv6 route recursive-lookup default-route protocol**](cmdqueryname=ipv6+route+recursive-lookup+default-route+protocol) { **static** | **msr** } 
   
   
   
   Route recursion to the default route is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display current-configuration**](cmdqueryname=display+current-configuration) command in the system view to verify it. The command output shows that route recursion to the default route is configured.