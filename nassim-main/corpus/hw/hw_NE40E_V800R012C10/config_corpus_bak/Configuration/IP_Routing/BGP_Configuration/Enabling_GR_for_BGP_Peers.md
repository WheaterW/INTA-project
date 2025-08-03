Enabling GR for BGP Peers
=========================

After the GR capability is configured for a BGP peer, a BGP speaker can negotiate with the peer to establish a BGP session with the GR capability.

#### Usage Scenario

A BGP restart causes re-establishment of all the involved peer relationships, resulting in traffic interruption. Enabling GR globally can prevent traffic interruption. However, this will disconnect all the BGP peer relationships on a device and cause the device to re-negotiate the GR capability with these peers, which affects all the BGP-dependent services running on the live network. To prevent this problem, you can enable GR on a BGP speaker for specified BGP peers so that the BGP speaker can establish GR-capable BGP sessions with the specified peers through negotiation.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+capability-advertise+graceful-restart) { *ipv4-address* | *group-name* } **capability-advertise graceful-restart**
   
   
   
   GR is enabled, and the device is configured to advertise the GR capability to the specified BGP peer or peer group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a specified peer group contains peers that do not support GR, you can run the **peer** *group-name* **local-graceful-restart enable** command to enable local GR for the specified peer group.
4. (Optional) Run [**peer**](cmdqueryname=peer+graceful-restart+timer+restart) { *ipv4-address* | *group-name* } **graceful-restart timer restart** *time-value*
   
   
   
   The maximum duration is set for a specified peer or peer group to wait for the local BGP peer relationship to be re-established, and the device is configured to advertise the duration to the peer or peer group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the specified peer does not support GR, run the [**peer**](cmdqueryname=peer+graceful-restart+timer+restart) *ipv4-address* **local-graceful-restart timer restart** *restart-time* command to set the maximum duration for the device to wait for its BGP peer relationship to be re-established with the specified peer.
   
   If a peer in a specified peer group does not support GR, you can run the [**peer**](cmdqueryname=peer+graceful-restart+timer+restart) *group-name* **local-graceful-restart timer restart** *restart-time* command to set the maximum duration for the local device to wait for its peer relationships to be re-established with the specified BGP peer group.
5. (Optional) Run [**peer**](cmdqueryname=peer+graceful-restart+peer-reset) { *ipv4-address* | *group-name* } [**graceful-restart peer-reset**](cmdqueryname=graceful-restart+peer-reset)
   
   
   
   The device is enabled to use the GR mode to reset the BGP connection with the specified peer or each peer in the specified group.
   
   
   
   Currently, BGP does not support dynamic capability negotiation. Therefore, BGP capability changes cause peer relationships to be re-established and routing entries to be deleted, interrupting services. If a BGP capability changes when BGP IPv4 unicast peer relationships have been established and IPv4 services are running properly, the BGP IPv4 unicast peer relationships will be reestablished, affecting the ongoing IPv4 services. To solve this problem, perform this step to enable the router to reset BGP connections in GR mode after GR is enabled for the BGP peer.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**peer capability-advertise graceful-restart**](cmdqueryname=peer+capability-advertise+graceful-restart) command is run but the [**peer graceful-restart peer-reset**](cmdqueryname=peer+graceful-restart+peer-reset) command is not run, the BGP connection is not reset in GR mode for the peer relationship reestablishment triggered by the [**reset bgp**](cmdqueryname=reset+bgp) command or dynamic capability negotiation. The BGP connection is reset in GR mode for the peer relationship reestablishment triggered by the [**reset bgp**](cmdqueryname=reset+bgp) command or dynamic capability negotiation only if both the [**peer capability-advertise graceful-restart**](cmdqueryname=peer+capability-advertise+graceful-restart) and [**peer graceful-restart peer-reset**](cmdqueryname=peer+graceful-restart+peer-reset) commands are run.
6. (Optional) Run [**peer**](cmdqueryname=peer+graceful-restart+timer+wait-for-rib) { *ipv4-address* | *group-name* } [**graceful-restart timer wait-for-rib**](cmdqueryname=graceful-restart+timer+wait-for-rib) *time-value*
   
   
   
   The maximum duration is set for the device to wait for the End-of-RIB flag from the specified peer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the specified peer does not support GR, you can run the [**peer**](cmdqueryname=peer+graceful-restart+timer+wait-for-rib) *ipv4-address* **local-graceful-restart** **timer wait-for-rib** *wfrtime* command to set the duration for the local end to wait for the End-of-RIB flag from the specified peer.
   
   If a specified peer group contains a peer that does not support GR, you can run the [**peer**](cmdqueryname=peer+graceful-restart+timer+wait-for-rib) *group-name* **local-graceful-restart** **timer wait-for-rib** *wfrtime* command to set the duration for the local end to wait for the End-of-RIB flag from the specified peer group.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) **verbose** command to check the BGP GR status.
* Run the [**display bgp**](cmdqueryname=display+bgp+graceful-restart+status) **graceful-restart status** command to check GR information on the BGP speaker.
* Run the [**display bgp**](cmdqueryname=display+bgp+local-graceful-restart+status) **local-graceful-restart status** command to check information about local GR on the BGP speaker.