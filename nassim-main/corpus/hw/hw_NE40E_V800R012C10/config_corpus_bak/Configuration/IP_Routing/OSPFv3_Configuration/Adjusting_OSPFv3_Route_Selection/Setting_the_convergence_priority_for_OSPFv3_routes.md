Setting the convergence priority for OSPFv3 routes
==================================================

You can adjust and optimize route selection by setting the convergence priority for OSPFv3 routes.

#### Context

You can set a convergence priority for the OSPFv3 routes matching the specified IPv6 prefix list. The configuration takes effect on the public network only.

OSPFv3 route calculation, LSA flooding, and LSDB synchronization can be implemented according to the configured priority. Therefore, route convergence can be controlled.

When an LSA meets multiple priorities, the highest priority takes effect.

OSPFv3 calculates LSAs in the sequence of intra-area routes, inter-area routes, and AS external routes. This command enables OSPFv3 to calculate the three types of routes separately according to the specified route calculation priorities. The convergence priority sequence is as follows: critical > high > medium > low. To speed up the processing of LSAs with the higher priority, during LSA flooding, the LSAs need to be placed into the corresponding critical, high, medium, and low queues according to priorities.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip ipv6-prefix**](cmdqueryname=ip+ipv6-prefix)*ipv6-prefix-name* [ **index***index-number* ] *matchMode* *ipv6-address* *masklen* [ **match-network** ] [ **greater-equal***greater-equal-value* ] [ **less-equal***less-equal-value* ]
   
   
   
   An IPv6 prefix list is configured.
3. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
4. Run [**prefix-priority**](cmdqueryname=prefix-priority) { **critical** | **high** | **medium** | **very-low** } **ipv6-prefix** *ipv6-prefix-name*
   
   
   
   The convergence priority for OSPFv3 routes is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.