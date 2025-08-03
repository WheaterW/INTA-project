display port-isolate group
==========================

display port-isolate group

Function
--------



The **display port-isolate group** command displays configurations of interface isolation groups.




Format
------

**display port-isolate group** { *group-id* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays configurations of all isolation groups. | - |
| **group** *group-id* | Displays configurations of a specified interface isolation group. | The value is an integer ranging from 1 to 64. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



After creating interface isolation groups using the **port-isolate enable** command, run the **display port-isolate group** command to view configurations of the interface isolation groups, which facilitates fault location and analysis.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configurations of all interface isolation groups.
```
<HUAWEI> display port-isolate group all
The ports in isolate group 3:
100GE1/0/1 100GE1/0/2

```

**Table 1** Description of the **display port-isolate group** command output
| Item | Description |
| --- | --- |
| The ports in isolate group | Interfaces in an interface isolation group. |