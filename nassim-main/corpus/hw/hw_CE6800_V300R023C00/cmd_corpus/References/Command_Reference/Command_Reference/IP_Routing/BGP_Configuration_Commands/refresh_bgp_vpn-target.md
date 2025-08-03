refresh bgp vpn-target
======================

refresh bgp vpn-target

Function
--------



The **refresh bgp vpn-target** command softly resets connections in the BGP-VPN-Target address family.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**refresh bgp vpn-target** { **all** | *ipv4-address* | *ipv6-address* | **group** *group-name* | **external** | **internal** } { **import** | **export** }

For CE6885-LL (low latency mode):

**refresh bgp vpn-target** { **all** | *ipv6-address* | **group** *group-name* | **external** | **internal** } { **import** | **export** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Softly resets all the BGP IPv4 connections. | - |
| *ipv4-address* | Specifies the IPv4 address of a BGP peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **group** *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **external** | Softly resets EBGP connections. | - |
| **internal** | Performs a soft reset on IBGP connections. | - |
| **import** | Triggers an inbound soft reset. | - |
| **export** | Triggers an outbound soft reset. | - |
| **vpn-target** | Softly resets the BGP connections related to VPN-Target. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the peer of a device supports route-refresh, you can run this command on the device to softly reset the BGP connection with the peer. BGP soft resetting can be used to refresh the BGP routing table and apply new routing policies, without tearing down any BGP connection.


Example
-------

# Softly resets the BGP connections related to VPN-Target.
```
<HUAWEI> refresh bgp vpn-target all import

```