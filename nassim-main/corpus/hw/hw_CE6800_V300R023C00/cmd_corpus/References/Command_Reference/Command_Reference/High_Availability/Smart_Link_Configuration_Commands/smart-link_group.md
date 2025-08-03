smart-link group
================

smart-link group

Function
--------



The **smart-link group** command creates a Smart Link group and displays the Smart Link group view. If a Smart Link group exists, the command displays the specified Smart Link group view.

The **undo smart-link group** command deletes a Smart Link group.



By default, no Smart Link group is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**smart-link group** *group-id*

**undo smart-link group** *group-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-id* | Specifies the ID of a Smart Link group. | The value is an integer ranging from 1 to 48. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Smart Link is a reliability mechanism that provides reliable and efficient link backup and a fast traffic switchover. Smart Link is used on dual-homing networks. Before configuring basic functions of Smart Link, run the smart-link group command to create a Smart Link group.

**Follow-up Procedure**

Perform the following steps to implement basic functions of Smart Link:

1. Configure the master and slave interfaces.
2. Enable the transmission of Flush packets.
3. Enable the Smart Link group.

**Precautions**

Do not delete a Smart Link group when it has member interfaces. You can run the **undo port** command to delete all member interfaces from the Smart Link group before deleting the group itself.


Example
-------

# Create Smart Link group 1.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1

```