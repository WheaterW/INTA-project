Creating a RIP process
======================

The creation of a RIP process is a precondition of all RIP configurations.

#### Usage Scenario

Before running RIP on a device, you need to create a RIP process on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
   
   RIP supports multi-instance. To bind a RIP process to a VPN instance, you can run the [**rip**](cmdqueryname=rip) [ *process-id* ] **vpn-instance** *vpn-instance-name* command.
3. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the RIP process.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

If you run RIP-related commands in the interface view before enabling RIP, the configurations take effect only after RIP is enabled.