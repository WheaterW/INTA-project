Enabling Loop Detection Globally
================================

Before loop detection is enabled on an interface, loop detection must be enabled in the system view.

#### Context

Perform the following steps on PEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**loop-detection enable**](cmdqueryname=loop-detection+enable)
   
   
   
   Loop detection is enabled globally.
3. (Optional) Run [**loop-detection identifier**](cmdqueryname=loop-detection+identifier) *identifier-value*
   
   
   
   An authentication identifier for L2VPN loop detection is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command can be configured only after L2VPN loop detection is enabled globally.