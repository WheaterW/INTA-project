Disabling the Maintenance Assistant Function
============================================

Disabling the Maintenance Assistant Function

#### Context

You can disable the maintenance assistant function when you do not need the functions provided by assistants.![](public_sys-resources/notice_3.0-en-us.png) 

Disabling the maintenance assistant function interrupts all the assistants. Exercise caution when you perform this operation.




#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OPS view.
   
   
   ```
   [ops](cmdqueryname=ops)
   ```
3. Disable the maintenance assistant function.
   
   
   ```
   [assistant scheduler suspend](cmdqueryname=assistant+scheduler+suspend)
   ```
   
   To re-enable the maintenance assistant function, run the [**undo assistant scheduler suspend**](cmdqueryname=undo+assistant+scheduler+suspend) command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```