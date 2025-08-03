Configuring an Ethernet Interface to Work in Auto-negotiation Mode
==================================================================

Configuring an Ethernet Interface to Work in Auto-negotiation Mode

#### Context

On a network, devices may have different transmission capabilities and must negotiate a proper data transmission capability to communicate with each other. The auto-negotiation function enables connected devices at both ends of a physical link to exchange information so that they can automatically choose the same working parameters and work at the maximum transmission capability that both devices support.

In auto-negotiation mode, interfaces on two connected devices need to negotiate their parameters, including the duplex mode and rate. The auto-negotiation result is affected by the media installed on the interfaces. If the negotiation succeeds, the two interfaces use the same duplex mode and rate. In non-auto-negotiation mode, you must manually set the preceding parameters.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Ethernet interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. (Optional) Pre-configure the transmission medium type of the interface as copper transceiver.
   
   
   ```
   [device transceiver](cmdqueryname=device+transceiver) transceiver-type
   ```
4. Configure the Ethernet interface to work in auto-negotiation mode.
   
   
   ```
   [undo negotiation disable](cmdqueryname=undo+negotiation+disable)
   ```
   
   By default, an Ethernet interface works in auto-negotiation mode.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If interface hardware complies with auto-negotiation standards, it is recommended that Ethernet interfaces work in auto-negotiation mode.
   
   Manually setting interface rates usually complicates network planning and maintenance, and improper settings will affect or even interrupt the network communication.
   
   Running the **negotiation disable** command on an interface in the up state will cause the interface to go down and then up again. Exercise caution when performing this operation.
   
   An optical interface with a GE optical module, GE copper transceiver, or copper cable works in auto-negotiation mode by default. To configure the interface to work in non-auto-negotiation mode, run the **negotiation disable** command. If another type of module is inserted into the interface, it works in non-auto-negotiation mode and does not support auto-negotiation.
   
   All electrical interfaces support auto-negotiation.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command in any view or the [**display this interface**](cmdqueryname=display+this+interface) command in the interface view to check whether auto-negotiation is enabled on the interface based on the **Negotiation** field in the command output.


#### Follow-up Procedure

If the interface goes down due to an auto-negotiation failure, you can attempt to run the [**negotiation compatible-mode**](cmdqueryname=negotiation+compatible-mode) [ [**precursor**](cmdqueryname=precursor) *precursor-value* [**postcursor**](cmdqueryname=postcursor) *postcursor-value* ] command to switch the interface to the auto-negotiation-compatible mode and then check whether the interface goes up. By default, an interface works in incompatible mode.

![](public_sys-resources/notice_3.0-en-us.png) 

Before using this command, contact technical support personnel to determine whether it is necessary to use this command and set parameters. Incorrectly using this command may cause interfaces in up state to go down.

This command can be used only when an interface has a copper cable installed or pre-configured and supports the auto-negotiation function.

This command is not supported on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.