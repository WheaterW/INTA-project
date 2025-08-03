refresh bgp
===========

refresh bgp

Function
--------



The **refresh bgp** command manually performs a soft reset on BGP connections.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**refresh bgp** { **all** | *ipv4-address* | **external** | **internal** | **group** *group-name* | *ipv6-address* } { **export** | **import** }

**refresh bgp vpn-instance** *vpn-instance-name* **ipv4-family** { **all** | *ipv4-address* | **external** | **internal** | **group** *group-name* } { **export** | **import** }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**refresh bgp** [ **instance** *bgpName* ] **vpn-instance** *vpn-instance-name* **ipv6-family** { **all** | *ipv6-address* | **external** | **internal** | **group** *group-name* } { **export** | **import** }

**refresh bgp vpn-instance** *vpn-instance-name* **ipv6-family** *ipv4-address* { **export** | **import** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Softly resets all the BGP IPv4 connections. | - |
| *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| **external** | Softly resets EBGP connections. | - |
| **internal** | Performs a soft reset on IBGP connections. | - |
| **group** *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **export** | Triggers an inbound soft reset. | - |
| **import** | Triggers an inbound soft reset. | - |
| *ipv6-address* | Specifies the IPv6 address of a BGP peer. | The value is in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-instance-name* | Softly resets the connection of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot be \_public\_. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **ipv6-family** | Indicates the IPv6 address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ipv4-family** | Indicates the IPv4 address family. | - |
| **instance** *bgpName* | Displays BGP routes of a specified BGP multi-instance.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



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

# Perform a soft reset on all BGP connections in the inbound direction to make new configurations take effect.
```
<HUAWEI> refresh bgp all import

```