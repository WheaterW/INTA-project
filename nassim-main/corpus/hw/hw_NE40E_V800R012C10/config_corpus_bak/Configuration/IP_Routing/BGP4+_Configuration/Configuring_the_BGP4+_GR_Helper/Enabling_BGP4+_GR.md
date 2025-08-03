Enabling BGP4+ GR
=================

Enabling or disabling GR may delete and re-establish all sessions and instances.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**graceful-restart**](cmdqueryname=graceful-restart)
   
   
   
   BGP4+ GR is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.