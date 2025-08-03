Specifying the Patch to Be Loaded at the Next Startup
=====================================================

If the patch file uploaded to the storage medium does not need to take effect immediately, you can specify the uploaded patch file as the one to be used at the next startup. Then, the patch file will take effect after the device is restarted.

#### Procedure

1. In the user view, run [**startup patch**](cmdqueryname=startup+patch) *file-name* **all**
   
   
   
   The patch file to be loaded at the next startup is specified for all main boards. *file-name* is suffixed with .pat.

#### Follow-up Procedure

To prevent the specified patch file from taking effect at the next startup, run the [**reset patch-configure**](cmdqueryname=reset+patch-configure) ****next-startup**** command to reset the patch file to be used at the next startup.