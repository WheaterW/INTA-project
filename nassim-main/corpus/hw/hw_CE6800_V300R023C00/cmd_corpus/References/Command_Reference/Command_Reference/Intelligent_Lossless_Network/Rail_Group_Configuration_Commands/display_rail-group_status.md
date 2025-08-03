display rail-group status
=========================

display rail-group status

Function
--------



The **display rail-group status** command displays the configuration and status of a rail group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display rail-group status** [ **group-name** *group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **group-name** *group-name* | Specifies the name of a rail group port-group. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the configuration and status of a rail group.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the Rail Group configuration and status.
```
<HUAWEI> system-view
[~HUAWEI] display rail-group status
Global rail-group configuration: Enable
-------------------------------------------
GroupName   Index       Interface          
-------------------------------------------
Leaf1           0       100GE1/0/1         
                1       100GE1/0/2         
Leaf2           0       100GE1/0/3         
                1       100GE1/0/4         
-------------------------------------------

```

**Table 1** Description of the **display rail-group status** command output
| Item | Description |
| --- | --- |
| Global rail-group configuration | Configuration and status of the global rail group function. |
| GroupName | Name of the rail group port-group. |
| Index | Index. |
| Interface | Name of an interface. |