peer local-graceful-restart (BGP multi-instance VPN instance IPv4 address family view)
======================================================================================

peer local-graceful-restart (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **peer local-graceful-restart enable** command enables local GR for a specified peer on a device. After this command is run, the device will not advertise the GR capability to the specified peer.

The **peer local-graceful-restart disable** command disables local GR for a specified peer on a device.



By default, local GR is not enabled for a peer specified on a device.


Format
------

**peer** *ipv4-address* **local-graceful-restart** **disable**

**peer** *ipv4-address* **local-graceful-restart** **enable**

**undo peer** *ipv4-address* **local-graceful-restart** **disable**

**undo peer** *ipv4-address* **local-graceful-restart** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a device supports GR but a BGP peer specified on the device does not support GR, you can run the peer local-graceful-restart enable command on the device to enable local GR for the peer. This configuration ensures that the device does not delete the routes received from the peer and related forwarding entries before the GR time elapses, thereby preventing traffic interruption.



**Precautions**



If a peer specified on a device does not support GR, you are advised to enable local GR for the peer.




Example
-------

# Enable local GR for a specified peer on a device.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100 instance a
[~HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-instance-a-vpn1] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp-instance-a-vpn1] peer 10.1.1.2 local-graceful-restart enable

```