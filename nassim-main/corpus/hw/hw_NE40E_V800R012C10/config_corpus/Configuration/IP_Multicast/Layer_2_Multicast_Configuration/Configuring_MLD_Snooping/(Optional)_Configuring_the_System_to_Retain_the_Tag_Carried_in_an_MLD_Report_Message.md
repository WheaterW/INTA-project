(Optional) Configuring the System to Retain the Tag Carried in an MLD Report Message
====================================================================================

When an L2VPN accesses an L3VPN, you can configure the system to retain the tag carried in an MLD Report message so that the message can be normally processed when being forwarded from an L2VE sub-interface to an L3VE QinQ VLAN tag termination sub-interface.

#### Context

The system receives an MLD Report message carrying one tag from a VPLS PW or VLL PW. When the message is forwarded from an L2VE sub-interface to an L3VE QinQ VLAN tag termination sub-interface, the message cannot be processed. To resolve this issue, run the [**l2-multicast ipv6 protocol-packet encapsulation raw**](cmdqueryname=l2-multicast+ipv6+protocol-packet+encapsulation+raw) command to enable the system to reserve the original tag and add another tag to an MLD Report message when the message is forwarded from an L2VE sub-interface to an L3VE QinQ VLAN tag termination sub-interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   The VSI view is displayed.
3. Run [**l2-multicast ipv6 protocol-packet encapsulation raw**](cmdqueryname=l2-multicast+ipv6+protocol-packet+encapsulation+raw)
   
   
   
   The system is enabled to retain the tag carried in an MLD Report message.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.