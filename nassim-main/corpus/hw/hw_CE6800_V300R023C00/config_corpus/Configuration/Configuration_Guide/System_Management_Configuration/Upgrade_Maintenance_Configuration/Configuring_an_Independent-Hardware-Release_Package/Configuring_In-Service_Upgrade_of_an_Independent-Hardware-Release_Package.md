Configuring In-Service Upgrade of an Independent-Hardware-Release Package
=========================================================================

Configuring In-Service Upgrade of an Independent-Hardware-Release Package

#### Prerequisites

Before configuring in-service upgrade of an independent-hardware-release package, you have completed the following task:

* [Prepare for upgrade maintenance](gx_upgrade_cfg_0005.html).

#### Context

If an independent-hardware-release package has been installed on a device and there is a new version released, you can perform an in-service upgrade of the package as needed.


#### Procedure

1. Upload an independent-hardware-release package to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Upgrade the independent-hardware-release package.
   
   
   ```
   [upgrade extended-system-software](cmdqueryname=upgrade+extended-system-software) file-name
   ```

#### Verifying the Configuration

Run the [**display startup**](cmdqueryname=display+startup) command to check whether the displayed independent-hardware-release package information is the same as the information of the upgraded package.


#### Follow-up Procedure

If the board is no longer needed, run the [**uninstall extended-system-software**](cmdqueryname=uninstall+extended-system-software) { *file-name* } &<1-4> command to uninstall the independent-hardware-release package from an in-service device to save storage space. Before uninstalling an independent-hardware-release package, ensure that the related boards are powered off. Otherwise, the independent-hardware-release package cannot be uninstalled.