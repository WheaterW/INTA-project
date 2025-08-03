peer local-graceful-restart timer wait-for-rib (BGP-VPN instance view) (group)
==============================================================================

peer local-graceful-restart timer wait-for-rib (BGP-VPN instance view) (group)

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
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *wfrtime* | Specifies the maximum duration for a BGP restarter to wait for the End-of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To set the maximum duration for a device to wait for the End-of-RIB flag from each peer in a group, run the **peer local-graceful-restart timer wait-for-rib** command on the device. After a BGP session between the device and a peer in the group is reestablished, if the device does not receive the End-of-RIB flag within the specified duration, the involved BGP session on the device exits from the GR process and the device selects the optimal route among reachable routes.


Example
-------

# Set the maximum duration for a device to wait for the End-of-RIB flag from each peer in a specified group to 100s.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group aa
[*HUAWEI-bgp-instance-vpn1] peer aa local-graceful-restart timer wait-for-rib 100

```