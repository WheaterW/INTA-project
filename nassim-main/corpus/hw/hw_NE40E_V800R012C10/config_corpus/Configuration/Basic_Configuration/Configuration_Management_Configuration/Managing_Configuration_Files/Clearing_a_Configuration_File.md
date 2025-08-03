Clearing a Configuration File
=============================

You can clear the configuration file that is loaded at the current startup of the system. This section describes how to clear the configuration file that has been loaded to a device and how to delete configurations from an interface at a time.

#### Context

The configuration file needs to be cleared in either of the following situations:

* The system software does not match the configuration file after the Router is upgraded.
* The configuration file is damaged or an incorrect configuration file is loaded.

#### Procedure

* Clear the currently loaded configuration file.
  
  
  
  Run [**reset saved-configuration**](cmdqueryname=reset+saved-configuration)
  
  The configuration file loaded at the current startup is cleared.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Before clearing the configuration file of the Router, the system compares the configuration file loaded at the current startup with that to be loaded at the next startup.
  
  + If the two configuration files are the same, running this command clears both of them. To ensure that a configuration file is available at the next startup, you must specify a configuration file on the Router.
  + If the two configuration files are different, running this command clears only the configuration file loaded at the next startup.
  + If the configuration file loaded at the current startup of the Router is empty and this command is run, the system displays a message, indicating that the configuration file does not exist.
  
  Exercise caution when running this command. If this command is required, run it with assistance from Huawei technical support personnel.
* Delete all configurations from an interface at a time.
  
  
  
  You can delete configurations from an interface at a time using either of the commands listed in [Table 1](#EN-US_TASK_0172359998__tab_1).
  
  **Table 1** Deleting all configurations from an interface at a time
  | View | Command | Description | Precautions |
  | --- | --- | --- | --- |
  | System view | [**clear configuration interface**](cmdqueryname=clear+configuration+interface) *interface-type interface-number* | Deletes all configurations from a specified interface. Note that the command is run in the system view, and you need to remember the type and number of the interface whose configurations are to be deleted. | Exercise caution when running either command. |
  | Interface view | [**clear configuration this**](cmdqueryname=clear+configuration+this) | Deletes all configurations from the current interface at a time. NOTE:  You cannot run this command in the controller interface view. |
* Delete the default configuration file.
  
  
  
  Run [**reset default-configuration**](cmdqueryname=reset+default-configuration)
  
  The default configuration file on the device is deleted.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Exercise caution when running this command. If this command is required, run it with assistance from Huawei technical support personnel.
* Delete the non-activated configuration data of the unregistered chassis and absent boards.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**clear inactive-configuration**](cmdqueryname=clear+inactive-configuration) { **slot** *slot-id* [ **card** *card-number* ] | **all**
     
     
     
     The non-activated configurations are deleted.