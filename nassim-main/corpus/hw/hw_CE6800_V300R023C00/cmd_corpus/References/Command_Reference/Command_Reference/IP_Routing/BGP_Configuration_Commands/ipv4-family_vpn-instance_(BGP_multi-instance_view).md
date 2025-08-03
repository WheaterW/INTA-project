ipv4-family vpn-instance (BGP multi-instance view)
==================================================

ipv4-family vpn-instance (BGP multi-instance view)

Function
--------



The **ipv4-family vpn-instance** command enables BGP multi-instance VPN instance IPv4 address family and displays the BGP multi-instance VPN instance IPv4 address family view.

The **undo ipv4-family vpn-instance** command deletes all configurations in the BGP multi-instance VPN instance IPv4 address family view.



By default, the BGP multi-instance VPN instance IPv4 address family is disabled.


Format
------

**ipv4-family vpn-instance** *vpn-instance-name*

**undo ipv4-family vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Associates a specified VPN instance with the IPv4 address family. This parameter displays the BGP multi-instance VPN instance IPv4 address family view. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Before performing configurations in the BGP multi-instance VPN instance IPv4 address family view, run the **ipv4-family vpn-instance** command in the BGP view to enable the BGP multi-instance VPN instance IPv4 address family and enter the address family view.



**Precautions**



If you attempt to configure the IPv4 VPN address family view in the BGP multi-instance view and MVPN services have been configured for the VPN instance, the configuration fails.




Example
-------

# Enter the BGP multi-instance VPN instance IPv4 address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] vpn-target 100:1 both
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1

```