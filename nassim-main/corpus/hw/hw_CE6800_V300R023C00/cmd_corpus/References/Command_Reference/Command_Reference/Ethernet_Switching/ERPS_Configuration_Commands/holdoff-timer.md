holdoff-timer
=============

holdoff-timer

Function
--------



The **holdoff-timer** command sets the Holdoff timer of an ERPS ring.

The **undo holdoff-timer** command restores the default value of the Holdoff timer.



By default, the Holdoff timer is 0 for the ERPS ring.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**holdoff-timer** *time-value*

**undo holdoff-timer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the value of the Holdoff timer for the ERPS ring. | The value is an integer ranging from 0 to 100, in hundred milliseconds. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On different Layer 2 networks running ERPS, there may be different requirements on protective switchovers. For example, if multi-layer services are provided, users hope that a protective switchover is not performed immediately after a server fails, ensuring that clients do not sense the failure.In this case, you can set run the **holdoff-timer** command to set a Holdoff timer. If the fault occurs, the fault is not immediately sent to ERPS until the Holdoff timer times out.


Example
-------

# Set the value of the Holdoff timer to 10 hundred milliseconds for ERPS ring 10.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 10
[*HUAWEI-erps-ring10] holdoff-timer 10

```