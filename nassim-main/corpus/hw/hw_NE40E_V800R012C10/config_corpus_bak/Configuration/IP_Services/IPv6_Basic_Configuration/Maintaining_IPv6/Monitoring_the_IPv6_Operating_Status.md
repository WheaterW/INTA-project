Monitoring the IPv6 Operating Status
====================================

This section describes how to monitor the IPv6 operating status.

#### Context

You can run the following commands in any view to check the IPv6 operating status in routine maintenance.


#### Procedure

* Run the [**display ipv6 interface**](cmdqueryname=display+ipv6+interface+interface+brief) [ **interface** *interface-type interface-number* | **brief** ] command to check IPv6 configurations on an interface.
* Run the [**display ipv6 statistics**](cmdqueryname=display+ipv6+statistics+interface) [ **interface** *interface-type interface-number* ] command to check IPv6 statistics.
* Run the [**display icmpv6 statistics**](cmdqueryname=display+icmpv6+statistics+interface) [ **interface** *interface-type interface-number* ] command to check ICMPv6 statistics.
* Run the [**display tcp ipv6 statistics**](cmdqueryname=display+tcp+ipv6+statistics) command to check TCP6 statistics.
* Run the [**display tcp ipv6 statistics verbose**](cmdqueryname=display+tcp+ipv6+statistics+verbose) command to check TCP6 statistics by application type.
* Run the [**display udp ipv6 statistics verbose**](cmdqueryname=display+udp+ipv6+statistics+verbose) command to check UDP6 statistics by application type.
* Run the [**display ipv6 address-policy**](cmdqueryname=display+ipv6+address-policy+vpn-instance+all) [ **vpn-instance** *vpn-instance-name* ] { **all** | *ipv6-address* *prefix-length* } command to check address selection policy entries.
* Run the [**display ipv6 pathmtu**](cmdqueryname=display+ipv6+pathmtu+vpn-instance+all+dynamic+static) [ **vpn-instance** *vpn-instance-name* ] { *ipv6-address* | **all** | **dynamic** | **static** } command to check all PMTU entries.
* Run the [**display forward-statistics packet discard**](cmdqueryname=display+forward-statistics+packet+discard+mac+mtu+ipv6+interface) [ **mac** | **mtu** ] **ipv6** { **interface** *interface-type* *interface-number* | **slot** *slot-id* } command to check statistics about packets that have been discarded because the packets' destination MAC addresses are different from an interface's MAC address or the packets' sizes exceed the interface's MTU.