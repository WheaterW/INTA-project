(Optional) Setting the Aging Time for Entries Triggered by Multicast Traffic
============================================================================

Setting the aging time for Layer 2 multicast forwarding entries triggered by multicast traffic can balance the forwarding efficiency and system performance.

#### Context

When a multicast source no longer sends multicast data for some multicast groups, the device needs to delete the (S, G) entries corresponding to the multicast groups. Therefore, the device needs to continuously detect the existence of the multicast traffic sent by the multicast source. After the aging time is set, if the device does not receive any multicast data sent by a multicast source within the aging time, the device deletes the multicast entry of the multicast source to improve device performance.

Before setting the aging time for entries triggered by multicast traffic, enable IGMP snooping both globally and in a specified VLAN/VSI.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Run [**l2-multicast source-lifetime**](cmdqueryname=l2-multicast+source-lifetime) *lifetime*
   
   
   
   The aging time is set for entries triggered by multicast traffic in the VLAN/VSI.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.