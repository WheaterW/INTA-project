clear configuration commit label
================================

clear configuration commit label

Function
--------



The **clear configuration commit label** command deletes a configuration rollback point with a specified user label.




Format
------

**clear configuration commit label** *label-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *label-name* | Specifies a user label for a configuration rollback point. | The value is a string of 1 to 256 case-sensitive characters. It can be any visible ASCII character except for the space. However, the string can contain spaces if it is enclosed with double quotation marks (" "). The string cannot start with a digit or be a hyphen (-).  The value of this parameter must be an existing configuration rollback point on the device. Otherwise, the command cannot be executed. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To delete a useless configuration rollback point with a specified label, run the clear configuration commit command. The system can generate a maximum of 20 configuration rollback points with a specified label, 10 scheduled configuration rollback points, and 1 historical scheduled configuration rollback point. If a configuration rollback point is no longer used, run this command to delete the configuration rollback point to reduce the amount of information cached in the system.

**Precautions**



After a configuration rollback point is deleted, system configurations cannot be rolled back to what they were at this configuration rollback point by running rollback commands.Run the **display configuration commit list** and **display configuration changes** commands to display information about the configuration rollback point. Checking the command output helps prevent misoperations.




Example
-------

# Delete the configuration rollback point with the label named new\_label.
```
<HUAWEI> clear configuration commit label new_label
Warning: The current operation will delete the rollback checkpoint. Continue? [Y/N]: y

```