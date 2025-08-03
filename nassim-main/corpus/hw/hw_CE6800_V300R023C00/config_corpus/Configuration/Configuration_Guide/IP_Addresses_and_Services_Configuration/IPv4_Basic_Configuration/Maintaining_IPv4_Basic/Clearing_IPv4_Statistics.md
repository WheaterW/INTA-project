Clearing IPv4 Statistics
========================

Clearing IPv4 Statistics

#### Procedure

![](public_sys-resources/notice_3.0-en-us.png) 

IPv4 statistics cannot be restored after they are cleared. Exercise caution when running reset commands.


**Table 1** Clearing IPv4 statistics
| Operation | Command |
| --- | --- |
| Clear TCP traffic statistics. | [**reset tcp statistics**](cmdqueryname=reset+tcp+statistics) |
| Clear UDP traffic statistics. | [**reset udp statistics**](cmdqueryname=reset+udp+statistics) |
| Clear IP traffic statistics. | [**reset ip statistics**](cmdqueryname=reset+ip+statistics+interface) [ **interface** *interface-type* *interface-number* ] |
| Clear ICMP fast reply statistics. | [**reset icmp fast-reply statistics slot**](cmdqueryname=reset+icmp+fast-reply+statistics+slot) *slot-id* |
| Clear statistics about IPv4 RawIP packets. | [**reset rawip statistics**](cmdqueryname=reset+rawip+statistics) |
| Clear statistics about RawLink packets. | [**reset rawlink statistics**](cmdqueryname=reset+rawlink+statistics) |