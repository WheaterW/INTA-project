clock wtr
=========

clock wtr

Function
--------



The **clock wtr** command sets the wait-to-restore (WTR) time for a clock source.



By default, the WTR time of a clock source is 5 minutes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock wtr** *wtr-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **wtr** *wtr-time* | Specifies the WTR time for a clock source. | The value is an integer ranging from 0 to 12, in minutes. The default value is 5. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the system detects that the clock source changes from abnormal to normal, the clock source status is updated only after the configured WTR time expires. (The effective clock source type does not include the PTP frequency source.) Setting a proper WTR time for the clock source status can effectively reduce the impact of frequent clock source status changes on the system clock source selection result.


Example
-------

# Set the WTR time of a clock source to 6 minutes.
```
<HUAWEI> system-view
[~HUAWEI] clock wtr 6

```