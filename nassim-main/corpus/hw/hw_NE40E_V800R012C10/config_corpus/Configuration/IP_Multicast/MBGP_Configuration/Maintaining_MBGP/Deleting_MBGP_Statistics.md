Deleting MBGP Statistics
========================

Deleting MBGP statistics involves deleting MBGP route flapping statistics and route dampening statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Deleted MBGP statistics cannot be restored. Therefore, exercise caution when deleting MBGP statistics.



#### Procedure

* To delete MBGP route dampening statistics, run the [**reset bgp multicast dampening**](cmdqueryname=reset+bgp+multicast+dampening) [ *ip-address* [ *mask* | *mask-length* ] ] command in the user view.
* To delete MBGP route flapping statistics, run the [**reset bgp multicast flap-info**](cmdqueryname=reset+bgp+multicast+flap-info) [ *ip-address* [ *mask*-length | *mask* ] | **as-path-filter** *as-path-list-number* | **regrexp** *regrexp* ] command in the user view.