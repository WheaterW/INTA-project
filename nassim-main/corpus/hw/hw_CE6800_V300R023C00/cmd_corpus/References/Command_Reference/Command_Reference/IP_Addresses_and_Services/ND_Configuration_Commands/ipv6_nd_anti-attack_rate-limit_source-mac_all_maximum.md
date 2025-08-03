ipv6 nd anti-attack rate-limit source-mac all maximum
=====================================================

ipv6 nd anti-attack rate-limit source-mac all maximum

Function
--------



The **ipv6 nd anti-attack rate-limit source-mac all maximum** command configures a rate limit for sending ND messages to the CPU based on any source MAC address, that is, the number of ND messages that can be processed per second based on any source MAC address.

The **undo ipv6 nd anti-attack rate-limit source-mac all maximum** command restores the default configuration.



The default rate limit for sending ND messages to the CPU based on any source MAC address is 0.45 times the rate limit for sending ND messages to the CPU that is configured in the system view.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd** { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **source-mac** **all** **maximum** *max-value*

**undo ipv6 nd** { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **source-mac** **all** **maximum** *max-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ns** | Indicates the rate at which NS messages are sent. | - |
| **na** | Indicates the rate at which NA messages are sent. | - |
| **rs** | Indicates the rate at which RS messages are sent. | - |
| **ra** | Indicates the rate at which RA messages are sent. | - |
| **maximum** *max-value* | Specifies a rate limit for sending ND messages to the CPU based on any source MAC address. | The value is an integer ranging from 0 to 5000, in pps. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a device is attacked, it receives a large number of ND messages within a short period. As a result, the device consumes many CPU resources to learn and respond to peer entries, affecting processing of other services. To resolve this issue, configure a rate limit for sending ND messages to the CPU based on any source MAC address. After the configuration is complete, the device counts the number of ND messages received per period based on any source MAC address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages.

**Configuration Impact**

After a rate limit for sending ND messages to the CPU based on any source MAC address is configured, the device counts the number of ND messages received per period based on any source MAC address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. As a result, the device may fail to process valid ND messages, causing user service interruptions.

**Precautions**

If the configured rate of sending ND messages based on each source MAC address is low, STelnet login fails. In this case, you can log in to the device through the console port and adjust the rate to a proper range.


Example
-------

# Set a rate limit for sending NS messages to the CPU based on any source MAC address to 550 pps.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ns anti-attack rate-limit source-mac all maximum 550

```

# Set a rate limit for sending RA messages to the CPU based on any source MAC address to 550 pps.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ra anti-attack rate-limit source-mac all maximum 550

```

# Set a rate limit for sending RS messages to the CPU based on any source MAC address to 550 pps.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd rs anti-attack rate-limit source-mac all maximum 550

```

# Set a rate limit for sending NA messages to the CPU based on any source MAC address to 550 pps.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd na anti-attack rate-limit source-mac all maximum 550

```