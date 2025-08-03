Configuring RIPng to Import External Routes
===========================================

RIPng can import routing information from other RIPng processes or routing protocols to enrich the RIPng routing table.

#### Context

On a large-scale network, multiple routing protocols may be configured for devices in different areas. In this situation, configure RIPng to import routes from other processes or routing protocols to implement inter-area communication.

If RIPng needs to advertise routing information of other RIPng processes or other routing protocols (such as direct, static, RIPng, OSPFv3, IS-IS, or BGP), you can specify *protocol* to filter routing information. If *protocol* is not specified, routing information to be advertised can be filtered, including the imported routes and local RIPng routes (functioning as direct routes).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ]
   
   
   
   The RIPng process is created and the RIPng view is displayed.
3. (Optional) Run [**default-cost**](cmdqueryname=default-cost) *cost*
   
   
   
   The default cost is set for the imported routes.
   
   If no cost is specified when external routes are imported, the default cost 0 is used.
4. Run [**import-route**](cmdqueryname=import-route) { **static** | **direct** | **bgp** [ **permit-ibgp** ] | **unr** | { **isis** | **ospfv3** | **ripng** } [ *process-id* ] } [ [ **cost** *cost* | **inherit-cost** ] | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }  ] \*
   
   
   
   External routes are imported.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is submitted.