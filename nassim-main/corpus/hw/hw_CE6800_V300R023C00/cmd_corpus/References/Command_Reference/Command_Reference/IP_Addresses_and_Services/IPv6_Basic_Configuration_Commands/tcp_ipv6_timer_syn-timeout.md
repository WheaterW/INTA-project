tcp ipv6 timer syn-timeout
==========================

tcp ipv6 timer syn-timeout

Function
--------



The **tcp ipv6 timer syn-timeout** command sets the TCP6 SYN-Wait timer.

The **undo tcp ipv6 timer syn-timeout** command restores the default value of the timer.

The default value of the TCP6 SYN-Wait timer is 75 seconds.



By default, the default value of the TCP6 SYN-Wait timer is 75 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tcp ipv6 timer syn-timeout** *interval*

**undo tcp ipv6 timer syn-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the value of the TCP6 SYN-Wait timer. | The value is an integer that ranges from 2 to 600, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a SYN packet is sent, TCP6 enables the SYN-Wait timer. If no response packet is received before SYN-Wait is timeout, the TCP6 connection is terminated.

**Precautions**

If this command is configured for several times in the same view, only the last configuration takes effect.You are recommended to configure the parameters under the guidance of the technical personnel.


Example
-------

# Set the TCP6 SYN-Wait timer to 100 seconds.
```
<HUAWEI> system-view
[~HUAWEI] tcp ipv6 timer syn-timeout 100

```