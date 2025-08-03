Stopping a Maintenance Assistant
================================

Stopping a Maintenance Assistant

#### Context

If a maintenance assistant is no longer needed, you can stop it.![](public_sys-resources/notice_3.0-en-us.png) 

Stopping a running maintenance assistant interrupts the task of the assistant. Exercise caution when you perform this operation.




#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OPS view.
   
   
   ```
   [ops](cmdqueryname=ops)
   ```
3. Stop a script assistant.
   
   
   ```
   [shutdown script-assistant](cmdqueryname=shutdown+script-assistant) script-name
   ```
   
   To restart the script assistant, run the [**undo shutdown script-assistant**](cmdqueryname=undo+shutdown+script-assistant) *script-name* command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```