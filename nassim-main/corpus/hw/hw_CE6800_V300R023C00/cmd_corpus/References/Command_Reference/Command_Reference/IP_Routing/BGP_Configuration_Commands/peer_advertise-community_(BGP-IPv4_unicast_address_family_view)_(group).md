peer advertise-community (BGP-IPv4 unicast address family view) (group)
=======================================================================

peer advertise-community (BGP-IPv4 unicast address family view) (group)

Function
--------



The **peer advertise-community** command configures a device to advertise a community attribute to its peer group.

The **undo peer advertise-community** command cancels the existing configuration.



By default, a device advertises no community attribute to its peer.


Format
------

**peer** *group-name* **advertise-community**

**undo peer** *group-name* **advertise-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



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

# Configure a device to advertise community attributes to each peer in a specified peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer test advertise-community

```