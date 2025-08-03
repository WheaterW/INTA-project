Associating a VRRP Group with a BFD Session to Implement a Rapid Master/Backup VRRP Switchover
==============================================================================================

You can associate a VRRP group with a BFD session. If the status of a BFD session changes, BFD notifies the VRRP group of the change. After receiving the notification, the VRRP group rapidly performs a master/backup VRRP switchover.

#### Context

If a link between devices in a VRRP group fails, VRRP Advertisement packets cannot be sent to negotiate the master/backup status. A backup device preempts the master role only after a period of three times the interval at which VRRP Advertisement packets are sent. During this period, service data is lost. To resolve this problem, associate the VRRP group with a BFD session. A BFD session is established between the master and backup devices to rapidly detect faults. If a fault occurs, BFD rapidly notifies the VRRP group of the fault and triggers a master/backup VRRP switchover.

[Table 1](#EN-US_TASK_0172361774__tab_dc_vrp_vrrp_cfg_011601) describes VRRP and BFD association modes.

**Table 1** VRRP and BFD association modes
| Association Mode | Usage Scenario | Type of Associated BFD Session | Impact Mode | BFD Support |
| --- | --- | --- | --- | --- |
| Association between a VRRP group and a common BFD session | A backup device monitors the status of the master device in a VRRP group. A common BFD session is used to monitor the link between the master and backup devices. | Static BFD sessions or static BFD sessions with automatically negotiated discriminators | The VRRP group adjusts priorities according to the BFD session status and determines whether to perform a master/backup switchover according to the adjusted priorities. | VRRP-enabled devices must support BFD. |
| Association between a VRRP group and link and peer BFD sessions | The master and backup devices monitor the link and peer BFD sessions simultaneously. A link BFD session is established between the master and backup devices. A peer BFD session is established between a downstream switch and each VRRP device. BFD helps determine whether the fault occurs between the master device and downstream switch or between the backup device and downstream switch. | Static BFD sessions or static BFD sessions with automatically negotiated discriminators | If the link or peer BFD session goes down, BFD notifies the VRRP group of the fault. After receiving the notification, the VRRP group immediately performs a master/backup VRRP switchover. | VRRP-enabled devices must support BFD. |


Perform the following steps on the device that needs to perform a rapid master/backup VRRP switchover:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The view of the interface on which the VRRP group is configured is displayed.
3. Perform any of the following operations as required:
   
   
   * To associate a VRRP group with a common BFD session, run the following command:
     
     Run the  [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **bfd-session** { *bfd-session-id* | **session-name** *bfd-configure-name* } [ **increased** *value-increased* | **reduced** *value-reduced* ] command to associate the VRRP group with a common BFD session.
   * To associate a VRRP group with a link or peer BFD session, perform the following steps:
     
     1. Run the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **bfd-session** { *bfd-session-id* | **session-name** *bfd-configure-name* } [ **peer** | **link** ] command to associate the VRRP group with a link or peer BFD session.
     2. Run the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track link-bfd down-number** *down-number* command to set a threshold for the number of times that the link BFD session tracked by the VRRP group goes down.
        
        When the number of times that the link BFD session tracked by the VRRP group goes down reaches or exceeds the *down-number*, the VRRP group performs a master/backup switchover.When associating a VRRP group with a BFD session, note the following points:
   * If **session-name** *bfd-configure-name* is specified, the VRRP group can be associated only with static BFD sessions with automatically negotiated discriminators or static BFD session discriminators.
   * If *bfd-session-id* is specified, the VRRP group can be associated only with static BFD sessions.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a VRRP group is bound to an mVRRP group, the mVRRP group maintains the VRRP group's status. The VRRP group is unable to track any BFD sessions.
   * When a VRRP group is associated with a link BFD session and a peer BFD session, a backup device's status becomes Master if the backup device detects the peer BFD session's status change before detecting the link BFD session's status change. The backup device's status changes from Master to Initialize after it detects the link BFD session's status is changed to down. To prevent the preceding situation, run the [**min-tx-interval**](cmdqueryname=min-tx-interval) command in the BFD session view to set the interval for sending link BFD control packets to be less than the interval for sending peer BFD control packets.
   * In VPLS aggregation scenarios, you must configure a link BFD session of the BFD for Default IP VSI type on the UPE and bind the session to an mPW. The default IP addresses on the PE-AGGs must also be different from those on the UPE and NPEs. For configuration details, see [**bfd bind peer-ip default-ip vsi**](cmdqueryname=bfd+bind+peer-ip+default-ip+vsi). You must configure a link BFD session of the BFD for Default IP type on the NPEs. For configuration details, see [**bfd bind peer-ip default-ip**](cmdqueryname=bfd+bind+peer-ip+default-ip).
4. (Optional) Run the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track link-bfd down-number** *down-number* command to set the maximum number of link BFD sessions allowed in the down state tracked by the VRRP group.
   
   
   
   If the number of associated link BFD sessions that are in the down state reaches the value specified by *down-number*, the VRRP group performs a master/backup switchover.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.