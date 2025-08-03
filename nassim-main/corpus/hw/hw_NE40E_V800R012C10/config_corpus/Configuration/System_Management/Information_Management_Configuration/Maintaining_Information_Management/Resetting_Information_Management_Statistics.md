Resetting Information Management Statistics
===========================================

The system provides statistics about information management, and sends information to an information buffer for user query. You can perform the following configuration operations to clear statistics and the information in an information buffer.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Information management statistics cannot be restored after they are cleared. Exercise caution when running reset commands.



#### Procedure

* Run the [**reset info-center statistics**](cmdqueryname=reset+info-center+statistics) command in the user view to clear the statistics about information management.
* Run the [**reset logbuffer**](cmdqueryname=reset+logbuffer) command in the user view to clear information in the log buffer.
* Run the [**reset trapbuffer**](cmdqueryname=reset+trapbuffer) command in the user view to clear information in the trap buffer.