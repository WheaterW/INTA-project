Maintaining DHCPv6
==================

Maintaining DHCPv6

#### Clearing DHCPv6 Message Statistics

![](public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when you run reset commands.

To clear DHCPv6 message statistics, run the following commands.

**Table 1** Clearing DHCPv6 message statistics
| Operation | Command |
| --- | --- |
| Clear statistics about DHCPv6 messages. | [**reset dhcpv6 statistics**](cmdqueryname=reset+dhcpv6+statistics) |
| Clear routing information learned from DHCPv6 PD clients on a DHCPv6 relay agent. | [**reset dhcpv6 relay prefix-delegation route**](cmdqueryname=reset+dhcpv6+relay+prefix-delegation+route) [ [**vpn6-instance**](cmdqueryname=vpn6-instance) *vpn-instance-name* ] *ipv6-address mask-length* |
| Clear statistics about DHCPv6 relay messages. | [**reset dhcpv6 relay statistics**](cmdqueryname=reset+dhcpv6+relay+statistics) [ **interface** *interface-type interface-number* ] |