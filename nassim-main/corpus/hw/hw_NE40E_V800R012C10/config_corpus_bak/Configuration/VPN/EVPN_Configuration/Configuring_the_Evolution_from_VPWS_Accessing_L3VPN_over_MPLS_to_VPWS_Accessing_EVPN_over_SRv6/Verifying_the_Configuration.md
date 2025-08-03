Verifying the Configuration
===========================

After the evolution from VPWS accessing L3VPN over MPLS to VPWS accessing EVPN over SRv6, you can check EVPN IP prefix route information on the ASGs and RSGs.

#### Prerequisites

The evolution from VPWS accessing L3VPN over MPLS to VPWS accessing EVPN over SRv6 has been configured.


#### Procedure

* Run the [**display bgp evpn all routing-table prefix-route**](cmdqueryname=display+bgp+evpn+routing-table) command to check information about EVPN IP prefix routes.