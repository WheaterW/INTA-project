Maintaining NetStream
=====================

Maintaining NetStream

#### Context

During routine maintenance, you can delete NetStream statistics.

![](public_sys-resources/note_3.0-en-us.png) 

Statistics cannot be restored after being deleted. Exercise caution when deleting them.



#### Procedure

* Run the [**reset netstream statistics ip**](cmdqueryname=reset+netstream+statistics+ip) **slot** *slot-id* command in the user view to delete IPv4 flow statistics.
* Run the [**reset netstream statistics ipv6**](cmdqueryname=reset+netstream+statistics+ipv6) **slot** *slot-id* command in the user view to delete IPv6 flow statistics.
* Run the [**reset netstream statistics vxlan inner-ip**](cmdqueryname=reset+netstream+statistics+vxlan+inner-ip) **slot** *slot-id* command in the user view to delete VXLAN flexible flow statistics.