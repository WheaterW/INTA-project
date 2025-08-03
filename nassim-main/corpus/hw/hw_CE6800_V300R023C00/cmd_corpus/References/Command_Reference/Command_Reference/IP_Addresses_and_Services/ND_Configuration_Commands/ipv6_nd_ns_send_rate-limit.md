ipv6 nd ns send rate-limit
==========================

ipv6 nd ns send rate-limit

Function
--------



The **ipv6 nd ns send rate-limit** command configures the rate limit of sending NS messages for address resolution or parsing.

The **undo ipv6 nd ns send rate-limit** command restores the default configuration.



By default, a maximum of 550 NS messages for address resolution or probing can be sent per second.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ns send rate-limit** *rate-limit*

**undo ipv6 nd ns send rate-limit** *rate-limit*

**undo ipv6 nd ns send rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rate-limit* | Specifies the rate limit of sending NS messages for address resolution or probing. | The value is an integer ranging from 1 to 1000, in packets per second. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the peer device is limited by the capability of receiving NS messages or the local device is limited by the capability of processing NA response messages, run the **ipv6 nd ns send rate-limit** command to configure the rate limit of sending NS messages for address resolution or parsing. This prevents a failure to learn ND entries or incorrect deletion of ND entries due to discarding of NA packets.

**Configuration Impact**

if the rate limit of sending NS messages is a small value, the address resolution of a large number of neighbor entries becomes slow.

**Precautions**

Using the default rate limit value is recommended. Exercise caution while using this command to configure the rate limit of sending NS messages for address resolution or parsing.


Example
-------

# Set the rate limit of sending NS messages for address resolution or probing to 500 per second.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ns send rate-limit 500

```