peer advertise-community (BGP-MVPN address family view) (BGPMVPN)
=================================================================

peer advertise-community (BGP-MVPN address family view) (BGPMVPN)

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
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer advertise-community** command configures a device to advertise community attributes to its peer.

**Precautions**

Before running the **peer advertise-community** command to configure a device to advertise a BGP community attribute, you can use a route-policy to define this community attribute.


Example
-------

# Configure a device to advertise community attributes to its peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.1 advertise-community

```