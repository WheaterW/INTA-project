Preparing Deployment Files
==========================

Preparing Deployment Files

#### Context

Before DHCP-based ZTP, you need to prepare deployment files, including the configuration file and intermediate file.

The configuration file name is a string of 5 to 64 characters and suffixed with \*.zip or \*.cfg. The configuration file is used for the next startup. The configuration file can be manually edited or copied from other devices. You can use either of the following methods to obtain the configuration file:

* Saving the configuration file: Run the **save shareable-configuration** command on the device that provides the configuration file to save the configuration file, and then export the configuration file using SFTP or other methods.
* Changing the system master key: Run the **set [**master-key**](cmdqueryname=master-key)** command to change the system master key, save the configuration file, and export the configuration file using SFTP or other methods.![](public_sys-resources/note_3.0-en-us.png) 
  
  To ensure security, you are advised to perform the following operations to export the configuration file and not advised to manually edit the configuration file.
  
  Ensure that the configuration file for deployment contains the console password or an AAA user name that can be used to log in to the device remotely. Otherwise, the configuration file cannot be successfully set, causing a deployment failure.

The name extension of the intermediate file is .ini or .python. By parsing the intermediate file, the device to be deployed obtains information about the deployment file server address and deployment files. The intermediate file needs to be manually edited.

* The intermediate file in .ini format is used to save information about the device and its deployment files. [Intermediate File in the INI Format](galaxy_ztp_cfg_0031.html) provides a file example.
* The intermediate file in Python format (known as a Python script) is used to download deployment files. For details about the file example, see [Intermediate File in the Python Format](galaxy_ztp_cfg_0132.html).

#### Procedure

1. Prepare the configuration file.
   * Configuration file saving mode
   1. Save the configuration file on the device that provides the configuration file.
      
      
      ```
      [save shareable-configuration](cmdqueryname=save+shareable-configuration) configuration-file [ password ]
      ```
      
      If the **password** parameter is not specified, the configuration file uses the default key information. If the **password** parameter is specified, the device generates key information in the configuration file based on the password entered in interactive mode.
   2. Export the configuration file using SFTP.
   * System master key changing mode
   1. Change the system master key.
      
      
      ```
      <HUAWEI> set [master-key](cmdqueryname=master-key)
      Enter the user password:  //Password of the current user, not the master key of the current system
      Warning: This operation will automatically save configurations. Are you sure you want to perform it? [Y/N]:y
      Do you want to enter the master key? (If you enter Y, you need to manually enter the master key and automatic key update stops. If you enter N, the system  automatically generates a master key. If you enter D, the system will change the current master key to the default master key.) [Y/N/D]:y
      Enter a new master key:    //System master key
      Confirm the new master key:
      Info: Keep the new master key well.
      Info: Operating, please wait for a moment......
      Info: Operation success.
      ```
      
      For details, see "System Master Key Configuration" in Configuration Guide > User Access and Authentication Configuration.
   2. Export the configuration file using SFTP.
2. Prepare the intermediate file.
   
   
   
   The intermediate file can be an .ini file or a Python script. You can select either format to configure related fields. In addition, the configuration of some fields in the intermediate file is related to the method of obtaining the configuration file. For details, see [Table 1](#EN-US_TASK_0000001513154394__table73271326246) and [Table 2](#EN-US_TASK_0000001513154394__table683917423194). For more information about the fields in an intermediate file, see [Intermediate File in the INI Format](galaxy_ztp_cfg_0031.html) and [Intermediate File in the Python Format](galaxy_ztp_cfg_0132.html).
   
   **Table 1** Fields in an intermediate file in .ini format
   | Field | Mandatory or Not | Description | Value Range |
   | --- | --- | --- | --- |
   | [BEGIN] | Yes | Start field of the intermediate file. | - |
   | EXPORTCFG | * This field is mandatory when the configuration file saving mode is used. * The field is optional when the system master key changing mode is used. | Password used for saving the configuration file. | * If the **password** parameter is not specified when the **save shareable-configuration** command is executed to save the configuration file, leave the **EXPORTCFG** field empty. * If the **password** parameter is specified when the **save shareable-configuration** command is executed to save the configuration file, set the **EXPORTCFG** field to a value that is the same as that of **password**. |
   | SET\_MASTER | * This field is optional when the configuration file saving mode is used. * The field is mandatory when the system master key changing mode is used. | System master key. | The value must be the same as the system master key of the device that provides the configuration file. |
   | CLEAR\_MASTER | * This field is optional when the configuration file saving mode is used. * The field is mandatory when the system master key changing mode is used. | Whether to clear the system master key. | * The value **1** indicates that the device restores the random master key after the device deployment is complete. * The value **0** indicates that the device still uses the value of **SET\_MASTER** as the master key after the device deployment is complete. |
   | [END] | Yes | End field of the intermediate file. | - |
   
   
   **Table 2** Fields in an intermediate file in Python format
   | Field | Mandatory or Not | Description | Value Range |
   | --- | --- | --- | --- |
   | master\_exportcfg | * This field is mandatory when the configuration file saving mode is used. * The field is optional when the system master key changing mode is used. | Password used for saving the configuration file. | * If the **password** parameter is not specified when the **save shareable-configuration** command is executed to save the configuration file, set the **master\_exportcfg** field to **None**. * If the **password** parameter is specified when the **save shareable-configuration** command is executed to save the configuration file, set the **master\_exportcfg** field to a value that is the same as that of **password**. |
   | is\_set\_master | * This field is optional when the configuration file saving mode is used. * The field is mandatory when the system master key changing mode is used. | System master key. | The value must be the same as the system master key of the device that provides the configuration file. |
   | is\_clear\_master | * This field is optional when the configuration file saving mode is used. * The field is mandatory when the system master key changing mode is used. | Whether to clear the system master key. | * The value **1** indicates that the device restores the random master key after the device deployment is complete. * The value **0** indicates that the device still uses the value of **SET\_MASTER** as the master key after the device deployment is complete. |