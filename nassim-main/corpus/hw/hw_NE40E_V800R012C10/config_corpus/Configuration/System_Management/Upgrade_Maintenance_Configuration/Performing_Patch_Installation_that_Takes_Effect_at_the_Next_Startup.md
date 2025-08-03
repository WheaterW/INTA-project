Performing Patch Installation that Takes Effect at the Next Startup
===================================================================

Performing patch installation that takes effect at the next startup can optimize device performance and add new features to the device.

#### Applicable Environment

To optimize device performance or add new features to a device, use either of the following methods to install a patch file:

* Performing in-service patch installation: The patch files take effect after a command is run, without having to restart the device. For details, see [Performing In-service Patch Installation](dc_vrp_upgrade_cfg_0015.html).
* Performing patch installation that takes effect at the next startup: The patch files take effect after the device has been restarted.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This feature is supported only on the Admin-VS but takes effect on all VSs.

#### Pre-configuration Tasks

Before performing patch installation that takes effect at the next startup, complete the following task:

* Logging in to a device where patch installation needs to be performed



[Uploading a Patch File](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_upgrade_cfg_0051.html)

This part describes how to upload a patch file to the storage medium of a device.

[Specifying the Patch to Be Loaded at the Next Startup](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_upgrade_cfg_0022.html)

If the patch file uploaded to the storage medium does not need to take effect immediately, you can specify the uploaded patch file as the one to be used at the next startup. Then, the patch file will take effect after the device is restarted.

[Restarting a Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_upgrade_cfg_0041.html)

The specified patch file to be used at the next startup will take effect only after the device is restarted.

[Verifying the Configuration of In-Service Patch Installation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_upgrade_cfg_0052.html)

This section describes how to check whether a patch file has been installed onto a device.