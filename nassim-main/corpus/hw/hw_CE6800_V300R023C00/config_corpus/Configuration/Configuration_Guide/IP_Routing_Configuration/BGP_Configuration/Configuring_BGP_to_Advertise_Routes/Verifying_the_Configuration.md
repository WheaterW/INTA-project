Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ip as-path-filter**](cmdqueryname=display+ip+as-path-filter) [ *as-path-filter-number* | *as-path-filter-name* ] command to check the AS\_Path filter information.
* Run the [**display ip community-filter**](cmdqueryname=display+ip+community-filter) [ *basic-comm-filter-num* | *adv-comm-filter-num* | *comm-filter-name* ] command to check the community filter information.
* Run the [**display ip extcommunity-filter**](cmdqueryname=display+ip+extcommunity-filter) [ *basic-extcomm-filter-num* | *advanced-extcomm-filter-num* | *extcomm-filter-name* ] command to check the VPN-Target extended community filter information.
* Run the [**display ip extcommunity-list soo**](cmdqueryname=display+ip+extcommunity-list+soo) [ *extcomm-filter-name* ] command to check the SoO extended community filter information.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **as-path-filter** *as-path-filter-number* command to check information about routes matching the specified AS\_Path filter.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **community-filter** { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check information about routes matching the specified BGP community filter.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **peer** *remoteIpv4Addr* **advertised-routes** [ **statistics** ] command to check information about routes advertised by the BGP device to a specified peer.