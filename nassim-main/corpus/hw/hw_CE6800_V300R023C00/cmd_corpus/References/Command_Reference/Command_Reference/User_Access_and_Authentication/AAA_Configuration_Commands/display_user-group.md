display user-group
==================

display user-group

Function
--------



The **display user-group** command displays user group information.




Format
------

**display user-group** [ *user-group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-group-name* | Indicates the user group name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

A user group is a group of users. Users in the same user group have the same rights. A user group consists of task groups and users need to be added to the user group. The rights of a user are controlled within the rights of the user group. The VRPv8 system predefines four user groups: manage-ug, system-ug, monitor-ug, and visit-ug, which are equivalent to predefined roles such as system-admin. Predefined user groups can only be used but cannot be modified. If a user is also configured with a level, level-based authorization is preferred.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the user group information.
```
<HUAWEI> display user-group
2021-02-24 15:53:48.104                                                                                                             
------------------------------------------------------                                                                              
User-group-name                          User-group-id                                                                              
------------------------------------------------------                                                                              
manage-ug                                            1                                                                              
system-ug                                            2                                                                              
monitor-ug                                           3                                                                              
visit-ug                                             4                                                                              
lvchen                                               5                                                                              
------------------------------------------------------                                                                              
Total 5

```

**Table 1** Description of the **display user-group** command output
| Item | Description |
| --- | --- |
| User-group-name | User group name. |