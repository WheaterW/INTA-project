peer advertise-ext-community (BGP view)
=======================================

peer advertise-ext-community (BGP view)

Function
--------



The **peer advertise-ext-community** command enables a device to advertise an extended community attribute to its peer.

The **undo peer advertise-ext-community** command cancels the existing configuration.



By default, a device does not advertise extended community attribute to its peer.


Format
------

**peer** *ipv4-address* **advertise-ext-community**

**undo peer** *ipv4-address* **advertise-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer advertise-ext-community** command to determine whether to advertise the extended community attribute to a specified peer.By default, the extended community attribute is advertised to the peer in the address family that does not support the **peer advertise-ext-community** command.

**Precautions**

Before running the **peer advertise-ext-community** command to configure extended community attributes, you can use a routing policy to define specific community attributes.


Example
-------

# Configure a device to advertise an extended community attribute to its peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 advertise-ext-community

```