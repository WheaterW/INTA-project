Verifying the Configuration
===========================

After configuring BGP community attributes, verify the configured BGP community attributes.

#### Prerequisites

A BGP community attribute has been configured.


#### Procedure

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *network* [ *mask* | *mask-length* ] command to check detailed information about a specified BGP route.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+community+internet+no-advertise) **community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ] command to check information about routes with a specified BGP community attribute.