peer capability-advertise (BGP-VPN instance IPv6 address family view) (IPv6)
============================================================================

peer capability-advertise (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer capability-advertise** command enables optional BGP functions when a BGP peer advertises routes to its peer. The optional BGP functions include route-refresh, general function, 4-byte AS number, and Add-Path.

The **undo peer capability-advertise** command restores the default setting.



By default, the route-refresh and 4-byte AS number functions are enabled, but the general function and Add-Path are disabled.

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
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is in the format of X:X:X:X:X:X:X:X. |
| **route-refresh** | Indicates the route-refresh function. | - |
| **4-byte-as** | Indicates the 4-byte AS number function. | - |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

There are multiple optional BGP functions when a BGP peer advertises routes to its peer. The optional BGP functions include route-refresh, general function, 4-byte AS number, and Add-Path. You can run the **peer capability-advertise** command to select one of the functions based on the needs on the live network.

**Precautions**

Enabling or disabling the route-refresh function or the 4-byte AS number function causes the peer session to be disconnected and then re-established. This operation will cause temporary network interruption. Therefore, exercise caution when performing this operation.


Example
-------

# Configure a BGP device to advertise the route-refresh capability to its peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 capability-advertise route-refresh

```