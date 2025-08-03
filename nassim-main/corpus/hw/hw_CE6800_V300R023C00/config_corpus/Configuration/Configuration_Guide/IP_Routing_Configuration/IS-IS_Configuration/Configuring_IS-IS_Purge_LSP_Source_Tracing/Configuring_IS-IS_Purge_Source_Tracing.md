Configuring IS-IS Purge Source Tracing
======================================

Configuring IS-IS Purge Source Tracing

#### Prerequisites

Before configuring IS-IS purge source tracing, you have completed the following task:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0011.html).

#### Context

If network-wide IS-IS LSP deletion causes network instability, source tracing must be implemented as soon as possible to locate and isolate the fault source. However, IS-IS itself does not support source tracing. A conventional solution is to isolate nodes one by one until the fault source is located, but the process is complex and time-consuming and may compromise network services. To address this problem, enable IS-IS purge source tracing.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable IS-IS purge source tracing.
   
   
   ```
   [isis purge-source-trace disable](cmdqueryname=isis+purge-source-trace+disable)
   ```
   
   By default, IS-IS purge source tracing is enabled globally. To disable IS-IS purge source tracing globally, run this command.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Disable IS-IS purge source tracing on the interface.
   
   
   ```
   [isis purge-source-trace block](cmdqueryname=isis+purge-source-trace+block)
   ```
   
   By default, IS-IS purge source tracing is enabled globally. That is, IS-IS purge source tracing is enabled on all interfaces in the IS-IS process. To disable IS-IS purge source tracing on a specified interface, run this command.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Configure a UDP port number for IS-IS purge source tracing packets.
   
   
   ```
   [isis purge-source-trace port](cmdqueryname=isis+purge-source-trace+port) port-number
   ```
   
   The IS-IS purge source tracing port is used to receive and send IS-IS purge source tracing packets and is identified by a UDP port number.
8. Return to the user view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Reset the IS-IS purge source tracing function.
   
   
   ```
   [reset isis](cmdqueryname=reset+isis) [ process-id ] purge-source-trace
   ```
   
   If a large number of IS-IS purge source tracing statistics exist on a device, you can run the [**reset isis purge-source-trace**](cmdqueryname=reset+isis+purge-source-trace) command to reset the statistics and restart IS-IS purge source tracing. If the command is run, all IS-IS purge source tracing statistics are deleted, and the device needs to re-negotiate the purge source tracing capability with neighboring devices.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display isis**](cmdqueryname=display+isis) *process-id* **purge-source-trace analysis-report** [ **level-1** | **level-2** ] command to check information about the fault source and possible fault sources identified by IS-IS purge source tracing.