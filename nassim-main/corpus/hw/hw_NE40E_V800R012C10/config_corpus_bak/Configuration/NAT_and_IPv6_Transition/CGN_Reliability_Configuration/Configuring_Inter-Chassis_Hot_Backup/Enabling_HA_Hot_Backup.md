Enabling HA Hot Backup
======================

HA hot backup must be enabled globally to implement inter-chassis hot backup.

#### Context

After HA hot backup is enabled, user tables and session tables are backed up between chassis on the master and backup devices. In load balancing over inter-chassis hot backup, global address pool entries are also backed up between the master and backup devices.


#### Procedure

1. Run system-view
   
   
   
   The system view is displayed.
2. Run [**service-ha hot-backup enable**](cmdqueryname=service-ha+hot-backup+enable)
   
   
   
   The HA hot backup function is enabled.
   
   If this function is not enabled, centralized backup is cold backup, and distributed backup is warm backup.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.