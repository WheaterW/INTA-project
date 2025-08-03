Verifying the Configuration of In-Service Patch Installation
============================================================

This section describes how to check whether a patch file has been installed onto a device.

#### Procedure

* Run the [**dir**](cmdqueryname=dir) *file-name* command in the user view to check whether the uploaded patch file (\*.PAT) is included in the information displayed on the main control boards.
* Run the [**display patch-information**](cmdqueryname=display+patch-information) command to check whether the installed patch file is in the running state.
* Run the [**display startup**](cmdqueryname=display+startup) command to check whether the next startup patch file is the file that you have configured.