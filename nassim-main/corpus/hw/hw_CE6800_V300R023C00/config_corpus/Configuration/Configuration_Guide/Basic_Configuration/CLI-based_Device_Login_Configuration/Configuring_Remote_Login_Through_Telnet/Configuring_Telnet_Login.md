Configuring Telnet Login
========================

Configuring Telnet Login

#### Prerequisites

Before configuring Telnet login, you have completed the following task:

* Ensure that there are reachable routes between the terminal and the device.
* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.

#### Context

![](public_sys-resources/note_3.0-en-us.png) 

* STelnet is more secure than Telnet, and is therefore recommended.
* In FIPS mode, Telnet cannot be used.

[Table 1](#EN-US_TASK_0000001563893017__tab_dc_cfg_login_000601) describes the tasks involved in the Telnet login configuration process.

**Table 1** Tasks involved in Telnet login configuration
| No. | Task | Description | Remarks |
| --- | --- | --- | --- |
| 1 | [Enable the Telnet server function and configure related parameters.](#EN-US_TASK_0000001563893017__cmd621941286175336) | Enable the Telnet server function and configure related parameters. | Tasks 1, 2, and 3 can be performed in any sequence. |
| 2 | [Configure a VTY user interface for Telnet login.](#EN-US_TASK_0000001563893017__cmd1171124761175336) | Configure the user privilege level, authentication mode, whether to support the Telnet protocol, and other basic VTY user interface attributes. |
| 3 | [Configure a local Telnet user.](#EN-US_TASK_0000001563893017__cmd632670411175336) | Create the Telnet user name and password, service type, and user privilege level. |
| 4 | [Log in to the device using Telnet from a terminal.](#EN-US_TASK_0000001563893017__cmd407162113175336) | Use the Telnet client software to log in to the device from a terminal. | - |



#### Default Settings

**Table 2** Default settings for configuring Telnet login
| Parameter | Default Setting |
| --- | --- |
| Telnet server function | Enabled |
| Telnet server port | 23 |
| Authentication mode for a VTY user interface | No authentication mode configured |
| Protocol supported by a VTY user interface | All protocols |
| User privilege level | The default command privilege level for a VTY user interface is 0. |



#### Procedure

* **Enable the Telnet server function and configure related parameters.**
  
  
  
  Before telneting to the device from a user terminal, ensure that the Telnet server function is enabled on the device.
  
  **Table 3** Enabling the Telnet server function and configuring related parameters
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Enable the Telnet server function. | **undo** [**telnet**](cmdqueryname=telnet+server+disable) [ **ipv6** ] **server disable** | By default:  + The Telnet server function is enabled. + If a device starts with a configuration file and the configuration file does not contain the [**telnet [ ipv6 ] server disable**](cmdqueryname=telnet+%5B+ipv6+%5D+server+disable) command, the Telnet service is enabled. |
  | (Optional) Configure a port number for the Telnet server. | [**telnet**](cmdqueryname=telnet+server+port) [ **ipv6** ] **server port** *port-number* | The default port number is 23.  Configuring a new port number for the Telnet server prevents attackers from accessing the server using the standard Telnet server port. |
  | (Optional) Configure an ACL. | + [**telnet server acl**](cmdqueryname=telnet+server+acl) { *acl4name* | *acl4num* } + [**telnet**](cmdqueryname=telnet+server+acl) [ **ipv6** ] **server acl** { *acl6name* | *acl6num* } | By default, no ACL is configured.  An ACL is configured to determine which clients can access the device using Telnet. |
  | Configure the source interface for the Telnet server. | + [**telnet server-source**](cmdqueryname=telnet+server-source) **-i**  { *interface-type* *interface-number* | *interface-name* } + [**telnet ipv6 server-source**](cmdqueryname=telnet+ipv6+server-source) **-a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ] + [**telnet**](cmdqueryname=telnet+server-source) [ **ipv6** ] [**server-source all-interface**](cmdqueryname=server-source+all-interface) | By default, no source interface is specified for a Telnet server.  NOTE:  + If the specified source interface is a loopback interface, the loopback interface must have been created. Otherwise, the configuration cannot be executed. + You can run one of the commands as required. |
  | (Optional) Enable the client IP address locking function on the Telnet server. | **undo** [**telnet server ip-block disable**](cmdqueryname=telnet+server+ip-block+disable) | By default, the function of locking client IP addresses is enabled on a Telnet server.  If a user fails authentication for six consecutive times within 5 minutes, the user's IP address will be locked for 5 minutes. To unlock the IP address before the locking period elapses, run the **activate vty ip-block ip-address** *ip-address* [ **vpnname** *vpn-name* ] command. |
  | (Optional) Configure alarm generation and clearance thresholds for the number of Telnet server login failures within a specified period. | [**telnet server login-failed threshold-alarm**](cmdqueryname=telnet+server+login-failed+threshold-alarm) **upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time* | By default, an alarm is generated when 30 or more login failures occur within 5 minutes. The alarm is cleared when the number of login failures within 5 minutes falls below 20. |
  | (Optional) Configure the maximum number of Telnet connections to the server that can be established for a single IP address. | [**telnet server ip-limit-session**](cmdqueryname=telnet+server+ip-limit-session) *limit-session-num* | By default, a maximum of 64 Telnet connections to the server can be established for a single IP address. |
  | (Optional) Configure the DSCP priority of Telnet packets. | [**telnet server dscp**](cmdqueryname=telnet+server+dscp) *value* | By default, the DSCP priority of Telnet packets is 48. |
  | Return to the user view. | [**quit**](cmdqueryname=quit) | - |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Configure a VTY user interface for Telnet login.**
  
  
  
  Configure the user privilege level and other basic attributes for the VTY user interface.
  
  **Table 4** Configuring a VTY user interface for Telnet login
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Enter the VTY user interface view. | [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ] | - |
  | Configure a user privilege level for the user interface. | [**user privilege**](cmdqueryname=user+privilege) **level** *level* | By default, the user privilege level of a VTY user interface is 0.  To run the commands of a higher privilege level, configure a higher user privilege level.  If the command privilege level configured for a user interface conflicts with the user privilege level configured for a user, the configured user privilege level takes precedence. |
  | Configure the user authentication mode. | [**authentication-mode**](cmdqueryname=authentication-mode) { **password** | **aaa** } | The device provides two authentication modes: password authentication and AAA authentication. You can choose either of them as required. + If the password authentication mode is selected, run the [**set authentication password**](cmdqueryname=set+authentication+password) command to set the local authentication password. + If the AAA authentication mode is selected, configure a Telnet local user by referring to [Configuring a local Telnet user (AAA authentication mode)](#EN-US_TASK_0000001563893017__login0403). For details about the authentication mode, see [Configuring a VTY User Interface](vrp_login_cfg_0025.html). You are advised to select the AAA authentication mode. |
  | Configure the VTY user interface to support the Telnet protocol. | [**protocol inbound**](cmdqueryname=protocol+inbound) { **all** | **telnet** } | By default, a VTY user interface supports all protocols. |
  | (Optional) Configuring other attributes of the user interface. | For details, see [Configuring a VTY User Interface](vrp_login_cfg_0025.html). | Use the default settings for other attributes of the VTY user interface. You can also modify these attributes according to your requirements. |
  | Exit the VTY user interface view. | [**quit**](cmdqueryname=quit) | - |
  | Return to the user view. | [**quit**](cmdqueryname=quit) | - |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Configure a local Telnet user (AAA authentication mode).**
  
  
  
  Configure a local user name and password for the administrator to ensure that only the administrator can log in to the device.
  
  **Table 5** Configuring a local Telnet user (AAA authentication mode)
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Enter the AAA view. | [**aaa**](cmdqueryname=aaa) | - |
  | Configure the local user name and password. | [**local-user**](cmdqueryname=local-user) *user-name* **password** **irreversible-cipher** *password* | For security purposes, change the password periodically. |
  | Configure the service type for the local user. | [**local-user**](cmdqueryname=local-user) *user-name* **service-type** **telnet** | - |
  | Configure the privilege level for the local user. | [**local-user**](cmdqueryname=local-user) *user-name* **privilege level** *level* | After login, a user can only run the commands at privilege levels equal to or lower than the user privilege level, thereby ensuring the device security.  If the command privilege level configured for a user interface conflicts with the user privilege level configured for a user, the configured user privilege level takes precedence. |
  | Exit the AAA view. | [**quit**](cmdqueryname=quit) | - |
  | Return to the user view. | [**quit**](cmdqueryname=quit) | - |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Log in to the device using Telnet from a terminal.**
  
  
  
  You can use Windows CLI or third-party software to log in to the device using Telnet from a terminal. Windows CLI is used in the following example.
  
  Perform the following operations on the terminal:
  
  1. Enter the Windows CLI.
  2. Run the **telnet** *ip-address port* command to log in to the device using Telnet.
     
     ```
     C:\Documents and Settings\Administrator> telnet 10.137.217.177 1025
     ```
  3. Press **Enter** and enter the password and the user name configured for the AAA authentication mode. If the authentication is successful, the command line prompt for the user view is displayed, indicating that you have successfully logged in to the device. (The following information is for reference only.)
     ```
     Username:admin1234
     Password:
     Info: The max number of VTY users is 21, the number of current VTY users online is 1, and total number of terminal users online is 1.
           The current login time is 2020-12-15 14:23:00.
     <Telnet Server>
     ```

#### Verifying the Configuration

* Run the [**display users**](cmdqueryname=display+users) [ **all** ] command to check information about users who have logged in to a device through the user interfaces.
* Run the [**display tcp status**](cmdqueryname=display+tcp+status) command to check all TCP connections.
* Run the [**display telnet server status**](cmdqueryname=display+telnet+server+status) command to check the current connections of the Telnet server.
* Run the [**display vty ip-block list**](cmdqueryname=display+vty+ip-block+list) command to check the list of IP addresses that are blocked due to authentication failures.
* Run the [**display vty ip-block all**](cmdqueryname=display+vty+ip-block+all) command to check all IP addresses that fail to be authenticated.