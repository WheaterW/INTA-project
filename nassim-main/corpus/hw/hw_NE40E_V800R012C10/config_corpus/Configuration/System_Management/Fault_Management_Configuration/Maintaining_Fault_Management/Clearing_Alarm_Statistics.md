Clearing Alarm Statistics
=========================

You can clear alarm statistics during routine maintenance.

#### Context

In routine maintenance, you can run the following commands in the alarm management view to clear alarm statistics.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Alarm statistics cannot be restored after they are cleared. Exercise caution when running the reset command.



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
3. Run the [**reset statistics**](cmdqueryname=reset+statistics) [ **name** *alarm-name* ] command to clear alarm statistics.
   
   
   
   The [**reset statistics**](cmdqueryname=reset+statistics) command clears all alarm statistics, and the [**reset statistics**](cmdqueryname=reset+statistics) **name** *alarm-name* command clears statistics about specific alarms.