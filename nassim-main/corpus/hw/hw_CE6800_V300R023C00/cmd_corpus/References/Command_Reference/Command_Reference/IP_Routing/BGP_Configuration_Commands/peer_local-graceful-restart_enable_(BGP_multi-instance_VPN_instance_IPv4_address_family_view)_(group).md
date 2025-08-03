peer local-graceful-restart enable (BGP multi-instance VPN instance IPv4 address family view) (group)
=====================================================================================================

peer local-graceful-restart enable (BGP multi-instance VPN instance IPv4 address family view) (group)

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
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



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
[*HUAWEI] bgp 100 instance a
[~HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-instance-a-vpn1] group aa
[*HUAWEI-bgp-instance-a-vpn1] peer aa local-graceful-restart enable

```