display debugging timeout
=========================

display debugging timeout

Function
--------



The **display debugging timeout** command displays the debugging timeout period.




Format
------

**display debugging timeout**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view the debugging timeout period, run the display debugging timeout command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the timeout period of the debugging function.
```
<HUAWEI> display debugging timeout
Debugging timeout
-----------------------------
Interval(min) RemainTime(sec)
-----------------------------
            5               0
-----------------------------

```

**Table 1** Description of the **display debugging timeout** command output
| Item | Description |
| --- | --- |
| Interval(min) | Timeout period (in minutes) after which the debugging function is disabled. |
| RemainTime(sec) | Remaining time (in seconds) before the debugging function is disabled. |