Enabling Remote Backup for IGMP Snooping Services
=================================================

This section describes how to enable remote backup for IGMP snooping services to implement IGMP snooping entry consistency on the master and backup devices.

#### Context

In a master/backup E-Trunk scenario, dual-device IGMP snooping hot backup enables the master device to back up IGMP snooping entries to the backup device through an RBS channel. In so doing, the system controls and manages multicast services more flexibly, improving multicast service reliability. To enable dual-device IGMP snooping hot backup to take effect, you must enable remote backup for IGMP snooping services.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   An RBP is created, and the RBP view is displayed.
3. Run [**service-type igmp-snooping**](cmdqueryname=service-type+igmp-snooping)
   
   
   
   Remote backup is enabled for IGMP snooping services.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) **trunk-id.subnumber**
   
   
   
   The Eth-Trunk sub-interface view is displayed.
6. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   The RBP is bound to the interface.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.