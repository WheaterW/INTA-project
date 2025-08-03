Setting the convergence priority for OSPF routes
================================================

You can adjust and optimize route selection by setting the convergence priority for OSPF routes.

#### Context

You can set a convergence priority for the OSPF routes matching the specified IP prefix list. The configuration takes effect on the public network only.

OSPF route calculation, link-state advertisement (LSA) flooding, and LSDB synchronization can be implemented according to the configured priority. Therefore, route convergence can be controlled.

When an LSA meets multiple priorities, the highest priority takes effect.

OSPF calculates LSAs in the sequence of intra-area routes, inter-area routes, and AS external routes and calculates the three types of routes separately according to the specified route calculation priorities. Convergence priorities are critical, high, medium, and low. To speed up the processing of LSAs with the higher priority, during LSA flooding, the LSAs need to be placed into the corresponding critical, high, medium, and low queues according to priorities.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip ip-prefix**](cmdqueryname=ip+ip-prefix) *ip-prefix-name* [ **index** *index-number* ] *matchMode* *ipv4-address* *mask-length* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]
   
   
   
   An IP prefix list is configured.
3. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
4. Run [**prefix-priority**](cmdqueryname=prefix-priority) { **critical** | **high** | **medium** } **ip-prefix** *ip-prefix-name*
   
   
   
   The convergence priority for OSPF routes is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.