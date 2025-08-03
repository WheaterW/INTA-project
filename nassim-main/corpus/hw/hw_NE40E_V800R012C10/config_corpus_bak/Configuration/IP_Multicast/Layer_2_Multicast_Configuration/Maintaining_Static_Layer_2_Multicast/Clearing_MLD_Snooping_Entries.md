Clearing MLD Snooping Entries
=============================

Clear MLD snooping entries if they are not needed.

#### Usage Scenario

Clearing MLD snooping entries in a VLAN or VSI may interrupt services.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After the entries are cleared, hosts in the VLAN or VSI may fail to receive multicast traffic until the device re-generates forwarding entries upon reception of the MLD Report messages sent by the hosts.



#### Procedure

* To clear dynamic MLD snooping entries, run the [**reset mld-snooping group**](cmdqueryname=reset+mld-snooping+group) { **vlan** { *vlan-id* | **all** } | **vsi** { **name** *vsi-name* | **all** } | **all** } command in the user view.