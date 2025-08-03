include task-group
==================

include task-group

Function
--------



The **include task-group** command combines the tasks and permissions of another task group into the current task group.

The **undo include task-group** command deletes the combination relationship configured for the current task group.



By default, the authority of a task group does not contain the authority of another task group.


Format
------

**include task-group** *task-group-name*

**undo include task-group** *task-group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *task-group-name* | Specifies the name of a task group. | The value is a string of 1 to 32 case-insensitive characters, spaces not supported. |



Views
-----

Task group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the tasks and permissions of the current task group do not meet user requirements and the required tasks and permissions have been configured in another task group, you can merge the tasks and permissions of the other task group into the current task group to complete the configuration of the current task group. This command simplifies the configuration process and improves configuration efficiency.After you modify the authority information of the combined task group, the authority information of the current task group is also modified. A maximum of one task group can be combined into one task group. To change the combination relationship, run the **undo include task-group** command to delete the existing configuration first.

**Prerequisites**

The contained task group must have existed. To be specific, the contained task group must have been configured or is the default task group.

**Precautions**

* The default group cannot contain other groups.
* A maximum of four levels of task groups can be combined, that is, A(B(C(D))). In addition, a task group cannot be combined with other task groups that are indirectly combined with the task group. For example, A(B(A)) is not allowed.

Example
-------

# Configure the task group named group1 to contain the task group named tg1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] task-group tg1
[*HUAWEI-aaa-task-group-tg1] quit
[*HUAWEI-aaa] task-group group1
[*HUAWEI-aaa-task-group-group1] include task-group tg1

```