set flow-change-ratio interval
==============================

set flow-change-ratio interval

Function
--------



The **set flow-change-ratio interval** command specifies the interval of flow-change-alarm.

The **undo set flow-change-ratio interval** command restores the default setting.



By default, the statistics interval of flow-change-alarm is 5 minutes.


Format
------

**set flow-change-ratio interval** *interval-value*

**undo set flow-change-ratio interval** [ *interval-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-value* | Specifies the interval of flow-change-alarm. | The value is an integer that ranges from 1 to 10, in minutes. The default value is 5. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To notify users that the incoming and outgoing traffic on an interface increases or decreases sharply, the device supports the alarm function for the sudden traffic change. The corresponding alarm is hwOutputRateChangeOverThresholdNotice or hwInputRateChangeOverThresholdNotice.In the statistical period specified by the **set flow-change-ratio interval** command:

* If the abrupt increase rate of interface traffic in the current period exceeds the threshold set using the **set flow-change-ratio** command and the interface bandwidth usage after the abrupt increase exceeds the value set using the **set flow-change-ratio start-check bandwidth-usage** command, a sudden traffic change alarm is generated.
* If the abrupt traffic decrease rate in the current period exceeds the threshold specified using the **set flow-change-ratio** command and the interface bandwidth usage after the abrupt traffic decrease exceeds the threshold specified using the **set flow-change-ratio start-check bandwidth-usage** command, a sudden traffic change alarm is generated.

Example
-------

# Set the interval of flow-change-alarm to 5 minutes on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] set flow-change-ratio interval 5

```

**Table 1** Description of the **set flow-change-ratio interval** command output
| Item | Description |
| --- | --- |
| flow-change-ratio interval | The interval of flow-change-alarm. |