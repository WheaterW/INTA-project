Verifying the Configuration
===========================

Verifying the Configuration

#### Prerequisites

All configurations in this scenario are complete.


#### Procedure

* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **interface** *interface-type interface-number* ] command on a PE to check local VPWS connection information.
* Run the [**display mpls switch-l2vc**](cmdqueryname=display+mpls+switch-l2vc) [ *ip-address* *vc-id* **encapsulation** *encapsulation-type* | **state** { **down** | **up** } | **brief** ] command on the SPE to check VPWS switching information.
* Run the [**display mpls l2vc track admin-vrrp**](cmdqueryname=display+mpls+l2vc+track+admin-vrrp) [ **interface** *interface-type interface-number* **vrid** *virtual-router-id* ] command to check information about the PW bound to the mVRRP group.
* Run the [**display mpls l2vc track admin-vc**](cmdqueryname=display+mpls+l2vc+track+admin-vc) command to check information about service PWs bound to an mPW.