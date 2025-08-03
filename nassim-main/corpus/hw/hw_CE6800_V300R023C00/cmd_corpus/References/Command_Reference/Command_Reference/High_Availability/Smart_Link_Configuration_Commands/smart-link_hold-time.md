smart-link hold-time
====================

smart-link hold-time

Function
--------



The **smart-link hold-time** command sets the delay in reporting the Up/Down event of an interface in a Smart Link group.

The **undo smart-link hold-time** command deletes the delay in reporting the Up/Down event of an interface in a Smart Link group.



By default, the delay for link switchovers in a Smart Link group is 0. That is, when an interface goes Up or Down, a Smart Link group performs a link switchover immediately.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**smart-link hold-time** *hold-time*

**undo smart-link hold-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hold-time* | Specifies a delay for link switchovers in a Smart Link group. | The value is an integer ranging from 1 to 60, in 100 ms. |



Views
-----

Smart Link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a Smart Link group performs link switchovers due to intermittent link disconnections, packet forwarding and system performance will be affected. To address this problem, run the smart-link hold-time command to configure a delay for link switchovers in the Smart Link group. If you configure a delay for link switchovers in a Smart Link group, the Smart Link group will not perform link switchovers whenever the interface status changes in the Smart Link group until the delay expires. This configuration suppresses link switchovers due to intermittent link disconnections.

**Prerequisites**

A Smart Link group has been created using the **smart-link group** command.


Example
-------

# Configure the delay for link switchovers in Smart Link group 1 as 300 ms.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] smart-link hold-time 3

```