peer public-as-only (BGP-VPN-Target address family view)
========================================================

peer public-as-only (BGP-VPN-Target address family view)

Function
--------



The **peer public-as-only** command configures the AS-Path attribute in a BGP Update message not to carry the private AS number. Only the public AS number is contained in the update messages.

The **undo peer public-as-only** command allows the AS-Path attribute in a BGP Update message to carry the private AS number.



By default, the AS-Path attribute in a BGP Update message is allowed to carry private AS numbers.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **public-as-only**

**undo peer** { *ipv4-address* | *ipv6-address* } **public-as-only**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **public-as-only**

**undo peer** *ipv4-address* **public-as-only**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, AS numbers range from 1 to 4294967295, including the public, private, and reserved AS numbers. If the **private-4-byte-as enable** command is not run, private AS numbers range from 64512 to 65534. AS number 65535 is reserved for special use. After the **private-4-byte-as enable** command is run, the private AS numbers range from 64512 to 65534 and from 4200000000-4294967294 to 65535 or 4294967295, which are reserved for special use.Public AS numbers can be used over the Internet, whereas private AS numbers cannot be advertised to the Internet. If private AS numbers are advertised to the Internet, routing loops may occur. Therefore, private AS numbers are used only within a routing domain.This command can be used to process the private and reserved AS numbers in the AS\_Path attribute of BGP routes as required. The processing of the reserved AS numbers is the same as that of the private AS numbers. After this command is configured, if the AS path attribute contains only private AS numbers, BGP deletes the private AS numbers and then advertises these update routes.

**Configuration Impact**

If the **peer public-as-only** command is run for a peer group, the peers of the peer group inherit the configuration.


Example
-------

# Configure a device to remove all private AS numbers from the AS\_Path attribute when sending a BGP Update message to its peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.2.2.2 as-number 200
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 public-as-only

```