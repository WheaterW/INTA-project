admin-user privilege level
==========================

admin-user privilege level

Function
--------

The **admin-user privilege level** command configures a user as an administrator to log in to the device and sets the user level.

The **undo admin-user privilege level** command cancels the default user level.

By default, the user level is not specified.



Format
------

**admin-user privilege level** *level*

**undo admin-user privilege level**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *level* | Specifies a user level.  A larger value indicates a higher user level. After logging in to the device, a user can run only the commands of the same level or lower levels. | The value is an integer that ranges from 0 to 3. |




Views
-----

Service scheme view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

A device manages users and commands by privilege level to limit user access permissions. After a user logs in to a device, the user can only use commands at the user's privilege level or lower. The command privilege level ranges from 0 to 3, and the user privilege level ranges from 0 to 3. The mapping between user privilege levels and command privilege levels is as follows:

* If the privilege level of a user is 0, the user can use the commands at the visit level (0), such as network diagnostic tool commands (ping and tracert), commands for accessing external devices from the local device (through the Telnet client), and some **display** commands.
* If the privilege level of a user is 1, the user can use the commands at the visit level (0) and monitoring level (1), such as the system maintenance commands and some **display** commands.
* If the privilege level of a user is 2, the user can use the commands at the visit level (0), monitoring level (1), and configuration level (2), including service configuration commands (routing commands and commands at each network layer), which are used to provide network services for users.
* If the privilege level of a user is 3, the user can use the commands at the visit level (0), monitoring level (1), configuration level (2), and management level (3), including the commands that are used for basic system operations, including file system, FTP, TFTP download, command privilege level configuration, and debugging.

The user privilege level can be locally configured or authorized by a server. The priorities of user privilege levels vary according to different authentication scenarios:

* If local authentication is used, the following administrator privilege levels can be configured, which are listed in descending order of priority:
  1. Local user privilege level configured using the **local-user privilege level** command
  2. Administrator privilege level configured using the **admin-user privilege level** command in the service scheme view
  3. User privilege level configured using the **user privilege** command in the VTY user interface view
* If remote authentication is used, the following administrator privilege levels can be configured, which are listed in descending order of priority. The privilege level authorized by the RADIUS or HWTACACS server has the highest priority.
  1. User privilege level authorized by the server after the authentication succeeds
  2. Administrator privilege level configured using the **admin-user privilege level** command in the service scheme view
  3. User privilege level configured using the **user privilege** command in the VTY user interface view
* If both remote authentication and local authentication are configured for a user and remote authentication takes precedence over local authentication: The administrator privilege level is the one used during remote authentication. If the remote server does not respond, local authentication is used. In this case, the administrator privilege level is the local user privilege level configured using the **local-user privilege level** command.

**Follow-up Procedure**

Run the **display service-scheme** command to view the user level in a service scheme.



Example
-------

# Configure a user as an administrator to log in to the device and set the administrator level to 3.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] service-scheme svcscheme1
[*HUAWEI-aaa-service-svcscheme1] admin-user privilege level 3

```