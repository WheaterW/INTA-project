Enabling ZTP
============

Enabling_ZTP

#### Context

To implement automatic deployment through ZTP on a device upon a start with base configuration, enable ZTP.


#### Procedure

1. Run [**set ztp enable**](cmdqueryname=set+ztp+enable)
   
   
   
   ZTP is enabled.
   
   
   
   If automatic deployment through ZTP is not needed, run the [**set ztp disable**](cmdqueryname=set+ztp+disable) command to disable ZTP.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   ZTP does not take effect in any of the following conditions:
   
   * The preconfiguration file contains IP address configuration.
   * An IP address is manually assigned before a device completes automatic configuration.
   * The [**undo pnp enable**](cmdqueryname=undo+pnp+enable) command is run before a device completes automatic configuration.
2. (Optional) Run [**display ztp status**](cmdqueryname=display+ztp+status)
   
   
   
   The ZTP status is displayed.