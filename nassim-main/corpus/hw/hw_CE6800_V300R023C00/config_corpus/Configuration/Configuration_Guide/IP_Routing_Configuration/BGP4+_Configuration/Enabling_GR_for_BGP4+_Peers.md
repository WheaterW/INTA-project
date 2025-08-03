Enabling GR for BGP4+ Peers
===========================

Enabling GR for BGP4+ Peers

#### Context

A BGP4+ restart causes re-establishment of all the involved peer relationships, resulting in traffic interruption. Enabling GR globally can prevent traffic interruption. However, this will disconnect all the BGP4+ peer relationships on a device and cause the device to re-negotiate the GR capability with these peers, which affects all the services that depend on BGP4+ on the live network. To prevent this problem, you can enable GR on a BGP4+ speaker for specified BGP4+ peers so that the BGP4+ speaker can establish GR-capable BGP4+ sessions with the specified peers through negotiation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enable GR and configure the device to advertise the GR capability to the specified BGP4+ peer or peer group.
   
   
   ```
   peer ipv6-address capability-advertise graceful-restart
   ```
   
   By default, GR is not enabled for a specified peer.
4. Set the maximum duration for a specified peer or peer group to wait for the local BGP4+ peer relationship to be re-established and configure the device to advertise the duration to the peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+graceful-restart+timer+restart) ipv6-address graceful-restart timer restart time-value
   ```
   
   By default, the maximum duration for a specified peer or peer group to wait for the local BGP4+ peer relationship to be re-established is 150s.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the specified peer does not support GR, run the **peer** *ipv6-address* **local-graceful-restart timer restart** *restart-time* command to set the maximum duration for the device to wait for its BGP4+ peer relationship to be reestablished with the specified peer.
5. (Optional) Enable the device to use the GR mode to reset BGP4+ connections with a specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) ipv6-address [graceful-restart peer-reset](cmdqueryname=graceful-restart+peer-reset)
   ```
   
   Currently, BGP4+ does not support dynamic capability negotiation. Therefore, a change in a BGP4+ capability causes peer relationship re-establishment. If a BGP4+ capability changes when BGP IPv6 unicast peer relationships have been established and IPv6 services are running properly, the BGP IPv6 unicast peer relationships will be reestablished, affecting the ongoing IPv6 services. To address this issue, run the [**peer**](cmdqueryname=peer) *ipv6-address* [**graceful-restart peer-reset**](cmdqueryname=graceful-restart+peer-reset) command in advance.
6. (Optional) Set the duration for the local end to wait for the End-of-RIB flag from the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) ipv6-address [graceful-restart timer wait-for-rib](cmdqueryname=graceful-restart+timer+wait-for-rib) time-value
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the specified peer does not support GR, run the **peer** *ipv6-address* **local-graceful-restart** **timer wait-for-rib** *wfrtime* command instead to set the duration for the local end to wait for the End-of-RIB flag from the specified peer.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring GR for BGP4+ peers, run the following commands to check the configuration.

* Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) **verbose** command to check the BGP4+ GR status.
* Run the [**display bgp**](cmdqueryname=display+bgp) **graceful-restart status** command to check GR information on the BGP speaker.
* Run the [**display bgp**](cmdqueryname=display+bgp) **local-graceful-restart status** command to check the local GR information of a BGP speaker.