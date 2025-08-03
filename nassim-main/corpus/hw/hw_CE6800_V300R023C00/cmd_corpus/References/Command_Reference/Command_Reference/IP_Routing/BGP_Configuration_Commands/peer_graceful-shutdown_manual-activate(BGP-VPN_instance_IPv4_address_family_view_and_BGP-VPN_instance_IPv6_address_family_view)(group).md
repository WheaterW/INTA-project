peer graceful-shutdown manual-activate(BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)(group)
==================================================================================================================================

peer graceful-shutdown manual-activate(BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)(group)

Function
--------



The **peer graceful-shutdown manual-activate** command activates the g-shut feature of a peer group.

The **undo peer graceful-shutdown manual-activate** command restores the default configuration.



By default, the g-shut feature of a peer group is not activated.


Format
------

**peer** *groupName* **graceful-shutdown** **manual-activate**

**undo peer** *groupName* **graceful-shutdown** **manual-activate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv4 address family view,BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To activate the g-shut feature for a peer group, run this command.


Example
-------

# Activate the g-shut feature for a peer group in the BGP-VPN instance IPv4 address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] group aa
[*HUAWEI-bgp-vpna] peer aa graceful-shutdown manual-activate

```