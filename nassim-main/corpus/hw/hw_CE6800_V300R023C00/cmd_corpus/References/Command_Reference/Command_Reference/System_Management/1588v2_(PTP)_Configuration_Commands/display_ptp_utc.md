display ptp utc
===============

display ptp utc

Function
--------



The **display ptp utc** command displays the Coordinated Universal Time (UTC).



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ptp utc**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

* If the system time is not synchronized with the UTC time, information similar to the following is displayed:Non-UTC Time:2000-01-04 09:56:24
* If the system time is synchronized with the UTC time, the UTC time of the grandmaster clock that the system traces is displayed. For example:UTC Time:2012-07-01 00:41:45

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the current UTC time.
```
<HUAWEI> display ptp utc
UTC Time:2012-07-01 00:41:45

```

**Table 1** Description of the **display ptp utc** command output
| Item | Description |
| --- | --- |
| UTC Time | UTC Time. |