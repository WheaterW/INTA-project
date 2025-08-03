refresh bgp ipv6
================

refresh bgp ipv6

Function
--------



The **refresh bgp ipv6** command softly resets connections in the BGP-IPv6 unicast address family.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**refresh bgp ipv6** { *ipv6-address* | **group** *group-name* } { **export** | **import** }

**refresh bgp ipv6** { **all** | *ipv4-address* | **external** | **internal** } { **export** | **import** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a BGP peer. | The value is in the format of X:X:X:X:X:X:X:X. |
| **group** *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **export** | Triggers an inbound soft reset. | - |
| **import** | Triggers an inbound soft reset. | - |
| **ipv6** | Softly resets BGP4+ connections. | - |
| **all** | Softly resets all the BGP IPv4 connections. | - |
| *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| **external** | Softly resets EBGP connections. | - |
| **internal** | Performs a soft reset on IBGP connections. | - |



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

# Softly resets BGP4+ connections.
```
<HUAWEI> refresh bgp ipv6 2001:DB8:1::1 export

```