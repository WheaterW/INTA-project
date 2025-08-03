Specifying the Configuration File for Next Startup
==================================================

Specifying the Configuration File for Next Startup

#### Context

When the system restarts, it uses the specified configuration file to restore configurations.

Before specifying the file for the next startup, you can run the [**display startup**](cmdqueryname=display+startup) command to view the current specified file.

If no configuration file is specified, the default configuration file **default.cfg** will be used for the next startup.

![](public_sys-resources/note_3.0-en-us.png) 

* Manually constructing a configuration file is not recommended because manual construction is prone to file format errors. The format error may cause a failure to restore configurations or an error during configuration restoration.
* The configuration file for the next startup must exist and be saved in the root directory of the storage medium.
* After specifying the file for the next startup, you cannot run the [**save**](cmdqueryname=save) command without any parameter in the user view. If you run this command, the system uses the saved configuration file instead of the specified configuration file for the next startup.
* You can perform one of the following operations to set the configuration file according to the actual situation.
* If whether the configuration file contains local user configurations (such as the local login user name and password) does not need to be checked, run the **configuration check local-user disable** command to disable local user configuration check.


#### Procedure

* Configure the configuration file for the next startup.
  
  
  ```
  [startup](cmdqueryname=startup) saved-configuration configuration-file
  ```
* Configure the configuration file containing key information for the next startup.
  
  
  ```
  [startup](cmdqueryname=startup) shareable-configuration configuration-file [ password ]
  ```
  
  If the configuration file configured for the next startup contains key information, you need to enter a password for authentication before using the file.
* Configure the preset configuration file.
  
  
  ```
  [startup default-configuration](cmdqueryname=startup+default-configuration) configuration-file
  ```
  
  If no configuration file is specified for the next startup, the preset configuration file will be used during system startup. The extension of the preset configuration file must be .defcfg, and the preset configuration file must have been stored in the root directory of the device in advance.

#### Verifying the Configuration

Run the [**display configuration recover-result**](cmdqueryname=display+configuration+recover-result) command to check the configuration restoration result after the restart and the failure cause.