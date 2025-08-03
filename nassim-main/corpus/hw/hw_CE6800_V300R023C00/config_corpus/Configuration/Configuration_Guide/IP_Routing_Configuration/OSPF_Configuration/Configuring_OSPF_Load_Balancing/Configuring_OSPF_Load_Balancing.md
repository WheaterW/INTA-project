Configuring OSPF Load Balancing
===============================

Configuring OSPF Load Balancing

#### Prerequisites

Before configuring OSPF load balancing, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### OSPF Load Balancing Conditions

When the number of OSPF routes allowed to participate in load balancing and the number of routes on the device that are allowed to participate in load balancing are both greater than 1 and multiple OSPF routes with the same prefix exist on the device, these OSPF routes work in load balancing mode if the following conditions are met:

* The OSPF route types (intra-area, inter-area, Type 1 external, or Type 2 external) are the same.
* The direct next hops are different.
* The costs are the same.
* In the case of Type 2 external routes, the costs of the paths to the ASBR/forwarding address must be the same.
* If OSPF selects routes according to the rules defined in related standards, the area IDs must be the same.

#### Context

You can set the maximum number of OSPF equal-cost routes and preferences to implement load balancing and adjust route selection. If the destinations and costs of the multiple routes discovered by a routing protocol are the same, load balancing can be implemented among the routes.

On the network shown in [Figure 1](#EN-US_TASK_0000001130783236__fig_dc_vrp_ospf_cfg_003901), three routes between DeviceA and DeviceB that run OSPF have the same cost. The three routes are equal-cost routes and are used for load balancing.

**Figure 1** Network diagram of equal-cost routes  
![](figure/en-us_image_0000001130623526.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Set the maximum number of equal-cost routes that can be used for load balancing.
   
   
   ```
   [maximum load-balancing](cmdqueryname=maximum+load-balancing) number
   ```
   
   If the number of equal-cost routes is greater than the number specified in the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* command, valid routes are selected for load balancing based on the following criteria:
   
   1. Next-hop weight: OSPF selects the routes with higher next-hop priorities (smaller weights) for load balancing. For details about the configuration, see Step 4.
   2. Index of the outbound interface corresponding to a next hop: If the next-hop weights of the candidate routes are the same, OSPF compares the indexes of the outbound interfaces corresponding to the next hops and selects the routes with larger outbound interface indexes for load balancing.
   3. Next-hop IP address: If the candidate routes have the same next-hop weight and outbound interface index, OSPF selects the routes with larger next-hop IP addresses for load balancing.
4. (Optional) Set a weight for the next hop of an equal-cost route.
   
   
   ```
   [nexthop](cmdqueryname=nexthop) ip-address weight value
   ```
   
   You can run the [**nexthop**](cmdqueryname=nexthop+weight+%28OSPFv3+view%29) command to set a weight for the next hop of each OSPF equal-cost route so that OSPF selects the routes with higher next-hop priorities for load balancing.
   
   * *ip-address* specifies the next-hop IP address of an equal-cost route.
   * *value* specifies a weight value for the next hop. The smaller the weight value, the higher the priority. The default weight value is 255.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check information about the OSPF routing table. The command output shows information about equal-cost routes.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **ecmp-group** command to check information about OSPF ECMP groups.