(Optional) Configuring Transparent Transmission of Protocol Messages
====================================================================

To prevent MLD snooping proxy-enabled upstream and downstream devices from learning multicast forwarding entries from each other, configure them to transparently transmit protocol messages.

#### Context

If MLD snooping proxy is enabled on upstream and downstream devices, they will learn the same multicast entries and continuously exchange MLD messages, causing multicast entries not to age. Consequently, multicast protocol messages and traffic are forwarded unnecessarily, wasting bandwidth.

To solve this problem, configure these devices to transparently transmit protocol messages. After this function is enabled, these devices can transparently transmit MLD messages received from a router port to other router ports, instead of learning the multicast entries created based on these MLD messages. This function ensures a proper aging of multicast entries.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**mld-snooping proxy router-protocol-pass**](cmdqueryname=mld-snooping+proxy+router-protocol-pass)
   
   
   
   The device enabled with MLD snooping proxy is configured to transparently transmit protocol messages in the VLAN or VSI.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   In a VSI scenario, if MLD snooping proxy is configured on one end of a PW, IPv6 addresses on the same network segment must be configured for the physical interfaces to which the two PW interfaces recurse. Otherwise, the sending of Group-specific Query messages is affected.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.