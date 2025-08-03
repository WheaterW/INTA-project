link-group
==========

link-group

Function
--------



The **link-group** command creates a link group and enters the link group view.

The **undo link-group** command deletes a link group and unbinds interfaces from the link group.



By default, no link group is created.


Format
------

**link-group** *group-name*

**undo link-group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a link group. | The value is a string of 1 to 32 case-sensitive characters. When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In an IS-IS dual-homing access scenario, when the traffic rate exceeds the bandwidth of a link, additional links are needed to carry the traffic. If one of the links fails and the bandwidth of the other links is not sufficient enough to carry the traffic, traffic will get lost. To prevent this problem, run the **link-group** command to bundle multiple links into a link group and run the **cost-offset** command to configure a link cost offset to be added to the link cost of the member links when the number of available member links falls below a specified number. After the link cost is adjusted, the traffic forwarding path is changed, preventing traffic loss.

**Prerequisites**

An IS-IS process has been enabled using the **isis** command.

**Precautions**

If you run the undo **link-group** command, the created link group and the configurations of the interfaces associated with the link group are deleted. Therefore, exercise caution when running this command.Perform the following operations for the link group feature to take effect:

* Run the **link-group** command in the IS-IS view to create a link group.
* Run the **cost-offset** command to set the automatically adjusted cost.
* Run the **isis link-group** or **isis ipv6 link-group** command in the interface view to bind the interface to the link group.

Example
-------

# Create an IS-IS link group named link-a.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] link-group link-a

```