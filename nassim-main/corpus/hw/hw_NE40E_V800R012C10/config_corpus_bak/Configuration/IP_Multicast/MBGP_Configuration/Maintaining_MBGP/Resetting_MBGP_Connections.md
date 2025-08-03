Resetting MBGP Connections
==========================

Resetting MBGP connections tears down peer relationships.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

MBGP peer relationships between Routers are torn down if you reset MBGP connections by using the [**reset bgp multicast**](cmdqueryname=reset+bgp+multicast) command. Exercise caution when resetting MBGP connections.



#### Procedure

* To reset the MBGP connection between specified peers, run the [**reset bgp multicast**](cmdqueryname=reset+bgp+multicast) *peer-address* command in the user view.
* To reset all MBGP connections, run the [**reset bgp multicast**](cmdqueryname=reset+bgp+multicast) **all** command in the user view.
* To reset the MBGP connections between all peers in a peer group, run the [**reset bgp multicast**](cmdqueryname=reset+bgp+multicast) **group** *group-name* command in the user view.
* To reset external connections, run the [**reset bgp multicast external**](cmdqueryname=reset+bgp+multicast+external) command in the user view.
* To reset internal connections, run the [**reset bgp multicast internal**](cmdqueryname=reset+bgp+multicast+internal) command in the user view.
* To reset the connections to slow MBGP peers on the public network, run the [**reset bgp multicast**](cmdqueryname=reset+bgp+multicast) [ *peerIpv4Addr* ] **slow-peer** command in the user view.
* To reset the connections to slow MBGP peers in a VPN, run the [**reset bgp**](cmdqueryname=reset+bgp) **vpn-instance** *vpn-instance-name* **multicast** [ *peerIpv4Addr* ] **slow-peer** command in the user view.