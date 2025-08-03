Clearing Routing Table Statistics
=================================

Clearing Routing Table Statistics

#### Context

Clear statistics about each routing protocol in the routing table. For details, see [Table 1](#EN-US_TASK_0000001130782564__table5606722102815).

![](public_sys-resources/note_3.0-en-us.png) 

Statistics about routes in IPv4 and IPv6 routing tables cannot be restored once being cleared. Therefore, exercise caution when running the following commands.


**Table 1** Clearing routing table statistics
| Operation | Command |
| --- | --- |
| Clear statistics about each routing protocol in the IPv4 routing table. | [**reset ip routing-table statistics protocol**](cmdqueryname=reset+ip+routing-table+statistics+protocol) [ **vpn-instance** *vpn-instance-name* ] { **al**l | **bgp** | **direct** | **isis** | **ospf** | **rip** | **static** } |
| Clear statistics about each routing protocol in the IPv6 routing table. | [**reset ipv6 routing-table**](cmdqueryname=reset+ipv6+routing-table) [ **vpn-instance** *vpn-instance-name* ] **statistics protocol** { **al**l | **bgp** | **direct** | **isis** | **ospfv3** | **ripng** | **static** }  NOTE:  The CE6885-LL in low latency mode does not support this command. |