set priority 8021p
==================

set priority 8021p

Function
--------



The **set priority 8021p** command configures the 802.1p priority of packets.

The **undo set priority 8021p** command cancels the configuration.



By default, no 802.1p priority is configured of packets.


Format
------

**set priority 8021p** *8021p-value*

**undo set priority 8021p**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *8021p-value* | Specifies the priority of 802.1p packets. A larger value indicates a higher priority. | The value is an integer ranging from 0 to 7. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **set priority 8021p** command configures the 802.1p priority of packets (When there are two layers of VLAN, only the outer VLAN is effective).




Example
-------

# Set the 802.1p priority of packets to 7.
```
<HUAWEI> system-view
[~HUAWEI] set priority 8021p 7

```