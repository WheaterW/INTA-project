Verifying the Configuration
===========================

After configuring VPLS accessing L2VPN, you can view the binding between the VE interfaces and VE group, and information about VPLS VSIs.

#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check the binding between the VE interfaces and VE group.
* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.