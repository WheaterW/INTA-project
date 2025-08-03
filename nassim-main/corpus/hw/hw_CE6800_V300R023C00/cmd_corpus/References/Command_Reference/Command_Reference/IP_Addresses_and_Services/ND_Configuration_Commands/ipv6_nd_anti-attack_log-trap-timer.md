ipv6 nd anti-attack log-trap-timer
==================================

ipv6 nd anti-attack log-trap-timer

Function
--------



The **ipv6 nd anti-attack log-trap-timer** command configures an interval for recording ND logs and sending ND traps in the case of potential attacks.

The **undo ipv6 nd anti-attack log-trap-timer** command restores the default configuration.



The default interval for recording ND logs and sending ND traps is 600s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd anti-attack log-trap-timer** *time-value*

**undo ipv6 nd anti-attack log-trap-timer**

**undo ipv6 nd anti-attack log-trap-timer** *time-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies an interval for recording ND logs and sending ND traps. | The value is an integer ranging from 60 to 3600, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After a rate limit is configured for ND or ND Miss messages, the device counts the number of received ND or ND Miss messages. If the number of ND or ND Miss messages received in a specified period exceeds the configured limit, the device discards excess ND or ND Miss messages. The device considers this is a potential attack, and records ND logs for the potential attack and sends the corresponding ND traps to the NMS.

If potential attacks frequently occur, the device generates a large number of logs and traps. To resolve this issue, configure a large interval for recording ND logs and sending ND traps.


Example
-------

# Set an interval for recording ND logs and sending ND traps to 120s.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd anti-attack log-trap-timer 120

```