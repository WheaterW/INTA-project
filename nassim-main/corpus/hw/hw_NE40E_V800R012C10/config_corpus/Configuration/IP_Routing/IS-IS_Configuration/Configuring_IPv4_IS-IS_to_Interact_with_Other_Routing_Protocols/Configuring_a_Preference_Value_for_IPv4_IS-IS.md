Configuring a Preference Value for IPv4 IS-IS
=============================================

If multiple routes to the same destination are discovered by different routing protocols, configure the highest priority value for IS-IS so that a route discovered by IS-IS can be selected preferentially.

#### Context

If multiple routes to the same destination are discovered by different routing protocols running on the same device, the route discovered by the protocol with the highest priority is selected.

For example, if both OSPF and IS-IS are configured on a network, the route discovered by OSPF is used because OSPF has a higher priority than IS-IS by default.

You can set a preference value for IS-IS to increase the priority of IS-IS routes so that they are preferentially selected. In addition, you can configure a route-policy to increase the priority of specified IS-IS routes, without affecting route selection.


#### Procedure

* Configure a preference value for IS-IS.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**preference**](cmdqueryname=preference) *preference*
     
     
     
     The IS-IS priority value is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A smaller *preference* value indicates a higher preference.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a preference value for specified IS-IS routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**preference**](cmdqueryname=preference) { { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } | *preference* } \*
     
     
     
     A preference value is configured for the matched IS-IS routes.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     *preference* takes effect only on the matched IS-IS routes.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.