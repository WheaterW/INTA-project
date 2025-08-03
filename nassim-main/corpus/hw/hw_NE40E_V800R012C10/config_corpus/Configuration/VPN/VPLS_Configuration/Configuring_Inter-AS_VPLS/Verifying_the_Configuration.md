Verifying the Configuration
===========================

After configuring inter-AS VPLS, check VPLS VSI and connection information.

#### Prerequisites

Inter-AS VPLS has been configured.


#### Procedure

* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.
* Run the [**display bgp l2vpn-ad peer**](cmdqueryname=display+bgp+l2vpn-ad+peer) [ [ *ipv4-address* ] **verbose** ] command to check the BGP VPLS peer relationship on the PE or ASBR.
* Run the [**display vpls connection**](cmdqueryname=display+vpls+connection) [ **bgp** | **vsi** *vsi-name* ] [ **down** | **up** ] [ **verbose** ] command to check the VPLS connection status on the PE.
* Run the [**display bgp routing-table label**](cmdqueryname=display+bgp+routing-table+label) command to check information about labeled IPv4 routes on the PE or ASBR.
* Run the [**display vsi bgp-ad remote**](cmdqueryname=display+vsi+bgp-ad+remote) **vpls-id** *vpls-id* command to check information about a specified remote PE.