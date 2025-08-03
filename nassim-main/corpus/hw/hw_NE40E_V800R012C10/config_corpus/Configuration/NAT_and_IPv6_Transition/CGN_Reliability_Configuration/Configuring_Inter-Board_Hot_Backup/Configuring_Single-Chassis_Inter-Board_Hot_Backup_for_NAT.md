Configuring Single-Chassis Inter-Board Hot Backup for NAT
=========================================================

You can configure the single-chassis inter-board hot backup function to improve the reliability of a NAT device.

#### Context

When a NAT device is equipped with two service boards, you can configure the active and standby service boards in the same chassis on the NAT device to implement inter-board backup on the single device. The inter-board backup mechanism verifies that the data stored on the active NAT service board is consistent with that stored on the standby NAT service board. If the active NAT service board fails, an active/standby NAT service board switchover is performed to ensure that services are running properly. In this situation, users are unaware of this fault.


#### Procedure

1. (Optional) Configure value-added service management (VSM) high availability (HA) hot backup functions.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-ha hot-backup enable**](cmdqueryname=service-ha+hot-backup+enable)
      
      
      
      HA hot standby is enabled.
   3. Run [**service-ha delay-time**](cmdqueryname=service-ha+delay-time) *delay-time*
      
      
      
      The delay time is set for VSM HA hot backup.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      On a device with the [**service-ha delay-time**](cmdqueryname=service-ha+delay-time) command run, session entries can be backed up only if the active time of session traffic is longer than the delay time configured for VSM HA hot backup.
   4. (Optional) Run [**service-ha preempt-time**](cmdqueryname=service-ha+preempt-time) *preempt-time*
      
      
      
      The delay for active/standby revertive switching is set.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      When the active service board recovers, it takes over services from the standby service board after the specified delay elapses.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure a service-location group that implements single-chassis inter-board VSM HA hot backup.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
      
      
      
      A service-location group is created, and its view is displayed.
   3. Run [**location**](cmdqueryname=location) **slot** *slot-id* **backup** **slot** *backup-slot-id*
      
      
      
      The service-location group is bound to the CPUs of the active and standby service boards.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Create a service-instance group and bind it to the service-location group.
   1. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
      
      
      
      A service-instance group is created, and its view is displayed.
   2. Run [**service-location**](cmdqueryname=service-location) *service-location-id* [ **weight** *weight-value* ]
      
      
      
      The service-location group is bound to the service-instance group.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Bind a NAT instance to a service-instance group.
   1. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
      
      
      
      The NAT instance view is displayed.
   2. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
      
      
      
      The NAT instance is bound to the service-instance group.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Each NAT instance group can only be bound to a single service-instance group. Different NAT instance groups can be bound to the same service-instance group.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.