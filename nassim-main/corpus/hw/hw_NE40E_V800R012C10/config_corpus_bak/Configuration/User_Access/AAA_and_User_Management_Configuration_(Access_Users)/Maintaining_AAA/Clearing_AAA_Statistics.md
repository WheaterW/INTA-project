Clearing AAA Statistics
=======================

This section describes how to clear AAA statistics, including statistics on authentication, accounting, and authorization servers and Accounting Stop packets.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when clearing statistics.



#### Procedure

* To clear statistics about RADIUS packets, run the [**reset radius statistics packet**](cmdqueryname=reset+radius+statistics+packet) command in the system view.
* Run the [**reset aaa statistics**](cmdqueryname=reset+aaa+statistics) { **authentication** | **accounting** } [ **domain** *domain-name* ] command in any view to clear statistics.
* Run the [**reset radius-attribute packet-count**](cmdqueryname=reset+radius-attribute+packet-count) command in the user view to clear counts of attributes in RADIUS packets.
* Run the [**reset aaa remote-download acl statistics**](cmdqueryname=reset+aaa+remote-download+acl+statistics) [ **classifier** *classifier-name* | **slot** *slot-id* ] command in the user view to clear statistics about dynamic ACLs delivered by the RADIUS server.
* Run the [**reset radius-server accounting-packet all**](cmdqueryname=reset+radius-server+accounting-packet+all) command in the user view to clear all accounting packets from a cache queue.
* Run the [**reset radius-server accounting-interim-packet**](cmdqueryname=reset+radius-server+accounting-interim-packet) { **all** | **ip** *ip-address* } command in the user view to clear real-time accounting packets from a cache queue.
* Run the [**reset aaa online-fail-record dhcp statistics**](cmdqueryname=reset+aaa+online-fail-record+dhcp+statistics) command in any view to clear user login failure records.
* Run the [**reset max-onlineusers**](cmdqueryname=reset+max-onlineusers) command in the system view to clear the maximum number of concurrent online users recorded by the system.
  
  
  
  You can clear statistics based on a specified board or domain.
* Run the [**reset capture-packet access information**](cmdqueryname=reset+capture-packet+access+information) command in any view to clear information about obtained packet headers.
* Run the [**reset cpu-defend whitelist session-car radius statistics**](cmdqueryname=reset+cpu-defend+whitelist+session-car+radius+statistics) **slot** *slot-id* command to clear whitelist session-CAR statistics about DHCP messages on a specified interface board.
* Run the [**reset cpu-defend whitelist-v6 session-car radiusv6 statistics**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car+radiusv6+statistics) **slot** *slot-id* command to clear whitelist session-CAR statistics about RADIUSv6 packets on a specified interface board.