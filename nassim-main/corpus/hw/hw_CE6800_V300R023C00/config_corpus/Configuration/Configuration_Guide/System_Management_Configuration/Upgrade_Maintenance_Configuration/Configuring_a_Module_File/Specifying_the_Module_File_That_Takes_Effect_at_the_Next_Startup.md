Specifying the Module File That Takes Effect at the Next Startup
================================================================

Specifying the Module File That Takes Effect at the Next Startup

#### Prerequisites

Before specifying the module file that takes effect at the next startup, you have completed the following task:

* [Prepare for upgrade maintenance.](gx_upgrade_cfg_0005.html)

#### Context

If a desired module file does not exist in the system, you can configure the module file to take effect at the next startup so that the module file is installed after the device is restarted.![](public_sys-resources/note_3.0-en-us.png) 

Ensure that the uploaded files are correct by comparing the file sizes and dates.




#### Procedure

1. Upload a module file to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Specify the module file that takes effect at the next startup.
   
   
   ```
   [install-module](cmdqueryname=install-module) module-name next-startup
   ```
3. Restart the device.
   
   
   ```
   [reboot](cmdqueryname=reboot)
   ```

#### Verifying the Configuration

* Run the [**dir**](cmdqueryname=dir) *file-name* command in the **$\_install\_mod** directory to check whether the file information contains the name of the uploaded module file (\*.MOD).
* Run the [**display module-information next-startup**](cmdqueryname=display+module-information+next-startup) command to check information about the next-startup module file.
* Run the [**display module-information verbose**](cmdqueryname=display+module-information+verbose) command to check whether the displayed information is consistent with the name of the installed module file and whether the module file takes effect.

#### Follow-up Procedure

If a module file is not needed for next startup, run the [**uninstall-module**](cmdqueryname=uninstall-module) *module-name* **next-startup** command to remove the module file from the next-startup module file list.

If all module files are not needed for next startup, run the [**uninstall-module next-startup all**](cmdqueryname=uninstall-module+next-startup+all) command to remove all module files from the next-startup module file list.