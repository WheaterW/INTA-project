peer public-as-only limited (BGP-VPN-Target address family view)(IPv4)
======================================================================

peer public-as-only limited (BGP-VPN-Target address family view)(IPv4)

Function
--------



The **peer public-as-only limited** command configures the AS-Path attribute in a BGP Update message to private AS numbers from the leftmost one to delete the local or a public AS number except the private AS number of a specified peer.

The **undo peer public-as-only limited** command restores the default setting.



By default, the AS-Path attribute in a BGP Update message is allowed to carry private AS numbers.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **public-as-only** **limited** [ **replace** ] [ **include-peer-as** ]

**undo peer** { *ipv4-address* | *ipv6-address* } **public-as-only** **limited** [ **replace** ] [ **include-peer-as** ]

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **public-as-only** **limited** [ **replace** ] [ **include-peer-as** ]

**undo peer** *ipv4-address* **public-as-only** **limited** [ **replace** ] [ **include-peer-as** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **limited** | Deletes private AS numbers from the leftmost one to the local or a public AS number except the private AS number of a specified peer. | - |
| **replace** | Replaces private AS numbers in an AS\_Path list with a local AS number:  If both force and replace are specified, private AS numbers in an AS\_Path list, except the AS number of a specified peer or peer group, are replaced with the local AS number.  If both limited and replace are specified, private AS numbers starting from the leftmost one in an AS\_Path list, except the local or private AS number of a specified peer or peer group, are replaced with the local AS number. | - |
| **include-peer-as** | Deletes AS numbers:  If both limited and include-peer-as are specified, the AS numbers starting from the leftmost one in an AS\_Path list, except the local and public AS numbers, are deleted.  If limited, replace, and include-peer-as are specified, private AS numbers starting from the leftmost one in an AS\_Path list, except the local or private AS numbers, are replaced with the local AS number. | - |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, AS numbers range from 1 to 4294967295, including the public, private, and reserved AS numbers. If the **private-4-byte-as enable** command is not run, private AS numbers range from 64512 to 65534, and the AS number 65535 is reserved for special use. If the **private-4-byte-as enable** command is run, private AS numbers range from 64512 to 65534 and from 4200000000 to 4294967294, and the AS numbers 65535 and 4294967295 are reserved for special use.Public AS numbers can be used over the Internet, whereas private AS numbers cannot be advertised to the Internet. If private AS numbers are advertised to the Internet, routing loops may occur. Therefore, private AS numbers are used only within a routing domain.This command enables BGP to process the private and reserved AS numbers in the AS\_Path attribute of BGP routes as required. Reserved AS numbers are processed the same as private AS numbers. The following uses private AS numbers as an example to illustrate the processing modes:If the **peer public-as-only** command is run without any optional parameter specified and the AS\_Path attribute of BGP routes contains only private AS numbers, BGP deletes these private AS numbers before advertising the routes. BGP does not delete private AS numbers in either of the following scenarios if the **peer public-as-only** command is run, without any parameter following public-as-only specified:â¢ The AS\_Path attribute of a route carries the AS number of the remote peer. In this case, deleting private AS numbers may lead to a routing loop.â¢ The AS\_Path attribute carries both public and private AS numbers, which indicates that the route has passed through the public network. In this case, deleting private AS numbers may lead to a traffic forwarding error.Parameters that are used to delete or replace private AS numbers are described as follows:â¢ limited: deletes private AS numbers from the leftmost one to the local or a public AS number except the private AS number of a specified peer group.â¢ limited replace: replaces private AS numbers from the leftmost one to the local or a public AS number in the AS\_Path attribute with the local AS number except the private AS number of a specified peer group.â¢ limited include-peer-as: deletes private AS numbers from the leftmost one to the local or a public AS number. This parameter ensures that all private AS numbers of the local network are deleted.â¢ limited replace include-peer-as: replaces private AS numbers from the leftmost one to the local or a public AS number in the AS\_Path attribute with the local AS number.Select one of the preceding parameters based on the network topology to prevent routing loops or forwarding errors.

**Configuration Impact**

If the **peer public-as-only** command is run for a peer group, the peers of the peer group inherit the configuration.


Example
-------

# Enable a device to delete private AS numbers from the AS\_Path attribute, starting from the leftmost one and stopping at the local or a public AS number (except the private AS number of a specified peer), when the device sends BGP Update messages to the peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.2.2.2 as-number 200
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 public-as-only limited

```