Configuring Suppression on BGP Peer Flapping
============================================

Suppression on BGP peer flapping allows a device to delay the establishment of a BGP peer relationship that flaps continuously.

#### Prerequisites

Before configuring suppression on BGP peer flapping, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

BGP peer flapping occurs when BGP peer relationships are disconnected and then immediately re-established in a quick sequence that is repeated. Frequent BGP peer flapping is caused by various factors; for example, a link is unstable, or an interface that carries BGP services is unstable. After a BGP peer relationship is established, the local device and its BGP peer usually exchange all routes in their BGP routing tables with each other. If the BGP peer relationship is disconnected, the local device deletes all the routes learned from the BGP peer. Generally, a large number of BGP routes exist, and in this case, a large number of routes change and a large amount of data is processed during frequent peer flapping. As a result, a large number of resources are consumed, causing high CPU usage. To prevent this issue, a device supports suppression on BGP peer flapping. With this function enabled, the local device suppresses the establishment of the BGP peer relationship if it flaps continuously.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enable BGP to suppress the establishment of a specified peer relationship that flaps repeatedly.
   
   
   ```
   [peer](cmdqueryname=peer+oscillation-dampening) peerIpv4Addr oscillation-dampening
   ```
   
   By default, a device suppresses the establishment of BGP peer relationships that flap repeatedly. To immediately remove the suppression, you can run the [**peer**](cmdqueryname=peer)*peerIpv4Addr* **oscillation-dampening** **disable** command. Alternatively, you can run a reset command or another command that can cause the peer relationship to be disconnected and re-established.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp peer verbose**](cmdqueryname=display+bgp+peer+verbose) command to check the status of suppression on BGP peer flapping and the remaining time to establish the BGP peer relationship.