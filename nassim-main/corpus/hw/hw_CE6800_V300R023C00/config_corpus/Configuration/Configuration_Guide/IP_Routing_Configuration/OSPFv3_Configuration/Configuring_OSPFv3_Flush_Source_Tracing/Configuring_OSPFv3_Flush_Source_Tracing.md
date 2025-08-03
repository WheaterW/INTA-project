Configuring OSPFv3 Flush Source Tracing
=======================================

Configuring OSPFv3 Flush Source Tracing

#### Prerequisites

Before configuring OSPFv3 flush source tracing, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

If network-wide OSPFv3 LSA flush causes network instability, source tracing must be implemented as soon as possible to locate and isolate the fault source. However, OSPFv3 itself does not support source tracing. A conventional solution is to isolate nodes one by one until the fault source is located, but the process is complex and time-consuming and may compromise network services. OSPFv3 flush source tracing can address this problem.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable OSPFv3 flush source tracing.
   
   
   ```
   [ospfv3 flush-source-trace disable](cmdqueryname=ospfv3+flush-source-trace+disable)
   ```
   
   By default, OSPFv3 flush source tracing is enabled globally. To disable OSPFv3 flush source tracing globally, run this command.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Disable OSPFv3 flush source tracing on the interface.
   
   
   ```
   [ospfv3 flush-source-trace block](cmdqueryname=ospfv3+flush-source-trace+block)
   ```
   
   By default, OSPFv3 flush source tracing is enabled globally. That is, OSPFv3 flush source tracing is enabled on all interfaces in the OSPFv3 process. To disable OSPFv3 flush source tracing on a specified interface, run this command.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Configure a UDP port number for OSPFv3 flush source tracing packets.
   
   
   ```
   [ospfv3 flush-source-trace port](cmdqueryname=ospfv3+flush-source-trace+port) port-number
   ```
   
   An OSPFv3 flush source tracing port is used to send and receive OSPFv3 flush source tracing packets and is represented by a UDP port number.
8. Return to the user view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Reset OSPFv3 flush source tracing.
   
   
   ```
   [reset ospfv3](cmdqueryname=reset+ospfv3) process-id flush-source-trace
   ```
   
   If a large number of OSPFv3 flush source tracing statistics exist on a device, you can run the [**reset ospfv3 flush-source-trace**](cmdqueryname=reset+ospfv3+flush-source-trace) command to reset the statistics and restart OSPFv3 flush source tracing. If the command is run, all OSPFv3 flush source tracing statistics are deleted, and the device needs to re-negotiate the source tracing capability with neighboring devices.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] [ **area** *area-id* ] **flush-source-trace analysis-info** command to check information about definitely and possibly fault sources identified by OSPFv3 flush source tracing.