Stopping an OPS Task
====================

Stopping an OPS Task

#### Context

The OPS allows you to run the scripts you compile. You can stop a script that is running or waiting to run.

![](public_sys-resources/notice_3.0-en-us.png) 

When you stop a script, subsequent operations specified in the script will not be performed. Exercise caution when you perform this operation.



#### Procedure

1. (Optional) View information about running OPS tasks to obtain the ID of the task to be stopped.
   
   
   ```
   [display ops process](cmdqueryname=display+ops+process) method
   ```
2. Stop the OPS task.
   
   
   ```
   [ops stop process](cmdqueryname=ops+stop+process) process-id
   ```