Configuring an Equal-Cost IS-IS Route Processing Mode
=====================================================

Configuring an Equal-Cost IS-IS Route Processing Mode

#### Context

If redundant links exist on an IS-IS network, multiple equal-cost routes may exist. In this case, you can configure either of the following processing modes for the equal-cost routes:

* Load balancing: allows traffic to be evenly distributed to each link. This mode improves link utilization and reduces the congestion caused by overloaded links. However, traffic is randomly forwarded in this mode, complicating traffic management.
* Configure weights for equal-cost routes so that the route with the highest priority is preferentially selected, with others functioning as backups. This mode facilitates traffic management and improves network reliability, without the need to modify existing configurations.


#### Procedure

* Configure IS-IS route load balancing.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure the maximum number of equal-cost routes for load balancing.
     
     
     ```
     [maximum load-balancing](cmdqueryname=maximum+load-balancing) number
     ```
     
     By default, load balancing is supported, and a maximum of 64 equal-cost routes can participate in load balancing.
     
     When the number of equal-cost routes is greater than the number specified in the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) command, valid routes are selected for load balancing based on the following criteria:
     1. Route weight: Routes with small weight values (high priority) are selected for load balancing.
     2. Next-hop system ID: If routes have the same weight, those with small system IDs are selected for load balancing.
     3. Outbound interface index: If routes have the same weight and system ID, those with small outbound interface indexes are selected for load balancing.
     4. Next-hop IP address: If the weights, next-hop system IDs, and interface indexes of the routes are the same, their next-hop IP addresses are compared. The routes with high IP addresses are selected for load balancing.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure weights for equal-cost IS-IS routes.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Set a weight for an equal-cost route with a specified next hop.
     
     
     ```
     [nexthop](cmdqueryname=nexthop) ip-address weight value
     ```
     
     
     
     By default, no weight is set for equal-cost IS-IS routes. The smaller the *value*, the higher the priority.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* command to check IPv4 IS-IS routing information.

* Run the **display isis lsdb** [ **verbose** | { **level-1** | **level-2** } | { **local** | *lspid* | **is-name** *isname* } ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.