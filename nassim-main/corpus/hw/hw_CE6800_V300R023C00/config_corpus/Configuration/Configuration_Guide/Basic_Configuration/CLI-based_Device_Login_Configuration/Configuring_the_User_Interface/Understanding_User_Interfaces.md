Understanding User Interfaces
=============================

The system supports console and virtual type terminal (VTY) user interfaces.

Each user interface has a corresponding view, which is a command-line interface (CLI). In this view, you can configure and manage all physical and logical interfaces that work in the asynchronous interaction mode to centrally manage user interfaces.

#### User Interfaces Supported by the Device

* Console (CON)
  
  The console port is a communication serial port.
  
  The serial port of a user terminal can be directly connected to the console port of the device for local access.
* VTY
  
  A VTY is a virtual port.
  
  When a Telnet or Secure Shell (SSH) connection is established between a terminal and a device, a VTY connection is established to connect to the device. A maximum of 21 users can log in to a device through the VTY.

#### Relationship Between a User and a User Interface

A user interface is not exclusive to a specific user. User interfaces are used to manage and monitor users who have logged in to the device using a specific method. Although a user interface may be used by only one user at a time, the user interface is not specific to the user.

When a user logs in, the system allocates the idle user interface with the smallest number to the user based on the user's login mode. The login process is restricted by the configuration in the user interface view. For example, when user A logs in through CON 0, the login process depends on the configuration in the CON 0 user interface view; when user A logs in through VTY 1, the login process depends on the configuration in the VTY 1 user interface view. If a user logs in to a device using different modes or at different times, the user may be allocated different user interfaces.


#### User Interface Numbering

When a user logs in, the system allocates the idle user interface with the smallest number to the user based on the user's login mode. User interfaces are numbered in either of the following methods:

* Relative numbering
  
  The numbering format is *User interface type* + *Number*.
  
  This method uniquely specifies a user interface or a group of user interfaces of the same type. Relative numbering must comply with the following rules:
  
  + Console user interface numbering: CON 0
  + VTY user interface numbering: The first VTY user interface is VTY 0, the second VTY user interface is VTY 1, and so on.
* Absolute numbering
  
  This method uniquely specifies a user interface or a group of user interfaces. You can run the [**display user-interface**](cmdqueryname=display+user-interface) command without specifying parameters to view user interfaces and their absolute numbers supported by the current device.
  
  Only one console user interface and 21 VTY user interfaces are supported. You can run the [**user-interface maximum-vty**](cmdqueryname=user-interface+maximum-vty) command in the system view to set the maximum number of available VTY user interfaces.
  
  [Table 1](#EN-US_CONCEPT_0000001513053078__tab_dc_cfg_ui_000201) lists the default absolute and relative numbers of the console and VTY user interfaces.

**Table 1** Absolute and relative numbers of user interfaces
| User Interface | Description | Absolute Number | Relative Number |
| --- | --- | --- | --- |
| Console user interface | Manages and controls users who log in to a device using the console port. | 0â19 | 0 |
| VTY user interface | Manages and controls users who log in to the device using Telnet or STelnet. | 34â54 | The first VTY user interface is VTY 0, the second VTY user interface is VTY 1, and so on. By default, VTY 0 to VTY 4 are available.  Absolute numbers 34 to 54 correspond to relative numbers VTY 0 to VTY 20, respectively. |



#### Authentication Modes for User Interfaces

After a user authentication mode is configured, the device authenticates users who want to log in using the configured authentication mode.

The following user authentication modes are available:

* Password authentication: A user is authenticated by password only.
* AAA authentication: A user is authenticated by user name and password. This mode is typically used to authenticate Telnet users.

#### User Privilege Levels for User Interfaces

You can manage login users based on their privilege levels. The privilege level of commands available to a user depends on the user privilege level.

* If password authentication is configured, the privilege level of commands that a user can use depends on the privilege level of the user interface through which the user logs in.
* If AAA authentication is configured, the privilege level of commands that a user can use depends on the privilege level of the local user specified in the AAA configuration.