ipv6 icmp source-address
========================

ipv6 icmp source-address

Function
--------



The **ipv6 icmp source-address** command configures the IPv6 address of the loopback interface as the source IPv6 address of ICMPv6 Port Unreachable or Time Exceeded messages.

The **undo ipv6 icmp source-address** command restores the default configuration.



By default, the IPv6 address of the loopback interface is not used as the source IPv6 address of ICMPv6 Port Unreachable or Time Exceeded messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 icmp** { **hop-limit-exceeded** | **port-unreachable** } **source-address**

**undo ipv6 icmp** { **hop-limit-exceeded** | **port-unreachable** } **source-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hop-limit-exceeded** | Indicates ICMPv6 Time Exceeded messages. | - |
| **port-unreachable** | Indicates ICMPv6 Port Unreachable messages. | - |



Views
-----

Loopback interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To reduce exposure of the IPv6 addresses of device interfaces in order to prevent against detection through ICMPv6 Port Unreachable or Time Exceeded messages, run the **ipv6 icmp source-address** command to specify the source IPv6 address of ICMPv6 Port Unreachable or Time Exceeded messages. After this command is run, if the device needs to give a reply to the messages, the device uses the IPv6 address of the loopback interface as the source IPv6 address of ICMPv6 Port Unreachable or Time Exceeded messages.

**Precautions**

This command can be configured only on one loopback interface in a VPN.


Example
-------

# Configure the IPv6 address of the Loopback2 interface as the source IPv6 address of ICMPv6 Port Unreachable messages.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback 2
[*HUAWEI-LoopBack2] ipv6 enable
[*HUAWEI-LoopBack2] ipv6 icmp port-unreachable source-address

```

# Configure the IPv6 address of the Loopback1 interface as the source IPv6 address of ICMPv6 Time Exceeded messages.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn10
[*HUAWEI-vpn-instance-vpn10] quit
[*HUAWEI] interface loopback 1
[*HUAWEI-LoopBack1] ipv6 enable
[*HUAWEI-LoopBack1] ip binding vpn-instance vpn10
[*HUAWEI-LoopBack1] ipv6 icmp hop-limit-exceeded source-address

```