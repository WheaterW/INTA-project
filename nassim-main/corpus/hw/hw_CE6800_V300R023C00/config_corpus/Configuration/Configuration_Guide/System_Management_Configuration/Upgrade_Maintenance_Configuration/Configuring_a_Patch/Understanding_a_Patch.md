Understanding a Patch
=====================

While a device is running, you may need to modify the device's system software. For example, you may need to remove system defects or add new functions based on service requirements. The conventional method is to disconnect a device from a network and upgrade system software in offline mode. This method adversely affects services and deteriorates communication service quality.

To address this issue, you can install a patch to system software to implement an in-service system software upgrade, ensuring service continuity.

#### Patch Classification

Based on the impact of patch effectiveness on running services, patches are classified into hot patches and cold patches.

* Hot patch (HP): takes effect without affecting or interrupting services. Using hot patches helps reduce device upgrade costs and prevent upgrade risks.
* Cold patch (CP): takes effect only after a device is restarted, which adversely affects services.

Based on patch dependency, patches are classified into incremental patches and non-incremental patches.

* Incremental patch: is dependent on previous patches. An incremental patch file must contain all patch information that is contained in the previous patch file. You can install an incremental patch file without uninstalling the existing patch file.
* Non-incremental patch: A device can have only one non-incremental patch installed. Before installing another patch on a device that already has a non-incremental patch, uninstall the existing non-incremental patch.

![](public_sys-resources/note_3.0-en-us.png) 

All patches released for products are hot patches and incremental patches. All patches mentioned in the following sections are such patches, unless otherwise specified.




#### Patch Status

Each patch has its own state that can be changed only with user intervention.

[Table 1](#EN-US_CONCEPT_0000001513169222__table188122529213) describes patch states.

**Table 1** Patch status
| State | Description | State Transition |
| --- | --- | --- |
| Idle | A patch file is stored in a storage medium of a device, but patches in the file are not installed into the patch area in the memory. In this situation, the patches in the file are in the idle state. | After the patches in the storage device are installed into the patch area in the memory, the patch state becomes running. |
| Running | After the patches in the storage device are installed into the patch area in the memory, the patch state becomes running.  After a device is reset, the running state remains if the patches were in the running state before the reset. | You can uninstall a running patch file so that the device deletes the patches from the patch area in the memory and sets the patch state to idle. |

[Figure 1](#EN-US_CONCEPT_0000001513169222__fig3679104644414) shows patch state transition.

**Figure 1** Transition between patch states  
![](figure/en-us_image_0000001563889237.png)

#### Patch Installation

For basic software, you can install a patch in either of the following modes:

* In-service patch installation: You can install a patch on an in-service device, without interrupting services. This mode is also called hot patch installation and is usually used.
  
  For details on how to install a patch in this mode, see the corresponding patch installation guide that is released with a patch version.
* Next-startup patch installation: You can specify the patch that takes effect at the next startup. This mode is also called cold patch installation. It is usually used during a device upgrade.

#### Manual Patch Uninstallation

After a patch is installed, if services become abnormal due to the patch, you can uninstall the patch to ensure normal services.


#### Automatic Patch Rollback

If an exception occurs during patch installation, the patch may fail to be installed. In this case, the system automatically rolls back to the previous patch version.


#### Obtaining a Patch Package

1. Visit [Huawei enterprise technical support website](https://support.huawei.com/enterprise/en/index.html) and select the corresponding product in the software download area.
2. Select the desired patch package.
3. Click **Download** next to the ***product*****\_*****version*****.PAT** file of the required version.

![](public_sys-resources/note_3.0-en-us.png) 

The version of a patch package must match that of the system software. Otherwise, the package cannot be successfully loaded.