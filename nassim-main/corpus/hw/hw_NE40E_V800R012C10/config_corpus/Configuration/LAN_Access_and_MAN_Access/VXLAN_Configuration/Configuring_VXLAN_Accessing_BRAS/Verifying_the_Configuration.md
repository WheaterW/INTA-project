Verifying the Configuration
===========================

After configuring VXLAN accessing BRAS, you can view binding between the VE interfaces and VE group and VXLAN tunnel information on the pUP.

#### Prerequisites

VXLAN accessing BRAS has been configured.


#### Procedure

1. Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check binding between the VE interfaces and VE group.
2. Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check VXLAN tunnel information.