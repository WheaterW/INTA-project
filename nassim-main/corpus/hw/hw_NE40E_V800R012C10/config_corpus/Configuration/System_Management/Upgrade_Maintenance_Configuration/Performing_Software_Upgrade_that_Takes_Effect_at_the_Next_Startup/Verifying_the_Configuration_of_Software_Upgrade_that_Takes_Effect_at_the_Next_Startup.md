Verifying the Configuration of Software Upgrade that Takes Effect at the Next Startup
=====================================================================================

After specifying the system software to be used at the next startup, you can check whether the upgrade is successful.

#### Prerequisites

The configuration of specifying the system software to be used at the next startup is complete.


#### Procedure

* In the user view, run the [**dir**](cmdqueryname=dir) *file-name* command to check whether the file name (\*.cc) of the system software saved on the main control board is the same as that of the uploaded system software.
* Run the [**display startup**](cmdqueryname=display+startup) command to check whether the file name in the "Startup system software" field is the same as that of the specified system software.