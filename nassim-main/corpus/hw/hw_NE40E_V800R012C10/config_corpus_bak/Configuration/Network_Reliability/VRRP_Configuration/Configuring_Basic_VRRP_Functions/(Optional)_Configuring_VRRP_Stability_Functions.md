(Optional) Configuring VRRP Stability Functions
===============================================

To help a VRRP group work stably, enable the preemption function, set a preemption delay, and specify an interval at which VRRP Advertisement packets are sent. The configuration can minimize impact of network flapping resulted from frequent master/backup VRRP switchovers on data forwarding.

#### Context

A VRRP group performs a master/backup switchover if the master device fails or a network is busy. After the master device or network communication recovers, a new master device is selected.

If a network flaps, service packets are adversely affected. VRRP stability functions can be configured to improve VRRP stability, minimizing network interruptions or packet loss resulted from frequent master/backup VRRP switchovers. [Table 1](#EN-US_TASK_0172361755__tab_dc_vrp_vrrp_cfg_010601) describes VRRP stability functions.

**Table 1** VRRP stability functions
| Basic Function | Usage Scenario |
| --- | --- |
| [Setting a preemption delay](#EN-US_TASK_0172361755__step_01) | Frequent master/backup switchovers on an unstable network may cause double master devices to coexist or hosts to learn incorrect master MAC address. To maintain the stable master/backup status, configure either of the following preemption modes:   * Immediate preemption: A backup device immediately preempts the Master state after the master device fails. The preemption delay is 0s. This setting minimizes the service interruption time. * Delayed preemption: The master device preempts the Master state a specified preemption delay after the master device recovers. During the preemption delay, other services (such as route convergence) are restored. The preemption delay helps minimize packet loss ratios. |
| [Setting the interval at which VRRP Advertisement packets are sent](#EN-US_TASK_0172361755__step_02) | Heavy network traffic or timer setting differences between devices may cause a backup device to incorrectly preempt the Master state. To prevent this issue, set a large value for the interval at which VRRP Advertisement packets are sent by the master device. |
| [Setting a recovery delay](#EN-US_TASK_0172361755__step_03) | If a VRRP-enabled interface status changes frequently, the VRRP status on the interface frequently alternates between Up and Down. To prevent this issue, set a recovery delay. A VRRP group responds to a VRRP interface Up event only after a specified recovery delay. The recovery delay helps prevent VRRP status flapping caused by frequent interface status changes. |
| [Setting a delay for sending the first packet of a VRRP group](#EN-US_TASK_0172361755__cmd75111873620) | When the device or board is restarted and the traffic is heavy, the backup device may not receive protocol packets from the master device immediately after the restart. As a result, the backup device becomes the master device due to a timeout, causing VRRP status flapping or the configured preemption delay not to take effect. To prevent this issue, you can set a delay for sending the first packet of the VRRP group. |



#### Procedure

* Set a preemption delay for a device in a VRRP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the VRRP group is configured is displayed.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **preempt-mode** **timer** **delay** *delay-time*
     
     
     
     A preemption delay is set for a device in a group.
     
     
     
     You can run the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **preempt-mode** **disable** command to configure non-preemption mode for devices in a VRRP group. When a VRRP group works in non-preemption mode, a backup device (regardless of priority) cannot preempt the master role as long as the master device is working properly.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When the IP address owner recovers from a fault, it immediately becomes the master device despite the configured delay. The preemption delay takes effect for backup devices in a group when they try to become the master device. Therefore, the preemption delay is meaningless for an IP address owner. Consequently, in a VRRP group that needs to be configured with a preemption delay, the master device cannot be configured as the IP address owner.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set an interval at which VRRP Advertisement packets are sent.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp timer-advertise learning enable**](cmdqueryname=vrrp+timer-advertise+learning+enable)
     
     
     
     The device is enabled to learn the interval at which VRRP Advertisement packets are sent.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     During a master/backup switchover, do not disable the device from learning the interval. Otherwise, two master devices may coexist.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the VRRP group is configured is displayed.
  4. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **timer** **advertise** *advertise-interval*
     
     
     
     An interval for sending VRRP Advertisement packets is set.
     
     Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **timer** **advertise** **millisecond** *millisecond-interval*
     
     An interval (in ms) for sending VRRP Advertisement packets is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a recovery delay.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the VRRP group is configured is displayed.
  3. Run [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) *delay-value*
     
     
     
     A recovery delay is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) command run in the system view takes effect on all VRRP groups on the same device.
     
     The [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) command run in the interface view takes effect on all VRRP groups on the same interface. If the [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) command is run in both the system and interface views, the setting in the interface view prefers.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a delay for sending the first packet of a VRRP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp first-packet-delay**](cmdqueryname=vrrp+first-packet-delay) *delay-value*
     
     
     
     A delay for sending the first packet of a VRRP group is set.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.