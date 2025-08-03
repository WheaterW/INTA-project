Clearing IPv6 Statistics
========================

Clearing IPv6 Statistics

#### Procedure

![](public_sys-resources/notice_3.0-en-us.png) 

IPv6 statistics cannot be restored after they are cleared. Exercise caution when running reset commands.


**Table 1** Clearing IPv6 statistics 
| Operation | Command |
| --- | --- |
| Clear statistics about IPv6 packets. | [**reset ipv6 statistics**](cmdqueryname=reset+ipv6+statistics) |
| Clear dynamic PMTU entries. | [**reset ipv6 pathmtu**](cmdqueryname=reset+ipv6+pathmtu+dynamic) [ **vpn-instance** *vpn-instance-name* ] **dynamic** |
| Clear statistics about IPv6 RawIP packets. | [**reset rawip ipv6 statistics**](cmdqueryname=reset+rawip+ipv6+statistics) |
| Clear statistics about TCP6 packets. | [**reset tcp ipv6 statistics**](cmdqueryname=reset+tcp+ipv6+statistics) |
| Clear statistics about UDP6 packets. | [**reset udp ipv6 statistics**](cmdqueryname=reset+udp+ipv6+statistics) |