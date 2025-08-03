Clearing Bidirectional Isolation Statistics About ARP Packets
=============================================================

This section describes how to clear ARP packet statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Be aware that statistics cannot be restored after being cleared. Exercise caution when clearing the statistics.



#### Procedure

* Run the [**reset arp-safeguard statistics**](cmdqueryname=reset+arp-safeguard+statistics) **slot** *slot-id* command in the user view to clear bidirectional isolation statistics about ARP packets.
* Run the [**reset arp-check**](cmdqueryname=reset+arp-check) { **check-destination-ip** | **check-valid** } **statistics** **slot** *slot-id* command in the user view to clear statistics about invalid ARP packets discarded by a specified interface board.
  
  
  
  In VS mode, this command is supported only by the admin VS.