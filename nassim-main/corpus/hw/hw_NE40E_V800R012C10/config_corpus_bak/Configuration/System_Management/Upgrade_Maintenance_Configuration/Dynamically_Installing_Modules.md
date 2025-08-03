Dynamically Installing Modules
==============================

This section describes how to load and unload modules without service outages.

#### Usage Scenario

If the in-use module does not exist in the system, the dynamic load function can be used to load desired module file to the system.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration process is supported only on the admin-VS.



#### Pre-configuration Tasks

Before dynamically installing modules, complete the following task:

* Log in to the device.
* Upload the module files to the device.

#### Procedure

1. Run [**check module**](cmdqueryname=check+module) { *file-name* | **startup** }
   
   
   
   Integrity verification is performed on the specified module file.
2. Run the [**install-module**](cmdqueryname=install-module) *file-name* [ **next-startup** ] command to dynamically load the specified module file.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the module is not required any more, use the [**uninstall-module**](cmdqueryname=uninstall-module) command to unload the module file.

#### Checking the Configuration

Run the [**display module-information**](cmdqueryname=display+module-information) [ **verbose** ] command to check information about the dynamically loaded module.