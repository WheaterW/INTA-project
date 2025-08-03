Installing a Patch File
=======================

After a patch file has been uploaded to the storage medium of a device, the patch file needs to be installed to the patch area in the memory.

#### Context

The system that is just started successfully needs to perform internal restoration. Installing or uninstalling a patch during the restoration process may fail. In this situation, run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether the internal restoration has completed. If the command output contains current configurations, the internal restoration has completed, and you can install or uninstall a patch as needed.


#### Procedure

1. In the user view, run [**patch load**](cmdqueryname=patch+load) *file-name* [**all**](cmdqueryname=all) [**run**](cmdqueryname=run)
   
   
   
   The patch file is loaded.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When a patch file is loaded, the system checks whether the patch version is the same as the system software version. If the patch file version is different from the system software version, the system prompts that the patch file loading fails.
   
   If there are running patch files in the system during non-incremental patching, the system displays a patch file installation failure. The [**patch delete**](cmdqueryname=patch+delete) **all** command needs to be run to delete the running patch files.

#### Follow-up Procedure

If a patch file needs to be deleted after having been installed, run the [**patch delete all**](cmdqueryname=patch+delete+all) command.