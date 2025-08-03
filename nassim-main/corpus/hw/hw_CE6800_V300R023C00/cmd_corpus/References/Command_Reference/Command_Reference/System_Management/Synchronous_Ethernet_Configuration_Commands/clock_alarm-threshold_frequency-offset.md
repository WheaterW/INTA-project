clock alarm-threshold frequency-offset
======================================

clock alarm-threshold frequency-offset

Function
--------



The **clock alarm-threshold frequency-offset** command configures an alarm threshold for frequency offset at the physical layer.

The **undo clock alarm-threshold frequency-offset** command restores the default configuration.



By default, the alarm threshold for frequency offset at the physical layer is 9200 ppb.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock alarm-threshold frequency-offset** *frequency-offset-value*

**undo clock alarm-threshold frequency-offset** [ *frequency-offset-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **frequency-offset** *frequency-offset-value* | Specifies an alarm threshold for frequency offset at the physical layer. | The value is an integer ranging from 10 to 92. The default value is 92, in 100 ppb. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The device can detect the frequency source specified in the frequency source priority list. When the frequency offset exceeds the threshold, the device reports a frequency offset threshold-crossing alarm.


Example
-------

# Configure the alarm threshold for frequency offset at the physical layer as 2000 ppb.
```
<HUAWEI> system-view
[~HUAWEI] clock alarm-threshold frequency-offset 20

```