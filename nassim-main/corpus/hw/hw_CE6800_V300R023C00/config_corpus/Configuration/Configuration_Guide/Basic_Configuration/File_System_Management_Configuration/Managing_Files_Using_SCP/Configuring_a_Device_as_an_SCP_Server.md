Configuring a Device as an SCP Server
=====================================

Configuring a Device as an SCP Server

#### Prerequisites

The Secure Copy Protocol (SCP) runs on top of SSH that allows you to use SCP to set up a connection between a user terminal and a remote device to upload or download files.

Before configuring a device as an SCP server to manage files, you have completed the following tasks:

* Ensure that there are reachable routes between the terminal and the device.
* Ensure that the terminal has SCP-capable SSH client software installed.

#### Context

[Table 1](#EN-US_TASK_0000001512831082__file08tab01) describes the process for configuring a device as an SCP server for file management.

**Table 1** Configuring a device as an SCP server for file management
| No. | Task | Description | Remarks |
| --- | --- | --- | --- |
| 1 | [Enable the SCP server function and configure related parameters.](#EN-US_TASK_0000001512831082__step1806377861175329) | Generate a local key pair, enable the SCP server function, and configure SCP server parameters, including the port number, key pair update interval, SSH authentication timeout duration, and number of SSH authentication retries. | * Before performing task 3, you need to perform tasks 1 and 2. * Tasks 1 and 2 can be performed in any sequence. |
| 2 | [Configure SSH user information.](#EN-US_TASK_0000001512831082__step1495862979175329) | Create an SSH user, configure the authentication mode, and set the service type. |
| 3 | [Perform file operations using SCP.](#EN-US_TASK_0000001512831082__step674417148175329) | Upload files from and download files to the SCP client. |



#### Default Settings

**Table 2** Default settings
| Parameter | Default Setting |
| --- | --- |
| SCP server function | Disabled |



#### Procedure

* **Enable the SCP server function and configure related parameters.**
  
  
  
  For details about how to generate the local server key pair and how to set server parameters including the port number, key pair update interval, SSH authentication timeout interval, and number of SSH authentication retries, see "Configuring the SSH Server Function and Related Parameters" in Configuration Guide > Security Configuration. For details about how to configure the SCP function, see [Table 3](#EN-US_TASK_0000001512831082__table1386493370175329).
  
  **Table 3** Enabling the SCP server function and configuring related parameters
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Enable the SCP server function. | [**scp**](cmdqueryname=scp) [ **ipv4** | **ipv6** ] **server enable** | By default, the SCP server function is disabled. |
  | (Optional) Set the maximum number of SCP clients allowed to connect to an SCP server concurrently. | [**scp max-sessions**](cmdqueryname=scp+max-sessions) *max-session-count* | By default, a maximum of two SCP clients are allowed to connect to an SCP server concurrently. |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Configure SSH user information.**
  
  
  
  For details, see [Configuring an SSH User](galaxy_ssh_cfg_0011.html) in Configuration Guide > Security Configuration.
* **Perform file operations using SCP.**
  
  
  
  The SCP-capable SSH client software must be installed on the terminal, so that the terminal can connect to the device using SCP to upload or download files. The following describes how to connect to the device using OpenSSH and the Windows CLI.
  
  + For details about how to install OpenSSH, see the OpenSSH installation guide.
  + To use OpenSSH to connect to the device using SCP, run the OpenSSH commands. For details about OpenSSH commands, see the OpenSSH help.
  + The Windows CLI can identify OpenSSH commands only when OpenSSH is installed on the terminal.
  
  Access the Windows CLI and run the OpenSSH commands to connect to the device for file operations using SCP. (The following information is for reference only.)
  
  ```
  C:\Documents and Settings\Administrator> scp scpuser@10.136.23.5:flash:/vrpcfg.zip vrpcfg-backup.zip
  The authenticity of host '10.136.23.5 (10.136.23.5)' can't be established.
  DSA key fingerprint is 46:b2:8a:52:88:42:41:d4:af:8f:4a:41:d9:b8:4f:ee.
  Are you sure you want to continue connecting (yes/no)? yes
  Warning: Permanently added '10.136.23.5' (DSA) to the list of known hosts.
  scpuser@10.136.23.5's password:
  vrpcfg.zip                                    100% 1257     1.2KB/s   00:00
  Read from remote host 10.136.23.5: Connection reset by peer
  
  C:\Documents and Settings\Administrator>
  ```
  
  According to the preceding command output, the user terminal uploads files to or downloads files from the SCP server while connecting to the SCP server and accesses the user local directory at last.
* **Disconnect from the SCP server.**
  
  
  
  **Table 4** Disconnecting from the SCP server
  | Operation | Command | Description |
  | --- | --- | --- |
  | Disconnect from the SCP server. | [**quit**](cmdqueryname=quit) | You can also run the [**bye**](cmdqueryname=bye) or [**exit**](cmdqueryname=exit) command to disconnect from the SCP server. |

#### Verifying the Configuration

* Run the [**display ssh user-information**](cmdqueryname=display+ssh+user-information) [ *username* ] command to check SSH user information on the SSH server.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **status** command to check global configuration of the SSH server.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **session** command on the SSH server to check the sessions between the SSH server and the SSH client.