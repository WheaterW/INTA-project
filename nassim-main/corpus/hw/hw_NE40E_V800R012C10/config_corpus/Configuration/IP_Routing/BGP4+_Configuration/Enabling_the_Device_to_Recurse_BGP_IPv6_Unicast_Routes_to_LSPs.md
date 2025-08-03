Enabling the Device to Recurse BGP IPv6 Unicast Routes to LSPs
==============================================================

By default, BGP IPv6 unicast routes can recurse to outbound interfaces and next hops, but not to LSPs. A device can be enabled to recurse BGP IPv6 unicast routes to LSPs.

#### Usage Scenario

On the IPv4/MPLS backbone network shown in [Figure 1](#EN-US_TASK_0172366508__fig_dc_vrp_bgp6_cfg_010101), PE1, P, and PE2 run an IGP for interworking, an LDP LSP or MPLS TE tunnel is established between PE1 and PE2, and a public network IPv6 EBGP peer relationship is established between CE1 on an IPv6 network and PE1 and between CE2 on another IPv6 network and PE2. To allow PE1 and PE2 to exchange BGP IPv6 unicast routes, an IBGP peer relationship is established between PE1 and PE2 using loopback interfaces, and a BGP IPv4 peer relationship is established between PE1 and PE2 in the IPv6 unicast address family. CE1 sends an IPv6 route to PE1 through the EBGP peer connection. Upon receipt of the route, PE1 changes the next-hop IP address of the route to a local IP address and sends the route to PE2 through the IBGP peer connection. After PE2 learns the IPv6 route, it can recurse the route only to an outbound interface and next hop by default. However, PE2 can be enabled to recurse BGP IPv6 unicast routes to LSPs.

**Figure 1** Scenario where BGP IPv6 unicast routes recurse to LSPs  
![](images/fig_dc_vrp_bgp6_cfg_010101.png)

#### Pre-configuration Tasks

Before enabling the device to recurse BGP IPv6 unicast routes to LSPs, complete the following tasks:

* Configure an IGP.
* Establish an LDP LSP or MPLS TE tunnel between PE1 and PE2.
* Establish an IBGP peer relationship between PE1 and PE2 using loopback interfaces, and establish a BGP IPv4 peer relationship between PE1 and PE2 in the IPv6 unicast address family view.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
   
   
   
   The BGP-IPv6 unicast address family view is displayed.
4. Run [**unicast-route recursive-lookup tunnel-v4**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v4+tunnel-selector) [ **tunnel-selector** *tunnel-selector-name* ]
   
   
   
   The device is enabled to recurse BGP IPv6 unicast routes to tunnels.
   
   To enable the device to recurse BGP IPv6 unicast routes to MPLS TE tunnels, specify **tunnel-selector** *tunnel-selector-name* in the command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the device is enabled to recurse BGP IPv6 unicast routes to LSPs, you can run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* command to view information about such route recursion.