peer preferred-value (BGP-VPN-Target address family view) (group)
=================================================================

peer preferred-value (BGP-VPN-Target address family view) (group)

Function
--------



The **peer preferred-value** command sets a preferred value for the peer group.

The **undo peer preferred-value** command deletes the preferred value set for the peer group.



By default, the preferred value of the routes learned from other BGP peer groups is 0.


Format
------

**peer** *group-name* **preferred-value** *preferredvalue*

**undo peer** *group-name* **preferred-value**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *preferredvalue* | Specifies the preferred value of the routes that a BGP device learns from its peer. | The value is an integer ranging from 0 to 65535. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After a preferred value is configured for a peer group, all the routes learned from the peer group have the preferred value. If multiple routes with the same prefix are available, the route with the largest preferred value is preferred.



**Prerequisites**



A BGP peer group must be configured before the preferred value is assigned to the peer group. If you run this command for a peer group that does not exist, the system displays a message indicating that the peer group does not exist.



**Configuration Impact**



If a preferred value is set for the routes that a BGP device learns from a peer group, all members of the peer group inherit the configuration.




Example
-------

# Set the preferred value of the routes received from a specified peer group to 50.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable
[*HUAWEI-bgp-af-vpn-target] peer test preferred-value 50

```