Clearing Dual-Device Backup Information
=======================================

This section describes how to clear dual-device ARP hot backup information.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

* Dual-device ARP hot backup information cannot be restored after it is cleared. Therefore, exercise caution when running the [**reset arp remote-backup**](cmdqueryname=reset+arp+remote-backup) command.
* Running the [**reset remote-backup-service statistic**](cmdqueryname=reset+remote-backup-service+statistic) command deletes statistics about an RBS, and the deleted statistics cannot recover. Therefore, exercise caution when running this command.


#### Procedure

* Run the [**reset arp remote-backup**](cmdqueryname=reset+arp+remote-backup) { **interface** *interface-type* *interface-number* | **all** } command in the user view to clear the original backup ARP entries and back up ARP entries again.
* Run the [**reset remote-backup-service**](cmdqueryname=reset+remote-backup-service) [ *rbs-name* ] [**statistic**](cmdqueryname=statistic) command in the user view to clear statistics about a specified RBS.