Verifying the Configuration
===========================

After configuring BGP route selection, verify information about route attributes.

#### Prerequisites

BGP route attributes have been configured.


#### Procedure

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+different-origin-as) **different-origin-as** command to check the routes with different origin ASs but the same destination address.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+regular-expression) **regular-expression** *as-regular-expression* command to check the routes matching the specified AS regular expression.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+longer-prefixes) [ *network* ] [ *mask* | *mask-length* ] [ **longer-prefixes** ] command to check information about the BGP routing table.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+community+internet+no-advertise) **community** [ *community-number* | *aa:nn* ] &<1-13> [ **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] \* [ **whole-match** ] command to check the routes with a specified BGP community attribute.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+community-filter+whole-match) **community-filter** { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check the routes matching a specified BGP community filter.