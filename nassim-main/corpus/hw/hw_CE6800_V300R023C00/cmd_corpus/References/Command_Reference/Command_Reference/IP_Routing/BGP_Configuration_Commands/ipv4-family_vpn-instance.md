ipv4-family vpn-instance
========================

ipv4-family vpn-instance

Function
--------



The **ipv4-family vpn-instance** command enables the BGP-VPN instance address family and displays the address family view.

The **undo ipv4-family vpn-instance** command deletes the configurations in the BGP-VPN instance address family.



By default, the BGP-VPN instance address family is disabled.


Format
------

**ipv4-family vpn-instance** *vpn-instance-name*

**undo ipv4-family vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Associates a specified VPN instance with the BGP-IPv4 address family. You can enter the BGP-VPN instance address family view using the parameter. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before performing BGP configurations in a BGP-VPN instance address family, you need to run the **ipv4-family vpn-instance** command in the BGP view to enable the BGP-VPN instance address family and enter the address family view. The configuration in this view takes effect for the IPv4 unicast routes and peers in the specified VPN instance.

**Precautions**

After the YANG management mode is enabled for a BGP VPN instance using the **bgp yang-mode enable** command, a VPN instance must have been created before you run the **ipv4-family vpn-instance** command.If the YANG management mode is disabled for a BGP VPN instance, running the **ipv4-family vpn-instance** command does not depend on the creation of the VPN instance.


Example
-------

# Enter the BGP-VPN instance IPv4 address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 both
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1]

```