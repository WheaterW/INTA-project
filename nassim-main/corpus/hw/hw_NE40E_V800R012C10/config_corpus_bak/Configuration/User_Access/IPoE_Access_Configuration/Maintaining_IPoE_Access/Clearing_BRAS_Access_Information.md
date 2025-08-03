Clearing BRAS Access Information
================================

This section describes how to clear BRAS access information if there are too many login and logout records. BRAS access information cannot be restored after it is cleared. Exercise caution when running the following commands.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Cleared statistics on BRAS access cannot be restored. Exercise caution when you perform this operation.

Run the reset command to clear running information.


#### Procedure

1. Run the [**reset aaa online-fail-record**](cmdqueryname=reset+aaa+online-fail-record) command in the user view to clear the login failure records.
2. Run the [**reset aaa offline-record**](cmdqueryname=reset+aaa+offline-record) command in the user view to clear the logout records.
3. Run the [**reset aaa abnormal-offline-record**](cmdqueryname=reset+aaa+abnormal-offline-record) command in the user view to clear the abnormal logout records.
4. Run the [**reset access trigger user-table**](cmdqueryname=reset+access+trigger+user-table) command in any view to clear information about users whose access packets are limited on a board.
5. Run the [**reset call rate**](cmdqueryname=reset+call+rate) command in the user view to clear call rate statistics of users.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.