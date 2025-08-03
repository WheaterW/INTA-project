Clearing AAA Statistics
=======================

Clearing AAA Statistics

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

The cleared statistics cannot be restored. Therefore, exercise caution when performing this operation.

To clear statistics, run the following commands as needed.


#### Procedure

* Run the [**reset aaa**](cmdqueryname=reset+aaa) { **abnormal-offline-record** | **offline-record** | **online-fail-record** } command in the system view to clear records about unexpected logouts, normal logouts, and login failures.
* Run the [**reset aaa statistics offline-reason**](cmdqueryname=reset+aaa+statistics+offline-reason) command in any view to clear statistics about user logout reasons.
* Run the [**reset hwtacacs-server statistics**](cmdqueryname=reset+hwtacacs-server+statistics) { **accounting** | **all** | **authentication** | **authorization** } command in the user view to clear statistics about HWTACACS authentication, accounting, and authorization.
* Run the [**reset hwtacacs-server accounting-stop-packet**](cmdqueryname=reset+hwtacacs-server+accounting-stop-packet) { **all** | **ip** *ip-address* } command in the user view to clear statistics on HWTACACS accounting-stop packets.
* Run the [**reset radius-server accounting-stop-packet**](cmdqueryname=reset+radius-server+accounting-stop-packet) { **all** | **ip** *ip-address* } command in the user view to clear the remaining buffer information of RADIUS accounting-stop packets.
* Run the **[**reset aaa-proxy statistics**](cmdqueryname=reset+aaa-proxy+statistics)** { **error** | **message** | **all**} command in the user view to clear statistics about messages of the AAA proxy module.
* Run the **[**reset local-user**](cmdqueryname=reset+local-user)** [ *user-name* ] **password** **history** **record** command in the user view to clear the historical passwords of a local administrator.