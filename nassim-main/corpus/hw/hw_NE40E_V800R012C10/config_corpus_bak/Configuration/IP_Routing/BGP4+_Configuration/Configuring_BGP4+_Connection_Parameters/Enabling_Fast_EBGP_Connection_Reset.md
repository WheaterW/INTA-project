Enabling Fast EBGP Connection Reset
===================================

After fast EBGP connection reset is enabled, BGP4+ can rapidly detect EBGP link faults and reset BGP4+ connections on interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ebgp-interface-sensitive**](cmdqueryname=ebgp-interface-sensitive)
   
   
   
   Fast EBGP connection reset is enabled.
   
   
   
   If the interface on which a BGP4+ connection is established alternates between up and down, you can run the [**undo ebgp-interface-sensitive**](cmdqueryname=ebgp-interface-sensitive) command to prevent repeated reestablishment and deletion of the BGP4+ session caused by route flapping. This saves network bandwidth.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.