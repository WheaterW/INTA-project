Verifying the Configuration
===========================

After configuring EVPN VPWS over MPLS accessing BRAS, check the binding relationships between the VE interfaces and VE group and information about the specified EVPL instance on each BNG.

#### Prerequisites

EVPN VPWS over MPLS accessing BRAS has been configured.


#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check binding between the VE interfaces and VE group.
* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) **instance-id** *instance-id* command to check information about the specified EVPL instance.