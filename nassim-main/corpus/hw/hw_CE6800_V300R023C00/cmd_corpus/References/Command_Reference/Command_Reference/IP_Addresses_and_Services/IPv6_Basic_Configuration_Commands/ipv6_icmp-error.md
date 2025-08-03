ipv6 icmp-error
===============

ipv6 icmp-error

Function
--------



The **ipv6 icmp-error** command limits the rate of sending ICMPv6 error messages.

The **undo ipv6 icmp-error** command restores the default.



By default, the size of the token buckets is 10 and the interval for placing tokens into the bucket is 100 milliseconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 icmp-error** { **ratelimit** *interval* | **bucket** *bucket-size* } \*

**undo ipv6 icmp-error**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ratelimit** *interval* | Specifies the interval for placing tokens into the bucket. | The value is an integer ranging from 0 to 2147483647, in milliseconds. |
| **bucket** *bucket-size* | Specifies the number of tokens the bucket contains. | It is an integer ranging from 1 to 200. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the case that a network does not suffer any attacks, a Router can correctly send ICMPv6 error messages to notify other devices of abnormalities in message transmission. If an attacker frequently sends ICMPv6 message to network devices, the network devices need to respond with ICMPv6 messages, which greatly affects the throughput and CPU usage of the system. Therefore, to prevent the system from sending a great number of ICMPv6 messages, you can run the **ipv6 icmp-error** command to limit the rate at which ICMPv6 messages are sent.The token bucket algorithm is used for counting ICMPv6 messages. One token represents an ICMPv6 message. The system places tokens into the virtual bucket at a certain interval until the number of tokens in the bucket reaches the upper limit. Once the number of ICMPv6 messages exceeds the maximum tokens that the bucket can contain, the excessive messages are discarded. You can limit the rate at which ICMPv6 messages are sent by setting the bucket size and the interval for placing tokens into the bucket.

**Configuration Impact**

The **ipv6 icmp-error** command is circular in nature. That is, if the bucket sizes and intervals set two times are different, the latest setting takes effect.If the interval for placing tokens into the bucket is 0, it indicates that the interval is not limited.


Example
-------

# Set the bucket size of ICMPv6 to 50.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 icmp-error bucket 50

```

# Set the interval for placing tokens into the bucket to 120 milliseconds and the bucket size to 50.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 icmp-error bucket 50 ratelimit 120

```

# Set the interval for placing tokens into the bucket to 120 milliseconds.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 icmp-error ratelimit 120

```