Configuring Task Authorization
==============================

Compared with level authorization, task authorization supports the customization of the user group and task group according to the application scenario. Therefore, task authorization provides a more flexible right control granularity.

#### Context

Configuring task authorization involves the following configurations:

* [Adding tasks to the task group](#EN-US_TASK_0172371822__dc_vrp_aaa_cfg_101201)
* [Adding task groups to the user group](#EN-US_TASK_0172371822__dc_vrp_aaa_cfg_101202)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**authorization-scheme**](cmdqueryname=authorization-scheme) *authorization-scheme-name*
   
   
   
   The authorization scheme view is displayed.
4. Run [**authorization-cmd**](cmdqueryname=authorization-cmd)[ *privilege-level* ] *mode1* [ *mode2* ]
   
   
   
   The level authorization mode is configured.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   The AAA view is displayed.
6. Run [**task-group**](cmdqueryname=task-group) *task-group-name*
   
   
   
   The task group is created, and the task group view is displayed.
7. Run one of the following commands to set task permissions.
   * Run the [**task**](cmdqueryname=task) *task-name* { **read** | **write** | **execute** | **debug** } \* command to set permissions for a specific task.
   * Run the [**batch-task**](cmdqueryname=batch-task) { **read** | **write** | **execute** | **debug** } \* **task-name-list** { *task-name* &<1-20> } command to set permissions for tasks in batches.
   * Run the [**task-all**](cmdqueryname=task-all) { **read** | **write** | **execute** | **debug** } \* command to set permissions for all tasks in batches.
8. (Optional) Run [**rule command**](cmdqueryname=rule+command) *rule-name* **permit** **view** *view-name* **expression** *command-string*
   
   
   
   The operation is allowed to be implemented on a specific command.
   
   This command applies to a single command. Compared with the [**task**](cmdqueryname=task) command, this command is more granular and can be used for a single command or a batch of commands with the same prefix.
   
   In the same task group,
   the priority of the **rule command** command is higher
   than that of the [**task**](cmdqueryname=task) command. When the **rule command** command
   configuration conflicts with the [**task**](cmdqueryname=task) command configuration, the **rule command** command configuration takes effect preferentially.
9. (Optional) Run [**include task-group**](cmdqueryname=include+task-group) *task-group-name*
   
   
   
   A specific task group is added to the current task group.
   
   To allow the authority
   of the current task group to contain the authority of another task
   group or the current task group to inherit the authority of an existing
   task group, run the **include task-group** command.
   
   If the authority of the contained task group changes,
   the authority of the current task group will change.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    The AAA view is displayed.
11. Run [**user-group**](cmdqueryname=user-group) *user-group-name*
    
    
    
    The user group is created, and the user group view is displayed.
12. Run [**task-group**](cmdqueryname=task-group) *task-group-name*
    
    
    
    The specified task group is added to the current user group.
13. (Optional) Run [**include user-group**](cmdqueryname=include+user-group) *user-group-name*
    
    
    
    A specific user group is added to the current user group.
    
    To allow the authority
    of the current user group to contain the authority of another user
    group or the current user group to inherit the authority of an existing
    user group, run the **include user-group** command.
    
    The authority of a user group is determined by that of
    the user group it contains. If the authority of the contained user
    group changes, the authority of the current user group will change.
14. (Optional) Run [**rule command**](cmdqueryname=rule+command) *rule-name* { **permit** | **deny** } **view** *view-name* **expression** *command-string*
    
    
    
    The operation is allowed to be implemented on a specific command.
    
    This command applies to a single command.
    
    The priorities of rules are displayed in descending order
    of rules configured in the user group view (including the rules inherited
    from other user groups using the [**include user-group**](cmdqueryname=include+user-group) command), rules configured in the task group view ([**rule command**](cmdqueryname=rule+command)), and tasks configured in the task group ([**task**](cmdqueryname=task)).
    
    If the rules configured in a user
    group conflict with the rules inherited from other user groups using
    the [**include
    user-group**](cmdqueryname=include+user-group) command, the rules configured in the user
    group take effect preferentially.
15. Run [**quit**](cmdqueryname=quit)
    
    
    
    The AAA view is displayed.
16. Run **local-user** *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
    
    
    
    A local user is created, and the password of the user is configured.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
17. Run [**local-user**](cmdqueryname=local-user) *user-name* **user-group** *user-group-name*
    
    
    
    The local user is added to the specified user group.
18. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.