Enabling Remote Backup for IGMP
===============================

This section describes how to enable remote backup for IGMP to implement IGMP entry consistency between the master and backup devices.

#### Context

In a master/backup E-Trunk scenario, IGMP dual-device hot backup enables IGMP entry backup between the master and backup devices through a remote backup service (RBS) channel, ensuring multicast service continuity. To enable IGMP dual-device hot backup to take effect, you must enable remote backup for IGMP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   An RBP is created, and the RBP view is displayed.
3. Run [**service-type igmp**](cmdqueryname=service-type+igmp)
   
   
   
   Remote backup is enabled for IGMP.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.