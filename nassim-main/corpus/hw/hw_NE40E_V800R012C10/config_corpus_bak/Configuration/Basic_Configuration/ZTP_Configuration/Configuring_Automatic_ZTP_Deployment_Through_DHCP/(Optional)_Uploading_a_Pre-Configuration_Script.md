(Optional) Uploading a Pre-Configuration Script
===============================================

(Optional)_Uploading_a_Pre-Configuration_Script

#### Context

If you want commands to be delivered to an unconfigured device before the ZTP process starts, upload a pre-configuration script to the device.


#### Procedure

1. Edit the pre-configuration script based on the file type and format instructions described in [Pre-configuration Script](dc_ne_ztp_feature_0012_01.html#EN-US_CONCEPT_0267196517).
2. Upload the pre-configuration script to the storage medium of the main control board.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   FTP, TFTP, or SFTP can be used to upload the script. For upload details, see [Using FTP to Access Other Devices](../vrp/dc_vrp_basic_cfg_0094.html), [Using TFTP to Access Other Devices](../vrp/dc_vrp_basic_cfg_0088.html), or [Using SFTP to Access Other Devices](../vrp/dc_vrp_basic_cfg_0101.html). Select an upload mode as needed.
3. Run [**set ztp pre-configuration**](cmdqueryname=set+ztp+pre-configuration) *file-name*
   
   
   
   The pre-configuration script is loaded.
   
   
   
   To disable a device from starting the ZTP process at device startup with base configuration, run the [**reset ztp pre-configuration**](cmdqueryname=reset+ztp+pre-configuration) command to clear the pre-configuration script.
4. Run [**display ztp status**](cmdqueryname=display+ztp+status)
   
   
   
   The ZTP status (including the status the pre-configuration script) is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the system software is upgraded from an earlier version to the current version, the loaded pre-configuration script is executed (to prevent this loaded pre-configuration script from being executed, run the reset ztp pre-configuration command) only if the configuration file set for startup is vrpcfg.zip.