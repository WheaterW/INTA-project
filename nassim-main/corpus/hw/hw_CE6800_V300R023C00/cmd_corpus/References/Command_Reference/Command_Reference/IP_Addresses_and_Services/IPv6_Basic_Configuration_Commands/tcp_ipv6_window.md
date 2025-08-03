tcp ipv6 window
===============

tcp ipv6 window

Function
--------



The **tcp ipv6 window** command sets a TCP6 window size for setting up a TCP6 connection.

The **undo tcp ipv6 window** command restores the default TCP6 window size.



By default, the TCP6 window size is 8 Kbytes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tcp ipv6 window** *window-size*

**undo tcp ipv6 window**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *window-size* | Specifies a TCP6 window size, in Kbytes. | The value is an integer ranging from 1 to 32, in KBytes. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To change the TCP6 window size that is used for setting up a TCP session, run the tcp window command.

**Precautions**

If the tcp window command is run more than once, the latest configuration overrides the previous one.Set parameters under the guidance of Huawei technical personnel.


Example
-------

# Configure a TCP6 window size for setting up a TCP6 connection as 4 Kbytes.
```
<HUAWEI> system-view
[~HUAWEI] tcp ipv6 window 4

```