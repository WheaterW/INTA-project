Loading Configuration Files
===========================

To run commands in a batch for function configuration on a device that is properly running, load a configuration file to the device.

#### Context

To load the configuration file on the remote server or local configuration file to the running configuration database, perform the following steps:

This function is supported only in the two-phase configuration validation mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform one of the following operations based on the location of the configuration file:
   
   
   * Run the [**load configuration**](cmdqueryname=load+configuration) **file** *file-name* **merge** [ **relative** ] command to load the local configuration file and deliver configurations.
   * Run the [**load configuration**](cmdqueryname=load+configuration) **server** *ip-address* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **ftp** | **sftp** } **username** *user-name* **password** *password-value* **file** *file-name* **merge** [ **relative** ] command to load the configuration file on an IPv4 server and deliver configurations to the local device.
   * Run the [**load configuration**](cmdqueryname=load+configuration) **server ipv6** *ipv6-address* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **ftp** | **sftp** } **username** *user-name* **password** *password-value* **file** *file-name* **merge** [ **relative** ] command to load the configuration file on an IPv6 server and deliver configurations to the local device.
   * Run the [**load configuration**](cmdqueryname=load+configuration) **server** **http url** *url-address* [ **vpn-instance** *vpn-instance-name* ] **merge** [ **relative** ] command to load the configuration file on the server at a specified URL and deliver configurations to the local device.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Manually constructing a configuration file is not recommended. If the format of a manually constructed configuration file is incorrect, the configuration restoration may fail or an error may occur during the configuration restoration.
   
   The specified configuration file to be loaded must exist and meet the following conditions:
   * The configuration file can contain only configuration commands, view switching commands, and pound signs (#). If you load other types of commands, such as display commands used for query, reset/save/ping commands used for maintenance, quit, commit, return, upgrade-compatible commands, and one-phase configuration validation commands, the device reports an error and continues to load follow-up commands.
   * The interactive commands in the configuration file support only Y/N automatic interaction.
   * The indentation of commands in the configuration file must be correct. In the configuration file, the commands in the system view and the level-1 view under the system view must be left-aligned, the commands in the level-1 view must be indented by one space, and each subsequent view must be indented by one more space.
   * If the pound sign (#) is left-aligned, the system view is displayed. If the pound sign (#) is indented, it is used only to isolate command blocks; in this case, the pound sign (#) must be aligned with the first command in the following command block. If the pound sign (#) is incorrectly used, configurations may be lost, or commands may be run in an unexpected view.
   * The configuration file name extension must be \*.zip, \*.cfg, \*.txt, \*.dat, or \*.bat, or name of text file without suffix. FTP or SFTP also supports the file names with a server directory. The file name does not support special characters "~" "?" "\*" "/" "\" ":" """ "|" "<" ">" "[" "]".
     
     + Both .cfg and .txt files are text files whose content can be directly viewed. If a .cfg or .txt file is specified as the configuration file to be loaded, the system restores the commands in the file one by one during the replacement process.
     + A .zip file is obtained by compressing a .cfg file, occupying less space. If a .zip file is specified as the configuration file to be loaded, the system decompresses the file into a .cfg file, and then restores the commands in the file one by one. The .cfg file must have the same name as the .zip file. Otherwise, the configuration file fails to be loaded.
     + A .dat file is a compressed file, which can be in binary or text mode. Only a .dat file exported from a Huawei device is supported, and the file cannot be modified manually. Otherwise, the file fails to be loaded.
     + A .bat file is used for batch processing. It is a text file that can be modified manually.
3. After loading the configuration file, run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.