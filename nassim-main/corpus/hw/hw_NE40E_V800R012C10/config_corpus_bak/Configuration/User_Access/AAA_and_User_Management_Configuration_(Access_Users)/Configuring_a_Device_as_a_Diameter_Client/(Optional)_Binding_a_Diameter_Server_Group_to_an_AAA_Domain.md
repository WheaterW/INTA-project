(Optional) Binding a Diameter Server Group to an AAA Domain
===========================================================

After a Diameter server group is configured, bind the server
group to an AAA domain.

#### Context

After a Diameter server group is
configured, bind the server group to an AAA domain so that the Diameter
server group can be used in this domain.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**diameter-server group**](cmdqueryname=diameter-server+group) *group-name*
   
   
   
   A Diameter server group is bound to the AAA domain.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.