Enabling GR for BGP Peers
=========================

Enabling GR for BGP Peers

#### Context

A BGP restart causes re-establishment of all the involved peer relationships, resulting in traffic interruption. Enabling GR globally can prevent traffic interruption. However, this will disconnect all the BGP peer relationships on a device and cause the device to re-negotiate the GR capability with these peers, which affects all the BGP-dependent services running on the live network. To prevent this problem, you can enable GR on a BGP speaker for specified BGP peers so that the BGP speaker can establish GR-capable BGP sessions with the specified peers through negotiation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enable GR and configure the device to advertise the GR capability to the specified BGP peer or peer group.
   
   
   ```
   peer { ipv4-address | group-name } capability-advertise graceful-restart
   ```
   
   By default, GR is not enabled for a specified peer.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If a specified peer group has peers that do not support GR, you can run both the **peer** *group-name* **capability-advertise graceful-restart** and **peer** *group-name* **local-graceful-restart enable** commands.
4. Set the maximum duration for a specified peer or peer group to wait for the local BGP peer relationship to be re-established and configure the device to advertise the duration to the peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+graceful-restart+timer+restart) { ipv4-address | group-name } graceful-restart timer restart time-value
   ```
   
   By default, the maximum duration for a specified peer or peer group to wait for the local BGP peer relationship to be re-established is 150s.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the specified peer does not support GR, run the **peer** *ipv4-address* **local-graceful-restart timer restart** *restart-time* command to set the maximum duration for the device to wait for its BGP peer relationship to be reestablished with the specified peer.
   
   If the specified peer group has peers that do not support GR, you can run both the **peer** *group-name* **graceful-restart timer restart** *time-value* and **peer** *group-name* **local-graceful-restart timer restart** *restart-time* commands.
5. (Optional) Enable the device to use the GR mode to reset BGP connections with a specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name } [graceful-restart peer-reset](cmdqueryname=graceful-restart+peer-reset)
   ```
   
   Currently, BGP does not support dynamic capability negotiation. Therefore, a change in a BGP capability causes peer relationship re-establishment. If a BGP capability changes when BGP IPv4 unicast peer relationships have been established and IPv4 services are running properly, the BGP IPv4 unicast peer relationships will be reestablished, affecting the ongoing IPv4 services. To solve this problem, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**graceful-restart peer-reset**](cmdqueryname=graceful-restart+peer-reset) command in advance.
6. (Optional) Set the duration for the local end to wait for the End-of-RIB flag from the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name } [graceful-restart timer wait-for-rib](cmdqueryname=graceful-restart+timer+wait-for-rib) time-value
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the specified peer does not support GR, you can run the **peer** *ipv4-address* **local-graceful-restart** **timer wait-for-rib** *wfrtime* command to set the duration for the local end to wait for the End-of-RIB flag from the specified peer.
   
   If the specified peer group has peers that do not support GR, you can run both the **peer** *group-name* [**graceful-restart timer wait-for-rib**](cmdqueryname=graceful-restart+timer+wait-for-rib) *time-value* and **peer** *group-name* **local-graceful-restart** **timer wait-for-rib** *wfrtime* commands.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring GR for BGP peers, run the following commands to check the configuration.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) **verbose** command to check the BGP GR status.
* Run the [**display bgp**](cmdqueryname=display+bgp) **graceful-restart status** command to check GR information on the BGP speaker.
* Run the [**display bgp**](cmdqueryname=display+bgp) **local-graceful-restart status** command to check information about local GR on the BGP speaker.