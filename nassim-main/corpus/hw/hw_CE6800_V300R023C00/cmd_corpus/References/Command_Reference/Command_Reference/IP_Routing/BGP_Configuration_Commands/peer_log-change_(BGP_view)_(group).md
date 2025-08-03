peer log-change (BGP view) (group)
==================================

peer log-change (BGP view) (group)

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
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **peer log-change** command can be used to enable a device to log the session status and events of a specified peer group, facilitating service management.


Example
-------

# Configure a BGP device to log the session status and events of peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test log-change

```