Verifying the Configuration of Route Reflection for BGP VPNv6 Routes
====================================================================

After configuring route reflection for BGP VPNv6 routes,
check information about VPNv6 peers and VPNv6 routes on the RR or
its client PEs.

#### Prerequisites

Route reflection for BGP VPNv6 routes has been configured.
#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** **all** **peer** [
  [ *ipv4-address* ] **verbose** ] command on the RR or a client PE to check information about BGP
  VPNv6 peers.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) **all** **routing-table** **peer** *peer-ipv4-address* { **advertised-routes** | **received-routes** } [ **statistics** ] command on the RR or
  a client PE to check VPNv6 routes received from the peer or advertised
  to the peer.
* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** **all** **group** [ *group-name* ] command on the RR to check information about
  the VPNv6 peer group.