Configuring BGP Recursion Suppression in Case of Next Hop Flapping
==================================================================

Configuring BGP Recursion Suppression in Case of Next Hop Flapping

#### Prerequisites

Before configuring BGP recursion suppression in case of next hop flapping, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

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
4. Enable recursion suppression in case of next hop flapping.
   
   
   ```
   [undo nexthop recursive-lookup restrain disable](cmdqueryname=undo+nexthop+recursive-lookup+restrain+disable)
   ```
   
   If you are not concerned about the system becoming occupied processing route selection and advertisement and the possible high CPU usage, run the [**nexthop recursive-lookup restrain disable**](cmdqueryname=nexthop+recursive-lookup+restrain+disable) command to disable recursion suppression in case of next hop flapping.
5. Return to the BGP view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Set the intervals for increasing, retaining, and clearing the penalty value required for recursion suppression in case of next hop flapping.
   
   
   ```
   [nexthop recursive-lookup restrain](cmdqueryname=nexthop+recursive-lookup+restrain+suppress-interval) suppress-interval add-count-time hold-interval hold-count-time clear-interval clear-count-time
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to check information about BGP public network routes.