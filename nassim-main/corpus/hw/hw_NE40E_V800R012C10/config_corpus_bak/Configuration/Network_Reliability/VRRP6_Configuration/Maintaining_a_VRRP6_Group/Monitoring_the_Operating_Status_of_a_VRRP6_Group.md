Monitoring the Operating Status of a VRRP6 Group
================================================

By monitoring the operating status of a VRRP6 group, you can understand the information about the VRRP6 group during the operation.

#### Context

During routine maintenance, you can perform the following operation to view the operating status of a VRRP6 group:


#### Procedure

* Run the [**display vrrp6**](cmdqueryname=display+vrrp6) [ **interface** *interface-type* *interface-number* ] [ **vrid** *virtual-router-id* ] **statistics** command in any view to check the statistics of VRRP6 Advertisement packets sent and received by a VRRP6 group.
* Run the [**display vrrp6 binding admin-vrrp6**](cmdqueryname=display+vrrp6+binding+admin-vrrp6) [ **interface** *interface-type1* *interface-number1* ] [ **vrid** *virtual-router-id1* ] [ **member-vrrp** [ **interface** *interface-type2* *interface-number2* ] [ **vrid** *virtual-router-id2* ] ] command to check the mapping between the mVRRP6 backup groups and service VRRP6 backup groups.