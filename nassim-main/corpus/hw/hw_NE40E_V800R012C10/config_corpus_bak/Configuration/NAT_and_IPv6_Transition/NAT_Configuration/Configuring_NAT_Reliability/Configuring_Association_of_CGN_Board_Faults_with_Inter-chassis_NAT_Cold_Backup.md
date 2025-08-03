Configuring Association of CGN Board Faults with Inter-chassis NAT Cold Backup
==============================================================================

You can associate CGN board faults with inter-chassis NAT cold backup to improve NAT device reliability.

#### Context

Two NAT devices equipped with CGN boards cannot detect the board faults. To resolve this issue, bind interfaces to an HA status monitoring group. The NAT devices can then detect the running status of the CGN boards. If one board fails, a master/backup device switchover is triggered, preventing services from being interrupted for a long time.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The association function takes effect only on [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595).

Do not configure the same public and private IP addresses for the master and backup CGN devices. Otherwise, packet loss may occur due to faults on access-side interfaces.



#### Procedure

1. Configure basic HA group functions.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
      
      
      
      An HA group is created, and its view is displayed.
   3. Run [**location**](cmdqueryname=location) **slot** *slot-id* [ **backup** **slot** *backup-slot-id* ]
      
      
      
      The active/standby information of the HA group is configured.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Create an HA status monitoring group and bind it to the service-location group.
   1. Run [**monitor-location-group**](cmdqueryname=monitor-location-group) *group-name*
      
      
      
      An HA status monitoring group is created, and its view is displayed.
   2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
      
      
      
      The HA status monitoring group is bound to the service-location group.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      One HA status monitoring group can be bound to up to 64 service-location groups, and one service-location group can be shared by multiple HA status monitoring groups.
   3. Run [**down-number**](cmdqueryname=down-number) *number*
      
      
      
      A status change threshold is configured for the HA status monitoring group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The status change of an HA status monitoring group must meet threshold requirements. When the number of faulty HA backup groups is greater than or equal to the threshold, the HA status monitoring group becomes Down, and services are switched to the backup device. When the number is less than the threshold, the interface status is restored.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Bind an interface to the HA status monitoring group.
   1. Run [**interface**](cmdqueryname=interface) *interface-name* *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   2. Run [**track monitor-location-group**](cmdqueryname=track+monitor-location-group) *group-name*
      
      
      
      The interface is bound to the HA status monitoring group.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.