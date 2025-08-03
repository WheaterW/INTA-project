task-group
==========

task-group

Function
--------

The **task-group** command binds a specified task group to a user group and grants the corresponding permission to the task group.

The **undo task-group** command unbinds the current user group from a specified task group and deletes the permission configuration.

By default, a new user group is not bound to any task group.



Format
------

**task-group** *task-group-name* { { **read** | **read-write** } | **debug** } \*

**undo task-group** *task-group-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *task-group-name* | Indicates the name of a task group. | The value is a string of 1 to 32 case-insensitive characters without spaces. |
| **read** | Indicates the read permission. | - |
| **read-write** | Indicates the read-write permission. | - |
| **debug** | Indicates the debug permission. | - |




Views
-----

User group view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

A task group is a group of tasks. A task can be assigned one or more of the following permissions when being added to a task group: read, write-read, and debug.

A task is a group of commands. Generally, commands of a feature or function belong to a task. To implement refined permission management, a feature can have multiple tasks. Tasks are pre-configured and cannot be added, modified, or deleted.

Example
-------

# Obtain the read permission on the task group common-tg.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] user-group test1
[*HUAWEI-aaa-user-group-test1] task-group common-tg read

```