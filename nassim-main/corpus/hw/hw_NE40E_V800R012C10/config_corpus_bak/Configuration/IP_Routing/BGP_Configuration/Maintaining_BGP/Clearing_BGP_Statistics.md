Clearing BGP Statistics
=======================

This section describes how to clear BGP statistics about flapping routes and dampened routes.

#### Procedure

* To clear statistics about flapping routes, run the [**reset bgp flap-info**](cmdqueryname=reset+bgp+flap-info+ipv4) [ **regexp** *as-path-regexp* | **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *ipv4-address* [ *mask* | *mask-length* ] ] command in the user view.
  
  ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
  
  BGP statistics cannot be restored after being cleared. Therefore, exercise caution when running the command.
* To clear statistics about flapping routes of a specified peer, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv4+flap-info) *ipv4-address* [**flap-info**](cmdqueryname=flap-info) command in the user view.
* To clear statistics about dampened routes and release dampened routes, run the [**reset bgp dampening**](cmdqueryname=reset+bgp+dampening) [ *ipv4-address* [ *mask* | *mask-length* ] ] command in the user view.