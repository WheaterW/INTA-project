Configuring In-Service Installation and Uninstallation of a Feature Software Package
====================================================================================

Configuring In-Service Installation and Uninstallation of a Feature Software Package

#### Prerequisites

Before configuring in-service installation of a feature software package, you have completed the following task:

* [Prepare for upgrade maintenance](gx_upgrade_cfg_0005.html).

#### Context

To use a feature that is not provided in the basic software package but in a feature software package, you can install the feature software package on an in-service device. In this case, services are not interrupted. If this feature is no longer needed, uninstall the corresponding feature software package.

![](public_sys-resources/note_3.0-en-us.png) 

Ensure that the uploaded files are correct by comparing the file sizes and dates.



#### Procedure

1. Upload a feature software package to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Perform in-service installation of the specified feature software package.
   
   
   ```
   [install feature-software](cmdqueryname=install+feature-software) {feature-file}&<1-9> 
   ```

#### Verifying the Configuration

Run the [**display startup**](cmdqueryname=display+startup) or [**display startup feature-software**](cmdqueryname=display+startup+feature-software) command to check whether the displayed information is the same as the file name of the desired feature software package.


#### Follow-up Procedure

When a feature software package is no longer needed, you can run the [**uninstall feature-software**](cmdqueryname=uninstall+feature-software) *{feature-file}&<1-9>* command to perform in-service uninstallation of the feature software package.

![](public_sys-resources/note_3.0-en-us.png) 

If you run the [**uninstall feature-software**](cmdqueryname=uninstall+feature-software) *{feature-file}&<1-9>* command to uninstall a damaged feature software package, no pre-check is performed. As a result, some dependent services may be unavailable. After the feature software package is reinstalled and then uninstalled, the check is still performed.

When a feature software package is no longer needed, you can run the [**uninstall feature-software**](cmdqueryname=uninstall+feature-software) *{feature-file}* command to perform in-service uninstallation of the feature software package.