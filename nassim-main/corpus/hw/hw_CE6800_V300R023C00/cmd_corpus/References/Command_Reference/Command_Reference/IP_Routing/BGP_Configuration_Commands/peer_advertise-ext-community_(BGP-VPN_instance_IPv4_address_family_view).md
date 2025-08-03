peer advertise-ext-community (BGP-VPN instance IPv4 address family view)
========================================================================

peer advertise-ext-community (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer advertise-ext-community** command enables a device to advertise an extended community attribute to its peer.

The **undo peer advertise-ext-community** command cancels the existing configuration.



By default, a device advertises no extended community attribute its peer or peer group.


Format
------

**peer** *ipv4-address* **advertise-ext-community**

**undo peer** *ipv4-address* **advertise-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer advertise-ext-community** command is used to advertise the extended community attribute to a specified peer or peer group.

**Precautions**

Before running the **peer advertise-ext-community** command to configure extended community attributes, you can use a routing policy to define specific community attributes.


Example
-------

# Configure a device to advertise an extended community attribute to its peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] peer 10.1.1.1 advertise-ext-community

```