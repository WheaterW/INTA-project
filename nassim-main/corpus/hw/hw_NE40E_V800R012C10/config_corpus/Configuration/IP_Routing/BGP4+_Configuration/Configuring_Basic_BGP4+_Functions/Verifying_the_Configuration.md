Verifying the Configuration
===========================

After configuring basic BGP4+ functions, verify BGP4+ peer information.

#### Prerequisites

Basic BGP4+ functions have been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **ipv6** [**peer**](cmdqueryname=peer) **verbose** command to check information about all BGP4+ peers.
* Run the [**display bgp**](cmdqueryname=display+bgp) **ipv6** [**peer**](cmdqueryname=peer) *ipv6-address* { **log-info** | **verbose** } command to check information about a specified BGP4+ peer.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) [ *ipv6-address* *prefix-length* ] command to check information about BGP4+ routes.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+as-path-filter) **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } command to check information about the routes that match the specified AS\_Path filter.