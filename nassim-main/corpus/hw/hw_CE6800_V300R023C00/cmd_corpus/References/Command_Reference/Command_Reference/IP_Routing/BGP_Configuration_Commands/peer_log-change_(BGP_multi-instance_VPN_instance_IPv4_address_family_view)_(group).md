peer log-change (BGP multi-instance VPN instance IPv4 address family view) (group)
==================================================================================

peer log-change (BGP multi-instance VPN instance IPv4 address family view) (group)

Function
--------



The **peer log-change** command enables a BGP device to log the session status and events of a specified group.

The **undo peer log-change** command cancels the configuration.



By default, a BGP device is enabled to log the session status and events of a specified peer group.


Format
------

**peer** *group-name* **log-change**

**undo peer** *group-name* **log-change**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **peer log-change** command can be used to enable a device to log the session status and events of a specified peer group, facilitating service management.




Example
-------

# Configure a BGP device to log the session status and events of a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] group test
[*HUAWEI-bgp-instance-a-vpna] peer test log-change

```