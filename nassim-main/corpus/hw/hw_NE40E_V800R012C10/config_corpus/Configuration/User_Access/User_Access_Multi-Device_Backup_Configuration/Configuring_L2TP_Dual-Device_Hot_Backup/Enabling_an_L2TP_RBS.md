Enabling an L2TP RBS
====================

To implement dual-device L2TP service hot backup, an RBS must be enabled on the devices that back up each other in the RBP view.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   The RBP view is displayed.
3. Run [**service-type**](cmdqueryname=service-type) **l2tp**
   
   
   
   An L2TP RBS is enabled.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If information about an L2TP tunnel, an L2TP session, or a PPPoE session has been backed up, the [**undo service-type l2tp**](cmdqueryname=undo+service-type+l2tp) command cannot be run.
   * Before deploying LAC hot backup, you must configure a base value for the L2TP Tunnel ID on the active/standby ME device to ensure that the tunnel ID is unique on each ME device.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.