Configuring Convergence Priorities for IPv4 IS-IS Routes
========================================================

You can set a high convergence priority for key routes on an IS-IS network to ensure that these routes converge first if the network topology changes. This minimizes the impact on important services.

#### Context

The NE40E allows you to configure the highest convergence priority for specific IS-IS routes so that those IS-IS routes converge first when a network topology changes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**prefix-priority**](cmdqueryname=prefix-priority) [ **level-1** | **level-2** ] { **critical** | **high** | **medium** | **very-low** } { **ip-prefix** *prefix-name* | **tag** *tag-value* }
   
   
   
   A convergence priority is set for IS-IS routes.
   
   
   
   The rules for applying the convergence priorities of IS-IS routes are as follows:
   * Existing IS-IS routes converge based on the priorities configured in the [**prefix-priority**](cmdqueryname=prefix-priority) command.
   * New IS-IS routes that match the filtering rules converge based on the priorities configured in the [**prefix-priority**](cmdqueryname=prefix-priority) command.
   * If an IS-IS route meets the matching rules of multiple convergence priorities, the highest convergence priority is used.
   * The convergence priority of Level-1 IS-IS routes is higher than that of Level-2 IS-IS routes.
   * If no level is specified, the configuration takes effect on both Level-1 and Level-2 IS-IS routes.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**prefix-priority**](cmdqueryname=prefix-priority) command is only applicable to the public network.
   
   After the [**prefix-priority**](cmdqueryname=prefix-priority) command is run, the convergence priority of 32-bit host routes is **low**, and the convergence priorities of the other routes are specified in the [**prefix-priority**](cmdqueryname=prefix-priority) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.