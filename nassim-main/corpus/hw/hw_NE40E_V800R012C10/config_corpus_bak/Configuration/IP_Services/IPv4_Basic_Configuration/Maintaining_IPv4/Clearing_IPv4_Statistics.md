Clearing IPv4 Statistics
========================

You can delete IPv4 statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

ICMP or IP traffic statistics cannot be restored after they are cleared. Exercise caution when running a reset command.



#### Procedure

* To clear IP and ICMP traffic statistics, run the [**reset ip statistics**](cmdqueryname=reset+ip+statistics) command in the user view.
* To clear statistics about packets that have been discarded because the packets' destination MAC addresses are different from an interface's MAC address or the packets' sizes exceed the interface's MTU, run the [**reset forward-statistics packet discard**](cmdqueryname=reset+forward-statistics+packet+discard+mac+mtu+ipv4+interface) [ **mac** | **mtu** ] **ipv4** { **interface** { *interface-type* *interface-number* | **interface-name** } | **slot** *slot-id* } command in the user view.