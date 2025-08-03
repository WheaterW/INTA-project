Configuring RIP to Import External Routes
=========================================

Routing Information Protocol (RIP) can import routes from other processes or other routing protocols to enrich the RIP routing table.

#### Context

On a large-scale network, different routing protocols may be configured. In this situation, configure RIP to import routes from other processes or other routing protocols.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. (Optional) Run [**default-cost**](cmdqueryname=default-cost) *cost*
   
   
   
   The default cost is set for imported routes.
   
   
   
   If no cost is specified for imported external routes, the default cost 0 takes effect.
4. Run [**import-route**](cmdqueryname=import-route)
   
   
   
   External routes are imported.
   
   
   
   * To import direct routes, static routes, IS-IS routes, OSPF routes, or routes of other RIP processes, run the [**import-route**](cmdqueryname=import-route) { [**direct**](cmdqueryname=direct) | **static** |{ **isis** | **ospf** | **rip** } [ *process-id* ] } [ **cost** *cost* | **route-policy** *route-policy-name* ] \* command.
   * To import IBGP routes, run the [**import-route**](cmdqueryname=import-route) [**bgp**](cmdqueryname=bgp) **permit-ibgp** [ **cost** { *cost* | **transparent** } | **route-policy** *route-policy-name* ] \* \* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Importing routes from other protocols to a RIP process may lead to routing loops. Therefore, exercise caution when running the [**import-route**](cmdqueryname=import-route) command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.