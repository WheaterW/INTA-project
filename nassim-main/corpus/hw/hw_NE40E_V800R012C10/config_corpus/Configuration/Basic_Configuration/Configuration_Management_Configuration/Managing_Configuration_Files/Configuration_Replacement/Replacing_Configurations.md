Replacing Configurations
========================

This section describes how to replace the configurations on multiple devices that share the same source to achieve configuration consistency between the devices.

#### Usage Scenario

In a scenario where a management server manages a device, the server stores the configurations required by the device. If the configurations on the management server change, the configurations on the device also need to be changed accordingly. In this case, you can load the configuration file on the management server and use this file to replace the configurations on the device, achieving configuration consistency between the management server and the device.

If one of the devices with the same configurations encounters a configuration change, the configurations of other devices must be changed accordingly to keep configuration consistency. In this case, you can load the configurations on the device with the configuration change to replace the configurations on the other devices. This ensures that the configurations on all the devices are the same.

The configuration replacement function can replace the entire configuration file on the current device or the configuration in a specific view, depending on the content in the source configuration file to be loaded. If the source configuration file contains the configurations of an entire device, this function replaces all configurations on the current device. If the source configuration file contains the configurations only in a specific view (the configurations saved in a view automatically carry the <replace/> tag), this function replaces the configurations in the corresponding view.

This function is supported only in the two-phase configuration validation mode.


#### Procedure

1. Save configurations in a configuration file.
   * To load the configuration file of a local device to replace the current running configurations, perform the following steps on the local device:
     
     + Run the [**save**](cmdqueryname=save) [ *configuration-file* ] command in the user view to save the configuration file of the entire device.
     + Run the [**save**](cmdqueryname=save) *configuration-file* command in the service view to save the configuration file in the corresponding view. Then, return to the user view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If a local configuration file is loaded to replace the current device configuration, the local configuration file must be stored in the root directory of the device. The [**save**](cmdqueryname=save) command saves a configuration file to the root directory by default.
   * To load the configuration file of a remote device to replace the current running configurations, perform the following steps on the remote device:
     + Run the [**save**](cmdqueryname=save) [ *configuration-file* ] command in the user view to save the configuration file of the entire device.
     + Run the [**save**](cmdqueryname=save) *configuration-file* command in the service view to save the configuration file in the corresponding view. Then, return to the user view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you run the command in a non-user view, the *configuration-file* parameter must be specified and the file name extension must be .zip or .cfg.
2. Load the configuration file to replace the current running configurations.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run any of the following commands according to the location of the source configuration file to be loaded:
      
      
      * Run the [**load configuration**](cmdqueryname=load+configuration) **file** *filename* **replace** [ **relative** ] command to load a local configuration file and use it to replace the configuration file in use.
      * Run the [**load configuration**](cmdqueryname=load+configuration) { **server** *ip-address* | **server ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **ftp** | **sftp** } **username** *user-name* **password** *password* **file** *filename* **replace** [ **relative** ] command to load the configuration file of a specified remote server and use it to replace the configuration file in use on the local device.
      * Run the [**load configuration**](cmdqueryname=load+configuration) **server http url** *url-address* [ **vpn-instance** *vpn-instance-name* ] [ **file** *filename* ] **replace** [ **relative** ] [ **file** *filename* ] **replace** [ **relative** ] command to load a configuration file on the remote server with a specified URL and use it to replace the configuration file in use on the local device.![](../../../../public_sys-resources/note_3.0-en-us.png) The specified configuration file to be loaded must exist and meet the following conditions:
      * The configuration file can contain only configuration commands, view switching commands, and pound signs (#). If you load other types of commands, such as display commands used for query, reset/save/ping commands used for maintenance, quit, commit, return, upgrade-compatible commands, and one-phase configuration validation commands, the device reports an error and continues to load follow-up commands.
      * The interactive commands in the configuration file support only Y/N automatic interaction.
      * The indentation of commands in the configuration file must be correct. In the configuration file, the commands in the system view and the level-1 view under the system view must be left-aligned, the commands in the level-1 view must be indented by one space, and each subsequent view must be indented by one more space.
      * If the pound sign (#) is left-aligned, the system view is displayed. If the pound sign (#) is indented, it is used only to isolate command blocks; in this case, the pound sign (#) must be aligned with the first command in the following command block. If the pound sign (#) is incorrectly used, configurations may be lost, or commands may be run in an unexpected view.
      * The configuration file name extension must be .zip, .cfg, .txt, .dat, or .bat, or the file name does not have an extension. In FTP or SFTP mode, a file name can contain a server directory. A file name does not contain the following special characters: ~, ?, \*, /, \, :, ", |, <, >, [, and ].
        
        + Both .cfg and .txt files are text files whose content can be directly viewed. If a .cfg or .txt file is specified as the configuration file to be loaded, the system restores the commands in the file one by one during the replacement process.
        + A .zip file is obtained by compressing a .cfg file, occupying less space. If a .zip file is specified as the configuration file to be loaded, the system decompresses the file into a .cfg file, and then restores the commands in the file one by one. The .cfg file must have the same name as the .zip file. Otherwise, the configuration file fails to be loaded.
        + A .dat file is a compressed file, which can be in binary or text mode. Only a .dat file exported from a Huawei device is supported, and the file cannot be modified manually. Otherwise, the file fails to be loaded.
        + A .bat file is used for batch processing. It is a text file that can be modified manually.
   3. (Optional) Run [**display configuration candidate**](cmdqueryname=display+configuration+candidate)
      
      
      
      Check whether the post-replacement configurations meet the expectation.
      
      
      
      * If the configurations meet the expectation, go to Step d.
      * If the configurations do not meet the expectation, run the [**clear configuration candidate**](cmdqueryname=clear+configuration+candidate) command to clear the configurations and perform Step b to load a correct configuration file.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

* Run the [**display configuration replace failed**](cmdqueryname=display+configuration+replace+failed) command to check information about configuration replacement failures.
* Run the [**display configuration replace file**](cmdqueryname=display+configuration+replace+file) command to check the differences between the new configuration and the target configuration.