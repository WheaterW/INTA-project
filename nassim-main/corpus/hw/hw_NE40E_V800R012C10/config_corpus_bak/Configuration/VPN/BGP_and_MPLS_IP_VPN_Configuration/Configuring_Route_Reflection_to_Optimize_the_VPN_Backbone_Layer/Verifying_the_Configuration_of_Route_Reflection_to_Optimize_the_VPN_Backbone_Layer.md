Verifying the Configuration of Route Reflection to Optimize the VPN Backbone Layer
==================================================================================

After configuring route reflection to optimize the VPN
backbone layer, check BGP VPNv4 peer information and VPNv4 routing
information on the RR or its client PEs.

#### Prerequisites

Route reflection has been configured.
#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv4** **all** **peer** [
  [ *ipv4-address* ] **verbose** ] command on the RR or a client PE to check information about BGP
  VPNv4 peers.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) **all** **routing-table** **peer** *peer-ipv4-address* { **advertised-routes** | **received-routes** } [ **statistics** ] command on the RR or
  client PE to view information about the routes received from the peer
  or the routes advertised to the peer.