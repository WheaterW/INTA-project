Configuring IS-IS Attributes for Interfaces of Different Network Types
======================================================================

Configuring IS-IS Attributes for Interfaces of Different Network Types

#### Prerequisites

Before configuring IS-IS attributes for interfaces of different network types, you have completed the following task:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0011.html).

#### Context

The process for establishing an IS-IS neighbor relationship on a broadcast network differs from that on a P2P network. As such, you can set different IS-IS attributes for interfaces of the two network types. Details are as follows:

* On a broadcast network, IS-IS must elect a DIS based on the DIS priorities of IS-IS interfaces. You can configure DIS priorities for IS-IS interfaces so that they run for the DIS.
* As IS-IS on a P2P network does not elect a DIS, it is not necessary to configure DIS priorities for interfaces. Instead, to ensure the reliability of P2P links, you can configure IS-IS P2P interfaces to use the three-way mode to establish IS-IS neighbor relationships, enabling unidirectional link faults to be detected. In normal cases, IS-IS checks the IP addresses of received IIHs, and a neighbor relationship can only be established if the source IP address carried in a received IIH and the address of the interface that receives the IIH are on the same network segment.


#### Procedure

* Configure a DIS priority for an interface on a broadcast network.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure a DIS priority for the interface.
     
     
     ```
     [isis dis-priority](cmdqueryname=isis+dis-priority) priority [ level-1 | level-2 ]
     ```
     
     The larger the *priority* value, the higher the priority.
  5. (Optional) Configure a DIS name.
     
     
     ```
     [isis dis-name](cmdqueryname=isis+dis-name) symbolic-name
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure attributes for an interface on a P2P network.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Enable IS-IS on the interface.
     
     
     ```
     [isis enable](cmdqueryname=isis+enable) [ process-id ]
     ```
  5. Set the network type of the interface to P2P.
     
     
     ```
     [isis circuit-type](cmdqueryname=isis+circuit-type) p2p
     ```
     
     By default, the network type of an interface is determined by its physical interface type.
  6. Set a negotiation mode for the P2P interface.
     
     
     ```
     [isis ppp-negotiation](cmdqueryname=isis+ppp-negotiation) { 2-way | 3-way [ only ] }
     ```
     
     This command applies only to neighbor relationship establishment over P2P links. To set a negotiation mode for an interface to establish neighbor relationships on a broadcast link, you need to first run the [**isis circuit-type**](cmdqueryname=isis+circuit-type) **p2p** command to set the link type of the interface to P2P, and then run the [**isis ppp-negotiation**](cmdqueryname=isis+ppp-negotiation) command.
  7. Enable Open System Interconnection Control Protocol (OSICP) state check on the interface.
     
     
     ```
     [isis ppp-osicp-check](cmdqueryname=isis+ppp-osicp-check)
     ```
     
     
     
     This command applies only to PPP interfaces, not to P2P interfaces using other data link protocols.
     
     After this command is configured, the OSI network negotiation status of PPP can affect the IS-IS interface status. If PPP detects that the OSI network fails, the link state of the IS-IS interface is set to down, and the route to the network segment to which the IP address of the interface belongs is no longer advertised through LSPs.
  8. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure IIH-related functions.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure the interface to send small-sized IIHs (without the padding field).
     
     
     ```
     [isis small-hello](cmdqueryname=isis+small-hello)
     ```
  5. Configure the interface to send standard IIHs (with the padding field).
     
     
     ```
     [isis padding-hello](cmdqueryname=isis+padding-hello)
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The [**isis small-hello**](cmdqueryname=isis+small-hello) and [**isis padding-hello**](cmdqueryname=isis+padding-hello) commands are mutually exclusive. Run either of them as required.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display isis**](cmdqueryname=display+isis) **interface verbose** command to check detailed IS-IS interface information.


[Example for Configuring IS-IS DIS Election](vrp_isis_ipv4_cfg_0190.html)