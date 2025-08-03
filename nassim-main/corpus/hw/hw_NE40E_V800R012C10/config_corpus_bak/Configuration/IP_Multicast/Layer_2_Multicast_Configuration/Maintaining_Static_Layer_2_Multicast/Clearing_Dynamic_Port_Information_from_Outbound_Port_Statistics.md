Clearing Dynamic Port Information from Outbound Port Statistics
===============================================================

Clearing multicast entries in a VLAN or VSI will cause a traffic interruption.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If you run this command to clear dynamic ports in the outbound port information, hosts in the VLAN or VSI cannot receive multicast traffic until outbound port information is generated again on the Router. Exercise caution while performing this operation.



#### Procedure

* Run the [**reset igmp-snooping group**](cmdqueryname=reset+igmp-snooping+group) { **vlan** { *vlan-id* | **all** } | **vsi** { **name** *vsi-name* | **all** } | **bridge-domain** { *bd-id* | **all** } | **all** } command in the user view to clear dynamic port information from outbound port statistics.