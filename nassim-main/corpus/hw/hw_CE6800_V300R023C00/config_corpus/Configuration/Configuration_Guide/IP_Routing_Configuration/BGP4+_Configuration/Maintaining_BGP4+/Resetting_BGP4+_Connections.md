Resetting BGP4+ Connections
===========================

Resetting BGP4+ Connections

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Running the [**reset bgp**](cmdqueryname=reset+bgp) **ipv6** command to reset BGP4+ connections disconnects the BGP4+ peer relationships between devices. Therefore, exercise caution when running the command.

If a BGP4+ route-policy changes and the device does not support route-refresh, you can reset BGP4+ connections for the new configuration to take effect.

To reset BGP4+ connections, run the following reset commands in the user view.

**Table 1** Resetting BGP4+ connections
| Operation | Command |
| --- | --- |
| Reset all BGP4+ connections. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6+all) **ipv6** **all** |
| Reset BGP4+ connections with a specified AS. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** *as-number* |
| Reset BGP4+ connections with a specified peer. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6) **ipv6** *ipv6-address* |
| Reset all EBGP connections. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6+external) **ipv6** **external** |
| Reset BGP4+ connections with a specified peer group. | [**reset bgp ipv6**](cmdqueryname=reset+bgp+ipv6+group) **group** *group-name* |
| Reset all IBGP connections. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6+internal) **ipv6** **internal** |
| Reset the BGP4+ connection with a specified slow peer. | [**reset bgp**](cmdqueryname=reset+bgp+ipv6+slow-peer) ****ipv6**** [ *ipv6-address* ] **slow-peer** |