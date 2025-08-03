Verifying the Configuration
===========================

After configuring VPLS accessing public network or L3VPN, check the binding relationship between the VE interfaces and VE group and VPLS VSI information.

#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check the binding relationship between the VE interfaces and VE group.
* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.