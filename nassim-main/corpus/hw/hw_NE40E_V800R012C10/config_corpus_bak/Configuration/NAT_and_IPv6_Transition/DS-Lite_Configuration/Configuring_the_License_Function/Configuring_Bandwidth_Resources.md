Configuring Bandwidth Resources
===============================

To improve DS-Lite forwarding performance on a dedicated board, configure DS-Lite bandwidth resources to increase bandwidth on the dedicated board.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active nat bandwidth-enhance**](cmdqueryname=active+nat+bandwidth-enhance) *bandwidth* [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   Board-wide bandwidth is configured.
   
   
   
   If no bandwidth resource is configured for a board, DS-Lite services are unavailable.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.