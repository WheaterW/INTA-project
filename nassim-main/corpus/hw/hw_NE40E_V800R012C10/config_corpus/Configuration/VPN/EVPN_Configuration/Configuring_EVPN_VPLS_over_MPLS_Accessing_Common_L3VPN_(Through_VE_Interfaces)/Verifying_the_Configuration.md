Verifying the Configuration
===========================

After configuring EVPN VPLS over MPLS accessing common L3VPN, you can view binding between VE interfaces and the VE group and EVPN instance information.

#### Prerequisites

EVPN VPLS over MPLS accessing common L3VPN has been configured.


#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check the binding relationship between the VE interfaces and VE group.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] command to check EVPN instance information.