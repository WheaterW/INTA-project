Configuring Equal-Cost Routes
=============================

You can set the maximum number of OSPF equal-cost routes and weights to implement load balancing and adjust route selection.

#### Context

Routes that are discovered by the same routing protocol and have the same destination and cost are equal-cost routes.

On the network shown in [Figure 1](#EN-US_TASK_0172365562__fig_dc_vrp_ospf_cfg_003901), three paths are available between DeviceA and DeviceB, and they all run OSPF and have the same cost. In this case, the three corresponding routes are equal-cost routes.

**Figure 1** Network diagram of equal-cost routes  
![](images/fig_dc_vrp_ospf_cfg_003901.png)
When there are multiple redundant links on an OSPF network, multiple equal-cost routes may exist. In this case, you can use either of the following methods:

* Configure load balancing so that traffic is evenly balanced among these links.
  
  This method improves link utilization and reduces the possibility of congestion caused by link overload. However, load balancing randomly forwards traffic, which may affect service traffic management.
* Configure weights for equal-cost routes so that the routes with higher priorities are preferentially selected, with others functioning as backups.
  
  In this mode, you can allow one or more routes to be preferentially selected without modifying the original configuration. This ensures network reliability and facilitates service traffic management.


#### Procedure

* Configure OSPF route load balancing.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF view is displayed.
  3. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number*
     
     
     
     The maximum number of equal-cost routes is set.
     
     
     
     If the number of equal-cost routes is greater than the number specified in the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* command, valid routes are selected for load balancing based on the following criteria:
     
     1. Route weight: Routes with smaller weight values (higher priority) are selected for load balancing.
     2. Interface index: If routes have the same weight, those with greater interface index values are selected for load balancing.
     3. Next hop IP address: If routes have the same weight and interface index, those with higher next hop IP addresses are selected for load balancing.
  4. (Optional) Run [**ecmp prefer**](cmdqueryname=ecmp+prefer) [ **te-tunnel** | **intact** ]
     
     
     
     A preference between the routes with a TE tunnel interface as the outbound interface and IP routes is set for OSPF load balancing.
     
     
     
     If both IGP-Shortcut-enabled TE tunnels and IP links are available, you can perform this step to set a preference between the routes with a TE tunnel interface as the outbound interface and IP routes for load balancing.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a weight for an OSPF equal-cost route with a specified next hop.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF view is displayed.
  3. Run [**nexthop**](cmdqueryname=nexthop) *ip-address* **weight** *value*
     
     
     
     A weight is set for an equal-cost route with a specified next hop.
     
     
     
     Among equal-cost OSPF routes, those with higher priorities (smaller weight values set using the [**nexthop**](cmdqueryname=nexthop) command) are selected for load balancing.