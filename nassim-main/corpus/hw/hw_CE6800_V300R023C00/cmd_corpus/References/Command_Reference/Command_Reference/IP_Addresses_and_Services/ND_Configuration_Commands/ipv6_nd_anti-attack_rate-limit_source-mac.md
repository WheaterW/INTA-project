ipv6 nd anti-attack rate-limit source-mac
=========================================

ipv6 nd anti-attack rate-limit source-mac

Function
--------



The **ipv6 nd anti-attack rate-limit source-mac** command configures a rate limit for sending ND messages to the CPU based on a specified source MAC address, that is, the number of ND messages that can be processed per second based on a specified source MAC address.

The **undo ipv6 nd anti-attack rate-limit source-mac** command restores the default configuration.



By default, no rate limit for sending ND messages to the CPU based on a specified source MAC address is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd** { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **source-mac** *mac-address* **maximum** *max-value*

**undo ipv6 nd** { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **source-mac** *mac-address* **maximum** *max-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ns** | Indicates the rate at which NS messages are sent. | - |
| **na** | Indicates the rate at which NA messages are sent. | - |
| **rs** | Indicates the rate at which RS messages are sent. | - |
| **ra** | Indicates the rate at which RA messages are sent. | - |
| **source-mac** *mac-address* | Specifies a source MAC address. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. For example, the MAC address is 00e0-fc12-3456. |
| **maximum** *max-value* | Specifies a rate limit for sending ND messages to the CPU based on a specified source MAC address. | The value is an integer ranging from 0 to 5000, in pps. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a device is attacked, it receives a large number of ND messages within a short period. As a result, the device consumes many CPU resources to learn and respond to peer entries, affecting processing of other services. To resolve this issue, configure a rate limit for sending ND messages to the CPU based on a specified source MAC address. After the configuration is complete, the device counts the number of ND messages received per period based on a specified source MAC address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages.

**Configuration Impact**

After a rate limit for sending ND messages to the CPU based on a specified source MAC address is configured, the device counts the number of ND messages received per period based on a specified source MAC address. If the number of ND messages exceeds the configured limit, the device does not process excess ND messages. As a result, the device may fail to process valid ND messages, causing user service interruptions.

**Precautions**

If the rate at which ND messages are sent based on source MAC addresses is set to a small value, STelnet login fails. In this case, you can log in to the device through the console port and adjust the rate to a proper value.


Example
-------

# Set a rate limit for sending NA messages to the CPU based on a specified source MAC address to 550 pps.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd na anti-attack rate-limit source-mac 00e0-fc12-3456 maximum 550

```

# Set a rate limit for sending RA messages to the CPU based on a specified source MAC address to 550 pps.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ra anti-attack rate-limit source-mac 00e0-fc12-3456 maximum 550

```

# Set a rate limit for sending RS messages to the CPU based on a specified source MAC address to 550 pps.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd rs anti-attack rate-limit source-mac 00e0-fc12-3456 maximum 550

```

# Set a rate limit for sending NS messages to the CPU based on a specified source MAC address to 550 pps.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd ns anti-attack rate-limit source-mac 00e0-fc12-3456 maximum 550

```