Verifying the Configuration
===========================

After the configurations for controlling BGP route advertisement and acceptance are configured, you can view information about the configured filters, routes that match the specified filter, routes advertised to peers, and the imported routes that match the specified filter.

#### Prerequisites

All configurations for controlling BGP route advertisement and acceptance have been completed.


#### Procedure

* Run the [**display ip as-path-filter**](cmdqueryname=display+ip+as-path-filter) [ *as-path-filter-number* | *as-path-filter-name* ] command to check information about a configured AS\_Path filter.
* Run the [**display ip community-filter**](cmdqueryname=display+ip+community-filter) [ *basic-comm-filter-num* | *adv-comm-filter-num* | *comm-filter-name* ] command to check information about a configured community filter.
* Run the [**display ip extcommunity-filter**](cmdqueryname=display+ip+extcommunity-filter) [ *basic-extcomm-filter-num* | *advanced-extcomm-filter-num* | *extcomm-filter-name* ] command to check the VPN-Target extended community filter information.
* Run the [**display ip extcommunity-list soo**](cmdqueryname=display+ip+extcommunity-list+soo) [ *extcomm-filter-name* ] command to check SoO extended community filter information.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+as-path-filter) **as-path-filter** *as-path-filter-number* command to check information about routes matching a specified AS\_Path filter.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+community-filter+whole-match) **community-filter** { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] command to check information about routes matching a specified BGP community filter.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+peer+advertised-routes+statistics) **peer** *ipv4-address* **advertised-routes** [ **statistics** ] command to check information about routes advertised by a BGP device to the specified peer.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+peer+received-routes+active+statistics) **peer** *ipv4-address* **received-routes** [ **active** ] [ **statistics** ] command to check information about routes received by a BGP device from the specified peer.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+peer+received-routes) **peer** *ipv4-address* **received-routes** *network* { *mask* | *mask-length* } **original-attributes** command to check information about the original attributes of the routes received from the specified peer.