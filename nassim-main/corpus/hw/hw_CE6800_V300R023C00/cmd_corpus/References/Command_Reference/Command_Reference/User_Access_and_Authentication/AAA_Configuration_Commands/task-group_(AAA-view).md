task-group (AAA-view)
=====================

task-group (AAA-view)

Function
--------



The **task-group** command creates a task group or displays the task group view.

The **undo task-group** command deletes a task group.



By default, the device has four task groups: manage-tg, system-tg, monitor-tg and visit-tg.


Format
------

**task-group** *task-group-name*

**undo task-group** *task-group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *task-group-name* | Specifies the name of a task group. | The value is a string of 1 to 32 case-insensitive characters, including letters, digits, and underscores (\_). The scheme name cannot contain the following characters: backward slash (\), forward slash (/), colon (:), asterisk (\*), question mark (?), quotation mark ("), vertical bar (|), less-than sign (<), and greater-than sign (>). |



Views
-----

AAA view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When the default task groups do not meet user requirements, you can create a task group and assign tasks and rights to the task group to flexibly control user rights.

**Follow-up Procedure**

Allocate required rights (tasks) to the new task group.

**Precautions**

After the **task-group** command is run to create a task group, the following configurations are automatically created in the task group:task interface-mgr read read-writetask config read write read-writetask vlan read write read-writetask shell read write read-writetask cli readtask system-view read write read-writeThe default task group cannot be deleted.


Example
-------

# Create a task group.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] task-group ospf_tg

```