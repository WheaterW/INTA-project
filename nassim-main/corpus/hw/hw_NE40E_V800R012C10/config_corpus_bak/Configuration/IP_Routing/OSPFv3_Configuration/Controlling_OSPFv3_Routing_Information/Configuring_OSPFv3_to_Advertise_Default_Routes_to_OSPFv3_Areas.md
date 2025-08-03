Configuring OSPFv3 to Advertise Default Routes to OSPFv3 Areas
==============================================================

You can configure OSPFv3 to advertise default routes to OSPFv3 areas. Only the routes that meet the conditions can be converted into LSAs and advertised.

#### Context

Perform the following steps on the Router that runs OSPFv3:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**default-route-advertise**](cmdqueryname=default-route-advertise) [ [ **always** | **permit-calculate-other** ] | **cost** *cost* | **type** *type* | **tag** *tag* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } ] \* or [**default-route-advertise**](cmdqueryname=default-route-advertise) [ **permit-calculate-other** | **cost** *cost* | **type** *type* | **tag** *tag* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } | **permit-preference-less-than** *preference-value* ] \*
   
   
   
   The device is configured to advertise default routes to OSPFv3 routing areas.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent low-priority active default routes from being imported, which would otherwise cause routing loops, you are advised to specify the **permit-preference-less-than** parameter. This parameter is used only when **always** is not specified.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.