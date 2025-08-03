refresh bgp vpn-instance ipv4-family
====================================

refresh bgp vpn-instance ipv4-family

Function
--------



The **refresh bgp vpn-instance ipv4-family** command softly resets connections in the BGP-VPN instance IPv4 address family.




Format
------

**refresh bgp** [ **instance** *instance-name* ] **vpn-instance** *vpn-instance-name* **ipv4-family** { **all** | *ipv4-address* | **external** | **internal** | **group** *group-name* } { **export** | **import** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Softly resets the connection of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **ipv4-family** | Indicates the IPv4 address family. | - |
| **all** | Softly resets all the BGP IPv4 connections. | - |
| *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| **external** | Softly resets EBGP connections. | - |
| **internal** | Performs a soft reset on IBGP connections. | - |
| **group** *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **export** | Triggers an inbound soft reset. | - |
| **import** | Triggers an inbound soft reset. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the peer of a device supports route-refresh, you can run this command on the device to softly reset the BGP connection with the peer. BGP soft resetting can be used to refresh the BGP routing table and apply new routing policies, without tearing down any BGP connection.



**Prerequisites**



Configuring BGP soft resetting requires that the peers support the route-refresh capability.



**Precautions**



Assume that a device supports route-refresh and is configured with the **peer keep-all-routes** command. After the **refresh bgp** command is run on the device, the device does not refresh its routing table.




Example
-------

# Softly resets the connection of a specified VPN instance enabled with an IPv4 address family.
```
<HUAWEI> refresh bgp vpn-instance vpna ipv4-family all export

```