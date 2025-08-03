(Optional) Configuring Transparent Transmission of Protocol Messages
====================================================================

To prevent IGMP snooping proxy-enabled upstream and downstream devices from learning multicast forwarding entries from each other, configure them to transparently transmit protocol messages.

#### Context

If IGMP snooping proxy is enabled on upstream and downstream devices, they will learn the same multicast entries and continuously exchange IGMP messages, causing multicast entries not to age. Consequently, multicast protocol messages and traffic are forwarded unnecessarily, wasting bandwidth.

To solve this problem, configure these devices to transparently transmit protocol messages. After this function is enabled, these devices can transparently transmit IGMP messages received from a router port to other router ports, instead of learning the multicast entries created based on these IGMP messages. This function ensures a proper aging of multicast entries.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**igmp-snooping proxy router-protocol-pass**](cmdqueryname=igmp-snooping+proxy+router-protocol-pass)
   
   
   
   The IGMP snooping proxy-enabled device is enabled to transparently transmit protocol messages in the VLAN or VSI.
4. (Optional) Run [**igmp-snooping proxy-uplink-port remote-peer**](cmdqueryname=igmp-snooping+proxy-uplink-port+remote-peer) *remote-peer-addr*
   
   
   
   The device is disabled from sending IGMP Query messages to the specified IGMP snooping proxy uplink interface.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.