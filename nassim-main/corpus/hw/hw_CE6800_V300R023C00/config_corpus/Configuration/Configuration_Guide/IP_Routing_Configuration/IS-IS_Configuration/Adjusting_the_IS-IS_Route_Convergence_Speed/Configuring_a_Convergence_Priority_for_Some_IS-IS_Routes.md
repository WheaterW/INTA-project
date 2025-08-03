Configuring a Convergence Priority for Some IS-IS Routes
========================================================

Configuring a Convergence Priority for Some IS-IS Routes

#### Context

You can configure the highest convergence priority for some IS-IS routes so that these routes converge first when a network topology changes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure a convergence priority for the IS-IS routes that match a specified filtering rule.
   
   
   ```
   [prefix-priority](cmdqueryname=prefix-priority) [ level-1 | level-2 ] { critical | high | medium } { ip-prefix prefix-name | tag tag-value }
   ```
   
   
   
   By default, the convergence priority of IS-IS host routes (with a 32-bit mask) is medium, and the convergence priority of the other IS-IS routes is low.
   
   The convergence priorities for IS-IS routes are used as follows:
   * If an IS-IS route matches the filtering conditions of multiple convergence priorities, the highest convergence priority is used.
   * By default, the convergence priority of Level-1 IS-IS routes is higher than that of Level-2 IS-IS routes.
   * If no level is specified in the [**prefix-priority**](cmdqueryname=prefix-priority) command, the configuration takes effect on both Level-1 and Level-2 IS-IS routes.
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the [**prefix-priority**](cmdqueryname=prefix-priority) command is run, the convergence priority of 32-bit host routes is changed from medium to low, and the convergence priorities of the other routes are changed based on the [**prefix-priority**](cmdqueryname=prefix-priority) command configuration.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```