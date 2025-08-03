Verifying the Configuration
===========================

After an L2VPN accesses multiple L2VPNs through sub-interfaces for VLAN tag termination, you can view the binding between the VE interfaces and VE group, and termination information on VE sub-interfaces.

#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check the binding between the VE interfaces and VE group.
* Run the [**display dot1q information termination**](cmdqueryname=display+dot1q+information+termination) [ **interface** *interface-type* *interface-number* [.*subinterface-number* ] ] command to check information about dot1q VLAN tag termination.
* Run the [**display qinq information termination**](cmdqueryname=display+qinq+information+termination) [ **interface virtual-ethernet** *interface-number*.*subinterface-number* ] command to check QinQ VLAN tag termination information on the VE sub-interface.