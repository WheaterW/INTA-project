(Optional) Configuring VRRP6 Stability Functions
================================================

To help a VRRP6 group work stably, enable the preemption function, set a preemption delay, and configure an interval for sending VRRP6 Advertisement packets. The configuration can minimize the impact of network flapping resulting from frequent master/backup VRRP6 switchovers on data forwarding.

#### Context

A VRRP6 group performs a master/backup switchover if the master device fails or if a network is busy. After the original master device recovers or network communication is restored, the VRRP6 group reselects the master device based on device priorities.

If a network frequently flaps, service traffic may fail to be forwarded. To resolve this issue, configure VRRP6 stability functions to improve VRRP6 group stability. This minimizes network interruptions or packet loss caused by frequent master/backup VRRP6 switchovers. [Table 1](#EN-US_TASK_0172361851__tab_dc_vrp_vrrp6_cfg_010501) describes VRRP6 stability functions.

**Table 1** VRRP6 stability functions
| Function Item | Description |
| --- | --- |
| [Enabling VRRP6 preemption and configuring a preemption delay](#EN-US_TASK_0172361851__step_01) | If a network is unstable, configure either of the following preemption modes to improve master/backup state stability, and to prevent dual masters from coexisting and hosts from learning an incorrect MAC address of the master device due to frequent master/backup switchovers:   * Immediate preemption: The preemption delay is 0s, indicating that a backup device immediately preempts the master role after the master device fails. This mode minimizes service interruption duration. * Delayed preemption: The master device preempts the master role after a specified preemption delay following recovery. Specifically, the master device waits for other services to recover (for example, route convergence is complete) before it preempts the master role to minimize packet loss. |
| [Configuring an interval for sending VRRP6 Advertisement packets](#EN-US_TASK_0172361851__step_02) | A backup device may fail to receive VRRP6 Advertisement packets before the configured timeout period expires, leading to incorrect preemption of the master role due to heavy network traffic or timer differences between devices. To resolve this problem, set the interval for sending VRRP6 Advertisement packets on the master device to a larger value. |
| [Configuring a VRRP6 status recovery delay](#EN-US_TASK_0172361851__step_03) | Frequent changes to the status of the interface on which a VRRP6 group resides result in the VRRP6 status frequently flapping. To resolve this problem, configure a VRRP6 status recovery delay. Once set, the VRRP6 group only responds to a VRRP6 interface up event after the specified status recovery delay expires, preventing frequent VRRP6 status flapping caused by frequent interface status changes. |
| [Configuring a delay for sending the first packet of a VRRP6 group](#EN-US_TASK_0172361851__cmd75111873620) | When the device or board is restarted and the traffic is heavy, the backup device may not receive protocol packets from the master device immediately after the restart. As a result, the backup device becomes the master device due to a timeout, causing VRRP status flapping or the configured preemption delay not to take effect. To prevent this issue, you can set a delay for sending the first packet of the VRRP group. |



#### Procedure

* Enable VRRP6 preemption and configure a preemption delay.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which a VRRP6 group resides is displayed.
  3. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **preempt-mode** **timer** **delay** *delay-time*
     
     
     
     A preemption delay is configured for the device in the VRRP6 group.
     
     When a VRRP6 group works in immediate preemption mode, a backup device in the group can immediately preempt the master role when its priority is higher than that of the master device.
     
     You can run the [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **preempt-mode** **disable** command to configure the non-preemption mode for devices in a VRRP6 group. When a VRRP6 group works in non-preemption mode, a backup device (regardless of priority) cannot preempt the master role as long as the master device is working properly.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When the IP address owner recovers from a fault, it immediately becomes the master device despite the configured delay. A preemption delay is a period of time during which the original master device in the backup state is waiting to preempt the master role, and it does not apply to the IP address owner. Consequently, in a VRRP6 group that needs to be configured with a preemption delay, the master device cannot be configured as the IP address owner.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an interval for sending VRRP6 Advertisement packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which a VRRP6 group resides is displayed.
  3. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **timer** **advertise** *advertise-interval*
     
     
     
     An interval at which the master device in the VRRP6 group sends VRRP6 Advertisement packets is configured.
  4. (Optional) Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **timer** **advertise** **millisecond** *millisecond-interval*
     
     
     
     An interval (in milliseconds) for sending VRRP6 Advertisement packets is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a VRRP6 status recovery delay.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which a VRRP6 group resides is displayed.
  3. Run [**vrrp6 recover-delay**](cmdqueryname=vrrp6+recover-delay) *delay-value*
     
     
     
     A VRRP6 status recovery delay is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a delay for sending the first packet of a VRRP6 group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp first-packet-delay**](cmdqueryname=vrrp+first-packet-delay) *delay-value*
     
     
     
     A delay for sending the first packet of the VRRP6 group is configured.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.