Clearing MLD Snooping Entries
=============================

Clearing MLD Snooping Entries

#### Context

MLD snooping entries are classified into static entries and dynamic entries. The methods of clearing the two types of entries are different.

![](../public_sys-resources/notice_3.0-en-us.png) 

After static entries are cleared, they cannot be automatically restored until static member ports are configured using commands again.

If dynamic entries are cleared, hosts in a VLAN will temporarily fail to receive the multicast traffic that depends on the entries. This problem persists until hosts send MLD Report messages and the device generates forwarding entries again.



#### Procedure

* Run the [**undo mld snooping static-group**](cmdqueryname=undo+mld+snooping+static-group) [ **source-address** *source-ip-address* ] **group-address** *group-ip-address* **vlan** { **all** | { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> } command in the interface view to delete a multicast group address statically added to an interface.
  
  
  
  You can also run one of the following commands to delete multiple multicast group addresses added to an interface in a batch.
  
  + [**undo mld snooping static-group**](cmdqueryname=undo+mld+snooping+static-group) [ **source-address** *source-ip-address* ] **group-address** *group-ip-address1* **to** *group-ip-address2* **vlan** *vlan-id*
  + [**undo mld snooping static-group**](cmdqueryname=undo+mld+snooping+static-group) [ **source-address** *source-ip-address* ] **group-address** **all** **vlan** { **all** | { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }
* Run the [**reset mld snooping group**](cmdqueryname=reset+mld+snooping+group) { **all** | **vlan** { **all** | *vlan-id* } } command in the user view to clear dynamic group entries.