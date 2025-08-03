Enabling IGMP Snooping Report Message Suppression
=================================================

The querier function enables a device to send Query messages on behalf of an upstream device and respond to IGMP messages sent by a downstream device.

#### Context

If a large number of hosts exist on an IGMP-enabled multicast network, processing redundant IGMP messages increases the burden on the upstream PE and wastes network bandwidth.

To solve this problem, enable IGMP snooping Report message suppression on a Layer 2 device. With the function, when sending Report or Leave messages to the upstream multicast device for the first time, the device sends a robustness variable (2 by default, and can be configured using the [**igmp-snooping robust-count**](cmdqueryname=igmp-snooping+robust-count) command) number of Report or Leave message copies. Subsequently, when periodically responding to IGMP Query messages from the upstream multicast device, the Layer 2 device sends only one IGMP Report message to the upstream multicast device, regardless of the number of user ports in the corresponding multicast group.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**igmp-snooping report-suppress**](cmdqueryname=igmp-snooping+report-suppress)
   
   
   
   IGMP snooping Report message suppression is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.