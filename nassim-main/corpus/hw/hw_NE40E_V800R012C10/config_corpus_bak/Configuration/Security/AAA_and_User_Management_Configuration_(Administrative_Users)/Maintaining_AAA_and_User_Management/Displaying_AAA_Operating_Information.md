Displaying AAA Operating Information
====================================

To learn about the operating status of AAA, you can check the operating information of AAA.

#### Context

In routine maintenance, you can run the following commands in any view to check the AAA operating status.


#### Procedure

* Run the [**display aaa configuration**](cmdqueryname=display+aaa+configuration) command to view brief AAA information.
* Run the [**display aaa offline-record**](cmdqueryname=display+aaa+offline-record) command to check user logout records in the system.
  
  
  
  The device records user logouts only when the user logout recording function is enabled.
  
  If the device is disabled from recording user logouts, you can run the [**aaa offline-record**](cmdqueryname=aaa+offline-record) command to enable this function.
* Run the [**display aaa online-fail-record**](cmdqueryname=display+aaa+online-fail-record) command to check user login failure records.
  
  
  
  The device records user login failures only when the user login failure recording function is enabled.
  
  If the device is disabled from recording user login failures, run the [**aaa online-fail-record**](cmdqueryname=aaa+online-fail-record) command to enable this function.
* Run the [**display max-onlineusers**](cmdqueryname=display+max-onlineusers) command to check the historical maximum number of concurrent online users.
* Run the [**display aaa abnormal-offline-record**](cmdqueryname=display+aaa+abnormal-offline-record) command to check unexpected logout records of users.
* Run the [**display access-user**](cmdqueryname=display+access-user) command to check information about users who have passed AAA authentication.
* Run the [**display accounting-scheme**](cmdqueryname=display+accounting-scheme) command to check the accounting scheme configuration.
* Run the [**display authentication-scheme**](cmdqueryname=display+authentication-scheme) [ *authentication-scheme-name* ] command to check the authentication scheme configuration.
* Run the [**display authorization-scheme**](cmdqueryname=display+authorization-scheme) [ *authorization-scheme-name* ] command to check the authorization scheme configuration.
* Run the [**display domain**](cmdqueryname=display+domain) *domain-name* command to check the domain configuration.
* Run the [**display hwtacacs current-status**](cmdqueryname=display+hwtacacs+current-status) command to check the current HWTACACS status.
* Run the [**display hwtacacs-server template**](cmdqueryname=display+hwtacacs-server+template) command to check the HWTACACS server configuration.
* Run the [**display local-user**](cmdqueryname=display+local-user) command to check the attributes of local users.
* Run the [**display radius-attribute packet-count**](cmdqueryname=display+radius-attribute+packet-count) command to check the number of times each attribute occurs in RADIUS packets.
* Run the [**display radius-server configuration**](cmdqueryname=display+radius-server+configuration) [ **group** *group-name* ] command to check the RADIUS server configuration.
* Run the [**display recording-scheme**](cmdqueryname=display+recording-scheme) command to check the recording scheme configuration.
* Run the [**display task-group**](cmdqueryname=display+task-group) [ *task-group-name* ] command to check the task group information.
* Run the [**display user-group**](cmdqueryname=display+user-group) [ *user-group-name* ] command to check the task group information.
* Run the [**display aaa user-group**](cmdqueryname=display+aaa+user-group) [ *user-group-name* ] command to check the task group information.