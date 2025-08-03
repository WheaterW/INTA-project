ipv6 nd send multicast rate-limit
=================================

ipv6 nd send multicast rate-limit

Function
--------



The **ipv6 nd send multicast rate-limit** command configures a rate limit for sending ND multicast messages, that is, the maximum number of ND multicast messages that can be sent per second.

The **undo ipv6 nd send multicast rate-limit** command restores the default configuration.



By default, the rate limit for sending ND multicast messages is not configured, and ND messages are sent at a globally configured rate limit.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd** { **rs** | **ns** | **na** } **send** **multicast** **rate-limit** *rate-limit*

**ipv6 nd ra send multicast rate-limit** *rate-limit*

**undo ipv6 nd** { **rs** | **ns** | **na** } **send** **multicast** **rate-limit** *rate-limit*

**undo ipv6 nd ra send multicast rate-limit** *rate-limit*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rs** | Specifies a rate limit for sending RS multicast messages. | - |
| **ns** | Specifies a rate limit for sending NS multicast messages. | - |
| **na** | Specifies a rate limit for sending NA multicast messages. | - |
| **rate-limit** *rate-limit* | Specifies a rate limit for sending ND multicast messages. | The value is an integer, in messages/second. If the message type is NA multicast, the value ranges from 1 to 10240; if the message type is NS, RS, or RA multicast, the value ranges from 1 to 1000. |
| **ra** | Specifies a rate limit for sending RA multicast messages. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a device is attacked, it receives a large number of ND or ND Miss messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for sending ND multicast messages on the device. After the configuration is complete, the device counts the number of ND multicast messages sent per period. If the number exceeds the configured limit, the device delays scheduling or ignores excess ND multicast messages.


Example
-------

# Set a rate limit for sending NS multicast messages to 550 messages/second.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ns send multicast rate-limit 550

```

# Set a rate limit for sending RA multicast messages to 550 messages/second.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ra send multicast rate-limit 550

```