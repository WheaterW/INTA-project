Enabling BGP GR
===============

Enabling or disabling GR may delete and re-establish all sessions and instances.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**graceful-restart**](cmdqueryname=graceful-restart)
   
   
   
   BGP GR is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Running the [**graceful-restart**](cmdqueryname=graceful-restart) command deletes and re-establishes all sessions and instances, causing service interruptions. Therefore, exercise caution when running this command. You are advised to enable GR when establishing BGP peer relationships.
4. (Optional) Run [**graceful-restart timer restart**](cmdqueryname=graceful-restart+timer+restart) *restart-time*
   
   
   
   The maximum time is set for the local end to wait for GR recovery on the peer end.
5. (Optional) Run [**graceful-restart peer-reset**](cmdqueryname=graceful-restart+peer-reset)
   
   
   
   The router is enabled to reset a BGP session in GR mode.
   
   
   
   Currently, BGP does not support dynamic capability negotiation. Therefore, BGP capability changes cause peer relationships to be re-established and routing entries to be deleted, interrupting services. If a BGP capability changes when BGP IPv4 unicast peer relationships have been established and IPv4 services are running properly, the BGP IPv4 unicast peer relationships will be reestablished, affecting the ongoing IPv4 services. To solve this problem, perform this step to enable the router to reset BGP connections in GR mode after GR is enabled globally.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**graceful-restart**](cmdqueryname=graceful-restart) command is run but the [**graceful-restart peer-reset**](cmdqueryname=graceful-restart+peer-reset) command is not run, the BGP connection is not reset in GR mode for the peer relationship reestablishment triggered by the [**reset bgp**](cmdqueryname=reset+bgp) command or dynamic capability negotiation. The BGP connection is reset in GR mode for the peer relationship reestablishment triggered by the [**reset bgp**](cmdqueryname=reset+bgp) command or dynamic capability negotiation only if both the [**graceful-restart**](cmdqueryname=graceful-restart) and [**graceful-restart peer-reset**](cmdqueryname=graceful-restart+peer-reset) commands are run.
6. (Optional) Run [**rpd-family**](cmdqueryname=rpd-family)
   
   
   
   The BGP RPD address family view is displayed.
7. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* [**enable**](cmdqueryname=peer+enable)
   
   
   
   The device is enabled to exchange routing information with the specified peer.
8. Run [**peer**](cmdqueryname=peer+graceful-restart) *ipv4-address* **graceful-restart** **static-timer** *restart-time*
   
   
   
   The maximum time is configured for the local end to wait for the peer end to recover from GR.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.