Enabling a BGP Device to Advertise Supernet Unicast Routes to BGP Peers
=======================================================================

Enabling a BGP Device to Advertise Supernet Unicast Routes to BGP Peers

#### Prerequisites

Before enabling a BGP device to advertise supernet unicast routes to BGP peers, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

In a BGP supernet unicast route, either the destination address and next hop address are the same, or the mask length of the destination address is longer than that of the next hop address. Any route that meets either of the following conditions is considered a supernet unicast route:

* If bitwise AND operations are performed on the destination address mask with the destination address and next hop address, the two obtained network addresses are the same, and destination address mask is greater than or equal to the next hop address mask.
* If bitwise AND operations are performed on the destination address mask with the destination address and next hop address, the two obtained network addresses are different. If bitwise AND operations are performed on the next hop address mask with the destination address and next hop address, however, the two obtained network addresses are the same.

By default, when a device receives a BGP supernet unicast route, the device sets the route to be invalid and does not advertise it to other BGP peers. However, such routes may need to be advertised to peers in some scenarios; for example, scenarios where a Huawei device needs to interwork with a non-Huawei device. If the Huawei device receives BGP supernet unicast routes from the non-Huawei device and needs to advertise them to other BGP peers, you can enable the Huawei device to advertise BGP supernet unicast routes to BGP peers.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Enable the device to advertise BGP supernet unicast routes to BGP peers.
   
   
   ```
   [supernet unicast advertise](cmdqueryname=supernet+unicast+advertise+enable) enable
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to check information about BGP supernet unicast routes.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *network* command to check information about the BGP supernet unicast routes advertised to peers.