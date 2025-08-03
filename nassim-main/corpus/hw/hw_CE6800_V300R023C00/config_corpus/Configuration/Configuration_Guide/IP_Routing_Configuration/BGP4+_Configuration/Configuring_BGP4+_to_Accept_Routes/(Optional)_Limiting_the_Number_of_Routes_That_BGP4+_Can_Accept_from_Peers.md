(Optional) Limiting the Number of Routes That BGP4+ Can Accept from Peers
=========================================================================

(Optional) Limiting the Number of Routes That BGP4+ Can Accept from Peers

#### Context

If a BGP4+ device is maliciously attacked or network configuration errors occur, the device will receive a large number of routes from its peers. As a result, a large number of resources are consumed on the device. To prevent this issue, the administrator must limit the resources to be consumed during device operation based on the network planning and device capacity. BGP4+ provides peer-based route control to limit the number of routes to be accepted from peers.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Set a limit on the number of routes that can be accepted from a peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { group-name | ipv6-address | ipv4-address } [route-limit](cmdqueryname=route-limit+alert-only+idle-forever+idle-timeout) limit [ percentage ] [ alert-only | idle-forever | idle-timeout times ]
   ```
   
   This command provides route control based on peers. You can specify parameters as needed to control the processing if the number of the routes accepted from a peer exceeds the limit specified.
   
   * **alert-only**: The peer relationship is not terminated. The device no longer accepts routes from the peer after the limit is exceeded, and an alarm is generated and logged.
   * If **idle-forever** is set, the peer relationship is interrupted and the system does not automatically attempt to re-establish the connection. In this case, an alarm is generated, and a log is recorded. In this case, the peer status is **Idle** in the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) [ **verbose** ] command output. To restore the BGP connection, run the [**reset bgp ipv6**](cmdqueryname=reset+bgp+ipv6) command.
   * If **idle-timeout** is set, the peer relationship is interrupted. The device retries setting up a connection after the timer expires. An alarm is generated, and a log is recorded. In this case, the peer status is **Idle** in the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) [ **verbose** ] command output. To restore the BGP connection before the timer expires, run the [**reset bgp ipv6**](cmdqueryname=reset+bgp+ipv6) command.
   * If none of the preceding parameters is set, the peer relationship is disconnected. The device retries setting up a connection in 30 seconds. An alarm is generated, and a log is recorded.![](public_sys-resources/note_3.0-en-us.png) 
   
   If the number of routes received by a device exceeds a specified limit and the [**peer route-limit**](cmdqueryname=peer+route-limit) command is used for the first time, the device re-establishes the peer relationship with the specified peer, regardless of whether **alert-only** is specified.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```