Configuring BGP-LU
==================

The BGP labeled unicast (BGP-LU) address family is used to transmit the mapping between labels and routes. After a BGP peer relationship is established in the BGP-LU address family, BGP peers can exchange BGP labeled routes and establish BGP LSPs between themselves.

#### Pre-configuration Tasks

Before configuring BGP-LU, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

1. Run **[**system-view**](cmdqueryname=system-view)**
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run **[**peer**](cmdqueryname=peer+as-number)** { *ipv4-address* | *group-name* } ****as-number**** **as-number**
   
   
   
   A BGP peer IP address and the number of the AS where the peer resides are specified.
4. Run [**ipv4-family labeled-unicast**](cmdqueryname=ipv4-family+labeled-unicast)
   
   
   
   The BGP-labeled address family view is displayed.
5. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
   
   
   
   The device is configured to exchange BGP-LU routing information with the specified peer.
6. (Optional) Run **[**network**](cmdqueryname=network)** **ipv4-address** [ **mask** | **mask-length** ] [ ****route-policy**** **route-policy-name** ]
   
   
   
   The device is configured to advertise the route of a loopback interface. After the command is run, the route of the loopback interface is advertised as a labeled route along the path corresponding to a BGP LSP, and the BGP LSP is established.
7. (Optional) Run **[**peer**](cmdqueryname=peer+next-hop-local)** { *ipv4-address* | *group-name* } ****next-hop-local****
   
   
   
   The device is configured to set the next hop to its IP address when advertising routes to a specified IBGP peer or peer group.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the **[**display bgp labeled peer**](cmdqueryname=display+bgp+labeled+peer)** command to check information about BGP-LU peers and their status.
* Run the [**display bgp labeled routing-table**](cmdqueryname=display+bgp+labeled+routing-table) command to check BGP-LU routing information.
* Run the **[**display bgp labeled routing-table statistics**](cmdqueryname=display+bgp+labeled+routing-table+statistics)** command to check statistics about BGP-LU routes.