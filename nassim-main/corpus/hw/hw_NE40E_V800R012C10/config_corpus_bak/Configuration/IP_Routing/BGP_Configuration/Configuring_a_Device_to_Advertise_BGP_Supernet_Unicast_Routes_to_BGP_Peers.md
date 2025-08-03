Configuring a Device to Advertise BGP Supernet Unicast Routes to BGP Peers
==========================================================================

This section describes how to configure a Border Gateway Protocol (BGP) device to advertise BGP supernet unicast routes to BGP peers.

#### Usage Scenario

A BGP supernet route has the same destination address and next hop address or has a more detailed destination address than the next hop address. Any route that meets one of the following conditions is a BGP supernet route.

* If bitwise AND operations are performed on the destination address mask with the destination address and next hop address, the two obtained network addresses are the same, and destination address mask is greater than or equal to the next hop address mask.
* If bitwise AND operations are performed on the destination address mask with the destination address and next hop address, the two obtained network addresses are different. If bitwise AND operations are performed on the next hop address mask with the destination address and next hop address, however, the two obtained network addresses are the same.

For example, the route with the destination address being 6.6.6.6 in the following command output is a BGP supernet route.

```
<HUAWEI> display bgp routing-table
```
```
 BGP Local router ID is 1.1.1.2
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 1
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn

 *>i    6.6.6.6/32         6.6.6.6         0          100        0       i
```

By default, when a BGP device receives a BGP supernet unicast route, the BGP device sets the route invalid and does not advertise it to other BGP peers. If a Huawei device is connected to a non-Huawei device and you want the Huawei device to advertise BGP supernet unicast routes that it receives from the non-Huawei device to other BGP peers, configure the Huawei device to advertise BGP supernet unicast routes to BGP peers.


#### Pre-configuration Tasks

Before you configure a device to send supernet unicast routes to its peers, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The BGP-IPv4 unicast address family view is displayed.
4. Run [**supernet unicast advertise**](cmdqueryname=supernet+unicast+advertise+enable) **enable**
   
   
   
   The device is enabled to advertise BGP supernet unicast routes to its peers.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) command to check BGP supernet unicast routes.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *network* command to check information about the BGP supernet unicast routes advertised to peers.