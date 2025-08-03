Configuring a Device as an FTP Server
=====================================

Configuring a Device as an FTP Server

#### Prerequisites

You can log in to a device that functions as an FTP server from a terminal to manage files. FTP is widely used for file service operations such as system software upgrade.

Before configuring a device as an FTP server to manage files, you have completed the following tasks:

* Ensure that there are reachable routes between the terminal and the device.
* Ensure that the terminal has FTP client software installed.
* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

SFTP V2 or SCP is more secure than FTP, and is therefore recommended.

In FIPS mode, FTP cannot be used to manage files.

[Table 1](#EN-US_TASK_0000001563990885__table12310195121710) describes the process for configuring a device as an FTP server for file management. Tasks 1, 2, 3, and 4 can be performed in any sequence.

**Table 1** Configuring a device as an FTP server for file management
| No. | Task | Description |
| --- | --- | --- |
| 1 | [Enable the FTP server function and configure related parameters.](#EN-US_TASK_0000001563990885__dc_cfg_file_0006step01) | Enable the FTP server function and configure related parameters such as the port number, source IP address, and timeout interval. |
| 2 | [Configure a local FTP user.](#EN-US_TASK_0000001563990885__dc_cfg_file_0006step02) | Configure the service type, user privilege level, and authorized directory for an FTP user. |
| 3 | [(Optional) Configure FTP access control.](#EN-US_TASK_0000001563990885__step1596607667175329) | Configure ACL rules and a basic FTP ACL to improve FTP access security. |
| 4 | [(Optional) Configure the IP address locking function.](#EN-US_TASK_0000001563990885__step524499282175329) | Enable the IP address locking function and configure parameters such as the maximum number of consecutive authentication failures and a period in which consecutive authentication failures are counted. |
| 5 | [Log in to the device through FTP.](#EN-US_TASK_0000001563990885__step1968137898175329) | Log in to the device from a terminal through FTP. |



#### Default Settings

**Table 2** Default settings
| Parameter | Default Setting |
| --- | --- |
| FTP server function | Disabled |
| Port number | 21 |
| FTP user | None created |



#### Procedure

* **Enable the FTP server function and configure related parameters.**
  
  
  
  **Table 3** Enabling the FTP server function and configuring related parameters
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | (Optional) Specify a port number for the FTP server. | [**ftp**](cmdqueryname=ftp) [ **ipv6** ] **server port** *port-number* | By default, the port number of the FTP server is 21.  If a new port number is configured, the FTP server terminates all FTP connections and then uses the new port number to listen to connection requests. In this way, attackers cannot connect to the server through the standard FTP port, ensuring security. |
  | (Optional) Specify the maximum number of connections to an FTP server. | [**ftp server max-sessions**](cmdqueryname=ftp+server+max-sessions) *max-session-count* | By default, the maximum number of connections to an FTP server is 15.  This command applies to both IPv4 and IPv6 connections.  If the maximum number is less that or equal to the number of current connections, the current connections are not disconnected, but new connection requests will be rejected. |
  | Enable the FTP server function. | [**ftp**](cmdqueryname=ftp) [ **ipv6** ] **server** **enable** | By default, the FTP server function is disabled. |
  | Specify the source interface or source IP address for the FTP server. | + [**ftp server source**](cmdqueryname=ftp+server+source) { **-a** *ip-address* | **-i** { *interface-type interface-number* | interface-name } } + [**ftp ipv6 server source -a**](cmdqueryname=ftp+ipv6+server+source+-a) *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ] + [**ftp**](cmdqueryname=ftp) [ **ipv6**  ] [**server source all-interface**](cmdqueryname=server+source+all-interface) | Specify the source interface or source IP address for the FTP server to filter incoming and outgoing packets, ensuring security.  After the source IP address is specified for the FTP server, you must use the specified IP address to log in to the FTP server. Otherwise, the login fails.  NOTE:  Run one of the commands as required. |
  | (Optional) Configure the idle duration for FTP connections. | [**ftp**](cmdqueryname=ftp) [ **ipv6** ] [**server**](cmdqueryname=server) **timeout** *minutes* | By default, the idle duration is 10 minutes.  If an FTP connection is idle during the specified period of time, the FTP server automatically disconnects from the FTP client. |
  | (Optional) Configure the alarm generation and clearance thresholds for the number of FTP server login failures within a specified period. | [**ftp server login-failed threshold-alarm**](cmdqueryname=ftp+server+login-failed+threshold-alarm) **upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time* | By default, an alarm is generated if the number of login failures reaches 30 within 5 minutes and is cleared if the number of login failures falls below 20 within the same period. |
  | (Optional) Configure the maximum number of FTP connections to the server that can be established for a single IP address. | [**ftp server ip-max-sessions**](cmdqueryname=ftp+server+ip-max-sessions) *ip-max-sessions-num* | By default, the maximum number of FTP connections to the server for a single IP address is 15. |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
  
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  + The FTP service port cannot be changed after the FTP server function is enabled. To change the port number, you must run the [**undo ftp**](cmdqueryname=undo+ftp) [ **ipv6** ] [**server**](cmdqueryname=server) command to disable the FTP server function first.
  + After file operations between the client and server are complete, run the [**undo ftp**](cmdqueryname=undo+ftp) [ **ipv6** ] [**server**](cmdqueryname=server) command to disable the FTP server function promptly to ensure device security.
* **Configure a local FTP user.**
  
  
  
  To use FTP to manage files, configure the local user name and password for logging in to the device that functions as an FTP server, and specify the service type and authorized directory.
  
  **Table 4** Configuring a local FTP user
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Enter the AAA view. | [**aaa**](cmdqueryname=aaa) | - |
  | Configure the local user name and password. | [**local-user**](cmdqueryname=local-user) *user-name* **password** **irreversible-cipher** *password* | For security purposes, change the password periodically. |
  | Configure the privilege level for the local user. | [**local-user**](cmdqueryname=local-user) *user-name* **privilege level** *level* | You must set the user privilege level to the management level. Otherwise, the FTP connection cannot be established. |
  | Set the service type of the local user to FTP. | [**local-user**](cmdqueryname=local-user) *user-name* **service-type** **ftp** | By default, a local user can use any type of access services. |
  | Configure an authorized directory for the FTP user. | [**local-user**](cmdqueryname=local-user) *user-name* **ftp-directory** *directory* | By default, no authorized directory is configured for the local user. |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **(Optional) Configure FTP access control.**
  
  
  
  An ACL is a list of rules that classify and filter packets according to their source address, destination address, port number, and other fields. After an ACL is applied to a routing device, the routing device determines whether to permit or deny a packet based on the ACL rules.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  You can configure an ACL to allow only specified clients to access an FTP server.
  
  ACL rule:
  + When the **permit** action is defined in an ACL rule, devices that match the rule can set up FTP connections with the local device.
  + When the **deny** action is defined in an ACL rule, devices that match the rule cannot set up FTP connections with the local device.
  + If packets from other devices do not match any rule in an ACL, these devices cannot set up FTP connections with the local device.
  + If no rule is defined in an ACL, any other devices can set up FTP connections with the local device.
  
  **Table 5** (Optional) Configuring FTP access control
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Enter the ACL view. | [**acl**](cmdqueryname=acl) { [ **number** ] *basic-acl-number* | **name** *basic-acl-name* } | - |
  | Configure an ACL rule. | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit**  | **deny** } [ **fragment-type** **fragment** | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* | **logging** ] \* | - |
  | Exit the system view. | [**quit**](cmdqueryname=quit) | - |
  | Apply the ACL for the FTP service. | [**ftp**](cmdqueryname=ftp) [ **ipv6** ] [**server**](cmdqueryname=server) **acl** { *acl-number* | *name* } | - |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **(Optional) Configure the IP address locking function.**
  
  
  
  After the IP address locking function is enabled, the number of FTP server login failures is recorded on a per IP address-basis. If the number of login failures for an IP address within a specified period reaches the threshold, the IP address is locked, and this IP address cannot set up an FTP connection with the FTP server.
  
  **Table 6** (Optional) Configuring the IP address locking function
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Enable the client IP address locking function on the FTP server. | [**undo ftp server ip-block disable**](cmdqueryname=undo+ftp+server+ip-block+disable) | By default, the client IP address locking function is enabled. |
  | Configure the maximum number of consecutive authentication failures and the period in which consecutive authentication failures are counted. | [**ftp server ip-block failed-times**](cmdqueryname=ftp+server+ip-block+failed-times) *failed-times* **period** *period* | By default, a maximum of 6 consecutive authentication failures is allowed within 5 minutes. |
  | Configure the period after which the system automatically unlocks a user. | [**ftp server ip-block reactive**](cmdqueryname=ftp+server+ip-block+reactive) *reactive-period* | By default, the period is 5 minutes. |
  | Exit the system view. | [**quit**](cmdqueryname=quit) | - |
  | Unlock an IP address. | [**activate ftp server ip-block ip-address**](cmdqueryname=activate+ftp+server+ip-block+ip-address) *ip-address* [ **vpn-instance** *vpn-name* ] | - |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Log in to the device through FTP.**
  
  
  
  To log in to the FTP server from a terminal, use either the Windows CLI or third-party software. The following uses the Windows CLI as an example.
  
  + Run the [**ftp**](cmdqueryname=ftp) *ip-address* command to log in to the device through FTP.
    
    The IP address entered here is the IP address configured on the device and must be reachable to the IP address of the user terminal.
  + Enter the user name and password at the prompt, and press **Enter**. If the command prompt of the FTP client view, **ftp>** for example, is displayed, you have entered the working directory of the FTP server. (The following information is for reference only.)
  ```
  C:\Windows\System32> ftp 192.168.150.208
  Connected to 192.168.150.208.
  220 FTP service ready.
  User(192.168.150.208:(none)):admin123331 Password required for admin123.
  Password:
  230 User logged in.
  ftp>
  ```
* **Perform file operations using FTP.**
  
  
  
  After logging in to the FTP server, you can run FTP commands to perform operations on files, including managing directories, managing files, configuring the file transfer mode, and viewing online help of FTP commands.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The operation rights of a user are set on the FTP server.
  
  You can perform one or more operations listed in the following table, and in any sequence.
  
  **Table 7** Performing file operations using FTP
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
* **(Optional) Change the login user.**
  
  
  
  You can log in to the FTP server using another user name without exiting the FTP client view. The created FTP connection is the same as the FTP connection created by running the [**ftp**](cmdqueryname=ftp) command.
  
  **Table 8** Changing the login user
  | Operation | Command | Description |
  | --- | --- | --- |
  | Change the current login user in the FTP client view. | [**user**](cmdqueryname=user) *username* | After the login user is changed, the original user is disconnected from the server. |
* **Disconnect from the FTP server.**
  
  
  
  You can run different commands in the FTP client view to disconnect from the FTP server.
  
  **Table 9** Disconnecting from the FTP server
  | Operation | Command | Description |
  | --- | --- | --- |
  | Disconnect from the FTP server and return to the user view. | [**bye**](cmdqueryname=bye)  or [**quit**](cmdqueryname=quit) | Run only one of the commands. |
  | Disconnect from the FTP server and remain in the FTP client view. | [**close**](cmdqueryname=close)  or [**disconnect**](cmdqueryname=disconnect) |

#### Verifying the Configuration

* Run the [**display ftp server**](cmdqueryname=display+ftp+server) command to check the configuration and status of the FTP server.
* Run the [**display ftp server users**](cmdqueryname=display+ftp+server+users) command to check information about FTP users.
* Run the [**display ftp server ip auth-fail information**](cmdqueryname=display+ftp+server+ip+auth-fail+information) command to check details about the IP addresses of the clients that fail to be authenticated, including the time when the first authentication fails and the number of authentication failures.
* Run the [**display ftp server ip-block list**](cmdqueryname=display+ftp+server+ip-block+list) command to check the FTP client IP addresses that are locked due to authentication failures and the remaining locking time.