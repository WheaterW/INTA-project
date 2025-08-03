Configuring Bandwidth Resources
===============================

Bandwidth resources are essential for dedicated NAT.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active nat bandwidth-enhance**](cmdqueryname=active+nat+bandwidth-enhance) *bandwidth* [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   Board-wide bandwidth resources are configured for a specified dedicated board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.