Resetting BGP4+ Connections
===========================

Resetting BGP4+ connections interrupts peer relationships.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The BGP peer relationship between Routers is torn down if the [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** command is run to reset the BGP4+ connection. Exercise caution when resetting BGP connections.

When a BGP4+ routing policy (the Router does not support the route-refresh capability) is changed, reset BGP connections so that the new configuration can take effect. To reset BGP4+ connections, run any of the following commands in the user view:


#### Procedure

* To reset all BGP4+ connections, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv6+all) **ipv6** **all** command in the user view.
* To reset BGP4+ connections with a specified AS, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** *as-number* command in the user view.
* To reset the BGP4+ connection with a specified peer, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** { *ipv4-address* | *ipv6-address* } command in the user view.
* To reset all external BGP4+ connections, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv6+external) **ipv6** **external** command in the user view.
* To reset all internal BGP4+ connections, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv6+internal) **ipv6** **internal** command in the user view.
* To reset the BGP4+ connection with a specified slow peer, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv6+slow-peer) ****ipv6**** [ **ipv6-address** ] **slow-peer** command in the user view.