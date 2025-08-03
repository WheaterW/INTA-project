Specifying the Feature Software Package That Takes Effect at the Next Startup
=============================================================================

Specifying the Feature Software Package That Takes Effect at the Next Startup

#### Prerequisites

Before specifying the feature software package that takes effect at the next startup, you have completed the following task:

* [Prepare for upgrade maintenance](gx_upgrade_cfg_0005.html).

#### Context

If an independent feature software package has been installed on a device and the basic software package and independent feature software package need to be upgraded, you can specify the feature software package that takes effect at the next startup. In this scenario, you need to delete the existing feature software package that takes effect at the next startup, specify the basic software package that takes effect at the next startup, and then specify a feature software package that matches this basic software package.

If only a feature software package needs to be upgraded, you are advised to use the in-service upgrade mode.

![](public_sys-resources/note_3.0-en-us.png) 

Ensure that the uploaded files are correct by comparing the file sizes and dates.

An independent feature software package is one that can be displayed in the **Next startup feature software** field of the **display startup** command output.



#### Procedure

1. Upload the desired basic software package and matching feature software package to the storage medium. For details, see "File System Management Configuration" in *Configuration Guide > Basic Configuration*. If the obtained software package is in the \*.zip format, decompress the package and upload it.
2. Delete the existing next-startup feature software package.
   
   
   ```
   [reset feature-software next-startup](cmdqueryname=reset+feature-software+next-startup) {feature-file}&<1-9>
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the **reset feature-software next-startup** command is executed, the feature software package will not be installed upon the next startup. If a feature is not integrated in the next-startup basic software package, the configuration of this feature will be deleted during a startup. To prevent configuration loss, run the [**startup feature-software**](cmdqueryname=startup+feature-software) *name* command before you restart the device. If a feature is integrated into the next-startup basic software package, it is automatically installed.
3. Specify a next-startup basic software package.
   
   
   ```
   [startup system-software](cmdqueryname=startup+system-software) name [ all | slot slot-id ]
   ```
4. Specify a feature software package that matches the next-startup basic software package.
   
   
   ```
   [startup feature-software](cmdqueryname=startup+feature-software) {feature-file}&<1-9>
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If a feature software package is not needed after you specify the next-startup basic software package, you do not need to install the feature software package or run the [**startup feature-software**](cmdqueryname=startup+feature-software) command. Instead, you can run the **reboot** command to restart the device directly.
5. Restart the device.
   
   
   ```
   [reboot](cmdqueryname=reboot)
   ```

#### Verifying the Configuration

Run the [**display startup**](cmdqueryname=display+startup) or [**display startup feature-software**](cmdqueryname=display+startup+feature-software) command to check whether the displayed information is the same as the file name of the independent feature software package to be upgraded.