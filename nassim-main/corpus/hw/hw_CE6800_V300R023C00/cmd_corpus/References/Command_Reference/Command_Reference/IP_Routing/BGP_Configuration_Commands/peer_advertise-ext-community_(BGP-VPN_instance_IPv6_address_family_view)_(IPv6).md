peer advertise-ext-community (BGP-VPN instance IPv6 address family view) (IPv6)
===============================================================================

peer advertise-ext-community (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer advertise-ext-community** command enables a device to advertise an extended community attribute to its peer.

The **undo peer advertise-ext-community** command cancels the existing configuration.



By default, a device does not advertise extended community attribute to its peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **advertise-ext-community**

**undo peer** *ipv6-address* **advertise-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer advertise-ext-community** command is used to enable a device to advertise an extended community attribute to a specified peer. If a device advertises an extended community attribute to a specified peer group, all the members of the peer group will inherit the configuration. This simplifies the application of routing policies and facilitates route maintenance and management.

**Precautions**

Before running the **peer advertise-community** command to advertise BGP community attributes, you can use a routing policy to define specific community attributes.


Example
-------

# Configure a device to advertise an extended community attribute to its peer.
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
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 advertise-ext-community

```