Configuring Suppression on BGP4+ Peer Flapping
==============================================

Suppression on BGP4+ peer flapping allows a device to delay the establishment of a BGP4+ peer relationship that flaps continuously.

#### Prerequisites

Before configuring suppression on BGP4+ peer flapping, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

BGP4+ peer flapping occurs when BGP4+ peer relationships are disconnected and then immediately re-established in a quick sequence that is repeated. Frequent BGP4+ peer flapping is caused by various factors; for example, a link is unstable, or an interface that carries BGP4+ services is unstable. After a BGP4+ peer relationship is established, the local device and its BGP4+ peer usually exchange all routes in their BGP4+ routing tables with each other. If the BGP4+ peer relationship is disconnected, the local device deletes all the routes learned from the BGP4+ peer. Generally, a large number of BGP4+ routes exist, and in this case, a large number of routes change and a large amount of data is processed during frequent peer flapping. As a result, a large number of resources are consumed, causing high CPU usage. To prevent this issue, a device supports suppression on BGP4+ peer flapping. With this function enabled, the local device suppresses the establishment of the BGP4+ peer relationship if it flaps continuously.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enable BGP4+ to suppress the establishment of a specified peer relationship that flaps repeatedly.
   
   
   ```
   [peer](cmdqueryname=peer+oscillation-dampening) peerIpv6Addr oscillation-dampening
   ```
   
   By default, a device suppresses the establishment of BGP4+ peer relationships that flap repeatedly. To immediately remove the suppression, you can run the [**peer**](cmdqueryname=peer)*peerIpv6Addr* **oscillation-dampening** **disable** command. Alternatively, you can run a reset command or another command that can cause the peer relationship to be disconnected and re-established.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp ipv6 peer verbose**](cmdqueryname=display+bgp+ipv6+peer+verbose) command to check the suppression status of the flapping BGP4+ peer relationship and the remaining time to establish the BGP4+ peer relationship.