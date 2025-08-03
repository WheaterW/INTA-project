Verifying the mVRRP Group Configuration
=======================================

You can view the status of an mVRRP group and verify the configuration.

#### Prerequisites

An mVRRP group has been configured.


#### Procedure

* Run the [**display vrrp binding admin-vrrp**](cmdqueryname=display+vrrp+binding+admin-vrrp) [ **interface** *interface-type1* *interface-number1* ] [ **vrid** *virtual-router-id1* ] **member-vrrp** [ **interface** *interface-type2* *interface-number2* ] [ **vrid** *virtual-router-id2* ] command to check the bindings between an mVRRP group and service VRRP groups.
* Run the [**display vrrp binding admin-vrrp**](cmdqueryname=display+vrrp+binding+admin-vrrp) [ **interface** *interface-type1* *interface-number1* ] [ **vrid** *virtual-router-id* ] **member-interface** [ **interface** *interface-type2* *interface-number2* ] command to check the bindings between an mVRRP group and VRRP-disabled interfaces.
* Run the [**display mpls l2vc track admin-vrrp**](cmdqueryname=display+mpls+l2vc+track+admin-vrrp) [ **interface** *interface-type1* *interface-number1* **vrid** *virtual-router-id* ] command to check the bindings between an mVRRP group and service PWs.
* Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** *interface-type* *interface-number* [ *virtual-router-id* ] ] [ **brief** ] command to check brief information about all VRRP groups or a specific one.