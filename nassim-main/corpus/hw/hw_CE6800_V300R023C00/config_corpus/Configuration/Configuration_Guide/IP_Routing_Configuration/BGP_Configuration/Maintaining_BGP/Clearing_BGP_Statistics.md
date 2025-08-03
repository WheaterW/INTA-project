Clearing BGP Statistics
=======================

Clearing BGP Statistics

#### Context

This section describes how to clear statistics about flapping and dampened routes.

![](public_sys-resources/notice_3.0-en-us.png) 

BGP statistics cannot be restored after being cleared. Therefore, exercise caution when performing this operation.

To clear BGP statistics, run the following reset commands in the user view.

**Table 1** Clearing BGP statistics
| Operation | Command |
| --- | --- |
| Clear statistics about flapping routes. | [**reset bgp flap-info**](cmdqueryname=reset+bgp+flap-info+regexp+as-path-filter) [ **regexp** *as-path-regexp* | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *ipv4-address* [ *mask* | *mask-length* ] ] |
| Clear statistics about flapping routes of a specified peer. | [**reset bgp**](cmdqueryname=reset+bgp) *ipv4-address* [**flap-info**](cmdqueryname=flap-info) |
| Clear statistics about dampened routes and release dampened routes. | [**reset bgp dampening**](cmdqueryname=reset+bgp+dampening) [ *ipv4-address* [ *mask* | *mask-length* ] ] |