Configuring the PADS Function
=============================

Configuring the PADS Function

#### Context

By default, the PADS function is enabled globally. To disable this function, perform the following operations.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Choose either of the following methods to disable the PADS function.
   
   
   * Disable the PADS function globally.
     
     ```
     [pads disable](cmdqueryname=pads+disable)
     ```
   * Disable the PADS function for a specific functional module.
     
     ```
     [pads switch](cmdqueryname=pads+switch) appName disable
     ```![](public_sys-resources/note_3.0-en-us.png) 
   
   The command for configuring the PADS function for a specified functional module takes precedence over the command for configuring the PADS function globally. That is, after the [**pads switch**](cmdqueryname=pads+switch) command is configured for a specified functional module, the PADS status for this functional module is not affected by the [**pads disable**](cmdqueryname=pads+disable) or [**pads enable**](cmdqueryname=pads+enable) command configuration.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

For more information about PADS diagnosis functions, see the *Diagnostic Command Reference*.