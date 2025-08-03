Configuring Automatic Blocking of User Access Domains and Boards on a BRAS
==========================================================================

This section describes how to configure automatic blocking of user access domains and boards on a BRAS so that the BRAS can automatically block the user access domains and boards and log out online users.

#### Context

In normal situations, you must manually block user access domains and boards on a device and log out online users before a device upgrade, and then run the [**reboot**](cmdqueryname=reboot) command to restart the device after users go offline. Alternatively, you can run the [**bras auto-upgrade enable**](cmdqueryname=bras+auto-upgrade+enable) command to enable a device to automatically block user access domains and boards and log out online users.

After this function is enabled, you must run the [**reboot**](cmdqueryname=reboot) command to restart the device.


#### Procedure

1. Run the [**bras auto-upgrade enable**](cmdqueryname=bras+auto-upgrade+enable) command to enable automatic blocking of user access domains and boards on a BRAS.
2. Run the [**reboot**](cmdqueryname=reboot) command to restart the system.
   
   
   
   The [**bras auto-upgrade enable**](cmdqueryname=bras+auto-upgrade+enable) command is not stored in the configuration file of the system, and therefore must be run each time you need this function.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.