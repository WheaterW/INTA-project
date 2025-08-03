Configuring the BGP4+ Default Route
===================================

Configuring the BGP4+ Default Route

#### Prerequisites

Before configuring the BGP4+ default route, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

On large or medium-sized BGP4+ networks, the BGP4+ routing table of a device contains a large number of routing entries, consuming a large number of memory resources. In addition, the transmission and processing of routing information consumes many network resources. In scenarios where a BGP4+ peer's routing table contains multiple routes advertised by the local device, you can configure the device to advertise the default route with the local address as the next hop address to this peer, regardless of whether the default route exists in the local routing table. This significantly reduces the number of routes transmitted on the network and minimizes consumption of network resources and the peer's memory resources.


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
4. Configure the device to advertise the default route to a specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+default-route-advertise+route-policy) group-name default-route-advertise [ route-policy route-policy-name ] { conditional-route-match-all | conditional-route-match-any } { ipv6-address mask-length } &<1-4>
   ```
   ```
   [peer](cmdqueryname=peer+default-route-advertise+route-policy) peerIpv6Addr default-route-advertise [ route-policy route-policy-name ] { conditional-route-match-all | conditional-route-match-any } { ipv6-address ipv6-mask-length } &<1-4>
   ```
   ```
   [peer](cmdqueryname=peer+default-route-advertise+route-policy) ipv4-address default-route-advertise [ route-policy route-policy-name ] { conditional-route-match-all | conditional-route-match-any } { ipv6-address mask-length } &<1-4>
   ```
   
   If **route-policy** *route-policy-name* is specified, the BGP4+ device changes attributes of the default route to be advertised to a specified peer or peer group based on the specified route-policy.
   
   If **conditional-route-match-all** { *ipv6-address1* *ipv6-mask-length1* } &<1-4> is specified, the BGP4+ device advertises the default route only if all the routes matching the specified conditions exist in the local IPv6 routing table.
   
   If **conditional-route-match-any** { *ipv6-address2* *ipv6-mask-length2* } &<1-4> is specified, the device advertises the default route if any route matching a specified condition exists in the local IPv6 routing table.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the [**peer default-route-advertise**](cmdqueryname=peer+default-route-advertise) command is run on a device, the device advertises a default route (with its local address as the next-hop address) to the specified peer, regardless of whether there is a default route in the local routing table.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify it:

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command on the peer device to check information about the default route received by BGP4+.