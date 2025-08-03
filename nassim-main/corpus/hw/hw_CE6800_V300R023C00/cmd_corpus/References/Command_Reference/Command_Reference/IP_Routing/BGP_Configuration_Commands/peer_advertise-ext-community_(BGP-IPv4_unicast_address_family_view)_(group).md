peer advertise-ext-community (BGP-IPv4 unicast address family view) (group)
===========================================================================

peer advertise-ext-community (BGP-IPv4 unicast address family view) (group)

Function
--------



The **peer advertise-ext-community** command enables a device to advertise extended community attributes to BGP peers in a peer group.

The **undo peer advertise-ext-community** command cancels the existing configuration.



By default, a device advertises no extended community attribute its peer or peer group.


Format
------

**peer** *group-name* **advertise-ext-community**

**undo peer** *group-name* **advertise-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-IPv4 unicast address family view


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

# Configure the device to advertise the extended community attribute to a peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer test advertise-ext-community

```