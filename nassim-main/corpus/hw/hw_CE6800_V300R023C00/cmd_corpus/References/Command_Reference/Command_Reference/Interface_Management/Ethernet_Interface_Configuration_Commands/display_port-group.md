display port-group
==================

display port-group

Function
--------



The **display port-group** command displays information about a permanent interface group.




Format
------

**display port-group** [ *port-group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-group-name* | Displays information about a specified permanent interface group. | The value is a string of 1 to 32 characters without spaces.  When quotation marks are used around the string, spaces are allowed in the string.  The specified name of a permanent interface group is case insensitive. For example, ABC and abc specify the same interface group. After ABC is specified for a permanent interface group, the information about the interface group named ABC will be displayed if you check the information about an interface group named abc. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **display port-group** command to view information about a specified permanent interface group or all permanent interface groups that have been created using the **port-group** command. The information includes the name of each permanent interface group, number of member interfaces in each permanent interface group, and names of the interfaces in each permanent interface group. The information helps view interface configurations or analyze problems.



**Precautions**



The **display port-group** command does not display information about a temporary interface group that has been created using the **port-group group-member** command.If no parameter is specified, the **display port-group** command displays only the total number of permanent interface groups that have been created in the system and their names.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the total number of permanent interface groups that have been created in the system and their names.
```
<HUAWEI> display port-group
 Total port-groups configured : 2
   port-group1
   port-group2

```

**Table 1** Description of the **display port-group** command output
| Item | Description |
| --- | --- |
| Total port-groups configured | Total number of permanent interface groups that have been created in the system and their names. |