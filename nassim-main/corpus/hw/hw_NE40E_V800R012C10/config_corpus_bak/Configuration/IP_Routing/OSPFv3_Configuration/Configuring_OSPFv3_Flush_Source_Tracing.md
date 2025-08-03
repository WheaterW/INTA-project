Configuring OSPFv3 Flush Source Tracing
=======================================

OSPFv3 flush source tracing helps improve fault locating efficiency.

#### Usage Scenario

If network-wide OSPFv3 LSAs are deleted, flush LSAs are flooded, which adversely affects network stability. In this case, source tracing must be implemented to locate the root cause of the fault immediately to minimize the impact. However, OSPFv3 itself does not support source tracing. A conventional solution is isolation node by node until the faulty node is located, but the solution is complex and time-consuming. To address this problem, enable OSPFv3 flush source tracing.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The following steps are optional, and choose them as required.



#### Pre-configuration Tasks

Before configuring OSPFv3 flush source tracing, complete the following task:

* Configure an IP address for each interface to ensure that neighboring devices are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**ospfv3 flush-source-trace disable**](cmdqueryname=ospfv3+flush-source-trace+disable)
   
   
   
   OSPFv3 flush source tracing is disabled globally.
   
   
   
   To disable OSPFv3 flush source tracing globally, perform this step.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. (Optional) Run [**ospfv3 flush-source-trace block**](cmdqueryname=ospfv3+flush-source-trace+block)
   
   
   
   OSPFv3 flush source tracing is disabled on the interface.
   
   
   
   To disable OSPFv3 flush source tracing on an interface, perform this step.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ] [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The OSPFv3 process is started, and the OSPFv3 view is displayed.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**ospfv3 flush-source-trace port**](cmdqueryname=ospfv3+flush-source-trace+port) *port-number*
   
   
   
   A UDP port number is configured for OSPFv3 flush source tracing packets.
   
   
   
   An OSPFv3 flush source tracing port is used to send and receive OSPFv3 flush source tracing packets and is represented by a UDP port number. If the port number used by UDP packets conflicts with that of another application, perform this step.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the user view.
11. Run [**reset ospfv3**](cmdqueryname=reset+ospfv3) *process-id* **flush-source-trace**
    
    
    
    OSPFv3 flush source tracing is reset.
    
    
    
    If a large number of OSPFv3 flush source tracing statistics exist on a device, you can run the [**reset ospfv3 flush-source-trace**](cmdqueryname=reset+ospfv3+flush-source-trace) command to reset the statistics and restart source tracing. If the command is run, all dynamic source tracing statistics are deleted, and the device needs to re-negotiate the source tracing capability with neighboring devices.

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] [ **area** *area-id-integer* ] **flush-source-trace analysis-info** command to check information about determined and suspected faulty nodes identified by OSPFv3 flush source tracing.