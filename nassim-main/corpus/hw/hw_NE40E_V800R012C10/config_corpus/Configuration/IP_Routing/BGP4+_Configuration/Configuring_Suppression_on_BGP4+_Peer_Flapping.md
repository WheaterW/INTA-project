Configuring Suppression on BGP4+ Peer Flapping
==============================================

Suppression on BGP4+ peer flapping allows a device to delay the establishment of a BGP4+ peer relationship that flaps continuously.

#### Usage Scenario

BGP4+ peer flapping occurs when BGP4+ peer relationships are disconnected and then immediately re-established in a quick sequence that is repeated. Frequent BGP4+ peer flapping is caused by various factors; for example, a link is unstable, or an interface that carries BGP4+ services is unstable. After a BGP4+ peer relationship is established, the local device and its BGP4+ peer usually exchange all routes in their BGP4+ routing tables with each other. If the BGP4+ peer relationship is disconnected, the local device deletes all the routes learned from the BGP4+ peer. Generally, a large number of BGP4+ routes exist, and in this case, a large number of routes change and a large amount of data is processed during frequent peer flapping. As a result, a large number of resources are consumed, causing high CPU usage. To prevent this issue, a device supports suppression on BGP4+ peer flapping. With this function enabled, the local device suppresses the establishment of the BGP4+ peer relationship if it flaps continuously.


#### Pre-configuration Tasks

Before configuring suppression on BGP4+ peer flapping, complete the following task:

* [Configuring Basic BGP4+ Functions](dc_vrp_bgp6_cfg_0003.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+oscillation-dampening)*peerIpv6Addr* **oscillation-dampening**
   
   
   
   BGP4+ is enabled to suppress the establishment of a specified peer relationship that flaps continuously.
   
   
   
   To immediately remove the suppression, you can run the [**peer oscillation-dampening disable**](cmdqueryname=peer+oscillation-dampening+disable) command. Alternatively, you can run a reset command or another command that can cause the peer relationship to be disconnected and re-established.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp ipv6 peer verbose**](cmdqueryname=display+bgp+ipv6+peer+verbose) command to check the suppression status of the flapping BGP4+ peer relationship and the remaining time to establish the BGP4+ peer relationship.