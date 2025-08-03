Verifying the Configuration of MBGP Route Advertisement
=======================================================

After configuring MBGP route advertisement, verify MBGP routing information.

#### Prerequisites

The policy for controlling MBGP route advertisement has been configured.


#### Procedure

* Run the [**display bgp multicast routing-table community**](cmdqueryname=display+bgp+multicast+routing-table+community) [ *aa:nn* ] [ **no-advertise** | **no-export** | **no-export-subconfed** ] \* & <1-33> [ **whole-match** ] command to check routes that carry the specified MBGP community attribute.
* Run the [**display bgp multicast routing-table community-filter**](cmdqueryname=display+bgp+multicast+routing-table+community-filter) { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check the routes that match the MBGP community filter.
* Run the [**display bgp multicast network**](cmdqueryname=display+bgp+multicast+network) command to check routing information advertised by MBGP.
* Run the [**display bgp multicast routing-table**](cmdqueryname=display+bgp+multicast+routing-table) command to check the MBGP routing table.
* Run the [**display bgp multicast routing-table cidr**](cmdqueryname=display+bgp+multicast+routing-table+cidr) command to check Classless InterDomain Routing (CIDR) information.
* Run the [**display bgp multicast routing-table statistics**](cmdqueryname=display+bgp+multicast+routing-table+statistics) command to check statistics about entries in the MBGP routing table.