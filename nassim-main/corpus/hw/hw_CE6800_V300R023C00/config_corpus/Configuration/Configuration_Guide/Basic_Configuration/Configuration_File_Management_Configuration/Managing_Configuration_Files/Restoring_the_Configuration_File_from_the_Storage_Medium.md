Restoring the Configuration File from the Storage Medium
========================================================

Restoring the Configuration File from the Storage Medium

#### Context

If functions do not operate properly due to incorrect configurations, you can restore the backup configuration file stored in the storage medium to the startup configuration file.


#### Procedure

1. Copy the backup configuration file and specify the name for the configuration file copy.
   
   
   ```
   [copy](cmdqueryname=copy) source-filename destination-filename [ all ]
   ```
2. Specify the configuration file for the next startup.
   
   
   ```
   [startup saved-configuration](cmdqueryname=startup+saved-configuration) configuration-file
   ```
3. Restart the device for the configuration file to take effect.
   
   
   ```
   [reboot fast](cmdqueryname=reboot+fast)
   ```