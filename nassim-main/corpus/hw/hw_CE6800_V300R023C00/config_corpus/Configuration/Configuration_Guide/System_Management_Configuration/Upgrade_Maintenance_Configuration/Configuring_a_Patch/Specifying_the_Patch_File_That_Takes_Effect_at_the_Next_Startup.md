Specifying the Patch File That Takes Effect at the Next Startup
===============================================================

Specifying the Patch File That Takes Effect at the Next Startup

#### Prerequisites

Before specifying the patch file that takes effect at the next startup, you have completed the following task:

* [Prepare for upgrade maintenance](gx_upgrade_cfg_0005.html).

#### Context

While a device is running, you may need to modify the device's system software. For example, you may need to remove system defects or add new functions based on service requirements. You can specify the patch file that takes effect at the next startup to optimize software.

![](public_sys-resources/note_3.0-en-us.png) 

Ensure that the uploaded files are correct by comparing the file sizes and dates.



#### Procedure

1. Upload a patch file to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Specify the patch file that takes effect at the next startup.
   
   
   ```
   [startup patch](cmdqueryname=startup+patch) patch-name all
   ```
3. Restart the device.
   
   
   ```
   [reboot](cmdqueryname=reboot)
   ```

#### Verifying the Configuration

* Run the [**dir**](cmdqueryname=dir) *file-name* command to check whether the file information contains the name of the uploaded patch file (\*.PAT).
* Run the [**display patch-information verbose**](cmdqueryname=display+patch-information+verbose) command to check whether **State** is displayed as **Running**.
* Run the [**display startup**](cmdqueryname=display+startup) command to check whether the displayed information is consistent with the file name of the installed patch.

#### Follow-up Procedure

To disable a patch file from taking effect at the next startup, run the [**reset patch-configure**](cmdqueryname=reset+patch-configure) **next-startup** command to delete the patch configuration for the next startup.