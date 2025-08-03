ipv6 nd multicast-suppress dynamic limit
========================================

ipv6 nd multicast-suppress dynamic limit

Function
--------



The **ipv6 nd multicast-suppress dynamic limit** command configures the maximum number of dynamic proxy ND entries that can be learned in a BD.

The **undo ipv6 nd multicast-suppress dynamic limit** command restores the default configuration.



By default, a maximum of 256 dynamic proxy ND entries can be learned in a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd multicast-suppress dynamic limit** *limit-value*

**undo ipv6 nd multicast-suppress dynamic limit** *limit-value*

**undo ipv6 nd multicast-suppress dynamic limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-value* | Specifies the maximum number of dynamic proxy ND entries that can be learned in a BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer from 0 to 16384. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When an illegitimate user sends a large number of RA messages to attack a device, the device may learn a lot of dynamic proxy ND entries within a short period of time. As a result, the CPU usage increases sharply and a lot of memory resources are used, which prevents legitimate users from accessing network resources. To effectively prevent overflow of dynamic proxy ND entries, run the ipv6 nd multicast-suppress dynamic limit command to configure the maximum number of dynamic proxy ND entries that can be learned in a BD.



**Prerequisites**



NS multicast suppression has been enabled using the ipv6 nd multicast-suppress { proxy-reply [ unknown-options-unicast ] | unicast-forward } [ mismatch-discard ] enable command in the BD view.




Example
-------

# Configure the maximum number of dynamic proxy ND entries that can be learned in a BD as 500.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] ipv6 nd multicast-suppress proxy-reply enable
[*HUAWEI-bd10] ipv6 nd multicast-suppress dynamic limit 500

```