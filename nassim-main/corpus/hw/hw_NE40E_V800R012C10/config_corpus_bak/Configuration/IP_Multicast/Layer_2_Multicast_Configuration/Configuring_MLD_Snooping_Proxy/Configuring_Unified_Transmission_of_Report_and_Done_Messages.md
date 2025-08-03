Configuring Unified Transmission of Report/Done Messages
========================================================

Unified transmission of Report/Done messages enables a device to summarize Report/Done messages of downstream hosts and send them to an upstream device in a unified manner. This saves bandwidth resources on the network side.

#### Context

Redundant MLD messages waste network-side bandwidth resources, especially when there are a large number of hosts on a network. To resolve this issue, configure unified transmission of Report/Done messages, allowing the device to respond only one MLD Report message to an MLD Query message of a group sent by the upstream device, regardless of the number of interfaces that have joined the same multicast group.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**mld-snooping proxy**](cmdqueryname=mld-snooping+proxy)
   
   
   
   MLD snooping proxy is enabled.
   
   
   
   MLD snooping proxy provides two functions: querier and unified message transmission. With the querier function, a Layer 2 device can send MLD Query messages on behalf of the upstream device. With the unified message transmission function, a Layer 2 device can receive MLD Report and Done messages from downstream devices and send them in a unified manner.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.