Configuring MED-related Functions
=================================

Configuring MED-related Functions

#### Prerequisites

Before configuring MED-related functions, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

Similar to the cost (or metric) used by an IGP, the MED is used to determine the optimal route when traffic enters an AS. When a BGP device learns multiple routes with the same destination address but different next hops from different EBGP peers, the route with the smallest MED value is selected as the optimal route if all other attributes are the same.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure MED-related functions. For details, see [Table 1](#EN-US_TASK_0000001130624132__table29861143141218).
   
   
   
   **Table 1** Configuring MED-related functions
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set the default MED value. | [**default med**](cmdqueryname=default+med) *med* | The [**default med**](cmdqueryname=default+med) command takes effect only for routes imported using the [**import-route**](cmdqueryname=import-route) command and BGP summary routes on the local device. |
   | Configure BGP to compare the MED values of routes from different ASs. | [**compare-different-as-med**](cmdqueryname=compare-different-as-med) | By default, a BGP device compares the MED values of only routes from different peers in the same AS. This command allows BGP to compare the MED values of routes received from different ASs. |
   | Enable the deterministic-MED function. | [**deterministic-med**](cmdqueryname=deterministic-med) | If the deterministic-MED function is not enabled and the device receives multiple routes with the same prefix from different ASs, the sequence in which routes are received determines the route selection result. After the deterministic-MED function is enabled, these routes are first grouped based on the leftmost AS number in the AS\_Path attribute. Routes with the same leftmost AS number are grouped together and compared, and an optimal route is selected in the group. This optimal route is then compared with optimal routes from other groups to determine the ultimate optimal route. With the deterministic-MED function, the route selection result is independent of the sequence in which routes are received. |
   | Configure BGP4+ to set the MED to the maximum value if a route carries no MED. | [**bestroute med-none-as-maximum**](cmdqueryname=bestroute+med-none-as-maximum) | If this command is run, BGP uses the maximum MED value during route selection for a route that carries no MED; otherwise, BGP uses 0 as the MED value for the route. |
   | Configure BGP to compare the MED values of routes in a confederation. | [**bestroute med-confederation**](cmdqueryname=bestroute+med-confederation) | By default, BGP compares the MED values of only routes from the same AS. |
   | Configure BGP to compare the sums of MED values multiplied by a MED multiplier and IGP metrics multiplied by an IGP metric multiplier for different routes. | [**bestroute med-plus-igp**](cmdqueryname=bestroute+med-plus-igp+igp-multiplier+med-multiplier) [ **igp-multiplier** *igp-multiplier* | **med-multiplier** *med-multiplier* ]\* | After this command is run, the device compares the sums of MED values multiplied by a MED multiplier and IGP metrics multiplied by an IGP metric multiplier during route selection. |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```