Configuring Suppression on BGP Peer Flapping
============================================

Suppression on BGP peer flapping allows a device to delay the establishment of a BGP peer relationship that flaps continuously.

#### Usage Scenario

BGP peer flapping occurs when BGP peer relationships are disconnected and then immediately re-established in a quick sequence that is repeated. Frequent BGP peer flapping is caused by various factors; for example, a link is unstable, or an interface that carries BGP services is unstable. After a BGP peer relationship is established, the local device and its BGP peer usually exchange all routes in their BGP routing tables with each other. If the BGP peer relationship is disconnected, the local device deletes all the routes learned from the BGP peer. Generally, a large number of BGP routes exist, and in this case, a large number of routes change and a large amount of data is processed when the BGP peer relationship is flapping. As a result, a high volume of resources are consumed, causing high CPU usage. To prevent this issue, a device supports suppression on BGP peer flapping. With this function enabled, the local device suppresses the establishment of the BGP peer relationship if it flaps continuously.


#### Pre-configuration Tasks

Before configuring suppression on BGP peer flapping, complete the following task:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+oscillation-dampening)*peerIpv4Addr* **oscillation-dampening**
   
   
   
   BGP is enabled to suppress the establishment of a specified peer relationship that flaps continuously.
   
   
   
   To immediately remove the suppression, you can run the [**peer oscillation-dampening disable**](cmdqueryname=peer+oscillation-dampening+disable) command. Alternatively, you can run a reset command or another command that can cause the peer relationship to be disconnected and re-established.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp peer verbose**](cmdqueryname=display+bgp+peer+verbose) command to check the status of suppression on BGP peer flapping and the remaining time to establish the BGP peer relationship.