(Optional) Configuring IPv4 IS-IS Attributes on Networks of Different Types
===========================================================================

Different IS-IS attributes can be configured for different types of network interfaces.

#### Context

The establishment mode of IS-IS neighbor relationships on a broadcast network is different from that on a P2P network. Different IS-IS attributes can be configured for interfaces on different types of networks.

IS-IS is required to select a DIS on a broadcast network. Configure the DIS priorities of IS-IS interfaces so that the interface with the highest priority is selected as the DIS.

The network types of the IS-IS interfaces on both ends of a link must be the same, otherwise, the IS-IS neighbor relationship cannot be established between the two interfaces. If the type of an interface on the neighbor is P2P, you can configure the interface type on the local device to P2P so that an IS-IS neighbor relationship can be established between the two devices.

IS-IS on a P2P network is not required to select a DIS. Therefore, you do not need to configure DIS priorities. To ensure the reliability of P2P links, configure IS-IS to use the three-way handshake mode for IS-IS neighbor relationship establishment so that faults on a unidirectional link can be detected.


#### Procedure

* Configure the DIS priority of an IS-IS interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis dis-priority**](cmdqueryname=isis+dis-priority) *priority* [ **level-1** | **level-2** ]
     
     
     
     The DIS priority is configured on the interface. The greater the value, the higher the priority.
  4. (Optional) Run [**isis dis-name**](cmdqueryname=isis+dis-name) *symbolic-name*
     
     
     
     A name is configured for the DIS to facilitate maintenance and management.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the network type of an IS-IS interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis circuit-type**](cmdqueryname=isis+circuit-type) **p2p**
     
     
     
     The network type of the interface is set to P2P
     
     
     
     When the network type of an IS-IS interface changes, interface configurations change accordingly.
     + After a broadcast interface is configured as a P2P interface using the [**isis circuit-type**](cmdqueryname=isis+circuit-type) **p2p** command, the default values of the interval at which Hello packets are sent, the number of Hello packets that IS-IS fails to receive from a neighbor before declaring the neighbor Down, the interval LSPs are retransmitted on a P2P link, and various IS-IS authentication modes take effect. Consequently, other configurations such as the DIS priority, DIS name, and interval at which CSNPs are sent on a broadcast network become invalid.
     + After the [**undo isis circuit-type**](cmdqueryname=undo+isis+circuit-type) command is run to restore the network type, the default values of the interval at which Hello packets are sent, the number of Hello packets that IS-IS fails to receive from a neighbor before declaring the neighbor Down, the interval LSPs are retransmitted on a P2P link, the IS-IS authentication mode, the DIS priority, and the interval at which CSNPs are sent on a broadcast network take effect.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the negotiation mode for the establishment of neighbor relationships over P2P links.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis ppp-negotiation**](cmdqueryname=isis+ppp-negotiation) { **2-way** | **3-way** [ **only** ]}
     
     
     
     A negotiation mode is specified for the interface.
     
     
     
     This command applies only to neighbor relationship establishment over P2P links. In the case of a broadcast link, you can run the [**isis circuit-type**](cmdqueryname=isis+circuit-type) **p2p** command to set the link type to P2P, and then set a negotiation mode for neighbor relationship establishment.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure OSICP negotiation check on PPP interfaces.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis ppp-osicp-check**](cmdqueryname=isis+ppp-osicp-check)
     
     
     
     The OSICP negotiation status is checked on a PPP interface.
     
     
     
     This command is applicable only to PPP interfaces. For P2P interfaces, this command is invalid.
     
     After this command is run, OSI network negotiation status of PPP affects IS-IS interface status. When PPP detects that the OSI network fails, the link status of the IS-IS interface goes down and the route to the network segment where the interface resides is not advertised through LSPs.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the scale of the Hello packets sent on the IS-IS interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Configure the size of the Hello packets to be sent by the IS-IS interface. Perform either of the following configurations as required:
     
     
     + To configure the interface to send Hello packets without the padding field, run the [**isis small-hello**](cmdqueryname=isis+small-hello) command.
     + To configure the interface to send standard Hello packets with the padding field, run the [**isis padding-hello**](cmdqueryname=isis+padding-hello) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IS-IS not to check the IP addresses of received Hello packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis peer-ip-ignore**](cmdqueryname=isis+peer-ip-ignore)
     
     
     
     IS-IS is configured not to check the IP addresses of received Hello packets.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.