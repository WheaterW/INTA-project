user-group
==========

user-group

Function
--------

The **user-group** command creates a user group or displays the user group view.

The **undo user-group** command deletes a user group.

By default, the device has four built-in user groups: manage-ug, system-ug, monitor-ug, and visit-ug.



Format
------

**user-group** *group-name*

**undo user-group** *group-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Name of a user group. | The value is a string of 1 to 32 case-insensitive characters. Spaces and Chinese characters are not supported. The value cannot contain the following characters: \ / : < > | \* " ?. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

A user group is a group of users. Users in the same user group have the same rights. A user group consists of task groups and users need to be added to the user group. The rights of a user are controlled within the rights of the user group. The system predefines four user groups: manage-ug, system-ug, monitor-ug, and visit-ug. Predefined user groups can only be used but cannot be modified. If a user is also configured with a level(including the local-user privilege level and admin-user privilege level in the service scheme), level authorization is preferred.



Example
-------

# Create a user group named test1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] user-group test1

```