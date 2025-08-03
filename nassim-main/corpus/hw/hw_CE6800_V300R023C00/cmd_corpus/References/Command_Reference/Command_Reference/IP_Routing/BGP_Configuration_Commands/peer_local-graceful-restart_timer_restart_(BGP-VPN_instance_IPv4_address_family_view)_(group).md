peer local-graceful-restart timer restart (BGP-VPN instance IPv4 address family view) (group)
=============================================================================================

peer local-graceful-restart timer restart (BGP-VPN instance IPv4 address family view) (group)

Function
--------



The **peer local-graceful-restart timer restart** command sets the maximum duration for a device to wait for the BGP peer relationship with each peer in a specified group to be reestablished. After this command is run, the device will not advertise the maximum duration to any peer in the specified group.

The **undo peer local-graceful-restart timer restart** command deletes the configured duration.



By default, a device waits for the BGP peer relationship with each peer in a specified group to be reestablished for a maximum of 150s.


Format
------

**peer** *group-name* **local-graceful-restart** **timer** **restart** *restart-time*

**undo peer** *group-name* **local-graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *restart-time* | Specifies the maximum duration for a device to wait for the GR recovery of each peer in a specified group. | The value is an integer ranging from 3 to 3600, in seconds. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the local device supports GR but the specified peer does not support GR, you can run this command to set the maximum waiting time for the local device to wait for the re-establishment of the BGP peer relationship.After the **peer local-graceful-restart timer restart** command is run, if the local end finds that the peer group is Down, the BGP session enters the GR process. The local end must establish a connection with the peer group within the configured maximum waiting time. Otherwise, the local end selects the optimal route from the existing routes.


Example
-------

# Set the maximum duration to 250s for a device to wait for the peer relationship with each peer in a specified group to be reestablished.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] group aa
[*HUAWEI-bgp-vpn1] peer aa local-graceful-restart timer restart 250

```