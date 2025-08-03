Verifying the Configuration
===========================

After configuring BGP4+ routing policies, check routes that are advertised and received by BGP4+.

#### Prerequisites

The routing policies have been configured.


#### Procedure

* Run the [**display bgp ipv6 network**](cmdqueryname=display+bgp+ipv6+network) command to check the routes imported by BGP4+ using the [**network**](cmdqueryname=network) command.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+as-path-filter) **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } command to check information about the routes that match the specified AS\_Path filter.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+community-filter+whole-match) **community-filter** { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check the routes that match a specified BGP4+ community filter.
* Run the [**display ip extcommunity-filter**](cmdqueryname=display+ip+extcommunity-filter) [ *basic-extcomm-filter-num* | *advanced-extcomm-filter-num* | *extcomm-filter-name* ] command to check the VPN-Target extended community filter information.
* Run the [**display ip extcommunity-list soo**](cmdqueryname=display+ip+extcommunity-list+soo) [ *extcomm-filter-name* ] command to check SoO extended community filter information.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+peer+advertised-routes) **peer** **remoteIpv6Addr** { **advertised-routes** | **received-routes** } [ **statistics** ] command to view the routes advertised to or received from a specified BGP4+ peer.