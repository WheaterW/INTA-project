(Optional) Configuring Automatic Patch Repair
=============================================

You can configure ZTP-based automatic patch repair to resolve a non-environment problem that occurs during automatic ZTP deployment.

#### Context

The automatic patch repair mechanism of ZTP can be used to resolve a non-environment problem (examples of environment problems include a device failing to run stably after startup, or a server failing to start) that occurs during automatic ZTP deployment. Using this mechanism can eliminate the need to perform an on-site repair or return the device to the factory for repair. After the root cause is manually located and a manually generated repair patch is loaded, ZTP automatically identifies the patch, sets it, and then restarts the device for the patch to take effect. ZTP runs again upon the device restart, allowing it to successfully complete deployment given the problem is resolved.


#### Procedure

1. Specify a repair patch in the ZTP intermediate file. For details, see [Automatic Patch Repair Mechanism](dc_ne_ztp_feature_0014.html).
2. Upload both the repair patch and ZTP intermediate file to the file server.
3. Restart the unconfigured device. After ZTP restarts, it identifies the repair patch in the intermediate file and automatically completes the repair.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After setting the repair patch during the repair process, ZTP immediately checks whether itself is enabled. If ZTP is disabled, the next-startup patch is restored to the patch used on the device before ZTP deployment.
   * After the repair is complete, the next-startup system software package, patch, and configuration file are all set by ZTP. If ZTP is disabled in this case, the next-startup patch is restored to the repair patch instead of the patch used on the device before the deployment.