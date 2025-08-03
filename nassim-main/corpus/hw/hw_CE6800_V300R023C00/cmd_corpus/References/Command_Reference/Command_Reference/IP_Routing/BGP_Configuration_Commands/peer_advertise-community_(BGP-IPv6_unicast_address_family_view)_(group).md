peer advertise-community (BGP-IPv6 unicast address family view) (group)
=======================================================================

peer advertise-community (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer advertise-community** command configures a device to advertise a community attribute to its peer group.

The **undo peer advertise-community** command cancels the existing configuration.



By default, a device advertises no community attribute to its peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **advertise-community**

**undo peer** *group-name* **advertise-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer advertise-community** command is used to configure a device to advertise a community attribute to its peer group. If a device advertises a community attribute to its peer group, all the members of the peer group will inherit the configuration. This simplifies the application of routing policies and facilitates route maintenance and management.

**Precautions**

Before running the **peer advertise-community** command to advertise BGP community attributes, you can use a routing policy to define specific community attributes.


Example
-------

# Configure a device to advertise a community attribute to its peer group.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[~HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test advertise-community

```