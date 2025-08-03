task
====

task

Function
--------



The **task** command adds a task to a task group.

The **undo task** command deletes a task from a task group.



By default, after a task group is created, some basic task permissions are enabled.

· interface-mgr task: has the read and write permissions. Users with these permissions can perform basic interface operations.

· config task: has the read and write permissions. Users with these permissions can enter the system view to perform configurations.

· vlan task: has the read and write permissions. Users with these permissions can perform basic VLAN-related operations.

· shell task: has the read and write permissions. Users with these permissions can perform basic access, such as Telnet access.

· cli task: has the read permission. Users with this permission can perform basic configurations, such as running display commands.




Format
------

**task** *task-name* { **read** | **read-write** | **debug** } \*

**undo task** *task-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *task-name* | Indicates the name of a task group. | The value must be set according to the device configuration. |
| **read** | Grants the read permission to users. | - |
| **read-write** | Grants the read-write permission to users. | - |
| **debug** | Grants the diagnosis permission to users. | - |



Views
-----

Task group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

For security purposes, different users are granted with different permissions. You can run the **task** command to configure the permission for a certain task group. Then the users associated with that task group can have the permission configured for the task.


Example
-------

# Add the task ospf to the task group ospf\_tg. Then the task has the read and read-write permissions of the task group but does not have the debug permission.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] task-group ospf_tg
[*HUAWEI-aaa-task-group-ospf_tg] task ospf read read-write

```