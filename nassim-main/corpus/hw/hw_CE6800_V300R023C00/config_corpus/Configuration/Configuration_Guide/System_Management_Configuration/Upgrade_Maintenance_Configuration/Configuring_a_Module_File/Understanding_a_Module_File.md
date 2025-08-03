Understanding a Module File
===========================

A module file uses the patch mechanism to implement specific functions. It is generated as a \*.MOD file, which is released as an extended package of the basic software package (\*.cc). A module file is a functional patch used to add major functions to the current basic software. You can install a module file for basic software to implement an in-service basic software upgrade, ensuring service continuity.

#### Module File Installation

For basic software, you can install a module file in either of the following modes:

* In-service module file installation: You can install a module file on an in-service device, without interrupting services. This mode is usually used.
* Next-startup module file installation: You can specify the module file that takes effect at the next startup. This mode is usually used during a device upgrade.

#### Manual Module File Uninstallation

After a module file is installed, if services become abnormal due to the module file, you can uninstall the module file to ensure normal services.


#### Automatic Module File Rollback

If an exception occurs during module file installation, the module file may fail to be installed. In this case, the system automatically rolls back to the previous version.


#### Obtaining a Module Package

1. Visit [Huawei enterprise technical support website](https://support.huawei.com/enterprise/en/index.html) and select the corresponding product in the software download area.
2. Select the desired module package.
3. Click **Download** next to the ***product*****\_*****version*****\_XXX.MOD** file of the required version.

![](public_sys-resources/note_3.0-en-us.png) 

The version of a module package must match that of the system software. Otherwise, the package cannot be successfully loaded.