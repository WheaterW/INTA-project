Clearing BRAS Access Statistics
===============================

This section describes how to clear the existing statistics on an interface before you collect statistics on this interface within a specified period of time. BRAS access statistics cannot be restored after being cleared. Therefore, exercise caution when performing the following operations.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Cleared running information about BRAS access cannot be restored. Exercise caution when you perform this operation.



#### Procedure

* Run the [**reset vlan-statistics**](cmdqueryname=reset+vlan-statistics) **interface** *interface-type interface-number*.*subinterface-number* **pevlan** *pe-vlan-id* [ **cevlan** *ce-vlan-id* ] command to clear statistics about traffic and Point-to-Point Protocol (PPP) packets on a specified sub-interface bound to a specified virtual local area network (VLAN).
* Run the [**reset access statistics packet discard**](cmdqueryname=reset+access+statistics+packet+discard) { **mac-spoofing** | **urpf** } [ **ipoe** | **pppoe** ] [ **ipv4** | **ipv6** ] { **interface** { *interface-type* *interface-name* | *interface-number* } | **slot** *slot-id* } command to clear statistics about MAC-spoofing-dropped packets of access users.
* Run the [**reset access statistics trigger slot**](cmdqueryname=reset+access+statistics+trigger+slot) *slot-id* command to clear access packet statistics on a board.
* Run the [**reset layer3-subscriber statistics port-mismatch**](cmdqueryname=reset+layer3-subscriber+statistics+port-mismatch) [ **interface**  { *interface-name* | *interface-type* *interface-num* } ] command to clear statistics about Layer 3 users' packets that are discarded due to an interface mismatch.
* Run the [**reset cpu-defend whitelist session-car web-auth-server statistics**](cmdqueryname=reset+cpu-defend+whitelist+session-car+web-auth-server+statistics) **slot** *slot-id* command to clear statistics about CAR for whitelisted portal sessions on a specified board.
* Run the [**reset cpu-defend whitelist-v6 session-car web-auth-serverv6 statistics**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car+web-auth-serverv6+statistics) **slot** *slot-id* command to clear statistics about CAR for whitelisted portalv6 sessions on a specified board.