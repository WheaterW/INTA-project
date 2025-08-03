Maintaining OpenFlow
====================

Maintaining OpenFlow

#### Context

If the OpenFlow connection fails, you can check the OpenFlow packet statistics to determine whether an error has occurred in OpenFlow packet sending and receiving.

![](public_sys-resources/notice_3.0-en-us.png) 

Be aware that statistics cannot be restored after being deleted. Exercise caution when running the commands.

Exercise caution when restarting an OpenFlow connection between a controller and a device, as this action interrupts the connection.



#### Procedure

[Table 1](#EN-US_TASK_0000001512830202__table51619515374) lists the related operations for maintaining OpenFlow.

**Table 1** OpenFlow maintenance operations
| Operation | Command |
| --- | --- |
| Check OpenFlow packet statistics. | [**display sdn openflow statistics**](cmdqueryname=display+sdn+openflow+statistics) [ **slave** | **controller** [ **vpn-instance** *vpn-instance-name* ] { *ipv4-address* | *ipv6-address* } ] |
| Clear OpenFlow packet statistics. | [**reset sdn openflow statistics**](cmdqueryname=reset+sdn+openflow+statistics) [ **controller** [ **vpn-instance** *vpn-instance-name* ] { *ipv4-address* | *ipv6-address* } ] |
| Restart an OpenFlow connection. | [**reset sdn openflow session**](cmdqueryname=reset+sdn+openflow+session) [ **controller** [ **vpn-instance** *vpn-instance-name* ] { *ipv4-address* | *ipv6-address* } ] |