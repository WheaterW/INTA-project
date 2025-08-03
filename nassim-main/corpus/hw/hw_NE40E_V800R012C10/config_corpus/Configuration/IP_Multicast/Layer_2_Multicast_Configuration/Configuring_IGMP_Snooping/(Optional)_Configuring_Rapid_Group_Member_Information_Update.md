(Optional) Configuring Rapid Group Member Information Update
============================================================

Rapid group member information update can be configured to enable devices to quickly update Layer 2 multicast entries generated based on Report/Leave messages received from group members, improving the multicast data forwarding efficiency.

#### Context

After rapid group member information update is configured on a device, the device can quickly respond to a received a Join or Leave message, improving the multicast service operating efficiency and user experience.

* Setting the aging time for group members: After receiving a Report/Leave message for a multicast group, the device creates a multicast forwarding entry. The entry ages after a period of time. The aging time of entries should be properly set so that the device can update Layer 2 multicast entries in time. This improves system performance.
* Prompt Join: After the prompt join function is enabled on a device, the device applies for resources for multicast groups in advance. When the device receives an IGMP Report message for a multicast group, it can immediately forward multicast data for the multicast group, improving the speed at which hosts join the multicast group and shortening the delay for the device to respond to the Report message.
* Prompt leave: If a device with prompt leave enabled receives an IGMP Leave message from a member port, the device immediately deletes the entry corresponding to the port from the multicast forwarding table without waiting for a Report message within the age timer.
  
  This function applies only to the scenario where IGMPv2 messages can be processed and each interface in a VLAN or VSI has only one receiver host.

The preceding functions are optional and can be configured in any order. Configure one or more functions as required. Default settings are recommended.

Before configuring rapid group member information update, enable IGMP snooping both globally and in a VLAN or VSI.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
3. Configure rapid member information update to improve multicast data forwarding efficiency. The following configurations are parallel. You can configure one or more items as required. For details, see [Table 1](#EN-US_TASK_0172367841__tab_dc_vrp_l2mc_cfg_000501).
   
   
   
   **Table 1** Rapid group member update
   | Function | Configuration Procedure | Description |
   | --- | --- | --- |
   | Dynamic member aging time | * Run the [**igmp-snooping query-interval**](cmdqueryname=igmp-snooping+query-interval) *query-interval* command to set an interval at which a querier sends General Query messages. * Run the [**igmp-snooping robust-count**](cmdqueryname=igmp-snooping+robust-count) *robust-count* command to set the number of Group-specific Query messages that a querier sends. * Run the [**igmp-snooping max-response-time**](cmdqueryname=igmp-snooping+max-response-time) *max-response-time* command to set the maximum time for a querier to wait for a response from downstream hosts. * Run the [**igmp-snooping lastmember-queryinterval**](cmdqueryname=igmp-snooping+lastmember-queryinterval) *lastmember-queryinterval* command to set an interval at which a querier sends Group-specific Query messages. | * After receiving a Report message from a downstream host, the device sets the dynamic member aging time based on following formula: Dynamic member aging time = *robust-count* x *query-interval* + *max-response-time*. * When receiving a Leave message from a downstream host, an interface calculates the member aging time based on the following formula: *robust-count* x *lastmember-queryinterval*. An IGMPv1 host does not send a Leave message when leaving a multicast group. Therefore, this configuration is valid only when IGMPv2 messages can be processed in the VLAN or VSI. * If the querier receives a Report message within a period (*robust-count* Ã *lastmember-queryinterval*), it continues to maintain the memberships for the group. Otherwise, the querier considers that there is no member of the group left and no longer maintains the memberships for the group. The aging time of multicast group members on the Layer 2 device must be the same as that on the upstream Layer 3 device. Otherwise, multicast data transmission between the Layer 2 and Layer 3 networks is affected. |
   | Prompt join | Run the [**l2-multicast fast-channel**](cmdqueryname=l2-multicast+fast-channel) [ **source-address** *source-address* { *mask* | *mask-length* } ] **group-address** *group-address* { *mask* | *mask-length* } command to configure prompt join. | After prompt join is configured, the device will reserve system resources for a specific multicast group. As a result, if there is no member of this multicast group, system performance will be affected. |
   | Prompt leave | Run the [**igmp-snooping prompt-leave**](cmdqueryname=igmp-snooping+prompt-leave) [ **group-policy** { *acl-number* | **acl-name** *acl-name* } ] command to configure prompt leave for member ports in the VLAN or VSI. By default, no member port is allowed to promptly leave a multicast group. | **group-policy** *acl-number* or **group-policy** **acl-name** *acl-name* sets the range of multicast groups that member ports are allowed to promptly leave. If **group-policy** *acl-number* or **group-policy** **acl-name** *acl-name* is set and a Leave message is received from a member port in the VLAN or VSI, the multicast entry corresponding to the member port is deleted.  Before setting *acl-number* or **acl-name** *acl-name*, configure an ACL to be referenced so that Leave messages are filtered based on the ACL in the VLAN or VSI. |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.