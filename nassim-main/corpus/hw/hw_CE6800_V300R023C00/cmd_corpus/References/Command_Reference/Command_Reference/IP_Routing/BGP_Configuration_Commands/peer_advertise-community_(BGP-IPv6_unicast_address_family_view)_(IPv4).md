peer advertise-community (BGP-IPv6 unicast address family view) (IPv4)
======================================================================

peer advertise-community (BGP-IPv6 unicast address family view) (IPv4)

Function
--------



The **peer advertise-community** command configures a device to advertise community attributes to its peer.

The **undo peer advertise-community** command cancels the existing configuration.



By default, a device does not advertise community attributes to any peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

BGP-IPv6 unicast address family view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 advertise-community

```