peer advertise-community (BGP-IPv4 unicast address family view)
===============================================================

peer advertise-community (BGP-IPv4 unicast address family view)

Function
--------



The **peer advertise-community** command configures a device to advertise a community attribute to its peer group.

The **undo peer advertise-community** command cancels the existing configuration.



By default, a device advertises no community attribute to its peer.


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

BGP-IPv4 unicast address family view


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
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 advertise-community

```