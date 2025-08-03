peer advertise-community (BGP view)
===================================

peer advertise-community (BGP view)

Function
--------



The **peer advertise-community** command configures a device to advertise a community attribute to its peer.

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
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer advertise-community** command is used to configure a device to advertise a community attribute to its peer. If a device advertises a community attribute to its peer group, all the members of the peer group will inherit the configuration. This simplifies the application of routing policies and facilitates route maintenance and management.

**Precautions**

Before running the **peer advertise-community** command to advertise BGP community attributes, you can use a routing policy to define specific community attributes.


Example
-------

# Configure a device to advertise a community attribute to its peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 advertise-community

```