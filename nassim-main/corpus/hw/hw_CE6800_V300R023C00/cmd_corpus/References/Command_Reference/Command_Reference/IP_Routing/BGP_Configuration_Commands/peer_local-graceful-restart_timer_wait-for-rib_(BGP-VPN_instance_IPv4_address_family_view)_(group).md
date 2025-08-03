peer local-graceful-restart timer wait-for-rib (BGP-VPN instance IPv4 address family view) (group)
==================================================================================================

peer local-graceful-restart timer wait-for-rib (BGP-VPN instance IPv4 address family view) (group)

Function
--------



The **peer local-graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from each peer in a specified group.

The **undo peer local-graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from each peer in a specified group for a maximum of 600s.


Format
------

**peer** *group-name* **local-graceful-restart** **timer** **wait-for-rib** *wfrtime*

**undo peer** *group-name* **local-graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| *wfrtime* | Specifies the maximum duration for a BGP restarter to wait for the End-of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To set the maximum duration for a device to wait for the End-of-RIB flag from each peer in a group, run the peer local-graceful-restart timer wait-for-rib command on the device. After a BGP session between the device and a peer in the group is reestablished, if the device does not receive the End-of-RIB flag within the specified duration, the involved BGP session on the device exits from the GR process and the device selects the optimal route among reachable routes.


Example
-------

# Set the maximum duration for a device to wait for the End-of-RIB flag from each peer in a specified group to 100s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] group aa
[*HUAWEI-bgp-vpn1] peer aa local-graceful-restart timer wait-for-rib 100

```