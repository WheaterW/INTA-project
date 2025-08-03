Saving a Configuration File
===========================

Saving a Configuration File

#### Context

You can run commands to modify current device configurations, but these modified configurations will be lost once the device restarts unless you save them to the configuration file before restarting the device. Two methods are available for saving configurations to a configuration file:

* Automatically saving configurations: With the auto-save function enabled, a device automatically saves configurations to the next-startup configuration file on condition that the current configurations are different from those in the next-startup configuration file and the time specified using the **interval** parameter arrives, regardless of whether the **save** command is run.
* Manually saving configurations: The configurations are saved only after the **save** command is run. After the command is delivered, the current configurations are saved to the configuration file regardless of whether the current configurations are changed.

Device configurations are stored in the configuration file of the storage medium. During startup, the system reads the configuration file to restore configurations of the device, and then saves the restored configurations to memory.

You can use the [**display saved-configuration**](cmdqueryname=display+saved-configuration) command to check configurations in the configuration file, and the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check those in memory.

When the device is running properly, the configurations in the configuration file should be the same as those in memory. If you add, modify, or delete configurations, the latest configurations are saved in memory, and will be different from those in the configuration file. In this case, you can run the [**save**](cmdqueryname=save) command to save the current configurations in memory to the configuration file.

When the device has not run properly during system startup, the configurations in the configuration file are not completely restored in memory. If you run the [**save**](cmdqueryname=save) command at this time, incomplete configurations in memory will override those in the configuration file. As a result, some configurations may be lost.


#### Procedure

* Enable the system to automatically save configurations.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the system to save the configurations at a scheduled time.
     
     
     ```
     [configuration file auto-save](cmdqueryname=configuration+file+auto-save) [ interval interval | delay delay-interval | cpu-limit cpu-usage ] *
     ```
     
     By default, scheduled saving of configurations is disabled.
     
     The system does not automatically save the configurations in the following scenarios when the scheduled time arrives:
     + The system is writing the configuration file.
     + The system is restoring device configurations.
     + CPU usage is high.
  3. (Optional) Enable configuration saving interruption upon configuration committing and trigger the system to automatically save configurations.
     
     
     ```
     [configuration save-policy interrupt-allowed](cmdqueryname=configuration+save-policy+interrupt-allowed)
     ```
     
     By default, configuration committing will interrupt configuration saving, and the system is disabled from automatically saving configurations.
     
     After this function is enabled, if a user delivers configurations during configuration saving, configuration saving will be interrupted and fail, and configuration delivery will succeed. The system automatically saves the configurations five minutes later.
     
     After this function is disabled, if a user delivers configurations during configuration saving, configuration saving will not be affected, and configuration delivery will fail.
  4. (Optional) Configure server information, including the IP address of the server where the configuration file is automatically saved, user name and password, storage path, and mode for transmitting the configuration file to the server.
     
     
     ```
     [configuration file auto-save backup-to-server](cmdqueryname=configuration+file+auto-save+backup-to-server) [server](cmdqueryname=server) [ ipv6 ] server-ip [ vpn-instance vpn-instance-name ] transport-type { { ftp | sftp } [ port port-value ] user user-name password password | tftp } [ path folder ]
     ```
     
     By default, the system does not periodically save configurations to a server.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If the local storage medium does not have sufficient space or is damaged, or the configuration file needs to be backed up, you can run this command to specify a file server for saving the backup configuration file.
     
     SFTP has higher security and is therefore recommended for saving the configuration file to the file server.
     
     The configuration file is saved on the server as a compressed package, named in the *YY-MM-DD.HH-MM-SS*.*Device name*.zip format (for example, **2019-10-25.15-13-37.HUAWEI.zip**). After decompression, the file with the file name extension .cfg is the configuration file.
  5. (Optional) Configure the function for uploading the configuration file at a specific time point of a certain day every month.
     
     
     ```
     [configuration current backup-to-server monthly](cmdqueryname=configuration+current+backup-to-server+monthly) date date-value [ time time-value ]
     ```
     
     By default, the function of uploading a configuration file to the server on a specific date and time every month is disabled.
  6. (Optional) Set the local backup start time and interval.
     
     
     ```
     [configuration current backup-to-file](cmdqueryname=configuration+current+backup-to-file) [ interval interval-time | from time ] *
     ```
     
     
     
     By default, the function of periodically backing up the configuration file is disabled.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Manually save the configurations.
  1. (Optional) Enable configuration saving interruption upon configuration committing and trigger the system to automatically save configurations.
     
     
     ```
     [configuration save-policy interrupt-allowed](cmdqueryname=configuration+save-policy+interrupt-allowed)
     ```
     
     By default, configuration committing will interrupt configuration saving, and the system is disabled from automatically saving configurations.
     
     After this function is enabled, if a user delivers configurations during configuration saving, configuration saving will be interrupted and fail, and configuration delivery will succeed. The system automatically saves the configurations five minutes later.
     
     After this function is disabled, if a user delivers configurations during configuration saving, configuration saving will not be affected, and configuration delivery will fail.
  2. Save the configurations.
     
     
     + Directly save the configuration file.
       ```
       [save](cmdqueryname=save) [ configuration-file ]
       ```
       
       The configuration file name extension must be .zip, .dat, or .cfg. If the configuration file will be loaded during system startup, it must be stored in the root directory of the storage medium.
       
       If the *configuration-file* parameter is not specified, the system asks you whether to name the configuration file **vrpcfg.zip** when you save the configuration file for the first time. The **vrpcfg.zip** file is the default configuration file and does not contain any configuration in the initial state. If configurations are not saved for the first time, they will be saved in the running configuration file. You can run the [**display startup**](cmdqueryname=display+startup) command to check the name of the running configuration file.
     + Enter a password to save the configuration file.
       ```
       [save](cmdqueryname=save) shareable-configuration configuration-file [ password ]
       ```
       
       The device generates a key in the configuration file based on the password entered by the user. When the configuration file is used next time, the password must be entered for authentication.
       
       ![](public_sys-resources/note_3.0-en-us.png) 
       
       After the weak password dictionary maintenance function is enabled, the passwords (which can be queried using the **display security weak-password-dictionary** command) defined in the weak password dictionary cannot be specified in this command.

#### Example

If the device is unexpectedly damaged, the configuration file cannot be restored. To prevent this problem, you can configure the device to periodically save the configuration file to the SFTP server for backup.

1. Configure a routing protocol to ensure that there are reachable routes between the device and SFTP server.
2. Configure the SFTP server function and related parameters, create an SSH user named **huawei**, set the authentication mode to password authentication, and set the password to YsHsjx\_202206. For details, see "File System Management Configuration" in Configuration Guide > Basic Configuration.
3. Set the interval at which the configuration file is saved to 60 minutes.
   ```
   <HUAWEI> system-view
   [~HUAWEI] configuration file auto-save interval 60
   ```
4. Configure the configuration file to be transferred to the SFTP server.
   ```
   [*HUAWEI] configuration file auto-save backup-to-server server 10.2.1.2 transport-type sftp user huawei password YsHsjx_202206
   ```
5. After 60 minutes, view the configuration file named after the date and time in the root directory on the SFTP server.