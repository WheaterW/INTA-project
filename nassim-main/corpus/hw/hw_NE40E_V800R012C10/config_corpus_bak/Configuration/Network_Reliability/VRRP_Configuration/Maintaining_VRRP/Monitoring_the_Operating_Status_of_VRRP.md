Monitoring the Operating Status of VRRP
=======================================

By monitoring the operating status of the Virtual Router Redundancy Protocol (VRRP), you can view information about VRRP during the operation.

#### Context

During routine maintenance, you can perform the following operations to view the operating status of VRRP:


#### Procedure

* Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** *interface-type* *interface-number* [ *virtual-router-id* ] ] [ **brief** ] command in any view to check the status and configurations of a VRRP group.
* Run the [**display vrrp binding admin-vrrp**](cmdqueryname=display+vrrp+binding+admin-vrrp) [ **interface** *interface-type* *interface-number* ] [ **vrid** *virtual-router-id* ] command to check all binding relationships configured for an mVRRP group.
* Run the [**display vrrp binding admin-vrrp**](cmdqueryname=display+vrrp+binding+admin-vrrp) [ **interface** *interface-type1* *interface-number1* ] [ **vrid** *virtual-router-id1* ] **member-vrrp** [ **interface** *interface-type2* *interface-number2* ] [ **vrid** *virtual-router-id2* ] command to check bindings between an mVRRP group and service VRRP groups.
* Run the **[**display vrrp admin-vrrp**](cmdqueryname=display+vrrp+admin-vrrp)** command to check information about all mVRRP groups configured on the device and their status.
* Run the **[**display vrrp protocol-information**](cmdqueryname=display+vrrp+protocol-information)** command to check VRRP information.