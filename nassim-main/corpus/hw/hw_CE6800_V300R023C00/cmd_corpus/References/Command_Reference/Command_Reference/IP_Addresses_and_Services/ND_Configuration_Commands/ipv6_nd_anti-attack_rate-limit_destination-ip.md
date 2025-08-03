ipv6 nd anti-attack rate-limit destination-ip
=============================================

ipv6 nd anti-attack rate-limit destination-ip

Function
--------



The **ipv6 nd anti-attack rate-limit destination-ip** command configures a rate limit for receiving ND messages based on a specified destination IPv6 address, that is, the number of ND messages that can be processed per second based on a specified destination IPv6 address.

The **undo ipv6 nd anti-attack rate-limit destination-ip** command restores the default configuration.



By default, no rate limit for receiving ND messages based on a specified destination IPv6 address is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd** { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **destination-ip** *ipv6-address* **maximum** *max-value*

**undo ipv6 nd** { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **destination-ip** *ipv6-address* **maximum** *max-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ns** | Sets a rate limit for receiving NS messages. | - |
| **na** | Sets a rate limit for receiving NA messages. | - |
| **rs** | Sets a rate limit for receiving RS messages. | - |
| **ra** | Sets a rate limit for receiving RA messages. | - |
| **destination-ip** *ipv6-address* | Specifies a destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **maximum** *max-value* | Specifies a rate limit for receiving ND messages based on a specified destination IPv6 address. | The value is an integer ranging from 0 to 5000, in messages per second. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a device is attacked, it receives a large number of ND messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for receiving ND messages based on a specified destination IPv6 address. After the configuration is complete, the device counts the number of ND messages received per period based on the specified destination IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages.

**Configuration Impact**

After a rate limit for receiving ND messages based on a specified destination IPv6 address is configured, the device counts the number of ND messages received per period based on the specified destination IPv6 address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. As a result, the device may fail to process valid ND messages, causing user service interruptions.

**Precautions**

If STelnet login fails because the configured rate at which ND messages are received based on destination IPv6 addresses is low, you can log in to the device through the console port and adjust the rate to a proper range.


Example
-------

# Set a rate limit for receiving NS messages based on a specified destination IPv6 address to 550 messages per second.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ns anti-attack rate-limit destination-ip 2001:db8:1::1 maximum 550

```