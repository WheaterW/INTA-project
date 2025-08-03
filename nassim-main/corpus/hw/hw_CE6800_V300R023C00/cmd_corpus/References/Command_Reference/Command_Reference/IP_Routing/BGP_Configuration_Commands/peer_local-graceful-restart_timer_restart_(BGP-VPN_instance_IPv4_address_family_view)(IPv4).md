peer local-graceful-restart timer restart (BGP-VPN instance IPv4 address family view)(IPv4)
===========================================================================================

peer local-graceful-restart timer restart (BGP-VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer local-graceful-restart timer restart** command sets the maximum duration for a device to wait for the BGP peer relationship with a specified peer to be reestablished. After this command is run, the device will not advertise the maximum duration to the specified peer.

The **undo peer local-graceful-restart timer restart** command deletes the configured duration.



By default, a device waits for the peer relationship with a peer to be reestablished for a maximum of 150 seconds.


Format
------

**peer** *ipv4-address* **local-graceful-restart** **timer** **restart** *restart-time*

**undo peer** *ipv4-address* **local-graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *restart-time* | Specifies the maximum time for the local end to wait for GR recovery of the peer. | The value is an integer ranging from 3 to 3600, in seconds. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the local device supports GR but the specified peer does not support GR, you can run this command to set the maximum waiting time for the local device to wait for the re-establishment of the BGP peer relationship.After the **peer local-graceful-restart timer restart** command is run, if the local end finds that the peer is Down, the BGP session enters the GR process. The local end must establish a connection with the peer within the configured maximum waiting time. Otherwise, the local end selects the optimal route from the existing routes.


Example
-------

# Set the maximum duration to 250 seconds for a device to wait for the peer relationship with a specified peer to be reestablished.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp-vpn1] peer 10.1.1.2 local-graceful-restart timer restart 250

```