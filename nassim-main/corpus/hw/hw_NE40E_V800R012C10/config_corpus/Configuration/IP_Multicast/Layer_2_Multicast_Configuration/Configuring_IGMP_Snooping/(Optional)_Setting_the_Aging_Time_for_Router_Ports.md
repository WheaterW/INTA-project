(Optional) Setting the Aging Time for Router Ports
==================================================

The aging time of router ports can be set based on the network stability to balance the update of multicast entries and network changes.

#### Context

Router ports are used to send users' Report messages to and receive multicast data packets from upstream devices. After IGMP snooping is enabled on a device, the device can dynamically learn a router port and monitor multicast data delivered by its upstream devices. If the network is congested or is unstable and the router port does not receive any IGMP general query message or Protocol Independent Multicast (PIM) Hello message within the aging time, the device deletes the router port from the router port list, causing multicast data interruption. To address this problem, you can prolong the aging time of the router port.

If the aging time is not configured for the router port, the device will age multicast entries based on the default aging time. If a router port does not receive any IGMP Query message with a non-0.0.0.0 source address or any PIM Hello message within the aging time, the system considers the router port invalid and deletes it from the forwarding table.

Before enabling dynamic router port learning, you must enable IGMP snooping globally and in the corresponding VLAN or VSI.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**igmp-snooping router-learning**](cmdqueryname=igmp-snooping+router-learning)
   
   
   
   Dynamic router port learning is enabled.
4. Run [**igmp-snooping router-aging-time**](cmdqueryname=igmp-snooping+router-aging-time) *router-aging-time*
   
   
   
   The router port aging time is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.