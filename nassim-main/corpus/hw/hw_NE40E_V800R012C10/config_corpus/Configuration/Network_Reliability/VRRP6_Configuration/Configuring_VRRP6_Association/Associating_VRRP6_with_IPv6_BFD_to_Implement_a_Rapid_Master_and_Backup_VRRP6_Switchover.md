Associating VRRP6 with IPv6 BFD to Implement a Rapid Master/Backup VRRP6 Switchover
===================================================================================

You can associate a VRRP6 group with an IPv6 BFD session. If the status of the IPv6 BFD session changes, IPv6 BFD notifies the VRRP6 group of the change. After receiving the notification, the VRRP6 group rapidly performs a master/backup VRRP6 switchover.

#### Context

A VRRP6 group uses VRRP6 Advertisement packets to negotiate the master/backup VRRP6 status, implementing device backup. If a link between devices in a VRRP6 group fails, VRRP6 Advertisement packets cannot be sent to negotiate the master/backup status. A backup device preempts the master role only after a period of three times the interval at which VRRP6 Advertisement packets are sent. During this period, service traffic is still sent to the master device. As a result, the service traffic is lost.

To resolve this issue, associate the VRRP6 group with an IPv6 BFD session. [Table 1](#EN-US_TASK_0172361859__tab_dc_vrp_vrrp6_cfg_012201) describes VRRP6 and IPv6 BFD association modes.

**Table 1** VRRP6 and IPv6 BFD association modes
| Association Mode | Usage Scenario | VRRP6 Status Change | Device Requirements |
| --- | --- | --- | --- |
| Association between a VRRP6 group and a common IPv6 BFD session | A backup device monitors the status of the master device in a VRRP6 group. A common IPv6 BFD session is used to monitor the link between the master and backup devices. | If the common IPv6 BFD session goes down, IPv6 BFD notifies the VRRP6 group of the fault. After receiving the notification, the VRRP6 group changes VRRP6 priorities and determines whether to perform a master/backup VRRP6 switchover. | VRRP6-enabled devices must support IPv6 BFD. |
| Association between a VRRP6 group and link and peer IPv6 BFD sessions | The master and backup devices monitor both link and peer IPv6 BFD sessions. A link IPv6 BFD session is established between the master and backup devices. A peer IPv6 BFD session is established between a downstream switch and each VRRP6 device. IPv6 BFD helps the VRRP6 group detect faults in the link between a VRRP6 device and the downstream switch. | If the link or peer IPv6 BFD session goes down, IPv6 BFD notifies the VRRP6 group of the fault. After receiving the notification, the VRRP6 group immediately performs a master/backup VRRP6 switchover. | VRRP6-enabled devices and the downstream switch must support IPv6 BFD. |


Perform the following steps on each device in a VRRP6 group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The view of the interface where the VRRP6 group resides is displayed.
3. Run any of the following commands:
   
   
   * To associate the VRRP6 group with a common IPv6 BFD session, run the [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **track** **bfd-session** { *bfd-session-id* | **session-name** *bfd-configure-name* } [ **increased** *value-increased* | **reduced** *value-reduced* ] command.
   * To associate the VRRP6 group with a link or peer IPv6 BFD session, run the [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **track** **bfd-session** { *bfd-session-id* | **session-name** *bfd-configure-name* } [ **peer** | **link** ] command.
   
   When associating a VRRP6 group with an IPv6 BFD session, note the following points:
   
   * If the **session-name** *bfd-configure-name* parameter is specified, the VRRP6 group can be associated only with static IPv6 BFD sessions with automatically negotiated discriminators or static IPv6 BFD session discriminators.
   * If *bfd-session-id* is specified, the VRRP6 group can be associated only with static IPv6 BFD sessions.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a VRRP6 group is bound to an mVRRP6 group, the mVRRP6 group maintains the VRRP6 group's status. The VRRP6 group cannot track any IPv6 BFD sessions.
   * When a VRRP6 group is associated with a link IPv6 BFD session and a peer IPv6 BFD session, a backup device's status becomes Master if the backup device detects the peer IPv6 BFD session's status change before detecting the link IPv6 BFD session's status change. The backup device's status changes from Master to Initialize after it detects the peer IPv6 BFD session's status change. To prevent the preceding case, run the [**min-tx-interval**](cmdqueryname=min-tx-interval) command in the BFD session view to set the interval at which link BFD control packets are sent to be less than the interval at which peer BFD control packets are sent.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.