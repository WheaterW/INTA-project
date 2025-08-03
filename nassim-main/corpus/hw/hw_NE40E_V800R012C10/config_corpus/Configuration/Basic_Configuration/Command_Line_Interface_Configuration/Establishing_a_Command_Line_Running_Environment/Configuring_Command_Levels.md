Configuring Command Levels
==========================

Configuring Command Levels

#### Context

If you do not change a command level separately, all originally registered commands automatically change based on the following rules after the command level is updated:

* The commands of Level 0 and Level 1 remain unchanged.
* The commands of Level 2 are updated to Level 10 and the commands of Level 3 are updated to Level 15.
* No commands exist in Level 2 to Level 9 and Level 11 to Level 14. You can change the commands to these levels separately to refine rights management.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Do not change the default level of a command. If the default level of a command is changed, some users may be unable to use the command any longer.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**command-privilege level rearrange**](cmdqueryname=command-privilege+level+rearrange)
   
   
   
   The command levels are updated in batches.
3. Run [**command-privilege level**](cmdqueryname=command-privilege+level) *level* **view** *view-name* *command-key*
   
   
   
   The level of a command is set in a specified view.
   
   
   
   All commands have default command views and levels. Generally, you do not need to configure them.
   
   The command lines are classified into visit level (0), monitoring level (1), configuration level (2), and management level (3) in an ascending order.
   
   **Table 1** Command level description
   | User Class (0 to 3) | User Class (0 to 15) | Command Level | Type Name | Description |
   | --- | --- | --- | --- | --- |
   | 0 | 0 | 0 | Visit level | Commands of this level include **ping**, **tracert**, and **Telnet** (commands used to access a remote device). |
   | 1 | 1 to 9 | 0, 1 | Monitoring level | Commands of this level are used for system maintenance, such as display commands. NOTE:  Not all display commands are of the monitoring level. For example, the [**display current-configuration**](cmdqueryname=display+current-configuration) commands for configuration file management are of management level (3). |
   | 2 | 10 to 14 | 0, 1, 2 | Configuration level | Service configuration commands are of this level. |
   | 3 | 15 | 0, 1, 2, 3 | Management level | Commands of the management level are used for system basic operation to support services, including file system, FTP, Trivial File Transfer Protocol (TFTP), and configuration file switching commands, slave board control commands, user management commands, command level configuration commands, **reboot** commands, and **debugging** commands. |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.