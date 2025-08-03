(Optional) Configuring the Command Timestamp Function
=====================================================

You can enable a device to record the date and time when commands are executed.

#### Procedure

* Enable the system command timestamp function.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**timestamp enable**](cmdqueryname=timestamp+enable)
     
     
     
     The system command timestamp function is enabled on the device.
     
     After this function is enabled, the device displays the date and time each time a display command is run.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This function takes effect only on display commands.
* Enable the session command timestamp function.
  1. Run [**terminal command timestamp**](cmdqueryname=terminal+command+timestamp)
     
     
     
     The command timestamp function is enabled for an existing session.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + After this function is enabled, the device displays the current system date and time once you enter any command and press **Enter**.
     + The [**terminal command timestamp**](cmdqueryname=terminal+command+timestamp) command takes effect on commands executed only within the existing user session. After you log out of and log in to the device, the command timestamp function becomes invalid and needs to be reconfigured.
     + If you run the [**timestamp enable**](cmdqueryname=timestamp+enable) command and then the [**undo terminal command timestamp**](cmdqueryname=undo+terminal+command+timestamp) command, the timestamps are displayed after you run display commands, but are not displayed after you run non-display commands.