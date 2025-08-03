Configuring OSPF Flush Source Tracing
=====================================

OSPF flush source tracing helps improve troubleshooting efficiency.

#### Usage Scenario

If network-wide OSPF LSPs are deleted, purge LSPs are flooded, which adversely affects network stability. In this case, source tracing must be implemented to locate the root cause of the fault immediately to minimize the impact. However, OSPF itself does not support source tracing. A conventional solution is isolation node by node until the faulty node is located, but the solution is complex and time-consuming. To address this problem, enable OSPF flush source tracing.


#### Pre-configuration Tasks

Before configuring OSPF flush source tracing, complete the following task:

* Configure an IP address for each interface to ensure that neighboring routers are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_2021.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**ospf flush-source-trace disable**](cmdqueryname=ospf+flush-source-trace+disable)
   
   
   
   OSPF flush source tracing is disabled globally.
   
   
   
   To disable OSPF flush source tracing globally, perform this step.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. (Optional) Run [**ospf flush-source-trace block**](cmdqueryname=ospf+flush-source-trace+block)
   
   
   
   OSPF flush source tracing is disabled on the interface.
   
   
   
   To disable OSPF flush source tracing on an interface, perform this step.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
6. Run [**ospf flush-source-trace port**](cmdqueryname=ospf+flush-source-trace+port) *port-number*
   
   
   
   A UDP port number is configured for OSPF flush source tracing packets.
   
   
   
   An OSPF flush source tracing port is used to send and receive OSPF flush source tracing packets and is represented by a UDP port number.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   The user view is displayed.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**reset ospf**](cmdqueryname=reset+ospf) *process-id* **flush-source-trace**
   
   
   
   OSPF flush source tracing is reset.
   
   
   
   If a large number of OSPF flush source tracing statistics exist on a device, you can run the [**reset ospf flush-source-trace**](cmdqueryname=reset+ospf+flush-source-trace) command to reset the statistics and restart OSPF flush source tracing. If the command is run, all dynamic source tracing statistics are deleted, and the device needs to re-negotiate the source tracing capability with neighboring devices.

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] [ **area** *area-id* ] **flush-source-trace analysis-info** command to check information about definitely and possibly faulty nodes identified by OSPF flush source tracing.