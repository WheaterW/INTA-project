Configuring In-Service Installation and Uninstallation of a Patch
=================================================================

Configuring In-Service Installation and Uninstallation of a Patch

#### Prerequisites

Before configuring in-service installation and uninstallation of a patch, you have completed the following task:

* [Prepare for upgrade maintenance](gx_upgrade_cfg_0005.html).

#### Context

While a device is running, you may need to modify the device's system software. For example, you may need to remove system defects or add new functions based on service requirements. Configuring in-service installation of a patch helps you optimize software without interrupting device running.

![](public_sys-resources/note_3.0-en-us.png) 

Ensure that the uploaded files are correct by comparing the file sizes and dates.



#### Procedure

1. Upload a patch file to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Perform in-service patch installation.
   
   
   ```
   [patch load](cmdqueryname=patch+load) patch-name all run
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * During patch installation, the device checks whether the patch version is consistent with the system software version. If they are not consistent, the device fails to install the patch.
   * For a non-incremental patch file, if a running patch file exists, the device displays a message indicating a failure to install the patch. In this case, run the [**patch delete**](cmdqueryname=patch+delete) **all** command to delete the existing patch file.
   * This command can be used to install a hot or cold patch. After installing a cold patch, you need to restart the device for the patch to take effect. If you run the [**reset patch-configure**](cmdqueryname=reset+patch-configure) **next-startup** command to delete the patch file from the device after the cold patch is installed, you do not need to restart the device.

#### Verifying the Configuration

* Run the [**dir**](cmdqueryname=dir) *file-name* command to check whether the file information contains the name of the uploaded patch file (\*.PAT).
* Run the [**display patch-information verbose**](cmdqueryname=display+patch-information+verbose) command to check whether **State** is displayed as **Running**.
* Run the [**display startup**](cmdqueryname=display+startup) command to check whether the displayed information is consistent with the file name of the installed patch.

#### Follow-up Procedure

If an exception occurs after a patch is installed, run the [**patch delete**](cmdqueryname=patch+delete) **all** command to delete the patch file and uninstall the patch.