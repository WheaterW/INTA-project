Monitoring the ARP Operating Status
===================================

This section describes how to monitor the ARP operating status.

#### Procedure

* Run the [**display arp all**](cmdqueryname=display+arp+all) command in any view to check ARP entries on the main control boards and all interface boards.
* Run the [**display arp interface**](cmdqueryname=display+arp+interface) *interface-type interface-number* command in any view to check the ARP status on a specified interface.
* Run the [**display arp slot**](cmdqueryname=display+arp+slot) *slot-id* command in any view to check the ARP status on the board in a specified slot.
* Run the [**display arp packet statistics**](cmdqueryname=display+arp+packet+statistics) [ **slot** *slot-id* | **interface** [ *interface-type* *interface-number* ] ] command in any view to check ARP packet statistics.