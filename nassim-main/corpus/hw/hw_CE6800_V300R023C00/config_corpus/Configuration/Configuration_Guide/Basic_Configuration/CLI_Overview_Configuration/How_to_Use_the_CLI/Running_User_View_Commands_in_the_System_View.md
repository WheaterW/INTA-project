Running User View Commands in the System View
=============================================

Running User View Commands in the System View

#### Context

Some commands can be run only in the user view. To run these commands, you need to return to the user view first. To facilitate command execution, this function allows you to run such commands in the system view without returning to the user view.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Run user view commands in the system view.
   
   
   ```
   [run](cmdqueryname=run) command-line
   ```