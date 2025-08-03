Monitoring the IPv4 Operating Status
====================================

You can monitor the IPv4 operating status.

#### Context

You can run the following commands in any view to check the IPv4 operating status in routine maintenance.


#### Procedure

* Run the [**display interface brief**](cmdqueryname=display+interface+brief) command in any view to check the interface summary.
* Run the [**display ip statistics**](cmdqueryname=display+ip+statistics) command in any view to check IP traffic statistics.
* Run the [**display icmp statistics**](cmdqueryname=display+icmp+statistics) [ **interface** *interface-type* *interface-num* ] command in any view to check ICMP traffic statistics.
* Run the [**display ip socket**](cmdqueryname=display+ip+socket) command in any view to check information about created IPv4 sockets.
* Run the [**display rawip status**](cmdqueryname=display+rawip+status) command in any view to check information about IPv4 RawIP connections.
* Run the [**display rawlink status**](cmdqueryname=display+rawlink+status) command in any view to check information about IPv4 RawLink connections.
* Run the [**display forward-statistics packet discard**](cmdqueryname=display+forward-statistics+packet+discard) [ **mac** | **mtu** ] **ipv4** { **interface** *interface-type* *interface-number* | **slot** *slot-id* } command to check statistics about packets that have been discarded because the packets' destination MAC addresses are different from an interface's MAC address or the packets' sizes exceed the interface's MTU.