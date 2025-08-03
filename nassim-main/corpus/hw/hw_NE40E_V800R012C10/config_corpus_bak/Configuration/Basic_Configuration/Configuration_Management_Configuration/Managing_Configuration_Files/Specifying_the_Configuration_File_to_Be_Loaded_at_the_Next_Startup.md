Specifying the Configuration File to Be Loaded at the Next Startup
==================================================================

You can specify a configuration file to be loaded at the next startup of the system.

#### Context

After the system restarts, it uses the specified configuration file to restore configurations.


#### Procedure

* Run [**startup saved-configuration**](cmdqueryname=startup+saved-configuration) *configuration-file*
  
  
  
  A configuration file to be loaded at the next startup is specified.
  
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Manually constructing a configuration file is not recommended. If the format of a manually constructed configuration file is incorrect, the configuration restoration may fail or an error may occur during the configuration restoration.
  
  The configuration file for the next startup must exist and meet the following requirements:
  
  + The extension of the configuration file must be .dat, .zip, or .cfg. In addition, the system startup configuration file must be saved in the root directory of the storage device.
  + The configuration file can contain only configuration commands, view switching commands, and pound signs (#). If you load other types of commands, such as display commands used for query, reset/save/ping commands used for maintenance, quit, commit, return, upgrade-compatible commands, and one-phase configuration validation commands, the device reports an error and continues to load follow-up commands.
  + The interactive commands in the configuration file support only Y/N automatic interaction.
  + The indentation of commands in the configuration file must be correct. In the configuration file, the commands in the system view and the level-1 view under the system view must be left-aligned, the commands in the level-1 view must be indented by one space, and each subsequent view must be indented by one more space.
  + If the pound sign (#) is left-aligned, the system view is displayed. If the pound sign (#) is indented, it is used only to isolate command blocks; in this case, the pound sign (#) must be aligned with the first command in the following command block.
  
  If a large amount of configuration data exists, it takes a long time to load the configuration data during the startup of the device.
* Run the [**startup default-configuration**](cmdqueryname=startup+default-configuration) *configuration-file* command to configure or update the default configuration file of the system.
  
  
  
  If no configuration file is specified for the next startup, the default configuration file will be used during system startup.
  
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + The extension of the configuration file must be .defcfg, and the configuration file must have been stored in the root directory of the device before being specified as the default configuration file.
  + The size of the default configuration file cannot exceed 50 KB.
  + Exercise caution when running this command. If this command is required, run it with assistance from technical support personnel.