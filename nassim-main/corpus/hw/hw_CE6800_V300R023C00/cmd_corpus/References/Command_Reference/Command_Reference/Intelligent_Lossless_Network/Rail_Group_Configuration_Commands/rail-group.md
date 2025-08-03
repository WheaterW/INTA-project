rail-group
==========

rail-group

Function
--------



The **rail-group** command creates a Rail Group port group and displays the Rail Group port group view. If a Rail Group port group already exists, the port group view is displayed.

The **undo rail-group** command deletes a Rail Group port group.



By default, no Rail Group port group exists in the system.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rail-group** *group-name*

**undo rail-group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a Rail Group port group. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Rail Group function defines a Rail Group port group. For a leaf node, you can add all its physical interfaces connected to servers to the same Rail Group port group. For a spine node, you can add all its physical interfaces connected to the same leaf node to the same Rail Group port group.

**Follow-up Procedure**

You need to run the group-member interface (Rail Group port group view) command to add a specified interface to a Rail Group port group.

**Precautions**

A maximum of 512 Rail Group port groups can be created in the system.


Example
-------

# Create a Rail Group port group named Leaf1.
```
<HUAWEI> system-view
[~HUAWEI] rail-group Leaf1
[*HUAWEI-rail-group-Leaf1]

```