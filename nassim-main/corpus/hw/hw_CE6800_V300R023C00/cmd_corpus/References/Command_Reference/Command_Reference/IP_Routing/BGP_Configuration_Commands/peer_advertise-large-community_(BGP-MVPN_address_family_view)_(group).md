peer advertise-large-community (BGP-MVPN address family view) (group)
=====================================================================

peer advertise-large-community (BGP-MVPN address family view) (group)

Function
--------



The **peer advertise-large-community** command enables a device to advertise the Large-Community attribute to a peer group.

The **undo peer advertise-large-community** command cancels the configuration.



By default, a device does not advertise the Large-Community attribute to its BGP peer group.


Format
------

**peer** *group-name* **advertise-large-community**

**undo peer** *group-name* **advertise-large-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Large-Community attribute to its BGP peer, run the **peer advertise-large-community** command. If the Large-Community attribute is advertised to a peer, all the peer members in the group inherit this configuration. This simplifies the application of route-policies and facilitates route maintenance and management.

**Prerequisites**

A route-policy has been used to define the large-community attribute.


Example
-------

# Enable a device to advertise the Large-Community attribute to a BGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix 1 permit 10.1.1.0 24
[*HUAWEI] route-policy RP permit node 10
[*HUAWEI-route-policy] if-match ip-prefix 1
[*HUAWEI-route-policy] apply large-community 35551:100:65552 additive
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer test enable
[*HUAWEI-bgp-af-mvpn] peer test advertise-large-community

```