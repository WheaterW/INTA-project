Performing In-Service Patch Installation
========================================

Performing in-service patch installation on a device allows the current system software on the device to be upgraded without service interruption.

#### Applicable Environment

You can use either of the following methods to install patches:

* Performing in-service patch installation: The patch files take effect after a command is run, without having to restart the device.
* Performing patch installation that takes effect at the next startup: The installed patch files take effect after the device is restarted. For details, see [Performing Patch Installation that Takes Effect at the Next Startup](dc_vrp_upgrade_cfg_0040.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This feature is supported only on the Admin-VS but takes effect on all VSs.

#### Pre-configuration Tasks

Before performing in-service patch installation, complete the following task:

* Logging in to a device to be upgraded



[Uploading a Patch File](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_upgrade_cfg_0017.html)

This part describes how to upload a patch file to the storage medium of a device.

[Installing a Patch File](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_upgrade_cfg_0018.html)

After a patch file has been uploaded to the storage medium of a device, the patch file needs to be installed to the patch area in the memory.

[Verifying the Configuration of In-Service Patch Installation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_upgrade_cfg_0021.html)

This section describes how to check whether a patch file has been installed onto a device.