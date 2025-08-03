(Optional) Configuring Prompt Response to Layer 2 Network Topology Changes
==========================================================================

Prompt response to Layer 2 network topology changes enables a device to correctly forward multicast data based on the new network topology, ensuring uninterrupted service forwarding.

#### Context

If a Layer 2 network topology changes, forwarding paths of multicast packets in the VLAN or VSI may change. After prompt response to Layer 2 network topology changes is configured on a device, the device will send an IGMP Query message upon a link fault. After receiving the IGMP Query message, group member hosts attached to the device will reply with an IGMP Report message. Based on the received IGMP Report message, the device updates information on multicast group member ports, and switches multicast data traffic to new forwarding paths.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**igmp-snooping send-query enable**](cmdqueryname=igmp-snooping+send-query+enable)
   
   
   
   Prompt response to Layer 2 network topology changes is configured.
   
   
   
   When the device detects a Layer 2 network topology change, it proactively sends an IGMP General Query message with a non-0.0.0.0 source address. This enables interface information to be updated quickly and downstream user hosts to receive multicast data uninterruptedly.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.