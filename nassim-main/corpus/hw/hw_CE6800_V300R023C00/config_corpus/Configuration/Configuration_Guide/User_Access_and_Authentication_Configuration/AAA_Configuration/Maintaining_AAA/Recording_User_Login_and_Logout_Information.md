Recording User Login and Logout Information
===========================================

Recording User Login and Logout Information

#### Context

To help administrators locate and analyze the causes of user login failures and unexpected logouts, you can enable the function of recording normal logouts, unexpected logouts, and login failures. After the function is enabled, you can run the following commands to view user login and logout information.


#### Procedure

| Operation | Command | Description |
| --- | --- | --- |
| In the system view, enable the function of recording normal logout information. | [**aaa offline-record**](cmdqueryname=aaa+offline-record) | By default, the function is enabled.  After the function is enabled, you can run the following commands to view user information:   * Run the [**display aaa**](cmdqueryname=display+aaa) command in any view to view records about normal logouts, unexpected logouts, and login failures. * Run the [**display aaa statistics offline-reason**](cmdqueryname=display+aaa+statistics+offline-reason) command in any view to view the reason why users go offline. |
| In the system view, enable the function of recording unexpected logout information. | [**aaa abnormal-offline-record**](cmdqueryname=aaa+abnormal-offline-record) |
| In the system view, enable the function of recording login failures. | [**aaa online-fail-record**](cmdqueryname=aaa+online-fail-record) |
| In the system view, set the maximum number of CIB cache entries that can be recorded and the aging time. | **access-user cib-record cache-record-num** *cache-record-num* **cache-aging-time** *cache-aging-time* | When an access user fails authentication, check the data in the access user cache table to locate the fault. To facilitate fault locating, run this command to specify the maximum number of CIB cache entries that can be recorded and the aging time. |