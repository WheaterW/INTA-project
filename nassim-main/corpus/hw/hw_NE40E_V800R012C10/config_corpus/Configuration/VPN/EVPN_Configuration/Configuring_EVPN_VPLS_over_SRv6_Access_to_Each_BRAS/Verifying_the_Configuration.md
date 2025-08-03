Verifying the Configuration
===========================

After configuring EVPN VPLS over SRv6 accessing BRAS, verify the binding between the VE interface and VE group and EVPN route information on each vBRAS-pUP.

#### Prerequisites

EVPN VPLS over SRv6 accessing BRAS has been configured.


#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check the binding relationship between the VE interfaces and VE group.
* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command to check EVPN route information.