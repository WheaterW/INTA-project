Setting Command Privilege Levels
================================

Setting Command Privilege Levels

#### Context

The system manages commands based on command privilege levels. Each command to be run in a command view has its privilege level. The device administrator can change the command privilege level as required, enabling lower-level users to run some high-level commands. The device administrator can also increase the command privilege level to improve device security.

* A device manages users by level, and maintains the relationship between user privilege levels and command privilege levels in order to limit user access permissions. After a user logs in to a device, the user can only use commands at the user's privilege level and below. By default, the values of both command privilege levels and user privilege levels range from 0 to 3. [Table 1](#EN-US_TASK_0000001513050518__tab_dc_vrp_cfg_00902901) describes the relationship between user privilege levels and command privilege levels.
  
  **Table 1** Relationship between command privilege levels and user privilege levels
  | User Privilege Level | Command Privilege Level | Description |
  | --- | --- | --- |
  | 0 | Visit level (0) | Commands at this privilege level include network diagnosis tool commands (such as ping and tracert), commands for accessing external devices from the local device (such as Telnet), and some display commands. |
  | 1 | Visit level (0) and monitoring level (1) | Commands at this level are used for system maintenance, including display commands. NOTE:  Not all display commands are at this level. For example, the **[**display current-configuration**](cmdqueryname=display+current-configuration)** and **[**display saved-configuration configuration**](cmdqueryname=display+saved-configuration+configuration)** commands are at level 3. For details about command privilege levels, see the *Command Reference*. |
  | 2 | Visit level (0), monitoring level (1), and configuration level (2) | Commands at this privilege level are used for service configurations to provide network services, including routing, Layer 2, and Layer 3 commands. |
  | 3 | Visit level (0), monitoring level (1), configuration level (2), and management level (3) | Commands at this privilege level are used for basic system operations, including file system, FTP, TFTP download, command privilege level configuration, and debugging. |

![](public_sys-resources/notice_3.0-en-us.png) 

To prevent security risks to devices, you are not advised to change the default command privilege level.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the command privilege level in the specified view.
   
   
   ```
   [command-privilege level](cmdqueryname=command-privilege+level) level view view-name command-key
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```