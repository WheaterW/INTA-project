Clearing DHCPv6 Snooping Statistics
===================================

This section describes how to clear DHCPv6 snooping statistics.

#### Context

After the alarm function is configured for DHCPv6 snooping, the system will collect statistics about the discarded attack packets. You can run the [**display dhcpv6 snooping interface**](cmdqueryname=display+dhcpv6+snooping+interface) { *interface-name* | *interface-type* *interface-num* } command to check statistics about the discarded packets. To get accurate statistics, you can clear the existing statistics about discarded packets.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

DHCPv6 snooping statistics cannot be restored after they are cleared. Exercise caution when running the commands.



#### Procedure

* Run the **reset dhcpv6 snooping bind-table** [ { **interface** { *interface-type* *interface-num* | *interface-name* } | **i****pv6-address** *i*pv6-address** | **ipv6-prefix** *ipv6-prefix-mask* | **mac-address** *mac-address* } ] [ **release** ] command in the user view to clear entries in a dynamic DHCPv6 snooping binding table.
* Run the [**reset dhcpv6 snooping interface**](cmdqueryname=reset+dhcpv6+snooping+interface) { *interface-name* | *interface-type* *interface-num* } command in the user view to clear statistics about discarded DHCPv6 snooping packets.
* Run the **reset dhcpv6 snooping statistics** command in the user view to clear statistics about the packets sent and received after DHCPv6 snooping is enabled.