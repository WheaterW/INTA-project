Clearing BGP4+ Statistics
=========================

Clearing BGP4+ Statistics

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

BGP4+ statistics cannot be restored after being cleared. Therefore, exercise caution when performing this operation.

To clear BGP4+ statistics, run the following reset commands in the user view.

**Table 1** Clearing BGP4+ statistics
| Operation | Command |
| --- | --- |
| Clear statistics about BGP4+ flapping routes. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** [**flap-info**](cmdqueryname=flap-info+regexp+as-path-filter) [ **regexp** *as-path-regexp* | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *ipv6-address* *prefix-length* ] |
| Clear statistics about flapping routes of a specified BGP4+ peer. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** *ipv6-address* [**flap-info**](cmdqueryname=flap-info) |
| Clear statistics about BGP4+ dampened routes and release BGP4+ dampened routes. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** [**dampening**](cmdqueryname=dampening) [ *ipv6-address* *prefix-length* ] |