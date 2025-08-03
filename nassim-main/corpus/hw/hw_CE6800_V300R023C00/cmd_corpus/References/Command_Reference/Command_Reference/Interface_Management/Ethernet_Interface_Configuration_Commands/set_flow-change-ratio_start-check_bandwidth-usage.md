set flow-change-ratio start-check bandwidth-usage
=================================================

set flow-change-ratio start-check bandwidth-usage

Function
--------



The **set flow-change-ratio start-check bandwidth-usage** command specifies the percentage of flow to start flow-change-alarm check.

The **undo set flow-change-ratio start-check bandwidth-usage** command restores the default setting.



By default, the percentage of interface bandwidth usage is 20% to start flow-change-alarm check.


Format
------

**set flow-change-ratio start-check bandwidth-usage** *value*

**undo set flow-change-ratio start-check bandwidth-usage** [ *value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the percentage of interface bandwidth usage to start flow-change-alarm check. | The value is an integer ranging from 1 to 100, in percentage. The default value is 20. |



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

# Set 50% of flow to start flow-change-alarm check. on interface 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] set flow-change-ratio start-check bandwidth-usage 50

```

**Table 1** Description of the **set flow-change-ratio start-check bandwidth-usage** command output
| Item | Description |
| --- | --- |
| flow-change-ratio start-check bandwidth-usage | The percent of flow to start flow-change-alarm check on interface. |