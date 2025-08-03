Clearing ARP Statistics
=======================

This section describes how to run **reset** commands to clear ARP statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

* Static ARP entries cannot be restored after being cleared. Exercise caution when you clear static ARP entries.
* After ARP entries are cleared, the mapping between IP and MAC addresses is deleted, which may cause a failure to access some nodes. Exercise caution when you clear ARP entries.


#### Procedure

* To clear ARP entries, run the [**reset arp**](cmdqueryname=reset+arp) { **all** | **dynamic** **ip** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **interface** *interface-type interface-number* [ **ip** *ip-address* ] | **slot** *slot-id* } command in the user view.
* To clear ARP packet statistics on a specified board or all boards, run the [**reset arp packet statistics**](cmdqueryname=reset+arp+packet+statistics) [ **slot** *slot-id* ] command in the user view.
* To clear ARP packet statistics on a specified Layer 3 interface or all Layer 3 interfaces, run the [**reset arp packet statistics**](cmdqueryname=reset+arp+packet+statistics) **interface** [ *interface-type* *interface-number* ] command in the user view.
* To clear ARP packet statistics in a specified BD, run the [**reset arp packet statistics bridge-domain**](cmdqueryname=reset+arp+packet+statistics+bridge-domain) *bd-id* command in the user view.