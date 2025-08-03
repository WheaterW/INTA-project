Configuring a Device as an SFTP Server
======================================

Configuring a Device as an SFTP Server

#### Prerequisites

SFTP runs over the SSH protocol and allows you to use SFTP to set up a secure connection between a user terminal (client) and a device (server), enabling you to manage files on the device while ensuring security of data transmission.

Before configuring a device as an SFTP server to manage files, you have completed the following tasks:

* Ensure that there are reachable routes between the terminal and the device.
* Install the SSH client software on the terminal.

#### Context

![](public_sys-resources/note_3.0-en-us.png) 

* SFTP V2 is more secure than SFTP V1, and is therefore recommended.

[Table 1](#EN-US_TASK_0000001563870605__file07tab01) describes the process for configuring a device as an SFTP server for file management.

**Table 1** Configuring a device as an SFTP server for file management
| No. | Task | Description | Remarks |
| --- | --- | --- | --- |
| 1 | [Enable the SFTP server function and configure related parameters.](#EN-US_TASK_0000001563870605__step165182312514) | Generate a local key pair, enable the SFTP server function, and configure SFTP server parameters, including the port number, key pair update interval, SSH authentication timeout duration, and number of SSH authentication retries. | Tasks 1 and 2 can be performed in any sequence. |
| 2 | [Configure SSH user information.](#EN-US_TASK_0000001563870605__step1242754855110) | Create an SSH user and set the service type, authorized directory for the SFTP service, and authentication mode. |
| 3 | [Connect to the device using SFTP.](#EN-US_TASK_0000001563870605__step59081731155216) | Use the SSH client software on the terminal to connect to the device. |
| 4 | [Perform file operations using SFTP commands.](#EN-US_TASK_0000001563870605__step15439531529) | You can use the SSH client software on the terminal to manage files and directories on the device. |
| 5 | [Disconnect from the SFTP server.](#EN-US_TASK_0000001563870605__step9106121615317) | - |



#### Default Settings

**Table 2** Default settings
| Parameter | Default Setting |
| --- | --- |
| SFTP server function | Disabled |
| Authorized directory of the SFTP service for the SSH user | No SFTP service authorized directory is available for an SSH user. |



#### Procedure

* **Enable the SFTP server function and configure related parameters.**
  
  
  
  For details about how to generate the local server key pair and how to set server parameters including the port number, key pair update interval, SSH authentication timeout interval, and number of SSH authentication retries, see "Configuring the SSH Server Function and Related Parameters" in Configuration Guide > Security Configuration. For details about how to configure the SFTP function, see [Table 3](#EN-US_TASK_0000001563870605__table1188580321175329).
  
  **Table 3** Enabling the SFTP server function and configuring related parameters
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Enable the SFTP server function. | [**sftp**](cmdqueryname=sftp) [ **ipv4** | **ipv6** ] **server enable** | By default, the SFTP server function is disabled. |
  | Configure the default authorized directory of the SFTP server. | [**sftp server default-directory**](cmdqueryname=sftp+server+default-directory) *sftpdir* | By default, the default authorized directory of the SFTP server is not configured.  You can use one of the following methods to configure the default authorized directory of the SFTP server (the methods are introduced by directory priority in descending order):  Run the [**ssh user**](cmdqueryname=ssh+user) *username* **sftp-directory** *directoryname* command to configure the directory for a specified user.  Run the [**local-user**](cmdqueryname=local-user) *user-name* **ftp-directory** *directory* command in the AAA view to configure an FTP directory for a specified user.  Run the [**sftp server default-directory**](cmdqueryname=sftp+server+default-directory) *sftpdir* command to configure the directory, which takes effect for all SSH users. |
  | (Optional) Configure the maximum number of clients that can connect to the SFTP server. | [**sftp max-sessions**](cmdqueryname=sftp+max-sessions) *max-session-count* | By default, a maximum of five clients can connect to the SSH server.  If the maximum number is changed to a value smaller than the number of current online users, these users will stay connected, but new connection requests will be rejected. |
  | (Optional) Configure the idle timeout period for disconnecting an SFTP client from the SFTP server. | [**sftp idle-timeout**](cmdqueryname=sftp+idle-timeout) *minutes* [ *seconds* ] | The default idle timeout period is 10 minutes.  You can run the **[**sftp idle-timeout**](cmdqueryname=sftp+idle-timeout) 0 0** command to disable the function of disconnecting the SFTP client from the SFTP server upon timeout. |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Configure SSH user information.**
  
  
  
  For details, see [Configuring an SSH User](galaxy_ssh_cfg_0011.html) in Configuration Guide > Security Configuration.
  
  
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  When an AAA user is configured, the user privilege level must be set to 3 to ensure successful connection.
* **Connect to the device using SFTP.**
  
  
  
  To connect to the device using SFTP from a terminal, the terminal must be installed with the SSH client software. The following describes how to connect to the device using OpenSSH and the Windows CLI.
  
  + For details about how to install OpenSSH, see the OpenSSH installation guide.
  + To use OpenSSH to connect to the device using SFTP, run the OpenSSH commands. For details about OpenSSH commands, see the OpenSSH help.
  + The Windows CLI can identify OpenSSH commands only when OpenSSH is installed on the terminal.
  
  Access the Windows CLI and run the OpenSSH commands to connect to the device using SFTP.
  
  If the command prompt of the SFTP client view, such as **sftp>**, is displayed, you have entered the working directory of the SFTP server. (The following information is for reference only.)
  
  ```
  C:/Documents and Settings/Administrator> sftp client001@10.136.23.4
  Connecting to 10.136.23.4...
  The authenticity of host "10.136.23.4 (10.136.23.4)" can't be established.
  DSA key fingerprint is 0d:48:82:fd:2f:52:1c:f0:c4:22:70:80:8f:7b:fd:78.
  Are you sure you want to continue connecting (yes/no)? yes
  Warning: Permanently added "10.136.23.4" (DSA) to the list of known hosts.
  client001@10.136.23.4's password:
  sftp>
  ```
* ***Perform file operations using SFTP commands.***
  
  *After logging in to the SSH server from the SFTP client, you can perform the operations listed in [Table 4](#EN-US_TASK_0000001563870605__en-us_task_0141109644_file13-table_03) on the SFTP client. The following operations can be performed in any sequence. You can select one or more operations as required.*
  
  **Table 4** *Performing file operations using SFTP commands*
  | *Operation* | *Command* | *Description* |
  | --- | --- | --- |
  | *Change the current working directory.* | *[**cd**](cmdqueryname=cd) [ *path* ]* | *-* |
  | *Chang the current working directory to its upper-level directory.* | *[**cdup**](cmdqueryname=cdup)* | *-* |
  | Display the current working directory. | [**pwd**](cmdqueryname=pwd) | - |
  | Display the list of files in the specified directory. | [**dir**](cmdqueryname=dir) [ *remote-directory* [ *local-filename* ] ]  or  [**ls**](cmdqueryname=ls) [ *remote-directory* [ *local-filename* ] ] | The [**dir**](cmdqueryname=dir) command has the same effect as the [**ls**](cmdqueryname=ls) command. |
  | Delete a directory from the server. | [**rmdir**](cmdqueryname=rmdir) *directory-name* | A maximum of 10 directories can be deleted at a time.  Before running the [**rmdir**](cmdqueryname=rmdir) command to delete directories, ensure that the directories do not contain any files. Otherwise, the deletion fails. |
  | Create a directory on the server. | [**mkdir**](cmdqueryname=mkdir) *remote-directory* | - |
  | Rename a file on the server. | [**rename**](cmdqueryname=rename) *old-name* *new-name* | - |
  | Download a file from the server. | [**get**](cmdqueryname=get) *remote-filename* [ *local-filename* ] | - |
  | Upload a file to the server. | [**put**](cmdqueryname=put) *local-filename* [ *remote-filename* ] | - |
  | Delete a file from the server. | [**remove**](cmdqueryname=remove) *path*  or  **[**delete**](cmdqueryname=delete)** *path* | A maximum of 10 files can be deleted at a time.  The [**remove**](cmdqueryname=remove) command has the same effect as the [**delete**](cmdqueryname=delete) command. |
  | Display the command help on the SFTP client. | [**help**](cmdqueryname=help) [ *command-name* ] | - |
* **Disconnect from the SFTP server.**
  
  
  
  **Table 5** Disconnecting from the SFTP server
  | Operation | Command | Description |
  | --- | --- | --- |
  | Disconnect from the SFTP server. | [**quit**](cmdqueryname=quit) | You can also run the [**bye**](cmdqueryname=bye) or [**exit**](cmdqueryname=exit) command to disconnect from the SFTP server. |

#### Verifying the Configuration

* Run the [**display ssh user-information**](cmdqueryname=display+ssh+user-information) [ *username* ] command to check SSH user information on the SSH server.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **status** command to check global configuration of the SSH server.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **session** command on the SSH server to check the sessions between the SSH server and the SSH client.