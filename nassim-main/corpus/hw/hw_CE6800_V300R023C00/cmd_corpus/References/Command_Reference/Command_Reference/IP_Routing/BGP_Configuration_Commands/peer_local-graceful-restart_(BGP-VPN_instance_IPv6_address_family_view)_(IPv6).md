peer local-graceful-restart (BGP-VPN instance IPv6 address family view) (IPv6)
==============================================================================

peer local-graceful-restart (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer local-graceful-restart enable** command enables local GR for a specified peer on a device. After this command is run, the device will not advertise the GR capability to the specified peer.

The **peer local-graceful-restart disable** command disables local GR for a specified peer on a device.



By default, local GR is not enabled for a peer specified on a device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **local-graceful-restart** **disable**

**peer** *ipv6-address* **local-graceful-restart** **enable**

**undo peer** *ipv6-address* **local-graceful-restart** **disable**

**undo peer** *ipv6-address* **local-graceful-restart** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


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
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpn1] peer 2001:DB8:1::1 local-graceful-restart enable

```