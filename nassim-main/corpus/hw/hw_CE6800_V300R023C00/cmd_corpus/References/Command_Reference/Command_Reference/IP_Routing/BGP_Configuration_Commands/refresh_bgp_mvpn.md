refresh bgp mvpn
================

refresh bgp mvpn

Function
--------



The **refresh bgp mvpn** command softly resets connections in the BGP-MVPN address family.




Format
------

**refresh bgp mvpn** { **all** | *ipv4-address* | **group** *group-name* | **external** | **internal** } { **import** | **export** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Softly resets all the BGP IPv4 connections. | - |
| *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| **group** *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **external** | Softly resets EBGP connections. | - |
| **internal** | Performs a soft reset on IBGP connections. | - |
| **import** | Triggers an inbound soft reset. | - |
| **export** | Triggers an inbound soft reset. | - |
| **mvpn** | Softly resets the BGP connections related to Multicast Virtual Private Network (MVPN). | - |



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

# Softly resets the BGP connections related to multicast virtual private network (MVPN).
```
<HUAWEI> refresh bgp mvpn all export

```