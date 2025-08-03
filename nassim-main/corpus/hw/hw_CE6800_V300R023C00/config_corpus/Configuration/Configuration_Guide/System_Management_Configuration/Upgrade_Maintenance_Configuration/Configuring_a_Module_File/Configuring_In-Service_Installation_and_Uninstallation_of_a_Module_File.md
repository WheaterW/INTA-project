Configuring In-Service Installation and Uninstallation of a Module File
=======================================================================

Configuring In-Service Installation and Uninstallation of a Module File

#### Prerequisites

Before configuring in-service installation and uninstallation of a module file, you have completed the following task:

* [Prepare for upgrade maintenance.](gx_upgrade_cfg_0005.html)

#### Context

If a desired module file does not exist in the system, you can perform in-service installation of the module file so that the functions of the module file can be used. In this process, services are not interrupted. You can also perform in-service uninstallation of a module file if you no longer need it.![](public_sys-resources/note_3.0-en-us.png) 

Ensure that the uploaded files are correct by comparing the file sizes and dates.




#### Procedure

1. Upload a module file to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Perform in-service module installation.
   
   
   ```
   [install-module](cmdqueryname=install-module) module-name
   ```

#### Verifying the Configuration

* Run the [**dir**](cmdqueryname=dir) *file-name* command in the **$\_install\_mod** directory to check whether the file information contains the name of the uploaded module file (\*.MOD).
* Run the [**display module-information verbose**](cmdqueryname=display+module-information+verbose) command to check whether the displayed information is consistent with the name of the installed module file and whether the module file takes effect.

#### Follow-up Procedure

If a module file is no longer needed, run the [**uninstall-module**](cmdqueryname=uninstall-module) { *module-name* | **all** } command to perform in-service uninstallation of the module file.