Resetting BGP Connections
=========================

Resetting a BGP connection will interrupt peer relationships.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The BGP peer relationship between Routers is interrupted after the BGP connection is reset using the [**reset bgp**](cmdqueryname=reset+bgp) command. Exercise caution when resetting BGP connections.

When the BGP routing policy on the Router that does not support the route-refresh capability changes, you need to reset BGP connections so that the change can take effect. To reset BGP connections, run the following reset commands in the user view:


#### Procedure

* To reset all BGP connections, run the [**reset bgp**](cmdqueryname=reset+bgp+all) **all** command.
* To reset BGP connections with a specified AS, run the [**reset bgp**](cmdqueryname=reset+bgp) *as-number* command.
* To reset BGP connections with a specified peer, run the [**reset bgp**](cmdqueryname=reset+bgp) *ipv4-address* command.
* To reset all EBGP connections, run the [**reset bgp**](cmdqueryname=reset+bgp+external) **external** command.
* To reset BGP connections with a specified peer group, run the [**reset bgp**](cmdqueryname=reset+bgp+group) **group** *group-name* command.
* To reset all IBGP connections, run the [**reset bgp**](cmdqueryname=reset+bgp+internal) **internal** command in the user view.
* To reset the BGP connection with a specified slow peer, run the [**reset bgp**](cmdqueryname=reset+bgp+ipv4+slow-peer) ****ipv4**** **ipv4-address** **slow-peer** command in the user view.