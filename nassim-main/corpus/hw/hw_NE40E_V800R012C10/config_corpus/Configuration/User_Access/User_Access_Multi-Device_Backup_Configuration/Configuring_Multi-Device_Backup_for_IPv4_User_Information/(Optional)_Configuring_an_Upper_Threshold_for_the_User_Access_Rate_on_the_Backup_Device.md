(Optional) Configuring an Upper Threshold for the User Access Rate on the Backup Device
=======================================================================================

This section describes how to configure an upper threshold for the user access rate on the backup device in a dual-device hot backup scenario.

#### Context

In a dual-device hot backup scenario, users will be triggered to go online on the backup device after they go online on the master device. You can configure an upper threshold for the user access rate on the backup device, so that the system dynamically adjusts the user access rate based on the CPU usage, with the rate never exceeding the upper threshold.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**peer-backup rui-trigger-speed**](cmdqueryname=peer-backup+rui-trigger-speed) *trigger-speed*
   
   
   
   An upper threshold is configured for the user access rate on the backup device in a dual-device hot backup scenario.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command must be run on both the master and backup devices.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.