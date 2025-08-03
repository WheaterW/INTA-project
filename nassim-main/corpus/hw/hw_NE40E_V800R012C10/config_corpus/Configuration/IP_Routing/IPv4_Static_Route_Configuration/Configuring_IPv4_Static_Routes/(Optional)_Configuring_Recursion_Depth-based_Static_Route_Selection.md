(Optional) Configuring Recursion Depth-based Static Route Selection
===================================================================

To prevent inter-board service transmission or routing loop in a static route scenario, configure recursion depth-based static route selection.

#### Context

Among static routes with the same prefix but different recursion depths, the static routes with shorter recursion depths are more stable. After recursion depth-based static route selection is configured, the system selects the static routes with shorter recursion depths as active routes and delivers them to the Forwarding Information Base (FIB) table. The other routes become inactive.

To prevent inter-board service transmission or routing loop in a static route scenario, configure recursion depth-based static route selection.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip route-static selection-rule relay-depth**](cmdqueryname=ip+route-static+selection-rule+relay-depth)
   
   
   
   Recursion depth-based static route selection is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.