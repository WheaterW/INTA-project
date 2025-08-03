Maintaining ARP Security
========================

Maintaining ARP Security

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

ARP security statistics cannot be restored after being cleared. Exercise caution when clearing the statistics.


**Table 1** Clearing ARP security statistics
| Operation | Command |
| --- | --- |
| Clear statistics about ARP messages discarded because the rate of ARP messages exceeds the limit. | [**reset arp anti-attack record**](cmdqueryname=reset+arp+anti-attack+record) |
| Clear statistics about ARP Miss messages discarded because the rate of ARP Miss messages exceeds the limit. | [**reset arp miss anti-attack record**](cmdqueryname=reset+arp+miss+anti-attack+record) |
| Clear ARP message statistics. | **[**reset arp packet statistics**](cmdqueryname=reset+arp+packet+statistics)** [ ****interface**** [ **interface-name** | *interface-type* *interface-number* ] ] |
| Clear statistics about ARP messages discarded because the rate of ARP messages exceeds the limit on interfaces. | [**reset arp anti-attack rate-limit statistics**](cmdqueryname=reset+arp+anti-attack+rate-limit+statistics) |
| Clear statistics about ARP messages discarded because the messages do not match binding entries. | **[**reset arp anti-attack statistics check user-bind**](cmdqueryname=reset+arp+anti-attack+statistics+check+user-bind)** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-type* *interface-number* ] | **bridge-domain** [ *bd-id* ] ] |