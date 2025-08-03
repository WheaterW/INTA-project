Configuring IS-IS to Import External Routes
===========================================

By configuring IS-IS to import routes, you can enable IS-IS
to learn routing information of other protocols or other IS-IS processes.

#### Context

IS-IS regards the routes discovered by other routing protocols
or other IS-IS processes as external routes. You can specify default
costs for imported routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Configure IS-IS to import external routes.
   
   
   
   Before setting costs for the imported routes, run the [**import-route**](cmdqueryname=import-route) { **direct** | **static** | { **ospf** | **rip** | **isis** } [ *process-id* ] | **bgp** [ **permit-ibgp** ] } [ **cost-type** { **external** | **internal** } | **cost** *cost* | **tag** *tag* | **route-policy** *route-policy* | [ **level-1** | **level-2** | **level-1-2** ] ] \* command
   to import external routes.
   
   Before retaining the original costs
   of the imported routes, run the [**import-route**](cmdqueryname=import-route) { { **ospf** | **rip** | **isis** } [ *process-id* ] | **bgp** [ **permit-ibgp** ] | **direct** } **inherit-cost** [ { **level-1** | **level-2** | **level-1-2** } | **tag** *tag* | **route-policy** *route-policy* ] \* command to import external routes.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   **permit-ibgp** takes effect only in the public network instance.
   
   When the
   cost type of IS-IS is narrow, the parameters **cost-type** { **external** | **internal** } will determine the cost of imported routes.
   * If you configure **external**, the cost
     of imported routes equals the original route cost plus 64.
   * If you configure **internal**, the cost
     of imported routes is the same as the original route cost.
   
   To better manage and maintain IS-IS networks,
   configure **route-policy** *route-policy* to import only required routes.
   
   If you do not specify **level-1**, **level-2**, or **level-1-2** in the command, routes are imported to the
   Level-2 routing table by default.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.