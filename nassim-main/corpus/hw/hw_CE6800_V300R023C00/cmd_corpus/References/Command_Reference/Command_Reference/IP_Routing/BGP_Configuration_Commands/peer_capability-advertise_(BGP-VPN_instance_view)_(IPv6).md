peer capability-advertise (BGP-VPN instance view) (IPv6)
========================================================

peer capability-advertise (BGP-VPN instance view) (IPv6)

Function
--------



The **peer capability-advertise** command enables optional functions for BGP to advertise routes, including the route-refresh function, conventional functions, and 4-byte AS number function.

The **undo peer capability-advertise** command restores the default setting.



By default, the BGP route-refresh and 4-byte AS number functions are enabled, but conventional functions are disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **capability-advertise** { **route-refresh** | **4-byte-as** }

**undo peer** *ipv6-address* **capability-advertise** { **route-refresh** | **4-byte-as** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **route-refresh** | Indicates the route-refresh function. | - |
| **4-byte-as** | Indicates the 4-byte AS number function. | - |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP has many optional functions when advertising routes, including the route-refresh function, conventional functions, and 4-byte AS number function. Using the **peer capability-advertise** command, you can enable or disable these functions as required.

**Precautions**

Enabling or disabling the route-refresh function or the 4-byte AS number function causes the peer session to be disconnected and then re-established. This operation will cause temporary network interruption. Therefore, exercise caution when performing this operation.


Example
-------

# Configure a BGP device to advertise the route-refresh capability to its peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn] quit
[~HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn
[*HUAWEI-bgp] peer 2001:DB8:4::4 as-number 100
[*HUAWEI-bgp-instance-vpn] peer 2001:DB8:4::4 capability-advertise route-refresh

```