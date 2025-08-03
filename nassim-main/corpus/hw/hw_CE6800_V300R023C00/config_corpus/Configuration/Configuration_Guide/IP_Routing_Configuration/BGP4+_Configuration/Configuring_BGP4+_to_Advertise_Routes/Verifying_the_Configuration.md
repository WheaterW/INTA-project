Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display bgp ipv6 network**](cmdqueryname=display+bgp+ipv6+network) command to check the routes imported by BGP4+ using the [**network**](cmdqueryname=network) command.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } command to check routes matching the specified AS\_Path filter.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) **community-filter** { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check the routes matching the specified BGP4+ community filter.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) **peer** { *remoteIpv6Addr* | *remoteIpv4Addr* } { **advertised-routes** | **received-routes** } [ **statistics** ] command to check the routes advertised to or received from a specified BGP4+ peer.