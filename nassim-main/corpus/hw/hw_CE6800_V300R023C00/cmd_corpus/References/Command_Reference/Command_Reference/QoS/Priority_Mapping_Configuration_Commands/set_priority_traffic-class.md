set priority traffic-class
==========================

set priority traffic-class

Function
--------



The **set priority traffic-class** command configures the internal priority of protocol packets sent by the local device.

The **undo set priority traffic-class** command restores the default internal priority of protocol packets sent by the local device.



By default, the internal priority is not configured for protocol packets sent by the local device, and the local device sends all protocol packets based on their original internal priorities.


Format
------

**set priority traffic-class** *traffic-class-value*

**undo set priority traffic-class** [ *traffic-class-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *traffic-class-value* | Specifies the internal priority of protocol packets. | The value is an integer that ranges from 0 to 7. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A device processes packets based on their internal priorities. You can change the internal priority of protocol packets sent by the local device to preferentially process packets with a high internal priority on the local device.


Example
-------

# Set the internal priority of protocol packets sent by the local device to 6.
```
<HUAWEI> system-view
[~HUAWEI] set priority traffic-class 6

```