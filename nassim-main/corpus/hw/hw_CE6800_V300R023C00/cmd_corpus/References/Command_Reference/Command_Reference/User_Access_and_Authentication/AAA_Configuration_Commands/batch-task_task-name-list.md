batch-task task-name-list
=========================

batch-task task-name-list

Function
--------



The **batch-task task-name-list** command configures permissions for tasks in batches.



By default, task permissions are not configured in batches.


Format
------

**batch-task** { **read** | **read-write** | **debug** } \* **task-name-list** *task-name* &<1-20>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **read** | Grants the read permission to users. | - |
| **read-write** | Grants the read-write permission to users. | - |
| **debug** | Grants the diagnosis permission to users. | - |
| *task-name* | Indicates the name of a task group. | The value must be set according to the device configuration. |



Views
-----

Task group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

For security purposes, different users are granted with different permissions. To configure permissions for a task group, run the task command in the task group view so that the users associated with that task group can have the permissions specified for the task group. The **batch-task** command configures task permissions in batches, facilitating configurations.


Example
-------

# Configure the read permission for the interface-mgr, aaa, and config tasks in batches.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] task-group 1
[*HUAWEI-aaa-task-group-1] batch-task read task-name-list interface-mgr aaa config

```