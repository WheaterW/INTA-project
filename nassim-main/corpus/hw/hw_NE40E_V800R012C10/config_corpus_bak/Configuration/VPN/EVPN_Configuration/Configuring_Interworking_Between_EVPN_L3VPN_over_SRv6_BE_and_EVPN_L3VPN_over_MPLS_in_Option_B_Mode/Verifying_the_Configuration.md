Verifying the Configuration
===========================

After configuring interworking between EVPN L3VPN over SRv6 BE and EVPN L3VPN over MPLS in Option B mode, check information about EVPN routes on PEs or ASBRs and the status of all BGP peer relationships.

#### Prerequisites

Interworking between EVPN L3VPN over SRv6 BE and EVPN L3VPN over MPLS in Option B mode has been configured.


#### Procedure

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **all** **routing-table** **prefix-route** *prefix* command to check EVPN IP prefix route information.