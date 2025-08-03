peer graceful-shutdown(BGP-VPN instance view)(group)
====================================================

peer graceful-shutdown(BGP-VPN instance view)(group)

Function
--------



The **peer graceful-shutdown** command enables the g-shut feature for a peer group.

The **undo peer graceful-shutdown** command restores the default configuration.



By default, the g-shut feature of a peer group is not enabled.


Format
------

**peer** *groupName* **graceful-shutdown** [ **local-preference** *local-preference-value* | **as-prepend** *as-prepend-value* ]

**undo peer** *groupName* **graceful-shutdown** [ **local-preference** *local-preference-value* | **as-prepend** *as-prepend-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **local-preference** *local-preference-value* | Specifies the local-preference value of the routes to be advertised to the peers in a peer group. Setting the value to 0 is recommended. If there are alternative routes, you can reduce the local preference of the routes advertised to IBGP peers to affect route selection. | The value is an integer that ranges from 0 to 4294967295. |
| **as-prepend** *as-prepend-value* | Specifies the number of ASs to be added to the AS\_Path of the route advertised to the peers in the peer group. If there are alternative routes, the length of the AS\_Path is increased to affect the route selection. | The value is an integer ranging from 1 to 6. |



Views
-----

BGP-VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To enable the g-shut feature for a peer group, run this command. You can specify multiple attribute values as required.




Example
-------

# Enable the g-shut feature for a peer group in the BGP-VPN instance view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-instance-vpna] group aa
[*HUAWEI-bgp-instance-vpna] peer aa graceful-shutdown local-preference 1

```