Resetting BGP Connections
=========================

Resetting BGP Connections

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Running the [**reset bgp**](cmdqueryname=reset+bgp) command to reset BGP connections disconnects the BGP peer relationships between devices. Exercise caution when resetting BGP connections.

If a BGP route-policy changes and the device does not support route-refresh, you can reset BGP connections for the new configuration to take effect.

To reset BGP connections, run the following reset commands in the user view.

**Table 1** Resetting BGP connections
| Operation | Command |
| --- | --- |
| Reset all BGP connections. | [**reset bgp**](cmdqueryname=reset++bgp) **all** |
| Reset BGP connections with a specified AS. | [**reset bgp**](cmdqueryname=reset++bgp) *as-number* |
| Reset BGP connections with a specified peer. | [**reset bgp**](cmdqueryname=reset++bgp) *ipv4-address* |
| Reset all EBGP connections. | [**reset bgp**](cmdqueryname=reset+bgp+external) **external** |
| Reset BGP connections with a specified peer group. | [**reset bgp**](cmdqueryname=reset+bgp+group) **group** *group-name* |
| Reset all IBGP connections. | [**reset bgp**](cmdqueryname=reset+bgp+internal) **internal** |
| Reset the BGP connection with a specified slow peer. | [**reset bgp**](cmdqueryname=reset+bgp+ipv4+slow-peer) ****ipv4**** [ **ipv4-address** | **ipv6-address** ] **slow-peer** |
| Reset the flapping count of a specified BGP peer. | [**reset bgp**](cmdqueryname=reset+bgp+flapping-count) *ipv4-address* **flapping-count** |