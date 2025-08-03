Clearing ARP Statistics
=======================

Clearing ARP Statistics

#### Context

![](public_sys-resources/caution_3.0-en-us.png) 

* Static ARP entries cannot be restored after being cleared. Exercise caution when you clear static ARP entries.
* After ARP entries are cleared, the mapping between IP and MAC addresses is deleted, which may cause a failure to access some nodes. Exercise caution when you clear ARP entries.

**Table 1** Clearing ARP statistics
| Operation | Command |
| --- | --- |
| Clear all ARP entries. | [**reset arp all**](cmdqueryname=reset+arp+all) |
| Clear ARP entries learned by a specified interface. | [**reset arp interface**](cmdqueryname=reset+arp+interface) { *interface-name* | *interface-type* *interface-number* } [ **ip** *ip-address* ] |
| Clear dynamic ARP entries containing a specified IP address. | [**reset arp dynamic ip**](cmdqueryname=reset+arp+dynamic+ip) *ip-address* |
| Clear ARP entries of a specified VPN instance. | [**reset arp vpn-instance**](cmdqueryname=reset+arp+vpn-instance)*vpn-instance-name* |
| Clear the dynamic ARP entry containing a specified IP address in a VPN instance. | [**reset arp dynamic ip**](cmdqueryname=reset+arp+dynamic+ip) *ip-address* **vpn-instance** *vpn-instance-name* |
| Clear ARP fast reply statistics. | **reset arp fast-reply** **slot** *slot-id* **statistics** |
| Clear ARP message statistics in a specified BD. | [**reset arp packet statistics bridge-domain**](cmdqueryname=reset+arp+packet+statistics+bridge-domain)*bd-id*  NOTE:  This function is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, and CE6863E-48S8CQ. |