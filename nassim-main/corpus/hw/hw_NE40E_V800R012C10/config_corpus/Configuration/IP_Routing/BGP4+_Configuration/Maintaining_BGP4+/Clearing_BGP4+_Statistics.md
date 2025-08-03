Clearing BGP4+ Statistics
=========================

Clearing BGP4+ statistics involves clearing route flapping statistics and route dampening statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

BGP4+ statistics cannot be restored after being cleared. Therefore, exercise caution when performing this operation.



#### Procedure

* To clear route flapping statistics, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv6+flap-info) **ipv6** [**flap-info**](cmdqueryname=flap-info+regexp+as-path-filter) [ **regexp** *as-path-regexp* | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *ipv6-address* *prefix-length* ] command in the user view.
* To clear route flapping statistics of a specified peer, run the [**reset bgp**](cmdqueryname=reset+bgp+flap-info+ipv6) **ipv6** *ipv6-address* [**flap-info**](cmdqueryname=flap-info) command in the user view.
* To clear route dampening information and release suppressed routes, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** [**dampening**](cmdqueryname=dampening) [ *ipv6-address* *prefix-length* ] command in the user view.