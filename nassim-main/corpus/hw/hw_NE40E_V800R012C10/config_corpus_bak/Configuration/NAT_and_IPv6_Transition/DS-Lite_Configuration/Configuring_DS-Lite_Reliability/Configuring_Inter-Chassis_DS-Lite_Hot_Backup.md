Configuring Inter-Chassis DS-Lite Hot Backup
============================================

You can configure the dual-device inter-chassis DS-Lite hot backup to improve the reliability of a DS-Lite device.

#### Context

If multiple DS-Lite devices with service boards exist on a network, you can configure a service board on a master device and a service board on a backup device to implement inter-chassis backup. The inter-chassis backup mechanism ensures that the data stored on CPUs of the service boards on the master and backup devices is consistent. If the master device, the service board on it, or the link between the master and backup devices fails, a master/backup switchover is performed to ensure that services run properly. In this situation, services are properly transmitted, and users are unaware of the fault.

* If multiple DS-Lite devices with service boards exist on a network and provide access services for a limited number of users, you can apply inter-chassis 1:1 backup. In this case, when the service board on the master device processes services, the service board on the backup device does not work. The service board on the master device backs up the user, session, and address pool entries to the service board on the backup device. Once the master device, the service board on it, or the link between the master and backup devices fails, the backup device becomes the master and processes services.
* If multiple DS-Lite devices with service boards exist on a network and provide access services for a large number of users, you can apply inter-chassis 1+1 backup. In this case, both service boards on the master and backup devices process services and back up their user, session, and address pool entries to each other. Once a service board, a device, or the link between the master and backup devices fails, the service board on the other device processes all services.

Perform the following steps on the master and backup devices:![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Configure the same DS-Lite parameters on both devices.
* Configure the same name and ID of a DS-Lite instance on both devices.
* Configure the same DS-Lite functions on both devices.
* Inter-board backup and inter-chassis backup cannot be configured simultaneously.



#### Procedure

1. Configure basic high availability (HA) hot backup functions.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-ha hot-backup enable**](cmdqueryname=service-ha+hot-backup+enable)
      
      
      
      HA hot backup is enabled.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure a Virtual Router Redundancy Protocol (VRRP) group for dual-device inter-chassis HA hot backup.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This section provides commonly used steps for configuring VRRP. For more information, see "VRRP Configuration."
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **virtual-ip** *virtual-address*
      
      
      
      A VRRP group is created, and a virtual IP address is assigned to the VRRP group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The *virtual-router-id* and *virtual-address* values configured on both devices must be the same.
   4. Run [**admin-vrrp vrid**](cmdqueryname=admin-vrrp+vrid) *virtual-router-id* [ **ignore-if-down** ]
      
      
      
      The VRRP group is configured as a management VRRP (mVRRP) backup group.
      
      
      
      The VRRP type must be mVRRP.
   5. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **priority** *priority-value*
      
      
      
      The priority of a device in the VRRP group is set.
      
      
      
      The DS-Lite devices must be assigned different VRRP priorities. The DS-Lite device with a higher priority serves as the master one.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure an HA backup group for dual-device inter-chassis HA hot backup and bind it to a VRRP group.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
      
      
      
      A service-location group is created, and the service-location group view is displayed
      
      
      
      The *service-location-id* value configured on both devices must be the same.
   3. Run [**location**](cmdqueryname=location) **slot** *slot-id* 
      
      
      
      The CPU of the service board is bound in the service-location group view.
   4. Run [**remote-backup interface**](cmdqueryname=remote-backup+interface) *interface-type* *interface-number* [**peer**](cmdqueryname=peer) *ip-address* [ **authentication-key** *key-value* **hash-algorithm** **hmac-sha256** ]
      
      
      
      A VRRP outbound interface is configured on the local device for inter-chassis backup, and the IP address of the peer device is specified.
   5. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The service-location group is bound to the VRRP group.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Create a service instance group and associate the service instance group with the HA backup group.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
      
      
      
      A service-instance group is created, and the service-instance group view is displayed.
   3. Run [**service-location**](cmdqueryname=service-location) *service-location-id* [ **weight** *weight-value* ]
      
      
      
      The service-location group is bound to the service-instance group.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Bind a DS-Lite instance to a service-instance group to implement dual-device inter-chassis HA hot backup for DS-Lite services.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* **id** *id*
      
      
      
      The DS-Lite instance view is displayed.
   3. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
      
      
      
      The DS-Lite instance is bound to the service-instance group.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
6. Associate a service-instance group with a VRRP group on an interface on which mVRRP is configured.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **service-location** *service-location-id* [ **reduced** *value-reduced* ]
      
      
      
      The VRRP group can track the status of a service-location group so that VRRP priorities can be adjusted.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.