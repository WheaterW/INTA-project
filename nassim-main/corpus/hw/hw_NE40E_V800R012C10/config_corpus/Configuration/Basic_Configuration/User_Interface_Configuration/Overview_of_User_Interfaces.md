Overview of User Interfaces
===========================

The system supports console and virtual type terminal (VTY) user interfaces.

You can configure, monitor, and maintain local or remote network devices only after configuring user interfaces, user management, and terminal services. User interfaces provide login venues, user management ensures login security, and terminal services provide login protocols. Routers support user login over console ports.

Each user interface has a user interface view. You can configure parameters in a user interface view to determine whether authentication is required for login users and specify levels for the users. This configuration implements uniform management of various user sessions.

The system supports the following user interfaces:

* Console user interface: manages and monitors users who log in through the console port.
  
  The type of the console interface is EIA/TIA-232 DCE.
* VTY user interface: manages and monitors users who log in using VTY.
  
  A VTY connection is set up when a user uses Telnet or SSH to log in to a router. A maximum of 21 users can log in to the router using VTY.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If a user logs in to a router in different login modes or at different times, the user may be allocated different user interfaces.


#### User Interface Numbering

When a user logs in to a router, the system allocates an idle user interface with the smallest number to the user based on the user's login mode. The login process is restricted by the configurations for the user interface.

User interfaces can be numbered in either of the following modes:

* Relative numbering
  
  This mode uniquely specifies a user interface or a group of user interfaces of the same type.
  
  The numbering format is user interface type + number, adhering to the following rules:
  
  + Console user interface numbering: CON 0.
  + VTY user interface numbering: The first VTY user interface is VTY 0, the second VTY user interface is VTY 1, and so on.
* Absolute numbering
  
  This mode uniquely specifies a user interface or a group of user interfaces. The number starts with 0, increasing by 1. Console user interfaces are numbered before VTY user interfaces.
  
  There are 1 console user interface and 21 VTY user interfaces. You can run the [**user-interface maximum-vty**](cmdqueryname=user-interface+maximum-vty) command in the system view to set the maximum number of VTY user interfaces.
  
  **Table 1** Absolute and relative numbers of user interfaces
  | User Interface | Description | Absolute Number | Relative Number |
  | --- | --- | --- | --- |
  | Console user interface | Manages and controls users who log in to the device using the console interface.  This user interface is supported only by the Admin-VS. | 0 | 0 |
  | TTY user interface  NOTE:  Currently, the system does not support the TTY user interface. | Manages and monitors users logging in through the asynchronized serial port. | 1â32 | The first one is TTY 0, the second one is TTY 1, and so forth.  Absolute numbers 1 to 32 correspond to relative numbers TTY 0 to TTY 31. |
  | VTY user interface | Manages and controls users who log in to the device using Telnet or SSH. | 34-54 | The first one is VTY 0, the second one is VTY 1, and so forth.  Absolute numbers 34 to 54 correspond to relative numbers VTY 0 to VTY 20. |

#### Authentication Modes for User Interfaces

After you configure a user authentication mode for a user interface, the system authenticates users before they access the user interface. The system supports the following authentication modes:

* Password authentication: Users must enter passwords for login.
* AAA authentication: Users must enter both user names and passwords for login. If either a user name or a password is incorrect, the login fails. AAA authentication is usually used for Telnet users.

#### User Levels for User Interfaces

You can manage login users based on their levels. The levels of commands that a user can use are determined by the user's level.

* If password authentication is configured, the levels of commands that a user can use depend on the level of the user interface through which the user logs in.
* If AAA authentication is configured, the levels of commands that a user can use depend on the local user level specified in the AAA configuration.

[Table 2](#EN-US_CONCEPT_0172359733__table1261713203819) describes the mapping between user levels and command levels.

**Table 2** Mapping between user levels and command levels
| User Level (0 to 3) | User Level (0 to 15) | Command Level | Permission | Description |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | Visit | Diagnostic commands, such as ping and tracert, and commands that are used to access a remote device such as a Telnet client. |
| 1 | 1-9 | 0, 1 | Monitoring | Commands of this level are used for system maintenance, including display commands. NOTE:  Not all display commands are of the monitoring level. For example, the [**display current-configuration**](cmdqueryname=display+current-configuration) command is of management level (3). For details about command levels, see *HUAWEI NE40E-M2 series Command Reference*. |
| 2 | 10 to 14 | 0, 1, and 2 | Configuration level | Service configuration commands |
| 3 | 15 | 0, 1, 2, and 3 | Management level | Commands of the management level are used for basic system operation to support services, including file system, FTP, TFTP, and configuration file switching commands, slave board control commands, user management commands, command level configuration commands, reboot commands, and debugging commands. |