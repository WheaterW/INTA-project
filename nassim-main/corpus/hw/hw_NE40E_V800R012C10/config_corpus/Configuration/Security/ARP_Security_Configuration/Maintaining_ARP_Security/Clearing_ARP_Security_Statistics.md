Clearing ARP Security Statistics
================================

This section describes how to clear Address Resolution Protocol (ARP) security statistics

#### Background Information

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

ARP security statistics cannot be restored after they are cleared. Exercise caution before clearing the statistics.



#### Procedure

* Run the [**reset arp packet statistics**](cmdqueryname=reset+arp+packet+statistics) [ **slot** *slot-id* ] command in the user view to reset ARP statistics of a specified or all boards.
* Run the [**reset arp packet statistics**](cmdqueryname=reset+arp+packet+statistics) **interface** [ *interface-type* *interface-number* ] command in the user view to reset ARP statistics of a specified or all Layer 3 interfaces.
* Run the [**reset arp-check**](cmdqueryname=reset+arp-check) { **check-destination-ip** | **check-valid** } **statistics** **slot** *slot-id* command in the user view to clear statistics about discarded invalid ARP packets on a specific interface board.
  
  
  
  In VS mode, this command is supported only by the admin VS.