ipv6 nd multicast-suppress dynamic expire-time
==============================================

ipv6 nd multicast-suppress dynamic expire-time

Function
--------



The **ipv6 nd multicast-suppress dynamic expire-time** command configures the aging time of dynamic proxy ND entries.

The **undo ipv6 nd multicast-suppress dynamic expire-time** command restores the default configuration.



By default, the aging time of dynamic proxy ND entries is 900s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd multicast-suppress dynamic expire-time** *expire-time-value*

**undo ipv6 nd multicast-suppress dynamic expire-time** *expire-time-value*

**undo ipv6 nd multicast-suppress dynamic expire-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *expire-time-value* | Specifies the aging time of dynamic proxy ND entries.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 60 to 86400, in seconds. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The proxy ND entries need to be updated regularly to ensure communication reliability. Dynamic proxy ND entries have a life cycle. If a dynamic proxy ND entry is not updated before its life cycle ends, this entry will be deleted from the proxy ND table. Such a life cycle is called aging time. If a dynamic proxy ND entry is updated before its life cycle expires, the aging time of the entry is recalculated. To configure the aging time of dynamic proxy ND entries, run the ipv6 nd multicast-suppress dynamic expire-time command.



**Prerequisites**



NS multicast suppression has been enabled using the ipv6 nd multicast-suppress { proxy-reply [ unknown-options-unicast ] | unicast-forward } [ mismatch-discard ] enable command in the BD view.



**Precautions**



Do not configure the aging time of dynamic proxy ND entries to a value more than four times of the aging time of MAC address entries (MAC address entries can be viewed using the **display mac-address aging-time** command).




Example
-------

# Configure the aging time of dynamic proxy ND entries as 1000s.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] ipv6 nd multicast-suppress proxy-reply enable
[*HUAWEI-bd10] ipv6 nd multicast-suppress dynamic expire-time 1000

```