Verifying the Configuration
===========================

After configuring BGP VPLS, check local and remote VSI and VPLS connection information.

#### Prerequisites

BGP VPLS has been configured.


#### Procedure

* Run the [**display vpls connection**](cmdqueryname=display+vpls+connection) [ **bgp** | **vsi** *vsi-name* ] [ **down** | **up** ] [ **verbose** ] command to check VPLS connection information.
* Run the [**display vsi remote**](cmdqueryname=display+vsi+remote) **bgp** [ **nexthop** *nexthop-address* [ **export-vpn-target** *vpn-target* ] | **route-distinguisher** *route-distinguisher* ] command to check remote VSI information.
* Run the [**display bgp l2vpn-ad routing-table vpls**](cmdqueryname=display+bgp+l2vpn-ad+routing-table+vpls) command to check information about VPLS routes in the L2VPN-AD address family.