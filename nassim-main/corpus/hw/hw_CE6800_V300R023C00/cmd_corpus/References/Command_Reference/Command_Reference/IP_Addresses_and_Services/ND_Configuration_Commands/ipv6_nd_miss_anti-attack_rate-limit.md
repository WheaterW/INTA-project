ipv6 nd miss anti-attack rate-limit
===================================

ipv6 nd miss anti-attack rate-limit

Function
--------



The **ipv6 nd miss anti-attack rate-limit** command configures the rate at which neighbor discovery (ND) Miss messages are sent, that is, the number of ND Miss messages allowed to be processed per second.

The **undo ipv6 nd miss anti-attack rate-limit** command restores the default configuration.



By default, 550 ND Miss messages are sent per second.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd miss anti-attack rate-limit** *limit-number*

**undo ipv6 nd miss anti-attack rate-limit** *limit-number*

**undo ipv6 nd miss anti-attack rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-number* | Specifies the rate at which ND Miss messages are sent. | The value is an integer in the range of 1 to 5000, in packets per second. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device sends an IPv6 packet, if the MAC address corresponding to the destination IPv6 address of the IPv6 packet does not exist, an ND Miss message is generated. This consumes device resources and affects the processing of other services. To resolve this problem, run the ipv6 nd miss anti-attack rate-limit command to configure the rate at which ND Miss messages are sent. With this configuration, the device processes only the allowed number of ND Miss messages within a specified period to ensure normal service running.

**Configuration Impact**

After the rate at which ND Miss messages are sent is limited, a device collects statistics about the number of received ND Miss messages. If the number of ND Miss messages received within a specified period exceeds the upper limit, the device discards the excess ND Miss messages.


Example
-------

# Configure the rate at which ND Miss messages are sent as 3000.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd miss anti-attack rate-limit 3000

```