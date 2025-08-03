ip route-static frr vpn-instance
================================

ip route-static frr vpn-instance

Function
--------



The **ip route-static frr vpn-instance** command enables fast reroute (FRR) for IPv4 static routes in a VPN instance.

The **undo ip route-static frr vpn-instance** command disables FRR for IPv4 static routes in a VPN instance.



By default, FRR is disabled for an IPv4 static route.


Format
------

**ip route-static frr vpn-instance** *vpn-instance-name*

**undo ip route-static frr vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect IPv4 static routes, configure FRR for IPv4 static routes using the ip route-static frr command.If the name of a VPN instance is specified, FRR is enabled for the static route of the VPN instance.

**Prerequisites**

A VPN instance has been configured if you want to configure FRR for the VPN.

**Configuration Impact**

Enabling or disabling FRR takes effect on all the static routes in the VPN instance.


Example
-------

# Enable FRR for static routes in a VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static frr vpn-instance v1

```