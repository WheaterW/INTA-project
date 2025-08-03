peer log-change (BGP multi-instance view) (group)
=================================================

peer log-change (BGP multi-instance view) (group)

Function
--------



The **peer log-change** command enables a BGP device to log the session status and events of a specified group.

The **undo peer log-change** command cancels the configuration.



By default, a BGP device is enabled to log the session status and events of a specified peer group.


Format
------

**peer** *group-name* **log-change**

**undo peer** *group-name* **log-change**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **peer log-change** command can be used to enable a device to log the session status and events of a specified peer group, facilitating service management.




Example
-------

# Configure a BGP device to log the session status and events of a peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] group test
[*HUAWEI-bgp-instance-a] peer test log-change

```