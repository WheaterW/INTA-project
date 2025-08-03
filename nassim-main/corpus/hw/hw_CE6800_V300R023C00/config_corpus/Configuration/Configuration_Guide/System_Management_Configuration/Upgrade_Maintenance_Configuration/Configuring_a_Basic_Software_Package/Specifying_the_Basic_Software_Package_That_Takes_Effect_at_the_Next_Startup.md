Specifying the Basic Software Package That Takes Effect at the Next Startup
===========================================================================

Specifying the Basic Software Package That Takes Effect at the Next Startup

#### Prerequisites

Before specifying the basic software package that takes effect at the next startup, you have completed the following task:

* [Prepare for upgrade maintenance](gx_upgrade_cfg_0005.html).

#### Context

Upgrading the basic software package version of the device can improve device performance, add new features, and eliminate defects existing because software in the current version is not updated in time.

![](public_sys-resources/note_3.0-en-us.png) 

* Ensure that the uploaded files are correct by comparing the file sizes and dates.
* Run the [**dir**](cmdqueryname=dir) *file-name* command to check whether the names of the basic software packages (\*.cc) in the storage media of the are the same as the name of the uploaded basic software package.


#### Procedure

1. Upload a basic software package to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. (Optional) Enable the version rollback function and set a rollback timeout period in an upgrade.
   
   
   ```
   [upgrade rollback rollback-timer](cmdqueryname=upgrade+rollback+rollback-timer) time-value
   ```
   
   If you do not log in to a device within the timeout period after the device is restarted, the system automatically rolls back to the source version.
3. Specify the basic software package that takes effect at the next startup.
   
   
   ```
   [startup system-software](cmdqueryname=startup+system-software) name [ all | slot slot-id ]
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If a feature software package has been installed on a device and the basic software package needs to be upgraded, delete the existing feature software package before you specify the basic software package that takes effect at the next startup. For details, see [Specifying the Feature Software Package That Takes Effect at the Next Startup](gx_upgrade_cfg_0014.html).
   
   If an independent-hardware-release package has been installed on a device and the basic software package that takes effect at the next startup supports the current board, you do not need to pay attention to the version of the independent-hardware-release package. If the basic software package that takes effect at the next startup does not support the current board, install an independent-hardware-release package that matches the new basic software package. For details, see [Specifying the Independent-Hardware-Release Package That Takes Effect at the Next Startup](gx_upgrade_cfg_0020.html).
   
   
   ![](public_sys-resources/notice_3.0-en-us.png) 
   * If the system is started with empty configuration, you must run the [**save**](cmdqueryname=save) command before specifying a next-startup configuration file.
   * To replace the next-startup configuration file with a **device.sys** configuration file containing new hardware configurations, you need to insert the new hardware. When the hardware successfully registers, run the [**save**](cmdqueryname=save) command.
   * In the current version, you are not allowed to upload the hardware configuration file (**device.sys**) of a device to any other devices and then restart the other devices directly. Otherwise, these devices' hardware fails to register.
   * The **device.sys** file is the system hardware configuration file that saves the hardware configuration information reported by a device.
4. (Optional) Specify the patch that takes effect at the next startup.
   
   
   ```
   [startup patch](cmdqueryname=startup+patch) pkgname all
   ```
   
   For an upgraded basic software package that has a patch installed before the upgrade, if it is rolled back to the source version by specifying the basic software package that takes effect at the next startup, run this command to make the patch take effect.
5. Restart the device.
   
   
   ```
   [reboot](cmdqueryname=reboot)
   ```

#### Verifying the Configuration

* Run the [**display startup**](cmdqueryname=display+startup) command to check whether the displayed information is the same as the name of the basic software package to be started.
* Run the [**display paf**](cmdqueryname=display+paf) command to check information about the PAF file.