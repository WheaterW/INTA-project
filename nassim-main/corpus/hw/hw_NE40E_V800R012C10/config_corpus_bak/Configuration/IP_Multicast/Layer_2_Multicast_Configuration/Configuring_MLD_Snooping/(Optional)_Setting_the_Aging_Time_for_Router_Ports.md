(Optional) Setting the Aging Time for Router Ports
==================================================

The aging time of router ports can be set based on the network stability to balance the update of multicast entries and network changes.

#### Context

Router ports are used to send users' Report messages to and receive multicast data packets from upstream devices. After Multicast Listener Discovery (MLD) snooping is enabled on a device, the device can dynamically learn router ports and monitor multicast data delivered by upstream devices. If the network is congested or is unstable and a router port does not receive any General MLD Query message or PIM Hello message within the aging time, the device deletes the router port from the router port list, causing multicast data interruption. To address this problem, you can increase the router port aging time.

If no aging time is set for router ports, the device will age multicast entries based on the default aging time. If a router port does not receive any MLD Query message or PIM Hello message within the aging time, the system considers the router port invalid and deletes it from the forwarding table.

Before configuring dynamic router port learning, you must enable MLD snooping globally and in the corresponding VLAN or VSI.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**mld-snooping router-learning**](cmdqueryname=mld-snooping+router-learning)
   
   
   
   Dynamic router port learning is enabled.
4. Run [**mld-snooping router-aging-time**](cmdqueryname=mld-snooping+router-aging-time) *router-aging-time*
   
   
   
   The router port aging time is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.