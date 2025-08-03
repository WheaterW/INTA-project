Verifying the Configuration
===========================

After configuring the BGP Large-Community attribute, verify the configuration.

#### Prerequisites

All configurations of the BGP Large-Community attribute have been performed.


#### Procedure

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *network* [ *mask* | *mask-length* ] command to check detailed information about a specified BGP route.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+large-community+whole-match) **large-community** [*aa:bb:cc* ] &<1-33> [ **whole-match** ] command to check information about the routes with the specified BGP Large-Community attribute.