peer advertise-large-community (BGP-VPN-Target address family view) (group)
===========================================================================

peer advertise-large-community (BGP-VPN-Target address family view) (group)

Function
--------



The **peer advertise-large-community** command enables a device to advertise the Large-Community attribute to a peer group.

The **undo peer advertise-large-community** command cancels the configuration.



By default, a device does not advertise the Large-Community attribute to any peer group.


Format
------

**peer** *group-name* **advertise-large-community**

**undo peer** *group-name* **advertise-large-community**


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



You can run the **peer advertise-large-community** command to determine whether to advertise the Large-Community attribute to a peer group. If the Large-Community attribute is advertised to a peer group, all the peers in the peer group inherit the Large-Community attribute. This simplifies the application of routing policies and facilitates route maintenance and management.



**Prerequisites**



Specific Large-Community values have been defined in a route-policy.




Example
-------

# Enable a device to advertise the Large-Community attribute to a BGP peer group.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable
[*HUAWEI-bgp-af-vpn-target] peer test advertise-large-community

```