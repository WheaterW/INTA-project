Configuring RIP to Import External Routes
=========================================

A RIP process can import the routes learned by other processes or routing protocols to enrich routing entries.

#### Context

On a large-scale network, different routing protocols may be configured for devices in different areas. To implement communication between a RIP area and other routing areas, you need to configure the device to import routes from other routing protocols.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. (Optional) Run [**default-cost**](cmdqueryname=default-cost) *cost*
   
   
   
   The default metric is configured for imported routes.
   
   
   
   If no metric is specified for imported external routes, the default metric 0 is used.
4. Import external routes.
   
   
   * To import direct routes, static routes, IS-IS routes, OSPF routes, or routes of another RIP process, run the [**import-route**](cmdqueryname=import-route) { **static** | **direct** | **bgp** | **unr** | { **isis** | **ospf** | **rip** } [ *process-id* ] } [ **cost** *cost* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }  ] \* command.
   * To import IBGP routes, run the [**import-route**](cmdqueryname=import-route) **bgp** **permit-ibgp** [ **cost** *cost* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }  ] \* or [**import-route**](cmdqueryname=import-route) **bgp** [ **permit-ibgp** ] { **cost** **transparent** { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }  | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }  **cost** **transparent** | **cost** **transparent** } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Importing routes from other protocols into a RIP process may lead to routing loops. Therefore, exercise caution when running the [**import-route**](cmdqueryname=import-route) command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.