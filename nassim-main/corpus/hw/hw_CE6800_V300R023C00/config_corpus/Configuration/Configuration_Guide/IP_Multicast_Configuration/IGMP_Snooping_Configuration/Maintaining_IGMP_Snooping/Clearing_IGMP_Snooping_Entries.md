Clearing IGMP Snooping Entries
==============================

Clearing IGMP Snooping Entries

#### Context

Different methods are used to clear static and dynamic IGMP snooping entries.

![](../public_sys-resources/notice_3.0-en-us.png) 

Static entries cannot be restored after being cleared. They can be created only when you run commands to configure static member ports.

Hosts in a VLAN will fail to receive any multicast flows that depend on cleared dynamic entries. This problem is resolved after the hosts send IGMP Report messages and the device generates forwarding entries again.



#### Procedure

* Run the [**undo igmp snooping static-group**](cmdqueryname=undo+igmp+snooping+static-group) [ **source-address** *source-ip-address* ] **group-address** *group-ip-address* **vlan** { **all** | { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> } command in the interface view to delete a multicast group address statically added to an interface.
  
  
  
  You can also run one of the following commands to delete multiple multicast group addresses added to an interface in a batch.
  
  + [**undo igmp snooping static-group**](cmdqueryname=undo+igmp+snooping+static-group) [ **source-address** *source-ip-address* ] **group-address** *group-ip-address1* **to** *group-ip-address2* **vlan** *vlan-id*
  + [**undo igmp snooping static-group**](cmdqueryname=undo+igmp+snooping+static-group) [ **source-address** *source-ip-address* ] **group-address** **all** **vlan** { **all** | { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }
* Run the [**reset igmp snooping group**](cmdqueryname=reset+igmp+snooping+group) { **all** | **vlan** { **all** | *vlan-id* } } command in the user view to clear dynamic group entries.
* Run the [**reset igmp snooping qinq-group interface**](cmdqueryname=reset+igmp+snooping+qinq-group+interface) *interface-type* *interface-number.subinterface-number* [ **pe-vid** *pe-vid* [ *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] [ *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] ] ] ] command in the user view to clear port entries of multicast groups on a Layer 3 sub-interface.