Configuring a Device to Advertise the Default Route
===================================================

Configuring a Device to Advertise the Default Route

#### Prerequisites

Before configuring a BGP device to advertise the default route, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure the device to advertise the default route to a specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+default-route-advertise+route-policy) { group-name | peerIpv4Addr | peerIpv6Addr } default-route-advertise [ route-policy route-policy-name ] [ conditional-route-match-all { ipv4-address1 { mask1 | mask-length1 } } &<1-4> | conditional-route-match-any { ipv4-address2 { mask2 | mask-length2 } } &<1-4> ]
   ```
   
   If **route-policy** *route-policy-name* is specified, the device changes attributes of the default route based on the specified route-policy.
   
   If **conditional-route-match-all** { *ipv4-address1* { *mask1* | *mask-length1* } } &<1-4> is specified, the BGP device advertises the default route only if all the routes matching the specified conditions exist in the local IP routing table.
   
   If **conditional-route-match-any** { *ipv4-address2* { *mask2* | *mask-length2* } } &<1-4> is specified, the device advertises the default route if any route matching a specified condition exists in the local IP routing table.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the [**peer default-route-advertise**](cmdqueryname=peer+default-route-advertise) command is run on a device, the device advertises a default route (with its local address as the next-hop address) to the specified peer, regardless of whether there is a default route in the local routing table.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *ipv4-address* [ *mask* | *mask-length*]] command on the peer end to check the received BGP default route.