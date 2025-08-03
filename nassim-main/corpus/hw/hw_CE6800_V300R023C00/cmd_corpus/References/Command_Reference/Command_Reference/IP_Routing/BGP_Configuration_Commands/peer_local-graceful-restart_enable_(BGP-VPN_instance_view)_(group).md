peer local-graceful-restart enable (BGP-VPN instance view) (group)
==================================================================

peer local-graceful-restart enable (BGP-VPN instance view) (group)

Function
--------



The **peer local-graceful-restart enable** command enables local GR for each peer in a specified group on a device. After this command is run, the device will not advertise the GR capability to any peer in the specified group.

The **undo peer local-graceful-restart enable** command disables local GR for each peer in a specified group on a device.



By default, local GR is not enabled for any peer in a specified group on a device.


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

BGP-VPN instance view,BGP multi-instance VPN instance session view


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
[*HUAWEI-vpn-instance-vpn1] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group aa
[*HUAWEI-bgp-instance-vpn1] peer aa local-graceful-restart enable

```