Enabling and Disabling the PADS
===============================

This section describes how to set the PADS function status when the PADS is used.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration process is supported only on the Admin-VS.

The protocol-aided diagnosis system (PADS) is an intelligent diagnosis system. It simulates service experts to be online for 7 x 24 hours and to implement automatic service fault prevention, discovery, and diagnosis from end to end. The PADS also supports automatic fault recovery with the help of the self-healing system.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Choose either of the following methods to disable the PADS function.
   
   
   * To disable the PADS function globally, run the [**pads disable**](cmdqueryname=pads+disable) command.
   * To disable the PADS function of a specific feature, run the [**pads switch**](cmdqueryname=pads+switch) *module-name* **disable** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**pads switch**](cmdqueryname=pads+switch) command is not run, the status of functions in the protocol-aided diagnosis system is determined by the [**pads disable**](cmdqueryname=pads+disable) command. If the [**pads switch**](cmdqueryname=pads+switch) command is run, the status of a specific function in the protocol-aided diagnosis system is determined by the [**pads switch**](cmdqueryname=pads+switch) command no matter the status of the entire protocol-aided diagnosis system is enabled or disabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.