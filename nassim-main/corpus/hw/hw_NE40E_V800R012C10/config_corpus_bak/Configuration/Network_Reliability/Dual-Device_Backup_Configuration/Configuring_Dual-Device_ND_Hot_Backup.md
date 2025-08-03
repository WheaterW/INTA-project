Configuring Dual-Device ND Hot Backup
=====================================

This section describes how to enable dual-device ND hot backup to back up ND entries between devices. This allows fast service switching if a network node or link fails, enhancing service reliability.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0183753474__fig_dc_vrp_dhcp_server_cfg_002003), users access Device A and Device B over a switch. A Virtual Router Redundancy Protocol for IPv6 (VRRP6) group is configured on Device A and Device B, with Device A as the master device and Device B as the backup device.

In normal circumstances, Device A forwards both upstream and downstream traffic. If Device A or the link between Device A and the switch fails, a master/backup VRRP6 switchover is triggered and Device B becomes the master device. Then, Device B needs to advertise a network segment route to network-side devices so that downstream traffic is directed from the network side to Device B. However, if Device B has not learned ND entries from user-side devices, the downstream traffic is interrupted. Device B can properly forward downstream traffic only after it learns ND entries from user-side devices.

If ND entries are not synchronized from Device A to Device B and a master/backup switchover occurs, downstream traffic may be interrupted because Device B fails to learn ND entries from users-side devices in time. To resolve this problem, deploy dual-device ND hot backup on Device A and Device B.

**Figure 1** Dual-device ND hot backup  
![](figure/en-us_image_0183753901.png)  

Perform the following steps on the devices that back up ND entries from each other:


#### Procedure

1. Configure basic VRRP6 group functions.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
      
      
      
      The interface view for a VRRP6 group is displayed.
   3. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* [ **virtual-ip** *virtual--address* [ link-local ] ]
      
      
      
      A VRRP6 group is created and a virtual IPv6 address is assigned.
   4. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **preempt-mode** **timer** **delay** *delay-time*
      
      
      
      A preemption delay is set for devices in the VRRP6 group.
      
      
      
      You are advised to set the preemption delay to 0 on a backup device to allow it to immediately preempt the master role and set the preemption delay to a non-0 value on the master device.
   5. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **priority** *priority-value*
      
      
      
      A priority is configured for a device in the VRRP6 group.
   6. (Optional) Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **timer** **advertise** *advertise-interval*
      
      
      
      The interval for sending VRRP6 Advertisement packets is configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The interval for sending VRRP6 Advertisement packets cannot be less than the time required for a master/backup switchover. Otherwise, VRRP may intermittently go down during a switchover. You are advised to set the interval for sending VRRP6 Advertisement packets to more than 1 second.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the interface view.
2. Configure an RBS.
   1. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *remote-backup-service-name*
      
      
      
      An RBS is created, and the RBS view is displayed.
   2. (Optional) Run [**batch-backup**](cmdqueryname=batch-backup) **service-type** **nd** **now**
      
      
      
      The device is enabled to immediately back up user services configured in the RBS.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the RBS view.
3. Configure an RBP.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      An RBP is created, and the RBP view is displayed.
   2. Run [**peer-backup**](cmdqueryname=peer-backup) **hot**
      
      
      
      A backup mode is configured for user information backup between devices.
   3. Run [**vrrp6-id**](cmdqueryname=vrrp6-id) *vrid* **interface** { *interface-name* | *interface-type* *interface-number* }
      
      
      
      The RBP is bound to the VRRP6 group.
      
      The *vrid* parameter specifies the ID of a VRRP6 group. The ID must be the same as the VRRP6 group's ID configured using the [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* [ **virtual-ip** *virtual-address* ] command in the interface view.
   4. Run [**backup-id**](cmdqueryname=backup-id) *backup-id* [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
      
      
      
      A user backup ID is set for the RBP, and the RBP is associated with the RBS.
      
      The *backup-id* parameter specifies a user backup ID for the RBP. You can use a backup ID and an RBS to determine an RBP. The backup IDs configured for the same RBP must be the same on the master and backup devices and can no longer be configured for other RBPs.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the RBP view.
4. Enable the remote backup function for ND.
   1. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP view is displayed.
   2. Run [**service-type nd**](cmdqueryname=service-type+nd)
      
      
      
      The remote backup function for ND is enabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the RBP view.
5. Bind the RBP to an interface.
   1. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
      
      
      
      The interface view for configuring the VRRP6 group is displayed.
   2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
      
      
      
      The RBP is bound to the interface.
      
      
      
      The name of the RBP to be bound to an interface must be the same as the name of the RBP created using the [**remote-backup-profile**](cmdqueryname=remote-backup-profile) command in the system view.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.