Creating a RIPng process
========================

The creation of a RIPng process is a precondition of all RIPng configurations.

#### Usage Scenario

Before running RIPng on a Router, you need to create a RIPng process on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ]
   
   
   
   The RIPng process is created, and the RIPng view is displayed.
   
   RIPng supports multi-instance. To bind a RIPng process to a VPN instance, you can run the [**ripng**](cmdqueryname=ripng) [ *process-id* ] **vpn-instance** *vpn-instance-name* command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you run RIPng-related commands in the interface view before enabling RIPng, the configurations take effect only after RIPng is enabled.
3. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the RIPng process.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is submitted.