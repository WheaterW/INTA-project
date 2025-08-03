Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **different-origin-as** command to check routes with different origin AS numbers but the same destination address.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **regular-expression** *as-regular-expression* command to check information about routes matching an AS regular expression.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* ] [ *mask* | *mask-length* ] [ **longer-prefixes** ] command to check information about the BGP routing table.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **community** [ *community-number* | *aa:nn* ] &<1-13> [ **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] \* [ **whole-match** ] command to check information about routes matching the specified BGP community attribute.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) **community-filter** { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check information about routes matching the specified BGP community filter.