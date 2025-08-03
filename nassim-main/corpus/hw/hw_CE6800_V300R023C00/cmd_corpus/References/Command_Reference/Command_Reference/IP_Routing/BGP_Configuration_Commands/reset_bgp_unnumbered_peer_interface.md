reset bgp unnumbered peer interface
===================================

reset bgp unnumbered peer interface

Function
--------



The **reset bgp unnumbered peer interface** command resets a specified unnumbered BGP peer connection.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset bgp unnumbered peer interface** { *interface-name* | *IfType* *IFNum* }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset bgp ipv6 unnumbered peer interface** { *interface-name* | *IfType* *IFNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | - |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **ipv6** | Indicates the IPv6 unicast address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **reset bgp unnumbered peer interface** command is used to make new BGP configurations take effect.If a BGP routing policy is configured on the device that does not support Route-Refresh, the **reset bgp unnumbered peer interface** command can be used to make the new routing policy to take effect.

**Configuration Impact**

This command resets all TCP connections established between BGP peers and therefore results in the re-establishment of the BGP peer relationships. Exercise caution when running this command.


Example
-------

# Reset unnumbered-interface peer connections.
```
<HUAWEI> reset bgp unnumbered peer interface 100GE 1/0/8

```