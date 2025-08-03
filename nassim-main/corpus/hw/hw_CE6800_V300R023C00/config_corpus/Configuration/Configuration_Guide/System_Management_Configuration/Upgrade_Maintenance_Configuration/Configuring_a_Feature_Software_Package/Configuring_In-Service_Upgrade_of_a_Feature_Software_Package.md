Configuring In-Service Upgrade of a Feature Software Package
============================================================

Configuring In-Service Upgrade of a Feature Software Package

#### Prerequisites

Before configuring in-service upgrade of a feature software package, you have completed the following task:

* [Prepare for upgrade maintenance.](gx_upgrade_cfg_0005.html)

#### Context

To optimize the feature software or remove defects in the existing feature version, you can upgrade the feature software package separately so that the device can provide new functions.

![](public_sys-resources/note_3.0-en-us.png) 

Ensure that the uploaded files are correct by comparing the file sizes and dates.



#### Procedure

1. Upload a feature software package to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Perform in-service upgrade of the feature software package.
   
   
   ```
   [upgrade](cmdqueryname=upgrade) feature-software {feature-file}&<1-9>  
   ```

#### Verifying the Configuration

Run the [**display startup**](cmdqueryname=display+startup) or [**display startup feature-software**](cmdqueryname=display+startup+feature-software) command to check whether the file name displayed in the command output is the same as the file name of the feature software package to be upgraded.