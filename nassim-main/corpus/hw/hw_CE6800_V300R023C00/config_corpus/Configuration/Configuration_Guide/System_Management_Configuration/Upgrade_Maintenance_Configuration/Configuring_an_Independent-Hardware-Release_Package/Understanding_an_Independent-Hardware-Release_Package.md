Understanding an Independent-Hardware-Release Package
=====================================================

An independent-hardware-release package, also called a hardware package, provides extended system software developed to implement plug-and-play of new hardware. It allows independent release of hardware. For example, to use a new board on a device running the basic software package of an earlier version, you only need to install the corresponding independent-hardware-release package, as shown in [Figure 1](#EN-US_CONCEPT_0000001563769581__fig10373183219247). In the past, you needed to replace the basic software package to support new hardware. Independent-hardware-release packages make this process more flexible. They decouple new hardware from basic software versions and improve the import efficiency of new hardware.

**Figure 1** Independent-hardware-release package  
![](figure/en-us_image_0000001817731010.png)
The configuration of an independent-hardware-release package includes the following operations:

* In-service installation/uninstallation of an independent-hardware-release package: If a basic software package is running on a device and new hardware needs to be supported to meet service requirements, you can perform in-service installation of an independent-hardware-release package (\*.cch). You can also uninstall an independent-hardware-release package on an in-service device.
* In-service upgrade of an independent-hardware-release package: If a new version is released for an independent-hardware-release package that has been running on a device, you can perform an in-service upgrade as needed.
* Specifying the independent-hardware-release package that takes effect at the next startup: Based on application scenarios, you can specify the independent-hardware-release package that takes effect at the next startup and restart the device to make the package take effect.
* Clearing the independent-hardware-release package that takes effect at the next startup: If the independent-hardware-release package that takes effect at the next startup is no longer needed, you can clear it.

![](public_sys-resources/note_3.0-en-us.png) 

* For details about the new hardware and features supported by installing an independent-hardware-release package in on-board mode, see the hardware description of the corresponding version and product.
* Before the upgrade, the system must have been installed with independent-hardware-release packages that are of the same type but different versions. You cannot upgrade an independent-hardware-release package to the same version.
* Device upgrades are closely related to newly released versions. Each new version comes with a corresponding upgrade guide, which provides instructions for performing an upgrade.
* After independent-hardware-release packages are loaded, you are not allowed to upgrade the system software using the **Update system software with disk format** function provided in the BootLoader main menu. Otherwise, the installed independent-hardware-release packages may be lost.

#### Obtaining an Independent-Hardware-Release Package

1. Visit [Huawei enterprise technical support website](https://support.huawei.com/enterprise/en/index.html) and select the corresponding product in the software download area.
2. Select the desired independent-hardware-release package.
3. Click **Download** next to the **XXX.cch** file (named in the format of product name + version number) of the required version.

![](public_sys-resources/note_3.0-en-us.png) 

The version of an independent-hardware-release package must match that of the system software. Otherwise, the package cannot be successfully loaded.