peer advertise-large-community (BGP-VPN instance IPv4 address family view) (group)
==================================================================================

peer advertise-large-community (BGP-VPN instance IPv4 address family view) (group)

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
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Large-Community attribute to its BGP peer or peer group, run the **peer advertise-large-community** command. If the Large-Community attribute is advertised to a peer group, all the peer members in the group inherit this configuration. This simplifies the application of route-policies and facilitates route maintenance and management.

**Prerequisites**

A route-policy has been used to define the large-community attribute.


Example
-------

# Enable a device to advertise the Large-Community attribute to a BGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] group test
[*HUAWEI-bgp-vpna] peer test advertise-large-community

```