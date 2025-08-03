Verifying the Configuration
===========================

After configuring EVPN VPLS over MPLS (inter-AS Option B), verify the status of all BGP peer relationships and EVPN routing information on PEs or ASBRs.

#### Prerequisites

EVPN VPLS over MPLS (inter-AS Option B) has been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **evpn** **peer** command on the PE or ASBR to check whether all BGP peer relationships are established.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **all** **routing-table** command on the PE or ASBR to check information about BGP EVPN routes.