remark local-precedence
=======================

remark local-precedence

Function
--------



The **remark local-precedence** command configures an action of re-marking the internal priority in packets in a traffic behavior.

The **undo remark local-precedence** command deletes the configuration.



By default, an action of re-marking the internal priority in packets is not configured in a traffic behavior.


Format
------

**remark local-precedence** { *local-precedence-name* | *local-precedence-value* } [ *color* ]

**undo remark local-precedence**

**undo remark local-precedence** { *local-precedence-name* | *local-precedence-value* } [ *color* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-precedence-name* | Specifies the internal priority name. | The value can be af1, af2, af3, af4, be, cs6, cs7, or ef. |
| *local-precedence-value* | Specifies the internal priority value. | The value is an integer that ranges from 0 to 7. A larger value indicates a higher priority. |
| *color* | Indicates the color corresponds to an internal priority. | The value can be green, yellow, and red. |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To provide differentiated services based on the internal priority of packets, run the **remark local-precedence** command to configure the device to re-mark the internal priority of packets so that the device can provide QoS based on the re-marked priority.

**Precautions**

* Re-marking the internal priority of packets affects only the QoS processing of packets on the device.
* If remark 8021p is configured in a traffic behavior, remark local-precedence cannot be configured in the traffic behavior.
* remark local-precedence is not supported in the outbound direction.
* If you run the **remark local-precedence** command multiple times, the latest configuration takes effect. That is, in the same traffic behavior view:
* If you run this command repeatedly to re-mark the internal priority and the packet color corresponding to the internal priority, only the latest configuration takes effect.
* If you run this command multiple times to re-mark the internal priority, the internal priority takes effect based on the latest configuration, and the packet color corresponding to the internal priority takes effect based on the previous configuration.


Example
-------

# Re-mark the internal priority of packets with 2 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] remark local-precedence 2

```