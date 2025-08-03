Clearing the Configuration File
===============================

Clearing the Configuration File

#### Context

Clearing the configuration file is necessary in the following scenarios:

* The software and configuration file do not match after the device software is upgraded.
* The configuration file is damaged, or an incorrect configuration file is loaded.![](public_sys-resources/notice_3.0-en-us.png) 
  
  The [**reset saved-configuration**](cmdqueryname=reset+saved-configuration) command will clear the configuration file used for the next startup. You are advised to run this command under the guidance of technical support personnel.

To configure an interface on a device for other uses, you need to first delete existing configurations from the interface one by one. If the interface has a large number of configurations, this can take a long time. A single command is available for deleting all configurations on an interface, reducing the maintenance workload and simplifying the deletion operation.


#### Procedure

* Delete configurations for the next startup.
  1. Cancel the configuration file specified for the next startup to restore the default configurations.
     
     
     ```
     [reset saved-configuration](cmdqueryname=reset+saved-configuration)
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     After the configuration file specified for the next startup is canceled, the device will use default configurations for startup, unless the [**startup saved-configuration**](cmdqueryname=startup+saved-configuration) command is used to specify a new configuration file, or new configurations have been saved to the configuration file for the next startup.
     
     Before the **reset saved-configuration** command is executed, the system checks whether the configuration files used for the current startup and the next startup are the same:
     
     + If they are the same, running the **reset saved-configuration** command clears both configuration files, and the default configuration file will be used for the next startup.
     + If they are not the same, running the **reset saved-configuration** command clears the configuration file for next startup, but the current configuration file remains unchanged.
     + If the current configuration file is empty and the configuration file for next startup is not empty, running the [**reset saved-configuration**](cmdqueryname=reset+saved-configuration) command clears the configuration file for next startup.
     + If the configuration file for next startup is empty and the current configuration file is not empty, after the [**reset saved-configuration**](cmdqueryname=reset+saved-configuration) command is run, the system reports an error and does not clear any configuration file. If you restart the device after running this command, the IP address of the management interface will become invalid. In this case, you need to log in to the device through the console port and reconfigure the IP address.
  2. Restart the device to validate the configuration.
     
     
     ```
     [reboot fast](cmdqueryname=reboot+fast)
     ```
* Delete all configurations from an interface using one single command to restore the default configurations.
  
  
  ```
  [clear configuration interface](cmdqueryname=clear+configuration+interface) interface-type interface-number
  ```
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  This command will delete all configurations of a specified interface. Exercise caution when running this command.
  
  Ensure that the specified interface type and number are correct. Otherwise, the configurations of another interface may be deleted, causing service interruption.
* Delete the preset configuration file.
  
  
  ```
  [reset default-configuration](cmdqueryname=reset+default-configuration)
  ```
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  Exercise caution when running this command. If this command is required, run it with assistance from technical support personnel.