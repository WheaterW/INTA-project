Configuring the Proposal/Agreement Mechanism
============================================

To enable Huawei Datacom devices to communicate with non-Huawei devices, a proper rapid transition mechanism needs to be configured on Huawei devices based on the Proposal/Agreement mechanism on non-Huawei devices.

#### Context

The rapid transition mechanism is also called the Proposal/Agreement mechanism. Devices currently support the following modes:

* Enhanced mode: The current interface counts a root port when it counts the synchronization flag bit.
  + An upstream device sends a Proposal message to a downstream device, requesting rapid status transition. After receiving the message, the downstream device sets the port connected to the upstream device to a root port and blocks all non-edge ports.
  + The upstream device then sends an Agreement message to the downstream device. After the downstream device receives the message, the root port transitions to the Forwarding state.
  + The downstream device responds the Proposal message with an Agreement message. After receiving the message, the upstream device sets the port connected to the downstream device as a designated port. The designated port then transitions to the Forwarding state.
* Common mode: The current interface ignores the root port when it counts the synchronization flag bit.
  + An upstream device sends a Proposal message to a downstream device, requesting rapid status transition. After receiving the message, the downstream device sets the port connected to the upstream device to a root port and blocks all non-edge ports. The root port then transitions to the Forwarding state.
  + The downstream device responds the Proposal message with an Agreement message. After receiving the message, the upstream device sets the port connected to the downstream device as a designated port. The designated port then transitions to the Forwarding state.

When Huawei datacom devices are interworking with non-Huawei devices, select either mode depending on the Proposal/Agreement mechanisms on non-Huawei devices.


#### Applicable Environment

On a network running STP/RSTP, inconsistent protocol packet formats and BPDU keys may lead to a communication failure. Configuring proper STP/RSTP parameters on Huawei devices ensures interoperability between Huawei devices and non-Huawei devices.


#### Pre-configuration Tasks

Before configuring STP/RSTP interoperability between Huawei devices and non-Huawei devices, complete the following task:

* Configuring basic STP/RSTP functions


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in STP calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. Run [**stp no-agreement-check**](cmdqueryname=stp+no-agreement-check)
   
   
   
   The common rapid transition mechanism is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Proposal/Agreement Mechanism Configuration

Run the [**display this**](cmdqueryname=display+this) command in the view of the interface participating in STP calculation to view the fast transition mechanism configured on the interface.