Configuring the Console User Interface
======================================

Configuring the Console User Interface

#### Prerequisites

To locally configure and manage a device through the console port, configure attributes for the console user interface as needed.


#### Procedure

**Table 1** Configuring physical attributes for the console user interface
| Operation | Command | Description |
| --- | --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
| Enter the console user interface view. | [**user-interface**](cmdqueryname=user-interface) **console** *interface-number* | - |
| Set the transmission rate. | [**speed**](cmdqueryname=speed) *speed-value* | By default, the transmission rate is 9600 bit/s. |
| Set the flow control mode. | [**flow-control**](cmdqueryname=flow-control) { **hardware** | **none** | **software** } | By default, the flow control mode is none. |
| Set the parity bit. | [**parity**](cmdqueryname=parity) { **even** | **mark** | **none** | **odd** | **space** } | By default, the parity bit is none. |
| Set the stop bit. | [**stopbits**](cmdqueryname=stopbits) { **1.5** | **1** | **2** } | By default, the stop bit is 1. |
| Set the data bit. | [**databits**](cmdqueryname=databits) { **5** | **6** | **7** | **8** } | By default, the data bit is 8. |
| Exit the console user interface view. | [**quit**](cmdqueryname=quit) | - |
| Return to the user view. | [**quit**](cmdqueryname=quit) | - |
| Commit the configuration. | [**commit**](cmdqueryname=commit) | - |


![](public_sys-resources/note_3.0-en-us.png) 

To log in to a device through a console interface, you must ensure that physical attribute configurations on the terminal emulator for the console user interface are the same as those of the console user interface on the device. Otherwise, you cannot log in to the device.


**Table 2** Configuring terminal attributes for the console user interface
| Operation | Command | Description |
| --- | --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
| Enter the console user interface view. | [**user-interface**](cmdqueryname=user-interface) **console** *interface-number* | - |
| Set the connection timeout period. | [**idle-timeout**](cmdqueryname=idle-timeout) *minutes* [ *seconds* ] | If a connection remains idle during the specified period, the terminal will be automatically disconnected from the device. By default, the connection timeout period is 5 minutes. NOTE:  If the connection timeout period is set to too large a value, the terminal will remain connected, posing security risks. To prevent risks, you are advised to run the [**lock**](cmdqueryname=lock) command in the user view to lock the connection. |
| Set the number of lines to be displayed on a terminal screen. | [**screen-length**](cmdqueryname=screen-length) *screen-length* [ **temporary** ] | The **temporary** parameter specifies the number of lines to be temporarily displayed on a terminal screen.  By default, 24 lines are displayed on a terminal screen. |
| Set the buffer size for historical commands. | [**history-command max-size**](cmdqueryname=history-command+max-size) *size-value* | By default, a maximum of 10 historical commands can be buffered. |
| Exit the console user interface view. | [**quit**](cmdqueryname=quit) | - |
| Return to the user view. | [**quit**](cmdqueryname=quit) | - |
| Commit the configuration. | [**commit**](cmdqueryname=commit) | - |


**Table 3** Configuring the user privilege level for the console user interface
| Operation | Command | Description |
| --- | --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
| Enter the console user interface view. | [**user-interface**](cmdqueryname=user-interface) **console** *interface-number* | - |
| Set the user privilege level. | [**user privilege**](cmdqueryname=user+privilege) **level** *level* | [Table 1](vrp_cli_cfg_0005.html#EN-US_TASK_0000001513050518__tab_dc_vrp_cfg_00902901) lists the mapping between user privilege levels and command privilege levels.  By default, the default command privilege level for the console user interface is 3.  NOTE:  If the command privilege level configured for a user interface conflicts with the user privilege level configured for a user, the configured user privilege level takes precedence. |
| Exit the console user interface view. | [**quit**](cmdqueryname=quit) | - |
| Return to the user view. | [**quit**](cmdqueryname=quit) | - |
| Commit the configuration. | [**commit**](cmdqueryname=commit) | - |


**Table 4** Configuring the AAA authentication mode for the console user interface
| Operation | Command | Description |
| --- | --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
| Enter the console user interface view. | [**user-interface**](cmdqueryname=user-interface) **console** *interface-number* | - |
| Set the user authentication mode to AAA. | [**authentication-mode**](cmdqueryname=authentication-mode) **aaa** | - |
| Exit the console user interface view. | [**quit**](cmdqueryname=quit) | - |
| Enter the AAA view. | [**aaa**](cmdqueryname=aaa) | - |
| Configure the local user name and password. | [**local-user**](cmdqueryname=local-user) *user-name* **password** **irreversible-cipher** *password* | For security purposes, change the password periodically. |
| Set the local user access type to console. | [**local-user**](cmdqueryname=local-user) *user-name* **service-type** **terminal** | **terminal**: indicates a terminal user, which is usually a user connected using a console port. |
| Exit the AAA view. | [**quit**](cmdqueryname=quit) | - |
| Return to the user view. | [**quit**](cmdqueryname=quit) | - |
| Commit the configuration. | [**commit**](cmdqueryname=commit) | - |


**Table 5** Configuring the password authentication mode for the console user interface
| Operation | Command | Description |
| --- | --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
| Enter the console user interface view. | [**user-interface**](cmdqueryname=user-interface) **console** *interface-number* | - |
| Set the user authentication mode to password authentication. | [**authentication-mode**](cmdqueryname=authentication-mode) **password** | - |
| Set the authentication password. | [**set authentication password**](cmdqueryname=set+authentication+password) [ **cipher** *password* ] | The password can be a ciphertext or cleartext password. If you do not specify **cipher** *password*, you can enter a cleartext password in interactive mode. If you specify **cipher** *password*, you can enter a cleartext or ciphertext password. Both types of passwords are saved to the configuration file in cipher text. For security purposes, change the password periodically.  NOTE:  After the weak password dictionary maintenance function is enabled, the passwords (which can be queried using the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command) defined in the weak password dictionary cannot be specified in this command. |
| Exit the console user interface view. | [**quit**](cmdqueryname=quit) | - |
| Return to the user view. | [**quit**](cmdqueryname=quit) | - |
| Commit the configuration. | [**commit**](cmdqueryname=commit) | - |


**Table 6** Disabling the console user interface
| Operation | Command | Description |
| --- | --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
| Enter the console user interface view. | [**user-interface**](cmdqueryname=user-interface) **console** *interface-number* | - |
| Disable the console user interface view. | [**shutdown**](cmdqueryname=shutdown) | By default, the console user interface is enabled.  After the **shutdown** command is run, the specified user interface is disabled and you cannot log in to the device through the user interface. However, you can still configure commands in the user interface view.  To enable the console user interface view, run the **undo shutdown** command. |
| Exit the console user interface view. | [**quit**](cmdqueryname=quit) | - |
| Return to the user view. | [**quit**](cmdqueryname=quit) | - |
| Commit the configuration. | [**commit**](cmdqueryname=commit) | - |