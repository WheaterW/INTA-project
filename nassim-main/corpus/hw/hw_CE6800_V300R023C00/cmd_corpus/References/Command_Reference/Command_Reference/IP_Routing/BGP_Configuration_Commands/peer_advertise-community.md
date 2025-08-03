peer advertise-community
========================

peer advertise-community

Function
--------



The **peer advertise-community** command configures a device to advertise community attributes to its peer.

The **undo peer advertise-community** command cancels the existing configuration.



By default, a device does not advertise community attributes to any peer.


Format
------

**peer** *ipv4-address* **advertise-community**

**undo peer** *ipv4-address* **advertise-community**


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

To configure a device to advertise community attributes to a specified peer or peer group, run the **peer advertise-community** command. If the command is run on the local device for a peer group, all the members in the peer group will inherit the configuration. This simplifies the application of routing policies and facilitates route maintenance and management.

**Precautions**

Before running the **peer advertise-community** command to configure a device to advertise a BGP community attribute, you can use a route-policy to define this community attribute.


Example
-------

# Configure a device to advertise community attributes to its peer.
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
[*HUAWEI-bgp-vpna] peer 10.1.1.1 advertise-community

```