Configuring a Proposal/Agreement Mechanism
==========================================

To enable Huawei Datacom devices to communicate with non-Huawei devices, configure a proper rapid transition mechanism on Huawei devices according to the Proposal/Agreement mechanism on non-Huawei devices.

#### Context

The rapid transition mechanism is also called the Proposal/Agreement mechanism. Devices currently support the following modes:

* Enhanced mode: The current interface counts a root port when it computes the synchronization flag bit.
  + An upstream device sends a Proposal message to a downstream device, requesting rapid status transition. After receiving the message, the downstream device sets the port connected to the upstream device as a root port and blocks all non-edge ports.
  + The upstream device then sends an Agreement message to the downstream device. After the downstream device receives the message, the root port transitions to the Forwarding state.
  + The downstream device then responds to the Proposal message with an Agreement message. After receiving the message, the upstream device sets the port connected to the downstream device as a designated port, and the designated port transitions to the Forwarding state.
* Common mode: The current interface ignores the root port when it computes the synchronization flag bit.
  + An upstream device sends a Proposal message to a downstream device, requesting rapid status transition. After receiving the message, the downstream device sets the port connected to the upstream device as a root port and blocks all non-edge ports. The root port then transitions to the Forwarding state.
  + The downstream device responds to the Proposal message with an Agreement message. After receiving the message, the upstream device sets the port connected to the downstream device as a designated port. The designated port then transitions to the Forwarding state.

When Huawei Datacom devices are interworking with non-Huawei devices, select either mode depending on the Proposal/Agreement mechanism on non-Huawei devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in spanning tree protocol calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. (Optional) Run [**stp binding process**](cmdqueryname=stp+binding+process) *process-id*
   
   
   
   The interface is bound to an MSTP process.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is performed only when the interface needs to be bound to an MSTP process with a non-zero ID. If the interface belongs to process 0, skip this step.
4. Run [**stp no-agreement-check**](cmdqueryname=stp+no-agreement-check)
   
   
   
   The common rapid transition mechanism is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.