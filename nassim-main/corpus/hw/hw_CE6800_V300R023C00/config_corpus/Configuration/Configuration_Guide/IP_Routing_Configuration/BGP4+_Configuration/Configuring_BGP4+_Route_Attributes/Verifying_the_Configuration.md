Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) **different-origin-as** command to check BGP4+ routes with different origin AS numbers.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) **regular-expression** *as-regular-expression* command to check BGP4+ routes matching an AS regular expression.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33> command to check routing information of a specified BGP4+ community.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) **community-filter** { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check routes matching the specified BGP4+ community filter.