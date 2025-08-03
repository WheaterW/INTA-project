Configuring IS-IS Purge Source Tracing
======================================

IS-IS purge source tracing helps improve fault locating efficiency.

#### Usage Scenario

If network-wide IS-IS LSP deletion causes network instability, source tracing must be implemented as soon as possible to locate and isolate the fault source. However, IS-IS itself does not support source tracing. A conventional solution is to isolate nodes one by one until the fault source is located, but the process is complex and time-consuming and may compromise network services. To address this problem, enable IS-IS purge source tracing.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The following steps are optional, choose them as required.



#### Pre-configuration Tasks

Before configuring IS-IS purge LSP source tracing, complete the following tasks:

* Configure IP addresses for interfaces and ensure that neighboring devices are reachable at the network layer.
* [Configure basic IS-IS functions](dc_vrp_isis_cfg_1000.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
   
   
   
   To disable IS-IS purge LSP source tracing globally, run the [**isis purge-source-trace disable**](cmdqueryname=isis+purge-source-trace+disable) command.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   To disable this function on an interface, run the [**isis purge-source-trace block**](cmdqueryname=isis+purge-source-trace+block) command.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**isis purge-source-trace port**](cmdqueryname=isis+purge-source-trace+port) *port-number*
   
   
   
   A UDP port number is configured for IS-IS purge source tracing packets.
   
   
   
   The IS-IS purge source tracing port is used to receive and send IS-IS purge source tracing packets and is identified by a UDP port number.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the user view.
6. Run [**reset isis**](cmdqueryname=reset+isis) [ *process-id* ] **purge-source-trace**
   
   
   
   IS-IS purge source tracing is reset.
   
   
   
   If a large number of IS-IS purge source tracing statistics exist on a device, you can run the [**reset isis purge-source-trace**](cmdqueryname=reset+isis+purge-source-trace) command to reset the statistics and restart IS-IS purge source tracing. If the command is run, all dynamic source tracing statistics are deleted, and the device needs to re-negotiate the source tracing capability with neighboring devices.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display isis**](cmdqueryname=display+isis) *process-id* **purge-source-trace analysis-report** [ **level-1** | **level-2** ] command. The command output shows information about definitely and possibly faulty nodes identified by IS-IS purge source tracing.