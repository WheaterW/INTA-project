Configuring the Single-Chassis Inter-Board Hot Backup Function for a DS-Lite Device
===================================================================================

The single-chassis inter-board hot backup function improves the reliability of a DS-Lite device.

#### Context

If two service boards are installed on a DS-Lite device, the service boards can be configured to work in active/standby mode in the same chassis to implement inter-board backup. The inter-board backup mechanism verifies that the data stored on the active service board is consistent with that stored on the standby service board. If the active service board fails, an active/standby service board switchover is performed to ensure that services are running properly. In this situation, services are properly transmitted, and users are unaware of the fault.


#### Procedure

1. (Optional) Configure value-added service management (VSM) high availability (HA) hot backup functions.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-ha hot-backup enable**](cmdqueryname=service-ha+hot-backup+enable)
      
      
      
      The HA hot backup function is enabled.
   3. Run [**service-ha delay-time**](cmdqueryname=service-ha+delay-time) *delay-time*
      
      
      
      The delay time is set for VSM HA hot backup.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      On a device with the [**service-ha delay-time**](cmdqueryname=service-ha+delay-time) *delay-time* command run, session entries can be backed up only if the active time of session traffic is longer than the delay time configured for VSM HA hot backup.
   4. (Optional) Run [**service-ha preempt-time**](cmdqueryname=service-ha+preempt-time) *preempt-time*
      
      
      
      A preemption delay is set.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      You can set a preemption delay for the former master service board to become the master again after it recovers.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure a service-location group that implements single-chassis inter-board VSM HA hot backup.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
      
      
      
      A service-location group is created, and the service-location group view is displayed.
   3. Run [**location**](cmdqueryname=location) **slot** *slot-id* **backup** **slot** *backup-slot-id* 
      
      
      
      The CPUs of the active and standby service boards are bound to the service-location group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Before hot backup is configured, the NE40E must be equipped with two service boards.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Create a service-instance group and bind it to the service-location group.
   1. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
      
      
      
      A service-instance group is created, and the service-instance group view is displayed.
   2. Run [**service-location**](cmdqueryname=service-location) *service-location-id* [ **weight** *weight-value* ]
      
      
      
      The service-location group is bound to the service-instance group.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Bind a DS-Lite instance to a service-instance group.
   1. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
      
      
      
      The DS-Lite instance view is displayed.
   2. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
      
      
      
      The DS-Lite instance is bound to the service-instance group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      One DS-Lite instance can only be bound to one service-instance group. Different DS-Lite instances can be bound to the same service-instance group.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.