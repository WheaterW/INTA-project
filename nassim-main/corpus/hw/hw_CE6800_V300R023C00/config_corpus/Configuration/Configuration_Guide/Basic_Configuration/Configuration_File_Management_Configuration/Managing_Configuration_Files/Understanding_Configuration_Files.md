Understanding Configuration Files
=================================

Understanding Configuration Files

#### Configuration File Format

Configuration files use text format and must meet the following requirements:

* A configuration file can contain only configuration commands, view switching commands, # symbols (used to switch to the system view), and the [**quit**](cmdqueryname=quit) command. When the device is loading a configuration file that contains other types of commands, such as **display** commands used for querying, **reset**, **save**, and **ping** commands used for maintenance, the [**return**](cmdqueryname=return) command, and commands for upgrade compatibility, the device reports an error when attempting to load such commands and continues to load other commands supported in the configuration file.
* A configuration file cannot contain repeated commands.
* Each view is displayed with an indentation of one character. Assume that an IP address needs to be configured in the 10GE1/0/1 interface view. The **ip address 10.1.1.5 255.255.255.0** command needs to be indented by one character compared with the **interface 10GE1/0/1** command. The configurations are as follows:
  ```
  #
  interface 10GE1/0/1
   ip address 10.1.1.5 255.255.255.0
  #
  ```
* If commands in a configuration file need to be executed in a view, the configuration file must also contain the command for entering the view.
* The configuration sequence and dependency must be correct.
* Interactive commands in a configuration file support only Y and N choices. Y is the default choice, which is entered automatically during configuration restoration.
* A configuration file must be saved to the root directory of the storage medium, with a file name extension as .zip, .cfg, or .dat.
  + A .cfg file is a text file, whose contents can be viewed directly. If a .cfg file is specified as the configuration file, the system restores the commands in the file one by one during device startup.
  + A .zip file is compressed from a .cfg file and occupies less space. If a .zip file is specified as the configuration file, the system first decompresses the file into a .cfg file, and then restores the commands in the .cfg file one by one during device startup.
  + A .dat file is a binary file. If the startup software version and the .dat file version are the same, the system restores all configurations at a time without the need to restore the commands one by one, accelerating device startup.


#### Configuration File Category

The following table lists the differences between the configurations loaded when the device is running. These configurations fall into the following types: factory configuration, preset configuration, current configuration, and next startup configuration.

| Type | Description | Command |
| --- | --- | --- |
| Factory configuration | Factory configurations are basic configurations provided for a new device. This type of configurations enables a device to start and operate correctly when there is no configuration file, or when the configuration file is lost or damaged. When a device starts with factory configurations, it is considered to start in unconfigured mode.  Factory configurations are different from the default command configurations. The default command configurations cannot be generated in a configuration file. You can run the [**display current-configuration**](cmdqueryname=display+current-configuration) **include-default** command to view the default configurations. For example, factory configurations may contain the **snetconf server enable** command, but the SNETCONF service is disabled by default. In this case, the SNETCONF service is enabled when the device restores factory configurations. | - |
| Preset configuration | When a device starts, it reads the preset default configuration file (\*.defcfg) from the default storage path to initialize the system. The configurations in this configuration file are called preset configurations. If no preset default configuration file exists in the default storage path, the device uses the factory configurations for initialization. | - |
| Current configuration | The configurations that are in effect during device running are current configurations. | Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the current configurations. |
| Next startup configuration | After the device starts, you can specify a configuration file as the initial configurations for the next startup, known as the next startup configurations. | Run the [**display startup**](cmdqueryname=display+startup) command to check the configuration file for the next startup.  Run the [**display saved-configuration**](cmdqueryname=display+saved-configuration) command to check content in the configuration file for the next startup. |


To use modified configurations as the next startup configurations, run the [**save**](cmdqueryname=save) command to save them to the default storage medium.![](public_sys-resources/note_3.0-en-us.png) 

If a command is configured in an incomplete format, the system saves the command to the configuration file in its complete format. As a result, the command may have more than 510 characters, which is the maximum length supported by the system. Such a command cannot be restored after the system restarts.