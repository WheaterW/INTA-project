Specifying the Independent-Hardware-Release Package That Takes Effect at the Next Startup
=========================================================================================

Specifying the Independent-Hardware-Release Package That Takes Effect at the Next Startup

#### Prerequisites

Before specifying the independent-hardware-release package that takes effect at the next startup, you have completed the following task:

* [Prepare for upgrade maintenance](gx_upgrade_cfg_0005.html).

#### Context

After uploading an independent-hardware-release package to the storage medium, you may not want the package to take effect immediately. In this case, you can specify the independent-hardware-release package that takes effect at the next startup, and then restart the device to support the new hardware.

Alternatively, a device may be running the basic software package that supports the new hardware but the basic software package cannot be used for some reasons. In this case, you can roll back the basic software package and specify the independent-hardware-release package that takes effect at the next startup to enable the old version to support the new hardware.


#### Procedure

1. Upload an independent-hardware-release package to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Specify the independent-hardware-release package that takes effect at the next startup.
   
   
   ```
   [startup extended-system-software](cmdqueryname=startup+extended-system-software) { file-name } &<1-4>
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   A maximum of four independent-hardware-release packages can be specified at a time. These packages are independent of each other. If one of these packages fails to be installed, the system is automatically restored to the state before the installation attempt. This does not affect the installation of the other packages.
3. Restart the device.
   
   
   ```
   [reboot](cmdqueryname=reboot)
   ```

#### Verifying the Configuration

Run the [**display startup**](cmdqueryname=display+startup) command to check whether the displayed independent-hardware-release package information is the same as the information of the installed package.


#### Follow-up Procedure

If the board is no longer needed, run the [**reset extended-system-software next-startup**](cmdqueryname=reset+extended-system-software+next-startup) { *file-name* } &<1-4> command and restart the device to uninstall the independent-hardware-release package to save storage space.