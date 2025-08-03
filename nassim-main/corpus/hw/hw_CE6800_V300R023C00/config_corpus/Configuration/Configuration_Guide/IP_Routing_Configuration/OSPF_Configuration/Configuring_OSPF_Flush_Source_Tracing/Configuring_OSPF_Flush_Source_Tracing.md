Configuring OSPF Flush Source Tracing
=====================================

Configuring OSPF Flush Source Tracing

#### Prerequisites

Before configuring OSPF flush source tracing, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

If network-wide OSPF LSA flush causes network instability, source tracing must be implemented as soon as possible to locate and isolate the fault source. However, OSPF itself does not support source tracing. A conventional solution is to isolate nodes one by one until the fault source is located, but the process is complex and time-consuming and may compromise network services. OSPF flush source tracing can address this problem.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable OSPF flush source tracing.
   
   
   ```
   [ospf flush-source-trace disable](cmdqueryname=ospf+flush-source-trace+disable)
   ```
   
   By default, OSPF flush source tracing is enabled globally. To disable OSPF flush source tracing globally, run this command.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Disable OSPF flush source tracing on the interface.
   
   
   ```
   [ospf flush-source-trace block](cmdqueryname=ospf+flush-source-trace+block)
   ```
   
   By default, OSPF flush source tracing is enabled globally. That is, OSPF flush source tracing is enabled on all interfaces in the OSPF process. To disable OSPF flush source tracing on a specified interface, run this command.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Configure a UDP port number for OSPF flush source tracing packets.
   
   
   ```
   [ospf flush-source-trace port](cmdqueryname=ospf+flush-source-trace+port) port-number
   ```
   
   An OSPF flush source tracing port is used to send and receive OSPF flush source tracing packets and is represented by a UDP port number.
8. Return to the user view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Reset OSPF flush source tracing.
   
   
   ```
   [reset ospf](cmdqueryname=reset+ospf) process-id flush-source-trace
   ```
   
   If a large number of OSPF flush source tracing statistics exist on a device, you can run the [**reset ospf flush-source-trace**](cmdqueryname=reset+ospf+flush-source-trace) command to reset the statistics and restart OSPF flush source tracing. If the command is run, all OSPF flush source tracing statistics are deleted, and the device needs to re-negotiate the source tracing capability with neighboring devices.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] [ **area** *area-id* ] **flush-source-trace analysis-info** command to check information about definitely and possibly fault sources identified by OSPF flush source tracing.