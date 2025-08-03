Configuring a Unicast VRRP Group
================================

This section describes how to configure a unicast VRRP group to implement the master/backup status negotiation between two devices on a Layer 3 network.

#### Usage Scenario

Common VRRP is multicast VRRP and only allows multicast VRRP Advertisement packets to be sent. Multicast VRRP Advertisement packets, however, can be forwarded within only one broadcast domain (for example, one VLAN or VSI). Therefore, common VRRP groups apply only to Layer 2 networks. This limitation means that common VRRP does not apply to Layer 3 devices that need to negotiate their master/backup status using VRRP. After a unicast VRRP group is configured on two devices on a Layer 3 network, the master device in this group sends unicast VRRP Advertisement packets to the backup device through the Layer 3 network, implementing the master/backup status negotiation between the two devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
   
   
   
   The loopback interface view is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **peer-ip** *ip-address* [ **source-ip** *source-ip-value* ]
   
   
   
   Unicast VRRP is enabled, a unicast VRRP group is created, and a peer IP address and a source IP address are configured for this group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Configuring a source IP address is recommended. If no source IP address is configured, the device listens to the source IP addresses in all VRRP packets, which poses security risks.
   * The·peer·IP·address·and·source·IP·address·cannot·be·the·same.
4. (Optional) Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **authentication-mode** { **md5** *md5-key* | [**hmac-sha256**](cmdqueryname=hmac-sha256) *hmac-sha256* }
   
   
   
   An authentication mode is configured for unicast VRRP Advertisement packets.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The same authentication mode and key must be configured on the two devices in a unicast VRRP group. If different authentication modes and keys are configured, the master/backup status negotiation fails.
   
   For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. For security purposes, you are advised to use the HMAC-SHA256 algorithm.
5. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **priority** *priority-value*
   
   
   
   A priority is configured for the device in the unicast VRRP group.
6. (Optional) Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **timer** **advertise** *advertise-interval*
   
   
   
   An interval at which unicast VRRP Advertisement packets are sent is configured.
7. (Optional) Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **preempt-mode** **timer** **delay** *delay-time*
   
   
   
   A preemption delay is set for the backup device in the unicast VRRP group.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After creating a unicast VRRP group, perform the following operations to implement rapid master/backup VRRP switchovers and further improve network reliability:

* Associate the unicast VRRP group with a VRRP-disabled interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
     
     The view of the interface on which the unicast VRRP group is configured is displayed.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **interface** *interface-type* *interface-number* [ **increased** *value-increased* | **reduced** *value-reduced* ]
     
     The unicast VRRP group is associated with a specified VRRP-disabled interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure the unicast VRRP group to track an interface monitoring group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
     
     The view of the interface on which the unicast VRRP group is configured is displayed.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **monitor-group** *monitor-group-name* **failure-ratio** *failure-ratio-value* { [ **reduced** *reduced-value* ] | **link** }
     
     The unicast VRRP group is configured to track an interface monitoring group. When the link failure ratio on the access or network side reaches a specified threshold, the unicast VRRP group performs a master/backup switchover.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) A unicast VRRP group can track three interface monitoring groups at the same time.
  + A unicast VRRP group can track two interface monitoring groups on the access side in normal mode (**link** is not specified). When the link failure ratio on the access side reaches a specified threshold, the VRRP group reduces the priority of the local device to trigger the remote device to preempt the Master state.
  + A VRRP group can track one interface monitoring group on the network side in link mode. When the link failure ratio on the network side reaches a specified threshold, the local device in the VRRP group changes to the Initialize state and sends a VRRP Advertisement packet carrying a priority of 0 to the remote device to trigger the remote device to preempt the Master state.
* Configure the unicast VRRP group to track a route monitoring group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
     
     The view of the interface on which the unicast VRRP group is configured is displayed.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **route-monitor-group** *route-monitor-group-name* **failure-ratio** *failure-ratio-value* [ **link** | [ **reduced** *priority-value* ] ]
     
     The unicast VRRP group is configured to track a route monitoring group. When the link failure ratio on the access or network side reaches a specified threshold, the unicast VRRP group performs a master/backup switchover.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.