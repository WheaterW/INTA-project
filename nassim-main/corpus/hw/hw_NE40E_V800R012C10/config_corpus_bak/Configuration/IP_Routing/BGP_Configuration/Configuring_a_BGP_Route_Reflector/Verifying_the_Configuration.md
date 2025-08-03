Verifying the Configuration
===========================

After configuring a BGP route reflector, verify information about BGP routes and BGP peer groups.

#### Prerequisites

A BGP route reflector has been configured.
#### Procedure

* Run the [**display bgp group**](cmdqueryname=display+bgp+group) [ *group-name* ] command to check information about peer groups.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+longer-prefixes) [ *network* ] [ *mask* | *mask-length* ] [ **longer-prefixes** ] command to check information about the BGP routing table.