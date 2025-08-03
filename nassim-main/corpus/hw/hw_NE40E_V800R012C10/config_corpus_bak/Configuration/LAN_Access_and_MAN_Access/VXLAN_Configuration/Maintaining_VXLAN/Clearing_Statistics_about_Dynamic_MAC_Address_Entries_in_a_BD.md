Clearing Statistics about Dynamic MAC Address Entries in a BD
=============================================================

To view dynamic MAC address entries in a BD within a specified period of time, clear existing dynamic MAC address entry information before starting statistics collection to ensure information accuracy.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Statistics about dynamic MAC address entries in a BD cannot be restored after they are cleared. Exercise caution when running the reset command.



#### Procedure

* Run the [**reset mac-address bridge-domain**](cmdqueryname=reset+mac-address+bridge-domain) *bd-id* command in the user view to clear statistics about dynamic MAC address entries in a BD.