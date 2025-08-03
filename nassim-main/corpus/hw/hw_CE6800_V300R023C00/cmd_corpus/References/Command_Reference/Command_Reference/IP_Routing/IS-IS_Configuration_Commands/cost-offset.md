cost-offset
===========

cost-offset

Function
--------



The **cost-offset** command configures a link cost offset to be added to the link cost of the member links in a link group when the number of available member links falls below a specified number.

The **undo cost-offset** command restores the original link cost of the member links in a link group.



By default, when the number of member links in a link group is smaller than the specified number, IS-IS automatically increases the link cost by 1.


Format
------

**cost-offset** { *cost* | **max-reachable** | **maximum** }

**undo cost-offset**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost* | Specifies the link cost offset to be added to the link cost of the member links in a link group when the number of available member links falls below a specified number. | The value is an integer ranging from 1 to 16777213. The default value is 1. |
| **max-reachable** | Indicates that the maximum link cost of reachable routes (16777214) is used as the link cost of member links in a link group when the number of available member links in the link group falls below a specified number. | - |
| **maximum** | Indicates that 16777215 is used as the link cost of member links in a link group when the number of available member links in the link group falls below a specified number. After 16777215 is used as the link cost, the routes along the links are used to transmit TE information, not selected for traffic forwarding. | - |



Views
-----

IS-IS link-group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In an IS-IS dual-homing access scenario, if user traffic exceeds the link bandwidth, multiple links are required to forward user traffic. If one or more links fail and the total bandwidth of other links is less than the user traffic volume, some traffic is lost. To prevent this problem, run the **link-group** command to bind multiple links to a link group. When one or more links fail, the cost of all member links is adjusted. In this manner, traffic forwarding paths are changed, preventing traffic loss. cost-offset specifies the cost to be adjusted.

**Prerequisites**

A link group has been created using the **link-group** command.


Example
-------

# Increase the link cost by 100 when the number of available member links in the link group falls below a specified number.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] link-group link-a
[*HUAWEI-isis-link-group-link-a] cost-offset 100

```