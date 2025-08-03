reset bgp vpn-target
====================

reset bgp vpn-target

Function
--------



The **reset bgp vpn-target** command resets BGP connections related to the VPN-Target address family.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset bgp vpn-target all**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset bgp vpn-target** { **external** | **internal** | *as-number* | *ipv4-address* | *ipv6-address* | **group** *group-name* }

For CE6885-LL (low latency mode):

**reset bgp vpn-target** { **external** | **internal** | *as-number* | *ipv4-address* | **group** *group-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **external** | Reset all EBGP connections. | - |
| **internal** | Resets all IBGP connections. | - |
| *as-number* | Specifies a 2-byte AS number (number<1-65535>) or a 4-byte AS number (number<1-65535>.number<0-65535>). | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |
| *ipv4-address* | Resets the BGP connection with a specified peer. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **group** *group-name* | Resets BGP connections with the specified peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **all** | Reset all BGP connections. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **reset bgp** command is used to make new BGP configurations take effect.If a BGP routing policy is configured on the device that does not support Route-Refresh, the **reset bgp** command can be used to make the new routing policy to take effect.


Example
-------

# Softly resets the BGP connections related to VPN-Target.
```
<HUAWEI> reset bgp vpn-target all

```