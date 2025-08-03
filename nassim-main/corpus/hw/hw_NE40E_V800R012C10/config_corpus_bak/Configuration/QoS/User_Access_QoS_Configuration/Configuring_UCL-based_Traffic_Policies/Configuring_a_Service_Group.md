Configuring a Service Group
===========================

You need to create a service group before configuring UCL-based traffic policies.

#### Context

This configuration is supported only on the Admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-group**](cmdqueryname=service-group) *server-group-name*
   
   
   
   A new service group is created.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.