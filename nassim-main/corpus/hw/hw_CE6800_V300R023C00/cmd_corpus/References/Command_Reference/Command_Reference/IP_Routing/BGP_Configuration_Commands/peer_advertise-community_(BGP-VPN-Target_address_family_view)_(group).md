peer advertise-community (BGP-VPN-Target address family view) (group)
=====================================================================

peer advertise-community (BGP-VPN-Target address family view) (group)

Function
--------



The **peer advertise-community** command configures a device to advertise a community attribute to its peer group.

The **undo peer advertise-community** command cancels the existing configuration.



By default, a device advertises no community attribute to its peer group.


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

BGP-VPN-target address family view


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
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable
[*HUAWEI-bgp-af-vpn-target] peer test advertise-community

```