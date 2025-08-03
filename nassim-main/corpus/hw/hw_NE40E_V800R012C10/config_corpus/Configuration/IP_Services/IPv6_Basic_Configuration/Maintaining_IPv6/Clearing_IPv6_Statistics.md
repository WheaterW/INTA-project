Clearing IPv6 Statistics
========================

This section describes how to clear IPv6 statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

IPv6 statistics cannot be restored after they are cleared. Exercise caution when running reset commands.



#### Procedure

* Run the [**reset ipv6 statistics**](cmdqueryname=reset+ipv6+statistics) command in the user view to clear IPv6 statistics.
* Run the [**reset tcp ipv6 statistics**](cmdqueryname=reset+tcp+ipv6+statistics) command in the user view to clear TCP6 statistics.
* Run the [**reset udp ipv6 statistics**](cmdqueryname=reset+udp+ipv6+statistics) command in the user view to clear UDP6 statistics.
* Run the [**reset ipv6 pathmtu**](cmdqueryname=reset+ipv6+pathmtu+vpn-instance+dynamic) [ **vpn-instance** *vpn-instance-name* ] **dynamic** command in the user view to clear the PMTU entries in the buffer.
* To clear statistics about packets that have been discarded because the packets' destination MAC addresses are different from an interface's MAC address or the packets' sizes exceed the interface's MTU, run the [**reset forward-statistics packet discard**](cmdqueryname=reset+forward-statistics+packet+discard+mac+mtu+ipv6+interface) [ **mac** | **mtu** ] **ipv6** { **interface** { *interface-type* *interface-number* | **interface-name** } | **slot** *slot-id* } command.