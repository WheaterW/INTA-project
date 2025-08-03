(Optional) Configuring Interfaces to Support EDSG Service Policies Delivered by Diameter Servers
================================================================================================

If Diameter needs to be used in EDSG service scenarios, configure Diameter interfaces to support EDSG service policies delivered by Diameter servers.

#### Context

If Diameter needs to be used in EDSG service scenarios, configure Diameter Gx interfaces to support the EDSG service policies delivered by Diameter servers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**diameter predefined-rule support-type edsg**](cmdqueryname=diameter+predefined-rule+support-type+edsg)
   
   
   
   Diameter Gx interfaces are configured to support the EDSG service policies delivered by Diameter servers.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.