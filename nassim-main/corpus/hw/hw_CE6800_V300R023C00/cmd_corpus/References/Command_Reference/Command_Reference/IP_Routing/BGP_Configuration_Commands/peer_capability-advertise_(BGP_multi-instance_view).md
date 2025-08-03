peer capability-advertise (BGP multi-instance view)
===================================================

peer capability-advertise (BGP multi-instance view)

Function
--------



The **peer capability-advertise** command enables optional functions for BGP to advertise routes, including the route-refresh function, conventional functions, and 4-byte AS number function.

The **undo peer capability-advertise** command restores the default setting.



By default, the BGP route-refresh and 4-byte AS number functions are enabled, but conventional functions are disabled.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *ipv4-address* **capability-advertise** { **conventional** | **route-refresh** | **4-byte-as** }

**undo peer** *ipv4-address* **capability-advertise** { **conventional** | **route-refresh** | **4-byte-as** }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *ipv6-address* **capability-advertise** { **route-refresh** | **4-byte-as** }

**undo peer** *ipv6-address* **capability-advertise** { **route-refresh** | **4-byte-as** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **conventional** | Indicates conventional functions.   * This parameter is valid only in the BGP view and BGP-VPN instance IPv4 address family view. * After conventional functions are enabled on a device, the device does not have extended functions, such as route-refresh and GR. | - |
| **route-refresh** | Indicates the route-refresh function. | - |
| **4-byte-as** | Indicates the 4-byte AS number function. | - |
| **peer** *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| **peer** *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP has many optional functions when advertising routes, including the route-refresh function, conventional functions, and 4-byte AS number function. Using the **peer capability-advertise** command, you can enable or disable these functions as required.

**Precautions**

Enabling or disabling the route-refresh function, conventional function, or 4-byte AS number function causes the peer session to be disconnected and then re-established, leading to a temporary network interruption. Therefore, exercise caution when performing this operation.


Example
-------

# Configure a BGP device to advertise the route-refresh capability to its peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 capability-advertise route-refresh

```