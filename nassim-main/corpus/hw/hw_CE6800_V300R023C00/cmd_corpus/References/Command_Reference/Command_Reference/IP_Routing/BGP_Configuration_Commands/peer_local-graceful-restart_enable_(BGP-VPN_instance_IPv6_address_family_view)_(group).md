peer local-graceful-restart enable (BGP-VPN instance IPv6 address family view) (group)
======================================================================================

peer local-graceful-restart enable (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer local-graceful-restart enable** command enables local GR for each peer in a specified group on a device. After this command is run, the device will not advertise the GR capability to any peer in the specified group.

The **undo peer local-graceful-restart enable** command disables local GR for each peer in a specified group on a device.



By default, local GR is not enabled for any peer in a specified group on a device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **local-graceful-restart** **enable**

**undo peer** *group-name* **local-graceful-restart** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable local GR for each peer in a specified group on a device, run the **peer local-graceful-restart enable** command on the device. This configuration ensures that the device does not delete the routes received from the peers in the group and related forwarding entries before the GR time elapses, thereby preventing traffic interruption.


Example
-------

# Enable local GR for each peer in a specified group on a device.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group aa
[*HUAWEI-bgp-6-vpn1] peer aa local-graceful-restart enable

```