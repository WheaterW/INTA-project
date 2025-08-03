CLI Overview
============

The command line interface (CLI) is a common tool for running commands. You can run CLI commands to configure and manage a Router.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

When a user runs a command that requires a password entry, some passwords are displayed in plaintext on a screen. To prevent a password leak, clear the screen promptly.


#### Command Line Interface

The command line interface (CLI) is an interface through which you can interact with a Router. The system provides a series of commands that allow you to configure and manage the Router.

The CLI is a traditional configuration tool, which is available on most data communication products. However, with the wider application of data communication products worldwide, customers require a more available, flexible, and friendly CLI.

After the device is switched to the UP, the cp-config view is automatically created. In the view, the name of the template that the CP delivers to the UP is stored, and the data in the template cannot be modified locally.

The CLI has the following characteristics:

* Supports local configurations through the console port.
* Supports local or remote configurations over Telnet or Secure Shell (SSH).
* Provides the user interface view and supports personal configuration and management for various terminal users.
* Supports the command-based hierarchical protection mode in which users of different levels can run only the commands of the corresponding levels.
* Allows users to type in a question mark (?) to obtain online help.
* Provides network testing commands, such as the [**tracert**](cmdqueryname=tracert) and [**ping**](cmdqueryname=ping) commands, for quickly diagnosing network connectivity.
* Provides various detailed debugging information to help diagnose network faults.
* Allows users to log in to and manage other Routers using the [**telnet**](cmdqueryname=telnet) command.
* Provides the FTP service to allow users to upload and download files.
* Provides the function to run a historical command.
* Provides multiple intelligent command resolution methods through the command line interpreter, such as partial match and context-sensitive, which facilitates users' command entry.