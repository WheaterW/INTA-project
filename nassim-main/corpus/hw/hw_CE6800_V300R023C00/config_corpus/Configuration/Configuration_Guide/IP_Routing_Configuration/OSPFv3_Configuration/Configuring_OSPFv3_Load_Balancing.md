Configuring OSPFv3 Load Balancing
=================================

Configuring OSPFv3 Load Balancing

#### Prerequisites

Before configuring OSPFv3 load balancing, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

If the destinations and costs of multiple routes discovered by a routing protocol are the same, load balancing can be implemented among these routes.

Perform the following steps on the device that runs OSPFv3.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Set the maximum number of equal-cost routes that can be used for load balancing.
   
   
   ```
   [maximum load-balancing](cmdqueryname=maximum+load-balancing) number
   ```
   
   If the number of equal-cost routes is greater than the number specified in the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* command, valid routes are selected for load balancing based on the following criteria:
   
   1. Next-hop preference: OSPFv3 selects the routes with higher next-hop preferences for load balancing. For details about the configuration of next-hop preferences, see step 4.
   2. Index of the outbound interface corresponding to a next hop: If the next-hop preferences of the candidate routes are the same, OSPFv3 compares the indexes of the outbound interfaces corresponding to the next hops and selects the routes with larger outbound interface indexes for load balancing.
   3. Next-hop IP address: If the candidate routes have the same next-hop preference and outbound interface index, the routes with larger next-hop IP addresses are selected for load balancing.
4. (Optional) Set a weight for the next hop of an equal-cost route.
   
   
   ```
   [nexthop](cmdqueryname=nexthop+weight+%28OSPFv3+view%29) neighbor-id { interface-name | interface-type interface-number } weight value
   ```
   
   You can run the [**nexthop**](cmdqueryname=nexthop+weight+%28OSPFv3+view%29) command to set a weight for the next hop of each OSPFv3 equal-cost route so that OSPFv3 selects routes with higher next-hop preferences for load balancing.
   
   *weight-value* specifies a weight value for the next hop. The smaller the weight value, the higher the preference of the next hop. The default weight value of a next hop is 255.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **routing** command to check information about the OSPFv3 routing table. The command output shows information about equal-cost routes.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **ecmp-group** command to check information about OSPFv3 ECMP groups.