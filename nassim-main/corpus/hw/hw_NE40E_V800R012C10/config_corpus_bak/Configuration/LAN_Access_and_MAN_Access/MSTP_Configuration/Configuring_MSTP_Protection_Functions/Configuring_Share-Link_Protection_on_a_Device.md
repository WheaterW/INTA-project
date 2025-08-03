Configuring Share-Link Protection on a Device
=============================================

The share-link protection function on a device helps automatically transition to the Rapid Spanning Tree Protocol (RSTP) working mode. It can also be used together with root protection to avoid network loops.

#### Context

Share-link protection is used in the scenario where a device is dual homed to a network.

When a share link fails, share-link protection forcibly changes the working mode of a local device to RSTP. This function can also be used together with root protection to avoid network loops.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp process**](cmdqueryname=stp+process) *process-id*
   
   
   
   The MSTP process view is displayed.
3. Run [**stp link-share-protection**](cmdqueryname=stp+link-share-protection)
   
   
   
   Share-link protection is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.