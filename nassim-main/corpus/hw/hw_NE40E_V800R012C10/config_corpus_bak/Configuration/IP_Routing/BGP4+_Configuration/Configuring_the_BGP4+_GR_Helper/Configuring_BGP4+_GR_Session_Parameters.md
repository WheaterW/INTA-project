Configuring BGP4+ GR Session Parameters
=======================================

You can change the restart time to reestablish a BGP peer relationship.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**graceful-restart timer wait-for-rib**](cmdqueryname=graceful-restart+timer+wait-for-rib) *time*
   
   
   
   The period during which the restarting speaker and receiving speaker wait for End-of-RIB messages is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can adjust GR parameter values for the BGP4+ session as needed. However, retaining default parameter values is recommended.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.