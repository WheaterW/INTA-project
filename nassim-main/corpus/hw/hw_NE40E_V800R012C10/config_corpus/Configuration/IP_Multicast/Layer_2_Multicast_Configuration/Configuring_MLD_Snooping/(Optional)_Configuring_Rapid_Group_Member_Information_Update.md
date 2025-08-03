(Optional) Configuring Rapid Group Member Information Update
============================================================

Rapid group member information update can be configured to enable devices to quickly update Layer 2 multicast entries generated based on Report/Done messages received from group members, improving the multicast data forwarding efficiency.

#### Context

After rapid group member information update is configured on a device, the device can quickly respond to a received a Join or Done message, improving user experience. Using this feature, the device implements the following functions:

* Setting the aging time of group members: After receiving a Report/Done message for a multicast group from a host, the device creates an entry. The entry ages out after a period of time. The aging time of entries should be properly set so that the device can update Layer 2 multicast entries in time. This improves system performance.
* Prompt join: After the prompt join function is enabled on a device, the device applies for resources for multicast groups in advance. When the device receives an MLD Report message for a multicast group, it can immediately forward multicast data for the multicast group, improving the speed at which hosts join the multicast group and shortening the delay for the device to respond to the Report message.
* Prompt leave: After prompt leave is enabled on a device, the device deletes the forwarding entry corresponding to a member port from the multicast forwarding table immediately after the device receives an MLD Done message from the member port, without waiting for a Report message before the aging timer expires.
  
  This function is applicable only when each interface in a VLAN or VSI has only one receiver host.

The preceding functions are optional and can be configured in any order. Configure one or more functions as required. Default settings are recommended.

Before configuring rapid group member information update, enable MLD snooping both globally and in a VLAN or VSI.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Configure rapid member information update to improve multicast data forwarding efficiency. The following configurations are parallel. You can configure one or more items as required. For details, see [Table 1](#EN-US_TASK_0172367923__tab_dc_vrp_l2mc_cfg_007501).
   
   
   
   **Table 1** Configuring rapid group member update
   | Function | Configuration Procedure | Description |
   | --- | --- | --- |
   | Dynamic member aging time | * Run the [**mld-snooping query-interval**](cmdqueryname=mld-snooping+query-interval) *query-interval* command to set an interval at which a querier sends General Query messages. * Run the [**mld-snooping robust-count**](cmdqueryname=mld-snooping+robust-count) *robust-count* command to set the number of times the querier sends Group-specific Query messages. * Run the [**mld-snooping max-response-time**](cmdqueryname=mld-snooping+max-response-time) *max-response-time* command to set the maximum time for a querier to wait for responses from downstream hosts. * Run the [**mld-snooping lastmember-queryinterval**](cmdqueryname=mld-snooping+lastmember-queryinterval) *lastmember-queryinterval* command to set an interval at which a querier sends Group-specific Query messages. | * After receiving a Report message from a downstream host, the device sets the dynamic member port aging time based on following formula: Dynamic member port aging time = *robust-count* x *query-interval* + *max-response-time*. * After receiving an MLD Done message from a downstream host, the device sets the member interface aging time based on the following formula: Member interface aging time = *robust-count* x *lastmember-queryinterval*. * If the querier receives a Report message within a period (*robust-count* Ã *lastmember-queryinterval*), it continues to maintain the memberships for the group. Otherwise, the querier considers that there is no member of the group left and no longer maintains the memberships for the group. The aging time of multicast group members on the Layer 2 device must be the same as that on the upstream Layer 3 device. Otherwise, multicast data transmission between the Layer 2 and Layer 3 networks is affected. |
   | Prompt join | Run the [**l2-multicast ipv6 fast-channel**](cmdqueryname=l2-multicast+ipv6+fast-channel) [ **source-address** *source-address* *mask-length* ] **group-address** *group-address* *mask-length* command to configure prompt join. | After prompt join is configured, the device will reserve system resources for a specific multicast group. As a result, if there is no member of this multicast group, system performance will be affected. |
   | Prompt leave | Run the [**mld-snooping prompt-leave**](cmdqueryname=mld-snooping+prompt-leave) [ **group-policy** { *acl6-number* | **acl6-name** *acl6-name* } ] command to configure prompt leave in a VLAN or VSI for member ports. | **group-policy** *acl6-number* or **group-policy** **acl6-name** *acl6-name* specifies the range of multicast groups for which prompt leave is enabled. If **group-policy** *acl6-number* or **group-policy** **acl6-name** *acl6-name* is set and a Done message is received from the VLAN or VSI, the multicast entry corresponding to the member port is deleted.  Before setting *acl6-number* or **acl6-name** *acl6-name*, configure rules for the ACL to be referenced so that Done messages are filtered based on the ACL rules in the VLAN or VSI. |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.