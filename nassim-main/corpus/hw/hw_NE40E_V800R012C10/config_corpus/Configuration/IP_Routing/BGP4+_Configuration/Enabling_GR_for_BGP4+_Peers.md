Enabling GR for BGP4+ Peers
===========================

After graceful restart (GR) is enabled for BGP4+ peers specified on a BGP4+ speaker, the BGP4+ speaker can negotiate the GR capability with these peers and establish BGP4+ connections with them if negotiation succeeds.

#### Usage Scenario

A BGP4+ restart causes re-establishment of all the involved peer relationships, resulting in traffic interruption. Enabling GR globally can prevent traffic interruption. However, this will disconnect all the BGP4+ peer relationships on a device and cause the device to re-negotiate the GR capability with these peers, which affects all the BGP4+-dependent services running on the live network. To prevent this problem, you can enable GR on a BGP4+ speaker for specified BGP4+ peers so that the BGP4+ speaker can establish GR-capable BGP4+ sessions with the specified peers through negotiation.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run **peer** *ipv6-address* **capability-advertise graceful-restart**
   
   
   
   GR is enabled for a specified BGP4+ peer, and the device is configured to advertise the GR capability to the specified peer.
4. (Optional) Run [**peer**](cmdqueryname=peer+graceful-restart+timer+restart) *ipv6-address***graceful-restart timer restart** *time-value*
   
   
   
   The maximum duration is set for a specified peer to wait for the local BGP4+ peer relationship to be re-established, the device is configured to advertise the duration to the peer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the specified peer does not support GR, you are advised to run the **peer** *ipv6-address* **local-graceful-restart timer restart** *restart-time* command instead to set the maximum duration for the device to wait for its BGP4+ peer relationship to be reestablished with the specified peer.
5. (Optional) Run [**peer**](cmdqueryname=peer) *ipv6-address* [**graceful-restart peer-reset**](cmdqueryname=graceful-restart+peer-reset)
   
   
   
   The device is enabled to use the GR mode to reset the BGP4+ connection with the specified peer.
   
   
   
   Currently, BGP4+ does not support dynamic capability negotiation. Therefore, a change in a BGP4+ capability causes peer relationship re-establishment. If a BGP4+ capability changes when BGP IPv6 unicast peer relationships have been established and IPv6 services are running properly, the BGP IPv6 unicast peer relationships will be reestablished, affecting the ongoing IPv6 services. To address this issue, run the [**peer**](cmdqueryname=peer) *ipv6-address* [**graceful-restart peer-reset**](cmdqueryname=graceful-restart+peer-reset) command in advance.
6. (Optional) Run [**peer**](cmdqueryname=peer) *ipv6-address* [**graceful-restart timer wait-for-rib**](cmdqueryname=graceful-restart+timer+wait-for-rib) *time-value*
   
   
   
   The maximum duration is set for the device to wait for the End-of-RIB flag from the specified peer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a specified peer does not support GR, run the **peer** *ipv6-address* **local-graceful-restart** **timer wait-for-rib** *wfrtime* command instead to set the maximum duration.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer+verbose) **verbose** command to check the BGP4+ GR status.
* Run the [**display bgp**](cmdqueryname=display+bgp+graceful-restart+status) **graceful-restart status** command to check GR information on the BGP speaker.
* Run the [**display bgp**](cmdqueryname=display+bgp+local-graceful-restart+status) **local-graceful-restart status** command to check information about local GR on the BGP speaker.