Configuring a Device as an FTP Client
=====================================

Configuring a Device as an FTP Client

#### Prerequisites

You can configure a device as an FTP client, through which you can log in to a remote FTP server to transfer files between the server and client and manage files and directories on the server.

Before configuring a device to access files on another device as an FTP client, you have completed the following tasks:

* Ensure that there are reachable routes between the device and FTP server.
* Obtain the IP address, user name, and password of the FTP server.
* Obtain the port number configured for the server if the standard port number is not used.
* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

SFTP V2 or SCP is more secure than FTP, and is therefore recommended.

In FIPS mode, FTP cannot be used.

[Table 1](#EN-US_TASK_0000001512831074__file12tab01) describes the process for configuring a device to access files on another device as an FTP client.

**Table 1** Configuring a device to access files on another device as an FTP client
| No. | Task | Description |
| --- | --- | --- |
| 1 | [(Optional) Configure the source interface or source IP address for the FTP client.](#EN-US_TASK_0000001512831074__step2117332249175329) | Configure the source interface or source IP address for the FTP client to implement security verification. |
| 2 | [(One-click mode) Log in to another device through FTP to perform file operations.](#EN-US_TASK_0000001512831074__step98861026195718) | Select only one of the tasks.   * One-click mode: You can upload and download files while the connection is set up. * Interactive mode: After a connection is set up, you can perform operations on directories and files, configure the file transfer mode, and view the online help of FTP commands on the FTP server. |
| [(Interactive mode) Log in to another device through FTP to perform file operations.](#EN-US_TASK_0000001512831074__step1693599655175329) |
| 3 | [(Optional) Change the login user.](#EN-US_TASK_0000001512831074__file1204_ftp) | - |
| 4 | [Disconnect from the FTP server.](#EN-US_TASK_0000001512831074__file1205_ftp) | - |



#### Procedure

* **(Optional) Configure the source interface or source IP address for the FTP client.**
  
  
  
  The source IP address to be configured must be that of a stable interface, such as a loopback interface. This configuration makes it easier to configure ACL rules. You simply need to specify the source or destination IP address in an ACL rule as the interface IP address, thereby allowing the device to filter incoming and outgoing packets.
  
  **Table 2** Configuring the source interface or source IP address for the FTP client
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Configure the source IPv4 address or source interface for the FTP client. | [**ftp client source**](cmdqueryname=ftp+client+source) { **-a** *ip-address* | **-i** *interface-type* *interface-number* } | The IP address of a loopback interface is recommended.  When the source address is set to a loopback interface, an IP address must be configured for the loopback interface in advance. Otherwise, the FTP connection fails to be set up. |
  | Configure the source IPv6 address for the FTP client. | [**ftp ipv6 client-source**](cmdqueryname=ftp+ipv6+client-source) **-a** *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] | If the specified source address does not exist, the configuration can be successful, but the function does not take effect. |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **(One-click mode) Log in to another device through FTP to perform file operations.**
  
  
  
  To only upload files to the FTP server or download files to the device, you can run commands in the user view to complete file transfer (These commands cannot be used to perform other FTP operations).
  
  **Table 3** One-click file operations using commands
  | Operation | Command | Description |
  | --- | --- | --- |
  | Connect to the FTP server using an IPv4 address. | [**ftp**](cmdqueryname=ftp) { **put** | **get** } [ **-a** *source-ip4* | **-i** { *interface-type interface-number* | interface-name } ] **host-ip** *ip4-address* [ **port** *portnumber* ] [ **vpn-instance** *ipv4-vpn-name* | **public-net** ] **username** *user-name* **sourcefile** *localfilename* [ **destination** *remotefilename* ] | Connect to the FTP server in IPv4 mode and download files from the server to the FTP client or upload files from the FTP client to the server. |
  | Connect to the FTP server using an IPv6 address. | [**ftp**](cmdqueryname=ftp){ **put** | **get** } **ipv6** [ **-a** *source-ip6* ] **host-ip** *ipv6-address* [ [ **vpn-instance** *ipv6-vpn-name* ] | **public** ] [ **port** *port-number* ] **username** *username* **sourcefile** *local-filename* [ **destination** *remote-filename* ] | Connect to the FTP server in IPv6 mode and download files from the server to the FTP client or upload files from the FTP client to the server. |
* **(Interactive mode) Log in to another device through FTP to perform file operations.**
  1. **Connect to another device using FTP commands.**
     
     
     
     In the user view or FTP client view, you can run a command to log in to the FTP server.
     
     Perform operations in either of the following tables based on the server's IP address type.
     
     **Table 4** Logging in to another device that functions as the FTP server configured with an IPv4 address
     | Operation | Command | Description |
     | --- | --- | --- |
     | Establish a connection with the IPv4 FTP server in the user view. | [**ftp**](cmdqueryname=ftp) [ **-a** *source-ip-address* | **-i** { *interface-type interface-number* | *interface-name* } ] *host-ip* [ *port-number* ] [ **vpn-instance** *vpn-instance-name* | **public-net** ] | Use either method  Before setting up a connection with the FTP server in the FTP client view, run the [**ftp**](cmdqueryname=ftp) command to enter the FTP client view. |
     | Establish a connection with the IPv4 FTP server in the FTP client view. | [**ftp**](cmdqueryname=ftp) |
     | [**open**](cmdqueryname=open) [ **-a** *source-ip* | **-i** { *interface-type interface-number* | *interface-name* } ] *host-ip-address* [ *port-number* ] [ **vpn-instance** *vpn-instance-name* | **public-net** ] |
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Before logging in to the FTP server, run the [**set net-manager vpn-instance**](cmdqueryname=set+net-manager+vpn-instance) command to set the default VPN instance. Then the default VPN instance will be used in the FTP operation.
     
     The source IP address specified in the [**ftp**](cmdqueryname=ftp) command takes precedence over the source IP address specified in the [**ftp client source**](cmdqueryname=ftp+client+source) command. If the source IP addresses specified in the [**ftp client source**](cmdqueryname=ftp+client+source) and [**ftp**](cmdqueryname=ftp) commands are different, the source IP address specified in the [**ftp**](cmdqueryname=ftp) command takes effect. The source IP address specified in the [**ftp client source**](cmdqueryname=ftp+client+source) command applies to all FTP connections, whereas the source IP address specified in the [**ftp**](cmdqueryname=ftp) command applies only to the current FTP connection.
     
     
     **Table 5** Logging in to another device that functions as the FTP server configured with an IPv6 address
     | Operation | Command | Description |
     | --- | --- | --- |
     | Establish a connection with the IPv6 FTP server in the user view. | [**ftp**](cmdqueryname=ftp) **ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ [ **vpn-instance** *ipv6-vpn-instance-name* ] | **public-net** ] [**-oi** { *interface-type interface-number* | *interface-name* } ] [ *port-number* ] | Use either method  Before setting up a connection with the FTP server in the FTP client view, run the [**ftp**](cmdqueryname=ftp) command to enter the FTP client view. |
     | Establish a connection with the IPv6 FTP server in the FTP client view. | [**ftp**](cmdqueryname=ftp) |
     | [**open**](cmdqueryname=open) **ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ **-oi** { *interface-type interface-number* | *interface-name* } ] [ *port-number* ] [ **vpn-instance** *vpn-instance* | **public-net** ] |
     
     You must enter a correct user name and password for authentication before you are allowed access to the FTP server.
  2. **Perform file operations using FTP.**
     
     
     
     After logging in to the FTP server, you can run FTP commands to perform operations on files, including managing directories, managing files, configuring the file transfer mode, and viewing online help of FTP commands.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The operation rights of a user are set on the FTP server.
     
     You can perform one or more operations listed in the following table, and in any sequence.
     
     **Table 6** Performing file operations using FTP
     | Operation | Command | Description |
     | --- | --- | --- |
     | Change the working directory of the FTP server. | [**cd**](cmdqueryname=cd) *pathname* | - |
     | Change the working directory of the FTP server to its upper-level directory. | [**cdup**](cmdqueryname=cdup) | - |
     | Display the working directory of the FTP server. | [**pwd**](cmdqueryname=pwd) | - |
     | Display or change the working directory of the FTP client. | [**lcd**](cmdqueryname=lcd) [ *directory* ] | The **lcd** command displays the local working directory of the FTP client, whereas the **pwd** command displays the working directory of the FTP server. |
     | Create a directory on the server. | [**mkdir**](cmdqueryname=mkdir) *remote-directory* | The name of a directory can contain letters and digits, but cannot contain the following special characters: < > ? \ : |
     | Delete a directory from the FTP server. | [**rmdir**](cmdqueryname=rmdir) *remote-directory* | - |
     | Display the specified directory or file on the FTP server. | [**dir**](cmdqueryname=dir) [ *remote-directory* [ *local-filename* ] ]  or  [**ls**](cmdqueryname=ls) [ *remote-directory* [ *local-filename* ] ] | + The [**ls**](cmdqueryname=ls) command displays only the name of a directory or file, but the [**dir**](cmdqueryname=dir) command displays details about a directory or file, such as the size and creation date. + If no path is specified for a remote file, the system searches an authorized directory for the specified file. |
     | Delete a specified file from the FTP server. | [**delete**](cmdqueryname=delete) *remote-filename* | - |
     | Upload one or more files. | [**put**](cmdqueryname=put) *local-filename* [ *remote-filename* ]  or  [**mput**](cmdqueryname=mput) *local-filenames* | + The [**put**](cmdqueryname=put) command uploads a single file. + The [**mput**](cmdqueryname=mput) command uploads multiple files at a time. |
     | Download one or more files. | [**get**](cmdqueryname=get) *remote-filename* [ *local-filename* ]  or  [**mget**](cmdqueryname=mget) *remote-filenames* | + The [**get**](cmdqueryname=get) command downloads a single file. + The [**mget**](cmdqueryname=mget) command downloads multiple files at a time. |
     | Set the data transmission mode to ASCII. | [**ascii**](cmdqueryname=ascii) | Run only one of the commands.  + By default, the data transmission mode is ASCII. + ASCII is used to transfer text files. Binary is used for transferring programs, system software, and database files. |
     | Set the data transmission mode to binary. | [**binary**](cmdqueryname=binary) |
     | Set the file transfer mode to passive. | [**passive**](cmdqueryname=passive) | Run only one of the commands.  By default, the file transfer mode is active. |
     | Set the file transfer mode to active. | [**undo passive**](cmdqueryname=undo+passive) |
     | Display online help for an FTP command. | [**remotehelp**](cmdqueryname=remotehelp) [ *command* ] | - |
     | Enable the file transfer prompt function. | [**prompt**](cmdqueryname=prompt) | By default, the prompt function is disabled. |
     | Enable the verbose function. | [**verbose**](cmdqueryname=verbose) | After the verbose function is enabled, all FTP responses are displayed on the FTP client, including the FTP protocol information and details about the responses. |
     | Enable resumable data transfer for the FTP client. | [**ftp client resumable-transfer enable**](cmdqueryname=ftp+client+resumable-transfer+enable) | By default, resumable data transfer is disabled for an FTP client. This command takes effect in the system view. |
* **(Optional) Change the login user.**
  
  
  
  You can log in to the FTP server using another user name without exiting the FTP client view. The created FTP connection is the same as the FTP connection created by running the [**ftp**](cmdqueryname=ftp) command.
  
  **Table 7** Changing the login user
  | Operation | Command | Description |
  | --- | --- | --- |
  | Change the current login user in the FTP client view. | [**user**](cmdqueryname=user) *username* | After the login user is changed, the original user is disconnected from the server. |
* **Disconnect from the FTP server.**
  
  
  
  You can run different commands in the FTP client view to disconnect from the FTP server.
  
  **Table 8** Disconnect from the FTP server.
  | Operation | Command | Description |
  | --- | --- | --- |
  | Disconnect from the FTP server and return to the user view. | [**bye**](cmdqueryname=bye)  or [**quit**](cmdqueryname=quit) | Run only one of the commands. |
  | Disconnect from the FTP server and remain in the FTP client view. | [**close**](cmdqueryname=close)  or [**disconnect**](cmdqueryname=disconnect) |

#### Verifying the Configuration

* Run the [**display ftp client**](cmdqueryname=display+ftp+client) command to check the source address of the FTP client.