Configuring In-Service Installation and Uninstallation of an Independent-Hardware-Release Package
=================================================================================================

Configuring In-Service Installation and Uninstallation of an Independent-Hardware-Release Package

#### Prerequisites

Before installing or uninstalling an independent-hardware-release package on an in-service device, you have completed the following tasks:

* [Prepare for upgrade maintenance](gx_upgrade_cfg_0005.html).
* You do not need to insert a board before installing an independent-hardware-release package. If a board is inserted and powered on, you need to power off and then power on the board after installing an independent-hardware-release package. If a board is inserted and powered off, you need to power on the board after installing an independent-hardware-release package.
* Before uninstalling an independent-hardware-release package, ensure that the related boards are powered off. Otherwise, the independent-hardware-release package cannot be uninstalled.

#### Context

If you want to support new hardware without changing the basic software package, you can install an independent-hardware-release package to the original basic software package. In this way, the new hardware is supported by installing the independent-hardware-release package without interrupting services. If the new hardware is no longer required, you can also uninstall the corresponding independent-hardware-release package.


#### Procedure

1. Upload an independent-hardware-release package to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Install the specified independent-hardware-release package.
   
   
   ```
   [install extended-system-software](cmdqueryname=install+extended-system-software) { file-name } &<1-4> 
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   A maximum of four independent-hardware-release packages can be installed at a time. These packages are independent of each other. If one of these packages fails to be installed, the system is automatically restored to the state before the installation attempt. This does not affect the installation of the other packages.
3. Insert and power on the corresponding board.

#### Verifying the Configuration

Run the [**display startup**](cmdqueryname=display+startup) command to check whether the displayed independent-hardware-release package information is the same as the information of the required package.


#### Follow-up Procedure

If the independent-hardware-release package is no longer needed, run the [**uninstall extended-system-software**](cmdqueryname=uninstall+extended-system-software) { *file-name* } **&<1-4>** command to uninstall it.