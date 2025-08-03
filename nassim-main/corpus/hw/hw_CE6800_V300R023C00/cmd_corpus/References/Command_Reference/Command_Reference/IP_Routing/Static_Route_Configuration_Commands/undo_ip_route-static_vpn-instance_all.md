undo ip route-static vpn-instance all
=====================================

undo ip route-static vpn-instance all

Function
--------



The **undo ip route-static vpn-instance all** command deletes all the configured IPv4 static route from a VPN instance.



By default, no IPv4 static routes are configured for a VPN instance.


Format
------

**undo ip route-static vpn-instance** *vpn-source-name* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-source-name* | Specifies the name of a source VPN instance. Each VPN instance has its own routing table. The configured static route is added to the routing table of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **undo ip route-static vpn-instance all** command deletes all the configured IPv4 static route from a VPN instance.


Example
-------

# Deletes all static routes from a VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] undo ip route-static vpn-instance vpn1 all

```