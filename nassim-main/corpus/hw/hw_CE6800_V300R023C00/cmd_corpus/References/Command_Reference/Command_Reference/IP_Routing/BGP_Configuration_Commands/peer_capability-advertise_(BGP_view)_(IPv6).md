peer capability-advertise (BGP view) (IPv6)
===========================================

peer capability-advertise (BGP view) (IPv6)

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
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **route-refresh** | Indicates the route-refresh function. | - |
| **4-byte-as** | Indicates the 4-byte AS number function. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP provides many optional functions for advertising routes, including route-refresh, conventional functions, and 4-byte AS numbers.

**Precautions**

Enabling or disabling the route-refresh function or the 4-byte AS number function causes the peer session to be disconnected and then re-established. This operation will cause temporary network interruption. Therefore, exercise caution when performing this operation.


Example
-------

# Configure a BGP device to advertise the route-refresh capability to its peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 capability-advertise route-refresh

```