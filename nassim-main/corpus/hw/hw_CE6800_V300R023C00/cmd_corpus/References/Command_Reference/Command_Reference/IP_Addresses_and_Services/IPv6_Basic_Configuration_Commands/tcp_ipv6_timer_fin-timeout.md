tcp ipv6 timer fin-timeout
==========================

tcp ipv6 timer fin-timeout

Function
--------



The **tcp ipv6 timer fin-timeout** command sets a TCP6 FIN-Wait timer value.

The **undo tcp ipv6 timer fin-timeout** command restores the default value.



By default, the TCP6 FIN-Wait timer value is 675 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tcp ipv6 timer fin-timeout** *interval*

**undo tcp ipv6 timer fin-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a TCP6 FIN-Wait timer value. | The value is an integer ranging from 76 to 3600, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the TCP6 connection status changes from FIN\_WAIT\_1 to FIN\_WAIT\_2, the FIN-Wait timer is enabled. If no FIN packet is received before the timeout of FIN-Wait timer, the TCP6 connection is terminated.

**Precautions**

If this command is configured for several times in the same view, only the last configuration takes effect.You are recommended to configure the parameter under the guidance of the technical personnel.


Example
-------

# Configure the TCP6 FIN-Wait timer value to 800 seconds.
```
<HUAWEI> system-view
[~HUAWEI] tcp ipv6 timer fin-timeout 800

```