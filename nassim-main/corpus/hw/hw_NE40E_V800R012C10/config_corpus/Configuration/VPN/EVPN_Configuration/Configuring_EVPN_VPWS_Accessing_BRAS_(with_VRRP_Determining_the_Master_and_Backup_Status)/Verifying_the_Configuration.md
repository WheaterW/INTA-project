Verifying the Configuration
===========================

After configuring EVPN VPWS accessing BRAS, you can check binding between the VE interfaces and VE group, VRRP or VRRP6 group status, and information about the specified EVPL instance on each BNG.

#### Prerequisites

EVPN VPWS accessing BRAS has been configured.


#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check binding between the VE interfaces and VE group.
* Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** *interface-type* *interface-number* [ *virtual-router-id* ] ] [ **brief** ] command to check VRRP group status.
* Run the [**display vrrp6**](cmdqueryname=display+vrrp6) [ **interface** *interface-type* *interface-number* [ **vrid** *virtual-router-id* ] ] [ **brief** ] command to check VRRP6 group status.
* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) **instance-id** *instance-id* command to check information about the specified EVPL instance.