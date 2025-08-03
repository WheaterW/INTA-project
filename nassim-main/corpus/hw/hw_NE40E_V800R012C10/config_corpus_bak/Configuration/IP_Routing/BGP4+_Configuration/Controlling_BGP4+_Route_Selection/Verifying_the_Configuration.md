Verifying the Configuration
===========================

After configuring BGP4+ route attributes, verify information about the route attributes.

#### Prerequisites

BGP4+ route attributes have been configured.


#### Procedure

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+different-origin-as) **different-origin-as** command to check the routes with different origin ASs.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+regular-expression) **regular-expression** *as-regular-expression* command to check the routes that match the AS regular expression.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+community+internet+no-advertise) **community** [ *aa:nn* &<1-33> ] [ **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] \* [ **whole-match** ] command to check the routes carrying the specified BGP4+ community attribute.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+community-filter+whole-match) **community-filter** { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check the routes that match the specified BGP4+ community filter.