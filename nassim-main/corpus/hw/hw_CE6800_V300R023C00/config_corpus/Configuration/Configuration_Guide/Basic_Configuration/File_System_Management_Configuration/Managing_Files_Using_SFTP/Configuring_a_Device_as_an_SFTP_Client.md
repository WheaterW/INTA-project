Configuring a Device as an SFTP Client
======================================

Configuring a Device as an SFTP Client

#### Prerequisites

After a device is configured as an SFTP client, client authentication and bidirectional data encryption are used to ensure secure file transfer and file and directory management.

Before configuring a device to access files on another device as an SFTP client, you have completed the following tasks:

* Ensure that there are reachable routes between the device and SSH server.
* Obtain the IP address of the SSH server and SSH user information, and ensure that the SSH user has been assigned the highest privilege level.
* Obtain the port number configured for the server if the standard port number is not used.

#### Context

[Table 1](#EN-US_TASK_0000001563750989__file13tab01) describes the process for configuring a device to access files on another device as an SFTP client.

**Table 1** Configuring a device to access files on another device as an SFTP client
| No. | Task | Description | Remarks |
| --- | --- | --- | --- |
| 1 | [(Optional) Configure the source interface or source IP address for the SFTP client.](#EN-US_TASK_0000001563750989__p_03C940EB) | Configure the source interface or source IP address for the SFTP client to implement security verification. | Tasks 1, 2, and 3 can be performed in any sequence. |
| 2 | [Configure the mode for connecting a device to the SSH server for the first time.](#EN-US_TASK_0000001563750989__file13-step_01) | You can enable first login for the SSH client or configure the SSH client to assign a public key to the SSH server. |
| 3 | [Configure SFTP client parameters.](#EN-US_TASK_0000001563750989__step57147208551) | SFTP client parameters include the interval for sending keepalive packets and the maximum number of keepalive packets sent by the SFTP client. |
| 4 | [(One-click mode) Log in to another device to perform file operations.](#EN-US_TASK_0000001563750989__step82084916614) | Select only one of the two tasks.   * One-click mode: You can upload and download files while the connection is set up. * Interactive mode: After the SSH server is connected, you can perform operations on directories and files on the SSH server and view the help of commands on the SFTP client. |
| [(Interactive mode) Log in to another device to perform file operations.](#EN-US_TASK_0000001563750989__step167318301294) |
| 5 | [Disconnect from the SFTP server.](#EN-US_TASK_0000001563750989__file1306_sftp) | - |



#### Procedure

* **(Optional) Configure the source interface or source IP address for the SFTP client.**
  
  
  
  The source IP address to be configured must be that of a stable interface, such as a loopback interface. This configuration makes it easier to configure ACL rules. You simply need to specify the source or destination IP address in an ACL rule as the interface IP address, thereby allowing the device to filter incoming and outgoing packets.
  
  **Table 2** Configuring the source interface or source IP address for the SFTP client
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Configure the source interface or source IP address for the SFTP client. | [**sftp client-source**](cmdqueryname=sftp+client-source) { **-a** *source-ip-address* [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | **-i** { *interface-type* *interface-number* | *interface-name* } }  or  [**sftp ipv6 client-source**](cmdqueryname=sftp+ipv6+client-source) **-a** *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] | By default, the source IP address is 0.0.0.0. |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Configure the mode for connecting a device to the SSH server for the first time.**
  
  
  
  For details, see "Configuring the Mode for Connecting a Device to the SSH Server for the First Time" in Configuration Guide > Security Configuration.
* **Configure SFTP client parameters.**
  
  
  
  For details, see "Setting SSH Client Parameters" in Configuration Guide > Security Configuration.
* **(One-click mode) Log in to another device to perform file operations.**
  
  
  
  You can run the commands listed in the following table in the system view to download files from the server or upload files to the server while the connection is set up.
  
  
  
  **Table 3** One-click file operations using commands
  | Operation | Command | Description |
  | --- | --- | --- |
  | Connect to the SFTP server using an IPv4 address. | [**sftp client-transfile**](cmdqueryname=sftp+client-transfile) { **get** | **put** } [ **-a** *source-address* | **-i** *interface-type interface-number* ] **host-ip** *host-ipv4* [ *port* ] [ **public-net** | **-vpn-instance** *vpn-instance-name* | **prefer\_kex** *prefer\_kex* | **identity-key** { **rsa** | **dsa** | **ecc** } | **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* | **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* | **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* | **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* | **-ki** *interval* | **-kc** *count* ] \* **username** *user-name* **password** *password* **sourcefile** *source-file* [ **destination** *destination* ] | Connect to the SFTP server in IPv4 mode and download files from the server to the SFTP client or upload files from the SFTP client to the server. |
  | Connect to the SFTP server using an IPv6 address. | [**sftp client-transfile**](cmdqueryname=sftp+client-transfile) { **get** | **put** } **ipv6** [ **-a** *source-ipv6-address* ] **host-ip** *host-ipv6* [ **-oi** *interface-type interface-number* ] [ *port* ] [ **public-net** | **-vpn-instance** *vpn-instance-name* | **prefer\_kex** *prefer\_kex* | **identity-key** { **rsa** | **dsa** | **ecc** } | **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* | **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* | **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* | **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* | **-ki** *interval* | **-kc** *count* ] \* **username** *user-name* **password** *password* **sourcefile** *source-file* [ **destination** *destination* ] | Connect to the SFTP server in IPv6 mode and download files from the server to the SFTP client or upload files from the SFTP client to the server. |
  
  
  The following is used for reference only.
  ```
  <HUAWEI> system-view
  [~HUAWEI] sftp client-transfile get host-ip 10.10.1.1 username client password YsHsjx_202206 sourcefile sourcefile.txt
  Trying 10.10.1.1 ...
  Press CTRL+K to abort
  Connected to 10.10.1.1 ...
  Remote file: /sourcefile.txt --->  Local file: 1#flash:/sourcefile.txt
  Downloading the file. Please wait..
  Downloading file successfully ended.  
  File download is completed in 375 seconds. 
  ```
* **(Interactive mode) Log in to another device to perform file operations.**
  1. **Connect to another device using SFTP commands.**
     
     
     
     **Table 4** Connecting to another device using SFTP commands
     | Operation | Command | Description |
     | --- | --- | --- |
     | Connect to the SFTP server using an IPv4 address in the system view. | [**sftp**](cmdqueryname=sftp) [ **-a** *source-ip-address* | **-i** *interface-type interface-number* ] [ **-force-receive-pubkey** ] *host-ip-address* [ *port-number* ] [ [ **prefer\_kex***prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **public-net** | **-vpn-instance***vpn-instance-name* ] | [ **-ki***interval* ] | [ **-kc***count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* | Select either of the commands based on the address type.  In most cases, only IP addresses need to be specified in the command.  If the source interface is specified using **-i** *interface-type interface-number*, the **public-net** and **-vpn-instance** *vpn-instance-name* parameters are not supported. |
     | Connect to the SFTP server using an IPv6 address in the system view. | [**sftp ipv6**](cmdqueryname=sftp+ipv6) [ **-force-receive-pubkey** ] [ **-a** *source-ipv6-address* ] *host-ipv6-address* [ [ [ **-vpn-instance** *vpn-instance-name* ] | **public-net** ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] [ *port-number* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ] \* |
     
     
     For example, after you run the following command:
     ```
     <HUAWEI> system-view
     [~HUAWEI] sftp 10.137.217.201
     ```
     
     If the command prompt **sftp-client>** is displayed, you have entered in the SFTP client view, indicating that the SFTP client is successfully connected to the server.
  2. **Perform file operations using SFTP commands.**
     
     
     
     After logging in to the SSH server from the SFTP client, you can perform the operations listed in [Table 5](#EN-US_TASK_0000001563750989__file13-table_03) on the SFTP client.
     
     You can perform one or more operations listed in the following table, and in any sequence.
     
     **Table 5** Performing file operations using SFTP commands
     | Operation | Command | Description |
     | --- | --- | --- |
     | Change the current working directory. | [**cd**](cmdqueryname=cd) [ *path* ] | - |
     | Chang the current working directory to its upper-level directory. | [**cdup**](cmdqueryname=cdup) | - |
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
  
  
  
  **Table 6** Disconnecting from the SFTP server
  | Operation | Command | Description |
  | --- | --- | --- |
  | Disconnect from the SFTP server. | [**quit**](cmdqueryname=quit) | You can also run the [**bye**](cmdqueryname=bye) or [**exit**](cmdqueryname=exit) command to disconnect from the SFTP server. |

#### Verifying the Configuration

* Run the [**display sftp client**](cmdqueryname=display+sftp+client) command to check the configuration of the SFTP client.
* Run the [**display ssh server-info**](cmdqueryname=display+ssh+server-info) command to check the mapping between all SSH servers and public keys on the client.