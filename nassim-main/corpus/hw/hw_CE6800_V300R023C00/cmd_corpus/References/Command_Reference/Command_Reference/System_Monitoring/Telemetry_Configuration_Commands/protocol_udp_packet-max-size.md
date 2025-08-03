protocol udp packet-max-size
============================

protocol udp packet-max-size

Function
--------



The **protocol udp packet-max-size** command sets the maximum size of telemetry packets sent through UDP.

The **undo protocol udp packet-max-size** command deletes the restriction on the maximum size of telemetry packets sent through UDP.



By default, the value is 0, indicating that the maximum size of a UDP packet is not limited.


Format
------

**protocol udp packet-max-size** *size*

**undo protocol udp packet-max-size** [ *size* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *size* | Specifies the maximum size of telemetry packets sent through UDP. | The value is 1472, in bytes. |



Views
-----

Telemetry view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When telemetry packets are sent through UDP, the packets may fail to be sent because the packet size is too large. You can run this command to limit the maximum packet size so that packets can be sent normally.


Example
-------

# Set the maximum size of telemetry packets sent through UDP to 1472 bytes.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] protocol udp packet-max-size 1472

```