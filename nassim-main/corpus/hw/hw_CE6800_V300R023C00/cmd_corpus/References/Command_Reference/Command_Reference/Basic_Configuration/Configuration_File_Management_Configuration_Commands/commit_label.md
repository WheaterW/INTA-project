commit label
============

commit label

Function
--------



The **commit label** command generates a user label for a configuration rollback point.




Format
------

**commit label** *label* [ **description** *description* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *label* | Specifies a user label for a configuration rollback point. | The value is a string of 1 to 256 case-sensitive characters. It can be any visible ASCII character except for the space. However, the string can contain spaces if it is enclosed with double quotation marks (" "). The string cannot start with a digit or be a hyphen (-). |
| **description** *description* | Specifies information about a configuration rollback point. | The value is a string of 1 to 60 case-sensitive ASCII characters, spaces supported. |



Views
-----

All views except the user view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To add a description for the committed configuration, run the **commit label description** command. The description provides guidance and help for configuration rollback. All the generated description information can be viewed using the **display configuration commit list verbose** command.




Example
-------

# Modify a configuration and commit the modified configuration.
```
<HUAWEI> system-view
[~HUAWEI] sysname DeviceA
[*HUAWEI] commit label a123
[~DeviceA]

```