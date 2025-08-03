Configuring BGP GR Helper for MP-BGP
====================================

When MP-BGP restarts, the peer relationship is re-established and traffic forwarding is interrupted. If BGP GR Helper is enabled, traffic interruption can be prevented.

#### Context

Configure BGP GR Helper for MP-BGP on all the PEs (including the PE that serves as the ASBR) and the RRs that reflect the VPNv4 route, unless BGP GR Helper has been configured for MP-BGP when BGP GR Helper is configured between PEs and CEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**graceful-restart**](cmdqueryname=graceful-restart)
   
   
   
   BGP GR is enabled.
4. Run [**graceful-restart timer wait-for-rib**](cmdqueryname=graceful-restart+timer+wait-for-rib) *time*
   
   
   
   The period during which the restarting speaker and receiving speaker wait for End-Of-RIB messages is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can adjust parameter values of a BGP GR session as required. Generally, the default values of parameters are recommended.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.