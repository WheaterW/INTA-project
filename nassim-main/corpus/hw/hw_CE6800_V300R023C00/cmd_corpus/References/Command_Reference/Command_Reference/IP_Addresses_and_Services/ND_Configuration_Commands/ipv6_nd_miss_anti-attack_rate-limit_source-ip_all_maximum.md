ipv6 nd miss anti-attack rate-limit source-ip all maximum
=========================================================

ipv6 nd miss anti-attack rate-limit source-ip all maximum

Function
--------



The **ipv6 nd miss anti-attack rate-limit source-ip all maximum** command configures a rate limit for receiving ND Miss messages based on any source IPv6 address, that is, the number of ND Miss messages that can be processed per second based on any source IPv6 address.

The **undo ipv6 nd miss anti-attack rate-limit source-ip all maximum** command restores the default configuration.



By default, the rate limit for receiving ND Miss messages based on any source IPv6 address is 0.45 times the rate limit for receiving ND Miss messages configured in the system view.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd miss anti-attack rate-limit source-ip all maximum** *max-value*

**undo ipv6 nd miss anti-attack rate-limit source-ip all maximum** *max-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **miss** | Sets a rate limit for receiving ND Miss messages. | - |
| **maximum** *max-value* | Specifies a rate limit for receiving ND Miss messages based on any source IPv6 address. | The value is an integer ranging from 0 to 5000, in messages per second. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a device is attacked, it receives a large number of ND Miss messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for receiving ND Miss messages based on any source IPv6 address. After the configuration is complete, the device counts the number of ND Miss messages received per period based on any source IPv6 address. If the number exceeds the configured limit, the device does not process excess ND Miss messages.

**Configuration Impact**

After a rate limit for receiving ND Miss messages based on any source IPv6 address is configured, the device counts the number of ND Miss messages received per period based on any source IPv6 address. If the number of ND Miss messages exceeds the configured limit, the device does not process excess ND Miss messages. As a result, the device may fail to process valid ND Miss messages, causing user service interruptions.

**Precautions**

If STelnet login fails because the configured rate at which ND Miss messages are received based on each source IPv6 address is low, you can log in to the device through the console port and adjust the rate to a proper range.


Example
-------

# Set a rate limit for receiving ND Miss messages based on any source IPv6 address to 550 messages per second.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd miss anti-attack rate-limit source-ip all maximum 550

```