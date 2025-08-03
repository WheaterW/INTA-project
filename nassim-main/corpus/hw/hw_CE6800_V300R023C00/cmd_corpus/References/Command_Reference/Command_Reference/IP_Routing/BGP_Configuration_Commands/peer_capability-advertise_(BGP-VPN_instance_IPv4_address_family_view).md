peer capability-advertise (BGP-VPN instance IPv4 address family view)
=====================================================================

peer capability-advertise (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer capability-advertise** command enables optional functions for BGP to advertise routes, including the route-refresh function, conventional functions, and 4-byte AS number function.

The **undo peer capability-advertise** command restores the default setting.



By default, the BGP route-refresh and 4-byte AS number functions are enabled, but conventional functions are disabled.


Format
------

**peer** *ipv4-address* **capability-advertise** { **conventional** | **route-refresh** | **4-byte-as** }

**undo peer** *ipv4-address* **capability-advertise** { **conventional** | **route-refresh** | **4-byte-as** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **conventional** | Indicates conventional functions.   * This parameter is valid only in the BGP view and BGP-VPN instance IPv4 address family view. * After conventional functions are enabled on a device, the device does not have extended functions, such as route-refresh and GR. | - |
| **route-refresh** | Indicates the route-refresh function. | - |
| **4-byte-as** | Indicates the 4-byte AS number function. | - |



Views
-----

BGP-VPN instance IPv4 address family view


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
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 capability-advertise route-refresh

```