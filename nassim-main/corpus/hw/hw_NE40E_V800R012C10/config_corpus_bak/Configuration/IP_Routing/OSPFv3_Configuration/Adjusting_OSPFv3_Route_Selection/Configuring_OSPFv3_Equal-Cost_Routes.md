Configuring OSPFv3 Equal-Cost Routes
====================================

Routes that are discovered by the same routing protocol and have the same destination and cost can implement load balancing.

#### Context

Perform the following steps on the device that runs OSPFv3.


#### Procedure

* Configure OSPFv3 route load balancing.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     
     
     The OSPFv3 view is displayed.
  3. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number*
     
     
     
     The maximum number of equal-cost routes is set.
     
     
     
     If the number of equal-cost routes is greater than the number specified in the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* command, valid routes are selected for load balancing based on the following criteria:
     
     1. Route weight: Routes with smaller weight values (higher priority) are selected for load balancing.
     2. Interface index: If routes have the same weight, those with greater interface index values are selected for load balancing.
     3. Next hop IP address: If routes have the same weight and interface index, those with higher next hop IP addresses are selected for load balancing.
* Set a weight for an OSPFv3 equal-cost route with a specified next hop.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     
     
     The OSPFv3 view is displayed.
  3. Run [**nexthop**](cmdqueryname=nexthop)*neighbor-id* { *interface-name* | *interfaceType* *i**nterfaceNum* } **weight***value*
     
     
     
     A weight is configured for the OSPFv3 equal-cost route with a specified next hop.
     
     
     
     After OSPFv3 calculates equal-cost routes, it selects some of them for load balancing based on their weight values. A smaller weight value indicates a higher priority.