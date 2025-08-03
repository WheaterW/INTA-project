(Optional) Configuring Rights- and Domain-based Management
==========================================================

(Optional) Configuring Rights- and Domain-based Management

#### Context

**Basic Concepts**

Rights- and domain-based management provides specific management rights for various types of administrators.

* Rights-based management, also known as operation authorization, controls the operations that an administrator can perform on the device. Unauthorized operations cannot be performed.
* Domain-based management, also known as management authorization, controls the objects that an administrator can manage on the device. Unauthorized objects cannot be managed.

In contrast to the traditional rights management mode (user privilege level + command privilege level), rights- and domain-based management handles permissions and objects in a more refined and flexible manner.

**Implementation**

In [Figure 1](#EN-US_TASK_0000001563755973__fig196931322187), the device implements rights- and domain-based management as follows: You can configure a specific task group for a user group and assign the specified operation rights to that user group. The administrator assigned the user group can manage the specified commands only through the specified operation rights.

**Figure 1** Rights- and domain-based management mechanism  
![](figure/en-us_image_0000001563875729.png)

* Task: a group of commands. Generally, the commands for the same feature (or function) belong to the same task. To achieve refined rights management, multiple tasks can be assigned to a feature.
* Task group: a group of tasks. After a task group is assigned specific operation rights, the commands in the task group can only be used to perform the specified operations. The operation rights include debug, read-only, and read-write.
* User group: a group of users. Administrators who require the same rights can be added to the same user group. A task group and operations can be specified for a user group in order to assign operation rights to that user group.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Assign a task group and operation rights to the user group.
   1. Create a task group or enter the task group view.
      
      
      ```
      [task-group](cmdqueryname=task-group) task-group-name
      ```
      
      By default, the device has four task groups: **manage-tg**, **system-tg**, **monitor-tg** and **visit-tg**. When the rights of the default task group cannot meet your requirements, you can create a task group and assign required rights to the new task group. In this manner, user rights can be controlled in a more flexible way.
   2. Adds a specified task to the current task group.
      
      
      ```
      [task](cmdqueryname=task) task-name { debug | read | read-write } *
      ```
      
      By default, no task is configured in a task group. The following table lists the default tasks and permissions after a task group is created.
      
      **Table 1** Default tasks and permissions
      | Task | Permission | Description |
      | --- | --- | --- |
      | interface-mgr | read and write | Users with this permission can perform basic interface operations. |
      | config | read and write | Users with this permission can enter the system view to perform configurations. |
      | vlan | read and write | Users with this permission can perform basic VLAN configurations. |
      | shell | read and write | Users with this permission can perform basic access operations, such as Telnet access. |
      | cli | read | Users with this permission can perform basic configurations, such as using display commands. |
      | system-view | read and write | Users with this permission can enter the system view to perform configurations. |
   3. (Optional) Set task permissions in batches.
      
      
      ```
      [batch-task](cmdqueryname=batch-task) { debug | read | read-write } * [task-name-list](cmdqueryname=task-name-list) task-name &<1-20>
      ```
      
      For security purposes, different users are assigned different permissions. To configure permissions for a task group, run the **task** command to configure permissions for the task group. To configure permissions for tasks in batches, run the **batch-task** command.
   4. (Optional) Combine the tasks and permissions of a task group to a specific task group.
      
      
      ```
      [include task-group](cmdqueryname=include+task-group) task-group-name
      ```
      
      If the tasks and permissions of the current task group do not meet user requirements and the required tasks and permissions have been configured in another task group, you can combine the tasks and permissions of the other task group into the current task group to complete the configuration of the current task group. This command simplifies the configuration process and improves configuration efficiency.
      
      When the authorization information of the combined task group is modified, the authorization information of the current task group is also modified. The tasks and permissions of a maximum of one task group can be combined into another task group. To change the combination relationship, run the **undo include task-group** command to delete the existing configuration first.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      * The tasks and permissions of other task groups cannot be combined into the default task group.
      * A maximum of four task group levels are supported, that is, A(B(C(D))) is supported. This means that task group A contains task group B, task group B contains task group C, and task group C contains task group D.
      * If a task group (A) has been directly or indirectly contained by another task group (B), task group A cannot contain task group B. For example, A(B(A)) is not supported. To be specific, when task group B contains task group A, task group A cannot contain task group B. A(B(C(A))) is not supported either. This means that when task group B contains task group C and task group C contains task group A, task group A cannot contain task group B.
   5. Return to the AAA view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
4. Assign a task group and operation rights to the user group.
   1. Create a user group or enter the specified user group view.
      
      
      ```
      [user-group](cmdqueryname=user-group) group-name
      ```
      
      By default, the device has four built-in user groups named **manage-ug**, **system-ug**, **monitor-ug**, and **visit-ug**.
      
      When an administrator is assigned the user group **manage-ug**, **system-ug**, **monitor-ug**, or **visit-ug**, a specific privilege level is configured for the administrator. User groups **manage-ug**, **system-ug**, **monitor-ug**, and **visit-ug** correspond to privilege levels 3, 2, 1, and 0, respectively.
   2. Assign a task group and operation rights to the user group.
      
      
      ```
      [task-group](cmdqueryname=task-group) task-group-name { { read | read-write } | debug } *
      ```
      
      By default, a new user group is not bound to any task group.

#### Verifying the Configuration

* Run the **display user-group** *group-name* command to check information about the specified user group.
* Run the **display task-group** *group-name* command to check information about the specified task group.
* Run the [**display task**](cmdqueryname=display+task) command to check information about all tasks.

#### Follow-up Procedure

Local authentication, RADIUS server authentication, and HWTACACS server authentication support rights- and domain-based management by authorizing user groups to administrators. The following describes how to configure these authentication methods:

* Local authentication:
  
  Run the [**local-user**](cmdqueryname=local-user) *user-name* **user-group** *group-name* command in the AAA view to assign a user group to an administrator using local authentication.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  An administrator can be assigned a user group for rights- and domain-based management only when no privilege level is configured for the administrator using the **local-user** *user-name* **privilege level** *level* or **admin-user privilege level** *level* command.
* RADIUS server authentication:
  
  Use the RADIUS attribute Filter-Id on the RADIUS server to specify the name of the authorized user group.
* HWTACACS server authentication:
  
  Use the HWTACACS attribute user-group-name on the HWTACACS server to specify the name of the authorized user group.