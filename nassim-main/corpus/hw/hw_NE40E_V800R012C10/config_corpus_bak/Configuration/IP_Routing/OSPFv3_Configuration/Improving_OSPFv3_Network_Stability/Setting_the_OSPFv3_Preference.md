Setting the OSPFv3 Preference
=============================

If multiple dynamic routing protocols run on a device, the device needs to select optimal routes from the routes of these protocols. In this case, you can set a priority for each routing protocol. In this manner, when different protocols discover the routes to the same destination, the route discovered by the protocol with the highest priority is selected.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**preference**](cmdqueryname=preference) [ **ase** ] { *preference* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } \*
   
   
   
   A preference is set for OSPFv3.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.