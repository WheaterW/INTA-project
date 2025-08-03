Verifying the Configuration
===========================

After an L2VPN accesses multiple L3VPNs through VLAN tag termination sub-interfaces, you can view the binding relationships between the VE interfaces and VE group as well as termination information on VE sub-interfaces.

#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check the binding relationship between the VE interfaces and VE group.
* Run the [**display dot1q information termination**](cmdqueryname=display+dot1q+information+termination) [ **interface** *interface-type* *interface-number* [.*subinterface-number* ] ] command to check dot1q VLAN tag termination information.
* Run the [**display qinq information termination**](cmdqueryname=display+qinq+information+termination) [ **interface** **virtual-ethernet** *interface-number*.*subinterface-number* ] command to check QinQ VLAN tag termination information on a VE sub-interface.