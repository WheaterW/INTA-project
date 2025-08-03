Replacing the Configuration File
================================

Replacing the Configuration File

#### Context

When the configuration file of a device needs to be updated, you can load the configuration file from the local or remote server to the local device to replace the running configuration file.

The configuration replacement function can replace the entire configuration file on the current device or the configurations in a specific view, depending on the content in the configuration file to be loaded. If the configuration file to be loaded contains the configurations of the entire device, all configurations on the current device are replaced. If the configuration file to be loaded contains the configurations saved in a view (the configurations saved in the view automatically carries the <replace/> tag), the configurations in the corresponding view are replaced.

![](public_sys-resources/note_3.0-en-us.png) The specified configuration file to be loaded must exist and meet the following conditions:

* The configuration file can contain only configuration commands, view switching commands, and number signs (#). If other commands including [**quit**](cmdqueryname=quit), [**commit**](cmdqueryname=commit), [**return**](cmdqueryname=return), query commands such as [**display**](cmdqueryname=display), maintenance commands such as [**reset**](cmdqueryname=reset), [**save**](cmdqueryname=save), and [**ping**](cmdqueryname=ping), and upgrade-compatible commands are executed, the device reports an error and continues to load subsequent commands.
* The interactive commands in the configuration file support only Y/N automatic interaction.
* The indentation of commands in the configuration file must be correct. The commands in the system view and the level-1 view under the system view must be left-aligned, the commands in the level-1 view must be indented by one space, and the commands in each subsequent view must be indented by one more space.
  
  If the number sign (#) is left-aligned, the system view is displayed. If the number sign (#) is indented, it is used only to isolate command blocks; in this case, the number sign (#) must be aligned with the first command in the following command block. If the number sign (#) is incorrectly used, configurations may be lost, or commands may be run in an unexpected view.
* The configuration file name extension must be .zip, .cfg, .txt, .dat, or .bat.
  
  + Both .cfg and .txt files are text files whose content can be directly viewed. If a .cfg or .txt file is specified as the configuration file to be loaded, the system restores the commands in the file one by one when the configuration file is loaded.
  + A .zip file is obtained by compressing a .cfg file, occupying less space. If a .zip file is specified as the configuration file to be loaded, the system decompresses the file into a .cfg file, and then restores the commands in the .cfg file one by one when the configuration file is loaded. The .cfg file must have the same name as the .zip file. Otherwise, the configuration file fails to be loaded.
  + A .dat file is a compressed file, which can be in binary or text mode. Only a .dat file exported from a Huawei device is supported, and the file cannot be modified manually. Otherwise, the file fails to be loaded.
  + A .bat file is used for batch processing. It is a text file that can be modified manually.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Run any of the following commands according to the location of the configuration file to be loaded:
   
   
   * Load the configuration file on the local device to replace the current running configurations on the device.
     
     ```
     [load configuration](cmdqueryname=load+configuration+replace) file filename replace [ relative ]
     ```
   * Load the configuration file on a specified remote server to replace the current running configurations on the device.
     
     ```
     [load configuration](cmdqueryname=load+configuration+replace) { server ip-address | server ipv6 ipv6-address } [ vpn-instance vpn-instance-name ] transport-type { ftp | sftp } username user-name password password file filename replace [ relative ]
     ```
   * Load the configuration file on the remote server based on the specified URL to replace the current running configurations on the device.
     
     ```
     [load configuration](cmdqueryname=load+configuration+replace) server http url url-address [ vpn-instance vpn-instance-name ] [ file filename ] replace [ relative ]
     ```

#### Verifying the Configuration

Perform the following operations to verify the configuration:

* Run the [**display configuration candidate**](cmdqueryname=display+configuration+candidate) command to check the uncommitted configurations and check whether the new configurations meet the expectation.
* Run the [**display configuration replace file**](cmdqueryname=display+configuration+replace+file) command to check the differences between the source configuration file and target configuration file.
* Run the [**display configuration replace failed**](cmdqueryname=display+configuration+replace+failed) command to check detailed information about the commands that fail to be replaced and the failure cause.