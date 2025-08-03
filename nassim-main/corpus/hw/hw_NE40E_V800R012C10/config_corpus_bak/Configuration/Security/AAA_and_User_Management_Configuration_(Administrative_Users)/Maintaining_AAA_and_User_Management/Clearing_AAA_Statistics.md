Clearing AAA Statistics
=======================

You can clear AAA statistics by running the [**reset**](cmdqueryname=reset) command.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Therefore, confirm the action before you run the following commands.



#### Procedure

* Run the [**reset aaa online-fail-record**](cmdqueryname=reset+aaa+online-fail-record) command in the user view to clear the statistics about all user login failure records.
* Run the [**reset aaa offline-record**](cmdqueryname=reset+aaa+offline-record) command in the user view to clear the statistics about all user offline records.
* Run the [**reset
  aaa abnormal-offline-record**](cmdqueryname=reset+aaa+abnormal-offline-record) command in the user view to clear the statistics about all user abnormal offline records.
* Run the [**reset aaa statistics**](cmdqueryname=reset+aaa+statistics) { **authentication** | **accounting** } [ **domain** *domain-name* ] command in any view to clear statistics about authentication or accounting packets.
* Run the [**reset hwtacacs-server statistics**](cmdqueryname=reset+hwtacacs-server+statistics) { **all** | **authentication** | **authorization** | **accounting** | **common** } command in the user view to clear the statistics on the HWTACACS server.
* Run the **[**reset radius-attribute packet-count**](cmdqueryname=reset+radius-attribute+packet-count)** command in the user view to clear the count of the attributes in RADIUS packets.
* Run the [**reset cpu-defend whitelist session-car radius statistics**](cmdqueryname=reset+cpu-defend+whitelist+session-car+radius+statistics) **slot** *slot-id* command to clear statistics about CAR for whitelisted RADIUS sessions on a specified board.
* Run the [**reset cpu-defend whitelist-v6 session-car radiusv6 statistics**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car+radiusv6+statistics) **slot** *slot-id* command to clear statistics about CAR for whitelisted RADIUSv6 sessions on a specified board.