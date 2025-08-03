ipv6 nd anti-attack rate-limit (interface view)
===============================================

ipv6 nd anti-attack rate-limit (interface view)

Function
--------



The **ipv6 nd anti-attack rate-limit** command sets the rate limit value for ND packets.

The **undo ipv6 nd anti-attack rate-limit** command deletes the rate limit value for ND packets.



By default, the ND anti-attack function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd** { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** *limit*

**undo ipv6 nd** { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** *limit*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ns** | Indicates the rate at which NS messages are sent. | - |
| **na** | Indicates the rate at which NA messages are sent. | - |
| **rs** | Indicates the rate at which RS messages are sent. | - |
| **ra** | Indicates the rate at which RA messages are sent. | - |
| **rate-limit** *limit* | Specify the speed limit value for ND packets. | The value is an integer that ranges from 0 to 5000, in packets per second. |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an attacker sends a large number of ND packets to a device within a short period, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for sending ND packets to the CPU. After the configuration is complete, the device counts the number of ND packets received per period based on source IP addresses. If the number of ND packets exceeds the configured limit, the device does not process excess ND packets.

**Configuration Impact**

After the rate limit value is set for ND packets, the device counts the number of received ND packets. If the number of ND packets received in a specified period exceeds the upper limit, the device discards the excess ND packets. As a result, the device may fail to process some valid ND packets, causing service interruptions.

**Precautions**

If STelnet login fails because the configured ND packet sending rate is too low, you can log in to the device through the console port and adjust the rate to a proper value.


Example
-------

# Set the value of NS packet rate limit based on suppression type to 550 pps on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ns anti-attack rate-limit 550

```